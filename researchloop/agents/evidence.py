from researchloop.models.research import Evidence


class EvidenceAgent:
    async def run(self, research_questions: list[str]) -> list[Evidence]:
        raise NotImplementedError("Connect evidence search/extraction to Model Studio.")
