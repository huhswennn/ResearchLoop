from fastapi import FastAPI
from pydantic import BaseModel

from researchloop.core.state import ResearchStage

app = FastAPI(title="ResearchLoop API", version="0.1.0")


class ProjectCreate(BaseModel):
    title: str
    goal: str
    mode: str = "discover"


@app.get("/health")
async def health() -> dict:
    return {"status": "ok", "service": "researchloop-api"}


@app.post("/projects")
async def create_project(payload: ProjectCreate) -> dict:
    return {
        "title": payload.title,
        "goal": payload.goal,
        "mode": payload.mode,
        "current_stage": ResearchStage.PLANNING,
    }
