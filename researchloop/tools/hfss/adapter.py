from researchloop.models.experiment import ExperimentSpec
from researchloop.tools.base import ResearchTool


class HFSSTool(ResearchTool):
    """Optional professional-tool adapter for later PyAEDT integration."""

    async def validate(self, experiment: ExperimentSpec) -> None:
        if experiment.executor != "hfss":
            raise ValueError("HFSSTool only accepts hfss experiments.")

    async def prepare(self, experiment: ExperimentSpec) -> None:
        return None

    async def execute(self, experiment: ExperimentSpec) -> str:
        raise NotImplementedError("PyAEDT integration is planned for a later milestone.")

    async def collect(self, run_id: str) -> dict:
        return {"run_id": run_id, "artifacts": []}
