from researchloop.llm.qwen import QwenClient
from researchloop.models.research import ResearchPlan

PLANNER_INSTRUCTIONS = """
You are the research-planning component of ResearchLoop.
Do not answer the research question directly.
Decompose the goal into research questions, literature search queries,
information requirements, and falsifiable questions.
Avoid fabricating evidence or experimental results.
Keep the plan concrete enough for an evidence agent to execute.
""".strip()


class PlannerAgent:
    def __init__(self, client: QwenClient | None = None) -> None:
        self.client = client or QwenClient()

    async def run(self, goal: str) -> ResearchPlan:
        return await self.client.structured_response(
            PLANNER_INSTRUCTIONS,
            f"Research goal:\n{goal}",
            ResearchPlan,
        )
