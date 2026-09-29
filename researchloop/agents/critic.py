from researchloop.models.experiment import CriticResult, ExperimentSpec
from researchloop.models.research import Hypothesis


class CriticAgent:
    async def run(
        self, hypothesis: Hypothesis, experiment: ExperimentSpec, observation: dict
    ) -> CriticResult:
        raise NotImplementedError("Evaluate results adversarially with Qwen.")
