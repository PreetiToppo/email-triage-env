# app.py — Production FastAPI wrapper with health endpoint
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from env import EmailTriageEnv
import time

app = FastAPI(
    title="EmailTriageEnv",
    description="OpenEnv RL environment for AI agent email triage",
    version="2.0.0"
)

envs = {}
START_TIME = time.time()


class ActionRequest(BaseModel):
    session_id: str = "default"
    label: str = "normal"
    department: str = "none"
    reply: str = ""
    escalate: str = "false"
    reason: str = ""


@app.get("/")
def root():
    return {
        "name": "email-triage-env",
        "version": "2.0.0",
        "status": "running",
        "tasks": ["classify", "route", "respond", "escalate"],
        "openenv": True,
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "uptime_seconds": round(time.time() - START_TIME, 1),
        "active_sessions": len(envs),
        "total_emails": 50,
    }


@app.post("/reset")
def reset(task: str = "classify", session_id: str = "default", max_emails: int = 10):
    if task not in ["classify", "route", "respond", "escalate"]:
        raise HTTPException(status_code=400, detail=f"Unknown task: {task}")
    env = EmailTriageEnv(task_name=task, max_emails=max_emails)
    obs = env.reset()
    envs[session_id] = env
    return {"observation": obs, "task": task, "session_id": session_id}


@app.post("/step")
def step(req: ActionRequest):
    env = envs.get(req.session_id)
    if not env:
        raise HTTPException(status_code=404, detail="Session not found. Call /reset first.")
    action = {
        "label": req.label,
        "department": req.department,
        "reply": req.reply,
        "escalate": req.escalate,
        "reason": req.reason,
    }
    obs, reward, done, info = env.step(action)
    return {"observation": obs, "reward": reward, "done": done, "info": info}


@app.get("/state")
def state(session_id: str = "default"):
    env = envs.get(session_id)
    if not env:
        raise HTTPException(status_code=404, detail="Session not found.")
    return env.state()


@app.get("/tasks")
def list_tasks():
    return {
        "tasks": [
            {"name": "classify", "difficulty": "easy", "description": "Classify email as urgent/normal/spam"},
            {"name": "route", "difficulty": "medium", "description": "Classify + route to correct department"},
            {"name": "respond", "difficulty": "hard", "description": "Classify + route + draft professional reply"},
            {"name": "escalate", "difficulty": "hard", "description": "Decide if email needs human escalation + reason"},
        ]
    }