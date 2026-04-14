""".env os.environ ENVIRONMENT VARIABLES settings module."""

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from my_agent.config.os_environ.apim_mcp import ApimMcpSettings
from my_agent.config.os_environ.azure_openai import AzureOpenAISettings


class Settings(BaseSettings):
    """Base class for settings."""

    model_config = SettingsConfigDict(
        extra="ignore",
        case_sensitive=False,
        env_prefix="",
        env_nested_delimiter="__",
    )

    debug: bool = Field(default=False)
    dry_run: bool = Field(default=True)
    environment: str = Field(min_length=2)

    azure_openai: AzureOpenAISettings = Field()

    apim_mcp: ApimMcpSettings = Field()
