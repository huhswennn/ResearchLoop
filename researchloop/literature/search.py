class LiteratureSearch:
    """Provider-neutral literature search boundary."""

    async def search(self, queries: list[str]) -> list[dict]:
        raise NotImplementedError(
            "Connect this boundary to Model Studio web search/file search."
        )
