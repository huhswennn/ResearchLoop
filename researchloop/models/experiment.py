from typing import Any, Literal
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class ExperimentSpec(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    hypothesis_id: UUID | None = None
    objective: str
    executor: str = "python"
    inputs: dict[str, Any] = Field(default_factory=dict)
    independent_variables: dict[str, Any] = Field(default_factory=dict)
    controlled_variables: dict[str, Any] = Field(default_factory=dict)
    metrics: list[str] = Field(default_factory=list)
    repetitions: int = 1
    success_criteria: list[str] = Field(default_factory=list)


class CriticResult(BaseModel):
    verdict: Literal[
        "supported", "partially_supported", "not_supported", "inconclusive"
    ]
    reasoning: str
    confounders: list[str] = Field(default_factory=list)
    alternative_explanations: list[str] = Field(default_factory=list)
    proposed_next_experiments: list[dict[str, Any]] = Field(default_factory=list)
