"""MS Learn ChatAgent."""

from dataclasses import dataclass, field

from agent_framework import ChatAgent, MCPStreamableHTTPTool
from agent_framework._clients import ChatClientProtocol


# SRC: https://github.com/microsoft/agent-framework/blob/python-1.0.0b251007/python/samples/getting_started/tools/ai_tool_with_approval.py
@dataclass
class McpChatAgent(ChatAgent):
    """MSLearnChatAgent class."""

    chat_client: ChatClientProtocol = field()

    mcp_tool: MCPStreamableHTTPTool = field()

    instructions: str = field(default=("You are a helpful assistant. Use the MCP tool."))

    def __post_init__(self) -> None:
        """Post-Initialize."""
        return super().__init__(
            chat_client=self.chat_client,
            name=self.__class__.__name__,
            instructions=self.instructions,
            tools=[self.mcp_tool],
        )
