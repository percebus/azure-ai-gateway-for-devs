"""Azure OpenAI Settings."""

from pydantic import BaseModel, Field

from my_agent.config.os_environ.typing import RightStrippedUrl


class AzureOpenAISettings(BaseModel):
    """AzureOpenAISettings class."""

    endpoint: RightStrippedUrl = Field()

    # NOTE: eventho we pass the deployment name via URL, we still need to specify it here.-
    #
    # "Azure OpenAI deployment name is required.
    #  Set via 'deployment_name' parameter or 'AZURE_OPENAI_CHAT_DEPLOYMENT_NAME' environment variable."
    deployment: str = Field()

    api_key: str | None = Field(default=None)
