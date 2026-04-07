"""
inference.py — Baseline inference script for EmailTriageEnv
Mandatory format: [START], [STEP], [END] stdout logs
"""

import json
import os
from openai import OpenAI
from env import EmailTriageEnv

API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")
API_KEY = os.getenv("HF_TOKEN") or os.getenv("API_KEY", "your-token-here")
BENCHMARK = "email-triage-env"

client = OpenAI(base_url=API_BASE_URL, api_key=API_KEY)


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
    # Strip markdown fences if present
    raw = raw.replace("```json", "").replace("```", "").strip()
    return json.loads(raw)


def run_task(task_name: str):
    env = EmailTriageEnv(task_name=task_name)
    obs = env.reset()
    done = False
    step = 0
    rewards = []

    print(f"[START] task={task_name} env={BENCHMARK} model={MODEL_NAME}")

    while not done:
        try:
            action = ask_llm(task_name, obs)
        except Exception as ex:
            action = {"label": "normal", "department": "none", "reply": ""}
            print(f"[STEP] step={step+1} action=fallback reward=0.00 done=false error={str(ex)[:80]}")
            obs, reward, done, info = env.step(action)
            rewards.append(reward)
            step += 1
            continue

        obs, reward, done, info = env.step(action)
        rewards.append(reward)
        step += 1

        action_str = f"label={action.get('label','?')},dept={action.get('department','?')}"
        done_str = "true" if done else "false"
        print(f"[STEP] step={step} action={action_str} reward={reward:.2f} done={done_str} error=null")

    score = round(sum(rewards) / len(rewards), 2) if rewards else 0.0
    success = score >= 0.5
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(f"[END] success={str(success).lower()} steps={step} score={score:.2f} rewards={rewards_str}")
    return score


if __name__ == "__main__":
    for task in ["classify", "route", "respond"]:
        run_task(task)
        print()