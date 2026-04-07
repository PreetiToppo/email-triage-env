# env.py — The main OpenEnv environment

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


class Action(BaseModel):
    label: str                  # urgent / normal / spam
    department: str = "none"   # technical / billing / sales / none
    reply: str = ""            # only used in respond task


class Reward(BaseModel):
    score: float
    feedback: str


class EmailTriageEnv:
    def __init__(self, task_name: str = "classify"):
        self.task = get_task(task_name)
        self.task_name = task_name
        self.emails = EMAILS.copy()
        self.current_email = None
        self.step_count = 0
        self.max_steps = len(self.emails)
        self.email_index = 0
        self.episode_rewards = []

    def reset(self) -> dict:
        self.email_index = 0
        self.step_count = 0
        self.episode_rewards = []
        random.shuffle(self.emails)
        self.current_email = self.emails[self.email_index]
        return self._make_observation().model_dump()

    def step(self, action: dict) -> tuple[dict, float, bool, dict]:
        if self.current_email is None:
            raise RuntimeError("Call reset() before step()")

        reward_score = self.task.grade(action, self.current_email)
        self.episode_rewards.append(reward_score)
        self.step_count += 1
        self.email_index += 1

        done = self.email_index >= len(self.emails)

        if not done:
            self.current_email = self.emails[self.email_index]
        
        obs = self._make_observation().model_dump()
        reward = Reward(
            score=reward_score,
            feedback="correct" if reward_score >= 0.8 else "partial" if reward_score > 0 else "incorrect"
        )

        info = {
            "email_id": self.current_email["id"] if not done else None,
            "episode_score": round(sum(self.episode_rewards) / len(self.episode_rewards), 2) if self.episode_rewards else 0.0
        }

        return obs, reward.score, done, info

    def state(self) -> dict:
        return {
            "task": self.task_name,
            "step": self.step_count,
            "max_steps": self.max_steps,
            "email_index": self.email_index,
            "episode_rewards": self.episode_rewards,
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
        )