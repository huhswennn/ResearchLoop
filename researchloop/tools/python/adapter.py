from researchloop.models.experiment import ExperimentSpec
from researchloop.tools.base import ResearchTool


class PythonTool(ResearchTool):
    async def validate(self, experiment: ExperimentSpec) -> None:
        if experiment.executor != "python":
            raise ValueError("PythonTool only accepts python experiments.")

    async def prepare(self, experiment: ExperimentSpec) -> None:
        return None

    async def execute(self, experiment: ExperimentSpec) -> str:
        raise NotImplementedError("Wire to Code Interpreter or isolated Docker runner.")

    async def collect(self, run_id: str) -> dict:
        return {"run_id": run_id, "artifacts": []}
