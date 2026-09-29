import json
import os
from typing import TypeVar

from openai import AsyncOpenAI
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


class QwenClient:
    def __init__(self) -> None:
        self.model = os.getenv("QWEN_MODEL", "qwen-max")
        api_key = os.getenv("DASHSCOPE_API_KEY")
        if not api_key:
            raise RuntimeError("DASHSCOPE_API_KEY is not configured.")
        self.client = AsyncOpenAI(
            api_key=api_key,
            base_url=os.getenv(
                "DASHSCOPE_BASE_URL",
                "https://dashscope.aliyuncs.com/compatible-mode/v1",
            ),
        )

    async def structured_response(
        self, instructions: str, input_text: str, schema: type[T]
    ) -> T:
        schema_json = json.dumps(schema.model_json_schema(), ensure_ascii=False)
        response = await self.client.responses.create(
            model=self.model,
            instructions=(
                instructions
                + "\nReturn only JSON matching this schema:\n"
                + schema_json
            ),
            input=input_text,
        )
        if not response.output_text:
            raise RuntimeError("Qwen returned an empty response.")
        return schema.model_validate_json(response.output_text)
