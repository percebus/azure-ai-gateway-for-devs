# Smoke testing with python

Back to the `.env` file

```
# openai via APIM
AZURE_OPENAI__ENDPOINT="https://ai-gw-{stack-id}-eastus-apim.azure-api.net/foundry-openai-lb/openai/deployments/gpt-4.1-mini-global-standard-latest/chat/completions?api-version=2025-01-01-preview"
AZURE_OPENAI__DEPLOYMENT="gpt-4.1-mini-global-standard-latest"

# Subscriptions
AZURE_OPENAI__API_KEY="{Smoke Test Agent @ ai-open}" # ai-open
# AZURE_OPENAI__API_KEY="{Smoke Test Agent @ ai-relaxed}" # ai-relaxed
# AZURE_OPENAI__API_KEY="{Smoke Test Agent @ ai-strict}" # ai-strict
```

## REMINDER

Again....

> [!IMPORTANT]
> This is the make-it-or-break-it test for the content safety policy.

If ANYTHING is missing, you will ALWAYS get the following.-

```json
{
  "statusCode": 403,
  "message": "Request failed content safety check."
}
```

Which is SUPER misleading (I would expect a 500 error of sorts).

### Checklist

So far we've accomplished the following:

- [x] Add APIM-to-Foundries _"Cognitive Services"_ **Managed Identity** Role Assignments
- [x] Connect APIM backends to both CognitiveServices APIs in their respective Foundries.
- [x] Make sure it uses System Managed Identity against `https://cognitiveservices.azure.com/`
- [x] Create a Load Balancer for the Cognitive Services backends
- [x] Created reusable Policy fragments
- [x] Created new Products that use those policies

Now, let's test it!

## ai-open

1. Run it against `ai-open`
   1. Make sure everything is still working as expected

```
2026-04-16 10:53:19,723 - agent - DEBUG - Setting up 'Ocp-Apim-Subscription-Key'
User: What tools are available to you?
Agent: I have access to the following tools:

1. microsoft_docs_search: To search official Microsoft/Azure documentation for relevant content based on queries.
2. microsoft_code_sample_search: To find code snippets and examples in official Microsoft documentation for specific Microsoft/Azure related coding tasks.
3. microsoft_docs_fetch: To fetch and convert a Microsoft Learn documentation webpage to markdown format for complete detailed information.

These tools help me provide accurate, trustworthy, and comprehensive answers related to Microsoft and Azure technologies.
```

## ai-relaxed

1. Then, comment out the `ai-open` key, and use the `ai-relaxed` subscription key to test the relaxed content safety settings.
   1. It should still work as expected

```
2026-04-16 10:37:03,399 - agent - DEBUG - Setting up 'Ocp-Apim-Subscription-Key'
2026-04-16 10:37:03,401 - agent - DEBUG - Setting up 'Ocp-Apim-Subscription-Key'
User: What tools are available to you?
Agent: I have access to the following tools within the functions namespace:

1. microsoft_docs_search: Search official Microsoft/Azure documentation to find relevant and trustworthy content related to a user's query. It returns high-quality content chunks from Microsoft Learn and other official sources.

2. microsoft_code_sample_search: Search for code snippets and examples in official Microsoft Learn documentation. It helps find practical implementation examples and best practices for Microsoft/Azure products and services in multiple programming languages.

3. microsoft_docs_fetch: Fetch and convert a Microsoft Learn documentation webpage to markdown format. This tool retrieves the complete and latest content of Microsoft documentation webpages including step-by-step procedures, troubleshooting sections, prerequisites, detailed explanations, and more.

Additionally, I can use a multi-tool function to run multiple of these tools in parallel if needed.

How can I assist you further using these tools?
```

## ai-strict

For w/e reason, a simple prompt like "What tools are available to you?" triggers the strict content safety policy, resulting in a 403 error.

However, we'll use this to our advantage to prove that the strict content safety policy is indeed being enforced correctly.

1. Then, comment out that key, and use the `ai-strict` subscription key to test the strict content safety settings.
   1. It should return a `403` error due to the strict content safety policy

> [!CAUTION]
> agent_framework.exceptions.ServiceResponseException:
> <class 'agent_framework.azure.\_chat_client.AzureOpenAIChatClient'> service failed to complete the prompt: Error code: 403 -
> `{'statusCode': 403, 'message': 'Request failed content safety chec
