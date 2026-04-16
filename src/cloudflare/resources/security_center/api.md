# SecurityCenter

## Insights

Types:

```python
from cloudflare.types.security_center import InsightListResponse, InsightDismissResponse
```

Methods:

- <code title="get /{accounts_or_zones}/{account_or_zone_id}/security-center/insights">client.security_center.insights.<a href="./src/cloudflare/resources/security_center/insights/insights.py">list</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/security_center/insight_list_params.py">params</a>) -> <a href="./src/cloudflare/types/security_center/insight_list_response.py">SyncV4PagePagination[Optional[InsightListResponse]]</a></code>
- <code title="put /{accounts_or_zones}/{account_or_zone_id}/security-center/insights/{issue_id}/dismiss">client.security_center.insights.<a href="./src/cloudflare/resources/security_center/insights/insights.py">dismiss</a>(issue_id, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/security_center/insight_dismiss_params.py">params</a>) -> <a href="./src/cloudflare/types/security_center/insight_dismiss_response.py">InsightDismissResponse</a></code>

### Class

Types:

```python
from cloudflare.types.security_center.insights import ClassGetResponse
```

Methods:

- <code title="get /{accounts_or_zones}/{account_or_zone_id}/security-center/insights/class">client.security*center.insights.class*.<a href="./src/cloudflare/resources/security_center/insights/class_.py">get</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/security_center/insights/class_get_params.py">params</a>) -> <a href="./src/cloudflare/types/security_center/insights/class_get_response.py">Optional[ClassGetResponse]</a></code>

### Severity

Types:

```python
from cloudflare.types.security_center.insights import SeverityGetResponse
```

Methods:

- <code title="get /{accounts_or_zones}/{account_or_zone_id}/security-center/insights/severity">client.security_center.insights.severity.<a href="./src/cloudflare/resources/security_center/insights/severity.py">get</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/security_center/insights/severity_get_params.py">params</a>) -> <a href="./src/cloudflare/types/security_center/insights/severity_get_response.py">Optional[SeverityGetResponse]</a></code>

### Type

Types:

```python
from cloudflare.types.security_center.insights import TypeGetResponse
```

Methods:

- <code title="get /{accounts_or_zones}/{account_or_zone_id}/security-center/insights/type">client.security_center.insights.type.<a href="./src/cloudflare/resources/security_center/insights/type.py">get</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/security_center/insights/type_get_params.py">params</a>) -> <a href="./src/cloudflare/types/security_center/insights/type_get_response.py">Optional[TypeGetResponse]</a></code>
