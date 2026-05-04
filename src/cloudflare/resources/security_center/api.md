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

### AuditLogs

Types:

```python
from cloudflare.types.security_center.insights import (
    AuditLogListResponse,
    AuditLogListByInsightResponse,
)
```

Methods:

- <code title="get /{accounts_or_zones}/{account_or_zone_id}/security-center/insights/audit-log">client.security_center.insights.audit_logs.<a href="./src/cloudflare/resources/security_center/insights/audit_logs.py">list</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/security_center/insights/audit_log_list_params.py">params</a>) -> <a href="./src/cloudflare/types/security_center/insights/audit_log_list_response.py">SyncCursorPagination[AuditLogListResponse]</a></code>
- <code title="get /{accounts_or_zones}/{account_or_zone_id}/security-center/insights/{issue_id}/audit-log">client.security_center.insights.audit_logs.<a href="./src/cloudflare/resources/security_center/insights/audit_logs.py">list_by_insight</a>(issue_id, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/security_center/insights/audit_log_list_by_insight_params.py">params</a>) -> <a href="./src/cloudflare/types/security_center/insights/audit_log_list_by_insight_response.py">SyncCursorPagination[AuditLogListByInsightResponse]</a></code>

### Classification

Types:

```python
from cloudflare.types.security_center.insights import ClassificationUpdateResponse
```

Methods:

- <code title="patch /{accounts_or_zones}/{account_or_zone_id}/security-center/insights/{issue_id}/classification">client.security_center.insights.classification.<a href="./src/cloudflare/resources/security_center/insights/classification.py">update</a>(issue_id, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/security_center/insights/classification_update_params.py">params</a>) -> <a href="./src/cloudflare/types/security_center/insights/classification_update_response.py">ClassificationUpdateResponse</a></code>

### Context

Types:

```python
from cloudflare.types.security_center.insights import ContextGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/security-center/insights/{issue_id}/context">client.security_center.insights.context.<a href="./src/cloudflare/resources/security_center/insights/context.py">get</a>(issue_id, \*, account_id) -> <a href="./src/cloudflare/types/security_center/insights/context_get_response.py">Optional[ContextGetResponse]</a></code>
