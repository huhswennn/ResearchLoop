from pydantic import BaseModel, Field


class ResearchPlan(BaseModel):
    research_questions: list[str] = Field(default_factory=list)
    search_queries: list[str] = Field(default_factory=list)
    falsifiable_questions: list[str] = Field(default_factory=list)


class PlannerAgent:
    async def run(self, goal: str) -> ResearchPlan:
        raise NotImplementedError("Connect PlannerAgent to Qwen structured output.")
