# Azure API Management

Remember when we added MS Foundry using the APIM wizard and it did everything for us?

Well, this time, we'll take it up a notch and manually add configuration.

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


## Policy fragments

We'll create a couple of Policy fragments

- A strict one
- And a lenient one


```xml
<fragment>
  <llm-content-safety
    backend-id="{backend or load balancer name}"
    shield-prompt="true" <<< Prompt injections protection
    enforce-on-completions="true"
  >
      <!-- SRC: https://learn.microsoft.com/en-us/azure/api-management/llm-content-safety-policy -->
      <categories output-type="EightSeverityLevels">
          <category name="Hate" threshold="1" />
          <category name="SelfHarm" threshold="2" />
          <category name="Sexual" threshold="3" />
          <category name="Violence" threshold="4" />
      </categories>
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
