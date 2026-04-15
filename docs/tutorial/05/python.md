# Smoke testing with python

Now that we have configured the subscription key for the MCP server in our `.env` file, we can perform a smoke test using `python` to ensure that everything is working correctly.

```
# MCP via APIM
APIM_MCP__URL="https://ai-gw-{stack-id}-eastus-apim.azure-api.net/mcp-existing-mslearn/api/mcp"
APIM_MCP__SUBSCRIPTION_KEY="{your-subscription-key}"
```

And `python src/my_agent`

```
2026-04-14 15:34:03,355 - agent - DEBUG - Setting up 'Ocp-Apim-Subscription-Key'
2026-04-14 15:34:03,358 - agent - DEBUG - Setting up 'Ocp-Apim-Subscription-Key'
User: What tools are available to you?
Agent: I have access to the following tools:

1. microsoft_docs_search: Search official Microsoft/Azure documentation for relevant and trustworthy content.
2. microsoft_code_sample_search: Search for code snippets and examples in official Microsoft Learn documentation.
3. microsoft_docs_fetch: Fetch and convert a Microsoft Learn documentation webpage to markdown format, retrieving the latest complete content of Microsoft documentation webpages.

I can use these tools to provide you with accurate and detailed information about Microsoft and Azure technologies. How can I assist you today?
```

## Next

[Back to Module](./README.md)
