# CloudConnector

## Rules

Types:

```python
from cloudflare.types.cloud_connector import RuleUpdateResponse, RuleListResponse
```

Methods:

- <code title="put /zones/{zone_id}/cloud_connector/rules">client.cloud_connector.rules.<a href="./src/cloudflare/resources/cloud_connector/rules.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/cloud_connector/rule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/cloud_connector/rule_update_response.py">SyncSinglePage[RuleUpdateResponse]</a></code>
- <code title="get /zones/{zone_id}/cloud_connector/rules">client.cloud_connector.rules.<a href="./src/cloudflare/resources/cloud_connector/rules.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/cloud_connector/rule_list_response.py">SyncSinglePage[RuleListResponse]</a></code>
