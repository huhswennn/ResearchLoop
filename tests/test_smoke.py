from researchloop.core.state import ResearchStage
from researchloop.models.research import ResearchProject


def test_project_starts_in_planning() -> None:
    project = ResearchProject(title="Demo", goal="Test a research loop")
    assert project.current_stage == ResearchStage.PLANNING
