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

## ai-relaxed

1. Then, comment out the `ai-open` key, and use the `ai-relaxed` subscription key to test the relaxed content safety settings.
   1. It should still work as expected

## ai-strict

For w/e reason, a simple prompt like "What tools are available to you?" triggers the strict content safety policy, resulting in a 403 error.

However, we'll use this to our advantage to prove that the strict content safety policy is indeed being enforced correctly.

1. Then, comment out that key, and use the `ai-strict` subscription key to test the strict content safety settings.
   1. It should return a `403` error due to the strict content safety policy

> [!CAUTION]
> agent_framework.exceptions.ServiceResponseException:
> <class 'agent_framework.azure.\_chat_client.AzureOpenAIChatClient'> service failed to complete the prompt: Error code: 403 -
> `{'statusCode': 403, 'message': 'Request failed content safety check.'}`
