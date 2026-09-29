from researchloop.models.research import Evidence, Hypothesis


class HypothesisAgent:
    async def run(self, evidence: list[Evidence]) -> list[Hypothesis]:
        raise NotImplementedError("Generate falsifiable hypotheses with Qwen.")
