# Azure API Management

## Backends

### Backend endpoints

When we're done, it will look something like this

![Backends](../../../../assets/img/tutorial/eastus/apim/Backends/02.png)

#### foundry-ptu-cognitiveservices

##### Create new backend

1. APIM > APIs > Backends
1. [ + Create new backend ]

- **Name**: `foundry-ptu-cognitiveservices-endpoint`
- **Runtime URL**: `https://ai-gw-{stack-id}-eastus-foundry-ptu.cognitiveservices.azure.com/`
- **Authorization credentials**
  - **Managed Identity**
    - [x] Enable
    - **Resource ID**: `https://cognitiveservices.azure.com/`

> [!IMPORTANT]
> Managed Identity tells APIM that it will authenticate against foundry, via the `https://cognitiveservices.azure.com/` URL

##### Circuit breaker

We will add a Circuit breaker policy, but this time, for any error `400-599`

- **Rule name**: `AnyFailure`
- **Failure Conditions**:
  - **Failure count**: `3`
  - **Failure interval**:
    - **Minutes**:`1`
- **Custom Range**: `400-599`
- **Trip duration**:
  - **Minutes**: `5`

#### foundry-payg-cognitiveservices

Follow the same steps as above to create a new backend for

- **Name**: `foundry-payg-cognitiveservices`
- **Runtime URL**: `https://ai-gw-{stack-id}-eastus2-foundry-payg.cognitiveservices.azure.com/`

### Load balancer

- Name: `foundry-cognitiveservices-lb`
- Add backends to pool
  - `foundry-ptu-cognitiveservices-endpoint`
  - `foundry-payg-cognitiveservices-endpoint`
- Backend weight and priority:
  - [x] Send requests evenly

## Checklist

So far we've accomplished the following:

- [x] Add APIM-to-Foundries _"Cognitive Services"_ **Managed Identity** Role Assignments
- [x] Connect APIM backends to both CognitiveServices APIs in their respective Foundries.
- [x] Make sure it uses System Managed Identity against `https://cognitiveservices.azure.com/`
- [x] Create a Load Balancer for the Cognitive Services backends
- [ ] Created reusable Policy fragments
- [ ] Created new Products that use those policies

Now, let's test it!

## APIs

To test the `bananas` blocklist we created in previous steps, we'll put it directly on the `foundry-openai-lb`, as it is easier to test it in APIM using the APIs > Test feature.

### foundry-openai-lb

1. APIM > APIs > APIs
2. `foundry-openai-lb` > Design > Inbound processing

Add the following policy fragmment to the inbound policies of the `foundry-openai-lb` API.

```xml
<llm-content-safety
  backend-id="foundry-cognitiveservices-lb"
  shield-prompt="false"
  enforce-on-completions="true"
>
  <blocklists>
    <id>bananas</id>
  </blocklists>
</llm-content-safety>
```

Resulting in

```xml
<policies>
    <inbound>
        <base />
        <set-backend-service id="apim-generated-policy" backend-id="foundry-openai-lb" />
        <llm-token-limit remaining-quota-tokens-header-name="remaining-tokens" remaining-tokens-header-name="remaining-tokens" tokens-per-minute="1000" token-quota="10000" token-quota-period="Hourly" counter-key="@(context.Subscription.Id)" estimate-prompt-tokens="true" tokens-consumed-header-name="consumed-tokens" />
        <llm-content-safety backend-id="foundry-cognitiveservices-lb" shield-prompt="false" enforce-on-completions="true">
            <blocklists>
                <id>bananas</id>
            </blocklists>
        </llm-content-safety>
    </inbound>
    <!-- ... -->
</policies>
```

#### Test

##### Positive test

```json
{
  "max_tokens": 50,
  "messages": [
    { "role": "system", "content": "You are a helpful assistant" },
    { "role": "user", "content": "Can I get an apple?" }
  ]
}
```

Responds

```json
{
  ...
  "message": {
      "annotations": [],
      "content": "I don't have the ability to provide physical items, but I can help you with information about apples or recipes if you'd like!",
      "refusal": null,
      "role": "assistant"
  },
  ...
}
```

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

##### Negative test

##### On User Input

```json
{
  "max_tokens": 50,
  "messages": [
    { "role": "system", "content": "You are a helpful assistant" },
    { "role": "user", "content": "Can I get a banana?" }
  ]
}
```

**Responds**

```json
{
  "statusCode": 403,
  "message": "Request failed content safety check."
}
```

![No banana](../../../../assets/img/tutorial/eastus/apim/APIs/foundry-openai-lb/Test/banana.png)

##### On Output

Now, we'll try to trick LLM to say "banana", by asking the scientific name of a banana: "Musa acuminata"

```json
{
  "max_tokens": 50,
  "messages": [
    { "role": "system", "content": "You are a helpful assistant" },
    { "role": "user", "content": "What is a Musa acuminata?" }
  ]
}
```

**Responds**

```json
{
  "statusCode": 403,
  "message": "Request failed content safety check."
}
```

## Policy fragments

Now that we've did a basic testing, let's create a couple of reusable Policy fragments that we'll use from the Products.

Now, we'll create a couple of Policy fragments

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

## Next

[Back to Module](../README.md)
