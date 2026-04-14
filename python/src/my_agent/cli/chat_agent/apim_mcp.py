"""MS Learn MCP ChatAgent example."""

import asyncio

from lagom import Container

from my_agent.ai.agents.mcp import McpChatAgent
from my_agent.ai.tools.mcp.apim import ApimMCPStreamableHttpTool


async def run_async(container: Container) -> None:
    """Run (async)."""
    chat_agent = container[McpChatAgent]
    mcp_tool = container[ApimMCPStreamableHttpTool]

    async with (
        mcp_tool,
        chat_agent,
    ):
        query = "What tools are available to you?"
        print(f"User: {query}")
        result = await chat_agent.run(query)
        print(f"Agent: {result.text}")


def main() -> None:
    from my_agent.dependency_injection.container import container  # noqa: PLC0415

    asyncio.run(run_async(container))


if __name__ == "__main__":
    main()
