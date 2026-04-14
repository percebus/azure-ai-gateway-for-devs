# Foundry instances

## Stacks

| Resource                | Primary                     | Secondary                    |
| ----------------------- | --------------------------- | ---------------------------- |
| Region                  | `eastus`                    | `eastus2`                    |
| Log Analytics Workspace | `-eastus-law`               | -`eastus2-law`               |
| App Insights            | `-eastus-appi`              | -`eastus2-appi`              |
| Foundry Instances       | `-eastus-foundry-{purpose}` | -`eastus2-foundry-{purpose}` |

![MS Foundry](../../../assets/img/buttons/foundry.png)

For foundry, we will create 2 instances.

1. One will represent (pre-)[P]aid [T]oken [U]sage: `ptu`
2. The other is a [P]ay [a]s [y]ou [G]o fallback instance: `payg`

| Instance | Name                                    | Region                       |
| -------- | --------------------------------------- | ---------------------------- |
| PTU      | `ai-gw-{stack-id}-eastus-foundry-ptu`   | `(US) East US`.- `eastus`    |
| PAYG     | `ai-gw-{stack-id}-eastus2-foundry-payg` | `(US) East US 2`.- `eastus2` |

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
            <li>Name: <pre>ai-gw-{stack-id}-eastus-foundry-ptu</pre></li>
            <li>Region: <pre>(US) East US`.- `eastus`</pre></li>
            <li>Default project name: <pre>ai-gw-{stack-id}-eastus-foundry-ptu-proj</pre></li>
            <li>Application Insights: <pre>ai-gw-{stack-id}-eastus-appi</pre> (created above)</li>
        </ul>
      </td>
      <td>
        <ul>
            <li>Name: <pre>ai-gw-{stack-id}-eastus2-foundry-payg</pre></li>
            <li>Region: <pre>(US) East US 2`.- `eastus2`</pre></li>
            <li>Default project name: <pre>ai-gw-{stack-id}-eastus2-foundry-payg-proj</pre></li>
            <li>Application Insights: <pre>ai-gw-{stack-id}-eastus2-appi</pre> (created above)</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

## Basics

![Foundry - PTU](../../../assets/img/tutorial/eastus/foundry/+/Basics.png)

## Storage

### Credential storage and application logging

- Application Insights: `ai-gw-{stack-id}-eastus-appi` (created above)

## Network

Leave as-is

![Network](../../../assets/img/tutorial/eastus/foundry/+/Network.png)

> [!WARNING]
> This is not production grade. For a guide using VPNs, see [Azure Secure Networking for Devs](https://github.com/percebus/azure-secure-networking-for-devs/)

## Identity

Leave as-is

![Identity](../../../assets/img/tutorial/eastus/foundry/+/Identity.png)

## Encryption

Leave as-is

![Encryption](../../../assets/img/tutorial/eastus/foundry/+/Encryption.png)

## Review + create

![Review + create](../../../assets/img/tutorial/eastus/foundry/+/Review.png)

## Snapshot

![Snapshot w/ Foundry](../../../assets/img/architecture/04_foundry_rg.png)
