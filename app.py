# app.py — FastAPI wrapper exposing OpenEnv interface
from fastapi import FastAPI
from pydantic import BaseModel
from env import EmailTriageEnv

app = FastAPI(title="EmailTriageEnv")

envs = {}

class ActionRequest(BaseModel):
    session_id: str
    label: str
    department: str = "none"
    reply: str = ""

@app.get("/")
def root():
    return {"name": "email-triage-env", "status": "running", "tasks": ["classify", "route", "respond"]}

@app.post("/reset")
def reset(task: str = "classify", session_id: str = "default"):
    env = EmailTriageEnv(task_name=task)
    obs = env.reset()
    envs[session_id] = env
    return {"observation": obs}

@app.post("/step")
def step(req: ActionRequest):
    env = envs.get(req.session_id)
    if not env:
        return {"error": "Session not found. Call /reset first."}
    action = {"label": req.label, "department": req.department, "reply": req.reply}
    obs, reward, done, info = env.step(action)
    return {"observation": obs, "reward": reward, "done": done, "info": info}

@app.get("/state")
def state(session_id: str = "default"):
    env = envs.get(session_id)
    if not env:
        return {"error": "Session not found."}
    return env.state()