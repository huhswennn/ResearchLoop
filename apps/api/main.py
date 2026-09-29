from uuid import UUID

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from researchloop.agents.planner import PlannerAgent
from researchloop.core.state import ProjectMode, ResearchStage
from researchloop.models.research import ResearchProject
from researchloop.storage.repository import InMemoryProjectRepository

app = FastAPI(title="ResearchLoop API", version="0.1.0")
repo = InMemoryProjectRepository()


class ProjectCreate(BaseModel):
    title: str
    goal: str
    mode: ProjectMode = ProjectMode.DISCOVER


@app.get("/health")
async def health() -> dict:
    return {"status": "ok", "service": "researchloop-api"}


@app.post("/projects", response_model=ResearchProject)
async def create_project(payload: ProjectCreate) -> ResearchProject:
    project = ResearchProject(**payload.model_dump())
    return await repo.save(project)


@app.get("/projects/{project_id}", response_model=ResearchProject)
async def get_project(project_id: UUID) -> ResearchProject:
    project = await repo.get(project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@app.post("/projects/{project_id}/plan", response_model=ResearchProject)
async def plan_project(project_id: UUID) -> ResearchProject:
    project = await repo.get(project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")

    planner = PlannerAgent()
    project.plan = await planner.run(project.goal)
    project.current_stage = ResearchStage.EVIDENCE_COLLECTION
    return await repo.save(project)
