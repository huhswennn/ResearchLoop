import os

from openai import AsyncOpenAI


class QwenClient:
    def __init__(self) -> None:
        self.model = os.getenv("QWEN_MODEL", "qwen-max")
        self.client = AsyncOpenAI(
            api_key=os.getenv("DASHSCOPE_API_KEY"),
            base_url=os.getenv(
                "DASHSCOPE_BASE_URL",
                "https://dashscope.aliyuncs.com/compatible-mode/v1",
            ),
        )

    async def response(self, instructions: str, input_text: str):
        return await self.client.responses.create(
            model=self.model,
            instructions=instructions,
            input=input_text,
        )
