# Azure Monitoring services

## Stacks

| Resource                | Primary                     | Secondary                    |
| ----------------------- | --------------------------- | ---------------------------- |
| Region                  | `eastus`                    | `eastus2`                    |
| Log Analytics Workspace | `-eastus-law`               | `-eastus2-law`               |
| App Insights            | `-eastus-appi`              | `-eastus2-appi`              |
| Foundry Instances       | `-eastus-foundry-{purpose}` | `-eastus2-foundry-{purpose}` |

## Log Analytics Workspace

![LAW](../../../assets/img/buttons/law.png)

We will funnel all of our logs into App Insights for monitoring and diagnostics, using log analytics workspace.

Since Foundry will be deployed across multiple regions, it is considered best practice to create Log Analytics Workspace in each region to collect and analyze logs.

For tutorial purposes, you can create only 1 Log Analytics Workspace + App Insights, however, we wanted to call it out.

| Resource                | Primary       | Secondary (Optional) |
| ----------------------- | ------------- | -------------------- |
| Log Analytics Workspace | `-eastus-law` | `-eastus2-law`       |

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
            <li>Name: <pre>ai-gw-{stack-id}-eastus-law</pre></li>
            <li>Region: <pre>(US) East US - eastus</pre></li>
        </ul>
      </td>
      <td>
        <ul>
            <li>Name: <pre>ai-gw-{stack-id}-eastus2-law</pre></li>
            <li>Region: <pre>(US) East US 2 - eastus2</pre></li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

### Basics

![LAW - Basics](../../../assets/img/tutorial/eastus/law/+/Basics.png)

### Review + create

![LAW - Review + Create](../../../assets/img/tutorial/eastus/law/+/Review.png)

### Snapshot

You should end up with this

![architecture 02](../../../assets/img/architecture/02_law_rg.png)

## App Insights

![appi](../../../assets/img/buttons/appi.png)

For each LAW, we will create an App Insights instance to collect and analyze telemetry data.

| Resource     | Primary        | Secondary       |
| ------------ | -------------- | --------------- |
| App Insights | `-eastus-appi` | `-eastus2-appi` |

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
            <li>Name: <pre>ai-gw-{stack-id}-eastus-appi</pre></li>
            <li>Region: <pre>(US) East US - eastus</pre></li>
            <li>Log Analytics Workspace: <pre>ai-gw-{stack-id}-eastus-law</pre> (created above)</li>
        </ul>
      </td>
      <td>
        <ul>
            <li>Name: <pre>ai-gw-{stack-id}-eastus2-appi</pre></li>
            <li>Region: <pre>(US) East US 2 - eastus2</pre></li>
            <li>Log Analytics Workspace: <pre>ai-gw-{stack-id}-eastus2-law</pre> (created above)</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

### Basics

![App Insights - Basics](../../../assets/img/tutorial/eastus/appi/+/Basics.png)

### Snapshot

![architecture 03](../../../assets/img/architecture/03_appi_rg.png)

#### Resource Visualization

![architecture 03](../../../assets/img/architecture/03_appi_visualizer.png)

## Next

[Back to Module](./README.md)
