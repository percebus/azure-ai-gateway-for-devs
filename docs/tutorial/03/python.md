# Smoke test w/ python

Same as we did in previous modules, we'll connect to the deployment model @ foundry. But this time we will go through API Management (APIM) instead of directly connecting to foundry.

## APIM

1. APIM > APIs > Subscriptions
1. Locate "Built-in all-access subscription"
1. Click on the `...` on the right
1. Click "Show/hide keys"
1. Copy the key somewhere. We will use it in the next step.

> [!WARNING]
> All-access subscription enables access **to every API in this API Management instance** and should only be used by authorized users. Never use it for routine API access or embed the all-access key in client apps.

> [!NOTE]
> Remember those `token-quota` policies by `@(context.Subscription.Id)`? It is this same key that is being used to track the token consumption for the subscription.

For this tutorial, Subscription Id is more akin to a Kafka consumer Id.

## python

1. Go to `python/`
1. Copy `.env.example` to `.env` if you haven't already done so.
1. Update the `.env` file with your APIM endpoint and API key.

- MCP: We will access the public MS Learn directly for now
- openai: We will access the OpenAI API via APIM, instead of directly

```
# openai via APIM
AZURE_OPENAI__ENDPOINT="https://ai-gw-{stack-id}-eastus-apim.azure-api.net/foundry-ptu-openai/openai/deployments/FIXME/chat/completions?api-version=FIXME"
AZURE_OPENAI__API_KEY="{Subscription Primary key}"
AZURE_OPENAI__DEPLOYMENT="gpt-4.1-mini-global-standard-latest"
```

> [!IMPORTANT]
> Yes, the deployment name appears in **both** `ENDPOINT` and `DEPLOYMENT`. The Agent Framework SDK requires the full URL path _and_ the deployment name separately. Replace both `FIXME` placeholders in the URL with the actual deployment name and API version (e.g. `2025-01-01-preview`).

4. Run the `my_agent` app: `python src/my_agent`

```
User: What tools are available to you?
Agent: I have access to the following tools:

1. microsoft_docs_search: This tool allows me to search official Microsoft/Azure documentation to find relevant and trustworthy content for your queries. It returns up to 10 high-quality content chunks from Microsoft Learn and other official sources.

2. microsoft_code_sample_search: This tool helps me search for code snippets and examples in official Microsoft Learn documentation. It's useful for providing practical implementation examples and best practices relating to Microsoft/Azure products and services.

3. microsoft_docs_fetch: This tool lets me fetch and convert a Microsoft Learn documentation webpage to markdown format. It retrieves the latest complete content of Microsoft documentation webpages, useful for detailed procedures, tutorials, troubleshooting sections, and comprehensive guides.

I can use these tools to provide accurate and detailed information from official Microsoft sources. If you have any specific questions or need information, just let me know!
```

Play w/ the following permutations:

1. `API_KEY`: Change from"Primary key" to "Secondary key"
1. `DEPLOYMENT`: Change from `-latest` to `-stable`
1. `api-version`: `2025-01-01-preview`, `2025-03-01-preview`, deployment model's version, etc.

## Next

[Back to Module](./README.md)
