# 📧 EmailTriageEnv — OpenEnv Environment

An RL environment where an AI agent triages customer support emails.

## Environment Description

Agents must read incoming emails and perform real customer support tasks:
classify urgency, route to the right team, and draft professional replies.

## Tasks

| Task     | Difficulty | Description                                       |
| -------- | ---------- | ------------------------------------------------- |
| classify | Easy       | Label email as urgent / normal / spam             |
| route    | Medium     | Classify + assign to technical/billing/sales/none |
| respond  | Hard       | Classify + route + write a professional reply     |

## Action Space

```json
{
  "label": "urgent|normal|spam",
  "department": "technical|billing|sales|none",
  "reply": "string"
}
```

## Observation Space

```json
{
  "email_id": "str",
  "subject": "str",
  "body": "str",
  "sender": "str",
  "task": "str",
  "step": "int"
}
```

## Reward

- Scores range from 0.0 to 1.0 per email
- Partial credit awarded for partially correct actions

## Setup

```bash
pip install -r requirements.txt
python inference.py
```

## Baseline Scores

| Task     | Score |
| -------- | ----- |
| classify | ~0.85 |
| route    | ~0.70 |
| respond  | ~0.55 |
