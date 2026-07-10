# Organizations

Types:

```python
from cloudflare.types.organizations import Organization, OrganizationDeleteResponse
```

Methods:

- <code title="post /organizations">client.organizations.<a href="./src/cloudflare/resources/organizations/organizations.py">create</a>(\*\*<a href="src/cloudflare/types/organizations/organization_create_params.py">params</a>) -> <a href="./src/cloudflare/types/organizations/organization.py">Organization</a></code>
- <code title="put /organizations/{organization_id}">client.organizations.<a href="./src/cloudflare/resources/organizations/organizations.py">update</a>(organization_id, \*\*<a href="src/cloudflare/types/organizations/organization_update_params.py">params</a>) -> <a href="./src/cloudflare/types/organizations/organization.py">Organization</a></code>
- <code title="get /organizations">client.organizations.<a href="./src/cloudflare/resources/organizations/organizations.py">list</a>(\*\*<a href="src/cloudflare/types/organizations/organization_list_params.py">params</a>) -> <a href="./src/cloudflare/types/organizations/organization.py">SyncSinglePage[Organization]</a></code>
- <code title="delete /organizations/{organization_id}">client.organizations.<a href="./src/cloudflare/resources/organizations/organizations.py">delete</a>(organization_id) -> <a href="./src/cloudflare/types/organizations/organization_delete_response.py">OrganizationDeleteResponse</a></code>
- <code title="get /organizations/{organization_id}">client.organizations.<a href="./src/cloudflare/resources/organizations/organizations.py">get</a>(organization_id) -> <a href="./src/cloudflare/types/organizations/organization.py">Organization</a></code>

## OrganizationProfile

Types:

```python
from cloudflare.types.organizations import OrganizationProfile
```

Methods:

- <code title="put /organizations/{organization_id}/profile">client.organizations.organization_profile.<a href="./src/cloudflare/resources/organizations/organization_profile.py">update</a>(organization_id, \*\*<a href="src/cloudflare/types/organizations/organization_profile_update_params.py">params</a>) -> None</code>
- <code title="get /organizations/{organization_id}/profile">client.organizations.organization_profile.<a href="./src/cloudflare/resources/organizations/organization_profile.py">get</a>(organization_id) -> <a href="./src/cloudflare/types/organizations/organization_profile.py">OrganizationProfile</a></code>

## Logs

### Audit

Types:

```python
from cloudflare.types.organizations.logs import AuditListResponse, AuditHistoryResponse
```

Methods:

- <code title="get /organizations/{organization_id}/logs/audit">client.organizations.logs.audit.<a href="./src/cloudflare/resources/organizations/logs/audit.py">list</a>(organization_id, \*\*<a href="src/cloudflare/types/organizations/logs/audit_list_params.py">params</a>) -> <a href="./src/cloudflare/types/organizations/logs/audit_list_response.py">SyncCursorPaginationAfter[AuditListResponse]</a></code>
- <code title="get /organizations/{organization_id}/logs/audit/{id}/history">client.organizations.logs.audit.<a href="./src/cloudflare/resources/organizations/logs/audit.py">history</a>(id, \*, organization_id, \*\*<a href="src/cloudflare/types/organizations/logs/audit_history_params.py">params</a>) -> <a href="./src/cloudflare/types/organizations/logs/audit_history_response.py">AuditHistoryResponse</a></code>

## Billing

### Usage

Types:

```python
from cloudflare.types.organizations.billing import UsageGetResponse
```

Methods:

- <code title="get /organizations/{organization_id}/billable/usage">client.organizations.billing.usage.<a href="./src/cloudflare/resources/organizations/billing/usage.py">get</a>(organization_id, \*\*<a href="src/cloudflare/types/organizations/billing/usage_get_params.py">params</a>) -> <a href="./src/cloudflare/types/organizations/billing/usage_get_response.py">UsageGetResponse</a></code>
