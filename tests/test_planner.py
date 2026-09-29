import pytest

from researchloop.agents.planner import PlannerAgent
from researchloop.models.research import ResearchPlan


class FakeQwenClient:
    async def structured_response(self, instructions, input_text, schema):
        assert "research-planning" in instructions
        assert "Research goal:" in input_text
        return schema(
            research_questions=["What is the baseline?"],
            search_queries=["radio map sparse sampling baseline"],
            falsifiable_questions=["Does method A reduce RMSE?"],
            information_requirements=["Comparable datasets and metrics"],
        )


@pytest.mark.asyncio
async def test_planner_returns_structured_plan() -> None:
    planner = PlannerAgent(client=FakeQwenClient())
    result = await planner.run("Improve sparse radio-map reconstruction")

    assert isinstance(result, ResearchPlan)
    assert result.search_queries
    assert result.falsifiable_questions
