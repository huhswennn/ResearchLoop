from researchloop.core.state import ResearchStage
from researchloop.models.research import ResearchProject


class ResearchOrchestrator:
    """Program controls lifecycle; agents decide scientific content."""

    async def advance(self, project: ResearchProject) -> ResearchProject:
        transitions = {
            ResearchStage.PLANNING: ResearchStage.EVIDENCE_COLLECTION,
            ResearchStage.EVIDENCE_COLLECTION: ResearchStage.HYPOTHESIS_GENERATION,
            ResearchStage.HYPOTHESIS_GENERATION: ResearchStage.EXPERIMENT_DESIGN,
            ResearchStage.EXPERIMENT_DESIGN: ResearchStage.AWAITING_APPROVAL,
            ResearchStage.EXECUTING: ResearchStage.ANALYZING,
            ResearchStage.ANALYZING: ResearchStage.DECIDING_NEXT_STEP,
        }
        next_stage = transitions.get(project.current_stage)
        if next_stage is not None:
            project.current_stage = next_stage
        return project
