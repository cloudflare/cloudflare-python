# MagicNetworkMonitoring

## VPCFlows

### Tokens

Types:

```python
from cloudflare.types.magic_network_monitoring.vpc_flows import TokenCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/mnm/vpc-flows/token">client.magic_network_monitoring.vpc_flows.tokens.<a href="./src/cloudflare/resources/magic_network_monitoring/vpc_flows/tokens.py">create</a>(\*, account_id) -> <a href="./src/cloudflare/types/magic_network_monitoring/vpc_flows/token_create_response.py">str</a></code>

## Configs

Types:

```python
from cloudflare.types.magic_network_monitoring import Configuration
```

Methods:

- <code title="post /accounts/{account_id}/mnm/config">client.magic_network_monitoring.configs.<a href="./src/cloudflare/resources/magic_network_monitoring/configs/configs.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/magic_network_monitoring/config_create_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_network_monitoring/configuration.py">Configuration</a></code>
- <code title="put /accounts/{account_id}/mnm/config">client.magic_network_monitoring.configs.<a href="./src/cloudflare/resources/magic_network_monitoring/configs/configs.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/magic_network_monitoring/config_update_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_network_monitoring/configuration.py">Configuration</a></code>
- <code title="delete /accounts/{account_id}/mnm/config">client.magic_network_monitoring.configs.<a href="./src/cloudflare/resources/magic_network_monitoring/configs/configs.py">delete</a>(\*, account_id) -> <a href="./src/cloudflare/types/magic_network_monitoring/configuration.py">Configuration</a></code>
- <code title="patch /accounts/{account_id}/mnm/config">client.magic_network_monitoring.configs.<a href="./src/cloudflare/resources/magic_network_monitoring/configs/configs.py">edit</a>(\*, account_id, \*\*<a href="src/cloudflare/types/magic_network_monitoring/config_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_network_monitoring/configuration.py">Configuration</a></code>
- <code title="get /accounts/{account_id}/mnm/config">client.magic_network_monitoring.configs.<a href="./src/cloudflare/resources/magic_network_monitoring/configs/configs.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/magic_network_monitoring/configuration.py">Configuration</a></code>

### Full

Methods:

- <code title="get /accounts/{account_id}/mnm/config/full">client.magic_network_monitoring.configs.full.<a href="./src/cloudflare/resources/magic_network_monitoring/configs/full.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/magic_network_monitoring/configuration.py">Configuration</a></code>

## Rules

Types:

```python
from cloudflare.types.magic_network_monitoring import MagicNetworkMonitoringRule
```

Methods:

- <code title="post /accounts/{account_id}/mnm/rules">client.magic_network_monitoring.rules.<a href="./src/cloudflare/resources/magic_network_monitoring/rules/rules.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/magic_network_monitoring/rule_create_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_network_monitoring/magic_network_monitoring_rule.py">Optional[MagicNetworkMonitoringRule]</a></code>
- <code title="put /accounts/{account_id}/mnm/rules">client.magic_network_monitoring.rules.<a href="./src/cloudflare/resources/magic_network_monitoring/rules/rules.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/magic_network_monitoring/rule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_network_monitoring/magic_network_monitoring_rule.py">Optional[MagicNetworkMonitoringRule]</a></code>
- <code title="get /accounts/{account_id}/mnm/rules">client.magic_network_monitoring.rules.<a href="./src/cloudflare/resources/magic_network_monitoring/rules/rules.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/magic_network_monitoring/magic_network_monitoring_rule.py">SyncSinglePage[Optional[MagicNetworkMonitoringRule]]</a></code>
- <code title="delete /accounts/{account_id}/mnm/rules/{rule_id}">client.magic_network_monitoring.rules.<a href="./src/cloudflare/resources/magic_network_monitoring/rules/rules.py">delete</a>(rule_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_network_monitoring/magic_network_monitoring_rule.py">Optional[MagicNetworkMonitoringRule]</a></code>
- <code title="patch /accounts/{account_id}/mnm/rules/{rule_id}">client.magic_network_monitoring.rules.<a href="./src/cloudflare/resources/magic_network_monitoring/rules/rules.py">edit</a>(rule_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_network_monitoring/rule_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_network_monitoring/magic_network_monitoring_rule.py">Optional[MagicNetworkMonitoringRule]</a></code>
- <code title="get /accounts/{account_id}/mnm/rules/{rule_id}">client.magic_network_monitoring.rules.<a href="./src/cloudflare/resources/magic_network_monitoring/rules/rules.py">get</a>(rule_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_network_monitoring/magic_network_monitoring_rule.py">Optional[MagicNetworkMonitoringRule]</a></code>

### Advertisements

Types:

```python
from cloudflare.types.magic_network_monitoring.rules import Advertisement
```

Methods:

- <code title="patch /accounts/{account_id}/mnm/rules/{rule_id}/advertisement">client.magic_network_monitoring.rules.advertisements.<a href="./src/cloudflare/resources/magic_network_monitoring/rules/advertisements.py">edit</a>(rule_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_network_monitoring/rules/advertisement_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_network_monitoring/rules/advertisement.py">Optional[Advertisement]</a></code>
