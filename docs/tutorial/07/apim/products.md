# Azure API Management

## Checklist

So far we've accomplished the following:

- [x] Add APIM-to-Foundries _"Cognitive Services"_ **Managed Identity** Role Assignments
- [x] Connect APIM backends to both CognitiveServices APIs in their respective Foundries.
- [x] Make sure it uses System Managed Identity against `https://cognitiveservices.azure.com/`
- [x] Create a Load Balancer for the Cognitive Services backends
- [ ] Created reusable Policy fragments
- [ ] Created new Products that use those policies

## Policy fragments

Now that we've done basic testing, let's create a couple of reusable Policy fragments that we'll use from the Products.

We'll do so by creating a couple of Policy fragments

- A strict one
- And a lenient one

```xml
<fragment>
  <llm-content-safety
    backend-id="{backend or load balancer name}"
    shield-prompt="true" <<< Prompt injections protection
    enforce-on-completions="true" << Applies to responses
  >
      <!-- SRC: https://learn.microsoft.com/en-us/azure/api-management/llm-content-safety-policy -->
      <categories output-type="EightSeverityLevels">
          <category name="Hate" threshold="1" />
          <category name="SelfHarm" threshold="2" />
          <category name="Sexual" threshold="3" />
          <category name="Violence" threshold="4" />
      </categories>

      <!-- NOTE no blocklist here! -->
  </llm-content-safety>
</fragment>
```

> [!IMPORTANT]
> Note `EightSeverityLevels` is used to define the output type for the content safety categories.
> `7` is the most relaxed, and `0` is the most strict.

> [!NOTE]
> There is NO mention of Subscription in this policy. So this applies to all requests regardless of subscription.

### llm-content-safety_relaxed

1. APIM > APIs > Policy fragments

- **Name**: `llm-content-safety_relaxed`
- **XML policy fragment**:

```xml
<fragment>
  <llm-content-safety
    backend-id="foundry-cognitiveservices-lb"
    shield-prompt="true"
    enforce-on-completions="true"
  >
      <!-- SRC: https://learn.microsoft.com/en-us/azure/api-management/llm-content-safety-policy -->
      <categories output-type="EightSeverityLevels">
          <category name="Hate" threshold="7" />
          <category name="SelfHarm" threshold="7" />
          <category name="Sexual" threshold="7" />
          <category name="Violence" threshold="7" />
      </categories>
  </llm-content-safety>
</fragment>
```

### llm-content-safety_strict

```xml
<fragment>
  <llm-content-safety
    backend-id="foundry-cognitiveservices-lb"
    shield-prompt="true"
    enforce-on-completions="true"
  >
      <!-- SRC: https://learn.microsoft.com/en-us/azure/api-management/llm-content-safety-policy -->
      <categories output-type="EightSeverityLevels">
          <category name="Hate" threshold="0" />
          <category name="SelfHarm" threshold="0" />
          <category name="Sexual" threshold="0" />
          <category name="Violence" threshold="0" />
      </categories>
  </llm-content-safety>
</fragment>
```

## Products

We'll create the following products:

- `ai-relaxed`
- `ai-strict`

### ai-relaxed

#### Add

Follow the steps you did for `ai-open`

1. APIM > Products
1. [ + Add ]

- Display name: `ai-relaxed`
- Id: `ai-relaxed`
- Description: "AI access with relaxed content safety settings"
- [x] Published
- [x] Requires subscription
- APIs: Select all 3 `foundry-`

#### Policies

Add the `<include-fragment fragment-id="llm-content-safety_relaxed" />` to the inbound policies of the `ai-relaxed` product.

```xml
<!--
    - Policies are applied in the order they appear.
    - Position <base/> inside a section to inherit policies from the outer scope.
    - Comments within policies are not preserved.
 -->
<!-- Add policies as children to the <inbound>, <outbound>, <backend>, and <on-error> elements -->
<policies>
    <!-- Throttle, authorize, validate, cache, or transform the requests -->
    <inbound>
        <base />
        <include-fragment fragment-id="llm-content-safety_relaxed" />
    </inbound>

    <!-- ... -->
</policies>
```

#### Subscriptions

1. [ + Add subscribers ]
1. Select both: `{your username}` and `Smoke Test Agent`
1. Rename policies to `{foo} @ ai-relaxed`


### ai-strict

We'll follow the same steps as `ai-relaxed`, but use the `llm-content-safety_strict` policy fragment instead.

## Python

Go to the `.env` file and dump the newly created subscription keys

it should contain something like this:

```
# openai via APIM
AZURE_OPENAI__ENDPOINT="https://ai-gw-{stack-id}-eastus-apim.azure-api.net/foundry-openai-lb/openai/deployments/gpt-4.1-mini-global-standard-latest/chat/completions?api-version=2025-01-01-preview"
AZURE_OPENAI__DEPLOYMENT="gpt-4.1-mini-global-standard-latest"

# Subscriptions
AZURE_OPENAI__API_KEY="{Smoke Test Agent @ ai-open}" # ai-open
# AZURE_OPENAI__API_KEY="{Smoke Test Agent @ ai-relaxed}" # ai-relaxed
# AZURE_OPENAI__API_KEY="{Smoke Test Agent @ ai-strict}" # ai-strict
```

## Next

[Back to Module](../README.md)
