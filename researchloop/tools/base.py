from abc import ABC, abstractmethod

from researchloop.models.experiment import ExperimentSpec


class ResearchTool(ABC):
    @abstractmethod
    async def validate(self, experiment: ExperimentSpec) -> None:
        ...

    @abstractmethod
    async def prepare(self, experiment: ExperimentSpec) -> None:
        ...

    @abstractmethod
    async def execute(self, experiment: ExperimentSpec) -> str:
        ...

    @abstractmethod
    async def collect(self, run_id: str) -> dict:
        ...
