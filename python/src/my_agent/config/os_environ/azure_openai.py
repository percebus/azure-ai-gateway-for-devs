"""Azure OpenAI Settings."""

from pydantic import BaseModel, Field

from my_agent.config.os_environ.typing import RightStrippedUrl


class AzureOpenAISettings(BaseModel):
    """AzureOpenAISettings class."""

    endpoint: RightStrippedUrl = Field()

    deployment: str = Field()

    api_key: str | None = Field(default=None)
