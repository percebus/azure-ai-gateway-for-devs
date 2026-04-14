# Foundry + APIM

## Add APIs

We'll add both Foundry instances as APIs in APIM.

1. APIs > APIs
2. Click on "Microsoft Foundry"

### PTU

#### Select AI Service

1. Filter by "PTU"
2. Select the PTU instance

![Select PTU instance](../../../assets/img/tutorial/eastus/apim/APIs/Foundry/ptu/+/Select_AI_Service.png)

#### Configure Model Route

Use `foundry-ptu-openai` for all 3

- Display name:
- Name:
- Base path:

For **Options**, Leave "Azure OpenAI" selected.

![Configure Model Route](../../../assets/img/tutorial/eastus/apim/APIs/Foundry/ptu/+/Configure_Model_Route.png)

> [!NOTE]
> The `-openai` suffix is important.

#### Manage token consumption

We will manually do this section later. However, we want you to know where that data comes from.

Note 2 important details:

- Limit by: Subscription
- Token quota

Please select everything as in the photo.

![Manage token consumption](../../../assets/img/tutorial/eastus/apim/APIs/Foundry/ptu/+/Manage_token_consumption.png)

#### Apply semantic caching

Semantic caching is outside the scope of this tutorial. However, you can experiment yourself by creating a ReDIS cache and configuring it in APIM.

> [!WARNING]
> OpenAI sometimes would reply w/ status 200, and message "Something went wrong". This gets cached

#### Setup AI content safety

APIM allows to connect directly to a Content Safety instance.

However, since foundry includes Content Safety as part of its built-in APIs, we'll do that instead in a later step.

#### Review + create

![Review + create](../../../assets/img/tutorial/eastus/apim/APIs/Foundry/ptu/+/Review.png)

#### Design

See how APIM read the OpenAPI spec (not to be confused with OpenAI) for all the methods.

![foundry-ptu-openai](../../../assets/img/tutorial/eastus/apim/APIs/Foundry/ptu/Design.png)

Note that in "Inbound processing" there is an XML symbol like this: `</>`. Click it

![Inbound processing](../../../assets/img/tutorial/eastus/apim/APIs/Foundry/ptu/Design_Inbound_processing.png)

Inside, you'll see

```xml
<policies>
    <inbound>
        <base />

        <!-- APIM-to-service -->
        <set-backend-service id="apim-generated-policy" backend-id="foundry-ptu-openai-ai-endpoint" />

        <!-- Sets limit -->
        <llm-token-limit
          remaining-quota-tokens-header-name="remaining-tokens"
          remaining-tokens-header-name="remaining-tokens"
          tokens-per-minute="1000"
          token-quota="10000" token-quota-period="Hourly"
          counter-key="@(context.Subscription.Id)"
          estimate-prompt-tokens="true"
          tokens-consumed-header-name="consumed-tokens" />
    </inbound>
```

Note this bit: `<set-backend-service id="apim-generated-policy" backend-id="foundry-ptu-openai-ai-endpoint" />`

1. Go to APIs > Backends. and find the backend with the ID `foundry-ptu-openai-ai-endpoint`. This is the backend service that the APIM policy is routing requests to.
1. Go to Authorization credentials > Managed Identity. Look at the following fields:

- Client identity: System managed identity
- Resource ID: `https://cognitiveservices.azure.com/`

![cognitiveservices](../../../assets/img/tutorial/eastus/apim/Backends/foundry-ptu-openai/Authorization_credentials/Managed_Identity.png)

#### Settings

1. Go back to the APIs > APIs > `foundry-ptu-openai`.
1. Click on "Settings".

##### General

1. Note that the wizard kindly added `/openai` suffixes for the APIs.

![Settings](../../../assets/img/tutorial/eastus/apim/APIs/Foundry/ptu/Settings_General.png)

> [!NOTE]
> Remember that "NOTE: `-openai` suffix is important?"

##### Subscription

APIM by default, uses `Ocp-Apim-Subscription-Key`header for subscriptions (we'll get to them later)

However, note that here the values are:

- Header name: `api-key`
- Query parameter name: `subscription-key`

This simplifies passing the `API_KEY` from a `python` app, where we can replace the **Primary Key**, for a **Subscription Key**.

### PayG

We'll follow the same process from PTU, but this time

- Name: `foundry-payg-openai`
