# Create Foundry Instances

## Stacks

| Resource                | Primary                     | Secondary                    |
| ----------------------- | --------------------------- | ---------------------------- |
| Log Analytics Workspace | `-eastus-law`               | -`eastus2-law`               |
| App Insights            | `-eastus-appi`              | -`eastus2-appi`              |
| Foundry Instances       | `-eastus-foundry-{purpose}` | -`eastus2-foundry-{purpose}` |

## Log Analytics Workspace

![LAW](../../../assets/img/resources/law.png)

We will funnel of our logs into App Insights for monitoring and diagnostics, using log analytics workspace.

Since Foundry will be deployed across multiple regions, it is considered best practice to create Log Analytics Workspace in each region to collect and analyze logs.

For tutorial purposes, you can create only 1 Log Analytics Workspace + App Insights, however, we wanted to call it out.

| Resource                | Primary       | Secondary (Optional) |
| ----------------------- | ------------- | -------------------- |
| Log Analytics Workspace | `-eastus-law` | -`eastus2-law`       |

<table>
  <thead>
    <tr>
      <th>eastus</th>
      <th>eastus2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <ul>
            <li>Name: `ai-gw-{stack-id}-eastus-law`</li>
            <li>Region: `(US) East US`.- `eastus`</li>
        </ul>
      </td>
      <td>
        <ul>
            <li>Name: `ai-gw-{stack-id}-eastus2-law`</li>
            <li>Region: `(US) East US 2`.- `eastus2`</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

### Basics

![LAW - Basics](../../../assets/img/tutorial/eastus/law/Basics.png)

### Review + create

![LAW - Review + Create](../../../assets/img/tutorial/eastus/law/Review.png)

### Snapshot

You should end up with this

![](../../../assets/img/architecture/02%20-%20law.png)

## App Insights

![appi](../../../assets/img/resources/appi.png)

For each LAW, we will create an App Insights instance to collect and analyze telemetry data.

| Resource                | Primary                     | Secondary                    |
| ----------------------- | --------------------------- | ---------------------------- |
| App Insights            | `-eastus-appi`              | -`eastus2-appi`              |

If you only created 1 Log Analytics Workspace, only create 1 App Insights instance.

<table>
  <thead>
    <tr>
      <th>eastus</th>
      <th>eastus2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <ul>
            <li>Name: `ai-gw-{stack-id}-eastus-appi`</li>
            <li>Region: `(US) East US`.- `eastus`</li>
            <li>Log Analytics Workspace: `ai-gw-{stack-id}-eastus-law` (created above)</li>
        </ul>
      </td>
      <td>
        <ul>
            <li>Name: `ai-gw-{stack-id}-eastus2-appi`</li>
            <li>Region: `(US) East US 2`.- `eastus2`</li>
            <li>Log Analytics Workspace: `ai-gw-{stack-id}-eastus2-law` (created above)</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

### Basics

![App Insights - Basics](../../../assets/img/tutorial/eastus/appi/Basics.png)

### Snapshot

## Foundry Instances

![MS Foundry](../../../assets/img/resources/foundry.png)

For foundry, we will create 2 instances.

1. One will represent (pre-)[P]aid [T]oken [U]sage: `ptu`
2. The other is a [P]ay [a]s [y]ou [G]o fallback instance: `payg`

| Instance | Name                            | Region                    |
| -------- | ------------------------------- | ------------------------- |
| PTU      | `ai-gw-{stack-id}-foundry-ptu`  | `(US) East US`.- `eastus` |
| PAYG     | `ai-gw-{stack-id}-foundry-payg` | `(US) East US`.- `eastus` |

### PTU

#### Basics

![Foundry - PTU](../../../assets/img/tutorial/eastus/foundry/Basics.png)

##### Instance Details

- Name: `ai-gw-{stack-id}-foundry-ptu`
- Region: `(US) East US`.- `eastus`

##### Your first project

- Default project name: `ai-gw-{stack-id}-foundry-ptu-proj`
