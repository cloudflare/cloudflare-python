## 5.1.0 (2026-05-04)

Full Changelog: [v5.0.0...v5.1.0](https://github.com/cloudflare/cloudflare-python/compare/v5.0.0...v5.1.0)

### Features

* **security_center:** add `audit_logs`, `classification`, and `context` sub-resources to insights ([ed7d261](https://github.com/cloudflare/cloudflare-python/commit/ed7d261e6))
* **zero_trust:** add `deployment_groups` sub-resource to devices ([7121a55](https://github.com/cloudflare/cloudflare-python/commit/7121a55d3))
* **aisearch:** update generated types and methods ([54b87759](https://github.com/cloudflare/cloudflare-python/commit/54b87759b))
* **email_security:** update generated types and methods ([23a979df](https://github.com/cloudflare/cloudflare-python/commit/23a979df2))
* **radar:** update generated types and methods ([b48274ef](https://github.com/cloudflare/cloudflare-python/commit/b48274ef7))
* **zones:** update generated types and methods ([f0a54099](https://github.com/cloudflare/cloudflare-python/commit/f0a540997))

#### Security Center - New Insights Sub-Resources

**AuditLogs** (`client.security_center.insights.audit_logs`)

- `list(*, account_id, zone_id, **params) -> SyncCursorPagination[AuditLogListResponse]`
- `list_by_insight(issue_id, *, account_id, zone_id, **params) -> SyncCursorPagination[AuditLogListByInsightResponse]`

New types:
```python
from cloudflare.types.security_center.insights import (
    AuditLogListResponse,
    AuditLogListByInsightResponse,
)
```

**Classification** (`client.security_center.insights.classification`)

- `update(issue_id, *, account_id, zone_id, **params) -> ClassificationUpdateResponse`

New types:
```python
from cloudflare.types.security_center.insights import ClassificationUpdateResponse
```

**Context** (`client.security_center.insights.context`)

- `get(issue_id, *, account_id) -> Optional[ContextGetResponse]`

New types:
```python
from cloudflare.types.security_center.insights import ContextGetResponse
```

#### Zero Trust - Device Deployment Groups

New sub-resource `client.zero_trust.devices.deployment_groups`:

- `create(*, account_id, **params) -> DeploymentGroup`
- `list(*, account_id, **params) -> SyncV4PagePaginationArray[DeploymentGroup]`
- `delete(group_id, *, account_id) -> DeploymentGroupDeleteResponse`
- `edit(group_id, *, account_id, **params) -> DeploymentGroup`
- `get(group_id, *, account_id) -> DeploymentGroup`

New types:
```python
from cloudflare.types.zero_trust.devices import DeploymentGroup, DeploymentGroupDeleteResponse
```
