from typing import Any, Literal
from uuid import UUID, uuid4

from pydantic import BaseModel, Field

from researchloop.core.state import ProjectMode, ResearchStage


class ResearchProject(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str
    goal: str
    mode: ProjectMode = ProjectMode.DISCOVER
    current_stage: ResearchStage = ResearchStage.PLANNING


class Evidence(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    claim: str
    relation: Literal["supports", "contradicts", "qualifies"]
    source: str
    conditions: dict[str, Any] = Field(default_factory=dict)


class Hypothesis(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    statement: str
    rationale: str
    evidence_ids: list[UUID] = Field(default_factory=list)
    assumptions: list[str] = Field(default_factory=list)
    uncertainty: list[str] = Field(default_factory=list)
    falsification_condition: str
