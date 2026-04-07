"""
inference.py — Baseline inference script for EmailTriageEnv
"""
import json
import os
from openai import OpenAI
from env import EmailTriageEnv

API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")
HF_TOKEN = os.getenv("HF_TOKEN")

if HF_TOKEN is None:
    raise ValueError("HF_TOKEN environment variable is required")

client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)

BENCHMARK = "email-triage-env"


def ask_llm(task_name: str, obs: dict) -> dict:
    system_prompt = """You are an expert customer support manager.
You will receive an email and must respond in JSON only with these fields:
- label: one of "urgent", "normal", "spam"
- department: one of "technical", "billing", "sales", "none"
- reply: a professional reply (empty string if spam)
Respond ONLY with valid JSON. No explanation."""

    user_prompt = f"""Task: {task_name}
From: {obs['sender']}
Subject: {obs['subject']}
Body: {obs['body']}"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        max_tokens=300,
        temperature=0.0,
    )

    raw = response.choices[0].message.content.strip()
    raw = raw.replace("```json", "").replace("```", "").strip()
    return json.loads(raw)


def run_task(task_name: str):
    env = EmailTriageEnv(task_name=task_name)
    obs = env.reset()
    done = False
    step = 0
    rewards = []
    last_error = None

    print(f"[START] task={task_name} env={BENCHMARK} model={MODEL_NAME}")

    while not done:
        try:
            action = ask_llm(task_name, obs)
            last_error = None
        except Exception as ex:
            action = {"label": "normal", "department": "none", "reply": ""}
            last_error = str(ex)[:80]

        obs, reward, done, info = env.step(action)
        rewards.append(reward)
        step += 1

        action_str = f"label={action.get('label','?')},dept={action.get('department','?')}"
        done_str = "true" if done else "false"
        error_str = last_error if last_error else "null"
        print(f"[STEP] step={step} action={action_str} reward={reward:.2f} done={done_str} error={error_str}")

    success = (sum(rewards) / len(rewards)) >= 0.5 if rewards else False
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(f"[END] success={str(success).lower()} steps={step} rewards={rewards_str}")
    print()


if __name__ == "__main__":
    for task in ["classify", "route", "respond"]:
        run_task(task)