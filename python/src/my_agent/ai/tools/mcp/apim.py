"""MS Learn MCP Streamable Http Tool."""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from agent_framework import MCPStreamableHTTPTool

from my_agent.config.configuration import Configuration
from my_agent.constants import MILLISECONDS_PER_SECOND

if TYPE_CHECKING:
    from my_agent.config.os_environ.apim_mcp import ApimMcpSettings


@dataclass
class ApimMCPStreamableHttpTool(MCPStreamableHTTPTool):
    """MSLearnMCPStreamableHttpTool class."""

    configuration: Configuration = field()

    description: str = field(default="MCP tool description")

    headers: dict[str, str] = field(default_factory=lambda: {})

    url: str = field(init=False)

    # TODO add headers
    def __post_init__(self) -> None:
        """Post-Initialize."""

        mcp_settings: ApimMcpSettings = self.configuration.settings.apim_mcp
        self.url = str(mcp_settings.url)

        if mcp_settings.subscription_key:
            self.configuration.logging.logger.debug("Setting up 'Ocp-Apim-Subscription-Key'")
            self.headers["Ocp-Apim-Subscription-Key"] = mcp_settings.subscription_key

        return super().__init__(
            name=self.__class__.__name__,
            description=self.description,
            load_prompts=False,  # NOT supported by APIM
            url=self.url,
            headers=self.headers,
            timeout=60 * MILLISECONDS_PER_SECOND,
        )
