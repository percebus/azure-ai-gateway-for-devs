"""Container w/ injectable dependencies."""

from logging import Logger

from agent_framework import ChatClientProtocol
from agent_framework.azure import AzureOpenAIChatClient
from azure.core.credentials import TokenCredential

# from azure.cosmos.aio import ContainerProxy, CosmosClient, DatabaseProxy # TODO
from azure.identity import AzureCliCredential, DefaultAzureCredential
from dotenv import load_dotenv
from lagom import Container, Singleton
from lagom.interfaces import ReadableContainer

from my_agent.ai.agents.mcp import McpChatAgent
from my_agent.ai.tools.mcp.apim import ApimMCPStreamableHttpTool
from my_agent.config.configuration import Configuration
from my_agent.config.logs import LoggingConfig
from my_agent.config.os_environ.azure_openai import AzureOpenAISettings
from my_agent.config.os_environ.settings import Settings


def create_settings(ctr: ReadableContainer):
    load_dotenv()
    return Settings()  # pyright: ignore[reportCallIssue]


def create_azure_openai_client(ctr: ReadableContainer):
    """Create AzureOpenAIChatClient."""
    azure_openai_settings = ctr[AzureOpenAISettings]

    # fmt: off
    kwargs = {
        "endpoint": str(azure_openai_settings.endpoint),
        "deployment_name": azure_openai_settings.deployment,
    }
    # fmt: on

    api_key = azure_openai_settings.api_key
    if api_key:
        kwargs["api_key"] = api_key
    else:
        kwargs["credential"] = ctr[TokenCredential]  # pyright: ignore[reportArgumentType]

    return AzureOpenAIChatClient(**kwargs)  # pyright: ignore[reportArgumentType]


container = Container()

### Configuration ###########################################################

load_dotenv()
container[Settings] = create_settings
container[AzureOpenAISettings] = container[Settings].azure_openai

container[LoggingConfig] = Singleton(LoggingConfig)
container[Logger] = lambda c: c[LoggingConfig].logger


# Credential providers
container[AzureCliCredential] = AzureCliCredential
container[DefaultAzureCredential] = DefaultAzureCredential

# Abstract the credential provider
# Choose either or
# container[AzureCliCredential] = AzureCliCredential
container[TokenCredential] = lambda c: c[DefaultAzureCredential]


# fmt: off
container[Configuration] = lambda c: Configuration(
    logging=c[LoggingConfig],
    settings=c[Settings],
    credential=c[TokenCredential],
)
# fmt: on


### Azure Foundry #######################################################

container[AzureOpenAIChatClient] = create_azure_openai_client
container[ChatClientProtocol] = lambda c: c[AzureOpenAIChatClient]


### Agent Framework #######################################################################

# fmt: off
container[ApimMCPStreamableHttpTool] = lambda c: ApimMCPStreamableHttpTool(
    configuration=c[Configuration]
)
# fmt: on

# fmt: off
container[McpChatAgent] = lambda c: McpChatAgent(
    chat_client=c[ChatClientProtocol],
    mcp_tool=c[ApimMCPStreamableHttpTool],
)
# fmt: on
