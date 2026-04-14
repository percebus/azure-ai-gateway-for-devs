"""Azure API Management MCP settings."""

from pydantic import BaseModel, Field

from my_agent.config.os_environ.typing import RightStrippedUrl


class ApimMcpSettings(BaseModel):
    """ApimMcpSettings class."""

    url: RightStrippedUrl = Field()

    subscription_key: str = Field(default="")  # FIXME
