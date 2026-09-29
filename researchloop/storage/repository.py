from uuid import UUID

from researchloop.models.research import ResearchProject


class InMemoryProjectRepository:
    def __init__(self) -> None:
        self._projects: dict[UUID, ResearchProject] = {}

    async def save(self, project: ResearchProject) -> ResearchProject:
        self._projects[project.id] = project
        return project

    async def get(self, project_id: UUID) -> ResearchProject | None:
        return self._projects.get(project_id)
