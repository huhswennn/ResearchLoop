from enum import Enum


class ResearchStage(str, Enum):
    PLANNING = "planning"
    EVIDENCE_COLLECTION = "evidence_collection"
    HYPOTHESIS_GENERATION = "hypothesis_generation"
    EXPERIMENT_DESIGN = "experiment_design"
    AWAITING_APPROVAL = "awaiting_approval"
    EXECUTING = "executing"
    ANALYZING = "analyzing"
    DECIDING_NEXT_STEP = "deciding_next_step"
    PAUSED = "paused"
    COMPLETED = "completed"


class ProjectMode(str, Enum):
    DISCOVER = "discover"
    REPRODUCE = "reproduce"
