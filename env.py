# env.py — Production-grade OpenEnv environment with penalties and history

import random
from typing import Any
from pydantic import BaseModel
from emails import EMAILS
from tasks import get_task


class Observation(BaseModel):
    email_id: str
    subject: str
    body: str
    sender: str
    task: str
    step: int
    total_emails: int


class Action(BaseModel):
    label: str = "normal"
    department: str = "none"
    reply: str = ""
    escalate: str = "false"
    reason: str = ""


class Reward(BaseModel):
    score: float
    feedback: str
    penalty: float = 0.0


class EmailTriageEnv:
    def __init__(self, task_name: str = "classify", max_emails: int = 10):
        self.task = get_task(task_name)
        self.task_name = task_name
        self.all_emails = EMAILS.copy()
        self.max_emails = min(max_emails, len(self.all_emails))
        self.emails = []
        self.current_email = None
        self.step_count = 0
        self.email_index = 0
        self.episode_rewards = []
        self.episode_history = []
        self.consecutive_wrong = 0

    def reset(self) -> dict:
        self.email_index = 0
        self.step_count = 0
        self.episode_rewards = []
        self.episode_history = []
        self.consecutive_wrong = 0
        random.shuffle(self.all_emails)
        self.emails = self.all_emails[:self.max_emails]
        self.current_email = self.emails[self.email_index]
        return self._make_observation().model_dump()

    def step(self, action: dict) -> tuple[dict, float, bool, dict]:
        if self.current_email is None:
            raise RuntimeError("Call reset() before step()")

        base_score = self.task.grade(action, self.current_email)

        # Penalty system
        penalty = 0.0

        # Penalty 1: repeated wrong answers (consecutive failures)
        if base_score < 0.3:
            self.consecutive_wrong += 1
            if self.consecutive_wrong >= 3:
                penalty += 0.1  # penalize persistent failure
        else:
            self.consecutive_wrong = 0

        # Penalty 2: missing required fields
        if not action.get("label"):
            penalty += 0.1
        if self.task_name in ("route", "respond") and not action.get("department"):
            penalty += 0.05

        # Penalty 3: responding to spam
        if self.current_email["label"] == "spam" and len(str(action.get("reply", ""))) > 50:
            penalty += 0.15

        final_score = round(max(0.0, min(1.0, base_score - penalty)), 2)

        self.episode_rewards.append(final_score)
        self.episode_history.append({
            "step": self.step_count + 1,
            "email_id": self.current_email["id"],
            "action": action,
            "score": final_score,
            "penalty": penalty,
        })
        self.step_count += 1
        self.email_index += 1

        done = self.email_index >= len(self.emails)

        if not done:
            self.current_email = self.emails[self.email_index]

        obs = self._make_observation().model_dump()
        avg = round(sum(self.episode_rewards) / len(self.episode_rewards), 2)

        feedback = "excellent" if final_score >= 0.9 else \
                   "good" if final_score >= 0.7 else \
                   "partial" if final_score >= 0.4 else "incorrect"

        info = {
            "email_id": self.current_email["id"] if not done else None,
            "episode_score": avg,
            "penalty_applied": penalty,
            "consecutive_wrong": self.consecutive_wrong,
            "feedback": feedback,
        }

        reward_obj = Reward(score=final_score, feedback=feedback, penalty=penalty)
        return obs, reward_obj.score, done, info

    def state(self) -> dict:
        return {
            "task": self.task_name,
            "step": self.step_count,
            "max_steps": len(self.emails),
            "email_index": self.email_index,
            "episode_rewards": self.episode_rewards,
            "episode_history": self.episode_history[-3:],  # last 3 for brevity
            "consecutive_wrong": self.consecutive_wrong,
            "current_avg_score": round(
                sum(self.episode_rewards) / len(self.episode_rewards), 2
            ) if self.episode_rewards else 0.0,
        }

    def _make_observation(self) -> Observation:
        e = self.current_email
        return Observation(
            email_id=e["id"],
            subject=e["subject"],
            body=e["body"],
            sender=e["sender"],
            task=self.task_name,
            step=self.step_count,
            total_emails=len(self.emails),
        )