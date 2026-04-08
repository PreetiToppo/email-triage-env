# tasks.py — 4 tasks with production-grade graders

from emails import EMAILS


def get_task(task_name: str):
    tasks = {
        "classify": ClassifyTask(),
        "route": RouteTask(),
        "respond": RespondTask(),
        "escalate": EscalateTask(),
    }
    if task_name not in tasks:
        raise ValueError(f"Unknown task: {task_name}. Choose from {list(tasks.keys())}")
    return tasks[task_name]


class ClassifyTask:
    """EASY: Classify email urgency as urgent / normal / spam"""
    name = "classify"
    description = "Classify each email as 'urgent', 'normal', or 'spam'."
    valid_labels = {"urgent", "normal", "spam"}

    def grade(self, action: dict, email: dict) -> float:
        predicted = str(action.get("label", "")).strip().lower()

        # Penalty: invalid label
        if predicted not in self.valid_labels:
            return 0.0

        if predicted == email["label"]:
            return 1.0

        # Partial credit: classifying urgent as normal (less bad than spam)
        if email["label"] == "urgent" and predicted == "normal":
            return 0.2

        # Penalty: classifying spam as urgent wastes human time
        if email["label"] == "spam" and predicted == "urgent":
            return 0.0

        return 0.0


class RouteTask:
    """MEDIUM: Classify urgency AND route to correct department"""
    name = "route"
    description = "Classify urgency and route to: technical, billing, sales, or none."
    valid_labels = {"urgent", "normal", "spam"}
    valid_departments = {"technical", "billing", "sales", "none"}

    def grade(self, action: dict, email: dict) -> float:
        predicted_label = str(action.get("label", "")).strip().lower()
        predicted_dept = str(action.get("department", "")).strip().lower()
        score = 0.0

        # Invalid inputs: penalize
        if predicted_label not in self.valid_labels:
            predicted_label = ""
        if predicted_dept not in self.valid_departments:
            predicted_dept = ""

        # Label score (50%)
        if predicted_label == email["label"]:
            score += 0.5
        elif email["label"] == "urgent" and predicted_label == "normal":
            score += 0.1  # small partial for near miss

        # Department score (50%)
        if predicted_dept == email["department"]:
            score += 0.5
        elif email["label"] == "spam" and predicted_dept == "none":
            score += 0.5  # spam always routes to none

        return round(min(score, 1.0), 2)


class RespondTask:
    """HARD: Classify + route + draft a quality professional reply"""
    name = "respond"
    description = "Classify, route, and draft a professional reply to the email."

    def grade(self, action: dict, email: dict) -> float:
        predicted_label = str(action.get("label", "")).strip().lower()
        predicted_dept = str(action.get("department", "")).strip().lower()
        reply = str(action.get("reply", "")).strip().lower()

        score = 0.0

        # 25% for correct label
        valid_labels = {"urgent", "normal", "spam"}
        if predicted_label in valid_labels and predicted_label == email["label"]:
            score += 0.25
        elif email["label"] == "urgent" and predicted_label == "normal":
            score += 0.05

        # 25% for correct department
        valid_depts = {"technical", "billing", "sales", "none"}
        if predicted_dept in valid_depts and predicted_dept == email["department"]:
            score += 0.25

        # 50% for reply quality
        if email["label"] == "spam":
            # Spam: agent should NOT write a reply (penalize long replies)
            if len(reply) == 0:
                score += 0.5
            elif len(reply) < 30:
                score += 0.3
            else:
                score += 0.0  # penalty for responding to spam
        else:
            # Non-spam: score reply quality
            reply_score = 0.0

            # Keyword matching (30% of reply score)
            keywords = email.get("ideal_reply_keywords", [])
            if keywords:
                matched = sum(1 for kw in keywords if kw in reply)
                reply_score += 0.3 * (matched / len(keywords))

            # Length check: too short = unhelpful, too long = ok (20% of reply score)
            if len(reply) > 100:
                reply_score += 0.2
            elif len(reply) > 50:
                reply_score += 0.1

            # Professionalism signals (20% of reply score)
            professional_signals = ["thank", "apolog", "help", "assist", "contact", "team", "resolv", "we will", "please"]
            prof_count = sum(1 for sig in professional_signals if sig in reply)
            reply_score += 0.2 * min(prof_count / 3, 1.0)

            # Urgency acknowledgment bonus (10% of reply score)
            if email["label"] == "urgent":
                urgency_words = ["immediately", "priorit", "urgent", "right away", "asap", "escalat"]
                if any(w in reply for w in urgency_words):
                    reply_score += 0.1

            # Penalty: very short reply for urgent email
            if email["label"] == "urgent" and len(reply) < 50:
                reply_score -= 0.2

            score += min(0.5, 0.5 * reply_score / 0.8)

        return round(min(max(score, 0.0), 1.0), 2)


class EscalateTask:
    """NOVEL/HARD: Agent decides if email needs human escalation + reason"""
    name = "escalate"
    description = (
        "Decide if each email requires human escalation. "
        "Return escalate=true/false and a one-line reason. "
        "Escalate when: multiple customers affected, legal/security risk, "
        "C-level sender, or repeat complaint. Do NOT escalate routine queries."
    )

    def grade(self, action: dict, email: dict) -> float:
        predicted_escalate = str(action.get("escalate", "false")).strip().lower()
        reason = str(action.get("reason", "")).strip()

        # Normalize to bool
        predicted = predicted_escalate in {"true", "yes", "1"}
        actual = email.get("needs_escalation", False)

        score = 0.0

        # 70% for correct escalation decision
        if predicted == actual:
            score += 0.7
        else:
            # False negative on escalation (missing real emergency) is worse
            if actual and not predicted:
                score += 0.0  # missing an escalation is a critical failure
            else:
                score += 0.2  # false alarm is less bad

        # 30% for quality of reason
        if len(reason) > 10:
            score += 0.15  # provided some reason
            reason_lower = reason.lower()
            good_reason_words = ["security", "legal", "multiple", "customer", "urgent",
                                  "critical", "breach", "data", "payment", "compli", "affect"]
            if any(w in reason_lower for w in good_reason_words):
                score += 0.15  # reason mentions relevant concept

        return round(min(score, 1.0), 2)