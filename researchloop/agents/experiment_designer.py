from researchloop.models.experiment import ExperimentSpec
from researchloop.models.research import Hypothesis


class ExperimentDesignerAgent:
    async def run(self, hypothesis: Hypothesis) -> ExperimentSpec:
        raise NotImplementedError("Translate scientific intent into ExperimentSpec.")
