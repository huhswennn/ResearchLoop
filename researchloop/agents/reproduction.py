class ReproductionAgent:
    async def extract_experiment(self, paper_text: str) -> dict:
        raise NotImplementedError(
            "Extract methods, parameters, provenance, and missing information."
        )
