# tasks.py — 3 tasks with graders (easy → medium → hard)

from emails import EMAILS


def get_task(task_name: str):
    tasks = {
        "classify": ClassifyTask(),
        "route": RouteTask(),
        "respond": RespondTask(),
    }
    if task_name not in tasks:
        raise ValueError(f"Unknown task: {task_name}. Choose from {list(tasks.keys())}")
    return tasks[task_name]


class ClassifyTask:
    """EASY: Agent must classify email urgency as urgent / normal / spam"""
    name = "classify"
    description = "Classify each email as 'urgent', 'normal', or 'spam'."
    valid_labels = {"urgent", "normal", "spam"}

    def grade(self, action: dict, email: dict) -> float:
        predicted = str(action.get("label", "")).strip().lower()
        if predicted not in self.valid_labels:
            return 0.0
        return 1.0 if predicted == email["label"] else 0.0


class RouteTask:
    """MEDIUM: Agent must classify urgency AND assign correct department"""
    name = "route"
    description = "Classify urgency AND route to: technical, billing, sales, or none."
    valid_labels = {"urgent", "normal", "spam"}
    valid_departments = {"technical", "billing", "sales", "none"}

    def grade(self, action: dict, email: dict) -> float:
        predicted_label = str(action.get("label", "")).strip().lower()
        predicted_dept = str(action.get("department", "")).strip().lower()
        score = 0.0
        if predicted_label == email["label"]:
            score += 0.5
        if predicted_dept == email["department"]:
            score += 0.5
        return score


class RespondTask:
    """HARD: Agent must classify + route + draft a quality reply"""
    name = "respond"
    description = "Classify, route, and draft a professional reply to the email."

    def grade(self, action: dict, email: dict) -> float:
        predicted_label = str(action.get("label", "")).strip().lower()
        predicted_dept = str(action.get("department", "")).strip().lower()
        reply = str(action.get("reply", "")).strip().lower()

        score = 0.0

        # 30% for correct label
        if predicted_label == email["label"]:
            score += 0.3

        # 30% for correct department
        if predicted_dept == email["department"]:
            score += 0.3

        # 40% for reply quality (keyword matching)
        if email["ideal_reply_keywords"]:
            matched = sum(1 for kw in email["ideal_reply_keywords"] if kw in reply)
            keyword_score = matched / len(email["ideal_reply_keywords"])
            score += 0.4 * keyword_score
        else:
            # spam: agent should NOT write a reply
            if len(reply) < 20:
                score += 0.4

        return round(min(score, 1.0), 2)