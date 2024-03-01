# Accounts

Types:

```python
from cloudflare.types import AccountUpdateResponse, AccountListResponse, AccountGetResponse
```

Methods:

- <code title="put /accounts/{account_id}">client.accounts.<a href="./src/cloudflare/resources/accounts/accounts.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/account_update_params.py">params</a>) -> <a href="./src/cloudflare/types/account_update_response.py">AccountUpdateResponse</a></code>
- <code title="get /accounts">client.accounts.<a href="./src/cloudflare/resources/accounts/accounts.py">list</a>(\*\*<a href="src/cloudflare/types/account_list_params.py">params</a>) -> <a href="./src/cloudflare/types/account_list_response.py">SyncV4PagePaginationArray[object]</a></code>
- <code title="get /accounts/{account_id}">client.accounts.<a href="./src/cloudflare/resources/accounts/accounts.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/account_get_response.py">AccountGetResponse</a></code>

## Members

Types:

```python
from cloudflare.types.accounts import (
    MemberCreateResponse,
    MemberUpdateResponse,
    MemberListResponse,
    MemberDeleteResponse,
    MemberGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/members">client.accounts.members.<a href="./src/cloudflare/resources/accounts/members.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/accounts/member_create_params.py">params</a>) -> <a href="./src/cloudflare/types/accounts/member_create_response.py">MemberCreateResponse</a></code>
- <code title="put /accounts/{account_id}/members/{member_id}">client.accounts.members.<a href="./src/cloudflare/resources/accounts/members.py">update</a>(member_id, \*, account_id, \*\*<a href="src/cloudflare/types/accounts/member_update_params.py">params</a>) -> <a href="./src/cloudflare/types/accounts/member_update_response.py">MemberUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/members">client.accounts.members.<a href="./src/cloudflare/resources/accounts/members.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/accounts/member_list_params.py">params</a>) -> <a href="./src/cloudflare/types/accounts/member_list_response.py">SyncV4PagePaginationArray[MemberListResponse]</a></code>
- <code title="delete /accounts/{account_id}/members/{member_id}">client.accounts.members.<a href="./src/cloudflare/resources/accounts/members.py">delete</a>(member_id, \*, account_id) -> <a href="./src/cloudflare/types/accounts/member_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/members/{member_id}">client.accounts.members.<a href="./src/cloudflare/resources/accounts/members.py">get</a>(member_id, \*, account_id) -> <a href="./src/cloudflare/types/accounts/member_get_response.py">MemberGetResponse</a></code>

## Roles

Types:

```python
from cloudflare.types.accounts import RoleListResponse, RoleGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/roles">client.accounts.roles.<a href="./src/cloudflare/resources/accounts/roles.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/accounts/role_list_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/roles/{role_id}">client.accounts.roles.<a href="./src/cloudflare/resources/accounts/roles.py">get</a>(role_id, \*, account_id) -> <a href="./src/cloudflare/types/accounts/role_get_response.py">RoleGetResponse</a></code>

# Certificates

Types:

```python
from cloudflare.types import (
    CertificateCreateResponse,
    CertificateListResponse,
    CertificateDeleteResponse,
    CertificateGetResponse,
)
```

Methods:

- <code title="post /certificates">client.certificates.<a href="./src/cloudflare/resources/certificates.py">create</a>(\*\*<a href="src/cloudflare/types/certificate_create_params.py">params</a>) -> <a href="./src/cloudflare/types/certificate_create_response.py">CertificateCreateResponse</a></code>
- <code title="get /certificates">client.certificates.<a href="./src/cloudflare/resources/certificates.py">list</a>() -> <a href="./src/cloudflare/types/certificate_list_response.py">Optional</a></code>
- <code title="delete /certificates/{certificate_id}">client.certificates.<a href="./src/cloudflare/resources/certificates.py">delete</a>(certificate_id) -> <a href="./src/cloudflare/types/certificate_delete_response.py">CertificateDeleteResponse</a></code>
- <code title="get /certificates/{certificate_id}">client.certificates.<a href="./src/cloudflare/resources/certificates.py">get</a>(certificate_id) -> <a href="./src/cloudflare/types/certificate_get_response.py">CertificateGetResponse</a></code>

# IPs

Types:

```python
from cloudflare.types import IPListResponse
```

Methods:

- <code title="get /ips">client.ips.<a href="./src/cloudflare/resources/ips.py">list</a>(\*\*<a href="src/cloudflare/types/ip_list_params.py">params</a>) -> <a href="./src/cloudflare/types/ip_list_response.py">IPListResponse</a></code>

# Memberships

Types:

```python
from cloudflare.types import (
    MembershipUpdateResponse,
    MembershipListResponse,
    MembershipDeleteResponse,
    MembershipGetResponse,
)
```

Methods:

- <code title="put /memberships/{membership_id}">client.memberships.<a href="./src/cloudflare/resources/memberships.py">update</a>(membership_id, \*\*<a href="src/cloudflare/types/membership_update_params.py">params</a>) -> <a href="./src/cloudflare/types/membership_update_response.py">MembershipUpdateResponse</a></code>
- <code title="get /memberships">client.memberships.<a href="./src/cloudflare/resources/memberships.py">list</a>(\*\*<a href="src/cloudflare/types/membership_list_params.py">params</a>) -> <a href="./src/cloudflare/types/membership_list_response.py">SyncV4PagePaginationArray[MembershipListResponse]</a></code>
- <code title="delete /memberships/{membership_id}">client.memberships.<a href="./src/cloudflare/resources/memberships.py">delete</a>(membership_id) -> <a href="./src/cloudflare/types/membership_delete_response.py">MembershipDeleteResponse</a></code>
- <code title="get /memberships/{membership_id}">client.memberships.<a href="./src/cloudflare/resources/memberships.py">get</a>(membership_id) -> <a href="./src/cloudflare/types/membership_get_response.py">MembershipGetResponse</a></code>

# User

Types:

```python
from cloudflare.types import UserListResponse, UserEditResponse
```

Methods:

- <code title="get /user">client.user.<a href="./src/cloudflare/resources/user/user.py">list</a>() -> <a href="./src/cloudflare/types/user_list_response.py">UserListResponse</a></code>
- <code title="patch /user">client.user.<a href="./src/cloudflare/resources/user/user.py">edit</a>(\*\*<a href="src/cloudflare/types/user_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/user_edit_response.py">UserEditResponse</a></code>

## AuditLogs

Types:

```python
from cloudflare.types.user import AuditLogListResponse
```

Methods:

- <code title="get /user/audit_logs">client.user.audit_logs.<a href="./src/cloudflare/resources/user/audit_logs.py">list</a>(\*\*<a href="src/cloudflare/types/user/audit_log_list_params.py">params</a>) -> <a href="./src/cloudflare/types/user/audit_log_list_response.py">SyncV4PagePaginationArray[AuditLogListResponse]</a></code>

## Billing

### History

Types:

```python
from cloudflare.types.user.billing import HistoryListResponse
```

Methods:

- <code title="get /user/billing/history">client.user.billing.history.<a href="./src/cloudflare/resources/user/billing/history.py">list</a>(\*\*<a href="src/cloudflare/types/user/billing/history_list_params.py">params</a>) -> <a href="./src/cloudflare/types/user/billing/history_list_response.py">SyncV4PagePaginationArray[HistoryListResponse]</a></code>

### Profiles

Types:

```python
from cloudflare.types.user.billing import ProfileListResponse
```

Methods:

- <code title="get /user/billing/profile">client.user.billing.profiles.<a href="./src/cloudflare/resources/user/billing/profiles.py">list</a>() -> <a href="./src/cloudflare/types/user/billing/profile_list_response.py">ProfileListResponse</a></code>

## Firewall

### AccessRules

Types:

```python
from cloudflare.types.user.firewall import (
    AccessRuleCreateResponse,
    AccessRuleListResponse,
    AccessRuleDeleteResponse,
    AccessRuleEditResponse,
)
```

Methods:

- <code title="post /user/firewall/access_rules/rules">client.user.firewall.access_rules.<a href="./src/cloudflare/resources/user/firewall/access_rules.py">create</a>(\*\*<a href="src/cloudflare/types/user/firewall/access_rule_create_params.py">params</a>) -> <a href="./src/cloudflare/types/user/firewall/access_rule_create_response.py">Optional</a></code>
- <code title="get /user/firewall/access_rules/rules">client.user.firewall.access_rules.<a href="./src/cloudflare/resources/user/firewall/access_rules.py">list</a>(\*\*<a href="src/cloudflare/types/user/firewall/access_rule_list_params.py">params</a>) -> <a href="./src/cloudflare/types/user/firewall/access_rule_list_response.py">SyncV4PagePaginationArray[AccessRuleListResponse]</a></code>
- <code title="delete /user/firewall/access_rules/rules/{identifier}">client.user.firewall.access_rules.<a href="./src/cloudflare/resources/user/firewall/access_rules.py">delete</a>(identifier) -> <a href="./src/cloudflare/types/user/firewall/access_rule_delete_response.py">Optional</a></code>
- <code title="patch /user/firewall/access_rules/rules/{identifier}">client.user.firewall.access_rules.<a href="./src/cloudflare/resources/user/firewall/access_rules.py">edit</a>(identifier, \*\*<a href="src/cloudflare/types/user/firewall/access_rule_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/user/firewall/access_rule_edit_response.py">Optional</a></code>

## Invites

Types:

```python
from cloudflare.types.user import InviteListResponse, InviteEditResponse, InviteGetResponse
```

Methods:

- <code title="get /user/invites">client.user.invites.<a href="./src/cloudflare/resources/user/invites.py">list</a>() -> <a href="./src/cloudflare/types/user/invite_list_response.py">Optional</a></code>
- <code title="patch /user/invites/{invite_id}">client.user.invites.<a href="./src/cloudflare/resources/user/invites.py">edit</a>(invite_id, \*\*<a href="src/cloudflare/types/user/invite_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/user/invite_edit_response.py">InviteEditResponse</a></code>
- <code title="get /user/invites/{invite_id}">client.user.invites.<a href="./src/cloudflare/resources/user/invites.py">get</a>(invite_id) -> <a href="./src/cloudflare/types/user/invite_get_response.py">InviteGetResponse</a></code>

## LoadBalancers

### Monitors

Types:

```python
from cloudflare.types.user.load_balancers import (
    MonitorCreateResponse,
    MonitorUpdateResponse,
    MonitorListResponse,
    MonitorDeleteResponse,
    MonitorEditResponse,
    MonitorGetResponse,
    MonitorPreviewResponse,
    MonitorReferencesResponse,
)
```

Methods:

- <code title="post /user/load_balancers/monitors">client.user.load_balancers.monitors.<a href="./src/cloudflare/resources/user/load_balancers/monitors.py">create</a>(\*\*<a href="src/cloudflare/types/user/load_balancers/monitor_create_params.py">params</a>) -> <a href="./src/cloudflare/types/user/load_balancers/monitor_create_response.py">MonitorCreateResponse</a></code>
- <code title="put /user/load_balancers/monitors/{monitor_id}">client.user.load_balancers.monitors.<a href="./src/cloudflare/resources/user/load_balancers/monitors.py">update</a>(monitor_id, \*\*<a href="src/cloudflare/types/user/load_balancers/monitor_update_params.py">params</a>) -> <a href="./src/cloudflare/types/user/load_balancers/monitor_update_response.py">MonitorUpdateResponse</a></code>
- <code title="get /user/load_balancers/monitors">client.user.load_balancers.monitors.<a href="./src/cloudflare/resources/user/load_balancers/monitors.py">list</a>() -> <a href="./src/cloudflare/types/user/load_balancers/monitor_list_response.py">Optional</a></code>
- <code title="delete /user/load_balancers/monitors/{monitor_id}">client.user.load_balancers.monitors.<a href="./src/cloudflare/resources/user/load_balancers/monitors.py">delete</a>(monitor_id) -> <a href="./src/cloudflare/types/user/load_balancers/monitor_delete_response.py">MonitorDeleteResponse</a></code>
- <code title="patch /user/load_balancers/monitors/{monitor_id}">client.user.load_balancers.monitors.<a href="./src/cloudflare/resources/user/load_balancers/monitors.py">edit</a>(monitor_id, \*\*<a href="src/cloudflare/types/user/load_balancers/monitor_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/user/load_balancers/monitor_edit_response.py">MonitorEditResponse</a></code>
- <code title="get /user/load_balancers/monitors/{monitor_id}">client.user.load_balancers.monitors.<a href="./src/cloudflare/resources/user/load_balancers/monitors.py">get</a>(monitor_id) -> <a href="./src/cloudflare/types/user/load_balancers/monitor_get_response.py">MonitorGetResponse</a></code>
- <code title="post /user/load_balancers/monitors/{monitor_id}/preview">client.user.load_balancers.monitors.<a href="./src/cloudflare/resources/user/load_balancers/monitors.py">preview</a>(monitor_id, \*\*<a href="src/cloudflare/types/user/load_balancers/monitor_preview_params.py">params</a>) -> <a href="./src/cloudflare/types/user/load_balancers/monitor_preview_response.py">MonitorPreviewResponse</a></code>
- <code title="get /user/load_balancers/monitors/{monitor_id}/references">client.user.load_balancers.monitors.<a href="./src/cloudflare/resources/user/load_balancers/monitors.py">references</a>(monitor_id) -> <a href="./src/cloudflare/types/user/load_balancers/monitor_references_response.py">Optional</a></code>

### Pools

Types:

```python
from cloudflare.types.user.load_balancers import (
    PoolCreateResponse,
    PoolUpdateResponse,
    PoolListResponse,
    PoolDeleteResponse,
    PoolEditResponse,
    PoolGetResponse,
    PoolHealthResponse,
    PoolPreviewResponse,
    PoolReferencesResponse,
)
```

Methods:

- <code title="post /user/load_balancers/pools">client.user.load_balancers.pools.<a href="./src/cloudflare/resources/user/load_balancers/pools.py">create</a>(\*\*<a href="src/cloudflare/types/user/load_balancers/pool_create_params.py">params</a>) -> <a href="./src/cloudflare/types/user/load_balancers/pool_create_response.py">PoolCreateResponse</a></code>
- <code title="put /user/load_balancers/pools/{pool_id}">client.user.load_balancers.pools.<a href="./src/cloudflare/resources/user/load_balancers/pools.py">update</a>(pool_id, \*\*<a href="src/cloudflare/types/user/load_balancers/pool_update_params.py">params</a>) -> <a href="./src/cloudflare/types/user/load_balancers/pool_update_response.py">PoolUpdateResponse</a></code>
- <code title="get /user/load_balancers/pools">client.user.load_balancers.pools.<a href="./src/cloudflare/resources/user/load_balancers/pools.py">list</a>(\*\*<a href="src/cloudflare/types/user/load_balancers/pool_list_params.py">params</a>) -> <a href="./src/cloudflare/types/user/load_balancers/pool_list_response.py">Optional</a></code>
- <code title="delete /user/load_balancers/pools/{pool_id}">client.user.load_balancers.pools.<a href="./src/cloudflare/resources/user/load_balancers/pools.py">delete</a>(pool_id) -> <a href="./src/cloudflare/types/user/load_balancers/pool_delete_response.py">PoolDeleteResponse</a></code>
- <code title="patch /user/load_balancers/pools/{pool_id}">client.user.load_balancers.pools.<a href="./src/cloudflare/resources/user/load_balancers/pools.py">edit</a>(pool_id, \*\*<a href="src/cloudflare/types/user/load_balancers/pool_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/user/load_balancers/pool_edit_response.py">PoolEditResponse</a></code>
- <code title="get /user/load_balancers/pools/{pool_id}">client.user.load_balancers.pools.<a href="./src/cloudflare/resources/user/load_balancers/pools.py">get</a>(pool_id) -> <a href="./src/cloudflare/types/user/load_balancers/pool_get_response.py">PoolGetResponse</a></code>
- <code title="get /user/load_balancers/pools/{pool_id}/health">client.user.load_balancers.pools.<a href="./src/cloudflare/resources/user/load_balancers/pools.py">health</a>(pool_id) -> <a href="./src/cloudflare/types/user/load_balancers/pool_health_response.py">PoolHealthResponse</a></code>
- <code title="post /user/load_balancers/pools/{pool_id}/preview">client.user.load_balancers.pools.<a href="./src/cloudflare/resources/user/load_balancers/pools.py">preview</a>(pool_id, \*\*<a href="src/cloudflare/types/user/load_balancers/pool_preview_params.py">params</a>) -> <a href="./src/cloudflare/types/user/load_balancers/pool_preview_response.py">PoolPreviewResponse</a></code>
- <code title="get /user/load_balancers/pools/{pool_id}/references">client.user.load_balancers.pools.<a href="./src/cloudflare/resources/user/load_balancers/pools.py">references</a>(pool_id) -> <a href="./src/cloudflare/types/user/load_balancers/pool_references_response.py">Optional</a></code>

### Preview

Types:

```python
from cloudflare.types.user.load_balancers import PreviewGetResponse
```

Methods:

- <code title="get /user/load_balancers/preview/{preview_id}">client.user.load_balancers.preview.<a href="./src/cloudflare/resources/user/load_balancers/preview.py">get</a>(preview_id) -> <a href="./src/cloudflare/types/user/load_balancers/preview_get_response.py">PreviewGetResponse</a></code>

### Analytics

#### Events

Types:

```python
from cloudflare.types.user.load_balancers.analytics import EventListResponse
```

Methods:

- <code title="get /user/load_balancing_analytics/events">client.user.load_balancers.analytics.events.<a href="./src/cloudflare/resources/user/load_balancers/analytics/events.py">list</a>(\*\*<a href="src/cloudflare/types/user/load_balancers/analytics/event_list_params.py">params</a>) -> <a href="./src/cloudflare/types/user/load_balancers/analytics/event_list_response.py">Optional</a></code>

## Organizations

Types:

```python
from cloudflare.types.user import (
    OrganizationListResponse,
    OrganizationDeleteResponse,
    OrganizationGetResponse,
)
```

Methods:

- <code title="get /user/organizations">client.user.organizations.<a href="./src/cloudflare/resources/user/organizations.py">list</a>(\*\*<a href="src/cloudflare/types/user/organization_list_params.py">params</a>) -> <a href="./src/cloudflare/types/user/organization_list_response.py">SyncV4PagePaginationArray[OrganizationListResponse]</a></code>
- <code title="delete /user/organizations/{organization_id}">client.user.organizations.<a href="./src/cloudflare/resources/user/organizations.py">delete</a>(organization_id) -> <a href="./src/cloudflare/types/user/organization_delete_response.py">OrganizationDeleteResponse</a></code>
- <code title="get /user/organizations/{organization_id}">client.user.organizations.<a href="./src/cloudflare/resources/user/organizations.py">get</a>(organization_id) -> <a href="./src/cloudflare/types/user/organization_get_response.py">OrganizationGetResponse</a></code>

## Subscriptions

Types:

```python
from cloudflare.types.user import (
    SubscriptionUpdateResponse,
    SubscriptionListResponse,
    SubscriptionDeleteResponse,
    SubscriptionEditResponse,
)
```

Methods:

- <code title="put /user/subscriptions/{identifier}">client.user.subscriptions.<a href="./src/cloudflare/resources/user/subscriptions.py">update</a>(identifier, \*\*<a href="src/cloudflare/types/user/subscription_update_params.py">params</a>) -> <a href="./src/cloudflare/types/user/subscription_update_response.py">SubscriptionUpdateResponse</a></code>
- <code title="get /user/subscriptions">client.user.subscriptions.<a href="./src/cloudflare/resources/user/subscriptions.py">list</a>() -> <a href="./src/cloudflare/types/user/subscription_list_response.py">Optional</a></code>
- <code title="delete /user/subscriptions/{identifier}">client.user.subscriptions.<a href="./src/cloudflare/resources/user/subscriptions.py">delete</a>(identifier) -> <a href="./src/cloudflare/types/user/subscription_delete_response.py">SubscriptionDeleteResponse</a></code>
- <code title="put /zones/{identifier}/subscription">client.user.subscriptions.<a href="./src/cloudflare/resources/user/subscriptions.py">edit</a>(identifier, \*\*<a href="src/cloudflare/types/user/subscription_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/user/subscription_edit_response.py">SubscriptionEditResponse</a></code>

## Tokens

Types:

```python
from cloudflare.types.user import (
    TokenCreateResponse,
    TokenUpdateResponse,
    TokenListResponse,
    TokenDeleteResponse,
    TokenGetResponse,
    TokenVerifyResponse,
)
```

Methods:

- <code title="post /user/tokens">client.user.tokens.<a href="./src/cloudflare/resources/user/tokens/tokens.py">create</a>(\*\*<a href="src/cloudflare/types/user/token_create_params.py">params</a>) -> <a href="./src/cloudflare/types/user/token_create_response.py">TokenCreateResponse</a></code>
- <code title="put /user/tokens/{token_id}">client.user.tokens.<a href="./src/cloudflare/resources/user/tokens/tokens.py">update</a>(token_id, \*\*<a href="src/cloudflare/types/user/token_update_params.py">params</a>) -> <a href="./src/cloudflare/types/user/token_update_response.py">TokenUpdateResponse</a></code>
- <code title="get /user/tokens">client.user.tokens.<a href="./src/cloudflare/resources/user/tokens/tokens.py">list</a>(\*\*<a href="src/cloudflare/types/user/token_list_params.py">params</a>) -> <a href="./src/cloudflare/types/user/token_list_response.py">SyncV4PagePaginationArray[object]</a></code>
- <code title="delete /user/tokens/{token_id}">client.user.tokens.<a href="./src/cloudflare/resources/user/tokens/tokens.py">delete</a>(token_id) -> <a href="./src/cloudflare/types/user/token_delete_response.py">Optional</a></code>
- <code title="get /user/tokens/{token_id}">client.user.tokens.<a href="./src/cloudflare/resources/user/tokens/tokens.py">get</a>(token_id) -> <a href="./src/cloudflare/types/user/token_get_response.py">TokenGetResponse</a></code>
- <code title="get /user/tokens/verify">client.user.tokens.<a href="./src/cloudflare/resources/user/tokens/tokens.py">verify</a>() -> <a href="./src/cloudflare/types/user/token_verify_response.py">TokenVerifyResponse</a></code>

### PermissionGroups

Types:

```python
from cloudflare.types.user.tokens import PermissionGroupListResponse
```

Methods:

- <code title="get /user/tokens/permission_groups">client.user.tokens.permission_groups.<a href="./src/cloudflare/resources/user/tokens/permission_groups.py">list</a>() -> <a href="./src/cloudflare/types/user/tokens/permission_group_list_response.py">Optional</a></code>

### Value

Types:

```python
from cloudflare.types.user.tokens import ValueUpdateResponse
```

Methods:

- <code title="put /user/tokens/{token_id}/value">client.user.tokens.value.<a href="./src/cloudflare/resources/user/tokens/value.py">update</a>(token_id, \*\*<a href="src/cloudflare/types/user/tokens/value_update_params.py">params</a>) -> <a href="./src/cloudflare/types/user/tokens/value_update_response.py">str</a></code>

# Zones

Types:

```python
from cloudflare.types import (
    ZoneCreateResponse,
    ZoneListResponse,
    ZoneDeleteResponse,
    ZoneEditResponse,
    ZoneGetResponse,
)
```

Methods:

- <code title="post /zones">client.zones.<a href="./src/cloudflare/resources/zones/zones.py">create</a>(\*\*<a href="src/cloudflare/types/zone_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zone_create_response.py">Optional</a></code>
- <code title="get /zones">client.zones.<a href="./src/cloudflare/resources/zones/zones.py">list</a>(\*\*<a href="src/cloudflare/types/zone_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zone_list_response.py">SyncV4PagePaginationArray[ZoneListResponse]</a></code>
- <code title="delete /zones/{zone_id}">client.zones.<a href="./src/cloudflare/resources/zones/zones.py">delete</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zone_delete_response.py">Optional</a></code>
- <code title="patch /zones/{zone_id}">client.zones.<a href="./src/cloudflare/resources/zones/zones.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zone_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zone_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}">client.zones.<a href="./src/cloudflare/resources/zones/zones.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zone_get_response.py">Optional</a></code>

## ActivationCheck

Types:

```python
from cloudflare.types.zones import ActivationCheckTriggerResponse
```

Methods:

- <code title="put /zones/{zone_id}/activation_check">client.zones.activation_check.<a href="./src/cloudflare/resources/zones/activation_check.py">trigger</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/activation_check_trigger_response.py">ActivationCheckTriggerResponse</a></code>

## Settings

Types:

```python
from cloudflare.types.zones import SettingListResponse, SettingEditResponse
```

Methods:

- <code title="get /zones/{zone_id}/settings">client.zones.settings.<a href="./src/cloudflare/resources/zones/settings/settings.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/setting_list_response.py">Optional</a></code>
- <code title="patch /zones/{zone_id}/settings">client.zones.settings.<a href="./src/cloudflare/resources/zones/settings/settings.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/setting_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/setting_edit_response.py">Optional</a></code>

### ZeroRTT

Types:

```python
from cloudflare.types.zones.settings import ZeroRTTEditResponse, ZeroRTTGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/0rtt">client.zones.settings.zero_rtt.<a href="./src/cloudflare/resources/zones/settings/zero_rtt.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/zero_rtt_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/zero_rtt_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/0rtt">client.zones.settings.zero_rtt.<a href="./src/cloudflare/resources/zones/settings/zero_rtt.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/zero_rtt_get_response.py">Optional</a></code>

### AdvancedDDOS

Types:

```python
from cloudflare.types.zones.settings import AdvancedDDOSGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/settings/advanced_ddos">client.zones.settings.advanced_ddos.<a href="./src/cloudflare/resources/zones/settings/advanced_ddos.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/advanced_ddos_get_response.py">Optional</a></code>

### AlwaysOnline

Types:

```python
from cloudflare.types.zones.settings import AlwaysOnlineEditResponse, AlwaysOnlineGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/always_online">client.zones.settings.always_online.<a href="./src/cloudflare/resources/zones/settings/always_online.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/always_online_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/always_online_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/always_online">client.zones.settings.always_online.<a href="./src/cloudflare/resources/zones/settings/always_online.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/always_online_get_response.py">Optional</a></code>

### AlwaysUseHTTPS

Types:

```python
from cloudflare.types.zones.settings import AlwaysUseHTTPSEditResponse, AlwaysUseHTTPSGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/always_use_https">client.zones.settings.always_use_https.<a href="./src/cloudflare/resources/zones/settings/always_use_https.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/always_use_https_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/always_use_https_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/always_use_https">client.zones.settings.always_use_https.<a href="./src/cloudflare/resources/zones/settings/always_use_https.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/always_use_https_get_response.py">Optional</a></code>

### AutomaticHTTPSRewrites

Types:

```python
from cloudflare.types.zones.settings import (
    AutomaticHTTPSRewriteEditResponse,
    AutomaticHTTPSRewriteGetResponse,
)
```

Methods:

- <code title="patch /zones/{zone_id}/settings/automatic_https_rewrites">client.zones.settings.automatic_https_rewrites.<a href="./src/cloudflare/resources/zones/settings/automatic_https_rewrites.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/automatic_https_rewrite_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/automatic_https_rewrite_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/automatic_https_rewrites">client.zones.settings.automatic_https_rewrites.<a href="./src/cloudflare/resources/zones/settings/automatic_https_rewrites.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/automatic_https_rewrite_get_response.py">Optional</a></code>

### AutomaticPlatformOptimization

Types:

```python
from cloudflare.types.zones.settings import (
    AutomaticPlatformOptimizationEditResponse,
    AutomaticPlatformOptimizationGetResponse,
)
```

Methods:

- <code title="patch /zones/{zone_id}/settings/automatic_platform_optimization">client.zones.settings.automatic_platform_optimization.<a href="./src/cloudflare/resources/zones/settings/automatic_platform_optimization.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/automatic_platform_optimization_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/automatic_platform_optimization_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/automatic_platform_optimization">client.zones.settings.automatic_platform_optimization.<a href="./src/cloudflare/resources/zones/settings/automatic_platform_optimization.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/automatic_platform_optimization_get_response.py">Optional</a></code>

### Brotli

Types:

```python
from cloudflare.types.zones.settings import BrotliEditResponse, BrotliGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/brotli">client.zones.settings.brotli.<a href="./src/cloudflare/resources/zones/settings/brotli.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/brotli_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/brotli_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/brotli">client.zones.settings.brotli.<a href="./src/cloudflare/resources/zones/settings/brotli.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/brotli_get_response.py">Optional</a></code>

### BrowserCacheTTL

Types:

```python
from cloudflare.types.zones.settings import BrowserCacheTTLEditResponse, BrowserCacheTTLGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/browser_cache_ttl">client.zones.settings.browser_cache_ttl.<a href="./src/cloudflare/resources/zones/settings/browser_cache_ttl.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/browser_cache_ttl_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/browser_cache_ttl_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/browser_cache_ttl">client.zones.settings.browser_cache_ttl.<a href="./src/cloudflare/resources/zones/settings/browser_cache_ttl.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/browser_cache_ttl_get_response.py">Optional</a></code>

### BrowserCheck

Types:

```python
from cloudflare.types.zones.settings import BrowserCheckEditResponse, BrowserCheckGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/browser_check">client.zones.settings.browser_check.<a href="./src/cloudflare/resources/zones/settings/browser_check.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/browser_check_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/browser_check_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/browser_check">client.zones.settings.browser_check.<a href="./src/cloudflare/resources/zones/settings/browser_check.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/browser_check_get_response.py">Optional</a></code>

### CacheLevel

Types:

```python
from cloudflare.types.zones.settings import CacheLevelEditResponse, CacheLevelGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/cache_level">client.zones.settings.cache_level.<a href="./src/cloudflare/resources/zones/settings/cache_level.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/cache_level_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/cache_level_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/cache_level">client.zones.settings.cache_level.<a href="./src/cloudflare/resources/zones/settings/cache_level.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/cache_level_get_response.py">Optional</a></code>

### ChallengeTTL

Types:

```python
from cloudflare.types.zones.settings import ChallengeTTLEditResponse, ChallengeTTLGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/challenge_ttl">client.zones.settings.challenge_ttl.<a href="./src/cloudflare/resources/zones/settings/challenge_ttl.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/challenge_ttl_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/challenge_ttl_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/challenge_ttl">client.zones.settings.challenge_ttl.<a href="./src/cloudflare/resources/zones/settings/challenge_ttl.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/challenge_ttl_get_response.py">Optional</a></code>

### Ciphers

Types:

```python
from cloudflare.types.zones.settings import CipherEditResponse, CipherGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/ciphers">client.zones.settings.ciphers.<a href="./src/cloudflare/resources/zones/settings/ciphers.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/cipher_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/cipher_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/ciphers">client.zones.settings.ciphers.<a href="./src/cloudflare/resources/zones/settings/ciphers.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/cipher_get_response.py">Optional</a></code>

### DevelopmentMode

Types:

```python
from cloudflare.types.zones.settings import DevelopmentModeEditResponse, DevelopmentModeGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/development_mode">client.zones.settings.development_mode.<a href="./src/cloudflare/resources/zones/settings/development_mode.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/development_mode_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/development_mode_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/development_mode">client.zones.settings.development_mode.<a href="./src/cloudflare/resources/zones/settings/development_mode.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/development_mode_get_response.py">Optional</a></code>

### EarlyHints

Types:

```python
from cloudflare.types.zones.settings import EarlyHintEditResponse, EarlyHintGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/early_hints">client.zones.settings.early_hints.<a href="./src/cloudflare/resources/zones/settings/early_hints.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/early_hint_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/early_hint_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/early_hints">client.zones.settings.early_hints.<a href="./src/cloudflare/resources/zones/settings/early_hints.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/early_hint_get_response.py">Optional</a></code>

### EmailObfuscation

Types:

```python
from cloudflare.types.zones.settings import (
    EmailObfuscationEditResponse,
    EmailObfuscationGetResponse,
)
```

Methods:

- <code title="patch /zones/{zone_id}/settings/email_obfuscation">client.zones.settings.email_obfuscation.<a href="./src/cloudflare/resources/zones/settings/email_obfuscation.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/email_obfuscation_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/email_obfuscation_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/email_obfuscation">client.zones.settings.email_obfuscation.<a href="./src/cloudflare/resources/zones/settings/email_obfuscation.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/email_obfuscation_get_response.py">Optional</a></code>

### H2Prioritization

Types:

```python
from cloudflare.types.zones.settings import (
    H2PrioritizationEditResponse,
    H2PrioritizationGetResponse,
)
```

Methods:

- <code title="patch /zones/{zone_id}/settings/h2_prioritization">client.zones.settings.h2_prioritization.<a href="./src/cloudflare/resources/zones/settings/h2_prioritization.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/h2_prioritization_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/h2_prioritization_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/h2_prioritization">client.zones.settings.h2_prioritization.<a href="./src/cloudflare/resources/zones/settings/h2_prioritization.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/h2_prioritization_get_response.py">Optional</a></code>

### HotlinkProtection

Types:

```python
from cloudflare.types.zones.settings import (
    HotlinkProtectionEditResponse,
    HotlinkProtectionGetResponse,
)
```

Methods:

- <code title="patch /zones/{zone_id}/settings/hotlink_protection">client.zones.settings.hotlink_protection.<a href="./src/cloudflare/resources/zones/settings/hotlink_protection.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/hotlink_protection_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/hotlink_protection_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/hotlink_protection">client.zones.settings.hotlink_protection.<a href="./src/cloudflare/resources/zones/settings/hotlink_protection.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/hotlink_protection_get_response.py">Optional</a></code>

### HTTP2

Types:

```python
from cloudflare.types.zones.settings import HTTP2EditResponse, HTTP2GetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/http2">client.zones.settings.http2.<a href="./src/cloudflare/resources/zones/settings/http2.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/http2_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/http2_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/http2">client.zones.settings.http2.<a href="./src/cloudflare/resources/zones/settings/http2.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/http2_get_response.py">Optional</a></code>

### HTTP3

Types:

```python
from cloudflare.types.zones.settings import HTTP3EditResponse, HTTP3GetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/http3">client.zones.settings.http3.<a href="./src/cloudflare/resources/zones/settings/http3.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/http3_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/http3_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/http3">client.zones.settings.http3.<a href="./src/cloudflare/resources/zones/settings/http3.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/http3_get_response.py">Optional</a></code>

### ImageResizing

Types:

```python
from cloudflare.types.zones.settings import ImageResizingEditResponse, ImageResizingGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/image_resizing">client.zones.settings.image_resizing.<a href="./src/cloudflare/resources/zones/settings/image_resizing.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/image_resizing_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/image_resizing_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/image_resizing">client.zones.settings.image_resizing.<a href="./src/cloudflare/resources/zones/settings/image_resizing.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/image_resizing_get_response.py">Optional</a></code>

### IPGeolocation

Types:

```python
from cloudflare.types.zones.settings import IPGeolocationEditResponse, IPGeolocationGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/ip_geolocation">client.zones.settings.ip_geolocation.<a href="./src/cloudflare/resources/zones/settings/ip_geolocation.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/ip_geolocation_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/ip_geolocation_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/ip_geolocation">client.zones.settings.ip_geolocation.<a href="./src/cloudflare/resources/zones/settings/ip_geolocation.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/ip_geolocation_get_response.py">Optional</a></code>

### IPV6

Types:

```python
from cloudflare.types.zones.settings import IPV6EditResponse, IPV6GetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/ipv6">client.zones.settings.ipv6.<a href="./src/cloudflare/resources/zones/settings/ipv6.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/ipv6_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/ipv6_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/ipv6">client.zones.settings.ipv6.<a href="./src/cloudflare/resources/zones/settings/ipv6.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/ipv6_get_response.py">Optional</a></code>

### MinTLSVersion

Types:

```python
from cloudflare.types.zones.settings import MinTLSVersionEditResponse, MinTLSVersionGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/min_tls_version">client.zones.settings.min_tls_version.<a href="./src/cloudflare/resources/zones/settings/min_tls_version.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/min_tls_version_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/min_tls_version_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/min_tls_version">client.zones.settings.min_tls_version.<a href="./src/cloudflare/resources/zones/settings/min_tls_version.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/min_tls_version_get_response.py">Optional</a></code>

### Minify

Types:

```python
from cloudflare.types.zones.settings import MinifyEditResponse, MinifyGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/minify">client.zones.settings.minify.<a href="./src/cloudflare/resources/zones/settings/minify.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/minify_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/minify_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/minify">client.zones.settings.minify.<a href="./src/cloudflare/resources/zones/settings/minify.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/minify_get_response.py">Optional</a></code>

### Mirage

Types:

```python
from cloudflare.types.zones.settings import MirageEditResponse, MirageGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/mirage">client.zones.settings.mirage.<a href="./src/cloudflare/resources/zones/settings/mirage.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/mirage_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/mirage_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/mirage">client.zones.settings.mirage.<a href="./src/cloudflare/resources/zones/settings/mirage.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/mirage_get_response.py">Optional</a></code>

### MobileRedirect

Types:

```python
from cloudflare.types.zones.settings import MobileRedirectEditResponse, MobileRedirectGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/mobile_redirect">client.zones.settings.mobile_redirect.<a href="./src/cloudflare/resources/zones/settings/mobile_redirect.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/mobile_redirect_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/mobile_redirect_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/mobile_redirect">client.zones.settings.mobile_redirect.<a href="./src/cloudflare/resources/zones/settings/mobile_redirect.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/mobile_redirect_get_response.py">Optional</a></code>

### NEL

Types:

```python
from cloudflare.types.zones.settings import NELEditResponse, NELGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/nel">client.zones.settings.nel.<a href="./src/cloudflare/resources/zones/settings/nel.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/nel_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/nel_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/nel">client.zones.settings.nel.<a href="./src/cloudflare/resources/zones/settings/nel.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/nel_get_response.py">Optional</a></code>

### OpportunisticEncryption

Types:

```python
from cloudflare.types.zones.settings import (
    OpportunisticEncryptionEditResponse,
    OpportunisticEncryptionGetResponse,
)
```

Methods:

- <code title="patch /zones/{zone_id}/settings/opportunistic_encryption">client.zones.settings.opportunistic_encryption.<a href="./src/cloudflare/resources/zones/settings/opportunistic_encryption.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/opportunistic_encryption_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/opportunistic_encryption_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/opportunistic_encryption">client.zones.settings.opportunistic_encryption.<a href="./src/cloudflare/resources/zones/settings/opportunistic_encryption.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/opportunistic_encryption_get_response.py">Optional</a></code>

### OpportunisticOnion

Types:

```python
from cloudflare.types.zones.settings import (
    OpportunisticOnionEditResponse,
    OpportunisticOnionGetResponse,
)
```

Methods:

- <code title="patch /zones/{zone_id}/settings/opportunistic_onion">client.zones.settings.opportunistic_onion.<a href="./src/cloudflare/resources/zones/settings/opportunistic_onion.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/opportunistic_onion_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/opportunistic_onion_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/opportunistic_onion">client.zones.settings.opportunistic_onion.<a href="./src/cloudflare/resources/zones/settings/opportunistic_onion.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/opportunistic_onion_get_response.py">Optional</a></code>

### OrangeToOrange

Types:

```python
from cloudflare.types.zones.settings import OrangeToOrangeEditResponse, OrangeToOrangeGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/orange_to_orange">client.zones.settings.orange_to_orange.<a href="./src/cloudflare/resources/zones/settings/orange_to_orange.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/orange_to_orange_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/orange_to_orange_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/orange_to_orange">client.zones.settings.orange_to_orange.<a href="./src/cloudflare/resources/zones/settings/orange_to_orange.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/orange_to_orange_get_response.py">Optional</a></code>

### OriginErrorPagePassThru

Types:

```python
from cloudflare.types.zones.settings import (
    OriginErrorPagePassThruEditResponse,
    OriginErrorPagePassThruGetResponse,
)
```

Methods:

- <code title="patch /zones/{zone_id}/settings/origin_error_page_pass_thru">client.zones.settings.origin_error_page_pass_thru.<a href="./src/cloudflare/resources/zones/settings/origin_error_page_pass_thru.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/origin_error_page_pass_thru_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/origin_error_page_pass_thru_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/origin_error_page_pass_thru">client.zones.settings.origin_error_page_pass_thru.<a href="./src/cloudflare/resources/zones/settings/origin_error_page_pass_thru.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/origin_error_page_pass_thru_get_response.py">Optional</a></code>

### OriginMaxHTTPVersion

Types:

```python
from cloudflare.types.zones.settings import (
    OriginMaxHTTPVersionEditResponse,
    OriginMaxHTTPVersionGetResponse,
)
```

Methods:

- <code title="patch /zones/{zone_id}/settings/origin_max_http_version">client.zones.settings.origin_max_http_version.<a href="./src/cloudflare/resources/zones/settings/origin_max_http_version.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/origin_max_http_version_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/origin_max_http_version_edit_response.py">OriginMaxHTTPVersionEditResponse</a></code>
- <code title="get /zones/{zone_id}/settings/origin_max_http_version">client.zones.settings.origin_max_http_version.<a href="./src/cloudflare/resources/zones/settings/origin_max_http_version.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/origin_max_http_version_get_response.py">OriginMaxHTTPVersionGetResponse</a></code>

### Polish

Types:

```python
from cloudflare.types.zones.settings import PolishEditResponse, PolishGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/polish">client.zones.settings.polish.<a href="./src/cloudflare/resources/zones/settings/polish.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/polish_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/polish_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/polish">client.zones.settings.polish.<a href="./src/cloudflare/resources/zones/settings/polish.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/polish_get_response.py">Optional</a></code>

### PrefetchPreload

Types:

```python
from cloudflare.types.zones.settings import PrefetchPreloadEditResponse, PrefetchPreloadGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/prefetch_preload">client.zones.settings.prefetch_preload.<a href="./src/cloudflare/resources/zones/settings/prefetch_preload.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/prefetch_preload_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/prefetch_preload_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/prefetch_preload">client.zones.settings.prefetch_preload.<a href="./src/cloudflare/resources/zones/settings/prefetch_preload.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/prefetch_preload_get_response.py">Optional</a></code>

### ProxyReadTimeout

Types:

```python
from cloudflare.types.zones.settings import (
    ProxyReadTimeoutEditResponse,
    ProxyReadTimeoutGetResponse,
)
```

Methods:

- <code title="patch /zones/{zone_id}/settings/proxy_read_timeout">client.zones.settings.proxy_read_timeout.<a href="./src/cloudflare/resources/zones/settings/proxy_read_timeout.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/proxy_read_timeout_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/proxy_read_timeout_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/proxy_read_timeout">client.zones.settings.proxy_read_timeout.<a href="./src/cloudflare/resources/zones/settings/proxy_read_timeout.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/proxy_read_timeout_get_response.py">Optional</a></code>

### PseudoIPV4

Types:

```python
from cloudflare.types.zones.settings import PseudoIPV4EditResponse, PseudoIPV4GetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/pseudo_ipv4">client.zones.settings.pseudo_ipv4.<a href="./src/cloudflare/resources/zones/settings/pseudo_ipv4.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/pseudo_ipv4_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/pseudo_ipv4_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/pseudo_ipv4">client.zones.settings.pseudo_ipv4.<a href="./src/cloudflare/resources/zones/settings/pseudo_ipv4.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/pseudo_ipv4_get_response.py">Optional</a></code>

### ResponseBuffering

Types:

```python
from cloudflare.types.zones.settings import (
    ResponseBufferingEditResponse,
    ResponseBufferingGetResponse,
)
```

Methods:

- <code title="patch /zones/{zone_id}/settings/response_buffering">client.zones.settings.response_buffering.<a href="./src/cloudflare/resources/zones/settings/response_buffering.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/response_buffering_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/response_buffering_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/response_buffering">client.zones.settings.response_buffering.<a href="./src/cloudflare/resources/zones/settings/response_buffering.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/response_buffering_get_response.py">Optional</a></code>

### RocketLoader

Types:

```python
from cloudflare.types.zones.settings import RocketLoaderEditResponse, RocketLoaderGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/rocket_loader">client.zones.settings.rocket_loader.<a href="./src/cloudflare/resources/zones/settings/rocket_loader.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/rocket_loader_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/rocket_loader_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/rocket_loader">client.zones.settings.rocket_loader.<a href="./src/cloudflare/resources/zones/settings/rocket_loader.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/rocket_loader_get_response.py">Optional</a></code>

### SecurityHeaders

Types:

```python
from cloudflare.types.zones.settings import SecurityHeaderEditResponse, SecurityHeaderGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/security_header">client.zones.settings.security_headers.<a href="./src/cloudflare/resources/zones/settings/security_headers.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/security_header_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/security_header_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/security_header">client.zones.settings.security_headers.<a href="./src/cloudflare/resources/zones/settings/security_headers.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/security_header_get_response.py">Optional</a></code>

### SecurityLevel

Types:

```python
from cloudflare.types.zones.settings import SecurityLevelEditResponse, SecurityLevelGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/security_level">client.zones.settings.security_level.<a href="./src/cloudflare/resources/zones/settings/security_level.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/security_level_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/security_level_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/security_level">client.zones.settings.security_level.<a href="./src/cloudflare/resources/zones/settings/security_level.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/security_level_get_response.py">Optional</a></code>

### ServerSideExcludes

Types:

```python
from cloudflare.types.zones.settings import (
    ServerSideExcludeEditResponse,
    ServerSideExcludeGetResponse,
)
```

Methods:

- <code title="patch /zones/{zone_id}/settings/server_side_exclude">client.zones.settings.server_side_excludes.<a href="./src/cloudflare/resources/zones/settings/server_side_excludes.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/server_side_exclude_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/server_side_exclude_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/server_side_exclude">client.zones.settings.server_side_excludes.<a href="./src/cloudflare/resources/zones/settings/server_side_excludes.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/server_side_exclude_get_response.py">Optional</a></code>

### SortQueryStringForCache

Types:

```python
from cloudflare.types.zones.settings import (
    SortQueryStringForCacheEditResponse,
    SortQueryStringForCacheGetResponse,
)
```

Methods:

- <code title="patch /zones/{zone_id}/settings/sort_query_string_for_cache">client.zones.settings.sort_query_string_for_cache.<a href="./src/cloudflare/resources/zones/settings/sort_query_string_for_cache.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/sort_query_string_for_cache_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/sort_query_string_for_cache_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/sort_query_string_for_cache">client.zones.settings.sort_query_string_for_cache.<a href="./src/cloudflare/resources/zones/settings/sort_query_string_for_cache.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/sort_query_string_for_cache_get_response.py">Optional</a></code>

### SSL

Types:

```python
from cloudflare.types.zones.settings import SSLEditResponse, SSLGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/ssl">client.zones.settings.ssl.<a href="./src/cloudflare/resources/zones/settings/ssl.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/ssl_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/ssl_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/ssl">client.zones.settings.ssl.<a href="./src/cloudflare/resources/zones/settings/ssl.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/ssl_get_response.py">Optional</a></code>

### SSLRecommender

Types:

```python
from cloudflare.types.zones.settings import SSLRecommenderEditResponse, SSLRecommenderGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/ssl_recommender">client.zones.settings.ssl_recommender.<a href="./src/cloudflare/resources/zones/settings/ssl_recommender.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/ssl_recommender_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/ssl_recommender_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/ssl_recommender">client.zones.settings.ssl_recommender.<a href="./src/cloudflare/resources/zones/settings/ssl_recommender.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/ssl_recommender_get_response.py">Optional</a></code>

### TLS1_3

Types:

```python
from cloudflare.types.zones.settings import TLS1_3EditResponse, TLS1_3GetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/tls_1_3">client.zones.settings.tls_1_3.<a href="./src/cloudflare/resources/zones/settings/tls_1_3.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/tls_1_3_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/tls_1_3_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/tls_1_3">client.zones.settings.tls_1_3.<a href="./src/cloudflare/resources/zones/settings/tls_1_3.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/tls_1_3_get_response.py">Optional</a></code>

### TLSClientAuth

Types:

```python
from cloudflare.types.zones.settings import TLSClientAuthEditResponse, TLSClientAuthGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/tls_client_auth">client.zones.settings.tls_client_auth.<a href="./src/cloudflare/resources/zones/settings/tls_client_auth.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/tls_client_auth_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/tls_client_auth_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/tls_client_auth">client.zones.settings.tls_client_auth.<a href="./src/cloudflare/resources/zones/settings/tls_client_auth.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/tls_client_auth_get_response.py">Optional</a></code>

### TrueClientIPHeader

Types:

```python
from cloudflare.types.zones.settings import (
    TrueClientIPHeaderEditResponse,
    TrueClientIPHeaderGetResponse,
)
```

Methods:

- <code title="patch /zones/{zone_id}/settings/true_client_ip_header">client.zones.settings.true_client_ip_header.<a href="./src/cloudflare/resources/zones/settings/true_client_ip_header.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/true_client_ip_header_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/true_client_ip_header_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/true_client_ip_header">client.zones.settings.true_client_ip_header.<a href="./src/cloudflare/resources/zones/settings/true_client_ip_header.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/true_client_ip_header_get_response.py">Optional</a></code>

### WAF

Types:

```python
from cloudflare.types.zones.settings import WAFEditResponse, WAFGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/waf">client.zones.settings.waf.<a href="./src/cloudflare/resources/zones/settings/waf.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/waf_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/waf_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/waf">client.zones.settings.waf.<a href="./src/cloudflare/resources/zones/settings/waf.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/waf_get_response.py">Optional</a></code>

### Webp

Types:

```python
from cloudflare.types.zones.settings import WebpEditResponse, WebpGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/webp">client.zones.settings.webp.<a href="./src/cloudflare/resources/zones/settings/webp.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/webp_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/webp_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/webp">client.zones.settings.webp.<a href="./src/cloudflare/resources/zones/settings/webp.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/webp_get_response.py">Optional</a></code>

### Websocket

Types:

```python
from cloudflare.types.zones.settings import WebsocketEditResponse, WebsocketGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/websockets">client.zones.settings.websocket.<a href="./src/cloudflare/resources/zones/settings/websocket.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/websocket_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/websocket_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/websockets">client.zones.settings.websocket.<a href="./src/cloudflare/resources/zones/settings/websocket.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/websocket_get_response.py">Optional</a></code>

### FontSettings

Types:

```python
from cloudflare.types.zones.settings import FontSettingEditResponse, FontSettingGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/fonts">client.zones.settings.font_settings.<a href="./src/cloudflare/resources/zones/settings/font_settings.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/settings/font_setting_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/settings/font_setting_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/fonts">client.zones.settings.font_settings.<a href="./src/cloudflare/resources/zones/settings/font_settings.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/settings/font_setting_get_response.py">Optional</a></code>

## CustomNameservers

Types:

```python
from cloudflare.types.zones import CustomNameserverUpdateResponse, CustomNameserverGetResponse
```

Methods:

- <code title="put /zones/{zone_id}/custom_ns">client.zones.custom_nameservers.<a href="./src/cloudflare/resources/zones/custom_nameservers.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/custom_nameserver_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/custom_nameserver_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/custom_ns">client.zones.custom_nameservers.<a href="./src/cloudflare/resources/zones/custom_nameservers.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/custom_nameserver_get_response.py">Optional</a></code>

## Holds

Types:

```python
from cloudflare.types.zones import HoldCreateResponse, HoldDeleteResponse, HoldGetResponse
```

Methods:

- <code title="post /zones/{zone_id}/hold">client.zones.holds.<a href="./src/cloudflare/resources/zones/holds.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/hold_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/hold_create_response.py">HoldCreateResponse</a></code>
- <code title="delete /zones/{zone_id}/hold">client.zones.holds.<a href="./src/cloudflare/resources/zones/holds.py">delete</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/hold_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/hold_delete_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/hold">client.zones.holds.<a href="./src/cloudflare/resources/zones/holds.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/hold_get_response.py">HoldGetResponse</a></code>

## Workers

### Script

Types:

```python
from cloudflare.types.zones.workers import ScriptUpdateResponse
```

Methods:

- <code title="put /zones/{zone_id}/workers/script">client.zones.workers.script.<a href="./src/cloudflare/resources/zones/workers/script.py">update</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/workers/script_update_response.py">ScriptUpdateResponse</a></code>
- <code title="delete /zones/{zone_id}/workers/script">client.zones.workers.script.<a href="./src/cloudflare/resources/zones/workers/script.py">delete</a>(\*, zone_id) -> None</code>
- <code title="get /zones/{zone_id}/workers/script">client.zones.workers.script.<a href="./src/cloudflare/resources/zones/workers/script.py">get</a>(\*, zone_id) -> BinaryAPIResponse</code>

## Subscriptions

Types:

```python
from cloudflare.types.zones import (
    SubscriptionCreateResponse,
    SubscriptionListResponse,
    SubscriptionGetResponse,
)
```

Methods:

- <code title="post /zones/{identifier}/subscription">client.zones.subscriptions.<a href="./src/cloudflare/resources/zones/subscriptions.py">create</a>(identifier, \*\*<a href="src/cloudflare/types/zones/subscription_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/subscription_create_response.py">SubscriptionCreateResponse</a></code>
- <code title="get /accounts/{account_identifier}/subscriptions">client.zones.subscriptions.<a href="./src/cloudflare/resources/zones/subscriptions.py">list</a>(account_identifier) -> <a href="./src/cloudflare/types/zones/subscription_list_response.py">Optional</a></code>
- <code title="get /zones/{identifier}/subscription">client.zones.subscriptions.<a href="./src/cloudflare/resources/zones/subscriptions.py">get</a>(identifier) -> <a href="./src/cloudflare/types/zones/subscription_get_response.py">SubscriptionGetResponse</a></code>

# LoadBalancers

Types:

```python
from cloudflare.types import (
    LoadBalancerCreateResponse,
    LoadBalancerUpdateResponse,
    LoadBalancerListResponse,
    LoadBalancerDeleteResponse,
    LoadBalancerEditResponse,
    LoadBalancerGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/load_balancers">client.load_balancers.<a href="./src/cloudflare/resources/load_balancers/load_balancers.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/load_balancer_create_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancer_create_response.py">LoadBalancerCreateResponse</a></code>
- <code title="put /zones/{zone_id}/load_balancers/{load_balancer_id}">client.load_balancers.<a href="./src/cloudflare/resources/load_balancers/load_balancers.py">update</a>(load_balancer_id, \*, zone_id, \*\*<a href="src/cloudflare/types/load_balancer_update_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancer_update_response.py">LoadBalancerUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/load_balancers">client.load_balancers.<a href="./src/cloudflare/resources/load_balancers/load_balancers.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/load_balancer_list_response.py">Optional</a></code>
- <code title="delete /zones/{zone_id}/load_balancers/{load_balancer_id}">client.load_balancers.<a href="./src/cloudflare/resources/load_balancers/load_balancers.py">delete</a>(load_balancer_id, \*, zone_id) -> <a href="./src/cloudflare/types/load_balancer_delete_response.py">LoadBalancerDeleteResponse</a></code>
- <code title="patch /zones/{zone_id}/load_balancers/{load_balancer_id}">client.load_balancers.<a href="./src/cloudflare/resources/load_balancers/load_balancers.py">edit</a>(load_balancer_id, \*, zone_id, \*\*<a href="src/cloudflare/types/load_balancer_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancer_edit_response.py">LoadBalancerEditResponse</a></code>
- <code title="get /zones/{zone_id}/load_balancers/{load_balancer_id}">client.load_balancers.<a href="./src/cloudflare/resources/load_balancers/load_balancers.py">get</a>(load_balancer_id, \*, zone_id) -> <a href="./src/cloudflare/types/load_balancer_get_response.py">LoadBalancerGetResponse</a></code>

## Monitors

Types:

```python
from cloudflare.types.load_balancers import (
    MonitorCreateResponse,
    MonitorUpdateResponse,
    MonitorListResponse,
    MonitorDeleteResponse,
    MonitorEditResponse,
    MonitorGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/load_balancers/monitors">client.load_balancers.monitors.<a href="./src/cloudflare/resources/load_balancers/monitors/monitors.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/load_balancers/monitor_create_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancers/monitor_create_response.py">MonitorCreateResponse</a></code>
- <code title="put /accounts/{account_id}/load_balancers/monitors/{monitor_id}">client.load_balancers.monitors.<a href="./src/cloudflare/resources/load_balancers/monitors/monitors.py">update</a>(monitor_id, \*, account_id, \*\*<a href="src/cloudflare/types/load_balancers/monitor_update_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancers/monitor_update_response.py">MonitorUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/load_balancers/monitors">client.load_balancers.monitors.<a href="./src/cloudflare/resources/load_balancers/monitors/monitors.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/load_balancers/monitor_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/load_balancers/monitors/{monitor_id}">client.load_balancers.monitors.<a href="./src/cloudflare/resources/load_balancers/monitors/monitors.py">delete</a>(monitor_id, \*, account_id) -> <a href="./src/cloudflare/types/load_balancers/monitor_delete_response.py">MonitorDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/load_balancers/monitors/{monitor_id}">client.load_balancers.monitors.<a href="./src/cloudflare/resources/load_balancers/monitors/monitors.py">edit</a>(monitor_id, \*, account_id, \*\*<a href="src/cloudflare/types/load_balancers/monitor_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancers/monitor_edit_response.py">MonitorEditResponse</a></code>
- <code title="get /accounts/{account_id}/load_balancers/monitors/{monitor_id}">client.load_balancers.monitors.<a href="./src/cloudflare/resources/load_balancers/monitors/monitors.py">get</a>(monitor_id, \*, account_id) -> <a href="./src/cloudflare/types/load_balancers/monitor_get_response.py">MonitorGetResponse</a></code>

### Previews

Types:

```python
from cloudflare.types.load_balancers.monitors import PreviewCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/load_balancers/monitors/{monitor_id}/preview">client.load_balancers.monitors.previews.<a href="./src/cloudflare/resources/load_balancers/monitors/previews.py">create</a>(monitor_id, \*, account_id, \*\*<a href="src/cloudflare/types/load_balancers/monitors/preview_create_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancers/monitors/preview_create_response.py">PreviewCreateResponse</a></code>

### References

Types:

```python
from cloudflare.types.load_balancers.monitors import ReferenceListResponse
```

Methods:

- <code title="get /accounts/{account_id}/load_balancers/monitors/{monitor_id}/references">client.load_balancers.monitors.references.<a href="./src/cloudflare/resources/load_balancers/monitors/references.py">list</a>(monitor_id, \*, account_id) -> <a href="./src/cloudflare/types/load_balancers/monitors/reference_list_response.py">Optional</a></code>

## Pools

Types:

```python
from cloudflare.types.load_balancers import (
    PoolCreateResponse,
    PoolUpdateResponse,
    PoolListResponse,
    PoolDeleteResponse,
    PoolEditResponse,
    PoolGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/load_balancers/pools">client.load_balancers.pools.<a href="./src/cloudflare/resources/load_balancers/pools/pools.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/load_balancers/pool_create_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancers/pool_create_response.py">PoolCreateResponse</a></code>
- <code title="put /accounts/{account_id}/load_balancers/pools/{pool_id}">client.load_balancers.pools.<a href="./src/cloudflare/resources/load_balancers/pools/pools.py">update</a>(pool_id, \*, account_id, \*\*<a href="src/cloudflare/types/load_balancers/pool_update_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancers/pool_update_response.py">PoolUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/load_balancers/pools">client.load_balancers.pools.<a href="./src/cloudflare/resources/load_balancers/pools/pools.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/load_balancers/pool_list_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancers/pool_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/load_balancers/pools/{pool_id}">client.load_balancers.pools.<a href="./src/cloudflare/resources/load_balancers/pools/pools.py">delete</a>(pool_id, \*, account_id) -> <a href="./src/cloudflare/types/load_balancers/pool_delete_response.py">PoolDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/load_balancers/pools/{pool_id}">client.load_balancers.pools.<a href="./src/cloudflare/resources/load_balancers/pools/pools.py">edit</a>(pool_id, \*, account_id, \*\*<a href="src/cloudflare/types/load_balancers/pool_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancers/pool_edit_response.py">PoolEditResponse</a></code>
- <code title="get /accounts/{account_id}/load_balancers/pools/{pool_id}">client.load_balancers.pools.<a href="./src/cloudflare/resources/load_balancers/pools/pools.py">get</a>(pool_id, \*, account_id) -> <a href="./src/cloudflare/types/load_balancers/pool_get_response.py">PoolGetResponse</a></code>

### Health

Types:

```python
from cloudflare.types.load_balancers.pools import HealthCreateResponse, HealthGetResponse
```

Methods:

- <code title="post /accounts/{account_id}/load_balancers/pools/{pool_id}/preview">client.load_balancers.pools.health.<a href="./src/cloudflare/resources/load_balancers/pools/health.py">create</a>(pool_id, \*, account_id, \*\*<a href="src/cloudflare/types/load_balancers/pools/health_create_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancers/pools/health_create_response.py">HealthCreateResponse</a></code>
- <code title="get /accounts/{account_id}/load_balancers/pools/{pool_id}/health">client.load_balancers.pools.health.<a href="./src/cloudflare/resources/load_balancers/pools/health.py">get</a>(pool_id, \*, account_id) -> <a href="./src/cloudflare/types/load_balancers/pools/health_get_response.py">HealthGetResponse</a></code>

### References

Types:

```python
from cloudflare.types.load_balancers.pools import ReferenceListResponse
```

Methods:

- <code title="get /accounts/{account_id}/load_balancers/pools/{pool_id}/references">client.load_balancers.pools.references.<a href="./src/cloudflare/resources/load_balancers/pools/references.py">list</a>(pool_id, \*, account_id) -> <a href="./src/cloudflare/types/load_balancers/pools/reference_list_response.py">Optional</a></code>

## Previews

Types:

```python
from cloudflare.types.load_balancers import PreviewGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/load_balancers/preview/{preview_id}">client.load_balancers.previews.<a href="./src/cloudflare/resources/load_balancers/previews.py">get</a>(preview_id, \*, account_id) -> <a href="./src/cloudflare/types/load_balancers/preview_get_response.py">PreviewGetResponse</a></code>

## Regions

Types:

```python
from cloudflare.types.load_balancers import RegionListResponse, RegionGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/load_balancers/regions">client.load_balancers.regions.<a href="./src/cloudflare/resources/load_balancers/regions.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/load_balancers/region_list_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancers/region_list_response.py">RegionListResponse</a></code>
- <code title="get /accounts/{account_id}/load_balancers/regions/{region_id}">client.load_balancers.regions.<a href="./src/cloudflare/resources/load_balancers/regions.py">get</a>(region_id, \*, account_id) -> <a href="./src/cloudflare/types/load_balancers/region_get_response.py">RegionGetResponse</a></code>

## Searches

Types:

```python
from cloudflare.types.load_balancers import SearchListResponse
```

Methods:

- <code title="get /accounts/{account_id}/load_balancers/search">client.load_balancers.searches.<a href="./src/cloudflare/resources/load_balancers/searches.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/load_balancers/search_list_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancers/search_list_response.py">Optional</a></code>

# Cache

Types:

```python
from cloudflare.types import CachePurgeResponse
```

Methods:

- <code title="post /zones/{zone_id}/purge_cache">client.cache.<a href="./src/cloudflare/resources/cache/cache.py">purge</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/cache_purge_params.py">params</a>) -> <a href="./src/cloudflare/types/cache_purge_response.py">Optional</a></code>

## CacheReserve

Types:

```python
from cloudflare.types.cache import (
    CacheReserveListResponse,
    CacheReserveClearResponse,
    CacheReserveEditResponse,
    CacheReserveStatusResponse,
)
```

Methods:

- <code title="get /zones/{zone_id}/cache/cache_reserve">client.cache.cache_reserve.<a href="./src/cloudflare/resources/cache/cache_reserve.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/cache/cache_reserve_list_response.py">CacheReserveListResponse</a></code>
- <code title="post /zones/{zone_id}/cache/cache_reserve_clear">client.cache.cache_reserve.<a href="./src/cloudflare/resources/cache/cache_reserve.py">clear</a>(\*, zone_id) -> <a href="./src/cloudflare/types/cache/cache_reserve_clear_response.py">CacheReserveClearResponse</a></code>
- <code title="patch /zones/{zone_id}/cache/cache_reserve">client.cache.cache_reserve.<a href="./src/cloudflare/resources/cache/cache_reserve.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/cache/cache_reserve_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/cache/cache_reserve_edit_response.py">CacheReserveEditResponse</a></code>
- <code title="get /zones/{zone_id}/cache/cache_reserve_clear">client.cache.cache_reserve.<a href="./src/cloudflare/resources/cache/cache_reserve.py">status</a>(\*, zone_id) -> <a href="./src/cloudflare/types/cache/cache_reserve_status_response.py">CacheReserveStatusResponse</a></code>

## TieredCacheSmartTopology

Types:

```python
from cloudflare.types.cache import (
    TieredCacheSmartTopologyDeleteResponse,
    TieredCacheSmartTopologyEditResponse,
    TieredCacheSmartTopologyGetResponse,
)
```

Methods:

- <code title="delete /zones/{zone_id}/cache/tiered_cache_smart_topology_enable">client.cache.tiered_cache_smart_topology.<a href="./src/cloudflare/resources/cache/tiered_cache_smart_topology.py">delete</a>(\*, zone_id) -> <a href="./src/cloudflare/types/cache/tiered_cache_smart_topology_delete_response.py">TieredCacheSmartTopologyDeleteResponse</a></code>
- <code title="patch /zones/{zone_id}/cache/tiered_cache_smart_topology_enable">client.cache.tiered_cache_smart_topology.<a href="./src/cloudflare/resources/cache/tiered_cache_smart_topology.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/cache/tiered_cache_smart_topology_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/cache/tiered_cache_smart_topology_edit_response.py">TieredCacheSmartTopologyEditResponse</a></code>
- <code title="get /zones/{zone_id}/cache/tiered_cache_smart_topology_enable">client.cache.tiered_cache_smart_topology.<a href="./src/cloudflare/resources/cache/tiered_cache_smart_topology.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/cache/tiered_cache_smart_topology_get_response.py">TieredCacheSmartTopologyGetResponse</a></code>

## Variants

Types:

```python
from cloudflare.types.cache import VariantListResponse, VariantDeleteResponse, VariantEditResponse
```

Methods:

- <code title="get /zones/{zone_id}/cache/variants">client.cache.variants.<a href="./src/cloudflare/resources/cache/variants.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/cache/variant_list_response.py">VariantListResponse</a></code>
- <code title="delete /zones/{zone_id}/cache/variants">client.cache.variants.<a href="./src/cloudflare/resources/cache/variants.py">delete</a>(\*, zone_id) -> <a href="./src/cloudflare/types/cache/variant_delete_response.py">VariantDeleteResponse</a></code>
- <code title="patch /zones/{zone_id}/cache/variants">client.cache.variants.<a href="./src/cloudflare/resources/cache/variants.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/cache/variant_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/cache/variant_edit_response.py">VariantEditResponse</a></code>

## RegionalTieredCache

Types:

```python
from cloudflare.types.cache import RegionalTieredCacheEditResponse, RegionalTieredCacheGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/cache/regional_tiered_cache">client.cache.regional_tiered_cache.<a href="./src/cloudflare/resources/cache/regional_tiered_cache.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/cache/regional_tiered_cache_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/cache/regional_tiered_cache_edit_response.py">RegionalTieredCacheEditResponse</a></code>
- <code title="get /zones/{zone_id}/cache/regional_tiered_cache">client.cache.regional_tiered_cache.<a href="./src/cloudflare/resources/cache/regional_tiered_cache.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/cache/regional_tiered_cache_get_response.py">RegionalTieredCacheGetResponse</a></code>

# SSL

## Analyze

Types:

```python
from cloudflare.types.ssl import AnalyzeCreateResponse
```

Methods:

- <code title="post /zones/{zone_id}/ssl/analyze">client.ssl.analyze.<a href="./src/cloudflare/resources/ssl/analyze.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/ssl/analyze_create_params.py">params</a>) -> <a href="./src/cloudflare/types/ssl/analyze_create_response.py">AnalyzeCreateResponse</a></code>

## CertificatePacks

Types:

```python
from cloudflare.types.ssl import (
    CertificatePackListResponse,
    CertificatePackDeleteResponse,
    CertificatePackEditResponse,
    CertificatePackGetResponse,
)
```

Methods:

- <code title="get /zones/{zone_id}/ssl/certificate_packs">client.ssl.certificate_packs.<a href="./src/cloudflare/resources/ssl/certificate_packs/certificate_packs.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/ssl/certificate_pack_list_params.py">params</a>) -> <a href="./src/cloudflare/types/ssl/certificate_pack_list_response.py">Optional</a></code>
- <code title="delete /zones/{zone_id}/ssl/certificate_packs/{certificate_pack_id}">client.ssl.certificate_packs.<a href="./src/cloudflare/resources/ssl/certificate_packs/certificate_packs.py">delete</a>(certificate_pack_id, \*, zone_id) -> <a href="./src/cloudflare/types/ssl/certificate_pack_delete_response.py">CertificatePackDeleteResponse</a></code>
- <code title="patch /zones/{zone_id}/ssl/certificate_packs/{certificate_pack_id}">client.ssl.certificate_packs.<a href="./src/cloudflare/resources/ssl/certificate_packs/certificate_packs.py">edit</a>(certificate_pack_id, \*, zone_id) -> <a href="./src/cloudflare/types/ssl/certificate_pack_edit_response.py">CertificatePackEditResponse</a></code>
- <code title="get /zones/{zone_id}/ssl/certificate_packs/{certificate_pack_id}">client.ssl.certificate_packs.<a href="./src/cloudflare/resources/ssl/certificate_packs/certificate_packs.py">get</a>(certificate_pack_id, \*, zone_id) -> <a href="./src/cloudflare/types/ssl/certificate_pack_get_response.py">CertificatePackGetResponse</a></code>

### Order

Types:

```python
from cloudflare.types.ssl.certificate_packs import OrderCreateResponse
```

Methods:

- <code title="post /zones/{zone_id}/ssl/certificate_packs/order">client.ssl.certificate_packs.order.<a href="./src/cloudflare/resources/ssl/certificate_packs/order.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/ssl/certificate_packs/order_create_params.py">params</a>) -> <a href="./src/cloudflare/types/ssl/certificate_packs/order_create_response.py">OrderCreateResponse</a></code>

### Quota

Types:

```python
from cloudflare.types.ssl.certificate_packs import QuotaListResponse
```

Methods:

- <code title="get /zones/{zone_id}/ssl/certificate_packs/quota">client.ssl.certificate_packs.quota.<a href="./src/cloudflare/resources/ssl/certificate_packs/quota.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/ssl/certificate_packs/quota_list_response.py">QuotaListResponse</a></code>

## Recommendations

Types:

```python
from cloudflare.types.ssl import RecommendationListResponse
```

Methods:

- <code title="get /zones/{zone_identifier}/ssl/recommendation">client.ssl.recommendations.<a href="./src/cloudflare/resources/ssl/recommendations.py">list</a>(zone_identifier) -> <a href="./src/cloudflare/types/ssl/recommendation_list_response.py">Optional</a></code>

## Universal

### Settings

Types:

```python
from cloudflare.types.ssl.universal import SettingEditResponse, SettingGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/ssl/universal/settings">client.ssl.universal.settings.<a href="./src/cloudflare/resources/ssl/universal/settings.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/ssl/universal/setting_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/ssl/universal/setting_edit_response.py">SettingEditResponse</a></code>
- <code title="get /zones/{zone_id}/ssl/universal/settings">client.ssl.universal.settings.<a href="./src/cloudflare/resources/ssl/universal/settings.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/ssl/universal/setting_get_response.py">SettingGetResponse</a></code>

## Verification

Types:

```python
from cloudflare.types.ssl import VerificationListResponse, VerificationEditResponse
```

Methods:

- <code title="get /zones/{zone_id}/ssl/verification">client.ssl.verification.<a href="./src/cloudflare/resources/ssl/verification.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/ssl/verification_list_params.py">params</a>) -> <a href="./src/cloudflare/types/ssl/verification_list_response.py">Optional</a></code>
- <code title="patch /zones/{zone_id}/ssl/verification/{certificate_pack_id}">client.ssl.verification.<a href="./src/cloudflare/resources/ssl/verification.py">edit</a>(certificate_pack_id, \*, zone_id, \*\*<a href="src/cloudflare/types/ssl/verification_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/ssl/verification_edit_response.py">VerificationEditResponse</a></code>

# Subscriptions

Types:

```python
from cloudflare.types import (
    SubscriptionCreateResponse,
    SubscriptionUpdateResponse,
    SubscriptionListResponse,
    SubscriptionDeleteResponse,
    SubscriptionGetResponse,
)
```

Methods:

- <code title="post /zones/{identifier}/subscription">client.subscriptions.<a href="./src/cloudflare/resources/subscriptions.py">create</a>(identifier, \*\*<a href="src/cloudflare/types/subscription_create_params.py">params</a>) -> <a href="./src/cloudflare/types/subscription_create_response.py">SubscriptionCreateResponse</a></code>
- <code title="put /accounts/{account_identifier}/subscriptions/{subscription_identifier}">client.subscriptions.<a href="./src/cloudflare/resources/subscriptions.py">update</a>(subscription_identifier, \*, account_identifier, \*\*<a href="src/cloudflare/types/subscription_update_params.py">params</a>) -> <a href="./src/cloudflare/types/subscription_update_response.py">SubscriptionUpdateResponse</a></code>
- <code title="get /accounts/{account_identifier}/subscriptions">client.subscriptions.<a href="./src/cloudflare/resources/subscriptions.py">list</a>(account_identifier) -> <a href="./src/cloudflare/types/subscription_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_identifier}/subscriptions/{subscription_identifier}">client.subscriptions.<a href="./src/cloudflare/resources/subscriptions.py">delete</a>(subscription_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/subscription_delete_response.py">SubscriptionDeleteResponse</a></code>
- <code title="get /zones/{identifier}/subscription">client.subscriptions.<a href="./src/cloudflare/resources/subscriptions.py">get</a>(identifier) -> <a href="./src/cloudflare/types/subscription_get_response.py">SubscriptionGetResponse</a></code>

# ACM

## TotalTLS

Types:

```python
from cloudflare.types.acm import TotalTLSCreateResponse, TotalTLSGetResponse
```

Methods:

- <code title="post /zones/{zone_id}/acm/total_tls">client.acm.total_tls.<a href="./src/cloudflare/resources/acm/total_tls.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/acm/total_tls_create_params.py">params</a>) -> <a href="./src/cloudflare/types/acm/total_tls_create_response.py">TotalTLSCreateResponse</a></code>
- <code title="get /zones/{zone_id}/acm/total_tls">client.acm.total_tls.<a href="./src/cloudflare/resources/acm/total_tls.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/acm/total_tls_get_response.py">TotalTLSGetResponse</a></code>

# Argo

## SmartRouting

Types:

```python
from cloudflare.types.argo import SmartRoutingEditResponse, SmartRoutingGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/argo/smart_routing">client.argo.smart_routing.<a href="./src/cloudflare/resources/argo/smart_routing.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/argo/smart_routing_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/argo/smart_routing_edit_response.py">SmartRoutingEditResponse</a></code>
- <code title="get /zones/{zone_id}/argo/smart_routing">client.argo.smart_routing.<a href="./src/cloudflare/resources/argo/smart_routing.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/argo/smart_routing_get_response.py">SmartRoutingGetResponse</a></code>

## TieredCaching

Types:

```python
from cloudflare.types.argo import TieredCachingEditResponse, TieredCachingGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/argo/tiered_caching">client.argo.tiered_caching.<a href="./src/cloudflare/resources/argo/tiered_caching.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/argo/tiered_caching_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/argo/tiered_caching_edit_response.py">TieredCachingEditResponse</a></code>
- <code title="get /zones/{zone_id}/argo/tiered_caching">client.argo.tiered_caching.<a href="./src/cloudflare/resources/argo/tiered_caching.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/argo/tiered_caching_get_response.py">TieredCachingGetResponse</a></code>

# AvailablePlans

Types:

```python
from cloudflare.types import AvailablePlanListResponse, AvailablePlanGetResponse
```

Methods:

- <code title="get /zones/{zone_identifier}/available_plans">client.available_plans.<a href="./src/cloudflare/resources/available_plans.py">list</a>(zone_identifier) -> <a href="./src/cloudflare/types/available_plan_list_response.py">Optional</a></code>
- <code title="get /zones/{zone_identifier}/available_plans/{plan_identifier}">client.available_plans.<a href="./src/cloudflare/resources/available_plans.py">get</a>(plan_identifier, \*, zone_identifier) -> <a href="./src/cloudflare/types/available_plan_get_response.py">AvailablePlanGetResponse</a></code>

# AvailableRatePlans

Types:

```python
from cloudflare.types import AvailableRatePlanListResponse
```

Methods:

- <code title="get /zones/{zone_identifier}/available_rate_plans">client.available_rate_plans.<a href="./src/cloudflare/resources/available_rate_plans.py">list</a>(zone_identifier) -> <a href="./src/cloudflare/types/available_rate_plan_list_response.py">Optional</a></code>

# CertificateAuthorities

## HostnameAssociations

Types:

```python
from cloudflare.types.certificate_authorities import (
    HostnameAssociationUpdateResponse,
    HostnameAssociationListResponse,
)
```

Methods:

- <code title="put /zones/{zone_id}/certificate_authorities/hostname_associations">client.certificate_authorities.hostname_associations.<a href="./src/cloudflare/resources/certificate_authorities/hostname_associations.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/certificate_authorities/hostname_association_update_params.py">params</a>) -> <a href="./src/cloudflare/types/certificate_authorities/hostname_association_update_response.py">HostnameAssociationUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/certificate_authorities/hostname_associations">client.certificate_authorities.hostname_associations.<a href="./src/cloudflare/resources/certificate_authorities/hostname_associations.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/certificate_authorities/hostname_association_list_params.py">params</a>) -> <a href="./src/cloudflare/types/certificate_authorities/hostname_association_list_response.py">HostnameAssociationListResponse</a></code>

# ClientCertificates

Types:

```python
from cloudflare.types import (
    ClientCertificateCreateResponse,
    ClientCertificateListResponse,
    ClientCertificateDeleteResponse,
    ClientCertificateEditResponse,
    ClientCertificateGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/client_certificates">client.client_certificates.<a href="./src/cloudflare/resources/client_certificates.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/client_certificate_create_params.py">params</a>) -> <a href="./src/cloudflare/types/client_certificate_create_response.py">ClientCertificateCreateResponse</a></code>
- <code title="get /zones/{zone_id}/client_certificates">client.client_certificates.<a href="./src/cloudflare/resources/client_certificates.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/client_certificate_list_params.py">params</a>) -> <a href="./src/cloudflare/types/client_certificate_list_response.py">SyncV4PagePaginationArray[ClientCertificateListResponse]</a></code>
- <code title="delete /zones/{zone_id}/client_certificates/{client_certificate_id}">client.client_certificates.<a href="./src/cloudflare/resources/client_certificates.py">delete</a>(client_certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/client_certificate_delete_response.py">ClientCertificateDeleteResponse</a></code>
- <code title="patch /zones/{zone_id}/client_certificates/{client_certificate_id}">client.client_certificates.<a href="./src/cloudflare/resources/client_certificates.py">edit</a>(client_certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/client_certificate_edit_response.py">ClientCertificateEditResponse</a></code>
- <code title="get /zones/{zone_id}/client_certificates/{client_certificate_id}">client.client_certificates.<a href="./src/cloudflare/resources/client_certificates.py">get</a>(client_certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/client_certificate_get_response.py">ClientCertificateGetResponse</a></code>

# CustomCertificates

Types:

```python
from cloudflare.types import (
    CustomCertificateCreateResponse,
    CustomCertificateListResponse,
    CustomCertificateDeleteResponse,
    CustomCertificateEditResponse,
    CustomCertificateGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/custom_certificates">client.custom_certificates.<a href="./src/cloudflare/resources/custom_certificates/custom_certificates.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/custom_certificate_create_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_certificate_create_response.py">CustomCertificateCreateResponse</a></code>
- <code title="get /zones/{zone_id}/custom_certificates">client.custom_certificates.<a href="./src/cloudflare/resources/custom_certificates/custom_certificates.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/custom_certificate_list_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_certificate_list_response.py">SyncV4PagePaginationArray[CustomCertificateListResponse]</a></code>
- <code title="delete /zones/{zone_id}/custom_certificates/{custom_certificate_id}">client.custom_certificates.<a href="./src/cloudflare/resources/custom_certificates/custom_certificates.py">delete</a>(custom_certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/custom_certificate_delete_response.py">CustomCertificateDeleteResponse</a></code>
- <code title="patch /zones/{zone_id}/custom_certificates/{custom_certificate_id}">client.custom_certificates.<a href="./src/cloudflare/resources/custom_certificates/custom_certificates.py">edit</a>(custom_certificate_id, \*, zone_id, \*\*<a href="src/cloudflare/types/custom_certificate_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_certificate_edit_response.py">CustomCertificateEditResponse</a></code>
- <code title="get /zones/{zone_id}/custom_certificates/{custom_certificate_id}">client.custom_certificates.<a href="./src/cloudflare/resources/custom_certificates/custom_certificates.py">get</a>(custom_certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/custom_certificate_get_response.py">CustomCertificateGetResponse</a></code>

## Prioritize

Types:

```python
from cloudflare.types.custom_certificates import PrioritizeUpdateResponse
```

Methods:

- <code title="put /zones/{zone_id}/custom_certificates/prioritize">client.custom_certificates.prioritize.<a href="./src/cloudflare/resources/custom_certificates/prioritize.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/custom_certificates/prioritize_update_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_certificates/prioritize_update_response.py">Optional</a></code>

# CustomHostnames

Types:

```python
from cloudflare.types import (
    CustomHostnameCreateResponse,
    CustomHostnameListResponse,
    CustomHostnameDeleteResponse,
    CustomHostnameEditResponse,
    CustomHostnameGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/custom_hostnames">client.custom_hostnames.<a href="./src/cloudflare/resources/custom_hostnames/custom_hostnames.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/custom_hostname_create_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_hostname_create_response.py">CustomHostnameCreateResponse</a></code>
- <code title="get /zones/{zone_id}/custom_hostnames">client.custom_hostnames.<a href="./src/cloudflare/resources/custom_hostnames/custom_hostnames.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/custom_hostname_list_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_hostname_list_response.py">SyncV4PagePaginationArray[CustomHostnameListResponse]</a></code>
- <code title="delete /zones/{zone_id}/custom_hostnames/{custom_hostname_id}">client.custom_hostnames.<a href="./src/cloudflare/resources/custom_hostnames/custom_hostnames.py">delete</a>(custom_hostname_id, \*, zone_id) -> <a href="./src/cloudflare/types/custom_hostname_delete_response.py">CustomHostnameDeleteResponse</a></code>
- <code title="patch /zones/{zone_id}/custom_hostnames/{custom_hostname_id}">client.custom_hostnames.<a href="./src/cloudflare/resources/custom_hostnames/custom_hostnames.py">edit</a>(custom_hostname_id, \*, zone_id, \*\*<a href="src/cloudflare/types/custom_hostname_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_hostname_edit_response.py">CustomHostnameEditResponse</a></code>
- <code title="get /zones/{zone_id}/custom_hostnames/{custom_hostname_id}">client.custom_hostnames.<a href="./src/cloudflare/resources/custom_hostnames/custom_hostnames.py">get</a>(custom_hostname_id, \*, zone_id) -> <a href="./src/cloudflare/types/custom_hostname_get_response.py">CustomHostnameGetResponse</a></code>

## FallbackOrigin

Types:

```python
from cloudflare.types.custom_hostnames import (
    FallbackOriginUpdateResponse,
    FallbackOriginDeleteResponse,
    FallbackOriginGetResponse,
)
```

Methods:

- <code title="put /zones/{zone_id}/custom_hostnames/fallback_origin">client.custom_hostnames.fallback_origin.<a href="./src/cloudflare/resources/custom_hostnames/fallback_origin.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/custom_hostnames/fallback_origin_update_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_hostnames/fallback_origin_update_response.py">FallbackOriginUpdateResponse</a></code>
- <code title="delete /zones/{zone_id}/custom_hostnames/fallback_origin">client.custom_hostnames.fallback_origin.<a href="./src/cloudflare/resources/custom_hostnames/fallback_origin.py">delete</a>(\*, zone_id) -> <a href="./src/cloudflare/types/custom_hostnames/fallback_origin_delete_response.py">FallbackOriginDeleteResponse</a></code>
- <code title="get /zones/{zone_id}/custom_hostnames/fallback_origin">client.custom_hostnames.fallback_origin.<a href="./src/cloudflare/resources/custom_hostnames/fallback_origin.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/custom_hostnames/fallback_origin_get_response.py">FallbackOriginGetResponse</a></code>

# CustomNameservers

Types:

```python
from cloudflare.types import (
    CustomNameserverCreateResponse,
    CustomNameserverListResponse,
    CustomNameserverDeleteResponse,
    CustomNameserverAvailabiltyResponse,
    CustomNameserverVerifyResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/custom_ns">client.custom_nameservers.<a href="./src/cloudflare/resources/custom_nameservers.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/custom_nameserver_create_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_nameserver_create_response.py">CustomNameserverCreateResponse</a></code>
- <code title="get /accounts/{account_id}/custom_ns">client.custom_nameservers.<a href="./src/cloudflare/resources/custom_nameservers.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/custom_nameserver_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/custom_ns/{custom_ns_id}">client.custom_nameservers.<a href="./src/cloudflare/resources/custom_nameservers.py">delete</a>(custom_ns_id, \*, account_id) -> <a href="./src/cloudflare/types/custom_nameserver_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/custom_ns/availability">client.custom_nameservers.<a href="./src/cloudflare/resources/custom_nameservers.py">availabilty</a>(\*, account_id) -> <a href="./src/cloudflare/types/custom_nameserver_availabilty_response.py">Optional</a></code>
- <code title="post /accounts/{account_id}/custom_ns/verify">client.custom_nameservers.<a href="./src/cloudflare/resources/custom_nameservers.py">verify</a>(\*, account_id) -> <a href="./src/cloudflare/types/custom_nameserver_verify_response.py">Optional</a></code>

# DNS

## Records

Types:

```python
from cloudflare.types.dns import (
    RecordCreateResponse,
    RecordUpdateResponse,
    RecordListResponse,
    RecordDeleteResponse,
    RecordEditResponse,
    RecordExportResponse,
    RecordGetResponse,
    RecordImportResponse,
    RecordScanResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/dns_records">client.dns.records.<a href="./src/cloudflare/resources/dns/records.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/dns/record_create_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/record_create_response.py">RecordCreateResponse</a></code>
- <code title="put /zones/{zone_id}/dns_records/{dns_record_id}">client.dns.records.<a href="./src/cloudflare/resources/dns/records.py">update</a>(dns_record_id, \*, zone_id, \*\*<a href="src/cloudflare/types/dns/record_update_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/record_update_response.py">RecordUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/dns_records">client.dns.records.<a href="./src/cloudflare/resources/dns/records.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/dns/record_list_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/record_list_response.py">SyncV4PagePaginationArray[RecordListResponse]</a></code>
- <code title="delete /zones/{zone_id}/dns_records/{dns_record_id}">client.dns.records.<a href="./src/cloudflare/resources/dns/records.py">delete</a>(dns_record_id, \*, zone_id) -> <a href="./src/cloudflare/types/dns/record_delete_response.py">Optional</a></code>
- <code title="patch /zones/{zone_id}/dns_records/{dns_record_id}">client.dns.records.<a href="./src/cloudflare/resources/dns/records.py">edit</a>(dns_record_id, \*, zone_id, \*\*<a href="src/cloudflare/types/dns/record_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/record_edit_response.py">RecordEditResponse</a></code>
- <code title="get /zones/{zone_id}/dns_records/export">client.dns.records.<a href="./src/cloudflare/resources/dns/records.py">export</a>(\*, zone_id) -> str</code>
- <code title="get /zones/{zone_id}/dns_records/{dns_record_id}">client.dns.records.<a href="./src/cloudflare/resources/dns/records.py">get</a>(dns_record_id, \*, zone_id) -> <a href="./src/cloudflare/types/dns/record_get_response.py">RecordGetResponse</a></code>
- <code title="post /zones/{zone_id}/dns_records/import">client.dns.records.<a href="./src/cloudflare/resources/dns/records.py">import\_</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/dns/record_import_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/record_import_response.py">RecordImportResponse</a></code>
- <code title="post /zones/{zone_id}/dns_records/scan">client.dns.records.<a href="./src/cloudflare/resources/dns/records.py">scan</a>(\*, zone_id) -> <a href="./src/cloudflare/types/dns/record_scan_response.py">RecordScanResponse</a></code>

## Analytics

### Reports

Types:

```python
from cloudflare.types.dns.analytics import ReportListResponse
```

Methods:

- <code title="get /zones/{identifier}/dns_analytics/report">client.dns.analytics.reports.<a href="./src/cloudflare/resources/dns/analytics/reports/reports.py">list</a>(identifier, \*\*<a href="src/cloudflare/types/dns/analytics/report_list_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/analytics/report_list_response.py">ReportListResponse</a></code>

#### Bytimes

Types:

```python
from cloudflare.types.dns.analytics.reports import BytimeListResponse
```

Methods:

- <code title="get /zones/{identifier}/dns_analytics/report/bytime">client.dns.analytics.reports.bytimes.<a href="./src/cloudflare/resources/dns/analytics/reports/bytimes.py">list</a>(identifier, \*\*<a href="src/cloudflare/types/dns/analytics/reports/bytime_list_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/analytics/reports/bytime_list_response.py">BytimeListResponse</a></code>

## Firewall

Types:

```python
from cloudflare.types.dns import (
    FirewallCreateResponse,
    FirewallListResponse,
    FirewallDeleteResponse,
    FirewallEditResponse,
    FirewallGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/dns_firewall">client.dns.firewall.<a href="./src/cloudflare/resources/dns/firewall/firewall.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/dns/firewall_create_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/firewall_create_response.py">FirewallCreateResponse</a></code>
- <code title="get /accounts/{account_id}/dns_firewall">client.dns.firewall.<a href="./src/cloudflare/resources/dns/firewall/firewall.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/dns/firewall_list_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/firewall_list_response.py">SyncV4PagePaginationArray[FirewallListResponse]</a></code>
- <code title="delete /accounts/{account_id}/dns_firewall/{dns_firewall_id}">client.dns.firewall.<a href="./src/cloudflare/resources/dns/firewall/firewall.py">delete</a>(dns_firewall_id, \*, account_id) -> <a href="./src/cloudflare/types/dns/firewall_delete_response.py">FirewallDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/dns_firewall/{dns_firewall_id}">client.dns.firewall.<a href="./src/cloudflare/resources/dns/firewall/firewall.py">edit</a>(dns_firewall_id, \*, account_id, \*\*<a href="src/cloudflare/types/dns/firewall_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/firewall_edit_response.py">FirewallEditResponse</a></code>
- <code title="get /accounts/{account_id}/dns_firewall/{dns_firewall_id}">client.dns.firewall.<a href="./src/cloudflare/resources/dns/firewall/firewall.py">get</a>(dns_firewall_id, \*, account_id) -> <a href="./src/cloudflare/types/dns/firewall_get_response.py">FirewallGetResponse</a></code>

### Analytics

#### Reports

Types:

```python
from cloudflare.types.dns.firewall.analytics import ReportListResponse
```

Methods:

- <code title="get /accounts/{account_identifier}/dns_firewall/{identifier}/dns_analytics/report">client.dns.firewall.analytics.reports.<a href="./src/cloudflare/resources/dns/firewall/analytics/reports/reports.py">list</a>(identifier, \*, account_identifier, \*\*<a href="src/cloudflare/types/dns/firewall/analytics/report_list_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/firewall/analytics/report_list_response.py">ReportListResponse</a></code>

##### Bytimes

Types:

```python
from cloudflare.types.dns.firewall.analytics.reports import BytimeListResponse
```

Methods:

- <code title="get /accounts/{account_identifier}/dns_firewall/{identifier}/dns_analytics/report/bytime">client.dns.firewall.analytics.reports.bytimes.<a href="./src/cloudflare/resources/dns/firewall/analytics/reports/bytimes.py">list</a>(identifier, \*, account_identifier, \*\*<a href="src/cloudflare/types/dns/firewall/analytics/reports/bytime_list_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/firewall/analytics/reports/bytime_list_response.py">BytimeListResponse</a></code>

# DNSSEC

Types:

```python
from cloudflare.types import DNSSECDeleteResponse, DNSSECEditResponse, DNSSECGetResponse
```

Methods:

- <code title="delete /zones/{zone_id}/dnssec">client.dnssec.<a href="./src/cloudflare/resources/dnssec.py">delete</a>(\*, zone_id) -> <a href="./src/cloudflare/types/dnssec_delete_response.py">DNSSECDeleteResponse</a></code>
- <code title="patch /zones/{zone_id}/dnssec">client.dnssec.<a href="./src/cloudflare/resources/dnssec.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/dnssec_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/dnssec_edit_response.py">DNSSECEditResponse</a></code>
- <code title="get /zones/{zone_id}/dnssec">client.dnssec.<a href="./src/cloudflare/resources/dnssec.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/dnssec_get_response.py">DNSSECGetResponse</a></code>

# Emails

## Routing

Types:

```python
from cloudflare.types.emails import RoutingGetResponse
```

Methods:

- <code title="get /zones/{zone_identifier}/email/routing">client.emails.routing.<a href="./src/cloudflare/resources/emails/routing/routing.py">get</a>(zone_identifier) -> <a href="./src/cloudflare/types/emails/routing_get_response.py">RoutingGetResponse</a></code>

### Disables

Types:

```python
from cloudflare.types.emails.routing import DisableCreateResponse
```

Methods:

- <code title="post /zones/{zone_identifier}/email/routing/disable">client.emails.routing.disables.<a href="./src/cloudflare/resources/emails/routing/disables.py">create</a>(zone_identifier) -> <a href="./src/cloudflare/types/emails/routing/disable_create_response.py">DisableCreateResponse</a></code>

### DNS

Types:

```python
from cloudflare.types.emails.routing import DNSGetResponse
```

Methods:

- <code title="get /zones/{zone_identifier}/email/routing/dns">client.emails.routing.dns.<a href="./src/cloudflare/resources/emails/routing/dns.py">get</a>(zone_identifier) -> <a href="./src/cloudflare/types/emails/routing/dns_get_response.py">Optional</a></code>

### Enables

Types:

```python
from cloudflare.types.emails.routing import EnableCreateResponse
```

Methods:

- <code title="post /zones/{zone_identifier}/email/routing/enable">client.emails.routing.enables.<a href="./src/cloudflare/resources/emails/routing/enables.py">create</a>(zone_identifier) -> <a href="./src/cloudflare/types/emails/routing/enable_create_response.py">EnableCreateResponse</a></code>

### Rules

Types:

```python
from cloudflare.types.emails.routing import (
    RuleCreateResponse,
    RuleUpdateResponse,
    RuleListResponse,
    RuleDeleteResponse,
    RuleGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_identifier}/email/routing/rules">client.emails.routing.rules.<a href="./src/cloudflare/resources/emails/routing/rules/rules.py">create</a>(zone_identifier, \*\*<a href="src/cloudflare/types/emails/routing/rule_create_params.py">params</a>) -> <a href="./src/cloudflare/types/emails/routing/rule_create_response.py">RuleCreateResponse</a></code>
- <code title="put /zones/{zone_identifier}/email/routing/rules/{rule_identifier}">client.emails.routing.rules.<a href="./src/cloudflare/resources/emails/routing/rules/rules.py">update</a>(rule_identifier, \*, zone_identifier, \*\*<a href="src/cloudflare/types/emails/routing/rule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/emails/routing/rule_update_response.py">RuleUpdateResponse</a></code>
- <code title="get /zones/{zone_identifier}/email/routing/rules">client.emails.routing.rules.<a href="./src/cloudflare/resources/emails/routing/rules/rules.py">list</a>(zone_identifier, \*\*<a href="src/cloudflare/types/emails/routing/rule_list_params.py">params</a>) -> <a href="./src/cloudflare/types/emails/routing/rule_list_response.py">SyncV4PagePaginationArray[RuleListResponse]</a></code>
- <code title="delete /zones/{zone_identifier}/email/routing/rules/{rule_identifier}">client.emails.routing.rules.<a href="./src/cloudflare/resources/emails/routing/rules/rules.py">delete</a>(rule_identifier, \*, zone_identifier) -> <a href="./src/cloudflare/types/emails/routing/rule_delete_response.py">RuleDeleteResponse</a></code>
- <code title="get /zones/{zone_identifier}/email/routing/rules/{rule_identifier}">client.emails.routing.rules.<a href="./src/cloudflare/resources/emails/routing/rules/rules.py">get</a>(rule_identifier, \*, zone_identifier) -> <a href="./src/cloudflare/types/emails/routing/rule_get_response.py">RuleGetResponse</a></code>

#### CatchAlls

Types:

```python
from cloudflare.types.emails.routing.rules import CatchAllUpdateResponse, CatchAllGetResponse
```

Methods:

- <code title="put /zones/{zone_identifier}/email/routing/rules/catch_all">client.emails.routing.rules.catch_alls.<a href="./src/cloudflare/resources/emails/routing/rules/catch_alls.py">update</a>(zone_identifier, \*\*<a href="src/cloudflare/types/emails/routing/rules/catch_all_update_params.py">params</a>) -> <a href="./src/cloudflare/types/emails/routing/rules/catch_all_update_response.py">CatchAllUpdateResponse</a></code>
- <code title="get /zones/{zone_identifier}/email/routing/rules/catch_all">client.emails.routing.rules.catch_alls.<a href="./src/cloudflare/resources/emails/routing/rules/catch_alls.py">get</a>(zone_identifier) -> <a href="./src/cloudflare/types/emails/routing/rules/catch_all_get_response.py">CatchAllGetResponse</a></code>

### Addresses

Types:

```python
from cloudflare.types.emails.routing import (
    AddressCreateResponse,
    AddressDeleteResponse,
    AddressEmailRoutingDestinationAddressesListDestinationAddressesResponse,
    AddressGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_identifier}/email/routing/addresses">client.emails.routing.addresses.<a href="./src/cloudflare/resources/emails/routing/addresses.py">create</a>(account_identifier, \*\*<a href="src/cloudflare/types/emails/routing/address_create_params.py">params</a>) -> <a href="./src/cloudflare/types/emails/routing/address_create_response.py">AddressCreateResponse</a></code>
- <code title="delete /accounts/{account_identifier}/email/routing/addresses/{destination_address_identifier}">client.emails.routing.addresses.<a href="./src/cloudflare/resources/emails/routing/addresses.py">delete</a>(destination_address_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/emails/routing/address_delete_response.py">AddressDeleteResponse</a></code>
- <code title="get /accounts/{account_identifier}/email/routing/addresses">client.emails.routing.addresses.<a href="./src/cloudflare/resources/emails/routing/addresses.py">email_routing_destination_addresses_list_destination_addresses</a>(account_identifier, \*\*<a href="src/cloudflare/types/emails/routing/address_email_routing_destination_addresses_list_destination_addresses_params.py">params</a>) -> <a href="./src/cloudflare/types/emails/routing/address_email_routing_destination_addresses_list_destination_addresses_response.py">Optional</a></code>
- <code title="get /accounts/{account_identifier}/email/routing/addresses/{destination_address_identifier}">client.emails.routing.addresses.<a href="./src/cloudflare/resources/emails/routing/addresses.py">get</a>(destination_address_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/emails/routing/address_get_response.py">AddressGetResponse</a></code>

# Filters

Types:

```python
from cloudflare.types import (
    FilterCreateResponse,
    FilterUpdateResponse,
    FilterListResponse,
    FilterDeleteResponse,
    FilterGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_identifier}/filters">client.filters.<a href="./src/cloudflare/resources/filters.py">create</a>(zone_identifier, \*\*<a href="src/cloudflare/types/filter_create_params.py">params</a>) -> <a href="./src/cloudflare/types/filter_create_response.py">Optional</a></code>
- <code title="put /zones/{zone_identifier}/filters/{id}">client.filters.<a href="./src/cloudflare/resources/filters.py">update</a>(id, \*, zone_identifier, \*\*<a href="src/cloudflare/types/filter_update_params.py">params</a>) -> <a href="./src/cloudflare/types/filter_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_identifier}/filters">client.filters.<a href="./src/cloudflare/resources/filters.py">list</a>(zone_identifier, \*\*<a href="src/cloudflare/types/filter_list_params.py">params</a>) -> <a href="./src/cloudflare/types/filter_list_response.py">SyncV4PagePaginationArray[FilterListResponse]</a></code>
- <code title="delete /zones/{zone_identifier}/filters/{id}">client.filters.<a href="./src/cloudflare/resources/filters.py">delete</a>(id, \*, zone_identifier) -> <a href="./src/cloudflare/types/filter_delete_response.py">Optional</a></code>
- <code title="get /zones/{zone_identifier}/filters/{id}">client.filters.<a href="./src/cloudflare/resources/filters.py">get</a>(id, \*, zone_identifier) -> <a href="./src/cloudflare/types/filter_get_response.py">Optional</a></code>

# Firewall

## Lockdowns

Types:

```python
from cloudflare.types.firewall import (
    LockdownCreateResponse,
    LockdownUpdateResponse,
    LockdownListResponse,
    LockdownDeleteResponse,
    LockdownGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_identifier}/firewall/lockdowns">client.firewall.lockdowns.<a href="./src/cloudflare/resources/firewall/lockdowns.py">create</a>(zone_identifier, \*\*<a href="src/cloudflare/types/firewall/lockdown_create_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/lockdown_create_response.py">Optional</a></code>
- <code title="put /zones/{zone_identifier}/firewall/lockdowns/{id}">client.firewall.lockdowns.<a href="./src/cloudflare/resources/firewall/lockdowns.py">update</a>(id, \*, zone_identifier, \*\*<a href="src/cloudflare/types/firewall/lockdown_update_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/lockdown_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_identifier}/firewall/lockdowns">client.firewall.lockdowns.<a href="./src/cloudflare/resources/firewall/lockdowns.py">list</a>(zone_identifier, \*\*<a href="src/cloudflare/types/firewall/lockdown_list_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/lockdown_list_response.py">SyncV4PagePaginationArray[LockdownListResponse]</a></code>
- <code title="delete /zones/{zone_identifier}/firewall/lockdowns/{id}">client.firewall.lockdowns.<a href="./src/cloudflare/resources/firewall/lockdowns.py">delete</a>(id, \*, zone_identifier) -> <a href="./src/cloudflare/types/firewall/lockdown_delete_response.py">Optional</a></code>
- <code title="get /zones/{zone_identifier}/firewall/lockdowns/{id}">client.firewall.lockdowns.<a href="./src/cloudflare/resources/firewall/lockdowns.py">get</a>(id, \*, zone_identifier) -> <a href="./src/cloudflare/types/firewall/lockdown_get_response.py">Optional</a></code>

## Rules

Types:

```python
from cloudflare.types.firewall import (
    RuleCreateResponse,
    RuleUpdateResponse,
    RuleListResponse,
    RuleDeleteResponse,
    RuleEditResponse,
    RuleGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_identifier}/firewall/rules">client.firewall.rules.<a href="./src/cloudflare/resources/firewall/rules.py">create</a>(zone_identifier, \*\*<a href="src/cloudflare/types/firewall/rule_create_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/rule_create_response.py">Optional</a></code>
- <code title="put /zones/{zone_identifier}/firewall/rules/{id}">client.firewall.rules.<a href="./src/cloudflare/resources/firewall/rules.py">update</a>(id, \*, zone_identifier, \*\*<a href="src/cloudflare/types/firewall/rule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/rule_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_identifier}/firewall/rules">client.firewall.rules.<a href="./src/cloudflare/resources/firewall/rules.py">list</a>(zone_identifier, \*\*<a href="src/cloudflare/types/firewall/rule_list_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/rule_list_response.py">SyncV4PagePaginationArray[RuleListResponse]</a></code>
- <code title="delete /zones/{zone_identifier}/firewall/rules/{id}">client.firewall.rules.<a href="./src/cloudflare/resources/firewall/rules.py">delete</a>(id, \*, zone_identifier, \*\*<a href="src/cloudflare/types/firewall/rule_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/rule_delete_response.py">Optional</a></code>
- <code title="patch /zones/{zone_identifier}/firewall/rules/{id}">client.firewall.rules.<a href="./src/cloudflare/resources/firewall/rules.py">edit</a>(id, \*, zone_identifier, \*\*<a href="src/cloudflare/types/firewall/rule_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/rule_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_identifier}/firewall/rules/{id}">client.firewall.rules.<a href="./src/cloudflare/resources/firewall/rules.py">get</a>(id, \*, zone_identifier) -> <a href="./src/cloudflare/types/firewall/rule_get_response.py">Optional</a></code>

## AccessRules

Types:

```python
from cloudflare.types.firewall import (
    AccessRuleCreateResponse,
    AccessRuleListResponse,
    AccessRuleDeleteResponse,
    AccessRuleEditResponse,
    AccessRuleGetResponse,
)
```

Methods:

- <code title="post /{account_or_zone}/{account_or_zone_id}/firewall/access_rules/rules">client.firewall.access_rules.<a href="./src/cloudflare/resources/firewall/access_rules.py">create</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/firewall/access_rule_create_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/access_rule_create_response.py">Optional</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/firewall/access_rules/rules">client.firewall.access_rules.<a href="./src/cloudflare/resources/firewall/access_rules.py">list</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/firewall/access_rule_list_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/access_rule_list_response.py">SyncV4PagePaginationArray[object]</a></code>
- <code title="delete /{account_or_zone}/{account_or_zone_id}/firewall/access_rules/rules/{identifier}">client.firewall.access_rules.<a href="./src/cloudflare/resources/firewall/access_rules.py">delete</a>(identifier, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/firewall/access_rule_delete_response.py">Optional</a></code>
- <code title="patch /{account_or_zone}/{account_or_zone_id}/firewall/access_rules/rules/{identifier}">client.firewall.access_rules.<a href="./src/cloudflare/resources/firewall/access_rules.py">edit</a>(identifier, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/firewall/access_rule_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/access_rule_edit_response.py">Optional</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/firewall/access_rules/rules/{identifier}">client.firewall.access_rules.<a href="./src/cloudflare/resources/firewall/access_rules.py">get</a>(identifier, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/firewall/access_rule_get_response.py">Optional</a></code>

## UARules

Types:

```python
from cloudflare.types.firewall import (
    UARuleCreateResponse,
    UARuleUpdateResponse,
    UARuleListResponse,
    UARuleDeleteResponse,
    UARuleGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_identifier}/firewall/ua_rules">client.firewall.ua_rules.<a href="./src/cloudflare/resources/firewall/ua_rules.py">create</a>(zone_identifier, \*\*<a href="src/cloudflare/types/firewall/ua_rule_create_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/ua_rule_create_response.py">Optional</a></code>
- <code title="put /zones/{zone_identifier}/firewall/ua_rules/{id}">client.firewall.ua_rules.<a href="./src/cloudflare/resources/firewall/ua_rules.py">update</a>(id, \*, zone_identifier, \*\*<a href="src/cloudflare/types/firewall/ua_rule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/ua_rule_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_identifier}/firewall/ua_rules">client.firewall.ua_rules.<a href="./src/cloudflare/resources/firewall/ua_rules.py">list</a>(zone_identifier, \*\*<a href="src/cloudflare/types/firewall/ua_rule_list_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/ua_rule_list_response.py">SyncV4PagePaginationArray[UARuleListResponse]</a></code>
- <code title="delete /zones/{zone_identifier}/firewall/ua_rules/{id}">client.firewall.ua_rules.<a href="./src/cloudflare/resources/firewall/ua_rules.py">delete</a>(id, \*, zone_identifier) -> <a href="./src/cloudflare/types/firewall/ua_rule_delete_response.py">Optional</a></code>
- <code title="get /zones/{zone_identifier}/firewall/ua_rules/{id}">client.firewall.ua_rules.<a href="./src/cloudflare/resources/firewall/ua_rules.py">get</a>(id, \*, zone_identifier) -> <a href="./src/cloudflare/types/firewall/ua_rule_get_response.py">Optional</a></code>

## WAF

### Overrides

Types:

```python
from cloudflare.types.firewall.waf import (
    OverrideCreateResponse,
    OverrideUpdateResponse,
    OverrideListResponse,
    OverrideDeleteResponse,
    OverrideGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_identifier}/firewall/waf/overrides">client.firewall.waf.overrides.<a href="./src/cloudflare/resources/firewall/waf/overrides.py">create</a>(zone_identifier, \*\*<a href="src/cloudflare/types/firewall/waf/override_create_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/waf/override_create_response.py">Optional</a></code>
- <code title="put /zones/{zone_identifier}/firewall/waf/overrides/{id}">client.firewall.waf.overrides.<a href="./src/cloudflare/resources/firewall/waf/overrides.py">update</a>(id, \*, zone_identifier, \*\*<a href="src/cloudflare/types/firewall/waf/override_update_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/waf/override_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_identifier}/firewall/waf/overrides">client.firewall.waf.overrides.<a href="./src/cloudflare/resources/firewall/waf/overrides.py">list</a>(zone_identifier, \*\*<a href="src/cloudflare/types/firewall/waf/override_list_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/waf/override_list_response.py">SyncV4PagePaginationArray[OverrideListResponse]</a></code>
- <code title="delete /zones/{zone_identifier}/firewall/waf/overrides/{id}">client.firewall.waf.overrides.<a href="./src/cloudflare/resources/firewall/waf/overrides.py">delete</a>(id, \*, zone_identifier) -> <a href="./src/cloudflare/types/firewall/waf/override_delete_response.py">Optional</a></code>
- <code title="get /zones/{zone_identifier}/firewall/waf/overrides/{id}">client.firewall.waf.overrides.<a href="./src/cloudflare/resources/firewall/waf/overrides.py">get</a>(id, \*, zone_identifier) -> <a href="./src/cloudflare/types/firewall/waf/override_get_response.py">Optional</a></code>

### Packages

Types:

```python
from cloudflare.types.firewall.waf import PackageListResponse, PackageGetResponse
```

Methods:

- <code title="get /zones/{zone_identifier}/firewall/waf/packages">client.firewall.waf.packages.<a href="./src/cloudflare/resources/firewall/waf/packages/packages.py">list</a>(zone_identifier, \*\*<a href="src/cloudflare/types/firewall/waf/package_list_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/waf/package_list_response.py">SyncV4PagePaginationArray[PackageListResponse]</a></code>
- <code title="get /zones/{zone_identifier}/firewall/waf/packages/{identifier}">client.firewall.waf.packages.<a href="./src/cloudflare/resources/firewall/waf/packages/packages.py">get</a>(identifier, \*, zone_identifier) -> <a href="./src/cloudflare/types/firewall/waf/package_get_response.py">PackageGetResponse</a></code>

#### Groups

Types:

```python
from cloudflare.types.firewall.waf.packages import (
    GroupListResponse,
    GroupEditResponse,
    GroupGetResponse,
)
```

Methods:

- <code title="get /zones/{zone_id}/firewall/waf/packages/{package_id}/groups">client.firewall.waf.packages.groups.<a href="./src/cloudflare/resources/firewall/waf/packages/groups.py">list</a>(package_id, \*, zone_id, \*\*<a href="src/cloudflare/types/firewall/waf/packages/group_list_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/waf/packages/group_list_response.py">SyncV4PagePaginationArray[GroupListResponse]</a></code>
- <code title="patch /zones/{zone_id}/firewall/waf/packages/{package_id}/groups/{group_id}">client.firewall.waf.packages.groups.<a href="./src/cloudflare/resources/firewall/waf/packages/groups.py">edit</a>(group_id, \*, zone_id, package_id, \*\*<a href="src/cloudflare/types/firewall/waf/packages/group_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/waf/packages/group_edit_response.py">GroupEditResponse</a></code>
- <code title="get /zones/{zone_id}/firewall/waf/packages/{package_id}/groups/{group_id}">client.firewall.waf.packages.groups.<a href="./src/cloudflare/resources/firewall/waf/packages/groups.py">get</a>(group_id, \*, zone_id, package_id) -> <a href="./src/cloudflare/types/firewall/waf/packages/group_get_response.py">GroupGetResponse</a></code>

#### Rules

Types:

```python
from cloudflare.types.firewall.waf.packages import (
    RuleListResponse,
    RuleEditResponse,
    RuleGetResponse,
)
```

Methods:

- <code title="get /zones/{zone_id}/firewall/waf/packages/{package_id}/rules">client.firewall.waf.packages.rules.<a href="./src/cloudflare/resources/firewall/waf/packages/rules.py">list</a>(package_id, \*, zone_id, \*\*<a href="src/cloudflare/types/firewall/waf/packages/rule_list_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/waf/packages/rule_list_response.py">SyncV4PagePaginationArray[RuleListResponse]</a></code>
- <code title="patch /zones/{zone_id}/firewall/waf/packages/{package_id}/rules/{rule_id}">client.firewall.waf.packages.rules.<a href="./src/cloudflare/resources/firewall/waf/packages/rules.py">edit</a>(rule_id, \*, zone_id, package_id, \*\*<a href="src/cloudflare/types/firewall/waf/packages/rule_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/waf/packages/rule_edit_response.py">RuleEditResponse</a></code>
- <code title="get /zones/{zone_id}/firewall/waf/packages/{package_id}/rules/{rule_id}">client.firewall.waf.packages.rules.<a href="./src/cloudflare/resources/firewall/waf/packages/rules.py">get</a>(rule_id, \*, zone_id, package_id) -> <a href="./src/cloudflare/types/firewall/waf/packages/rule_get_response.py">RuleGetResponse</a></code>

# Healthchecks

Types:

```python
from cloudflare.types import (
    HealthcheckCreateResponse,
    HealthcheckUpdateResponse,
    HealthcheckListResponse,
    HealthcheckDeleteResponse,
    HealthcheckEditResponse,
    HealthcheckGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_identifier}/healthchecks">client.healthchecks.<a href="./src/cloudflare/resources/healthchecks/healthchecks.py">create</a>(zone_identifier, \*\*<a href="src/cloudflare/types/healthcheck_create_params.py">params</a>) -> <a href="./src/cloudflare/types/healthcheck_create_response.py">HealthcheckCreateResponse</a></code>
- <code title="put /zones/{zone_identifier}/healthchecks/{identifier}">client.healthchecks.<a href="./src/cloudflare/resources/healthchecks/healthchecks.py">update</a>(identifier, \*, zone_identifier, \*\*<a href="src/cloudflare/types/healthcheck_update_params.py">params</a>) -> <a href="./src/cloudflare/types/healthcheck_update_response.py">HealthcheckUpdateResponse</a></code>
- <code title="get /zones/{zone_identifier}/healthchecks">client.healthchecks.<a href="./src/cloudflare/resources/healthchecks/healthchecks.py">list</a>(zone_identifier) -> <a href="./src/cloudflare/types/healthcheck_list_response.py">Optional</a></code>
- <code title="delete /zones/{zone_identifier}/healthchecks/{identifier}">client.healthchecks.<a href="./src/cloudflare/resources/healthchecks/healthchecks.py">delete</a>(identifier, \*, zone_identifier) -> <a href="./src/cloudflare/types/healthcheck_delete_response.py">HealthcheckDeleteResponse</a></code>
- <code title="patch /zones/{zone_identifier}/healthchecks/{identifier}">client.healthchecks.<a href="./src/cloudflare/resources/healthchecks/healthchecks.py">edit</a>(identifier, \*, zone_identifier, \*\*<a href="src/cloudflare/types/healthcheck_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/healthcheck_edit_response.py">HealthcheckEditResponse</a></code>
- <code title="get /zones/{zone_identifier}/healthchecks/{identifier}">client.healthchecks.<a href="./src/cloudflare/resources/healthchecks/healthchecks.py">get</a>(identifier, \*, zone_identifier) -> <a href="./src/cloudflare/types/healthcheck_get_response.py">HealthcheckGetResponse</a></code>

## Previews

Types:

```python
from cloudflare.types.healthchecks import (
    PreviewCreateResponse,
    PreviewDeleteResponse,
    PreviewGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_identifier}/healthchecks/preview">client.healthchecks.previews.<a href="./src/cloudflare/resources/healthchecks/previews.py">create</a>(zone_identifier, \*\*<a href="src/cloudflare/types/healthchecks/preview_create_params.py">params</a>) -> <a href="./src/cloudflare/types/healthchecks/preview_create_response.py">PreviewCreateResponse</a></code>
- <code title="delete /zones/{zone_identifier}/healthchecks/preview/{identifier}">client.healthchecks.previews.<a href="./src/cloudflare/resources/healthchecks/previews.py">delete</a>(identifier, \*, zone_identifier) -> <a href="./src/cloudflare/types/healthchecks/preview_delete_response.py">PreviewDeleteResponse</a></code>
- <code title="get /zones/{zone_identifier}/healthchecks/preview/{identifier}">client.healthchecks.previews.<a href="./src/cloudflare/resources/healthchecks/previews.py">get</a>(identifier, \*, zone_identifier) -> <a href="./src/cloudflare/types/healthchecks/preview_get_response.py">PreviewGetResponse</a></code>

# KeylessCertificates

Types:

```python
from cloudflare.types import (
    KeylessCertificateCreateResponse,
    KeylessCertificateListResponse,
    KeylessCertificateDeleteResponse,
    KeylessCertificateEditResponse,
    KeylessCertificateGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/keyless_certificates">client.keyless_certificates.<a href="./src/cloudflare/resources/keyless_certificates.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/keyless_certificate_create_params.py">params</a>) -> <a href="./src/cloudflare/types/keyless_certificate_create_response.py">KeylessCertificateCreateResponse</a></code>
- <code title="get /zones/{zone_id}/keyless_certificates">client.keyless_certificates.<a href="./src/cloudflare/resources/keyless_certificates.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/keyless_certificate_list_response.py">Optional</a></code>
- <code title="delete /zones/{zone_id}/keyless_certificates/{keyless_certificate_id}">client.keyless_certificates.<a href="./src/cloudflare/resources/keyless_certificates.py">delete</a>(keyless_certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/keyless_certificate_delete_response.py">KeylessCertificateDeleteResponse</a></code>
- <code title="patch /zones/{zone_id}/keyless_certificates/{keyless_certificate_id}">client.keyless_certificates.<a href="./src/cloudflare/resources/keyless_certificates.py">edit</a>(keyless_certificate_id, \*, zone_id, \*\*<a href="src/cloudflare/types/keyless_certificate_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/keyless_certificate_edit_response.py">KeylessCertificateEditResponse</a></code>
- <code title="get /zones/{zone_id}/keyless_certificates/{keyless_certificate_id}">client.keyless_certificates.<a href="./src/cloudflare/resources/keyless_certificates.py">get</a>(keyless_certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/keyless_certificate_get_response.py">KeylessCertificateGetResponse</a></code>

# Logpush

## Datasets

### Fields

Types:

```python
from cloudflare.types.logpush.datasets import FieldListResponse
```

Methods:

- <code title="get /{account_or_zone}/{account_or_zone_id}/logpush/datasets/{dataset_id}/fields">client.logpush.datasets.fields.<a href="./src/cloudflare/resources/logpush/datasets/fields.py">list</a>(dataset_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/logpush/datasets/field_list_response.py">object</a></code>

### Jobs

Types:

```python
from cloudflare.types.logpush.datasets import JobListResponse
```

Methods:

- <code title="get /{account_or_zone}/{account_or_zone_id}/logpush/datasets/{dataset_id}/jobs">client.logpush.datasets.jobs.<a href="./src/cloudflare/resources/logpush/datasets/jobs.py">list</a>(dataset_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/logpush/datasets/job_list_response.py">JobListResponse</a></code>

## Edge

Types:

```python
from cloudflare.types.logpush import EdgeCreateResponse, EdgeGetResponse
```

Methods:

- <code title="post /zones/{zone_id}/logpush/edge">client.logpush.edge.<a href="./src/cloudflare/resources/logpush/edge.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/logpush/edge_create_params.py">params</a>) -> <a href="./src/cloudflare/types/logpush/edge_create_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/logpush/edge">client.logpush.edge.<a href="./src/cloudflare/resources/logpush/edge.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/logpush/edge_get_response.py">EdgeGetResponse</a></code>

## Jobs

Types:

```python
from cloudflare.types.logpush import (
    JobCreateResponse,
    JobUpdateResponse,
    JobListResponse,
    JobDeleteResponse,
    JobGetResponse,
)
```

Methods:

- <code title="post /{account_or_zone}/{account_or_zone_id}/logpush/jobs">client.logpush.jobs.<a href="./src/cloudflare/resources/logpush/jobs.py">create</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/logpush/job_create_params.py">params</a>) -> <a href="./src/cloudflare/types/logpush/job_create_response.py">Optional</a></code>
- <code title="put /{account_or_zone}/{account_or_zone_id}/logpush/jobs/{job_id}">client.logpush.jobs.<a href="./src/cloudflare/resources/logpush/jobs.py">update</a>(job_id, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/logpush/job_update_params.py">params</a>) -> <a href="./src/cloudflare/types/logpush/job_update_response.py">Optional</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/logpush/jobs">client.logpush.jobs.<a href="./src/cloudflare/resources/logpush/jobs.py">list</a>(\*, account_id, zone_id) -> <a href="./src/cloudflare/types/logpush/job_list_response.py">JobListResponse</a></code>
- <code title="delete /{account_or_zone}/{account_or_zone_id}/logpush/jobs/{job_id}">client.logpush.jobs.<a href="./src/cloudflare/resources/logpush/jobs.py">delete</a>(job_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/logpush/job_delete_response.py">Optional</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/logpush/jobs/{job_id}">client.logpush.jobs.<a href="./src/cloudflare/resources/logpush/jobs.py">get</a>(job_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/logpush/job_get_response.py">Optional</a></code>

## Ownership

Types:

```python
from cloudflare.types.logpush import OwnershipCreateResponse, OwnershipValidateResponse
```

Methods:

- <code title="post /{account_or_zone}/{account_or_zone_id}/logpush/ownership">client.logpush.ownership.<a href="./src/cloudflare/resources/logpush/ownership.py">create</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/logpush/ownership_create_params.py">params</a>) -> <a href="./src/cloudflare/types/logpush/ownership_create_response.py">Optional</a></code>
- <code title="post /{account_or_zone}/{account_or_zone_id}/logpush/ownership/validate">client.logpush.ownership.<a href="./src/cloudflare/resources/logpush/ownership.py">validate</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/logpush/ownership_validate_params.py">params</a>) -> <a href="./src/cloudflare/types/logpush/ownership_validate_response.py">Optional</a></code>

## Validate

Types:

```python
from cloudflare.types.logpush import ValidateDestinationResponse, ValidateOriginResponse
```

Methods:

- <code title="post /{account_or_zone}/{account_or_zone_id}/logpush/validate/destination/exists">client.logpush.validate.<a href="./src/cloudflare/resources/logpush/validate.py">destination</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/logpush/validate_destination_params.py">params</a>) -> <a href="./src/cloudflare/types/logpush/validate_destination_response.py">Optional</a></code>
- <code title="post /{account_or_zone}/{account_or_zone_id}/logpush/validate/origin">client.logpush.validate.<a href="./src/cloudflare/resources/logpush/validate.py">origin</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/logpush/validate_origin_params.py">params</a>) -> <a href="./src/cloudflare/types/logpush/validate_origin_response.py">Optional</a></code>

# Logs

## Controls

### Retentions

#### Flags

Types:

```python
from cloudflare.types.logs.controls.retentions import (
    FlagCreateResponse,
    FlagLogsReceivedGetLogRetentionFlagResponse,
)
```

Methods:

- <code title="post /zones/{zone_identifier}/logs/control/retention/flag">client.logs.controls.retentions.flags.<a href="./src/cloudflare/resources/logs/controls/retentions/flags.py">create</a>(zone_identifier, \*\*<a href="src/cloudflare/types/logs/controls/retentions/flag_create_params.py">params</a>) -> <a href="./src/cloudflare/types/logs/controls/retentions/flag_create_response.py">FlagCreateResponse</a></code>
- <code title="get /zones/{zone_identifier}/logs/control/retention/flag">client.logs.controls.retentions.flags.<a href="./src/cloudflare/resources/logs/controls/retentions/flags.py">logs_received_get_log_retention_flag</a>(zone_identifier) -> <a href="./src/cloudflare/types/logs/controls/retentions/flag_logs_received_get_log_retention_flag_response.py">FlagLogsReceivedGetLogRetentionFlagResponse</a></code>

### Cmb

#### Config

Types:

```python
from cloudflare.types.logs.controls.cmb import (
    ConfigCreateResponse,
    ConfigDeleteResponse,
    ConfigGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/logs/control/cmb/config">client.logs.controls.cmb.config.<a href="./src/cloudflare/resources/logs/controls/cmb/config.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/logs/controls/cmb/config_create_params.py">params</a>) -> <a href="./src/cloudflare/types/logs/controls/cmb/config_create_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/logs/control/cmb/config">client.logs.controls.cmb.config.<a href="./src/cloudflare/resources/logs/controls/cmb/config.py">delete</a>(\*, account_id) -> <a href="./src/cloudflare/types/logs/controls/cmb/config_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/logs/control/cmb/config">client.logs.controls.cmb.config.<a href="./src/cloudflare/resources/logs/controls/cmb/config.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/logs/controls/cmb/config_get_response.py">Optional</a></code>

## Rayids

Types:

```python
from cloudflare.types.logs import RayidGetResponse
```

Methods:

- <code title="get /zones/{zone_identifier}/logs/rayids/{ray_identifier}">client.logs.rayids.<a href="./src/cloudflare/resources/logs/rayids.py">get</a>(ray_identifier, \*, zone_identifier, \*\*<a href="src/cloudflare/types/logs/rayid_get_params.py">params</a>) -> <a href="./src/cloudflare/types/logs/rayid_get_response.py">RayidGetResponse</a></code>

## Received

Types:

```python
from cloudflare.types.logs import ReceivedGetResponse
```

Methods:

- <code title="get /zones/{zone_identifier}/logs/received">client.logs.received.<a href="./src/cloudflare/resources/logs/received/received.py">get</a>(zone_identifier, \*\*<a href="src/cloudflare/types/logs/received_get_params.py">params</a>) -> <a href="./src/cloudflare/types/logs/received_get_response.py">ReceivedGetResponse</a></code>

### Fields

Types:

```python
from cloudflare.types.logs.received import FieldListResponse
```

Methods:

- <code title="get /zones/{zone_identifier}/logs/received/fields">client.logs.received.fields.<a href="./src/cloudflare/resources/logs/received/fields.py">list</a>(zone_identifier) -> <a href="./src/cloudflare/types/logs/received/field_list_response.py">FieldListResponse</a></code>

# OriginTLSClientAuth

Types:

```python
from cloudflare.types import (
    OriginTLSClientAuthCreateResponse,
    OriginTLSClientAuthListResponse,
    OriginTLSClientAuthDeleteResponse,
    OriginTLSClientAuthGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/origin_tls_client_auth">client.origin_tls_client_auth.<a href="./src/cloudflare/resources/origin_tls_client_auth/origin_tls_client_auth.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/origin_tls_client_auth_create_params.py">params</a>) -> <a href="./src/cloudflare/types/origin_tls_client_auth_create_response.py">OriginTLSClientAuthCreateResponse</a></code>
- <code title="get /zones/{zone_id}/origin_tls_client_auth">client.origin_tls_client_auth.<a href="./src/cloudflare/resources/origin_tls_client_auth/origin_tls_client_auth.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/origin_tls_client_auth_list_response.py">Optional</a></code>
- <code title="delete /zones/{zone_id}/origin_tls_client_auth/{certificate_id}">client.origin_tls_client_auth.<a href="./src/cloudflare/resources/origin_tls_client_auth/origin_tls_client_auth.py">delete</a>(certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/origin_tls_client_auth_delete_response.py">OriginTLSClientAuthDeleteResponse</a></code>
- <code title="get /zones/{zone_id}/origin_tls_client_auth/{certificate_id}">client.origin_tls_client_auth.<a href="./src/cloudflare/resources/origin_tls_client_auth/origin_tls_client_auth.py">get</a>(certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/origin_tls_client_auth_get_response.py">OriginTLSClientAuthGetResponse</a></code>

## Hostnames

Types:

```python
from cloudflare.types.origin_tls_client_auth import HostnameUpdateResponse, HostnameGetResponse
```

Methods:

- <code title="put /zones/{zone_id}/origin_tls_client_auth/hostnames">client.origin_tls_client_auth.hostnames.<a href="./src/cloudflare/resources/origin_tls_client_auth/hostnames/hostnames.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/origin_tls_client_auth/hostname_update_params.py">params</a>) -> <a href="./src/cloudflare/types/origin_tls_client_auth/hostname_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/origin_tls_client_auth/hostnames/{hostname}">client.origin_tls_client_auth.hostnames.<a href="./src/cloudflare/resources/origin_tls_client_auth/hostnames/hostnames.py">get</a>(hostname, \*, zone_id) -> <a href="./src/cloudflare/types/origin_tls_client_auth/hostname_get_response.py">HostnameGetResponse</a></code>

### Certificates

Types:

```python
from cloudflare.types.origin_tls_client_auth.hostnames import (
    CertificateCreateResponse,
    CertificateListResponse,
    CertificateDeleteResponse,
    CertificateGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/origin_tls_client_auth/hostnames/certificates">client.origin_tls_client_auth.hostnames.certificates.<a href="./src/cloudflare/resources/origin_tls_client_auth/hostnames/certificates.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/origin_tls_client_auth/hostnames/certificate_create_params.py">params</a>) -> <a href="./src/cloudflare/types/origin_tls_client_auth/hostnames/certificate_create_response.py">CertificateCreateResponse</a></code>
- <code title="get /zones/{zone_id}/origin_tls_client_auth/hostnames/certificates">client.origin_tls_client_auth.hostnames.certificates.<a href="./src/cloudflare/resources/origin_tls_client_auth/hostnames/certificates.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/origin_tls_client_auth/hostnames/certificate_list_response.py">Optional</a></code>
- <code title="delete /zones/{zone_id}/origin_tls_client_auth/hostnames/certificates/{certificate_id}">client.origin_tls_client_auth.hostnames.certificates.<a href="./src/cloudflare/resources/origin_tls_client_auth/hostnames/certificates.py">delete</a>(certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/origin_tls_client_auth/hostnames/certificate_delete_response.py">CertificateDeleteResponse</a></code>
- <code title="get /zones/{zone_id}/origin_tls_client_auth/hostnames/certificates/{certificate_id}">client.origin_tls_client_auth.hostnames.certificates.<a href="./src/cloudflare/resources/origin_tls_client_auth/hostnames/certificates.py">get</a>(certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/origin_tls_client_auth/hostnames/certificate_get_response.py">CertificateGetResponse</a></code>

## Settings

Types:

```python
from cloudflare.types.origin_tls_client_auth import SettingUpdateResponse, SettingGetResponse
```

Methods:

- <code title="put /zones/{zone_id}/origin_tls_client_auth/settings">client.origin_tls_client_auth.settings.<a href="./src/cloudflare/resources/origin_tls_client_auth/settings.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/origin_tls_client_auth/setting_update_params.py">params</a>) -> <a href="./src/cloudflare/types/origin_tls_client_auth/setting_update_response.py">SettingUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/origin_tls_client_auth/settings">client.origin_tls_client_auth.settings.<a href="./src/cloudflare/resources/origin_tls_client_auth/settings.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/origin_tls_client_auth/setting_get_response.py">SettingGetResponse</a></code>

# Pagerules

Types:

```python
from cloudflare.types import (
    PageruleCreateResponse,
    PageruleUpdateResponse,
    PageruleListResponse,
    PageruleDeleteResponse,
    PageruleEditResponse,
    PageruleGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/pagerules">client.pagerules.<a href="./src/cloudflare/resources/pagerules/pagerules.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/pagerule_create_params.py">params</a>) -> <a href="./src/cloudflare/types/pagerule_create_response.py">PageruleCreateResponse</a></code>
- <code title="put /zones/{zone_id}/pagerules/{pagerule_id}">client.pagerules.<a href="./src/cloudflare/resources/pagerules/pagerules.py">update</a>(pagerule_id, \*, zone_id, \*\*<a href="src/cloudflare/types/pagerule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/pagerule_update_response.py">PageruleUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/pagerules">client.pagerules.<a href="./src/cloudflare/resources/pagerules/pagerules.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/pagerule_list_params.py">params</a>) -> <a href="./src/cloudflare/types/pagerule_list_response.py">PageruleListResponse</a></code>
- <code title="delete /zones/{zone_id}/pagerules/{pagerule_id}">client.pagerules.<a href="./src/cloudflare/resources/pagerules/pagerules.py">delete</a>(pagerule_id, \*, zone_id) -> <a href="./src/cloudflare/types/pagerule_delete_response.py">Optional</a></code>
- <code title="patch /zones/{zone_id}/pagerules/{pagerule_id}">client.pagerules.<a href="./src/cloudflare/resources/pagerules/pagerules.py">edit</a>(pagerule_id, \*, zone_id, \*\*<a href="src/cloudflare/types/pagerule_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/pagerule_edit_response.py">PageruleEditResponse</a></code>
- <code title="get /zones/{zone_id}/pagerules/{pagerule_id}">client.pagerules.<a href="./src/cloudflare/resources/pagerules/pagerules.py">get</a>(pagerule_id, \*, zone_id) -> <a href="./src/cloudflare/types/pagerule_get_response.py">PageruleGetResponse</a></code>

## Settings

Types:

```python
from cloudflare.types.pagerules import SettingListResponse
```

Methods:

- <code title="get /zones/{zone_id}/pagerules/settings">client.pagerules.settings.<a href="./src/cloudflare/resources/pagerules/settings.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/pagerules/setting_list_response.py">SettingListResponse</a></code>

# RateLimits

Types:

```python
from cloudflare.types import (
    RateLimitCreateResponse,
    RateLimitListResponse,
    RateLimitDeleteResponse,
    RateLimitEditResponse,
    RateLimitGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_identifier}/rate_limits">client.rate_limits.<a href="./src/cloudflare/resources/rate_limits.py">create</a>(zone_identifier, \*\*<a href="src/cloudflare/types/rate_limit_create_params.py">params</a>) -> <a href="./src/cloudflare/types/rate_limit_create_response.py">Optional</a></code>
- <code title="get /zones/{zone_identifier}/rate_limits">client.rate_limits.<a href="./src/cloudflare/resources/rate_limits.py">list</a>(zone_identifier, \*\*<a href="src/cloudflare/types/rate_limit_list_params.py">params</a>) -> <a href="./src/cloudflare/types/rate_limit_list_response.py">SyncV4PagePaginationArray[RateLimitListResponse]</a></code>
- <code title="delete /zones/{zone_identifier}/rate_limits/{id}">client.rate_limits.<a href="./src/cloudflare/resources/rate_limits.py">delete</a>(id, \*, zone_identifier) -> <a href="./src/cloudflare/types/rate_limit_delete_response.py">Optional</a></code>
- <code title="put /zones/{zone_identifier}/rate_limits/{id}">client.rate_limits.<a href="./src/cloudflare/resources/rate_limits.py">edit</a>(id, \*, zone_identifier, \*\*<a href="src/cloudflare/types/rate_limit_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/rate_limit_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_identifier}/rate_limits/{id}">client.rate_limits.<a href="./src/cloudflare/resources/rate_limits.py">get</a>(id, \*, zone_identifier) -> <a href="./src/cloudflare/types/rate_limit_get_response.py">Optional</a></code>

# SecondaryDNS

## ForceAxfrs

Types:

```python
from cloudflare.types.secondary_dns import ForceAxfrCreateResponse
```

Methods:

- <code title="post /zones/{zone_id}/secondary_dns/force_axfr">client.secondary_dns.force_axfrs.<a href="./src/cloudflare/resources/secondary_dns/force_axfrs.py">create</a>(\*, zone_id) -> <a href="./src/cloudflare/types/secondary_dns/force_axfr_create_response.py">str</a></code>

## Incoming

Types:

```python
from cloudflare.types.secondary_dns import (
    IncomingCreateResponse,
    IncomingUpdateResponse,
    IncomingDeleteResponse,
    IncomingGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/secondary_dns/incoming">client.secondary_dns.incoming.<a href="./src/cloudflare/resources/secondary_dns/incoming.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/secondary_dns/incoming_create_params.py">params</a>) -> <a href="./src/cloudflare/types/secondary_dns/incoming_create_response.py">IncomingCreateResponse</a></code>
- <code title="put /zones/{zone_id}/secondary_dns/incoming">client.secondary_dns.incoming.<a href="./src/cloudflare/resources/secondary_dns/incoming.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/secondary_dns/incoming_update_params.py">params</a>) -> <a href="./src/cloudflare/types/secondary_dns/incoming_update_response.py">IncomingUpdateResponse</a></code>
- <code title="delete /zones/{zone_id}/secondary_dns/incoming">client.secondary_dns.incoming.<a href="./src/cloudflare/resources/secondary_dns/incoming.py">delete</a>(\*, zone_id) -> <a href="./src/cloudflare/types/secondary_dns/incoming_delete_response.py">IncomingDeleteResponse</a></code>
- <code title="get /zones/{zone_id}/secondary_dns/incoming">client.secondary_dns.incoming.<a href="./src/cloudflare/resources/secondary_dns/incoming.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/secondary_dns/incoming_get_response.py">IncomingGetResponse</a></code>

## Outgoing

Types:

```python
from cloudflare.types.secondary_dns import (
    OutgoingCreateResponse,
    OutgoingUpdateResponse,
    OutgoingDeleteResponse,
    OutgoingDisableResponse,
    OutgoingEnableResponse,
    OutgoingForceNotifyResponse,
    OutgoingGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/secondary_dns/outgoing">client.secondary_dns.outgoing.<a href="./src/cloudflare/resources/secondary_dns/outgoing/outgoing.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/secondary_dns/outgoing_create_params.py">params</a>) -> <a href="./src/cloudflare/types/secondary_dns/outgoing_create_response.py">OutgoingCreateResponse</a></code>
- <code title="put /zones/{zone_id}/secondary_dns/outgoing">client.secondary_dns.outgoing.<a href="./src/cloudflare/resources/secondary_dns/outgoing/outgoing.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/secondary_dns/outgoing_update_params.py">params</a>) -> <a href="./src/cloudflare/types/secondary_dns/outgoing_update_response.py">OutgoingUpdateResponse</a></code>
- <code title="delete /zones/{zone_id}/secondary_dns/outgoing">client.secondary_dns.outgoing.<a href="./src/cloudflare/resources/secondary_dns/outgoing/outgoing.py">delete</a>(\*, zone_id) -> <a href="./src/cloudflare/types/secondary_dns/outgoing_delete_response.py">OutgoingDeleteResponse</a></code>
- <code title="post /zones/{zone_id}/secondary_dns/outgoing/disable">client.secondary_dns.outgoing.<a href="./src/cloudflare/resources/secondary_dns/outgoing/outgoing.py">disable</a>(\*, zone_id) -> <a href="./src/cloudflare/types/secondary_dns/outgoing_disable_response.py">str</a></code>
- <code title="post /zones/{zone_id}/secondary_dns/outgoing/enable">client.secondary_dns.outgoing.<a href="./src/cloudflare/resources/secondary_dns/outgoing/outgoing.py">enable</a>(\*, zone_id) -> <a href="./src/cloudflare/types/secondary_dns/outgoing_enable_response.py">str</a></code>
- <code title="post /zones/{zone_id}/secondary_dns/outgoing/force_notify">client.secondary_dns.outgoing.<a href="./src/cloudflare/resources/secondary_dns/outgoing/outgoing.py">force_notify</a>(\*, zone_id) -> <a href="./src/cloudflare/types/secondary_dns/outgoing_force_notify_response.py">str</a></code>
- <code title="get /zones/{zone_id}/secondary_dns/outgoing">client.secondary_dns.outgoing.<a href="./src/cloudflare/resources/secondary_dns/outgoing/outgoing.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/secondary_dns/outgoing_get_response.py">OutgoingGetResponse</a></code>

### Status

Types:

```python
from cloudflare.types.secondary_dns.outgoing import StatusGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/secondary_dns/outgoing/status">client.secondary_dns.outgoing.status.<a href="./src/cloudflare/resources/secondary_dns/outgoing/status.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/secondary_dns/outgoing/status_get_response.py">str</a></code>

## ACLs

Types:

```python
from cloudflare.types.secondary_dns import (
    ACLCreateResponse,
    ACLUpdateResponse,
    ACLListResponse,
    ACLDeleteResponse,
    ACLGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/secondary_dns/acls">client.secondary_dns.acls.<a href="./src/cloudflare/resources/secondary_dns/acls.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/secondary_dns/acl_create_params.py">params</a>) -> <a href="./src/cloudflare/types/secondary_dns/acl_create_response.py">ACLCreateResponse</a></code>
- <code title="put /accounts/{account_id}/secondary_dns/acls/{acl_id}">client.secondary_dns.acls.<a href="./src/cloudflare/resources/secondary_dns/acls.py">update</a>(acl_id, \*, account_id, \*\*<a href="src/cloudflare/types/secondary_dns/acl_update_params.py">params</a>) -> <a href="./src/cloudflare/types/secondary_dns/acl_update_response.py">ACLUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/secondary_dns/acls">client.secondary_dns.acls.<a href="./src/cloudflare/resources/secondary_dns/acls.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/secondary_dns/acl_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/secondary_dns/acls/{acl_id}">client.secondary_dns.acls.<a href="./src/cloudflare/resources/secondary_dns/acls.py">delete</a>(acl_id, \*, account_id) -> <a href="./src/cloudflare/types/secondary_dns/acl_delete_response.py">ACLDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/secondary_dns/acls/{acl_id}">client.secondary_dns.acls.<a href="./src/cloudflare/resources/secondary_dns/acls.py">get</a>(acl_id, \*, account_id) -> <a href="./src/cloudflare/types/secondary_dns/acl_get_response.py">ACLGetResponse</a></code>

## Peers

Types:

```python
from cloudflare.types.secondary_dns import (
    PeerCreateResponse,
    PeerUpdateResponse,
    PeerListResponse,
    PeerDeleteResponse,
    PeerGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/secondary_dns/peers">client.secondary_dns.peers.<a href="./src/cloudflare/resources/secondary_dns/peers.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/secondary_dns/peer_create_params.py">params</a>) -> <a href="./src/cloudflare/types/secondary_dns/peer_create_response.py">PeerCreateResponse</a></code>
- <code title="put /accounts/{account_id}/secondary_dns/peers/{peer_id}">client.secondary_dns.peers.<a href="./src/cloudflare/resources/secondary_dns/peers.py">update</a>(peer_id, \*, account_id, \*\*<a href="src/cloudflare/types/secondary_dns/peer_update_params.py">params</a>) -> <a href="./src/cloudflare/types/secondary_dns/peer_update_response.py">PeerUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/secondary_dns/peers">client.secondary_dns.peers.<a href="./src/cloudflare/resources/secondary_dns/peers.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/secondary_dns/peer_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/secondary_dns/peers/{peer_id}">client.secondary_dns.peers.<a href="./src/cloudflare/resources/secondary_dns/peers.py">delete</a>(peer_id, \*, account_id) -> <a href="./src/cloudflare/types/secondary_dns/peer_delete_response.py">PeerDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/secondary_dns/peers/{peer_id}">client.secondary_dns.peers.<a href="./src/cloudflare/resources/secondary_dns/peers.py">get</a>(peer_id, \*, account_id) -> <a href="./src/cloudflare/types/secondary_dns/peer_get_response.py">PeerGetResponse</a></code>

## TSIGs

Types:

```python
from cloudflare.types.secondary_dns import (
    TSIGCreateResponse,
    TSIGUpdateResponse,
    TSIGListResponse,
    TSIGDeleteResponse,
    TSIGGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/secondary_dns/tsigs">client.secondary_dns.tsigs.<a href="./src/cloudflare/resources/secondary_dns/tsigs.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/secondary_dns/tsig_create_params.py">params</a>) -> <a href="./src/cloudflare/types/secondary_dns/tsig_create_response.py">TSIGCreateResponse</a></code>
- <code title="put /accounts/{account_id}/secondary_dns/tsigs/{tsig_id}">client.secondary_dns.tsigs.<a href="./src/cloudflare/resources/secondary_dns/tsigs.py">update</a>(tsig_id, \*, account_id, \*\*<a href="src/cloudflare/types/secondary_dns/tsig_update_params.py">params</a>) -> <a href="./src/cloudflare/types/secondary_dns/tsig_update_response.py">TSIGUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/secondary_dns/tsigs">client.secondary_dns.tsigs.<a href="./src/cloudflare/resources/secondary_dns/tsigs.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/secondary_dns/tsig_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/secondary_dns/tsigs/{tsig_id}">client.secondary_dns.tsigs.<a href="./src/cloudflare/resources/secondary_dns/tsigs.py">delete</a>(tsig_id, \*, account_id) -> <a href="./src/cloudflare/types/secondary_dns/tsig_delete_response.py">TSIGDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/secondary_dns/tsigs/{tsig_id}">client.secondary_dns.tsigs.<a href="./src/cloudflare/resources/secondary_dns/tsigs.py">get</a>(tsig_id, \*, account_id) -> <a href="./src/cloudflare/types/secondary_dns/tsig_get_response.py">TSIGGetResponse</a></code>

# WaitingRooms

Types:

```python
from cloudflare.types import (
    WaitingRoomCreateResponse,
    WaitingRoomUpdateResponse,
    WaitingRoomListResponse,
    WaitingRoomDeleteResponse,
    WaitingRoomEditResponse,
    WaitingRoomGetResponse,
    WaitingRoomPreviewResponse,
)
```

Methods:

- <code title="post /zones/{zone_identifier}/waiting_rooms">client.waiting_rooms.<a href="./src/cloudflare/resources/waiting_rooms/waiting_rooms.py">create</a>(zone_identifier, \*\*<a href="src/cloudflare/types/waiting_room_create_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_room_create_response.py">WaitingRoomCreateResponse</a></code>
- <code title="put /zones/{zone_identifier}/waiting_rooms/{waiting_room_id}">client.waiting_rooms.<a href="./src/cloudflare/resources/waiting_rooms/waiting_rooms.py">update</a>(waiting_room_id, \*, zone_identifier, \*\*<a href="src/cloudflare/types/waiting_room_update_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_room_update_response.py">WaitingRoomUpdateResponse</a></code>
- <code title="get /zones/{zone_identifier}/waiting_rooms">client.waiting_rooms.<a href="./src/cloudflare/resources/waiting_rooms/waiting_rooms.py">list</a>(zone_identifier) -> <a href="./src/cloudflare/types/waiting_room_list_response.py">Optional</a></code>
- <code title="delete /zones/{zone_identifier}/waiting_rooms/{waiting_room_id}">client.waiting_rooms.<a href="./src/cloudflare/resources/waiting_rooms/waiting_rooms.py">delete</a>(waiting_room_id, \*, zone_identifier) -> <a href="./src/cloudflare/types/waiting_room_delete_response.py">WaitingRoomDeleteResponse</a></code>
- <code title="patch /zones/{zone_identifier}/waiting_rooms/{waiting_room_id}">client.waiting_rooms.<a href="./src/cloudflare/resources/waiting_rooms/waiting_rooms.py">edit</a>(waiting_room_id, \*, zone_identifier, \*\*<a href="src/cloudflare/types/waiting_room_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_room_edit_response.py">WaitingRoomEditResponse</a></code>
- <code title="get /zones/{zone_identifier}/waiting_rooms/{waiting_room_id}">client.waiting_rooms.<a href="./src/cloudflare/resources/waiting_rooms/waiting_rooms.py">get</a>(waiting_room_id, \*, zone_identifier) -> <a href="./src/cloudflare/types/waiting_room_get_response.py">WaitingRoomGetResponse</a></code>
- <code title="post /zones/{zone_identifier}/waiting_rooms/preview">client.waiting_rooms.<a href="./src/cloudflare/resources/waiting_rooms/waiting_rooms.py">preview</a>(zone_identifier, \*\*<a href="src/cloudflare/types/waiting_room_preview_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_room_preview_response.py">WaitingRoomPreviewResponse</a></code>

## Events

Types:

```python
from cloudflare.types.waiting_rooms import (
    EventCreateResponse,
    EventUpdateResponse,
    EventListResponse,
    EventDeleteResponse,
    EventEditResponse,
    EventGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/events">client.waiting_rooms.events.<a href="./src/cloudflare/resources/waiting_rooms/events/events.py">create</a>(waiting_room_id, \*, zone_identifier, \*\*<a href="src/cloudflare/types/waiting_rooms/event_create_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/event_create_response.py">EventCreateResponse</a></code>
- <code title="put /zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/events/{event_id}">client.waiting_rooms.events.<a href="./src/cloudflare/resources/waiting_rooms/events/events.py">update</a>(event_id, \*, zone_identifier, waiting_room_id, \*\*<a href="src/cloudflare/types/waiting_rooms/event_update_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/event_update_response.py">EventUpdateResponse</a></code>
- <code title="get /zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/events">client.waiting_rooms.events.<a href="./src/cloudflare/resources/waiting_rooms/events/events.py">list</a>(waiting_room_id, \*, zone_identifier) -> <a href="./src/cloudflare/types/waiting_rooms/event_list_response.py">Optional</a></code>
- <code title="delete /zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/events/{event_id}">client.waiting_rooms.events.<a href="./src/cloudflare/resources/waiting_rooms/events/events.py">delete</a>(event_id, \*, zone_identifier, waiting_room_id) -> <a href="./src/cloudflare/types/waiting_rooms/event_delete_response.py">EventDeleteResponse</a></code>
- <code title="patch /zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/events/{event_id}">client.waiting_rooms.events.<a href="./src/cloudflare/resources/waiting_rooms/events/events.py">edit</a>(event_id, \*, zone_identifier, waiting_room_id, \*\*<a href="src/cloudflare/types/waiting_rooms/event_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/event_edit_response.py">EventEditResponse</a></code>
- <code title="get /zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/events/{event_id}">client.waiting_rooms.events.<a href="./src/cloudflare/resources/waiting_rooms/events/events.py">get</a>(event_id, \*, zone_identifier, waiting_room_id) -> <a href="./src/cloudflare/types/waiting_rooms/event_get_response.py">EventGetResponse</a></code>

### Details

Types:

```python
from cloudflare.types.waiting_rooms.events import DetailGetResponse
```

Methods:

- <code title="get /zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/events/{event_id}/details">client.waiting_rooms.events.details.<a href="./src/cloudflare/resources/waiting_rooms/events/details.py">get</a>(event_id, \*, zone_identifier, waiting_room_id) -> <a href="./src/cloudflare/types/waiting_rooms/events/detail_get_response.py">DetailGetResponse</a></code>

## Rules

Types:

```python
from cloudflare.types.waiting_rooms import (
    RuleCreateResponse,
    RuleUpdateResponse,
    RuleListResponse,
    RuleDeleteResponse,
    RuleEditResponse,
)
```

Methods:

- <code title="post /zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/rules">client.waiting_rooms.rules.<a href="./src/cloudflare/resources/waiting_rooms/rules.py">create</a>(waiting_room_id, \*, zone_identifier, \*\*<a href="src/cloudflare/types/waiting_rooms/rule_create_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/rule_create_response.py">Optional</a></code>
- <code title="put /zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/rules">client.waiting_rooms.rules.<a href="./src/cloudflare/resources/waiting_rooms/rules.py">update</a>(waiting_room_id, \*, zone_identifier, \*\*<a href="src/cloudflare/types/waiting_rooms/rule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/rule_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/rules">client.waiting_rooms.rules.<a href="./src/cloudflare/resources/waiting_rooms/rules.py">list</a>(waiting_room_id, \*, zone_identifier) -> <a href="./src/cloudflare/types/waiting_rooms/rule_list_response.py">Optional</a></code>
- <code title="delete /zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/rules/{rule_id}">client.waiting_rooms.rules.<a href="./src/cloudflare/resources/waiting_rooms/rules.py">delete</a>(rule_id, \*, zone_identifier, waiting_room_id) -> <a href="./src/cloudflare/types/waiting_rooms/rule_delete_response.py">Optional</a></code>
- <code title="patch /zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/rules/{rule_id}">client.waiting_rooms.rules.<a href="./src/cloudflare/resources/waiting_rooms/rules.py">edit</a>(rule_id, \*, zone_identifier, waiting_room_id, \*\*<a href="src/cloudflare/types/waiting_rooms/rule_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/rule_edit_response.py">Optional</a></code>

## Statuses

Types:

```python
from cloudflare.types.waiting_rooms import StatusGetResponse
```

Methods:

- <code title="get /zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/status">client.waiting_rooms.statuses.<a href="./src/cloudflare/resources/waiting_rooms/statuses.py">get</a>(waiting_room_id, \*, zone_identifier) -> <a href="./src/cloudflare/types/waiting_rooms/status_get_response.py">StatusGetResponse</a></code>

## Settings

Types:

```python
from cloudflare.types.waiting_rooms import (
    SettingUpdateResponse,
    SettingEditResponse,
    SettingGetResponse,
)
```

Methods:

- <code title="put /zones/{zone_identifier}/waiting_rooms/settings">client.waiting_rooms.settings.<a href="./src/cloudflare/resources/waiting_rooms/settings.py">update</a>(zone_identifier, \*\*<a href="src/cloudflare/types/waiting_rooms/setting_update_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/setting_update_response.py">SettingUpdateResponse</a></code>
- <code title="patch /zones/{zone_identifier}/waiting_rooms/settings">client.waiting_rooms.settings.<a href="./src/cloudflare/resources/waiting_rooms/settings.py">edit</a>(zone_identifier, \*\*<a href="src/cloudflare/types/waiting_rooms/setting_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/setting_edit_response.py">SettingEditResponse</a></code>
- <code title="get /zones/{zone_identifier}/waiting_rooms/settings">client.waiting_rooms.settings.<a href="./src/cloudflare/resources/waiting_rooms/settings.py">get</a>(zone_identifier) -> <a href="./src/cloudflare/types/waiting_rooms/setting_get_response.py">SettingGetResponse</a></code>

# Web3

## Hostnames

Types:

```python
from cloudflare.types.web3 import (
    HostnameCreateResponse,
    HostnameListResponse,
    HostnameDeleteResponse,
    HostnameEditResponse,
    HostnameGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_identifier}/web3/hostnames">client.web3.hostnames.<a href="./src/cloudflare/resources/web3/hostnames/hostnames.py">create</a>(zone_identifier, \*\*<a href="src/cloudflare/types/web3/hostname_create_params.py">params</a>) -> <a href="./src/cloudflare/types/web3/hostname_create_response.py">HostnameCreateResponse</a></code>
- <code title="get /zones/{zone_identifier}/web3/hostnames">client.web3.hostnames.<a href="./src/cloudflare/resources/web3/hostnames/hostnames.py">list</a>(zone_identifier) -> <a href="./src/cloudflare/types/web3/hostname_list_response.py">Optional</a></code>
- <code title="delete /zones/{zone_identifier}/web3/hostnames/{identifier}">client.web3.hostnames.<a href="./src/cloudflare/resources/web3/hostnames/hostnames.py">delete</a>(identifier, \*, zone_identifier) -> <a href="./src/cloudflare/types/web3/hostname_delete_response.py">Optional</a></code>
- <code title="patch /zones/{zone_identifier}/web3/hostnames/{identifier}">client.web3.hostnames.<a href="./src/cloudflare/resources/web3/hostnames/hostnames.py">edit</a>(identifier, \*, zone_identifier, \*\*<a href="src/cloudflare/types/web3/hostname_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/web3/hostname_edit_response.py">HostnameEditResponse</a></code>
- <code title="get /zones/{zone_identifier}/web3/hostnames/{identifier}">client.web3.hostnames.<a href="./src/cloudflare/resources/web3/hostnames/hostnames.py">get</a>(identifier, \*, zone_identifier) -> <a href="./src/cloudflare/types/web3/hostname_get_response.py">HostnameGetResponse</a></code>

### IPFSUniversalPaths

#### ContentLists

Types:

```python
from cloudflare.types.web3.hostnames.ipfs_universal_paths import (
    ContentListUpdateResponse,
    ContentListListResponse,
)
```

Methods:

- <code title="put /zones/{zone_identifier}/web3/hostnames/{identifier}/ipfs_universal_path/content_list">client.web3.hostnames.ipfs_universal_paths.content_lists.<a href="./src/cloudflare/resources/web3/hostnames/ipfs_universal_paths/content_lists/content_lists.py">update</a>(identifier, \*, zone_identifier, \*\*<a href="src/cloudflare/types/web3/hostnames/ipfs_universal_paths/content_list_update_params.py">params</a>) -> <a href="./src/cloudflare/types/web3/hostnames/ipfs_universal_paths/content_list_update_response.py">ContentListUpdateResponse</a></code>
- <code title="get /zones/{zone_identifier}/web3/hostnames/{identifier}/ipfs_universal_path/content_list">client.web3.hostnames.ipfs_universal_paths.content_lists.<a href="./src/cloudflare/resources/web3/hostnames/ipfs_universal_paths/content_lists/content_lists.py">list</a>(identifier, \*, zone_identifier) -> <a href="./src/cloudflare/types/web3/hostnames/ipfs_universal_paths/content_list_list_response.py">ContentListListResponse</a></code>

##### Entries

Types:

```python
from cloudflare.types.web3.hostnames.ipfs_universal_paths.content_lists import (
    EntryCreateResponse,
    EntryUpdateResponse,
    EntryListResponse,
    EntryDeleteResponse,
    EntryGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_identifier}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries">client.web3.hostnames.ipfs_universal_paths.content_lists.entries.<a href="./src/cloudflare/resources/web3/hostnames/ipfs_universal_paths/content_lists/entries.py">create</a>(identifier, \*, zone_identifier, \*\*<a href="src/cloudflare/types/web3/hostnames/ipfs_universal_paths/content_lists/entry_create_params.py">params</a>) -> <a href="./src/cloudflare/types/web3/hostnames/ipfs_universal_paths/content_lists/entry_create_response.py">EntryCreateResponse</a></code>
- <code title="put /zones/{zone_identifier}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries/{content_list_entry_identifier}">client.web3.hostnames.ipfs_universal_paths.content_lists.entries.<a href="./src/cloudflare/resources/web3/hostnames/ipfs_universal_paths/content_lists/entries.py">update</a>(content_list_entry_identifier, \*, zone_identifier, identifier, \*\*<a href="src/cloudflare/types/web3/hostnames/ipfs_universal_paths/content_lists/entry_update_params.py">params</a>) -> <a href="./src/cloudflare/types/web3/hostnames/ipfs_universal_paths/content_lists/entry_update_response.py">EntryUpdateResponse</a></code>
- <code title="get /zones/{zone_identifier}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries">client.web3.hostnames.ipfs_universal_paths.content_lists.entries.<a href="./src/cloudflare/resources/web3/hostnames/ipfs_universal_paths/content_lists/entries.py">list</a>(identifier, \*, zone_identifier) -> <a href="./src/cloudflare/types/web3/hostnames/ipfs_universal_paths/content_lists/entry_list_response.py">Optional</a></code>
- <code title="delete /zones/{zone_identifier}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries/{content_list_entry_identifier}">client.web3.hostnames.ipfs_universal_paths.content_lists.entries.<a href="./src/cloudflare/resources/web3/hostnames/ipfs_universal_paths/content_lists/entries.py">delete</a>(content_list_entry_identifier, \*, zone_identifier, identifier) -> <a href="./src/cloudflare/types/web3/hostnames/ipfs_universal_paths/content_lists/entry_delete_response.py">Optional</a></code>
- <code title="get /zones/{zone_identifier}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries/{content_list_entry_identifier}">client.web3.hostnames.ipfs_universal_paths.content_lists.entries.<a href="./src/cloudflare/resources/web3/hostnames/ipfs_universal_paths/content_lists/entries.py">get</a>(content_list_entry_identifier, \*, zone_identifier, identifier) -> <a href="./src/cloudflare/types/web3/hostnames/ipfs_universal_paths/content_lists/entry_get_response.py">EntryGetResponse</a></code>

# Workers

## AI

Types:

```python
from cloudflare.types.workers import AIRunResponse
```

Methods:

- <code title="post /accounts/{account_id}/ai/run/{model_name}">client.workers.ai.<a href="./src/cloudflare/resources/workers/ai.py">run</a>(model_name, \*, account_id, \*\*<a href="src/cloudflare/types/workers/ai_run_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/ai_run_response.py">object</a></code>

## Scripts

Types:

```python
from cloudflare.types.workers import ScriptUpdateResponse, ScriptListResponse
```

Methods:

- <code title="put /accounts/{account_id}/workers/scripts/{script_name}">client.workers.scripts.<a href="./src/cloudflare/resources/workers/scripts/scripts.py">update</a>(script_name, \*, account_id, \*\*<a href="src/cloudflare/types/workers/script_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/script_update_response.py">ScriptUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/workers/scripts">client.workers.scripts.<a href="./src/cloudflare/resources/workers/scripts/scripts.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/workers/script_list_response.py">ScriptListResponse</a></code>
- <code title="delete /accounts/{account_id}/workers/scripts/{script_name}">client.workers.scripts.<a href="./src/cloudflare/resources/workers/scripts/scripts.py">delete</a>(script_name, \*, account_id, \*\*<a href="src/cloudflare/types/workers/script_delete_params.py">params</a>) -> None</code>
- <code title="get /accounts/{account_id}/workers/scripts/{script_name}">client.workers.scripts.<a href="./src/cloudflare/resources/workers/scripts/scripts.py">get</a>(script_name, \*, account_id) -> BinaryAPIResponse</code>

### Bindings

Types:

```python
from cloudflare.types.workers.scripts import BindingListResponse
```

Methods:

- <code title="get /zones/{zone_id}/workers/script/bindings">client.workers.scripts.bindings.<a href="./src/cloudflare/resources/workers/scripts/bindings.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/workers/scripts/binding_list_response.py">BindingListResponse</a></code>

### Schedules

Types:

```python
from cloudflare.types.workers.scripts import ScheduleUpdateResponse, ScheduleListResponse
```

Methods:

- <code title="put /accounts/{account_id}/workers/scripts/{script_name}/schedules">client.workers.scripts.schedules.<a href="./src/cloudflare/resources/workers/scripts/schedules.py">update</a>(script_name, \*, account_id, \*\*<a href="src/cloudflare/types/workers/scripts/schedule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/scripts/schedule_update_response.py">ScheduleUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/workers/scripts/{script_name}/schedules">client.workers.scripts.schedules.<a href="./src/cloudflare/resources/workers/scripts/schedules.py">list</a>(script_name, \*, account_id) -> <a href="./src/cloudflare/types/workers/scripts/schedule_list_response.py">ScheduleListResponse</a></code>

### Tail

Types:

```python
from cloudflare.types.workers.scripts import (
    TailCreateResponse,
    TailListResponse,
    TailDeleteResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/workers/scripts/{script_name}/tails">client.workers.scripts.tail.<a href="./src/cloudflare/resources/workers/scripts/tail.py">create</a>(script_name, \*, account_id) -> <a href="./src/cloudflare/types/workers/scripts/tail_create_response.py">TailCreateResponse</a></code>
- <code title="get /accounts/{account_id}/workers/scripts/{script_name}/tails">client.workers.scripts.tail.<a href="./src/cloudflare/resources/workers/scripts/tail.py">list</a>(script_name, \*, account_id) -> <a href="./src/cloudflare/types/workers/scripts/tail_list_response.py">TailListResponse</a></code>
- <code title="delete /accounts/{account_id}/workers/scripts/{script_name}/tails/{id}">client.workers.scripts.tail.<a href="./src/cloudflare/resources/workers/scripts/tail.py">delete</a>(id, \*, account_id, script_name) -> <a href="./src/cloudflare/types/workers/scripts/tail_delete_response.py">TailDeleteResponse</a></code>

### UsageModel

Types:

```python
from cloudflare.types.workers.scripts import UsageModelUpdateResponse, UsageModelGetResponse
```

Methods:

- <code title="put /accounts/{account_id}/workers/scripts/{script_name}/usage-model">client.workers.scripts.usage_model.<a href="./src/cloudflare/resources/workers/scripts/usage_model.py">update</a>(script_name, \*, account_id, \*\*<a href="src/cloudflare/types/workers/scripts/usage_model_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/scripts/usage_model_update_response.py">UsageModelUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/workers/scripts/{script_name}/usage-model">client.workers.scripts.usage_model.<a href="./src/cloudflare/resources/workers/scripts/usage_model.py">get</a>(script_name, \*, account_id) -> <a href="./src/cloudflare/types/workers/scripts/usage_model_get_response.py">UsageModelGetResponse</a></code>

### Content

Types:

```python
from cloudflare.types.workers.scripts import ContentUpdateResponse
```

Methods:

- <code title="put /accounts/{account_id}/workers/scripts/{script_name}/content">client.workers.scripts.content.<a href="./src/cloudflare/resources/workers/scripts/content.py">update</a>(script_name, \*, account_id, \*\*<a href="src/cloudflare/types/workers/scripts/content_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/scripts/content_update_response.py">ContentUpdateResponse</a></code>

### ContentV2

Methods:

- <code title="get /accounts/{account_id}/workers/scripts/{script_name}/content/v2">client.workers.scripts.content_v2.<a href="./src/cloudflare/resources/workers/scripts/content_v2.py">get</a>(script_name, \*, account_id) -> BinaryAPIResponse</code>

### Settings

Types:

```python
from cloudflare.types.workers.scripts import SettingEditResponse, SettingGetResponse
```

Methods:

- <code title="patch /accounts/{account_id}/workers/scripts/{script_name}/settings">client.workers.scripts.settings.<a href="./src/cloudflare/resources/workers/scripts/settings.py">edit</a>(script_name, \*, account_id, \*\*<a href="src/cloudflare/types/workers/scripts/setting_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/scripts/setting_edit_response.py">SettingEditResponse</a></code>
- <code title="get /accounts/{account_id}/workers/scripts/{script_name}/settings">client.workers.scripts.settings.<a href="./src/cloudflare/resources/workers/scripts/settings.py">get</a>(script_name, \*, account_id) -> <a href="./src/cloudflare/types/workers/scripts/setting_get_response.py">SettingGetResponse</a></code>

## Filters

Types:

```python
from cloudflare.types.workers import (
    FilterCreateResponse,
    FilterUpdateResponse,
    FilterListResponse,
    FilterDeleteResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/workers/filters">client.workers.filters.<a href="./src/cloudflare/resources/workers/filters.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/workers/filter_create_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/filter_create_response.py">Optional</a></code>
- <code title="put /zones/{zone_id}/workers/filters/{filter_id}">client.workers.filters.<a href="./src/cloudflare/resources/workers/filters.py">update</a>(filter_id, \*, zone_id, \*\*<a href="src/cloudflare/types/workers/filter_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/filter_update_response.py">FilterUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/workers/filters">client.workers.filters.<a href="./src/cloudflare/resources/workers/filters.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/workers/filter_list_response.py">FilterListResponse</a></code>
- <code title="delete /zones/{zone_id}/workers/filters/{filter_id}">client.workers.filters.<a href="./src/cloudflare/resources/workers/filters.py">delete</a>(filter_id, \*, zone_id) -> <a href="./src/cloudflare/types/workers/filter_delete_response.py">Optional</a></code>

## Routes

Types:

```python
from cloudflare.types.workers import (
    RouteCreateResponse,
    RouteUpdateResponse,
    RouteListResponse,
    RouteDeleteResponse,
    RouteGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/workers/routes">client.workers.routes.<a href="./src/cloudflare/resources/workers/routes.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/workers/route_create_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/route_create_response.py">RouteCreateResponse</a></code>
- <code title="put /zones/{zone_id}/workers/routes/{route_id}">client.workers.routes.<a href="./src/cloudflare/resources/workers/routes.py">update</a>(route_id, \*, zone_id, \*\*<a href="src/cloudflare/types/workers/route_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/route_update_response.py">RouteUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/workers/routes">client.workers.routes.<a href="./src/cloudflare/resources/workers/routes.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/workers/route_list_response.py">RouteListResponse</a></code>
- <code title="delete /zones/{zone_id}/workers/routes/{route_id}">client.workers.routes.<a href="./src/cloudflare/resources/workers/routes.py">delete</a>(route_id, \*, zone_id) -> <a href="./src/cloudflare/types/workers/route_delete_response.py">RouteDeleteResponse</a></code>
- <code title="get /zones/{zone_id}/workers/routes/{route_id}">client.workers.routes.<a href="./src/cloudflare/resources/workers/routes.py">get</a>(route_id, \*, zone_id) -> <a href="./src/cloudflare/types/workers/route_get_response.py">RouteGetResponse</a></code>

## AccountSettings

Types:

```python
from cloudflare.types.workers import AccountSettingUpdateResponse, AccountSettingGetResponse
```

Methods:

- <code title="put /accounts/{account_id}/workers/account-settings">client.workers.account_settings.<a href="./src/cloudflare/resources/workers/account_settings.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/workers/account_setting_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/account_setting_update_response.py">AccountSettingUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/workers/account-settings">client.workers.account_settings.<a href="./src/cloudflare/resources/workers/account_settings.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/workers/account_setting_get_response.py">AccountSettingGetResponse</a></code>

## Deployments

### ByScripts

Types:

```python
from cloudflare.types.workers.deployments import ByScriptListResponse, ByScriptGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/workers/deployments/by-script/{script_id}">client.workers.deployments.by_scripts.<a href="./src/cloudflare/resources/workers/deployments/by_scripts.py">list</a>(script_id, \*, account_id) -> <a href="./src/cloudflare/types/workers/deployments/by_script_list_response.py">ByScriptListResponse</a></code>
- <code title="get /accounts/{account_id}/workers/deployments/by-script/{script_id}/detail/{deployment_id}">client.workers.deployments.by_scripts.<a href="./src/cloudflare/resources/workers/deployments/by_scripts.py">get</a>(deployment_id, \*, account_id, script_id) -> <a href="./src/cloudflare/types/workers/deployments/by_script_get_response.py">ByScriptGetResponse</a></code>

## Domains

Types:

```python
from cloudflare.types.workers import DomainUpdateResponse, DomainListResponse, DomainGetResponse
```

Methods:

- <code title="put /accounts/{account_id}/workers/domains">client.workers.domains.<a href="./src/cloudflare/resources/workers/domains.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/workers/domain_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/domain_update_response.py">DomainUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/workers/domains">client.workers.domains.<a href="./src/cloudflare/resources/workers/domains.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/workers/domain_list_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/domain_list_response.py">DomainListResponse</a></code>
- <code title="delete /accounts/{account_id}/workers/domains/{domain_id}">client.workers.domains.<a href="./src/cloudflare/resources/workers/domains.py">delete</a>(domain_id, \*, account_id) -> None</code>
- <code title="get /accounts/{account_id}/workers/domains/{domain_id}">client.workers.domains.<a href="./src/cloudflare/resources/workers/domains.py">get</a>(domain_id, \*, account_id) -> <a href="./src/cloudflare/types/workers/domain_get_response.py">DomainGetResponse</a></code>

## Subdomains

Types:

```python
from cloudflare.types.workers import SubdomainUpdateResponse, SubdomainGetResponse
```

Methods:

- <code title="put /accounts/{account_id}/workers/subdomain">client.workers.subdomains.<a href="./src/cloudflare/resources/workers/subdomains.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/workers/subdomain_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/subdomain_update_response.py">SubdomainUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/workers/subdomain">client.workers.subdomains.<a href="./src/cloudflare/resources/workers/subdomains.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/workers/subdomain_get_response.py">SubdomainGetResponse</a></code>

## Services

### Environments

#### Content

Types:

```python
from cloudflare.types.workers.services.environments import ContentUpdateResponse
```

Methods:

- <code title="put /accounts/{account_id}/workers/services/{service_name}/environments/{environment_name}/content">client.workers.services.environments.content.<a href="./src/cloudflare/resources/workers/services/environments/content.py">update</a>(environment_name, \*, account_id, service_name, \*\*<a href="src/cloudflare/types/workers/services/environments/content_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/services/environments/content_update_response.py">ContentUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/workers/services/{service_name}/environments/{environment_name}/content">client.workers.services.environments.content.<a href="./src/cloudflare/resources/workers/services/environments/content.py">get</a>(environment_name, \*, account_id, service_name) -> BinaryAPIResponse</code>

#### Settings

Types:

```python
from cloudflare.types.workers.services.environments import SettingEditResponse, SettingGetResponse
```

Methods:

- <code title="patch /accounts/{account_id}/workers/services/{service_name}/environments/{environment_name}/settings">client.workers.services.environments.settings.<a href="./src/cloudflare/resources/workers/services/environments/settings.py">edit</a>(environment_name, \*, account_id, service_name, \*\*<a href="src/cloudflare/types/workers/services/environments/setting_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/services/environments/setting_edit_response.py">SettingEditResponse</a></code>
- <code title="get /accounts/{account_id}/workers/services/{service_name}/environments/{environment_name}/settings">client.workers.services.environments.settings.<a href="./src/cloudflare/resources/workers/services/environments/settings.py">get</a>(environment_name, \*, account_id, service_name) -> <a href="./src/cloudflare/types/workers/services/environments/setting_get_response.py">SettingGetResponse</a></code>

# KV

## Namespaces

Types:

```python
from cloudflare.types.kv import (
    NamespaceCreateResponse,
    NamespaceUpdateResponse,
    NamespaceListResponse,
    NamespaceDeleteResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/storage/kv/namespaces">client.kv.namespaces.<a href="./src/cloudflare/resources/kv/namespaces/namespaces.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/kv/namespace_create_params.py">params</a>) -> <a href="./src/cloudflare/types/kv/namespace_create_response.py">NamespaceCreateResponse</a></code>
- <code title="put /accounts/{account_id}/storage/kv/namespaces/{namespace_id}">client.kv.namespaces.<a href="./src/cloudflare/resources/kv/namespaces/namespaces.py">update</a>(namespace_id, \*, account_id, \*\*<a href="src/cloudflare/types/kv/namespace_update_params.py">params</a>) -> <a href="./src/cloudflare/types/kv/namespace_update_response.py">NamespaceUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/storage/kv/namespaces">client.kv.namespaces.<a href="./src/cloudflare/resources/kv/namespaces/namespaces.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/kv/namespace_list_params.py">params</a>) -> <a href="./src/cloudflare/types/kv/namespace_list_response.py">SyncV4PagePaginationArray[NamespaceListResponse]</a></code>
- <code title="delete /accounts/{account_id}/storage/kv/namespaces/{namespace_id}">client.kv.namespaces.<a href="./src/cloudflare/resources/kv/namespaces/namespaces.py">delete</a>(namespace_id, \*, account_id) -> <a href="./src/cloudflare/types/kv/namespace_delete_response.py">NamespaceDeleteResponse</a></code>

### Bulk

Types:

```python
from cloudflare.types.kv.namespaces import BulkUpdateResponse, BulkDeleteResponse
```

Methods:

- <code title="put /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk">client.kv.namespaces.bulk.<a href="./src/cloudflare/resources/kv/namespaces/bulk.py">update</a>(namespace_id, \*, account_id, \*\*<a href="src/cloudflare/types/kv/namespaces/bulk_update_params.py">params</a>) -> <a href="./src/cloudflare/types/kv/namespaces/bulk_update_response.py">BulkUpdateResponse</a></code>
- <code title="delete /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk">client.kv.namespaces.bulk.<a href="./src/cloudflare/resources/kv/namespaces/bulk.py">delete</a>(namespace_id, \*, account_id, \*\*<a href="src/cloudflare/types/kv/namespaces/bulk_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/kv/namespaces/bulk_delete_response.py">BulkDeleteResponse</a></code>

### Keys

Types:

```python
from cloudflare.types.kv.namespaces import KeyListResponse
```

Methods:

- <code title="get /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/keys">client.kv.namespaces.keys.<a href="./src/cloudflare/resources/kv/namespaces/keys.py">list</a>(namespace_id, \*, account_id, \*\*<a href="src/cloudflare/types/kv/namespaces/key_list_params.py">params</a>) -> <a href="./src/cloudflare/types/kv/namespaces/key_list_response.py">KeyListResponse</a></code>

### Metadata

Types:

```python
from cloudflare.types.kv.namespaces import MetadataGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/metadata/{key_name}">client.kv.namespaces.metadata.<a href="./src/cloudflare/resources/kv/namespaces/metadata.py">get</a>(key_name, \*, account_id, namespace_id) -> <a href="./src/cloudflare/types/kv/namespaces/metadata_get_response.py">object</a></code>

### Values

Types:

```python
from cloudflare.types.kv.namespaces import (
    ValueUpdateResponse,
    ValueDeleteResponse,
    ValueGetResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}">client.kv.namespaces.values.<a href="./src/cloudflare/resources/kv/namespaces/values.py">update</a>(key_name, \*, account_id, namespace_id, \*\*<a href="src/cloudflare/types/kv/namespaces/value_update_params.py">params</a>) -> <a href="./src/cloudflare/types/kv/namespaces/value_update_response.py">ValueUpdateResponse</a></code>
- <code title="delete /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}">client.kv.namespaces.values.<a href="./src/cloudflare/resources/kv/namespaces/values.py">delete</a>(key_name, \*, account_id, namespace_id) -> <a href="./src/cloudflare/types/kv/namespaces/value_delete_response.py">ValueDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}">client.kv.namespaces.values.<a href="./src/cloudflare/resources/kv/namespaces/values.py">get</a>(key_name, \*, account_id, namespace_id) -> str</code>

# DurableObjects

## Namespaces

Types:

```python
from cloudflare.types.durable_objects import NamespaceListResponse
```

Methods:

- <code title="get /accounts/{account_id}/workers/durable_objects/namespaces">client.durable_objects.namespaces.<a href="./src/cloudflare/resources/durable_objects/namespaces/namespaces.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/durable_objects/namespace_list_response.py">Optional</a></code>

### Objects

Types:

```python
from cloudflare.types.durable_objects.namespaces import ObjectListResponse
```

Methods:

- <code title="get /accounts/{account_id}/workers/durable_objects/namespaces/{id}/objects">client.durable_objects.namespaces.objects.<a href="./src/cloudflare/resources/durable_objects/namespaces/objects.py">list</a>(id, \*, account_id, \*\*<a href="src/cloudflare/types/durable_objects/namespaces/object_list_params.py">params</a>) -> <a href="./src/cloudflare/types/durable_objects/namespaces/object_list_response.py">Optional</a></code>

# Queues

Types:

```python
from cloudflare.types import (
    QueueCreateResponse,
    QueueUpdateResponse,
    QueueListResponse,
    QueueDeleteResponse,
    QueueGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/workers/queues">client.queues.<a href="./src/cloudflare/resources/queues/queues.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/queue_create_params.py">params</a>) -> <a href="./src/cloudflare/types/queue_create_response.py">Optional</a></code>
- <code title="put /accounts/{account_id}/workers/queues/{name}">client.queues.<a href="./src/cloudflare/resources/queues/queues.py">update</a>(name, \*, account_id, \*\*<a href="src/cloudflare/types/queue_update_params.py">params</a>) -> <a href="./src/cloudflare/types/queue_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/workers/queues">client.queues.<a href="./src/cloudflare/resources/queues/queues.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/queue_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/workers/queues/{name}">client.queues.<a href="./src/cloudflare/resources/queues/queues.py">delete</a>(name, \*, account_id) -> <a href="./src/cloudflare/types/queue_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/workers/queues/{name}">client.queues.<a href="./src/cloudflare/resources/queues/queues.py">get</a>(name, \*, account_id) -> <a href="./src/cloudflare/types/queue_get_response.py">Optional</a></code>

## Consumers

Types:

```python
from cloudflare.types.queues import (
    ConsumerCreateResponse,
    ConsumerUpdateResponse,
    ConsumerListResponse,
    ConsumerDeleteResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/workers/queues/{name}/consumers">client.queues.consumers.<a href="./src/cloudflare/resources/queues/consumers.py">create</a>(name, \*, account_id, \*\*<a href="src/cloudflare/types/queues/consumer_create_params.py">params</a>) -> <a href="./src/cloudflare/types/queues/consumer_create_response.py">Optional</a></code>
- <code title="put /accounts/{account_id}/workers/queues/{name}/consumers/{consumer_name}">client.queues.consumers.<a href="./src/cloudflare/resources/queues/consumers.py">update</a>(consumer_name, \*, account_id, name, \*\*<a href="src/cloudflare/types/queues/consumer_update_params.py">params</a>) -> <a href="./src/cloudflare/types/queues/consumer_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/workers/queues/{name}/consumers">client.queues.consumers.<a href="./src/cloudflare/resources/queues/consumers.py">list</a>(name, \*, account_id) -> <a href="./src/cloudflare/types/queues/consumer_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/workers/queues/{name}/consumers/{consumer_name}">client.queues.consumers.<a href="./src/cloudflare/resources/queues/consumers.py">delete</a>(consumer_name, \*, account_id, name) -> <a href="./src/cloudflare/types/queues/consumer_delete_response.py">Optional</a></code>

# ManagedHeaders

Types:

```python
from cloudflare.types import ManagedHeaderListResponse, ManagedHeaderEditResponse
```

Methods:

- <code title="get /zones/{zone_id}/managed_headers">client.managed_headers.<a href="./src/cloudflare/resources/managed_headers.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/managed_header_list_response.py">ManagedHeaderListResponse</a></code>
- <code title="patch /zones/{zone_id}/managed_headers">client.managed_headers.<a href="./src/cloudflare/resources/managed_headers.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/managed_header_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/managed_header_edit_response.py">ManagedHeaderEditResponse</a></code>

# PageShield

Types:

```python
from cloudflare.types import PageShieldUpdateResponse, PageShieldListResponse
```

Methods:

- <code title="put /zones/{zone_id}/page_shield">client.page_shield.<a href="./src/cloudflare/resources/page_shield/page_shield.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/page_shield_update_params.py">params</a>) -> <a href="./src/cloudflare/types/page_shield_update_response.py">PageShieldUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/page_shield">client.page_shield.<a href="./src/cloudflare/resources/page_shield/page_shield.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/page_shield_list_response.py">PageShieldListResponse</a></code>

## Policies

Types:

```python
from cloudflare.types.page_shield import (
    PolicyCreateResponse,
    PolicyUpdateResponse,
    PolicyListResponse,
    PolicyGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/page_shield/policies">client.page_shield.policies.<a href="./src/cloudflare/resources/page_shield/policies.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/page_shield/policy_create_params.py">params</a>) -> <a href="./src/cloudflare/types/page_shield/policy_create_response.py">PolicyCreateResponse</a></code>
- <code title="put /zones/{zone_id}/page_shield/policies/{policy_id}">client.page_shield.policies.<a href="./src/cloudflare/resources/page_shield/policies.py">update</a>(policy_id, \*, zone_id, \*\*<a href="src/cloudflare/types/page_shield/policy_update_params.py">params</a>) -> <a href="./src/cloudflare/types/page_shield/policy_update_response.py">PolicyUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/page_shield/policies">client.page_shield.policies.<a href="./src/cloudflare/resources/page_shield/policies.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/page_shield/policy_list_response.py">Optional</a></code>
- <code title="delete /zones/{zone_id}/page_shield/policies/{policy_id}">client.page_shield.policies.<a href="./src/cloudflare/resources/page_shield/policies.py">delete</a>(policy_id, \*, zone_id) -> None</code>
- <code title="get /zones/{zone_id}/page_shield/policies/{policy_id}">client.page_shield.policies.<a href="./src/cloudflare/resources/page_shield/policies.py">get</a>(policy_id, \*, zone_id) -> <a href="./src/cloudflare/types/page_shield/policy_get_response.py">PolicyGetResponse</a></code>

## Connections

Types:

```python
from cloudflare.types.page_shield import ConnectionListResponse, ConnectionGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/page_shield/connections">client.page_shield.connections.<a href="./src/cloudflare/resources/page_shield/connections.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/page_shield/connection_list_params.py">params</a>) -> <a href="./src/cloudflare/types/page_shield/connection_list_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/page_shield/connections/{connection_id}">client.page_shield.connections.<a href="./src/cloudflare/resources/page_shield/connections.py">get</a>(connection_id, \*, zone_id) -> <a href="./src/cloudflare/types/page_shield/connection_get_response.py">ConnectionGetResponse</a></code>

## Scripts

Types:

```python
from cloudflare.types.page_shield import ScriptListResponse, ScriptGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/page_shield/scripts">client.page_shield.scripts.<a href="./src/cloudflare/resources/page_shield/scripts.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/page_shield/script_list_params.py">params</a>) -> <a href="./src/cloudflare/types/page_shield/script_list_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/page_shield/scripts/{script_id}">client.page_shield.scripts.<a href="./src/cloudflare/resources/page_shield/scripts.py">get</a>(script_id, \*, zone_id) -> <a href="./src/cloudflare/types/page_shield/script_get_response.py">ScriptGetResponse</a></code>

# Rulesets

Types:

```python
from cloudflare.types import (
    RulesetCreateResponse,
    RulesetUpdateResponse,
    RulesetListResponse,
    RulesetGetResponse,
)
```

Methods:

- <code title="post /{account_or_zone}/{account_or_zone_id}/rulesets">client.rulesets.<a href="./src/cloudflare/resources/rulesets/rulesets.py">create</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/ruleset_create_params.py">params</a>) -> <a href="./src/cloudflare/types/ruleset_create_response.py">RulesetCreateResponse</a></code>
- <code title="put /{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}">client.rulesets.<a href="./src/cloudflare/resources/rulesets/rulesets.py">update</a>(ruleset_id, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/ruleset_update_params.py">params</a>) -> <a href="./src/cloudflare/types/ruleset_update_response.py">RulesetUpdateResponse</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/rulesets">client.rulesets.<a href="./src/cloudflare/resources/rulesets/rulesets.py">list</a>(\*, account_id, zone_id) -> <a href="./src/cloudflare/types/ruleset_list_response.py">RulesetListResponse</a></code>
- <code title="delete /{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}">client.rulesets.<a href="./src/cloudflare/resources/rulesets/rulesets.py">delete</a>(ruleset_id, \*, account_id, zone_id) -> None</code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}">client.rulesets.<a href="./src/cloudflare/resources/rulesets/rulesets.py">get</a>(ruleset_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/ruleset_get_response.py">RulesetGetResponse</a></code>

## Phases

Types:

```python
from cloudflare.types.rulesets import PhaseUpdateResponse, PhaseGetResponse
```

Methods:

- <code title="put /{account_or_zone}/{account_or_zone_id}/rulesets/phases/{ruleset_phase}/entrypoint">client.rulesets.phases.<a href="./src/cloudflare/resources/rulesets/phases/phases.py">update</a>(ruleset_phase, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/rulesets/phase_update_params.py">params</a>) -> <a href="./src/cloudflare/types/rulesets/phase_update_response.py">PhaseUpdateResponse</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/rulesets/phases/{ruleset_phase}/entrypoint">client.rulesets.phases.<a href="./src/cloudflare/resources/rulesets/phases/phases.py">get</a>(ruleset_phase, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/rulesets/phase_get_response.py">PhaseGetResponse</a></code>

### Versions

Types:

```python
from cloudflare.types.rulesets.phases import VersionListResponse, VersionGetResponse
```

Methods:

- <code title="get /{account_or_zone}/{account_or_zone_id}/rulesets/phases/{ruleset_phase}/entrypoint/versions">client.rulesets.phases.versions.<a href="./src/cloudflare/resources/rulesets/phases/versions.py">list</a>(ruleset_phase, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/rulesets/phases/version_list_response.py">VersionListResponse</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/rulesets/phases/{ruleset_phase}/entrypoint/versions/{ruleset_version}">client.rulesets.phases.versions.<a href="./src/cloudflare/resources/rulesets/phases/versions.py">get</a>(ruleset_version, \*, ruleset_phase, account_id, zone_id) -> <a href="./src/cloudflare/types/rulesets/phases/version_get_response.py">VersionGetResponse</a></code>

## Rules

Types:

```python
from cloudflare.types.rulesets import RuleCreateResponse, RuleDeleteResponse, RuleEditResponse
```

Methods:

- <code title="post /{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/rules">client.rulesets.rules.<a href="./src/cloudflare/resources/rulesets/rules.py">create</a>(ruleset_id, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/rulesets/rule_create_params.py">params</a>) -> <a href="./src/cloudflare/types/rulesets/rule_create_response.py">RuleCreateResponse</a></code>
- <code title="delete /{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/rules/{rule_id}">client.rulesets.rules.<a href="./src/cloudflare/resources/rulesets/rules.py">delete</a>(rule_id, \*, ruleset_id, account_id, zone_id) -> <a href="./src/cloudflare/types/rulesets/rule_delete_response.py">RuleDeleteResponse</a></code>
- <code title="patch /{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/rules/{rule_id}">client.rulesets.rules.<a href="./src/cloudflare/resources/rulesets/rules.py">edit</a>(rule_id, \*, ruleset_id, account_id, zone_id, \*\*<a href="src/cloudflare/types/rulesets/rule_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/rulesets/rule_edit_response.py">RuleEditResponse</a></code>

## Versions

Types:

```python
from cloudflare.types.rulesets import VersionListResponse, VersionGetResponse
```

Methods:

- <code title="get /{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/versions">client.rulesets.versions.<a href="./src/cloudflare/resources/rulesets/versions/versions.py">list</a>(ruleset_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/rulesets/version_list_response.py">VersionListResponse</a></code>
- <code title="delete /{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/versions/{ruleset_version}">client.rulesets.versions.<a href="./src/cloudflare/resources/rulesets/versions/versions.py">delete</a>(ruleset_version, \*, ruleset_id, account_id, zone_id) -> None</code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/versions/{ruleset_version}">client.rulesets.versions.<a href="./src/cloudflare/resources/rulesets/versions/versions.py">get</a>(ruleset_version, \*, ruleset_id, account_id, zone_id) -> <a href="./src/cloudflare/types/rulesets/version_get_response.py">VersionGetResponse</a></code>

### ByTags

Types:

```python
from cloudflare.types.rulesets.versions import ByTagGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/rulesets/{ruleset_id}/versions/{ruleset_version}/by_tag/{rule_tag}">client.rulesets.versions.by_tags.<a href="./src/cloudflare/resources/rulesets/versions/by_tags.py">get</a>(rule_tag, \*, account_id, ruleset_id, ruleset_version) -> <a href="./src/cloudflare/types/rulesets/versions/by_tag_get_response.py">ByTagGetResponse</a></code>

# URLNormalization

Types:

```python
from cloudflare.types import URLNormalizationUpdateResponse, URLNormalizationGetResponse
```

Methods:

- <code title="put /zones/{zone_id}/url_normalization">client.url_normalization.<a href="./src/cloudflare/resources/url_normalization.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/url_normalization_update_params.py">params</a>) -> <a href="./src/cloudflare/types/url_normalization_update_response.py">URLNormalizationUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/url_normalization">client.url_normalization.<a href="./src/cloudflare/resources/url_normalization.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/url_normalization_get_response.py">URLNormalizationGetResponse</a></code>

# Spectrum

## Analytics

### Aggregates

#### Currents

Types:

```python
from cloudflare.types.spectrum.analytics.aggregates import CurrentGetResponse
```

Methods:

- <code title="get /zones/{zone}/spectrum/analytics/aggregate/current">client.spectrum.analytics.aggregates.currents.<a href="./src/cloudflare/resources/spectrum/analytics/aggregates/currents.py">get</a>(zone, \*\*<a href="src/cloudflare/types/spectrum/analytics/aggregates/current_get_params.py">params</a>) -> <a href="./src/cloudflare/types/spectrum/analytics/aggregates/current_get_response.py">CurrentGetResponse</a></code>

### Events

#### Bytimes

Types:

```python
from cloudflare.types.spectrum.analytics.events import BytimeGetResponse
```

Methods:

- <code title="get /zones/{zone}/spectrum/analytics/events/bytime">client.spectrum.analytics.events.bytimes.<a href="./src/cloudflare/resources/spectrum/analytics/events/bytimes.py">get</a>(zone, \*\*<a href="src/cloudflare/types/spectrum/analytics/events/bytime_get_params.py">params</a>) -> <a href="./src/cloudflare/types/spectrum/analytics/events/bytime_get_response.py">Optional</a></code>

#### Summaries

Types:

```python
from cloudflare.types.spectrum.analytics.events import SummaryGetResponse
```

Methods:

- <code title="get /zones/{zone}/spectrum/analytics/events/summary">client.spectrum.analytics.events.summaries.<a href="./src/cloudflare/resources/spectrum/analytics/events/summaries.py">get</a>(zone, \*\*<a href="src/cloudflare/types/spectrum/analytics/events/summary_get_params.py">params</a>) -> <a href="./src/cloudflare/types/spectrum/analytics/events/summary_get_response.py">Optional</a></code>

## Apps

Types:

```python
from cloudflare.types.spectrum import (
    AppCreateResponse,
    AppUpdateResponse,
    AppListResponse,
    AppDeleteResponse,
    AppGetResponse,
)
```

Methods:

- <code title="post /zones/{zone}/spectrum/apps">client.spectrum.apps.<a href="./src/cloudflare/resources/spectrum/apps.py">create</a>(zone, \*\*<a href="src/cloudflare/types/spectrum/app_create_params.py">params</a>) -> <a href="./src/cloudflare/types/spectrum/app_create_response.py">Optional</a></code>
- <code title="put /zones/{zone}/spectrum/apps/{app_id}">client.spectrum.apps.<a href="./src/cloudflare/resources/spectrum/apps.py">update</a>(app_id, \*, zone, \*\*<a href="src/cloudflare/types/spectrum/app_update_params.py">params</a>) -> <a href="./src/cloudflare/types/spectrum/app_update_response.py">Optional</a></code>
- <code title="get /zones/{zone}/spectrum/apps">client.spectrum.apps.<a href="./src/cloudflare/resources/spectrum/apps.py">list</a>(zone, \*\*<a href="src/cloudflare/types/spectrum/app_list_params.py">params</a>) -> <a href="./src/cloudflare/types/spectrum/app_list_response.py">SyncV4PagePaginationArray[object]</a></code>
- <code title="delete /zones/{zone}/spectrum/apps/{app_id}">client.spectrum.apps.<a href="./src/cloudflare/resources/spectrum/apps.py">delete</a>(app_id, \*, zone) -> <a href="./src/cloudflare/types/spectrum/app_delete_response.py">Optional</a></code>
- <code title="get /zones/{zone}/spectrum/apps/{app_id}">client.spectrum.apps.<a href="./src/cloudflare/resources/spectrum/apps.py">get</a>(app_id, \*, zone) -> <a href="./src/cloudflare/types/spectrum/app_get_response.py">Optional</a></code>

# Addressing

## Services

Types:

```python
from cloudflare.types.addressing import ServiceListResponse
```

Methods:

- <code title="get /accounts/{account_id}/addressing/services">client.addressing.services.<a href="./src/cloudflare/resources/addressing/services.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/addressing/service_list_response.py">ServiceListResponse</a></code>

## AddressMaps

Types:

```python
from cloudflare.types.addressing import (
    AddressMapCreateResponse,
    AddressMapListResponse,
    AddressMapDeleteResponse,
    AddressMapEditResponse,
    AddressMapGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/addressing/address_maps">client.addressing.address_maps.<a href="./src/cloudflare/resources/addressing/address_maps/address_maps.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/addressing/address_map_create_params.py">params</a>) -> <a href="./src/cloudflare/types/addressing/address_map_create_response.py">AddressMapCreateResponse</a></code>
- <code title="get /accounts/{account_id}/addressing/address_maps">client.addressing.address_maps.<a href="./src/cloudflare/resources/addressing/address_maps/address_maps.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/addressing/address_map_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/addressing/address_maps/{address_map_id}">client.addressing.address_maps.<a href="./src/cloudflare/resources/addressing/address_maps/address_maps.py">delete</a>(address_map_id, \*, account_id) -> <a href="./src/cloudflare/types/addressing/address_map_delete_response.py">Optional</a></code>
- <code title="patch /accounts/{account_id}/addressing/address_maps/{address_map_id}">client.addressing.address_maps.<a href="./src/cloudflare/resources/addressing/address_maps/address_maps.py">edit</a>(address_map_id, \*, account_id, \*\*<a href="src/cloudflare/types/addressing/address_map_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/addressing/address_map_edit_response.py">AddressMapEditResponse</a></code>
- <code title="get /accounts/{account_id}/addressing/address_maps/{address_map_id}">client.addressing.address_maps.<a href="./src/cloudflare/resources/addressing/address_maps/address_maps.py">get</a>(address_map_id, \*, account_id) -> <a href="./src/cloudflare/types/addressing/address_map_get_response.py">AddressMapGetResponse</a></code>

### Accounts

Types:

```python
from cloudflare.types.addressing.address_maps import AccountUpdateResponse, AccountDeleteResponse
```

Methods:

- <code title="put /accounts/{account_id}/addressing/address_maps/{address_map_id}/accounts/{account_id}">client.addressing.address_maps.accounts.<a href="./src/cloudflare/resources/addressing/address_maps/accounts.py">update</a>(address_map_id, \*, account_id) -> <a href="./src/cloudflare/types/addressing/address_maps/account_update_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/addressing/address_maps/{address_map_id}/accounts/{account_id}">client.addressing.address_maps.accounts.<a href="./src/cloudflare/resources/addressing/address_maps/accounts.py">delete</a>(address_map_id, \*, account_id) -> <a href="./src/cloudflare/types/addressing/address_maps/account_delete_response.py">Optional</a></code>

### IPs

Types:

```python
from cloudflare.types.addressing.address_maps import IPUpdateResponse, IPDeleteResponse
```

Methods:

- <code title="put /accounts/{account_id}/addressing/address_maps/{address_map_id}/ips/{ip_address}">client.addressing.address_maps.ips.<a href="./src/cloudflare/resources/addressing/address_maps/ips.py">update</a>(ip_address, \*, account_id, address_map_id) -> <a href="./src/cloudflare/types/addressing/address_maps/ip_update_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/addressing/address_maps/{address_map_id}/ips/{ip_address}">client.addressing.address_maps.ips.<a href="./src/cloudflare/resources/addressing/address_maps/ips.py">delete</a>(ip_address, \*, account_id, address_map_id) -> <a href="./src/cloudflare/types/addressing/address_maps/ip_delete_response.py">Optional</a></code>

### Zones

Types:

```python
from cloudflare.types.addressing.address_maps import ZoneUpdateResponse, ZoneDeleteResponse
```

Methods:

- <code title="put /accounts/{account_id}/addressing/address_maps/{address_map_id}/zones/{zone_id}">client.addressing.address_maps.zones.<a href="./src/cloudflare/resources/addressing/address_maps/zones.py">update</a>(address_map_id, \*, zone_id, account_id) -> <a href="./src/cloudflare/types/addressing/address_maps/zone_update_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/addressing/address_maps/{address_map_id}/zones/{zone_id}">client.addressing.address_maps.zones.<a href="./src/cloudflare/resources/addressing/address_maps/zones.py">delete</a>(address_map_id, \*, zone_id, account_id) -> <a href="./src/cloudflare/types/addressing/address_maps/zone_delete_response.py">Optional</a></code>

## LOADocuments

Types:

```python
from cloudflare.types.addressing import LOADocumentCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/addressing/loa_documents">client.addressing.loa_documents.<a href="./src/cloudflare/resources/addressing/loa_documents/loa_documents.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/addressing/loa_document_create_params.py">params</a>) -> <a href="./src/cloudflare/types/addressing/loa_document_create_response.py">LOADocumentCreateResponse</a></code>

### Downloads

Types:

```python
from cloudflare.types.addressing.loa_documents import DownloadListResponse
```

Methods:

- <code title="get /accounts/{account_id}/addressing/loa_documents/{loa_document_id}/download">client.addressing.loa_documents.downloads.<a href="./src/cloudflare/resources/addressing/loa_documents/downloads.py">list</a>(loa_document_id, \*, account_id) -> <a href="./src/cloudflare/types/addressing/loa_documents/download_list_response.py">object</a></code>

## Prefixes

Types:

```python
from cloudflare.types.addressing import (
    PrefixCreateResponse,
    PrefixListResponse,
    PrefixDeleteResponse,
    PrefixEditResponse,
    PrefixGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/addressing/prefixes">client.addressing.prefixes.<a href="./src/cloudflare/resources/addressing/prefixes/prefixes.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/addressing/prefix_create_params.py">params</a>) -> <a href="./src/cloudflare/types/addressing/prefix_create_response.py">PrefixCreateResponse</a></code>
- <code title="get /accounts/{account_id}/addressing/prefixes">client.addressing.prefixes.<a href="./src/cloudflare/resources/addressing/prefixes/prefixes.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/addressing/prefix_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/addressing/prefixes/{prefix_id}">client.addressing.prefixes.<a href="./src/cloudflare/resources/addressing/prefixes/prefixes.py">delete</a>(prefix_id, \*, account_id) -> <a href="./src/cloudflare/types/addressing/prefix_delete_response.py">Optional</a></code>
- <code title="patch /accounts/{account_id}/addressing/prefixes/{prefix_id}">client.addressing.prefixes.<a href="./src/cloudflare/resources/addressing/prefixes/prefixes.py">edit</a>(prefix_id, \*, account_id, \*\*<a href="src/cloudflare/types/addressing/prefix_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/addressing/prefix_edit_response.py">PrefixEditResponse</a></code>
- <code title="get /accounts/{account_id}/addressing/prefixes/{prefix_id}">client.addressing.prefixes.<a href="./src/cloudflare/resources/addressing/prefixes/prefixes.py">get</a>(prefix_id, \*, account_id) -> <a href="./src/cloudflare/types/addressing/prefix_get_response.py">PrefixGetResponse</a></code>

### BGP

#### Bindings

Types:

```python
from cloudflare.types.addressing.prefixes.bgp import (
    BindingCreateResponse,
    BindingListResponse,
    BindingDeleteResponse,
    BindingGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings">client.addressing.prefixes.bgp.bindings.<a href="./src/cloudflare/resources/addressing/prefixes/bgp/bindings.py">create</a>(prefix_id, \*, account_id, \*\*<a href="src/cloudflare/types/addressing/prefixes/bgp/binding_create_params.py">params</a>) -> <a href="./src/cloudflare/types/addressing/prefixes/bgp/binding_create_response.py">BindingCreateResponse</a></code>
- <code title="get /accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings">client.addressing.prefixes.bgp.bindings.<a href="./src/cloudflare/resources/addressing/prefixes/bgp/bindings.py">list</a>(prefix_id, \*, account_id) -> <a href="./src/cloudflare/types/addressing/prefixes/bgp/binding_list_response.py">BindingListResponse</a></code>
- <code title="delete /accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings/{binding_id}">client.addressing.prefixes.bgp.bindings.<a href="./src/cloudflare/resources/addressing/prefixes/bgp/bindings.py">delete</a>(binding_id, \*, account_id, prefix_id) -> <a href="./src/cloudflare/types/addressing/prefixes/bgp/binding_delete_response.py">BindingDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings/{binding_id}">client.addressing.prefixes.bgp.bindings.<a href="./src/cloudflare/resources/addressing/prefixes/bgp/bindings.py">get</a>(binding_id, \*, account_id, prefix_id) -> <a href="./src/cloudflare/types/addressing/prefixes/bgp/binding_get_response.py">BindingGetResponse</a></code>

#### Prefixes

Types:

```python
from cloudflare.types.addressing.prefixes.bgp import (
    PrefixListResponse,
    PrefixEditResponse,
    PrefixGetResponse,
)
```

Methods:

- <code title="get /accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/prefixes">client.addressing.prefixes.bgp.prefixes.<a href="./src/cloudflare/resources/addressing/prefixes/bgp/prefixes.py">list</a>(prefix_id, \*, account_id) -> <a href="./src/cloudflare/types/addressing/prefixes/bgp/prefix_list_response.py">Optional</a></code>
- <code title="patch /accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/prefixes/{bgp_prefix_id}">client.addressing.prefixes.bgp.prefixes.<a href="./src/cloudflare/resources/addressing/prefixes/bgp/prefixes.py">edit</a>(bgp_prefix_id, \*, account_id, prefix_id, \*\*<a href="src/cloudflare/types/addressing/prefixes/bgp/prefix_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/addressing/prefixes/bgp/prefix_edit_response.py">PrefixEditResponse</a></code>
- <code title="get /accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/prefixes/{bgp_prefix_id}">client.addressing.prefixes.bgp.prefixes.<a href="./src/cloudflare/resources/addressing/prefixes/bgp/prefixes.py">get</a>(bgp_prefix_id, \*, account_id, prefix_id) -> <a href="./src/cloudflare/types/addressing/prefixes/bgp/prefix_get_response.py">PrefixGetResponse</a></code>

#### Statuses

Types:

```python
from cloudflare.types.addressing.prefixes.bgp import StatusEditResponse, StatusGetResponse
```

Methods:

- <code title="patch /accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/status">client.addressing.prefixes.bgp.statuses.<a href="./src/cloudflare/resources/addressing/prefixes/bgp/statuses.py">edit</a>(prefix_id, \*, account_id, \*\*<a href="src/cloudflare/types/addressing/prefixes/bgp/status_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/addressing/prefixes/bgp/status_edit_response.py">StatusEditResponse</a></code>
- <code title="get /accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/status">client.addressing.prefixes.bgp.statuses.<a href="./src/cloudflare/resources/addressing/prefixes/bgp/statuses.py">get</a>(prefix_id, \*, account_id) -> <a href="./src/cloudflare/types/addressing/prefixes/bgp/status_get_response.py">StatusGetResponse</a></code>

### Delegations

Types:

```python
from cloudflare.types.addressing.prefixes import (
    DelegationCreateResponse,
    DelegationListResponse,
    DelegationDeleteResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/addressing/prefixes/{prefix_id}/delegations">client.addressing.prefixes.delegations.<a href="./src/cloudflare/resources/addressing/prefixes/delegations.py">create</a>(prefix_id, \*, account_id, \*\*<a href="src/cloudflare/types/addressing/prefixes/delegation_create_params.py">params</a>) -> <a href="./src/cloudflare/types/addressing/prefixes/delegation_create_response.py">DelegationCreateResponse</a></code>
- <code title="get /accounts/{account_id}/addressing/prefixes/{prefix_id}/delegations">client.addressing.prefixes.delegations.<a href="./src/cloudflare/resources/addressing/prefixes/delegations.py">list</a>(prefix_id, \*, account_id) -> <a href="./src/cloudflare/types/addressing/prefixes/delegation_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/addressing/prefixes/{prefix_id}/delegations/{delegation_id}">client.addressing.prefixes.delegations.<a href="./src/cloudflare/resources/addressing/prefixes/delegations.py">delete</a>(delegation_id, \*, account_id, prefix_id) -> <a href="./src/cloudflare/types/addressing/prefixes/delegation_delete_response.py">DelegationDeleteResponse</a></code>

# AuditLogs

Types:

```python
from cloudflare.types import AuditLogListResponse
```

Methods:

- <code title="get /accounts/{account_identifier}/audit_logs">client.audit_logs.<a href="./src/cloudflare/resources/audit_logs.py">list</a>(account_identifier, \*\*<a href="src/cloudflare/types/audit_log_list_params.py">params</a>) -> <a href="./src/cloudflare/types/audit_log_list_response.py">SyncV4PagePaginationArray[AuditLogListResponse]</a></code>

# Billing

## Profiles

Types:

```python
from cloudflare.types.billing import ProfileGetResponse
```

Methods:

- <code title="get /accounts/{account_identifier}/billing/profile">client.billing.profiles.<a href="./src/cloudflare/resources/billing/profiles.py">get</a>(account_identifier) -> <a href="./src/cloudflare/types/billing/profile_get_response.py">ProfileGetResponse</a></code>

# BrandProtection

Types:

```python
from cloudflare.types import BrandProtectionSubmitResponse, BrandProtectionURLInfoResponse
```

Methods:

- <code title="post /accounts/{account_id}/brand-protection/submit">client.brand_protection.<a href="./src/cloudflare/resources/brand_protection.py">submit</a>(\*, account_id, \*\*<a href="src/cloudflare/types/brand_protection_submit_params.py">params</a>) -> <a href="./src/cloudflare/types/brand_protection_submit_response.py">BrandProtectionSubmitResponse</a></code>
- <code title="get /accounts/{account_id}/brand-protection/url-info">client.brand_protection.<a href="./src/cloudflare/resources/brand_protection.py">url_info</a>(\*, account_id, \*\*<a href="src/cloudflare/types/brand_protection_url_info_params.py">params</a>) -> <a href="./src/cloudflare/types/brand_protection_url_info_response.py">BrandProtectionURLInfoResponse</a></code>

# Diagnostics

## Traceroutes

Types:

```python
from cloudflare.types.diagnostics import TracerouteCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/diagnostics/traceroute">client.diagnostics.traceroutes.<a href="./src/cloudflare/resources/diagnostics/traceroutes.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/diagnostics/traceroute_create_params.py">params</a>) -> <a href="./src/cloudflare/types/diagnostics/traceroute_create_response.py">Optional</a></code>

# Images

## V1

Types:

```python
from cloudflare.types.images import (
    V1CreateResponse,
    V1ListResponse,
    V1DeleteResponse,
    V1EditResponse,
    V1GetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/images/v1">client.images.v1.<a href="./src/cloudflare/resources/images/v1/v1.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/images/v1_create_params.py">params</a>) -> <a href="./src/cloudflare/types/images/v1_create_response.py">V1CreateResponse</a></code>
- <code title="get /accounts/{account_id}/images/v1">client.images.v1.<a href="./src/cloudflare/resources/images/v1/v1.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/images/v1_list_params.py">params</a>) -> <a href="./src/cloudflare/types/images/v1_list_response.py">SyncV4PagePagination[V1ListResponse]</a></code>
- <code title="delete /accounts/{account_id}/images/v1/{image_id}">client.images.v1.<a href="./src/cloudflare/resources/images/v1/v1.py">delete</a>(image_id, \*, account_id) -> <a href="./src/cloudflare/types/images/v1_delete_response.py">V1DeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/images/v1/{image_id}">client.images.v1.<a href="./src/cloudflare/resources/images/v1/v1.py">edit</a>(image_id, \*, account_id, \*\*<a href="src/cloudflare/types/images/v1_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/images/v1_edit_response.py">V1EditResponse</a></code>
- <code title="get /accounts/{account_id}/images/v1/{image_id}">client.images.v1.<a href="./src/cloudflare/resources/images/v1/v1.py">get</a>(image_id, \*, account_id) -> <a href="./src/cloudflare/types/images/v1_get_response.py">V1GetResponse</a></code>

### Keys

Types:

```python
from cloudflare.types.images.v1 import KeyListResponse
```

Methods:

- <code title="get /accounts/{account_id}/images/v1/keys">client.images.v1.keys.<a href="./src/cloudflare/resources/images/v1/keys.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/images/v1/key_list_response.py">KeyListResponse</a></code>

### Stats

Types:

```python
from cloudflare.types.images.v1 import StatGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/images/v1/stats">client.images.v1.stats.<a href="./src/cloudflare/resources/images/v1/stats.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/images/v1/stat_get_response.py">StatGetResponse</a></code>

### Variants

Types:

```python
from cloudflare.types.images.v1 import (
    VariantCreateResponse,
    VariantListResponse,
    VariantDeleteResponse,
    VariantEditResponse,
    VariantGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/images/v1/variants">client.images.v1.variants.<a href="./src/cloudflare/resources/images/v1/variants.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/images/v1/variant_create_params.py">params</a>) -> <a href="./src/cloudflare/types/images/v1/variant_create_response.py">VariantCreateResponse</a></code>
- <code title="get /accounts/{account_id}/images/v1/variants">client.images.v1.variants.<a href="./src/cloudflare/resources/images/v1/variants.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/images/v1/variant_list_response.py">VariantListResponse</a></code>
- <code title="delete /accounts/{account_id}/images/v1/variants/{variant_id}">client.images.v1.variants.<a href="./src/cloudflare/resources/images/v1/variants.py">delete</a>(variant_id, \*, account_id) -> <a href="./src/cloudflare/types/images/v1/variant_delete_response.py">VariantDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/images/v1/variants/{variant_id}">client.images.v1.variants.<a href="./src/cloudflare/resources/images/v1/variants.py">edit</a>(variant_id, \*, account_id, \*\*<a href="src/cloudflare/types/images/v1/variant_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/images/v1/variant_edit_response.py">VariantEditResponse</a></code>
- <code title="get /accounts/{account_id}/images/v1/variants/{variant_id}">client.images.v1.variants.<a href="./src/cloudflare/resources/images/v1/variants.py">get</a>(variant_id, \*, account_id) -> <a href="./src/cloudflare/types/images/v1/variant_get_response.py">VariantGetResponse</a></code>

### Blobs

Methods:

- <code title="get /accounts/{account_id}/images/v1/{image_id}/blob">client.images.v1.blobs.<a href="./src/cloudflare/resources/images/v1/blobs.py">get</a>(image_id, \*, account_id) -> BinaryAPIResponse</code>

## V2

Types:

```python
from cloudflare.types.images import V2ListResponse
```

Methods:

- <code title="get /accounts/{account_id}/images/v2">client.images.v2.<a href="./src/cloudflare/resources/images/v2/v2.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/images/v2_list_params.py">params</a>) -> <a href="./src/cloudflare/types/images/v2_list_response.py">V2ListResponse</a></code>

### DirectUploads

Types:

```python
from cloudflare.types.images.v2 import DirectUploadCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/images/v2/direct_upload">client.images.v2.direct_uploads.<a href="./src/cloudflare/resources/images/v2/direct_uploads.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/images/v2/direct_upload_create_params.py">params</a>) -> <a href="./src/cloudflare/types/images/v2/direct_upload_create_response.py">DirectUploadCreateResponse</a></code>

# Intel

## ASN

Types:

```python
from cloudflare.types.intel import ASNGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/intel/asn/{asn}">client.intel.asn.<a href="./src/cloudflare/resources/intel/asn/asn.py">get</a>(asn, \*, account_id) -> <a href="./src/cloudflare/types/intel/asn_get_response.py">ASNGetResponse</a></code>

### Subnets

Types:

```python
from cloudflare.types.intel.asn import SubnetListResponse
```

Methods:

- <code title="get /accounts/{account_id}/intel/asn/{asn}/subnets">client.intel.asn.subnets.<a href="./src/cloudflare/resources/intel/asn/subnets.py">list</a>(asn, \*, account_id) -> <a href="./src/cloudflare/types/intel/asn/subnet_list_response.py">SubnetListResponse</a></code>

## DNS

Types:

```python
from cloudflare.types.intel import DNSGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/intel/dns">client.intel.dns.<a href="./src/cloudflare/resources/intel/dns.py">get</a>(\*, account_id, \*\*<a href="src/cloudflare/types/intel/dns_get_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/dns_get_response.py">DNSGetResponse</a></code>

## Domains

Types:

```python
from cloudflare.types.intel import DomainGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/intel/domain">client.intel.domains.<a href="./src/cloudflare/resources/intel/domains/domains.py">get</a>(\*, account_id, \*\*<a href="src/cloudflare/types/intel/domain_get_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/domain_get_response.py">DomainGetResponse</a></code>

### Bulks

Types:

```python
from cloudflare.types.intel.domains import BulkGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/intel/domain/bulk">client.intel.domains.bulks.<a href="./src/cloudflare/resources/intel/domains/bulks.py">get</a>(\*, account_id, \*\*<a href="src/cloudflare/types/intel/domains/bulk_get_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/domains/bulk_get_response.py">Optional</a></code>

## DomainHistories

Types:

```python
from cloudflare.types.intel import DomainHistoryListResponse
```

Methods:

- <code title="get /accounts/{account_id}/intel/domain-history">client.intel.domain_histories.<a href="./src/cloudflare/resources/intel/domain_histories.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/intel/domain_history_list_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/domain_history_list_response.py">Optional</a></code>

## IPs

Types:

```python
from cloudflare.types.intel import IPGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/intel/ip">client.intel.ips.<a href="./src/cloudflare/resources/intel/ips.py">get</a>(\*, account_id, \*\*<a href="src/cloudflare/types/intel/ip_get_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/ip_get_response.py">Optional</a></code>

## IPLists

Types:

```python
from cloudflare.types.intel import IPListGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/intel/ip-list">client.intel.ip_lists.<a href="./src/cloudflare/resources/intel/ip_lists.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/intel/ip_list_get_response.py">Optional</a></code>

## Miscategorizations

Types:

```python
from cloudflare.types.intel import MiscategorizationCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/intel/miscategorization">client.intel.miscategorizations.<a href="./src/cloudflare/resources/intel/miscategorizations.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/intel/miscategorization_create_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/miscategorization_create_response.py">MiscategorizationCreateResponse</a></code>

## Whois

Types:

```python
from cloudflare.types.intel import WhoisGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/intel/whois">client.intel.whois.<a href="./src/cloudflare/resources/intel/whois.py">get</a>(\*, account_id, \*\*<a href="src/cloudflare/types/intel/whois_get_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/whois_get_response.py">WhoisGetResponse</a></code>

## IndicatorFeeds

Types:

```python
from cloudflare.types.intel import (
    IndicatorFeedCreateResponse,
    IndicatorFeedUpdateResponse,
    IndicatorFeedListResponse,
    IndicatorFeedDataResponse,
    IndicatorFeedGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/intel/indicator-feeds">client.intel.indicator_feeds.<a href="./src/cloudflare/resources/intel/indicator_feeds/indicator_feeds.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/intel/indicator_feed_create_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/indicator_feed_create_response.py">IndicatorFeedCreateResponse</a></code>
- <code title="put /accounts/{account_id}/intel/indicator-feeds/{feed_id}/snapshot">client.intel.indicator_feeds.<a href="./src/cloudflare/resources/intel/indicator_feeds/indicator_feeds.py">update</a>(feed_id, \*, account_id, \*\*<a href="src/cloudflare/types/intel/indicator_feed_update_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/indicator_feed_update_response.py">IndicatorFeedUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/intel/indicator-feeds">client.intel.indicator_feeds.<a href="./src/cloudflare/resources/intel/indicator_feeds/indicator_feeds.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/intel/indicator_feed_list_response.py">IndicatorFeedListResponse</a></code>
- <code title="get /accounts/{account_id}/intel/indicator-feeds/{feed_id}/data">client.intel.indicator_feeds.<a href="./src/cloudflare/resources/intel/indicator_feeds/indicator_feeds.py">data</a>(feed_id, \*, account_id) -> str</code>
- <code title="get /accounts/{account_id}/intel/indicator-feeds/{feed_id}">client.intel.indicator_feeds.<a href="./src/cloudflare/resources/intel/indicator_feeds/indicator_feeds.py">get</a>(feed_id, \*, account_id) -> <a href="./src/cloudflare/types/intel/indicator_feed_get_response.py">IndicatorFeedGetResponse</a></code>

### Permissions

Types:

```python
from cloudflare.types.intel.indicator_feeds import (
    PermissionCreateResponse,
    PermissionListResponse,
    PermissionDeleteResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/intel/indicator-feeds/permissions/add">client.intel.indicator_feeds.permissions.<a href="./src/cloudflare/resources/intel/indicator_feeds/permissions.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/intel/indicator_feeds/permission_create_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/indicator_feeds/permission_create_response.py">PermissionCreateResponse</a></code>
- <code title="get /accounts/{account_id}/intel/indicator-feeds/permissions/view">client.intel.indicator_feeds.permissions.<a href="./src/cloudflare/resources/intel/indicator_feeds/permissions.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/intel/indicator_feeds/permission_list_response.py">PermissionListResponse</a></code>
- <code title="put /accounts/{account_id}/intel/indicator-feeds/permissions/remove">client.intel.indicator_feeds.permissions.<a href="./src/cloudflare/resources/intel/indicator_feeds/permissions.py">delete</a>(\*, account_id, \*\*<a href="src/cloudflare/types/intel/indicator_feeds/permission_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/indicator_feeds/permission_delete_response.py">PermissionDeleteResponse</a></code>

## Sinkholes

Types:

```python
from cloudflare.types.intel import SinkholeListResponse
```

Methods:

- <code title="get /accounts/{account_id}/intel/sinkholes">client.intel.sinkholes.<a href="./src/cloudflare/resources/intel/sinkholes.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/intel/sinkhole_list_response.py">SinkholeListResponse</a></code>

# MagicTransit

## CfInterconnects

Types:

```python
from cloudflare.types.magic_transit import (
    CfInterconnectUpdateResponse,
    CfInterconnectListResponse,
    CfInterconnectGetResponse,
)
```

Methods:

- <code title="put /accounts/{account_identifier}/magic/cf_interconnects/{tunnel_identifier}">client.magic_transit.cf_interconnects.<a href="./src/cloudflare/resources/magic_transit/cf_interconnects.py">update</a>(tunnel_identifier, \*, account_identifier, \*\*<a href="src/cloudflare/types/magic_transit/cf_interconnect_update_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/cf_interconnect_update_response.py">CfInterconnectUpdateResponse</a></code>
- <code title="get /accounts/{account_identifier}/magic/cf_interconnects">client.magic_transit.cf_interconnects.<a href="./src/cloudflare/resources/magic_transit/cf_interconnects.py">list</a>(account_identifier) -> <a href="./src/cloudflare/types/magic_transit/cf_interconnect_list_response.py">CfInterconnectListResponse</a></code>
- <code title="get /accounts/{account_identifier}/magic/cf_interconnects/{tunnel_identifier}">client.magic_transit.cf_interconnects.<a href="./src/cloudflare/resources/magic_transit/cf_interconnects.py">get</a>(tunnel_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/magic_transit/cf_interconnect_get_response.py">CfInterconnectGetResponse</a></code>

## GRETunnels

Types:

```python
from cloudflare.types.magic_transit import (
    GRETunnelCreateResponse,
    GRETunnelUpdateResponse,
    GRETunnelListResponse,
    GRETunnelDeleteResponse,
    GRETunnelGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_identifier}/magic/gre_tunnels">client.magic_transit.gre_tunnels.<a href="./src/cloudflare/resources/magic_transit/gre_tunnels.py">create</a>(account_identifier, \*\*<a href="src/cloudflare/types/magic_transit/gre_tunnel_create_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/gre_tunnel_create_response.py">GRETunnelCreateResponse</a></code>
- <code title="put /accounts/{account_identifier}/magic/gre_tunnels/{tunnel_identifier}">client.magic_transit.gre_tunnels.<a href="./src/cloudflare/resources/magic_transit/gre_tunnels.py">update</a>(tunnel_identifier, \*, account_identifier, \*\*<a href="src/cloudflare/types/magic_transit/gre_tunnel_update_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/gre_tunnel_update_response.py">GRETunnelUpdateResponse</a></code>
- <code title="get /accounts/{account_identifier}/magic/gre_tunnels">client.magic_transit.gre_tunnels.<a href="./src/cloudflare/resources/magic_transit/gre_tunnels.py">list</a>(account_identifier) -> <a href="./src/cloudflare/types/magic_transit/gre_tunnel_list_response.py">GRETunnelListResponse</a></code>
- <code title="delete /accounts/{account_identifier}/magic/gre_tunnels/{tunnel_identifier}">client.magic_transit.gre_tunnels.<a href="./src/cloudflare/resources/magic_transit/gre_tunnels.py">delete</a>(tunnel_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/magic_transit/gre_tunnel_delete_response.py">GRETunnelDeleteResponse</a></code>
- <code title="get /accounts/{account_identifier}/magic/gre_tunnels/{tunnel_identifier}">client.magic_transit.gre_tunnels.<a href="./src/cloudflare/resources/magic_transit/gre_tunnels.py">get</a>(tunnel_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/magic_transit/gre_tunnel_get_response.py">GRETunnelGetResponse</a></code>

## IPSECTunnels

Types:

```python
from cloudflare.types.magic_transit import (
    IPSECTunnelCreateResponse,
    IPSECTunnelUpdateResponse,
    IPSECTunnelListResponse,
    IPSECTunnelDeleteResponse,
    IPSECTunnelGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_identifier}/magic/ipsec_tunnels">client.magic_transit.ipsec_tunnels.<a href="./src/cloudflare/resources/magic_transit/ipsec_tunnels/ipsec_tunnels.py">create</a>(account_identifier, \*\*<a href="src/cloudflare/types/magic_transit/ipsec_tunnel_create_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/ipsec_tunnel_create_response.py">IPSECTunnelCreateResponse</a></code>
- <code title="put /accounts/{account_identifier}/magic/ipsec_tunnels/{tunnel_identifier}">client.magic_transit.ipsec_tunnels.<a href="./src/cloudflare/resources/magic_transit/ipsec_tunnels/ipsec_tunnels.py">update</a>(tunnel_identifier, \*, account_identifier, \*\*<a href="src/cloudflare/types/magic_transit/ipsec_tunnel_update_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/ipsec_tunnel_update_response.py">IPSECTunnelUpdateResponse</a></code>
- <code title="get /accounts/{account_identifier}/magic/ipsec_tunnels">client.magic_transit.ipsec_tunnels.<a href="./src/cloudflare/resources/magic_transit/ipsec_tunnels/ipsec_tunnels.py">list</a>(account_identifier) -> <a href="./src/cloudflare/types/magic_transit/ipsec_tunnel_list_response.py">IPSECTunnelListResponse</a></code>
- <code title="delete /accounts/{account_identifier}/magic/ipsec_tunnels/{tunnel_identifier}">client.magic_transit.ipsec_tunnels.<a href="./src/cloudflare/resources/magic_transit/ipsec_tunnels/ipsec_tunnels.py">delete</a>(tunnel_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/magic_transit/ipsec_tunnel_delete_response.py">IPSECTunnelDeleteResponse</a></code>
- <code title="get /accounts/{account_identifier}/magic/ipsec_tunnels/{tunnel_identifier}">client.magic_transit.ipsec_tunnels.<a href="./src/cloudflare/resources/magic_transit/ipsec_tunnels/ipsec_tunnels.py">get</a>(tunnel_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/magic_transit/ipsec_tunnel_get_response.py">IPSECTunnelGetResponse</a></code>

### PSKGenerates

Types:

```python
from cloudflare.types.magic_transit.ipsec_tunnels import PSKGenerateCreateResponse
```

Methods:

- <code title="post /accounts/{account_identifier}/magic/ipsec_tunnels/{tunnel_identifier}/psk_generate">client.magic_transit.ipsec_tunnels.psk_generates.<a href="./src/cloudflare/resources/magic_transit/ipsec_tunnels/psk_generates.py">create</a>(tunnel_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/magic_transit/ipsec_tunnels/psk_generate_create_response.py">PSKGenerateCreateResponse</a></code>

## Routes

Types:

```python
from cloudflare.types.magic_transit import (
    RouteCreateResponse,
    RouteUpdateResponse,
    RouteListResponse,
    RouteDeleteResponse,
    RouteEmptyResponse,
    RouteGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_identifier}/magic/routes">client.magic_transit.routes.<a href="./src/cloudflare/resources/magic_transit/routes.py">create</a>(account_identifier, \*\*<a href="src/cloudflare/types/magic_transit/route_create_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/route_create_response.py">RouteCreateResponse</a></code>
- <code title="put /accounts/{account_identifier}/magic/routes/{route_identifier}">client.magic_transit.routes.<a href="./src/cloudflare/resources/magic_transit/routes.py">update</a>(route_identifier, \*, account_identifier, \*\*<a href="src/cloudflare/types/magic_transit/route_update_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/route_update_response.py">RouteUpdateResponse</a></code>
- <code title="get /accounts/{account_identifier}/magic/routes">client.magic_transit.routes.<a href="./src/cloudflare/resources/magic_transit/routes.py">list</a>(account_identifier) -> <a href="./src/cloudflare/types/magic_transit/route_list_response.py">RouteListResponse</a></code>
- <code title="delete /accounts/{account_identifier}/magic/routes/{route_identifier}">client.magic_transit.routes.<a href="./src/cloudflare/resources/magic_transit/routes.py">delete</a>(route_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/magic_transit/route_delete_response.py">RouteDeleteResponse</a></code>
- <code title="delete /accounts/{account_identifier}/magic/routes">client.magic_transit.routes.<a href="./src/cloudflare/resources/magic_transit/routes.py">empty</a>(account_identifier, \*\*<a href="src/cloudflare/types/magic_transit/route_empty_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/route_empty_response.py">RouteEmptyResponse</a></code>
- <code title="get /accounts/{account_identifier}/magic/routes/{route_identifier}">client.magic_transit.routes.<a href="./src/cloudflare/resources/magic_transit/routes.py">get</a>(route_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/magic_transit/route_get_response.py">RouteGetResponse</a></code>

# MagicNetworkMonitoring

## Configs

Types:

```python
from cloudflare.types.magic_network_monitoring import (
    ConfigCreateResponse,
    ConfigUpdateResponse,
    ConfigListResponse,
    ConfigDeleteResponse,
    ConfigEditResponse,
)
```

Methods:

- <code title="post /accounts/{account_identifier}/mnm/config">client.magic_network_monitoring.configs.<a href="./src/cloudflare/resources/magic_network_monitoring/configs/configs.py">create</a>(account_identifier) -> <a href="./src/cloudflare/types/magic_network_monitoring/config_create_response.py">ConfigCreateResponse</a></code>
- <code title="put /accounts/{account_identifier}/mnm/config">client.magic_network_monitoring.configs.<a href="./src/cloudflare/resources/magic_network_monitoring/configs/configs.py">update</a>(account_identifier) -> <a href="./src/cloudflare/types/magic_network_monitoring/config_update_response.py">ConfigUpdateResponse</a></code>
- <code title="get /accounts/{account_identifier}/mnm/config">client.magic_network_monitoring.configs.<a href="./src/cloudflare/resources/magic_network_monitoring/configs/configs.py">list</a>(account_identifier) -> <a href="./src/cloudflare/types/magic_network_monitoring/config_list_response.py">ConfigListResponse</a></code>
- <code title="delete /accounts/{account_identifier}/mnm/config">client.magic_network_monitoring.configs.<a href="./src/cloudflare/resources/magic_network_monitoring/configs/configs.py">delete</a>(account_identifier) -> <a href="./src/cloudflare/types/magic_network_monitoring/config_delete_response.py">ConfigDeleteResponse</a></code>
- <code title="patch /accounts/{account_identifier}/mnm/config">client.magic_network_monitoring.configs.<a href="./src/cloudflare/resources/magic_network_monitoring/configs/configs.py">edit</a>(account_identifier) -> <a href="./src/cloudflare/types/magic_network_monitoring/config_edit_response.py">ConfigEditResponse</a></code>

### Fulls

Types:

```python
from cloudflare.types.magic_network_monitoring.configs import FullListResponse
```

Methods:

- <code title="get /accounts/{account_identifier}/mnm/config/full">client.magic_network_monitoring.configs.fulls.<a href="./src/cloudflare/resources/magic_network_monitoring/configs/fulls.py">list</a>(account_identifier) -> <a href="./src/cloudflare/types/magic_network_monitoring/configs/full_list_response.py">FullListResponse</a></code>

## Rules

Types:

```python
from cloudflare.types.magic_network_monitoring import (
    RuleCreateResponse,
    RuleUpdateResponse,
    RuleListResponse,
    RuleDeleteResponse,
    RuleEditResponse,
    RuleGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_identifier}/mnm/rules">client.magic_network_monitoring.rules.<a href="./src/cloudflare/resources/magic_network_monitoring/rules/rules.py">create</a>(account_identifier) -> <a href="./src/cloudflare/types/magic_network_monitoring/rule_create_response.py">Optional</a></code>
- <code title="put /accounts/{account_identifier}/mnm/rules">client.magic_network_monitoring.rules.<a href="./src/cloudflare/resources/magic_network_monitoring/rules/rules.py">update</a>(account_identifier) -> <a href="./src/cloudflare/types/magic_network_monitoring/rule_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_identifier}/mnm/rules">client.magic_network_monitoring.rules.<a href="./src/cloudflare/resources/magic_network_monitoring/rules/rules.py">list</a>(account_identifier) -> <a href="./src/cloudflare/types/magic_network_monitoring/rule_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_identifier}/mnm/rules/{rule_identifier}">client.magic_network_monitoring.rules.<a href="./src/cloudflare/resources/magic_network_monitoring/rules/rules.py">delete</a>(rule_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/magic_network_monitoring/rule_delete_response.py">Optional</a></code>
- <code title="patch /accounts/{account_identifier}/mnm/rules/{rule_identifier}">client.magic_network_monitoring.rules.<a href="./src/cloudflare/resources/magic_network_monitoring/rules/rules.py">edit</a>(rule_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/magic_network_monitoring/rule_edit_response.py">Optional</a></code>
- <code title="get /accounts/{account_identifier}/mnm/rules/{rule_identifier}">client.magic_network_monitoring.rules.<a href="./src/cloudflare/resources/magic_network_monitoring/rules/rules.py">get</a>(rule_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/magic_network_monitoring/rule_get_response.py">Optional</a></code>

### Advertisements

Types:

```python
from cloudflare.types.magic_network_monitoring.rules import AdvertisementEditResponse
```

Methods:

- <code title="patch /accounts/{account_identifier}/mnm/rules/{rule_identifier}/advertisement">client.magic_network_monitoring.rules.advertisements.<a href="./src/cloudflare/resources/magic_network_monitoring/rules/advertisements.py">edit</a>(rule_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/magic_network_monitoring/rules/advertisement_edit_response.py">Optional</a></code>

# MTLSCertificates

Types:

```python
from cloudflare.types import (
    MTLSCertificateCreateResponse,
    MTLSCertificateListResponse,
    MTLSCertificateDeleteResponse,
    MTLSCertificateGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/mtls_certificates">client.mtls_certificates.<a href="./src/cloudflare/resources/mtls_certificates/mtls_certificates.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/mtls_certificate_create_params.py">params</a>) -> <a href="./src/cloudflare/types/mtls_certificate_create_response.py">MTLSCertificateCreateResponse</a></code>
- <code title="get /accounts/{account_id}/mtls_certificates">client.mtls_certificates.<a href="./src/cloudflare/resources/mtls_certificates/mtls_certificates.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/mtls_certificate_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/mtls_certificates/{mtls_certificate_id}">client.mtls_certificates.<a href="./src/cloudflare/resources/mtls_certificates/mtls_certificates.py">delete</a>(mtls_certificate_id, \*, account_id) -> <a href="./src/cloudflare/types/mtls_certificate_delete_response.py">MTLSCertificateDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/mtls_certificates/{mtls_certificate_id}">client.mtls_certificates.<a href="./src/cloudflare/resources/mtls_certificates/mtls_certificates.py">get</a>(mtls_certificate_id, \*, account_id) -> <a href="./src/cloudflare/types/mtls_certificate_get_response.py">MTLSCertificateGetResponse</a></code>

## Associations

Types:

```python
from cloudflare.types.mtls_certificates import AssociationListResponse
```

Methods:

- <code title="get /accounts/{account_id}/mtls_certificates/{mtls_certificate_id}/associations">client.mtls_certificates.associations.<a href="./src/cloudflare/resources/mtls_certificates/associations.py">list</a>(mtls_certificate_id, \*, account_id) -> <a href="./src/cloudflare/types/mtls_certificates/association_list_response.py">Optional</a></code>

# Pages

## Projects

Types:

```python
from cloudflare.types.pages import (
    ProjectCreateResponse,
    ProjectListResponse,
    ProjectDeleteResponse,
    ProjectEditResponse,
    ProjectGetResponse,
    ProjectPurgeBuildCacheResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/pages/projects">client.pages.projects.<a href="./src/cloudflare/resources/pages/projects/projects.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/pages/project_create_params.py">params</a>) -> <a href="./src/cloudflare/types/pages/project_create_response.py">ProjectCreateResponse</a></code>
- <code title="get /accounts/{account_id}/pages/projects">client.pages.projects.<a href="./src/cloudflare/resources/pages/projects/projects.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/pages/project_list_response.py">ProjectListResponse</a></code>
- <code title="delete /accounts/{account_id}/pages/projects/{project_name}">client.pages.projects.<a href="./src/cloudflare/resources/pages/projects/projects.py">delete</a>(project_name, \*, account_id) -> <a href="./src/cloudflare/types/pages/project_delete_response.py">object</a></code>
- <code title="patch /accounts/{account_id}/pages/projects/{project_name}">client.pages.projects.<a href="./src/cloudflare/resources/pages/projects/projects.py">edit</a>(project_name, \*, account_id, \*\*<a href="src/cloudflare/types/pages/project_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/pages/project_edit_response.py">ProjectEditResponse</a></code>
- <code title="get /accounts/{account_id}/pages/projects/{project_name}">client.pages.projects.<a href="./src/cloudflare/resources/pages/projects/projects.py">get</a>(project_name, \*, account_id) -> <a href="./src/cloudflare/types/pages/project_get_response.py">ProjectGetResponse</a></code>
- <code title="post /accounts/{account_id}/pages/projects/{project_name}/purge_build_cache">client.pages.projects.<a href="./src/cloudflare/resources/pages/projects/projects.py">purge_build_cache</a>(project_name, \*, account_id) -> <a href="./src/cloudflare/types/pages/project_purge_build_cache_response.py">object</a></code>

### Deployments

Types:

```python
from cloudflare.types.pages.projects import (
    DeploymentCreateResponse,
    DeploymentListResponse,
    DeploymentDeleteResponse,
    DeploymentGetResponse,
    DeploymentRetryResponse,
    DeploymentRollbackResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/pages/projects/{project_name}/deployments">client.pages.projects.deployments.<a href="./src/cloudflare/resources/pages/projects/deployments/deployments.py">create</a>(project_name, \*, account_id, \*\*<a href="src/cloudflare/types/pages/projects/deployment_create_params.py">params</a>) -> <a href="./src/cloudflare/types/pages/projects/deployment_create_response.py">DeploymentCreateResponse</a></code>
- <code title="get /accounts/{account_id}/pages/projects/{project_name}/deployments">client.pages.projects.deployments.<a href="./src/cloudflare/resources/pages/projects/deployments/deployments.py">list</a>(project_name, \*, account_id) -> <a href="./src/cloudflare/types/pages/projects/deployment_list_response.py">DeploymentListResponse</a></code>
- <code title="delete /accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}">client.pages.projects.deployments.<a href="./src/cloudflare/resources/pages/projects/deployments/deployments.py">delete</a>(deployment_id, \*, account_id, project_name) -> <a href="./src/cloudflare/types/pages/projects/deployment_delete_response.py">object</a></code>
- <code title="get /accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}">client.pages.projects.deployments.<a href="./src/cloudflare/resources/pages/projects/deployments/deployments.py">get</a>(deployment_id, \*, account_id, project_name) -> <a href="./src/cloudflare/types/pages/projects/deployment_get_response.py">DeploymentGetResponse</a></code>
- <code title="post /accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}/retry">client.pages.projects.deployments.<a href="./src/cloudflare/resources/pages/projects/deployments/deployments.py">retry</a>(deployment_id, \*, account_id, project_name) -> <a href="./src/cloudflare/types/pages/projects/deployment_retry_response.py">DeploymentRetryResponse</a></code>
- <code title="post /accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}/rollback">client.pages.projects.deployments.<a href="./src/cloudflare/resources/pages/projects/deployments/deployments.py">rollback</a>(deployment_id, \*, account_id, project_name) -> <a href="./src/cloudflare/types/pages/projects/deployment_rollback_response.py">DeploymentRollbackResponse</a></code>

#### History

##### Logs

Types:

```python
from cloudflare.types.pages.projects.deployments.history import LogListResponse
```

Methods:

- <code title="get /accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}/history/logs">client.pages.projects.deployments.history.logs.<a href="./src/cloudflare/resources/pages/projects/deployments/history/logs.py">list</a>(deployment_id, \*, account_id, project_name) -> <a href="./src/cloudflare/types/pages/projects/deployments/history/log_list_response.py">LogListResponse</a></code>

### Domains

Types:

```python
from cloudflare.types.pages.projects import (
    DomainCreateResponse,
    DomainListResponse,
    DomainDeleteResponse,
    DomainEditResponse,
    DomainGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/pages/projects/{project_name}/domains">client.pages.projects.domains.<a href="./src/cloudflare/resources/pages/projects/domains.py">create</a>(project_name, \*, account_id, \*\*<a href="src/cloudflare/types/pages/projects/domain_create_params.py">params</a>) -> <a href="./src/cloudflare/types/pages/projects/domain_create_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/pages/projects/{project_name}/domains">client.pages.projects.domains.<a href="./src/cloudflare/resources/pages/projects/domains.py">list</a>(project_name, \*, account_id) -> <a href="./src/cloudflare/types/pages/projects/domain_list_response.py">DomainListResponse</a></code>
- <code title="delete /accounts/{account_id}/pages/projects/{project_name}/domains/{domain_name}">client.pages.projects.domains.<a href="./src/cloudflare/resources/pages/projects/domains.py">delete</a>(domain_name, \*, account_id, project_name) -> <a href="./src/cloudflare/types/pages/projects/domain_delete_response.py">object</a></code>
- <code title="patch /accounts/{account_id}/pages/projects/{project_name}/domains/{domain_name}">client.pages.projects.domains.<a href="./src/cloudflare/resources/pages/projects/domains.py">edit</a>(domain_name, \*, account_id, project_name) -> <a href="./src/cloudflare/types/pages/projects/domain_edit_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/pages/projects/{project_name}/domains/{domain_name}">client.pages.projects.domains.<a href="./src/cloudflare/resources/pages/projects/domains.py">get</a>(domain_name, \*, account_id, project_name) -> <a href="./src/cloudflare/types/pages/projects/domain_get_response.py">Optional</a></code>

# PCAPs

Types:

```python
from cloudflare.types import PCAPCreateResponse, PCAPListResponse, PCAPGetResponse
```

Methods:

- <code title="post /accounts/{account_id}/pcaps">client.pcaps.<a href="./src/cloudflare/resources/pcaps/pcaps.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/pcap_create_params.py">params</a>) -> <a href="./src/cloudflare/types/pcap_create_response.py">PCAPCreateResponse</a></code>
- <code title="get /accounts/{account_id}/pcaps">client.pcaps.<a href="./src/cloudflare/resources/pcaps/pcaps.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/pcap_list_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/pcaps/{pcap_id}">client.pcaps.<a href="./src/cloudflare/resources/pcaps/pcaps.py">get</a>(pcap_id, \*, account_id) -> <a href="./src/cloudflare/types/pcap_get_response.py">PCAPGetResponse</a></code>

## Ownerships

Types:

```python
from cloudflare.types.pcaps import (
    OwnershipCreateResponse,
    OwnershipGetResponse,
    OwnershipValidateResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/pcaps/ownership">client.pcaps.ownerships.<a href="./src/cloudflare/resources/pcaps/ownerships.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/pcaps/ownership_create_params.py">params</a>) -> <a href="./src/cloudflare/types/pcaps/ownership_create_response.py">OwnershipCreateResponse</a></code>
- <code title="delete /accounts/{account_id}/pcaps/ownership/{ownership_id}">client.pcaps.ownerships.<a href="./src/cloudflare/resources/pcaps/ownerships.py">delete</a>(ownership_id, \*, account_id) -> None</code>
- <code title="get /accounts/{account_id}/pcaps/ownership">client.pcaps.ownerships.<a href="./src/cloudflare/resources/pcaps/ownerships.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/pcaps/ownership_get_response.py">Optional</a></code>
- <code title="post /accounts/{account_id}/pcaps/ownership/validate">client.pcaps.ownerships.<a href="./src/cloudflare/resources/pcaps/ownerships.py">validate</a>(\*, account_id, \*\*<a href="src/cloudflare/types/pcaps/ownership_validate_params.py">params</a>) -> <a href="./src/cloudflare/types/pcaps/ownership_validate_response.py">OwnershipValidateResponse</a></code>

## Downloads

Methods:

- <code title="get /accounts/{account_id}/pcaps/{pcap_id}/download">client.pcaps.downloads.<a href="./src/cloudflare/resources/pcaps/downloads.py">get</a>(pcap_id, \*, account_id) -> BinaryAPIResponse</code>

# Registrar

## Domains

Types:

```python
from cloudflare.types.registrar import DomainUpdateResponse, DomainListResponse, DomainGetResponse
```

Methods:

- <code title="put /accounts/{account_id}/registrar/domains/{domain_name}">client.registrar.domains.<a href="./src/cloudflare/resources/registrar/domains.py">update</a>(domain_name, \*, account_id, \*\*<a href="src/cloudflare/types/registrar/domain_update_params.py">params</a>) -> <a href="./src/cloudflare/types/registrar/domain_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/registrar/domains">client.registrar.domains.<a href="./src/cloudflare/resources/registrar/domains.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/registrar/domain_list_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/registrar/domains/{domain_name}">client.registrar.domains.<a href="./src/cloudflare/resources/registrar/domains.py">get</a>(domain_name, \*, account_id) -> <a href="./src/cloudflare/types/registrar/domain_get_response.py">Optional</a></code>

# RequestTracers

## Traces

Types:

```python
from cloudflare.types.request_tracers import TraceCreateResponse
```

Methods:

- <code title="post /accounts/{account_identifier}/request-tracer/trace">client.request_tracers.traces.<a href="./src/cloudflare/resources/request_tracers/traces.py">create</a>(account_identifier, \*\*<a href="src/cloudflare/types/request_tracers/trace_create_params.py">params</a>) -> <a href="./src/cloudflare/types/request_tracers/trace_create_response.py">TraceCreateResponse</a></code>

# Rules

## Lists

Types:

```python
from cloudflare.types.rules import (
    ListCreateResponse,
    ListUpdateResponse,
    ListListResponse,
    ListDeleteResponse,
    ListGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/rules/lists">client.rules.lists.<a href="./src/cloudflare/resources/rules/lists/lists.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/rules/list_create_params.py">params</a>) -> <a href="./src/cloudflare/types/rules/list_create_response.py">Optional</a></code>
- <code title="put /accounts/{account_id}/rules/lists/{list_id}">client.rules.lists.<a href="./src/cloudflare/resources/rules/lists/lists.py">update</a>(list_id, \*, account_id, \*\*<a href="src/cloudflare/types/rules/list_update_params.py">params</a>) -> <a href="./src/cloudflare/types/rules/list_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/rules/lists">client.rules.lists.<a href="./src/cloudflare/resources/rules/lists/lists.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/rules/list_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/rules/lists/{list_id}">client.rules.lists.<a href="./src/cloudflare/resources/rules/lists/lists.py">delete</a>(list_id, \*, account_id) -> <a href="./src/cloudflare/types/rules/list_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/rules/lists/{list_id}">client.rules.lists.<a href="./src/cloudflare/resources/rules/lists/lists.py">get</a>(list_id, \*, account_id) -> <a href="./src/cloudflare/types/rules/list_get_response.py">Optional</a></code>

### BulkOperations

Types:

```python
from cloudflare.types.rules.lists import BulkOperationGetResponse
```

Methods:

- <code title="get /accounts/{account_identifier}/rules/lists/bulk_operations/{operation_id}">client.rules.lists.bulk_operations.<a href="./src/cloudflare/resources/rules/lists/bulk_operations.py">get</a>(operation_id, \*, account_identifier) -> <a href="./src/cloudflare/types/rules/lists/bulk_operation_get_response.py">Optional</a></code>

### Items

Types:

```python
from cloudflare.types.rules.lists import (
    ItemCreateResponse,
    ItemUpdateResponse,
    ItemListResponse,
    ItemDeleteResponse,
    ItemGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/rules/lists/{list_id}/items">client.rules.lists.items.<a href="./src/cloudflare/resources/rules/lists/items.py">create</a>(list_id, \*, account_id, \*\*<a href="src/cloudflare/types/rules/lists/item_create_params.py">params</a>) -> <a href="./src/cloudflare/types/rules/lists/item_create_response.py">Optional</a></code>
- <code title="put /accounts/{account_id}/rules/lists/{list_id}/items">client.rules.lists.items.<a href="./src/cloudflare/resources/rules/lists/items.py">update</a>(list_id, \*, account_id, \*\*<a href="src/cloudflare/types/rules/lists/item_update_params.py">params</a>) -> <a href="./src/cloudflare/types/rules/lists/item_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/rules/lists/{list_id}/items">client.rules.lists.items.<a href="./src/cloudflare/resources/rules/lists/items.py">list</a>(list_id, \*, account_id, \*\*<a href="src/cloudflare/types/rules/lists/item_list_params.py">params</a>) -> <a href="./src/cloudflare/types/rules/lists/item_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/rules/lists/{list_id}/items">client.rules.lists.items.<a href="./src/cloudflare/resources/rules/lists/items.py">delete</a>(list_id, \*, account_id, \*\*<a href="src/cloudflare/types/rules/lists/item_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/rules/lists/item_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_identifier}/rules/lists/{list_id}/items/{item_id}">client.rules.lists.items.<a href="./src/cloudflare/resources/rules/lists/items.py">get</a>(item_id, \*, account_identifier, list_id) -> <a href="./src/cloudflare/types/rules/lists/item_get_response.py">Optional</a></code>

# Storage

## Analytics

Types:

```python
from cloudflare.types.storage import AnalyticsListResponse, AnalyticsStoredResponse
```

Methods:

- <code title="get /accounts/{account_id}/storage/analytics">client.storage.analytics.<a href="./src/cloudflare/resources/storage/analytics.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/storage/analytics_list_params.py">params</a>) -> <a href="./src/cloudflare/types/storage/analytics_list_response.py">AnalyticsListResponse</a></code>
- <code title="get /accounts/{account_id}/storage/analytics/stored">client.storage.analytics.<a href="./src/cloudflare/resources/storage/analytics.py">stored</a>(\*, account_id, \*\*<a href="src/cloudflare/types/storage/analytics_stored_params.py">params</a>) -> <a href="./src/cloudflare/types/storage/analytics_stored_response.py">AnalyticsStoredResponse</a></code>

# Stream

Types:

```python
from cloudflare.types import StreamListResponse, StreamGetResponse
```

Methods:

- <code title="post /accounts/{account_id}/stream">client.stream.<a href="./src/cloudflare/resources/stream/stream.py">create</a>(\*, account_id) -> None</code>
- <code title="get /accounts/{account_id}/stream">client.stream.<a href="./src/cloudflare/resources/stream/stream.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/stream_list_params.py">params</a>) -> <a href="./src/cloudflare/types/stream_list_response.py">StreamListResponse</a></code>
- <code title="delete /accounts/{account_id}/stream/{identifier}">client.stream.<a href="./src/cloudflare/resources/stream/stream.py">delete</a>(identifier, \*, account_id) -> None</code>
- <code title="get /accounts/{account_id}/stream/{identifier}">client.stream.<a href="./src/cloudflare/resources/stream/stream.py">get</a>(identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream_get_response.py">StreamGetResponse</a></code>

## AudioTracks

Types:

```python
from cloudflare.types.stream import (
    AudioTrackCreateResponse,
    AudioTrackListResponse,
    AudioTrackDeleteResponse,
    AudioTrackEditResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/stream/{identifier}/audio/copy">client.stream.audio_tracks.<a href="./src/cloudflare/resources/stream/audio_tracks.py">create</a>(identifier, \*, account_id, \*\*<a href="src/cloudflare/types/stream/audio_track_create_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/audio_track_create_response.py">AudioTrackCreateResponse</a></code>
- <code title="get /accounts/{account_id}/stream/{identifier}/audio">client.stream.audio_tracks.<a href="./src/cloudflare/resources/stream/audio_tracks.py">list</a>(identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/audio_track_list_response.py">AudioTrackListResponse</a></code>
- <code title="delete /accounts/{account_id}/stream/{identifier}/audio/{audio_identifier}">client.stream.audio_tracks.<a href="./src/cloudflare/resources/stream/audio_tracks.py">delete</a>(audio_identifier, \*, account_id, identifier) -> <a href="./src/cloudflare/types/stream/audio_track_delete_response.py">AudioTrackDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/stream/{identifier}/audio/{audio_identifier}">client.stream.audio_tracks.<a href="./src/cloudflare/resources/stream/audio_tracks.py">edit</a>(audio_identifier, \*, account_id, identifier, \*\*<a href="src/cloudflare/types/stream/audio_track_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/audio_track_edit_response.py">AudioTrackEditResponse</a></code>

## Videos

Types:

```python
from cloudflare.types.stream import VideoStorageUsageResponse
```

Methods:

- <code title="get /accounts/{account_id}/stream/storage-usage">client.stream.videos.<a href="./src/cloudflare/resources/stream/videos.py">storage_usage</a>(\*, account_id, \*\*<a href="src/cloudflare/types/stream/video_storage_usage_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/video_storage_usage_response.py">VideoStorageUsageResponse</a></code>

## Clips

Types:

```python
from cloudflare.types.stream import ClipCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/stream/clip">client.stream.clips.<a href="./src/cloudflare/resources/stream/clips.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/stream/clip_create_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/clip_create_response.py">ClipCreateResponse</a></code>

## Copies

Types:

```python
from cloudflare.types.stream import CopyCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/stream/copy">client.stream.copies.<a href="./src/cloudflare/resources/stream/copies.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/stream/copy_create_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/copy_create_response.py">CopyCreateResponse</a></code>

## DirectUploads

Types:

```python
from cloudflare.types.stream import DirectUploadCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/stream/direct_upload">client.stream.direct_uploads.<a href="./src/cloudflare/resources/stream/direct_uploads.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/stream/direct_upload_create_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/direct_upload_create_response.py">DirectUploadCreateResponse</a></code>

## Keys

Types:

```python
from cloudflare.types.stream import KeyCreateResponse, KeyListResponse, KeyDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/stream/keys">client.stream.keys.<a href="./src/cloudflare/resources/stream/keys.py">create</a>(\*, account_id) -> <a href="./src/cloudflare/types/stream/key_create_response.py">KeyCreateResponse</a></code>
- <code title="get /accounts/{account_id}/stream/keys">client.stream.keys.<a href="./src/cloudflare/resources/stream/keys.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/stream/key_list_response.py">KeyListResponse</a></code>
- <code title="delete /accounts/{account_id}/stream/keys/{identifier}">client.stream.keys.<a href="./src/cloudflare/resources/stream/keys.py">delete</a>(identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/key_delete_response.py">KeyDeleteResponse</a></code>

## LiveInputs

Types:

```python
from cloudflare.types.stream import (
    LiveInputCreateResponse,
    LiveInputUpdateResponse,
    LiveInputListResponse,
    LiveInputGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/stream/live_inputs">client.stream.live_inputs.<a href="./src/cloudflare/resources/stream/live_inputs/live_inputs.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/stream/live_input_create_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/live_input_create_response.py">LiveInputCreateResponse</a></code>
- <code title="put /accounts/{account_id}/stream/live_inputs/{live_input_identifier}">client.stream.live_inputs.<a href="./src/cloudflare/resources/stream/live_inputs/live_inputs.py">update</a>(live_input_identifier, \*, account_id, \*\*<a href="src/cloudflare/types/stream/live_input_update_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/live_input_update_response.py">LiveInputUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/stream/live_inputs">client.stream.live_inputs.<a href="./src/cloudflare/resources/stream/live_inputs/live_inputs.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/stream/live_input_list_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/live_input_list_response.py">LiveInputListResponse</a></code>
- <code title="delete /accounts/{account_id}/stream/live_inputs/{live_input_identifier}">client.stream.live_inputs.<a href="./src/cloudflare/resources/stream/live_inputs/live_inputs.py">delete</a>(live_input_identifier, \*, account_id) -> None</code>
- <code title="get /accounts/{account_id}/stream/live_inputs/{live_input_identifier}">client.stream.live_inputs.<a href="./src/cloudflare/resources/stream/live_inputs/live_inputs.py">get</a>(live_input_identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/live_input_get_response.py">LiveInputGetResponse</a></code>

### Outputs

Types:

```python
from cloudflare.types.stream.live_inputs import (
    OutputCreateResponse,
    OutputUpdateResponse,
    OutputListResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs">client.stream.live_inputs.outputs.<a href="./src/cloudflare/resources/stream/live_inputs/outputs.py">create</a>(live_input_identifier, \*, account_id, \*\*<a href="src/cloudflare/types/stream/live_inputs/output_create_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/live_inputs/output_create_response.py">OutputCreateResponse</a></code>
- <code title="put /accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs/{output_identifier}">client.stream.live_inputs.outputs.<a href="./src/cloudflare/resources/stream/live_inputs/outputs.py">update</a>(output_identifier, \*, account_id, live_input_identifier, \*\*<a href="src/cloudflare/types/stream/live_inputs/output_update_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/live_inputs/output_update_response.py">OutputUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs">client.stream.live_inputs.outputs.<a href="./src/cloudflare/resources/stream/live_inputs/outputs.py">list</a>(live_input_identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/live_inputs/output_list_response.py">OutputListResponse</a></code>
- <code title="delete /accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs/{output_identifier}">client.stream.live_inputs.outputs.<a href="./src/cloudflare/resources/stream/live_inputs/outputs.py">delete</a>(output_identifier, \*, account_id, live_input_identifier) -> None</code>

## Watermarks

Types:

```python
from cloudflare.types.stream import (
    WatermarkCreateResponse,
    WatermarkListResponse,
    WatermarkDeleteResponse,
    WatermarkGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/stream/watermarks">client.stream.watermarks.<a href="./src/cloudflare/resources/stream/watermarks.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/stream/watermark_create_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/watermark_create_response.py">WatermarkCreateResponse</a></code>
- <code title="get /accounts/{account_id}/stream/watermarks">client.stream.watermarks.<a href="./src/cloudflare/resources/stream/watermarks.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/stream/watermark_list_response.py">WatermarkListResponse</a></code>
- <code title="delete /accounts/{account_id}/stream/watermarks/{identifier}">client.stream.watermarks.<a href="./src/cloudflare/resources/stream/watermarks.py">delete</a>(identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/watermark_delete_response.py">WatermarkDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/stream/watermarks/{identifier}">client.stream.watermarks.<a href="./src/cloudflare/resources/stream/watermarks.py">get</a>(identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/watermark_get_response.py">WatermarkGetResponse</a></code>

## Webhooks

Types:

```python
from cloudflare.types.stream import WebhookUpdateResponse, WebhookDeleteResponse, WebhookGetResponse
```

Methods:

- <code title="put /accounts/{account_id}/stream/webhook">client.stream.webhooks.<a href="./src/cloudflare/resources/stream/webhooks.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/stream/webhook_update_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/webhook_update_response.py">WebhookUpdateResponse</a></code>
- <code title="delete /accounts/{account_id}/stream/webhook">client.stream.webhooks.<a href="./src/cloudflare/resources/stream/webhooks.py">delete</a>(\*, account_id) -> <a href="./src/cloudflare/types/stream/webhook_delete_response.py">WebhookDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/stream/webhook">client.stream.webhooks.<a href="./src/cloudflare/resources/stream/webhooks.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/stream/webhook_get_response.py">WebhookGetResponse</a></code>

## Captions

Types:

```python
from cloudflare.types.stream import (
    CaptionUpdateResponse,
    CaptionListResponse,
    CaptionDeleteResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/stream/{identifier}/captions/{language}">client.stream.captions.<a href="./src/cloudflare/resources/stream/captions.py">update</a>(language, \*, account_id, identifier, \*\*<a href="src/cloudflare/types/stream/caption_update_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/caption_update_response.py">CaptionUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/stream/{identifier}/captions">client.stream.captions.<a href="./src/cloudflare/resources/stream/captions.py">list</a>(identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/caption_list_response.py">CaptionListResponse</a></code>
- <code title="delete /accounts/{account_id}/stream/{identifier}/captions/{language}">client.stream.captions.<a href="./src/cloudflare/resources/stream/captions.py">delete</a>(language, \*, account_id, identifier) -> <a href="./src/cloudflare/types/stream/caption_delete_response.py">CaptionDeleteResponse</a></code>

## Downloads

Types:

```python
from cloudflare.types.stream import (
    DownloadCreateResponse,
    DownloadListResponse,
    DownloadDeleteResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/stream/{identifier}/downloads">client.stream.downloads.<a href="./src/cloudflare/resources/stream/downloads.py">create</a>(identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/download_create_response.py">DownloadCreateResponse</a></code>
- <code title="get /accounts/{account_id}/stream/{identifier}/downloads">client.stream.downloads.<a href="./src/cloudflare/resources/stream/downloads.py">list</a>(identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/download_list_response.py">DownloadListResponse</a></code>
- <code title="delete /accounts/{account_id}/stream/{identifier}/downloads">client.stream.downloads.<a href="./src/cloudflare/resources/stream/downloads.py">delete</a>(identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/download_delete_response.py">DownloadDeleteResponse</a></code>

## Embeds

Types:

```python
from cloudflare.types.stream import EmbedListResponse
```

Methods:

- <code title="get /accounts/{account_id}/stream/{identifier}/embed">client.stream.embeds.<a href="./src/cloudflare/resources/stream/embeds.py">list</a>(identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/embed_list_response.py">object</a></code>

## Tokens

Types:

```python
from cloudflare.types.stream import TokenCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/stream/{identifier}/token">client.stream.tokens.<a href="./src/cloudflare/resources/stream/tokens.py">create</a>(identifier, \*, account_id, \*\*<a href="src/cloudflare/types/stream/token_create_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/token_create_response.py">TokenCreateResponse</a></code>

# Alerting

## V3

Types:

```python
from cloudflare.types.alerting import V3ListResponse
```

Methods:

- <code title="get /accounts/{account_id}/alerting/v3/available_alerts">client.alerting.v3.<a href="./src/cloudflare/resources/alerting/v3/v3.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/alerting/v3_list_response.py">Optional</a></code>

### Destinations

#### Eligible

Types:

```python
from cloudflare.types.alerting.v3.destinations import EligibleGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/alerting/v3/destinations/eligible">client.alerting.v3.destinations.eligible.<a href="./src/cloudflare/resources/alerting/v3/destinations/eligible.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/alerting/v3/destinations/eligible_get_response.py">Optional</a></code>

#### Pagerduty

Types:

```python
from cloudflare.types.alerting.v3.destinations import (
    PagerdutyCreateResponse,
    PagerdutyDeleteResponse,
    PagerdutyGetResponse,
    PagerdutyLinkResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/alerting/v3/destinations/pagerduty/connect">client.alerting.v3.destinations.pagerduty.<a href="./src/cloudflare/resources/alerting/v3/destinations/pagerduty.py">create</a>(\*, account_id) -> <a href="./src/cloudflare/types/alerting/v3/destinations/pagerduty_create_response.py">PagerdutyCreateResponse</a></code>
- <code title="delete /accounts/{account_id}/alerting/v3/destinations/pagerduty">client.alerting.v3.destinations.pagerduty.<a href="./src/cloudflare/resources/alerting/v3/destinations/pagerduty.py">delete</a>(\*, account_id) -> <a href="./src/cloudflare/types/alerting/v3/destinations/pagerduty_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/alerting/v3/destinations/pagerduty">client.alerting.v3.destinations.pagerduty.<a href="./src/cloudflare/resources/alerting/v3/destinations/pagerduty.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/alerting/v3/destinations/pagerduty_get_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/alerting/v3/destinations/pagerduty/connect/{token_id}">client.alerting.v3.destinations.pagerduty.<a href="./src/cloudflare/resources/alerting/v3/destinations/pagerduty.py">link</a>(token_id, \*, account_id) -> <a href="./src/cloudflare/types/alerting/v3/destinations/pagerduty_link_response.py">PagerdutyLinkResponse</a></code>

#### Webhooks

Types:

```python
from cloudflare.types.alerting.v3.destinations import (
    WebhookCreateResponse,
    WebhookUpdateResponse,
    WebhookListResponse,
    WebhookDeleteResponse,
    WebhookGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/alerting/v3/destinations/webhooks">client.alerting.v3.destinations.webhooks.<a href="./src/cloudflare/resources/alerting/v3/destinations/webhooks.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/alerting/v3/destinations/webhook_create_params.py">params</a>) -> <a href="./src/cloudflare/types/alerting/v3/destinations/webhook_create_response.py">WebhookCreateResponse</a></code>
- <code title="put /accounts/{account_id}/alerting/v3/destinations/webhooks/{webhook_id}">client.alerting.v3.destinations.webhooks.<a href="./src/cloudflare/resources/alerting/v3/destinations/webhooks.py">update</a>(webhook_id, \*, account_id, \*\*<a href="src/cloudflare/types/alerting/v3/destinations/webhook_update_params.py">params</a>) -> <a href="./src/cloudflare/types/alerting/v3/destinations/webhook_update_response.py">WebhookUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/alerting/v3/destinations/webhooks">client.alerting.v3.destinations.webhooks.<a href="./src/cloudflare/resources/alerting/v3/destinations/webhooks.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/alerting/v3/destinations/webhook_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/alerting/v3/destinations/webhooks/{webhook_id}">client.alerting.v3.destinations.webhooks.<a href="./src/cloudflare/resources/alerting/v3/destinations/webhooks.py">delete</a>(webhook_id, \*, account_id) -> <a href="./src/cloudflare/types/alerting/v3/destinations/webhook_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/alerting/v3/destinations/webhooks/{webhook_id}">client.alerting.v3.destinations.webhooks.<a href="./src/cloudflare/resources/alerting/v3/destinations/webhooks.py">get</a>(webhook_id, \*, account_id) -> <a href="./src/cloudflare/types/alerting/v3/destinations/webhook_get_response.py">WebhookGetResponse</a></code>

### Histories

Types:

```python
from cloudflare.types.alerting.v3 import HistoryListResponse
```

Methods:

- <code title="get /accounts/{account_id}/alerting/v3/history">client.alerting.v3.histories.<a href="./src/cloudflare/resources/alerting/v3/histories.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/alerting/v3/history_list_params.py">params</a>) -> <a href="./src/cloudflare/types/alerting/v3/history_list_response.py">SyncV4PagePaginationArray[HistoryListResponse]</a></code>

### Policies

Types:

```python
from cloudflare.types.alerting.v3 import (
    PolicyCreateResponse,
    PolicyUpdateResponse,
    PolicyListResponse,
    PolicyDeleteResponse,
    PolicyGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/alerting/v3/policies">client.alerting.v3.policies.<a href="./src/cloudflare/resources/alerting/v3/policies.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/alerting/v3/policy_create_params.py">params</a>) -> <a href="./src/cloudflare/types/alerting/v3/policy_create_response.py">PolicyCreateResponse</a></code>
- <code title="put /accounts/{account_id}/alerting/v3/policies/{policy_id}">client.alerting.v3.policies.<a href="./src/cloudflare/resources/alerting/v3/policies.py">update</a>(policy_id, \*, account_id, \*\*<a href="src/cloudflare/types/alerting/v3/policy_update_params.py">params</a>) -> <a href="./src/cloudflare/types/alerting/v3/policy_update_response.py">PolicyUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/alerting/v3/policies">client.alerting.v3.policies.<a href="./src/cloudflare/resources/alerting/v3/policies.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/alerting/v3/policy_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/alerting/v3/policies/{policy_id}">client.alerting.v3.policies.<a href="./src/cloudflare/resources/alerting/v3/policies.py">delete</a>(policy_id, \*, account_id) -> <a href="./src/cloudflare/types/alerting/v3/policy_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/alerting/v3/policies/{policy_id}">client.alerting.v3.policies.<a href="./src/cloudflare/resources/alerting/v3/policies.py">get</a>(policy_id, \*, account_id) -> <a href="./src/cloudflare/types/alerting/v3/policy_get_response.py">PolicyGetResponse</a></code>

# Devices

Types:

```python
from cloudflare.types import DeviceDevicesListDevicesResponse, DeviceGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/devices">client.devices.<a href="./src/cloudflare/resources/devices/devices.py">devices_list_devices</a>(\*, account_id) -> <a href="./src/cloudflare/types/device_devices_list_devices_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/devices/{device_id}">client.devices.<a href="./src/cloudflare/resources/devices/devices.py">get</a>(device_id, \*, account_id) -> <a href="./src/cloudflare/types/device_get_response.py">Optional</a></code>

## DEXTests

Types:

```python
from cloudflare.types.devices import (
    DEXTestCreateResponse,
    DEXTestUpdateResponse,
    DEXTestListResponse,
    DEXTestDeleteResponse,
    DEXTestGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/devices/dex_tests">client.devices.dex_tests.<a href="./src/cloudflare/resources/devices/dex_tests.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/devices/dex_test_create_params.py">params</a>) -> <a href="./src/cloudflare/types/devices/dex_test_create_response.py">Optional</a></code>
- <code title="put /accounts/{account_id}/devices/dex_tests/{dex_test_id}">client.devices.dex_tests.<a href="./src/cloudflare/resources/devices/dex_tests.py">update</a>(dex_test_id, \*, account_id, \*\*<a href="src/cloudflare/types/devices/dex_test_update_params.py">params</a>) -> <a href="./src/cloudflare/types/devices/dex_test_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/devices/dex_tests">client.devices.dex_tests.<a href="./src/cloudflare/resources/devices/dex_tests.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/devices/dex_test_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/devices/dex_tests/{dex_test_id}">client.devices.dex_tests.<a href="./src/cloudflare/resources/devices/dex_tests.py">delete</a>(dex_test_id, \*, account_id) -> <a href="./src/cloudflare/types/devices/dex_test_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/devices/dex_tests/{dex_test_id}">client.devices.dex_tests.<a href="./src/cloudflare/resources/devices/dex_tests.py">get</a>(dex_test_id, \*, account_id) -> <a href="./src/cloudflare/types/devices/dex_test_get_response.py">Optional</a></code>

## Networks

Types:

```python
from cloudflare.types.devices import (
    NetworkCreateResponse,
    NetworkUpdateResponse,
    NetworkListResponse,
    NetworkDeleteResponse,
    NetworkGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/devices/networks">client.devices.networks.<a href="./src/cloudflare/resources/devices/networks.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/devices/network_create_params.py">params</a>) -> <a href="./src/cloudflare/types/devices/network_create_response.py">Optional</a></code>
- <code title="put /accounts/{account_id}/devices/networks/{network_id}">client.devices.networks.<a href="./src/cloudflare/resources/devices/networks.py">update</a>(network_id, \*, account_id, \*\*<a href="src/cloudflare/types/devices/network_update_params.py">params</a>) -> <a href="./src/cloudflare/types/devices/network_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/devices/networks">client.devices.networks.<a href="./src/cloudflare/resources/devices/networks.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/devices/network_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/devices/networks/{network_id}">client.devices.networks.<a href="./src/cloudflare/resources/devices/networks.py">delete</a>(network_id, \*, account_id) -> <a href="./src/cloudflare/types/devices/network_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/devices/networks/{network_id}">client.devices.networks.<a href="./src/cloudflare/resources/devices/networks.py">get</a>(network_id, \*, account_id) -> <a href="./src/cloudflare/types/devices/network_get_response.py">Optional</a></code>

## Policies

Types:

```python
from cloudflare.types.devices import (
    PolicyCreateResponse,
    PolicyListResponse,
    PolicyDeleteResponse,
    PolicyEditResponse,
    PolicyGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/devices/policy">client.devices.policies.<a href="./src/cloudflare/resources/devices/policies/policies.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/devices/policy_create_params.py">params</a>) -> <a href="./src/cloudflare/types/devices/policy_create_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/devices/policies">client.devices.policies.<a href="./src/cloudflare/resources/devices/policies/policies.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/devices/policy_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/devices/policy/{policy_id}">client.devices.policies.<a href="./src/cloudflare/resources/devices/policies/policies.py">delete</a>(policy_id, \*, account_id) -> <a href="./src/cloudflare/types/devices/policy_delete_response.py">Optional</a></code>
- <code title="patch /accounts/{account_id}/devices/policy/{policy_id}">client.devices.policies.<a href="./src/cloudflare/resources/devices/policies/policies.py">edit</a>(policy_id, \*, account_id, \*\*<a href="src/cloudflare/types/devices/policy_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/devices/policy_edit_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/devices/policy/{policy_id}">client.devices.policies.<a href="./src/cloudflare/resources/devices/policies/policies.py">get</a>(policy_id, \*, account_id) -> <a href="./src/cloudflare/types/devices/policy_get_response.py">Optional</a></code>

### DefaultPolicy

Types:

```python
from cloudflare.types.devices.policies import DefaultPolicyGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/devices/policy">client.devices.policies.default_policy.<a href="./src/cloudflare/resources/devices/policies/default_policy.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/devices/policies/default_policy_get_response.py">Optional</a></code>

### Excludes

Types:

```python
from cloudflare.types.devices.policies import (
    ExcludeUpdateResponse,
    ExcludeListResponse,
    ExcludeGetResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/devices/policy/exclude">client.devices.policies.excludes.<a href="./src/cloudflare/resources/devices/policies/excludes.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/devices/policies/exclude_update_params.py">params</a>) -> <a href="./src/cloudflare/types/devices/policies/exclude_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/devices/policy/exclude">client.devices.policies.excludes.<a href="./src/cloudflare/resources/devices/policies/excludes.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/devices/policies/exclude_list_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/devices/policy/{policy_id}/exclude">client.devices.policies.excludes.<a href="./src/cloudflare/resources/devices/policies/excludes.py">get</a>(policy_id, \*, account_id) -> <a href="./src/cloudflare/types/devices/policies/exclude_get_response.py">Optional</a></code>

### FallbackDomains

Types:

```python
from cloudflare.types.devices.policies import (
    FallbackDomainUpdateResponse,
    FallbackDomainListResponse,
    FallbackDomainGetResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/devices/policy/{policy_id}/fallback_domains">client.devices.policies.fallback_domains.<a href="./src/cloudflare/resources/devices/policies/fallback_domains.py">update</a>(policy_id, \*, account_id, \*\*<a href="src/cloudflare/types/devices/policies/fallback_domain_update_params.py">params</a>) -> <a href="./src/cloudflare/types/devices/policies/fallback_domain_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/devices/policy/fallback_domains">client.devices.policies.fallback_domains.<a href="./src/cloudflare/resources/devices/policies/fallback_domains.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/devices/policies/fallback_domain_list_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/devices/policy/{policy_id}/fallback_domains">client.devices.policies.fallback_domains.<a href="./src/cloudflare/resources/devices/policies/fallback_domains.py">get</a>(policy_id, \*, account_id) -> <a href="./src/cloudflare/types/devices/policies/fallback_domain_get_response.py">Optional</a></code>

### Includes

Types:

```python
from cloudflare.types.devices.policies import (
    IncludeUpdateResponse,
    IncludeListResponse,
    IncludeGetResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/devices/policy/include">client.devices.policies.includes.<a href="./src/cloudflare/resources/devices/policies/includes.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/devices/policies/include_update_params.py">params</a>) -> <a href="./src/cloudflare/types/devices/policies/include_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/devices/policy/include">client.devices.policies.includes.<a href="./src/cloudflare/resources/devices/policies/includes.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/devices/policies/include_list_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/devices/policy/{policy_id}/include">client.devices.policies.includes.<a href="./src/cloudflare/resources/devices/policies/includes.py">get</a>(policy_id, \*, account_id) -> <a href="./src/cloudflare/types/devices/policies/include_get_response.py">Optional</a></code>

## Postures

Types:

```python
from cloudflare.types.devices import (
    PostureCreateResponse,
    PostureUpdateResponse,
    PostureListResponse,
    PostureDeleteResponse,
    PostureGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/devices/posture">client.devices.postures.<a href="./src/cloudflare/resources/devices/postures/postures.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/devices/posture_create_params.py">params</a>) -> <a href="./src/cloudflare/types/devices/posture_create_response.py">Optional</a></code>
- <code title="put /accounts/{account_id}/devices/posture/{rule_id}">client.devices.postures.<a href="./src/cloudflare/resources/devices/postures/postures.py">update</a>(rule_id, \*, account_id, \*\*<a href="src/cloudflare/types/devices/posture_update_params.py">params</a>) -> <a href="./src/cloudflare/types/devices/posture_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/devices/posture">client.devices.postures.<a href="./src/cloudflare/resources/devices/postures/postures.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/devices/posture_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/devices/posture/{rule_id}">client.devices.postures.<a href="./src/cloudflare/resources/devices/postures/postures.py">delete</a>(rule_id, \*, account_id) -> <a href="./src/cloudflare/types/devices/posture_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/devices/posture/{rule_id}">client.devices.postures.<a href="./src/cloudflare/resources/devices/postures/postures.py">get</a>(rule_id, \*, account_id) -> <a href="./src/cloudflare/types/devices/posture_get_response.py">Optional</a></code>

### Integrations

Types:

```python
from cloudflare.types.devices.postures import (
    IntegrationCreateResponse,
    IntegrationListResponse,
    IntegrationDeleteResponse,
    IntegrationEditResponse,
    IntegrationGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/devices/posture/integration">client.devices.postures.integrations.<a href="./src/cloudflare/resources/devices/postures/integrations.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/devices/postures/integration_create_params.py">params</a>) -> <a href="./src/cloudflare/types/devices/postures/integration_create_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/devices/posture/integration">client.devices.postures.integrations.<a href="./src/cloudflare/resources/devices/postures/integrations.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/devices/postures/integration_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/devices/posture/integration/{integration_id}">client.devices.postures.integrations.<a href="./src/cloudflare/resources/devices/postures/integrations.py">delete</a>(integration_id, \*, account_id) -> <a href="./src/cloudflare/types/devices/postures/integration_delete_response.py">Optional</a></code>
- <code title="patch /accounts/{account_id}/devices/posture/integration/{integration_id}">client.devices.postures.integrations.<a href="./src/cloudflare/resources/devices/postures/integrations.py">edit</a>(integration_id, \*, account_id, \*\*<a href="src/cloudflare/types/devices/postures/integration_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/devices/postures/integration_edit_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/devices/posture/integration/{integration_id}">client.devices.postures.integrations.<a href="./src/cloudflare/resources/devices/postures/integrations.py">get</a>(integration_id, \*, account_id) -> <a href="./src/cloudflare/types/devices/postures/integration_get_response.py">Optional</a></code>

## Revokes

Types:

```python
from cloudflare.types.devices import RevokeCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/devices/revoke">client.devices.revokes.<a href="./src/cloudflare/resources/devices/revokes.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/devices/revoke_create_params.py">params</a>) -> <a href="./src/cloudflare/types/devices/revoke_create_response.py">Optional</a></code>

## Settings

Types:

```python
from cloudflare.types.devices import SettingUpdateResponse, SettingListResponse
```

Methods:

- <code title="put /accounts/{account_id}/devices/settings">client.devices.settings.<a href="./src/cloudflare/resources/devices/settings.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/devices/setting_update_params.py">params</a>) -> <a href="./src/cloudflare/types/devices/setting_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/devices/settings">client.devices.settings.<a href="./src/cloudflare/resources/devices/settings.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/devices/setting_list_response.py">Optional</a></code>

## Unrevokes

Types:

```python
from cloudflare.types.devices import UnrevokeCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/devices/unrevoke">client.devices.unrevokes.<a href="./src/cloudflare/resources/devices/unrevokes.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/devices/unrevoke_create_params.py">params</a>) -> <a href="./src/cloudflare/types/devices/unrevoke_create_response.py">Optional</a></code>

## OverrideCodes

Types:

```python
from cloudflare.types.devices import OverrideCodeListResponse
```

Methods:

- <code title="get /accounts/{account_id}/devices/{device_id}/override_codes">client.devices.override_codes.<a href="./src/cloudflare/resources/devices/override_codes.py">list</a>(device_id, \*, account_id) -> <a href="./src/cloudflare/types/devices/override_code_list_response.py">Optional</a></code>

# D1

## Database

Types:

```python
from cloudflare.types.d1 import (
    DatabaseCreateResponse,
    DatabaseListResponse,
    DatabaseDeleteResponse,
    DatabaseGetResponse,
    DatabaseQueryResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/d1/database">client.d1.database.<a href="./src/cloudflare/resources/d1/database.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/d1/database_create_params.py">params</a>) -> <a href="./src/cloudflare/types/d1/database_create_response.py">DatabaseCreateResponse</a></code>
- <code title="get /accounts/{account_id}/d1/database">client.d1.database.<a href="./src/cloudflare/resources/d1/database.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/d1/database_list_params.py">params</a>) -> <a href="./src/cloudflare/types/d1/database_list_response.py">SyncV4PagePaginationArray[DatabaseListResponse]</a></code>
- <code title="delete /accounts/{account_identifier}/d1/database/{database_identifier}">client.d1.database.<a href="./src/cloudflare/resources/d1/database.py">delete</a>(database_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/d1/database_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_identifier}/d1/database/{database_identifier}">client.d1.database.<a href="./src/cloudflare/resources/d1/database.py">get</a>(database_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/d1/database_get_response.py">DatabaseGetResponse</a></code>
- <code title="post /accounts/{account_identifier}/d1/database/{database_identifier}/query">client.d1.database.<a href="./src/cloudflare/resources/d1/database.py">query</a>(database_identifier, \*, account_identifier, \*\*<a href="src/cloudflare/types/d1/database_query_params.py">params</a>) -> <a href="./src/cloudflare/types/d1/database_query_response.py">DatabaseQueryResponse</a></code>

# R2

## Buckets

Types:

```python
from cloudflare.types.r2 import (
    BucketCreateResponse,
    BucketListResponse,
    BucketDeleteResponse,
    BucketGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/r2/buckets">client.r2.buckets.<a href="./src/cloudflare/resources/r2/buckets.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/r2/bucket_create_params.py">params</a>) -> <a href="./src/cloudflare/types/r2/bucket_create_response.py">BucketCreateResponse</a></code>
- <code title="get /accounts/{account_id}/r2/buckets">client.r2.buckets.<a href="./src/cloudflare/resources/r2/buckets.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/r2/bucket_list_params.py">params</a>) -> <a href="./src/cloudflare/types/r2/bucket_list_response.py">BucketListResponse</a></code>
- <code title="delete /accounts/{account_id}/r2/buckets/{bucket_name}">client.r2.buckets.<a href="./src/cloudflare/resources/r2/buckets.py">delete</a>(bucket_name, \*, account_id) -> <a href="./src/cloudflare/types/r2/bucket_delete_response.py">object</a></code>
- <code title="get /accounts/{account_id}/r2/buckets/{bucket_name}">client.r2.buckets.<a href="./src/cloudflare/resources/r2/buckets.py">get</a>(bucket_name, \*, account_id) -> <a href="./src/cloudflare/types/r2/bucket_get_response.py">BucketGetResponse</a></code>

## Sippy

Types:

```python
from cloudflare.types.r2 import SippyUpdateResponse, SippyDeleteResponse, SippyGetResponse
```

Methods:

- <code title="put /accounts/{account_id}/r2/buckets/{bucket_name}/sippy">client.r2.sippy.<a href="./src/cloudflare/resources/r2/sippy.py">update</a>(bucket_name, \*, account_id, \*\*<a href="src/cloudflare/types/r2/sippy_update_params.py">params</a>) -> <a href="./src/cloudflare/types/r2/sippy_update_response.py">SippyUpdateResponse</a></code>
- <code title="delete /accounts/{account_id}/r2/buckets/{bucket_name}/sippy">client.r2.sippy.<a href="./src/cloudflare/resources/r2/sippy.py">delete</a>(bucket_name, \*, account_id) -> <a href="./src/cloudflare/types/r2/sippy_delete_response.py">SippyDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/r2/buckets/{bucket_name}/sippy">client.r2.sippy.<a href="./src/cloudflare/resources/r2/sippy.py">get</a>(bucket_name, \*, account_id) -> <a href="./src/cloudflare/types/r2/sippy_get_response.py">SippyGetResponse</a></code>

# WARPConnector

Types:

```python
from cloudflare.types import (
    WARPConnectorCreateResponse,
    WARPConnectorListResponse,
    WARPConnectorDeleteResponse,
    WARPConnectorEditResponse,
    WARPConnectorGetResponse,
    WARPConnectorTokenResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/warp_connector">client.warp_connector.<a href="./src/cloudflare/resources/warp_connector.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/warp_connector_create_params.py">params</a>) -> <a href="./src/cloudflare/types/warp_connector_create_response.py">WARPConnectorCreateResponse</a></code>
- <code title="get /accounts/{account_id}/warp_connector">client.warp_connector.<a href="./src/cloudflare/resources/warp_connector.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/warp_connector_list_params.py">params</a>) -> <a href="./src/cloudflare/types/warp_connector_list_response.py">SyncV4PagePaginationArray[WARPConnectorListResponse]</a></code>
- <code title="delete /accounts/{account_id}/warp_connector/{tunnel_id}">client.warp_connector.<a href="./src/cloudflare/resources/warp_connector.py">delete</a>(tunnel_id, \*, account_id, \*\*<a href="src/cloudflare/types/warp_connector_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/warp_connector_delete_response.py">WARPConnectorDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/warp_connector/{tunnel_id}">client.warp_connector.<a href="./src/cloudflare/resources/warp_connector.py">edit</a>(tunnel_id, \*, account_id, \*\*<a href="src/cloudflare/types/warp_connector_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/warp_connector_edit_response.py">WARPConnectorEditResponse</a></code>
- <code title="get /accounts/{account_id}/warp_connector/{tunnel_id}">client.warp_connector.<a href="./src/cloudflare/resources/warp_connector.py">get</a>(tunnel_id, \*, account_id) -> <a href="./src/cloudflare/types/warp_connector_get_response.py">WARPConnectorGetResponse</a></code>
- <code title="get /accounts/{account_id}/warp_connector/{tunnel_id}/token">client.warp_connector.<a href="./src/cloudflare/resources/warp_connector.py">token</a>(tunnel_id, \*, account_id) -> <a href="./src/cloudflare/types/warp_connector_token_response.py">WARPConnectorTokenResponse</a></code>

# WorkersForPlatforms

## Dispatch

### Namespaces

#### Scripts

Types:

```python
from cloudflare.types.workers_for_platforms.dispatch.namespaces import (
    ScriptUpdateResponse,
    ScriptGetResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}">client.workers_for_platforms.dispatch.namespaces.scripts.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/scripts.py">update</a>(script_name, \*, account_id, dispatch_namespace, \*\*<a href="src/cloudflare/types/workers_for_platforms/dispatch/namespaces/script_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers_for_platforms/dispatch/namespaces/script_update_response.py">ScriptUpdateResponse</a></code>
- <code title="delete /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}">client.workers_for_platforms.dispatch.namespaces.scripts.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/scripts.py">delete</a>(script_name, \*, account_id, dispatch_namespace, \*\*<a href="src/cloudflare/types/workers_for_platforms/dispatch/namespaces/script_delete_params.py">params</a>) -> None</code>
- <code title="get /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}">client.workers_for_platforms.dispatch.namespaces.scripts.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/scripts.py">get</a>(script_name, \*, account_id, dispatch_namespace) -> <a href="./src/cloudflare/types/workers_for_platforms/dispatch/namespaces/script_get_response.py">ScriptGetResponse</a></code>

##### Content

###### Scripts

Types:

```python
from cloudflare.types.workers_for_platforms.dispatch.namespaces.scripts.content import (
    ScriptUpdateResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/content">client.workers_for_platforms.dispatch.namespaces.scripts.content.scripts.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/content/scripts.py">update</a>(script_name, \*, account_id, dispatch_namespace, \*\*<a href="src/cloudflare/types/workers_for_platforms/dispatch/namespaces/scripts/content/script_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers_for_platforms/dispatch/namespaces/scripts/content/script_update_response.py">ScriptUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/content">client.workers_for_platforms.dispatch.namespaces.scripts.content.scripts.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/content/scripts.py">get</a>(script_name, \*, account_id, dispatch_namespace) -> BinaryAPIResponse</code>

###### Settings

Types:

```python
from cloudflare.types.workers_for_platforms.dispatch.namespaces.scripts.content import (
    SettingEditResponse,
    SettingGetResponse,
)
```

Methods:

- <code title="patch /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/settings">client.workers_for_platforms.dispatch.namespaces.scripts.content.settings.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/content/settings.py">edit</a>(script_name, \*, account_id, dispatch_namespace, \*\*<a href="src/cloudflare/types/workers_for_platforms/dispatch/namespaces/scripts/content/setting_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/workers_for_platforms/dispatch/namespaces/scripts/content/setting_edit_response.py">SettingEditResponse</a></code>
- <code title="get /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/settings">client.workers_for_platforms.dispatch.namespaces.scripts.content.settings.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/content/settings.py">get</a>(script_name, \*, account_id, dispatch_namespace) -> <a href="./src/cloudflare/types/workers_for_platforms/dispatch/namespaces/scripts/content/setting_get_response.py">SettingGetResponse</a></code>

###### Bindings

Types:

```python
from cloudflare.types.workers_for_platforms.dispatch.namespaces.scripts.content import (
    BindingGetResponse,
)
```

Methods:

- <code title="get /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/bindings">client.workers_for_platforms.dispatch.namespaces.scripts.content.bindings.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/content/bindings.py">get</a>(script_name, \*, account_id, dispatch_namespace) -> <a href="./src/cloudflare/types/workers_for_platforms/dispatch/namespaces/scripts/content/binding_get_response.py">BindingGetResponse</a></code>

# ZeroTrust

## IdentityProviders

Types:

```python
from cloudflare.types.zero_trust import (
    IdentityProviderCreateResponse,
    IdentityProviderUpdateResponse,
    IdentityProviderListResponse,
    IdentityProviderDeleteResponse,
    IdentityProviderGetResponse,
)
```

Methods:

- <code title="post /{account_or_zone}/{account_or_zone_id}/access/identity_providers">client.zero_trust.identity_providers.<a href="./src/cloudflare/resources/zero_trust/identity_providers.py">create</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/identity_provider_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/identity_provider_create_response.py">IdentityProviderCreateResponse</a></code>
- <code title="put /{account_or_zone}/{account_or_zone_id}/access/identity_providers/{uuid}">client.zero_trust.identity_providers.<a href="./src/cloudflare/resources/zero_trust/identity_providers.py">update</a>(uuid, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/identity_provider_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/identity_provider_update_response.py">IdentityProviderUpdateResponse</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/identity_providers">client.zero_trust.identity_providers.<a href="./src/cloudflare/resources/zero_trust/identity_providers.py">list</a>(\*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/identity_provider_list_response.py">Optional</a></code>
- <code title="delete /{account_or_zone}/{account_or_zone_id}/access/identity_providers/{uuid}">client.zero_trust.identity_providers.<a href="./src/cloudflare/resources/zero_trust/identity_providers.py">delete</a>(uuid, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/identity_provider_delete_response.py">IdentityProviderDeleteResponse</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/identity_providers/{uuid}">client.zero_trust.identity_providers.<a href="./src/cloudflare/resources/zero_trust/identity_providers.py">get</a>(uuid, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/identity_provider_get_response.py">IdentityProviderGetResponse</a></code>

## Organizations

Types:

```python
from cloudflare.types.zero_trust import (
    OrganizationCreateResponse,
    OrganizationUpdateResponse,
    OrganizationListResponse,
    OrganizationRevokeUsersResponse,
)
```

Methods:

- <code title="post /{account_or_zone}/{account_or_zone_id}/access/organizations">client.zero_trust.organizations.<a href="./src/cloudflare/resources/zero_trust/organizations.py">create</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/organization_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/organization_create_response.py">OrganizationCreateResponse</a></code>
- <code title="put /{account_or_zone}/{account_or_zone_id}/access/organizations">client.zero_trust.organizations.<a href="./src/cloudflare/resources/zero_trust/organizations.py">update</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/organization_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/organization_update_response.py">OrganizationUpdateResponse</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/organizations">client.zero_trust.organizations.<a href="./src/cloudflare/resources/zero_trust/organizations.py">list</a>(\*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/organization_list_response.py">OrganizationListResponse</a></code>
- <code title="post /{account_or_zone}/{account_or_zone_id}/access/organizations/revoke_user">client.zero_trust.organizations.<a href="./src/cloudflare/resources/zero_trust/organizations.py">revoke_users</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/organization_revoke_users_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/organization_revoke_users_response.py">Optional</a></code>

## Seats

Types:

```python
from cloudflare.types.zero_trust import SeatEditResponse
```

Methods:

- <code title="patch /accounts/{identifier}/access/seats">client.zero_trust.seats.<a href="./src/cloudflare/resources/zero_trust/seats.py">edit</a>(identifier, \*\*<a href="src/cloudflare/types/zero_trust/seat_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/seat_edit_response.py">Optional</a></code>

## Access

### Applications

Types:

```python
from cloudflare.types.zero_trust.access import (
    ApplicationCreateResponse,
    ApplicationUpdateResponse,
    ApplicationListResponse,
    ApplicationDeleteResponse,
    ApplicationGetResponse,
    ApplicationRevokeTokensResponse,
)
```

Methods:

- <code title="post /{account_or_zone}/{account_or_zone_id}/access/apps">client.zero_trust.access.applications.<a href="./src/cloudflare/resources/zero_trust/access/applications/applications.py">create</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/application_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/application_create_response.py">ApplicationCreateResponse</a></code>
- <code title="put /{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}">client.zero_trust.access.applications.<a href="./src/cloudflare/resources/zero_trust/access/applications/applications.py">update</a>(app_id, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/application_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/application_update_response.py">ApplicationUpdateResponse</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/apps">client.zero_trust.access.applications.<a href="./src/cloudflare/resources/zero_trust/access/applications/applications.py">list</a>(\*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/application_list_response.py">Optional</a></code>
- <code title="delete /{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}">client.zero_trust.access.applications.<a href="./src/cloudflare/resources/zero_trust/access/applications/applications.py">delete</a>(app_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/application_delete_response.py">ApplicationDeleteResponse</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}">client.zero_trust.access.applications.<a href="./src/cloudflare/resources/zero_trust/access/applications/applications.py">get</a>(app_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/application_get_response.py">ApplicationGetResponse</a></code>
- <code title="post /{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}/revoke_tokens">client.zero_trust.access.applications.<a href="./src/cloudflare/resources/zero_trust/access/applications/applications.py">revoke_tokens</a>(app_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/application_revoke_tokens_response.py">object</a></code>

#### CAs

Types:

```python
from cloudflare.types.zero_trust.access.applications import (
    CACreateResponse,
    CAListResponse,
    CADeleteResponse,
    CAGetResponse,
)
```

Methods:

- <code title="post /{account_or_zone}/{account_or_zone_id}/access/apps/{uuid}/ca">client.zero_trust.access.applications.cas.<a href="./src/cloudflare/resources/zero_trust/access/applications/cas.py">create</a>(uuid, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/applications/ca_create_response.py">CACreateResponse</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/apps/ca">client.zero_trust.access.applications.cas.<a href="./src/cloudflare/resources/zero_trust/access/applications/cas.py">list</a>(\*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/applications/ca_list_response.py">Optional</a></code>
- <code title="delete /{account_or_zone}/{account_or_zone_id}/access/apps/{uuid}/ca">client.zero_trust.access.applications.cas.<a href="./src/cloudflare/resources/zero_trust/access/applications/cas.py">delete</a>(uuid, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/applications/ca_delete_response.py">CADeleteResponse</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/apps/{uuid}/ca">client.zero_trust.access.applications.cas.<a href="./src/cloudflare/resources/zero_trust/access/applications/cas.py">get</a>(uuid, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/applications/ca_get_response.py">CAGetResponse</a></code>

#### UserPolicyChecks

Types:

```python
from cloudflare.types.zero_trust.access.applications import UserPolicyCheckListResponse
```

Methods:

- <code title="get /{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}/user_policy_checks">client.zero_trust.access.applications.user_policy_checks.<a href="./src/cloudflare/resources/zero_trust/access/applications/user_policy_checks.py">list</a>(app_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/applications/user_policy_check_list_response.py">UserPolicyCheckListResponse</a></code>

#### Policies

Types:

```python
from cloudflare.types.zero_trust.access.applications import (
    PolicyCreateResponse,
    PolicyUpdateResponse,
    PolicyListResponse,
    PolicyDeleteResponse,
    PolicyGetResponse,
)
```

Methods:

- <code title="post /{account_or_zone}/{account_or_zone_id}/access/apps/{uuid}/policies">client.zero_trust.access.applications.policies.<a href="./src/cloudflare/resources/zero_trust/access/applications/policies.py">create</a>(uuid, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/applications/policy_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/applications/policy_create_response.py">PolicyCreateResponse</a></code>
- <code title="put /{account_or_zone}/{account_or_zone_id}/access/apps/{uuid1}/policies/{uuid}">client.zero_trust.access.applications.policies.<a href="./src/cloudflare/resources/zero_trust/access/applications/policies.py">update</a>(uuid, \*, uuid1, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/applications/policy_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/applications/policy_update_response.py">PolicyUpdateResponse</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/apps/{uuid}/policies">client.zero_trust.access.applications.policies.<a href="./src/cloudflare/resources/zero_trust/access/applications/policies.py">list</a>(uuid, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/applications/policy_list_response.py">Optional</a></code>
- <code title="delete /{account_or_zone}/{account_or_zone_id}/access/apps/{uuid1}/policies/{uuid}">client.zero_trust.access.applications.policies.<a href="./src/cloudflare/resources/zero_trust/access/applications/policies.py">delete</a>(uuid, \*, uuid1, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/applications/policy_delete_response.py">PolicyDeleteResponse</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/apps/{uuid1}/policies/{uuid}">client.zero_trust.access.applications.policies.<a href="./src/cloudflare/resources/zero_trust/access/applications/policies.py">get</a>(uuid, \*, uuid1, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/applications/policy_get_response.py">PolicyGetResponse</a></code>

### Certificates

Types:

```python
from cloudflare.types.zero_trust.access import (
    CertificateCreateResponse,
    CertificateUpdateResponse,
    CertificateListResponse,
    CertificateDeleteResponse,
    CertificateGetResponse,
)
```

Methods:

- <code title="post /{account_or_zone}/{account_or_zone_id}/access/certificates">client.zero_trust.access.certificates.<a href="./src/cloudflare/resources/zero_trust/access/certificates/certificates.py">create</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/certificate_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/certificate_create_response.py">CertificateCreateResponse</a></code>
- <code title="put /{account_or_zone}/{account_or_zone_id}/access/certificates/{uuid}">client.zero_trust.access.certificates.<a href="./src/cloudflare/resources/zero_trust/access/certificates/certificates.py">update</a>(uuid, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/certificate_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/certificate_update_response.py">CertificateUpdateResponse</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/certificates">client.zero_trust.access.certificates.<a href="./src/cloudflare/resources/zero_trust/access/certificates/certificates.py">list</a>(\*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/certificate_list_response.py">Optional</a></code>
- <code title="delete /{account_or_zone}/{account_or_zone_id}/access/certificates/{uuid}">client.zero_trust.access.certificates.<a href="./src/cloudflare/resources/zero_trust/access/certificates/certificates.py">delete</a>(uuid, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/certificate_delete_response.py">CertificateDeleteResponse</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/certificates/{uuid}">client.zero_trust.access.certificates.<a href="./src/cloudflare/resources/zero_trust/access/certificates/certificates.py">get</a>(uuid, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/certificate_get_response.py">CertificateGetResponse</a></code>

#### Settings

Types:

```python
from cloudflare.types.zero_trust.access.certificates import (
    SettingUpdateResponse,
    SettingListResponse,
)
```

Methods:

- <code title="put /{account_or_zone}/{account_or_zone_id}/access/certificates/settings">client.zero_trust.access.certificates.settings.<a href="./src/cloudflare/resources/zero_trust/access/certificates/settings.py">update</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/certificates/setting_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/certificates/setting_update_response.py">Optional</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/certificates/settings">client.zero_trust.access.certificates.settings.<a href="./src/cloudflare/resources/zero_trust/access/certificates/settings.py">list</a>(\*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/certificates/setting_list_response.py">Optional</a></code>

### Groups

Types:

```python
from cloudflare.types.zero_trust.access import (
    GroupCreateResponse,
    GroupUpdateResponse,
    GroupListResponse,
    GroupDeleteResponse,
    GroupGetResponse,
)
```

Methods:

- <code title="post /{account_or_zone}/{account_or_zone_id}/access/groups">client.zero_trust.access.groups.<a href="./src/cloudflare/resources/zero_trust/access/groups.py">create</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/group_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/group_create_response.py">GroupCreateResponse</a></code>
- <code title="put /{account_or_zone}/{account_or_zone_id}/access/groups/{uuid}">client.zero_trust.access.groups.<a href="./src/cloudflare/resources/zero_trust/access/groups.py">update</a>(uuid, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/group_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/group_update_response.py">GroupUpdateResponse</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/groups">client.zero_trust.access.groups.<a href="./src/cloudflare/resources/zero_trust/access/groups.py">list</a>(\*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/group_list_response.py">Optional</a></code>
- <code title="delete /{account_or_zone}/{account_or_zone_id}/access/groups/{uuid}">client.zero_trust.access.groups.<a href="./src/cloudflare/resources/zero_trust/access/groups.py">delete</a>(uuid, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/group_delete_response.py">GroupDeleteResponse</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/groups/{uuid}">client.zero_trust.access.groups.<a href="./src/cloudflare/resources/zero_trust/access/groups.py">get</a>(uuid, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/group_get_response.py">GroupGetResponse</a></code>

### ServiceTokens

Types:

```python
from cloudflare.types.zero_trust.access import (
    ServiceTokenCreateResponse,
    ServiceTokenUpdateResponse,
    ServiceTokenListResponse,
    ServiceTokenDeleteResponse,
    ServiceTokenRefreshResponse,
    ServiceTokenRotateResponse,
)
```

Methods:

- <code title="post /{account_or_zone}/{account_or_zone_id}/access/service_tokens">client.zero_trust.access.service_tokens.<a href="./src/cloudflare/resources/zero_trust/access/service_tokens.py">create</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/service_token_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/service_token_create_response.py">ServiceTokenCreateResponse</a></code>
- <code title="put /{account_or_zone}/{account_or_zone_id}/access/service_tokens/{uuid}">client.zero_trust.access.service_tokens.<a href="./src/cloudflare/resources/zero_trust/access/service_tokens.py">update</a>(uuid, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/service_token_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/service_token_update_response.py">ServiceTokenUpdateResponse</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/service_tokens">client.zero_trust.access.service_tokens.<a href="./src/cloudflare/resources/zero_trust/access/service_tokens.py">list</a>(\*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/service_token_list_response.py">Optional</a></code>
- <code title="delete /{account_or_zone}/{account_or_zone_id}/access/service_tokens/{uuid}">client.zero_trust.access.service_tokens.<a href="./src/cloudflare/resources/zero_trust/access/service_tokens.py">delete</a>(uuid, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/service_token_delete_response.py">ServiceTokenDeleteResponse</a></code>
- <code title="post /accounts/{identifier}/access/service_tokens/{uuid}/refresh">client.zero_trust.access.service_tokens.<a href="./src/cloudflare/resources/zero_trust/access/service_tokens.py">refresh</a>(uuid, \*, identifier) -> <a href="./src/cloudflare/types/zero_trust/access/service_token_refresh_response.py">ServiceTokenRefreshResponse</a></code>
- <code title="post /accounts/{identifier}/access/service_tokens/{uuid}/rotate">client.zero_trust.access.service_tokens.<a href="./src/cloudflare/resources/zero_trust/access/service_tokens.py">rotate</a>(uuid, \*, identifier) -> <a href="./src/cloudflare/types/zero_trust/access/service_token_rotate_response.py">ServiceTokenRotateResponse</a></code>

### Bookmarks

Types:

```python
from cloudflare.types.zero_trust.access import (
    BookmarkCreateResponse,
    BookmarkUpdateResponse,
    BookmarkListResponse,
    BookmarkDeleteResponse,
    BookmarkGetResponse,
)
```

Methods:

- <code title="post /accounts/{identifier}/access/bookmarks/{uuid}">client.zero_trust.access.bookmarks.<a href="./src/cloudflare/resources/zero_trust/access/bookmarks.py">create</a>(uuid, \*, identifier) -> <a href="./src/cloudflare/types/zero_trust/access/bookmark_create_response.py">BookmarkCreateResponse</a></code>
- <code title="put /accounts/{identifier}/access/bookmarks/{uuid}">client.zero_trust.access.bookmarks.<a href="./src/cloudflare/resources/zero_trust/access/bookmarks.py">update</a>(uuid, \*, identifier) -> <a href="./src/cloudflare/types/zero_trust/access/bookmark_update_response.py">BookmarkUpdateResponse</a></code>
- <code title="get /accounts/{identifier}/access/bookmarks">client.zero_trust.access.bookmarks.<a href="./src/cloudflare/resources/zero_trust/access/bookmarks.py">list</a>(identifier) -> <a href="./src/cloudflare/types/zero_trust/access/bookmark_list_response.py">Optional</a></code>
- <code title="delete /accounts/{identifier}/access/bookmarks/{uuid}">client.zero_trust.access.bookmarks.<a href="./src/cloudflare/resources/zero_trust/access/bookmarks.py">delete</a>(uuid, \*, identifier) -> <a href="./src/cloudflare/types/zero_trust/access/bookmark_delete_response.py">BookmarkDeleteResponse</a></code>
- <code title="get /accounts/{identifier}/access/bookmarks/{uuid}">client.zero_trust.access.bookmarks.<a href="./src/cloudflare/resources/zero_trust/access/bookmarks.py">get</a>(uuid, \*, identifier) -> <a href="./src/cloudflare/types/zero_trust/access/bookmark_get_response.py">BookmarkGetResponse</a></code>

### Keys

Types:

```python
from cloudflare.types.zero_trust.access import KeyUpdateResponse, KeyListResponse, KeyRotateResponse
```

Methods:

- <code title="put /accounts/{identifier}/access/keys">client.zero_trust.access.keys.<a href="./src/cloudflare/resources/zero_trust/access/keys.py">update</a>(identifier, \*\*<a href="src/cloudflare/types/zero_trust/access/key_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/key_update_response.py">KeyUpdateResponse</a></code>
- <code title="get /accounts/{identifier}/access/keys">client.zero_trust.access.keys.<a href="./src/cloudflare/resources/zero_trust/access/keys.py">list</a>(identifier) -> <a href="./src/cloudflare/types/zero_trust/access/key_list_response.py">KeyListResponse</a></code>
- <code title="post /accounts/{identifier}/access/keys/rotate">client.zero_trust.access.keys.<a href="./src/cloudflare/resources/zero_trust/access/keys.py">rotate</a>(identifier) -> <a href="./src/cloudflare/types/zero_trust/access/key_rotate_response.py">KeyRotateResponse</a></code>

### Logs

#### AccessRequests

Types:

```python
from cloudflare.types.zero_trust.access.logs import AccessRequestListResponse
```

Methods:

- <code title="get /accounts/{identifier}/access/logs/access_requests">client.zero_trust.access.logs.access_requests.<a href="./src/cloudflare/resources/zero_trust/access/logs/access_requests.py">list</a>(identifier) -> <a href="./src/cloudflare/types/zero_trust/access/logs/access_request_list_response.py">Optional</a></code>

### Users

Types:

```python
from cloudflare.types.zero_trust.access import UserListResponse
```

Methods:

- <code title="get /accounts/{identifier}/access/users">client.zero_trust.access.users.<a href="./src/cloudflare/resources/zero_trust/access/users/users.py">list</a>(identifier) -> <a href="./src/cloudflare/types/zero_trust/access/user_list_response.py">Optional</a></code>

#### ActiveSessions

Types:

```python
from cloudflare.types.zero_trust.access.users import (
    ActiveSessionListResponse,
    ActiveSessionGetResponse,
)
```

Methods:

- <code title="get /accounts/{identifier}/access/users/{id}/active_sessions">client.zero_trust.access.users.active_sessions.<a href="./src/cloudflare/resources/zero_trust/access/users/active_sessions.py">list</a>(id, \*, identifier) -> <a href="./src/cloudflare/types/zero_trust/access/users/active_session_list_response.py">Optional</a></code>
- <code title="get /accounts/{identifier}/access/users/{id}/active_sessions/{nonce}">client.zero_trust.access.users.active_sessions.<a href="./src/cloudflare/resources/zero_trust/access/users/active_sessions.py">get</a>(nonce, \*, identifier, id) -> <a href="./src/cloudflare/types/zero_trust/access/users/active_session_get_response.py">ActiveSessionGetResponse</a></code>

#### LastSeenIdentity

Types:

```python
from cloudflare.types.zero_trust.access.users import LastSeenIdentityListResponse
```

Methods:

- <code title="get /accounts/{identifier}/access/users/{id}/last_seen_identity">client.zero_trust.access.users.last_seen_identity.<a href="./src/cloudflare/resources/zero_trust/access/users/last_seen_identity.py">list</a>(id, \*, identifier) -> <a href="./src/cloudflare/types/zero_trust/access/users/last_seen_identity_list_response.py">LastSeenIdentityListResponse</a></code>

#### FailedLogins

Types:

```python
from cloudflare.types.zero_trust.access.users import FailedLoginListResponse
```

Methods:

- <code title="get /accounts/{identifier}/access/users/{id}/failed_logins">client.zero_trust.access.users.failed_logins.<a href="./src/cloudflare/resources/zero_trust/access/users/failed_logins.py">list</a>(id, \*, identifier) -> <a href="./src/cloudflare/types/zero_trust/access/users/failed_login_list_response.py">Optional</a></code>

### CustomPages

Types:

```python
from cloudflare.types.zero_trust.access import (
    CustomPageCreateResponse,
    CustomPageUpdateResponse,
    CustomPageListResponse,
    CustomPageDeleteResponse,
    CustomPageGetResponse,
)
```

Methods:

- <code title="post /accounts/{identifier}/access/custom_pages">client.zero_trust.access.custom_pages.<a href="./src/cloudflare/resources/zero_trust/access/custom_pages.py">create</a>(identifier, \*\*<a href="src/cloudflare/types/zero_trust/access/custom_page_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/custom_page_create_response.py">CustomPageCreateResponse</a></code>
- <code title="put /accounts/{identifier}/access/custom_pages/{uuid}">client.zero_trust.access.custom_pages.<a href="./src/cloudflare/resources/zero_trust/access/custom_pages.py">update</a>(uuid, \*, identifier, \*\*<a href="src/cloudflare/types/zero_trust/access/custom_page_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/custom_page_update_response.py">CustomPageUpdateResponse</a></code>
- <code title="get /accounts/{identifier}/access/custom_pages">client.zero_trust.access.custom_pages.<a href="./src/cloudflare/resources/zero_trust/access/custom_pages.py">list</a>(identifier) -> <a href="./src/cloudflare/types/zero_trust/access/custom_page_list_response.py">Optional</a></code>
- <code title="delete /accounts/{identifier}/access/custom_pages/{uuid}">client.zero_trust.access.custom_pages.<a href="./src/cloudflare/resources/zero_trust/access/custom_pages.py">delete</a>(uuid, \*, identifier) -> <a href="./src/cloudflare/types/zero_trust/access/custom_page_delete_response.py">CustomPageDeleteResponse</a></code>
- <code title="get /accounts/{identifier}/access/custom_pages/{uuid}">client.zero_trust.access.custom_pages.<a href="./src/cloudflare/resources/zero_trust/access/custom_pages.py">get</a>(uuid, \*, identifier) -> <a href="./src/cloudflare/types/zero_trust/access/custom_page_get_response.py">CustomPageGetResponse</a></code>

### Tags

Types:

```python
from cloudflare.types.zero_trust.access import (
    TagCreateResponse,
    TagUpdateResponse,
    TagListResponse,
    TagDeleteResponse,
    TagGetResponse,
)
```

Methods:

- <code title="post /accounts/{identifier}/access/tags">client.zero_trust.access.tags.<a href="./src/cloudflare/resources/zero_trust/access/tags.py">create</a>(identifier, \*\*<a href="src/cloudflare/types/zero_trust/access/tag_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/tag_create_response.py">TagCreateResponse</a></code>
- <code title="put /accounts/{identifier}/access/tags/{name}">client.zero_trust.access.tags.<a href="./src/cloudflare/resources/zero_trust/access/tags.py">update</a>(tag_name, \*, identifier, \*\*<a href="src/cloudflare/types/zero_trust/access/tag_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/tag_update_response.py">TagUpdateResponse</a></code>
- <code title="get /accounts/{identifier}/access/tags">client.zero_trust.access.tags.<a href="./src/cloudflare/resources/zero_trust/access/tags.py">list</a>(identifier) -> <a href="./src/cloudflare/types/zero_trust/access/tag_list_response.py">Optional</a></code>
- <code title="delete /accounts/{identifier}/access/tags/{name}">client.zero_trust.access.tags.<a href="./src/cloudflare/resources/zero_trust/access/tags.py">delete</a>(name, \*, identifier) -> <a href="./src/cloudflare/types/zero_trust/access/tag_delete_response.py">TagDeleteResponse</a></code>
- <code title="get /accounts/{identifier}/access/tags/{name}">client.zero_trust.access.tags.<a href="./src/cloudflare/resources/zero_trust/access/tags.py">get</a>(name, \*, identifier) -> <a href="./src/cloudflare/types/zero_trust/access/tag_get_response.py">TagGetResponse</a></code>

## DEX

### Colos

Types:

```python
from cloudflare.types.zero_trust.dex import ColoListResponse
```

Methods:

- <code title="get /accounts/{account_id}/dex/colos">client.zero_trust.dex.colos.<a href="./src/cloudflare/resources/zero_trust/dex/colos.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dex/colo_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dex/colo_list_response.py">Optional</a></code>

### FleetStatus

#### Devices

Types:

```python
from cloudflare.types.zero_trust.dex.fleet_status import DeviceListResponse
```

Methods:

- <code title="get /accounts/{account_id}/dex/fleet-status/devices">client.zero_trust.dex.fleet_status.devices.<a href="./src/cloudflare/resources/zero_trust/dex/fleet_status/devices.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dex/fleet_status/device_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dex/fleet_status/device_list_response.py">SyncV4PagePaginationArray[DeviceListResponse]</a></code>

#### Live

Types:

```python
from cloudflare.types.zero_trust.dex.fleet_status import LiveListResponse
```

Methods:

- <code title="get /accounts/{account_id}/dex/fleet-status/live">client.zero_trust.dex.fleet_status.live.<a href="./src/cloudflare/resources/zero_trust/dex/fleet_status/live.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dex/fleet_status/live_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dex/fleet_status/live_list_response.py">LiveListResponse</a></code>

#### OverTime

Methods:

- <code title="get /accounts/{account_id}/dex/fleet-status/over-time">client.zero_trust.dex.fleet_status.over_time.<a href="./src/cloudflare/resources/zero_trust/dex/fleet_status/over_time.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dex/fleet_status/over_time_list_params.py">params</a>) -> None</code>

### HTTPTests

Types:

```python
from cloudflare.types.zero_trust.dex import HTTPTestGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/dex/http-tests/{test_id}">client.zero_trust.dex.http_tests.<a href="./src/cloudflare/resources/zero_trust/dex/http_tests/http_tests.py">get</a>(test_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dex/http_test_get_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dex/http_test_get_response.py">HTTPTestGetResponse</a></code>

#### Percentiles

Types:

```python
from cloudflare.types.zero_trust.dex.http_tests import PercentileListResponse
```

Methods:

- <code title="get /accounts/{account_id}/dex/http-tests/{test_id}/percentiles">client.zero_trust.dex.http_tests.percentiles.<a href="./src/cloudflare/resources/zero_trust/dex/http_tests/percentiles.py">list</a>(test_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dex/http_tests/percentile_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dex/http_tests/percentile_list_response.py">PercentileListResponse</a></code>

### Tests

Types:

```python
from cloudflare.types.zero_trust.dex import TestListResponse
```

Methods:

- <code title="get /accounts/{account_id}/dex/tests">client.zero_trust.dex.tests.<a href="./src/cloudflare/resources/zero_trust/dex/tests/tests.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dex/test_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dex/test_list_response.py">SyncV4PagePagination[TestListResponse]</a></code>

#### UniqueDevices

Types:

```python
from cloudflare.types.zero_trust.dex.tests import UniqueDeviceListResponse
```

Methods:

- <code title="get /accounts/{account_id}/dex/tests/unique-devices">client.zero_trust.dex.tests.unique_devices.<a href="./src/cloudflare/resources/zero_trust/dex/tests/unique_devices.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dex/tests/unique_device_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dex/tests/unique_device_list_response.py">UniqueDeviceListResponse</a></code>

### TracerouteTestResults

#### NetworkPath

Types:

```python
from cloudflare.types.zero_trust.dex.traceroute_test_results import NetworkPathListResponse
```

Methods:

- <code title="get /accounts/{account_id}/dex/traceroute-test-results/{test_result_id}/network-path">client.zero_trust.dex.traceroute_test_results.network_path.<a href="./src/cloudflare/resources/zero_trust/dex/traceroute_test_results/network_path.py">list</a>(test_result_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dex/traceroute_test_results/network_path_list_response.py">NetworkPathListResponse</a></code>

### TracerouteTests

Types:

```python
from cloudflare.types.zero_trust.dex import (
    TracerouteTestGetResponse,
    TracerouteTestNetworkPathResponse,
    TracerouteTestPercentilesResponse,
)
```

Methods:

- <code title="get /accounts/{account_id}/dex/traceroute-tests/{test_id}">client.zero_trust.dex.traceroute_tests.<a href="./src/cloudflare/resources/zero_trust/dex/traceroute_tests.py">get</a>(test_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dex/traceroute_test_get_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dex/traceroute_test_get_response.py">TracerouteTestGetResponse</a></code>
- <code title="get /accounts/{account_id}/dex/traceroute-tests/{test_id}/network-path">client.zero_trust.dex.traceroute_tests.<a href="./src/cloudflare/resources/zero_trust/dex/traceroute_tests.py">network_path</a>(test_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dex/traceroute_test_network_path_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dex/traceroute_test_network_path_response.py">TracerouteTestNetworkPathResponse</a></code>
- <code title="get /accounts/{account_id}/dex/traceroute-tests/{test_id}/percentiles">client.zero_trust.dex.traceroute_tests.<a href="./src/cloudflare/resources/zero_trust/dex/traceroute_tests.py">percentiles</a>(test_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dex/traceroute_test_percentiles_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dex/traceroute_test_percentiles_response.py">TracerouteTestPercentilesResponse</a></code>

## Tunnels

Types:

```python
from cloudflare.types.zero_trust import (
    TunnelCreateResponse,
    TunnelListResponse,
    TunnelDeleteResponse,
    TunnelEditResponse,
    TunnelGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/tunnels">client.zero_trust.tunnels.<a href="./src/cloudflare/resources/zero_trust/tunnels/tunnels.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/tunnel_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/tunnel_create_response.py">TunnelCreateResponse</a></code>
- <code title="get /accounts/{account_id}/tunnels">client.zero_trust.tunnels.<a href="./src/cloudflare/resources/zero_trust/tunnels/tunnels.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/tunnel_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/tunnel_list_response.py">SyncV4PagePaginationArray[TunnelListResponse]</a></code>
- <code title="delete /accounts/{account_id}/tunnels/{tunnel_id}">client.zero_trust.tunnels.<a href="./src/cloudflare/resources/zero_trust/tunnels/tunnels.py">delete</a>(tunnel_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/tunnel_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/tunnel_delete_response.py">TunnelDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/cfd_tunnel/{tunnel_id}">client.zero_trust.tunnels.<a href="./src/cloudflare/resources/zero_trust/tunnels/tunnels.py">edit</a>(tunnel_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/tunnel_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/tunnel_edit_response.py">TunnelEditResponse</a></code>
- <code title="get /accounts/{account_id}/tunnels/{tunnel_id}">client.zero_trust.tunnels.<a href="./src/cloudflare/resources/zero_trust/tunnels/tunnels.py">get</a>(tunnel_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/tunnel_get_response.py">TunnelGetResponse</a></code>

### Configurations

Types:

```python
from cloudflare.types.zero_trust.tunnels import (
    ConfigurationUpdateResponse,
    ConfigurationListResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/cfd_tunnel/{tunnel_id}/configurations">client.zero_trust.tunnels.configurations.<a href="./src/cloudflare/resources/zero_trust/tunnels/configurations.py">update</a>(tunnel_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/tunnels/configuration_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/tunnels/configuration_update_response.py">ConfigurationUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/cfd_tunnel/{tunnel_id}/configurations">client.zero_trust.tunnels.configurations.<a href="./src/cloudflare/resources/zero_trust/tunnels/configurations.py">list</a>(tunnel_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/tunnels/configuration_list_response.py">ConfigurationListResponse</a></code>

### Connections

Types:

```python
from cloudflare.types.zero_trust.tunnels import ConnectionListResponse, ConnectionDeleteResponse
```

Methods:

- <code title="get /accounts/{account_id}/cfd_tunnel/{tunnel_id}/connections">client.zero_trust.tunnels.connections.<a href="./src/cloudflare/resources/zero_trust/tunnels/connections.py">list</a>(tunnel_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/tunnels/connection_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/tunnels/{tunnel_id}/connections">client.zero_trust.tunnels.connections.<a href="./src/cloudflare/resources/zero_trust/tunnels/connections.py">delete</a>(tunnel_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/tunnels/connection_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/tunnels/connection_delete_response.py">ConnectionDeleteResponse</a></code>

### Token

Types:

```python
from cloudflare.types.zero_trust.tunnels import TokenGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/cfd_tunnel/{tunnel_id}/token">client.zero_trust.tunnels.token.<a href="./src/cloudflare/resources/zero_trust/tunnels/token.py">get</a>(tunnel_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/tunnels/token_get_response.py">TokenGetResponse</a></code>

### Connectors

Types:

```python
from cloudflare.types.zero_trust.tunnels import ConnectorGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/cfd_tunnel/{tunnel_id}/connectors/{connector_id}">client.zero_trust.tunnels.connectors.<a href="./src/cloudflare/resources/zero_trust/tunnels/connectors.py">get</a>(connector_id, \*, account_id, tunnel_id) -> <a href="./src/cloudflare/types/zero_trust/tunnels/connector_get_response.py">ConnectorGetResponse</a></code>

### Management

Types:

```python
from cloudflare.types.zero_trust.tunnels import ManagementCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/cfd_tunnel/{tunnel_id}/management">client.zero_trust.tunnels.management.<a href="./src/cloudflare/resources/zero_trust/tunnels/management.py">create</a>(tunnel_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/tunnels/management_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/tunnels/management_create_response.py">ManagementCreateResponse</a></code>

## ConnectivitySettings

Types:

```python
from cloudflare.types.zero_trust import (
    ConnectivitySettingEditResponse,
    ConnectivitySettingGetResponse,
)
```

Methods:

- <code title="patch /accounts/{account_id}/zerotrust/connectivity_settings">client.zero_trust.connectivity_settings.<a href="./src/cloudflare/resources/zero_trust/connectivity_settings.py">edit</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/connectivity_setting_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/connectivity_setting_edit_response.py">ConnectivitySettingEditResponse</a></code>
- <code title="get /accounts/{account_id}/zerotrust/connectivity_settings">client.zero_trust.connectivity_settings.<a href="./src/cloudflare/resources/zero_trust/connectivity_settings.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/connectivity_setting_get_response.py">ConnectivitySettingGetResponse</a></code>

## DLP

### Datasets

Types:

```python
from cloudflare.types.zero_trust.dlp import (
    DatasetCreateResponse,
    DatasetUpdateResponse,
    DatasetListResponse,
    DatasetGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/dlp/datasets">client.zero_trust.dlp.datasets.<a href="./src/cloudflare/resources/zero_trust/dlp/datasets/datasets.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/dataset_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/dataset_create_response.py">Optional</a></code>
- <code title="put /accounts/{account_id}/dlp/datasets/{dataset_id}">client.zero_trust.dlp.datasets.<a href="./src/cloudflare/resources/zero_trust/dlp/datasets/datasets.py">update</a>(dataset_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/dataset_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/dataset_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/dlp/datasets">client.zero_trust.dlp.datasets.<a href="./src/cloudflare/resources/zero_trust/dlp/datasets/datasets.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/dataset_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/dlp/datasets/{dataset_id}">client.zero_trust.dlp.datasets.<a href="./src/cloudflare/resources/zero_trust/dlp/datasets/datasets.py">delete</a>(dataset_id, \*, account_id) -> None</code>
- <code title="get /accounts/{account_id}/dlp/datasets/{dataset_id}">client.zero_trust.dlp.datasets.<a href="./src/cloudflare/resources/zero_trust/dlp/datasets/datasets.py">get</a>(dataset_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/dataset_get_response.py">Optional</a></code>

#### Upload

Types:

```python
from cloudflare.types.zero_trust.dlp.datasets import UploadCreateResponse, UploadEditResponse
```

Methods:

- <code title="post /accounts/{account_id}/dlp/datasets/{dataset_id}/upload">client.zero_trust.dlp.datasets.upload.<a href="./src/cloudflare/resources/zero_trust/dlp/datasets/upload.py">create</a>(dataset_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/datasets/upload_create_response.py">Optional</a></code>
- <code title="post /accounts/{account_id}/dlp/datasets/{dataset_id}/upload/{version}">client.zero_trust.dlp.datasets.upload.<a href="./src/cloudflare/resources/zero_trust/dlp/datasets/upload.py">edit</a>(version, \*, account_id, dataset_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/datasets/upload_edit_response.py">Optional</a></code>

### Patterns

Types:

```python
from cloudflare.types.zero_trust.dlp import PatternValidateResponse
```

Methods:

- <code title="post /accounts/{account_id}/dlp/patterns/validate">client.zero_trust.dlp.patterns.<a href="./src/cloudflare/resources/zero_trust/dlp/patterns.py">validate</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/pattern_validate_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/pattern_validate_response.py">PatternValidateResponse</a></code>

### PayloadLogs

Types:

```python
from cloudflare.types.zero_trust.dlp import PayloadLogUpdateResponse, PayloadLogGetResponse
```

Methods:

- <code title="put /accounts/{account_id}/dlp/payload_log">client.zero_trust.dlp.payload_logs.<a href="./src/cloudflare/resources/zero_trust/dlp/payload_logs.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/payload_log_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/payload_log_update_response.py">PayloadLogUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/dlp/payload_log">client.zero_trust.dlp.payload_logs.<a href="./src/cloudflare/resources/zero_trust/dlp/payload_logs.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/payload_log_get_response.py">PayloadLogGetResponse</a></code>

### Profiles

Types:

```python
from cloudflare.types.zero_trust.dlp import ProfileListResponse, ProfileGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/dlp/profiles">client.zero_trust.dlp.profiles.<a href="./src/cloudflare/resources/zero_trust/dlp/profiles/profiles.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/profile_list_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/dlp/profiles/{profile_id}">client.zero_trust.dlp.profiles.<a href="./src/cloudflare/resources/zero_trust/dlp/profiles/profiles.py">get</a>(profile_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/profile_get_response.py">ProfileGetResponse</a></code>

#### Customs

Types:

```python
from cloudflare.types.zero_trust.dlp.profiles import (
    CustomCreateResponse,
    CustomUpdateResponse,
    CustomDeleteResponse,
    CustomGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/dlp/profiles/custom">client.zero_trust.dlp.profiles.customs.<a href="./src/cloudflare/resources/zero_trust/dlp/profiles/customs.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/profiles/custom_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/profiles/custom_create_response.py">Optional</a></code>
- <code title="put /accounts/{account_id}/dlp/profiles/custom/{profile_id}">client.zero_trust.dlp.profiles.customs.<a href="./src/cloudflare/resources/zero_trust/dlp/profiles/customs.py">update</a>(profile_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/profiles/custom_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/profiles/custom_update_response.py">CustomUpdateResponse</a></code>
- <code title="delete /accounts/{account_id}/dlp/profiles/custom/{profile_id}">client.zero_trust.dlp.profiles.customs.<a href="./src/cloudflare/resources/zero_trust/dlp/profiles/customs.py">delete</a>(profile_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/profiles/custom_delete_response.py">CustomDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/dlp/profiles/custom/{profile_id}">client.zero_trust.dlp.profiles.customs.<a href="./src/cloudflare/resources/zero_trust/dlp/profiles/customs.py">get</a>(profile_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/profiles/custom_get_response.py">CustomGetResponse</a></code>

#### Predefineds

Types:

```python
from cloudflare.types.zero_trust.dlp.profiles import PredefinedUpdateResponse, PredefinedGetResponse
```

Methods:

- <code title="put /accounts/{account_id}/dlp/profiles/predefined/{profile_id}">client.zero_trust.dlp.profiles.predefineds.<a href="./src/cloudflare/resources/zero_trust/dlp/profiles/predefineds.py">update</a>(profile_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/profiles/predefined_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/profiles/predefined_update_response.py">PredefinedUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/dlp/profiles/predefined/{profile_id}">client.zero_trust.dlp.profiles.predefineds.<a href="./src/cloudflare/resources/zero_trust/dlp/profiles/predefineds.py">get</a>(profile_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/profiles/predefined_get_response.py">PredefinedGetResponse</a></code>

## Gateway

Types:

```python
from cloudflare.types.zero_trust import GatewayCreateResponse, GatewayListResponse
```

Methods:

- <code title="post /accounts/{account_id}/gateway">client.zero_trust.gateway.<a href="./src/cloudflare/resources/zero_trust/gateway/gateway.py">create</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway_create_response.py">GatewayCreateResponse</a></code>
- <code title="get /accounts/{account_id}/gateway">client.zero_trust.gateway.<a href="./src/cloudflare/resources/zero_trust/gateway/gateway.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway_list_response.py">GatewayListResponse</a></code>

### AuditSSHSettings

Types:

```python
from cloudflare.types.zero_trust.gateway import (
    AuditSSHSettingUpdateResponse,
    AuditSSHSettingGetResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/gateway/audit_ssh_settings">client.zero_trust.gateway.audit_ssh_settings.<a href="./src/cloudflare/resources/zero_trust/gateway/audit_ssh_settings.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/audit_ssh_setting_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/audit_ssh_setting_update_response.py">AuditSSHSettingUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/gateway/audit_ssh_settings">client.zero_trust.gateway.audit_ssh_settings.<a href="./src/cloudflare/resources/zero_trust/gateway/audit_ssh_settings.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/audit_ssh_setting_get_response.py">AuditSSHSettingGetResponse</a></code>

### Categories

Types:

```python
from cloudflare.types.zero_trust.gateway import CategoryListResponse
```

Methods:

- <code title="get /accounts/{account_id}/gateway/categories">client.zero_trust.gateway.categories.<a href="./src/cloudflare/resources/zero_trust/gateway/categories.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/category_list_response.py">Optional</a></code>

### AppTypes

Types:

```python
from cloudflare.types.zero_trust.gateway import AppTypeListResponse
```

Methods:

- <code title="get /accounts/{account_id}/gateway/app_types">client.zero_trust.gateway.app_types.<a href="./src/cloudflare/resources/zero_trust/gateway/app_types.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/app_type_list_response.py">Optional</a></code>

### Configurations

Types:

```python
from cloudflare.types.zero_trust.gateway import (
    ConfigurationUpdateResponse,
    ConfigurationEditResponse,
    ConfigurationGetResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/gateway/configuration">client.zero_trust.gateway.configurations.<a href="./src/cloudflare/resources/zero_trust/gateway/configurations.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/configuration_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/configuration_update_response.py">ConfigurationUpdateResponse</a></code>
- <code title="patch /accounts/{account_id}/gateway/configuration">client.zero_trust.gateway.configurations.<a href="./src/cloudflare/resources/zero_trust/gateway/configurations.py">edit</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/configuration_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/configuration_edit_response.py">ConfigurationEditResponse</a></code>
- <code title="get /accounts/{account_id}/gateway/configuration">client.zero_trust.gateway.configurations.<a href="./src/cloudflare/resources/zero_trust/gateway/configurations.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/configuration_get_response.py">ConfigurationGetResponse</a></code>

### Lists

Types:

```python
from cloudflare.types.zero_trust.gateway import (
    ListCreateResponse,
    ListUpdateResponse,
    ListListResponse,
    ListDeleteResponse,
    ListEditResponse,
    ListGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/gateway/lists">client.zero_trust.gateway.lists.<a href="./src/cloudflare/resources/zero_trust/gateway/lists/lists.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/list_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/list_create_response.py">ListCreateResponse</a></code>
- <code title="put /accounts/{account_id}/gateway/lists/{list_id}">client.zero_trust.gateway.lists.<a href="./src/cloudflare/resources/zero_trust/gateway/lists/lists.py">update</a>(list_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/list_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/list_update_response.py">ListUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/gateway/lists">client.zero_trust.gateway.lists.<a href="./src/cloudflare/resources/zero_trust/gateway/lists/lists.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/list_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/gateway/lists/{list_id}">client.zero_trust.gateway.lists.<a href="./src/cloudflare/resources/zero_trust/gateway/lists/lists.py">delete</a>(list_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/list_delete_response.py">ListDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/gateway/lists/{list_id}">client.zero_trust.gateway.lists.<a href="./src/cloudflare/resources/zero_trust/gateway/lists/lists.py">edit</a>(list_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/list_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/list_edit_response.py">ListEditResponse</a></code>
- <code title="get /accounts/{account_id}/gateway/lists/{list_id}">client.zero_trust.gateway.lists.<a href="./src/cloudflare/resources/zero_trust/gateway/lists/lists.py">get</a>(list_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/list_get_response.py">ListGetResponse</a></code>

#### Items

Types:

```python
from cloudflare.types.zero_trust.gateway.lists import ItemListResponse
```

Methods:

- <code title="get /accounts/{account_id}/gateway/lists/{list_id}/items">client.zero_trust.gateway.lists.items.<a href="./src/cloudflare/resources/zero_trust/gateway/lists/items.py">list</a>(list_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/lists/item_list_response.py">Optional</a></code>

### Locations

Types:

```python
from cloudflare.types.zero_trust.gateway import (
    LocationCreateResponse,
    LocationUpdateResponse,
    LocationListResponse,
    LocationDeleteResponse,
    LocationGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/gateway/locations">client.zero_trust.gateway.locations.<a href="./src/cloudflare/resources/zero_trust/gateway/locations.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/location_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/location_create_response.py">LocationCreateResponse</a></code>
- <code title="put /accounts/{account_id}/gateway/locations/{location_id}">client.zero_trust.gateway.locations.<a href="./src/cloudflare/resources/zero_trust/gateway/locations.py">update</a>(location_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/location_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/location_update_response.py">LocationUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/gateway/locations">client.zero_trust.gateway.locations.<a href="./src/cloudflare/resources/zero_trust/gateway/locations.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/location_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/gateway/locations/{location_id}">client.zero_trust.gateway.locations.<a href="./src/cloudflare/resources/zero_trust/gateway/locations.py">delete</a>(location_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/location_delete_response.py">LocationDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/gateway/locations/{location_id}">client.zero_trust.gateway.locations.<a href="./src/cloudflare/resources/zero_trust/gateway/locations.py">get</a>(location_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/location_get_response.py">LocationGetResponse</a></code>

### Loggings

Types:

```python
from cloudflare.types.zero_trust.gateway import LoggingUpdateResponse, LoggingGetResponse
```

Methods:

- <code title="put /accounts/{account_id}/gateway/logging">client.zero_trust.gateway.loggings.<a href="./src/cloudflare/resources/zero_trust/gateway/loggings.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/logging_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/logging_update_response.py">LoggingUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/gateway/logging">client.zero_trust.gateway.loggings.<a href="./src/cloudflare/resources/zero_trust/gateway/loggings.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/logging_get_response.py">LoggingGetResponse</a></code>

### ProxyEndpoints

Types:

```python
from cloudflare.types.zero_trust.gateway import (
    ProxyEndpointCreateResponse,
    ProxyEndpointListResponse,
    ProxyEndpointDeleteResponse,
    ProxyEndpointEditResponse,
    ProxyEndpointGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/gateway/proxy_endpoints">client.zero_trust.gateway.proxy_endpoints.<a href="./src/cloudflare/resources/zero_trust/gateway/proxy_endpoints.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/proxy_endpoint_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/proxy_endpoint_create_response.py">ProxyEndpointCreateResponse</a></code>
- <code title="get /accounts/{account_id}/gateway/proxy_endpoints">client.zero_trust.gateway.proxy_endpoints.<a href="./src/cloudflare/resources/zero_trust/gateway/proxy_endpoints.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/proxy_endpoint_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/gateway/proxy_endpoints/{proxy_endpoint_id}">client.zero_trust.gateway.proxy_endpoints.<a href="./src/cloudflare/resources/zero_trust/gateway/proxy_endpoints.py">delete</a>(proxy_endpoint_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/proxy_endpoint_delete_response.py">ProxyEndpointDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/gateway/proxy_endpoints/{proxy_endpoint_id}">client.zero_trust.gateway.proxy_endpoints.<a href="./src/cloudflare/resources/zero_trust/gateway/proxy_endpoints.py">edit</a>(proxy_endpoint_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/proxy_endpoint_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/proxy_endpoint_edit_response.py">ProxyEndpointEditResponse</a></code>
- <code title="get /accounts/{account_id}/gateway/proxy_endpoints/{proxy_endpoint_id}">client.zero_trust.gateway.proxy_endpoints.<a href="./src/cloudflare/resources/zero_trust/gateway/proxy_endpoints.py">get</a>(proxy_endpoint_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/proxy_endpoint_get_response.py">ProxyEndpointGetResponse</a></code>

### Rules

Types:

```python
from cloudflare.types.zero_trust.gateway import (
    RuleCreateResponse,
    RuleUpdateResponse,
    RuleListResponse,
    RuleDeleteResponse,
    RuleGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/gateway/rules">client.zero_trust.gateway.rules.<a href="./src/cloudflare/resources/zero_trust/gateway/rules.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/rule_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/rule_create_response.py">RuleCreateResponse</a></code>
- <code title="put /accounts/{account_id}/gateway/rules/{rule_id}">client.zero_trust.gateway.rules.<a href="./src/cloudflare/resources/zero_trust/gateway/rules.py">update</a>(rule_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/rule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/rule_update_response.py">RuleUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/gateway/rules">client.zero_trust.gateway.rules.<a href="./src/cloudflare/resources/zero_trust/gateway/rules.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/rule_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/gateway/rules/{rule_id}">client.zero_trust.gateway.rules.<a href="./src/cloudflare/resources/zero_trust/gateway/rules.py">delete</a>(rule_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/rule_delete_response.py">RuleDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/gateway/rules/{rule_id}">client.zero_trust.gateway.rules.<a href="./src/cloudflare/resources/zero_trust/gateway/rules.py">get</a>(rule_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/rule_get_response.py">RuleGetResponse</a></code>

## Networks

### Routes

Types:

```python
from cloudflare.types.zero_trust.networks import (
    RouteCreateResponse,
    RouteListResponse,
    RouteDeleteResponse,
    RouteEditResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/teamnet/routes">client.zero_trust.networks.routes.<a href="./src/cloudflare/resources/zero_trust/networks/routes/routes.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/networks/route_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/networks/route_create_response.py">RouteCreateResponse</a></code>
- <code title="get /accounts/{account_id}/teamnet/routes">client.zero_trust.networks.routes.<a href="./src/cloudflare/resources/zero_trust/networks/routes/routes.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/networks/route_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/networks/route_list_response.py">SyncV4PagePaginationArray[RouteListResponse]</a></code>
- <code title="delete /accounts/{account_id}/teamnet/routes/{route_id}">client.zero_trust.networks.routes.<a href="./src/cloudflare/resources/zero_trust/networks/routes/routes.py">delete</a>(route_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/networks/route_delete_response.py">RouteDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/teamnet/routes/{route_id}">client.zero_trust.networks.routes.<a href="./src/cloudflare/resources/zero_trust/networks/routes/routes.py">edit</a>(route_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/networks/route_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/networks/route_edit_response.py">RouteEditResponse</a></code>

#### IPs

Types:

```python
from cloudflare.types.zero_trust.networks.routes import IPGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/teamnet/routes/ip/{ip}">client.zero_trust.networks.routes.ips.<a href="./src/cloudflare/resources/zero_trust/networks/routes/ips.py">get</a>(ip, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/networks/routes/ip_get_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/networks/routes/ip_get_response.py">IPGetResponse</a></code>

#### Networks

Types:

```python
from cloudflare.types.zero_trust.networks.routes import (
    NetworkCreateResponse,
    NetworkDeleteResponse,
    NetworkEditResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}">client.zero_trust.networks.routes.networks.<a href="./src/cloudflare/resources/zero_trust/networks/routes/networks.py">create</a>(ip_network_encoded, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/networks/routes/network_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/networks/routes/network_create_response.py">NetworkCreateResponse</a></code>
- <code title="delete /accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}">client.zero_trust.networks.routes.networks.<a href="./src/cloudflare/resources/zero_trust/networks/routes/networks.py">delete</a>(ip_network_encoded, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/networks/routes/network_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/networks/routes/network_delete_response.py">NetworkDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}">client.zero_trust.networks.routes.networks.<a href="./src/cloudflare/resources/zero_trust/networks/routes/networks.py">edit</a>(ip_network_encoded, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/networks/routes/network_edit_response.py">NetworkEditResponse</a></code>

### VirtualNetworks

Types:

```python
from cloudflare.types.zero_trust.networks import (
    VirtualNetworkCreateResponse,
    VirtualNetworkListResponse,
    VirtualNetworkDeleteResponse,
    VirtualNetworkEditResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/teamnet/virtual_networks">client.zero_trust.networks.virtual_networks.<a href="./src/cloudflare/resources/zero_trust/networks/virtual_networks.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/networks/virtual_network_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/networks/virtual_network_create_response.py">VirtualNetworkCreateResponse</a></code>
- <code title="get /accounts/{account_id}/teamnet/virtual_networks">client.zero_trust.networks.virtual_networks.<a href="./src/cloudflare/resources/zero_trust/networks/virtual_networks.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/networks/virtual_network_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/networks/virtual_network_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/teamnet/virtual_networks/{virtual_network_id}">client.zero_trust.networks.virtual_networks.<a href="./src/cloudflare/resources/zero_trust/networks/virtual_networks.py">delete</a>(virtual_network_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/networks/virtual_network_delete_response.py">VirtualNetworkDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/teamnet/virtual_networks/{virtual_network_id}">client.zero_trust.networks.virtual_networks.<a href="./src/cloudflare/resources/zero_trust/networks/virtual_networks.py">edit</a>(virtual_network_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/networks/virtual_network_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/networks/virtual_network_edit_response.py">VirtualNetworkEditResponse</a></code>

# Challenges

## Widgets

Types:

```python
from cloudflare.types.challenges import (
    WidgetCreateResponse,
    WidgetUpdateResponse,
    WidgetListResponse,
    WidgetDeleteResponse,
    WidgetGetResponse,
    WidgetRotateSecretResponse,
)
```

Methods:

- <code title="post /accounts/{account_identifier}/challenges/widgets">client.challenges.widgets.<a href="./src/cloudflare/resources/challenges/widgets.py">create</a>(account_identifier, \*\*<a href="src/cloudflare/types/challenges/widget_create_params.py">params</a>) -> <a href="./src/cloudflare/types/challenges/widget_create_response.py">Optional</a></code>
- <code title="put /accounts/{account_identifier}/challenges/widgets/{sitekey}">client.challenges.widgets.<a href="./src/cloudflare/resources/challenges/widgets.py">update</a>(sitekey, \*, account_identifier, \*\*<a href="src/cloudflare/types/challenges/widget_update_params.py">params</a>) -> <a href="./src/cloudflare/types/challenges/widget_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_identifier}/challenges/widgets">client.challenges.widgets.<a href="./src/cloudflare/resources/challenges/widgets.py">list</a>(account_identifier, \*\*<a href="src/cloudflare/types/challenges/widget_list_params.py">params</a>) -> <a href="./src/cloudflare/types/challenges/widget_list_response.py">SyncV4PagePaginationArray[WidgetListResponse]</a></code>
- <code title="delete /accounts/{account_identifier}/challenges/widgets/{sitekey}">client.challenges.widgets.<a href="./src/cloudflare/resources/challenges/widgets.py">delete</a>(sitekey, \*, account_identifier) -> <a href="./src/cloudflare/types/challenges/widget_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_identifier}/challenges/widgets/{sitekey}">client.challenges.widgets.<a href="./src/cloudflare/resources/challenges/widgets.py">get</a>(sitekey, \*, account_identifier) -> <a href="./src/cloudflare/types/challenges/widget_get_response.py">Optional</a></code>
- <code title="post /accounts/{account_identifier}/challenges/widgets/{sitekey}/rotate_secret">client.challenges.widgets.<a href="./src/cloudflare/resources/challenges/widgets.py">rotate_secret</a>(sitekey, \*, account_identifier, \*\*<a href="src/cloudflare/types/challenges/widget_rotate_secret_params.py">params</a>) -> <a href="./src/cloudflare/types/challenges/widget_rotate_secret_response.py">Optional</a></code>

# Hyperdrive

## Configs

Types:

```python
from cloudflare.types.hyperdrive import (
    ConfigCreateResponse,
    ConfigUpdateResponse,
    ConfigListResponse,
    ConfigDeleteResponse,
    ConfigEditResponse,
    ConfigGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/hyperdrive/configs">client.hyperdrive.configs.<a href="./src/cloudflare/resources/hyperdrive/configs.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/hyperdrive/config_create_params.py">params</a>) -> <a href="./src/cloudflare/types/hyperdrive/config_create_response.py">Optional</a></code>
- <code title="put /accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}">client.hyperdrive.configs.<a href="./src/cloudflare/resources/hyperdrive/configs.py">update</a>(hyperdrive_id, \*, account_id, \*\*<a href="src/cloudflare/types/hyperdrive/config_update_params.py">params</a>) -> <a href="./src/cloudflare/types/hyperdrive/config_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/hyperdrive/configs">client.hyperdrive.configs.<a href="./src/cloudflare/resources/hyperdrive/configs.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/hyperdrive/config_list_response.py">ConfigListResponse</a></code>
- <code title="delete /accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}">client.hyperdrive.configs.<a href="./src/cloudflare/resources/hyperdrive/configs.py">delete</a>(hyperdrive_id, \*, account_id) -> <a href="./src/cloudflare/types/hyperdrive/config_delete_response.py">Optional</a></code>
- <code title="patch /accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}">client.hyperdrive.configs.<a href="./src/cloudflare/resources/hyperdrive/configs.py">edit</a>(hyperdrive_id, \*, account_id, \*\*<a href="src/cloudflare/types/hyperdrive/config_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/hyperdrive/config_edit_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}">client.hyperdrive.configs.<a href="./src/cloudflare/resources/hyperdrive/configs.py">get</a>(hyperdrive_id, \*, account_id) -> <a href="./src/cloudflare/types/hyperdrive/config_get_response.py">Optional</a></code>

# RUM

## SiteInfos

Types:

```python
from cloudflare.types.rum import (
    SiteInfoCreateResponse,
    SiteInfoUpdateResponse,
    SiteInfoListResponse,
    SiteInfoDeleteResponse,
    SiteInfoGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/rum/site_info">client.rum.site_infos.<a href="./src/cloudflare/resources/rum/site_infos.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/rum/site_info_create_params.py">params</a>) -> <a href="./src/cloudflare/types/rum/site_info_create_response.py">Optional</a></code>
- <code title="put /accounts/{account_id}/rum/site_info/{site_id}">client.rum.site_infos.<a href="./src/cloudflare/resources/rum/site_infos.py">update</a>(site_id, \*, account_id, \*\*<a href="src/cloudflare/types/rum/site_info_update_params.py">params</a>) -> <a href="./src/cloudflare/types/rum/site_info_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/rum/site_info/list">client.rum.site_infos.<a href="./src/cloudflare/resources/rum/site_infos.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/rum/site_info_list_params.py">params</a>) -> <a href="./src/cloudflare/types/rum/site_info_list_response.py">SyncV4PagePaginationArray[SiteInfoListResponse]</a></code>
- <code title="delete /accounts/{account_id}/rum/site_info/{site_id}">client.rum.site_infos.<a href="./src/cloudflare/resources/rum/site_infos.py">delete</a>(site_id, \*, account_id) -> <a href="./src/cloudflare/types/rum/site_info_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/rum/site_info/{site_id}">client.rum.site_infos.<a href="./src/cloudflare/resources/rum/site_infos.py">get</a>(site_id, \*, account_id) -> <a href="./src/cloudflare/types/rum/site_info_get_response.py">Optional</a></code>

## Rules

Types:

```python
from cloudflare.types.rum import (
    RuleCreateResponse,
    RuleUpdateResponse,
    RuleListResponse,
    RuleDeleteResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/rum/v2/{ruleset_id}/rule">client.rum.rules.<a href="./src/cloudflare/resources/rum/rules.py">create</a>(ruleset_id, \*, account_id, \*\*<a href="src/cloudflare/types/rum/rule_create_params.py">params</a>) -> <a href="./src/cloudflare/types/rum/rule_create_response.py">Optional</a></code>
- <code title="put /accounts/{account_id}/rum/v2/{ruleset_id}/rule/{rule_id}">client.rum.rules.<a href="./src/cloudflare/resources/rum/rules.py">update</a>(rule_id, \*, account_id, ruleset_id, \*\*<a href="src/cloudflare/types/rum/rule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/rum/rule_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/rum/v2/{ruleset_id}/rules">client.rum.rules.<a href="./src/cloudflare/resources/rum/rules.py">list</a>(ruleset_id, \*, account_id) -> <a href="./src/cloudflare/types/rum/rule_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/rum/v2/{ruleset_id}/rule/{rule_id}">client.rum.rules.<a href="./src/cloudflare/resources/rum/rules.py">delete</a>(rule_id, \*, account_id, ruleset_id) -> <a href="./src/cloudflare/types/rum/rule_delete_response.py">Optional</a></code>

# Vectorize

## Indexes

Types:

```python
from cloudflare.types.vectorize import (
    IndexCreateResponse,
    IndexUpdateResponse,
    IndexListResponse,
    IndexDeleteResponse,
    IndexDeleteByIDsResponse,
    IndexGetResponse,
    IndexGetByIDsResponse,
    IndexInsertResponse,
    IndexQueryResponse,
    IndexUpsertResponse,
)
```

Methods:

- <code title="post /accounts/{account_identifier}/vectorize/indexes">client.vectorize.indexes.<a href="./src/cloudflare/resources/vectorize/indexes.py">create</a>(account_identifier, \*\*<a href="src/cloudflare/types/vectorize/index_create_params.py">params</a>) -> <a href="./src/cloudflare/types/vectorize/index_create_response.py">Optional</a></code>
- <code title="put /accounts/{account_identifier}/vectorize/indexes/{index_name}">client.vectorize.indexes.<a href="./src/cloudflare/resources/vectorize/indexes.py">update</a>(index_name, \*, account_identifier, \*\*<a href="src/cloudflare/types/vectorize/index_update_params.py">params</a>) -> <a href="./src/cloudflare/types/vectorize/index_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_identifier}/vectorize/indexes">client.vectorize.indexes.<a href="./src/cloudflare/resources/vectorize/indexes.py">list</a>(account_identifier) -> <a href="./src/cloudflare/types/vectorize/index_list_response.py">IndexListResponse</a></code>
- <code title="delete /accounts/{account_identifier}/vectorize/indexes/{index_name}">client.vectorize.indexes.<a href="./src/cloudflare/resources/vectorize/indexes.py">delete</a>(index_name, \*, account_identifier) -> <a href="./src/cloudflare/types/vectorize/index_delete_response.py">Optional</a></code>
- <code title="post /accounts/{account_identifier}/vectorize/indexes/{index_name}/delete-by-ids">client.vectorize.indexes.<a href="./src/cloudflare/resources/vectorize/indexes.py">delete_by_ids</a>(index_name, \*, account_identifier, \*\*<a href="src/cloudflare/types/vectorize/index_delete_by_ids_params.py">params</a>) -> <a href="./src/cloudflare/types/vectorize/index_delete_by_ids_response.py">Optional</a></code>
- <code title="get /accounts/{account_identifier}/vectorize/indexes/{index_name}">client.vectorize.indexes.<a href="./src/cloudflare/resources/vectorize/indexes.py">get</a>(index_name, \*, account_identifier) -> <a href="./src/cloudflare/types/vectorize/index_get_response.py">Optional</a></code>
- <code title="post /accounts/{account_identifier}/vectorize/indexes/{index_name}/get-by-ids">client.vectorize.indexes.<a href="./src/cloudflare/resources/vectorize/indexes.py">get_by_ids</a>(index_name, \*, account_identifier, \*\*<a href="src/cloudflare/types/vectorize/index_get_by_ids_params.py">params</a>) -> <a href="./src/cloudflare/types/vectorize/index_get_by_ids_response.py">object</a></code>
- <code title="post /accounts/{account_identifier}/vectorize/indexes/{index_name}/insert">client.vectorize.indexes.<a href="./src/cloudflare/resources/vectorize/indexes.py">insert</a>(index_name, \*, account_identifier) -> <a href="./src/cloudflare/types/vectorize/index_insert_response.py">Optional</a></code>
- <code title="post /accounts/{account_identifier}/vectorize/indexes/{index_name}/query">client.vectorize.indexes.<a href="./src/cloudflare/resources/vectorize/indexes.py">query</a>(index_name, \*, account_identifier, \*\*<a href="src/cloudflare/types/vectorize/index_query_params.py">params</a>) -> <a href="./src/cloudflare/types/vectorize/index_query_response.py">Optional</a></code>
- <code title="post /accounts/{account_identifier}/vectorize/indexes/{index_name}/upsert">client.vectorize.indexes.<a href="./src/cloudflare/resources/vectorize/indexes.py">upsert</a>(index_name, \*, account_identifier) -> <a href="./src/cloudflare/types/vectorize/index_upsert_response.py">Optional</a></code>

# URLScanner

Types:

```python
from cloudflare.types import URLScannerScanResponse
```

Methods:

- <code title="get /accounts/{accountId}/urlscanner/scan">client.url_scanner.<a href="./src/cloudflare/resources/url_scanner/url_scanner.py">scan</a>(account_id, \*\*<a href="src/cloudflare/types/url_scanner_scan_params.py">params</a>) -> <a href="./src/cloudflare/types/url_scanner_scan_response.py">URLScannerScanResponse</a></code>

## Scans

Types:

```python
from cloudflare.types.url_scanner import ScanCreateResponse, ScanGetResponse, ScanHarResponse
```

Methods:

- <code title="post /accounts/{accountId}/urlscanner/scan">client.url_scanner.scans.<a href="./src/cloudflare/resources/url_scanner/scans.py">create</a>(account_id, \*\*<a href="src/cloudflare/types/url_scanner/scan_create_params.py">params</a>) -> <a href="./src/cloudflare/types/url_scanner/scan_create_response.py">ScanCreateResponse</a></code>
- <code title="get /accounts/{accountId}/urlscanner/scan/{scanId}">client.url_scanner.scans.<a href="./src/cloudflare/resources/url_scanner/scans.py">get</a>(scan_id, \*, account_id) -> <a href="./src/cloudflare/types/url_scanner/scan_get_response.py">ScanGetResponse</a></code>
- <code title="get /accounts/{accountId}/urlscanner/scan/{scanId}/har">client.url_scanner.scans.<a href="./src/cloudflare/resources/url_scanner/scans.py">har</a>(scan_id, \*, account_id) -> <a href="./src/cloudflare/types/url_scanner/scan_har_response.py">ScanHarResponse</a></code>
- <code title="get /accounts/{accountId}/urlscanner/scan/{scanId}/screenshot">client.url_scanner.scans.<a href="./src/cloudflare/resources/url_scanner/scans.py">screenshot</a>(scan_id, \*, account_id, \*\*<a href="src/cloudflare/types/url_scanner/scan_screenshot_params.py">params</a>) -> BinaryAPIResponse</code>

# Radar

## Annotations

### Outages

Types:

```python
from cloudflare.types.radar.annotations import OutageGetResponse, OutageLocationsResponse
```

Methods:

- <code title="get /radar/annotations/outages">client.radar.annotations.outages.<a href="./src/cloudflare/resources/radar/annotations/outages.py">get</a>(\*\*<a href="src/cloudflare/types/radar/annotations/outage_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/annotations/outage_get_response.py">OutageGetResponse</a></code>
- <code title="get /radar/annotations/outages/locations">client.radar.annotations.outages.<a href="./src/cloudflare/resources/radar/annotations/outages.py">locations</a>(\*\*<a href="src/cloudflare/types/radar/annotations/outage_locations_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/annotations/outage_locations_response.py">OutageLocationsResponse</a></code>

## BGP

Types:

```python
from cloudflare.types.radar import BGPTimeseriesResponse
```

Methods:

- <code title="get /radar/bgp/timeseries">client.radar.bgp.<a href="./src/cloudflare/resources/radar/bgp/bgp.py">timeseries</a>(\*\*<a href="src/cloudflare/types/radar/bgp_timeseries_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bgp_timeseries_response.py">BGPTimeseriesResponse</a></code>

### Leaks

Types:

```python
from cloudflare.types.radar.bgp import LeakEventsResponse
```

Methods:

- <code title="get /radar/bgp/leaks/events">client.radar.bgp.leaks.<a href="./src/cloudflare/resources/radar/bgp/leaks.py">events</a>(\*\*<a href="src/cloudflare/types/radar/bgp/leak_events_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bgp/leak_events_response.py">LeakEventsResponse</a></code>

### Top

Types:

```python
from cloudflare.types.radar.bgp import TopPrefixesResponse
```

Methods:

- <code title="get /radar/bgp/top/prefixes">client.radar.bgp.top.<a href="./src/cloudflare/resources/radar/bgp/top/top.py">prefixes</a>(\*\*<a href="src/cloudflare/types/radar/bgp/top_prefixes_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bgp/top_prefixes_response.py">TopPrefixesResponse</a></code>

#### Ases

Types:

```python
from cloudflare.types.radar.bgp.top import AseGetResponse, AsePrefixesResponse
```

Methods:

- <code title="get /radar/bgp/top/ases">client.radar.bgp.top.ases.<a href="./src/cloudflare/resources/radar/bgp/top/ases.py">get</a>(\*\*<a href="src/cloudflare/types/radar/bgp/top/ase_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bgp/top/ase_get_response.py">AseGetResponse</a></code>
- <code title="get /radar/bgp/top/ases/prefixes">client.radar.bgp.top.ases.<a href="./src/cloudflare/resources/radar/bgp/top/ases.py">prefixes</a>(\*\*<a href="src/cloudflare/types/radar/bgp/top/ase_prefixes_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bgp/top/ase_prefixes_response.py">AsePrefixesResponse</a></code>

### Hijacks

Types:

```python
from cloudflare.types.radar.bgp import HijackEventsResponse
```

Methods:

- <code title="get /radar/bgp/hijacks/events">client.radar.bgp.hijacks.<a href="./src/cloudflare/resources/radar/bgp/hijacks.py">events</a>(\*\*<a href="src/cloudflare/types/radar/bgp/hijack_events_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bgp/hijack_events_response.py">HijackEventsResponse</a></code>

### Routes

Types:

```python
from cloudflare.types.radar.bgp import (
    RouteMoasResponse,
    RoutePfx2asResponse,
    RouteStatsResponse,
    RouteTimeseriesResponse,
)
```

Methods:

- <code title="get /radar/bgp/routes/moas">client.radar.bgp.routes.<a href="./src/cloudflare/resources/radar/bgp/routes.py">moas</a>(\*\*<a href="src/cloudflare/types/radar/bgp/route_moas_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bgp/route_moas_response.py">RouteMoasResponse</a></code>
- <code title="get /radar/bgp/routes/pfx2as">client.radar.bgp.routes.<a href="./src/cloudflare/resources/radar/bgp/routes.py">pfx2as</a>(\*\*<a href="src/cloudflare/types/radar/bgp/route_pfx2as_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bgp/route_pfx2as_response.py">RoutePfx2asResponse</a></code>
- <code title="get /radar/bgp/routes/stats">client.radar.bgp.routes.<a href="./src/cloudflare/resources/radar/bgp/routes.py">stats</a>(\*\*<a href="src/cloudflare/types/radar/bgp/route_stats_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bgp/route_stats_response.py">RouteStatsResponse</a></code>
- <code title="get /radar/bgp/routes/timeseries">client.radar.bgp.routes.<a href="./src/cloudflare/resources/radar/bgp/routes.py">timeseries</a>(\*\*<a href="src/cloudflare/types/radar/bgp/route_timeseries_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bgp/route_timeseries_response.py">RouteTimeseriesResponse</a></code>

## Datasets

Types:

```python
from cloudflare.types.radar import DatasetListResponse, DatasetDownloadResponse, DatasetGetResponse
```

Methods:

- <code title="get /radar/datasets">client.radar.datasets.<a href="./src/cloudflare/resources/radar/datasets.py">list</a>(\*\*<a href="src/cloudflare/types/radar/dataset_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/dataset_list_response.py">DatasetListResponse</a></code>
- <code title="post /radar/datasets/download">client.radar.datasets.<a href="./src/cloudflare/resources/radar/datasets.py">download</a>(\*\*<a href="src/cloudflare/types/radar/dataset_download_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/dataset_download_response.py">DatasetDownloadResponse</a></code>
- <code title="get /radar/datasets/{alias}">client.radar.datasets.<a href="./src/cloudflare/resources/radar/datasets.py">get</a>(alias, \*\*<a href="src/cloudflare/types/radar/dataset_get_params.py">params</a>) -> str</code>

## DNS

### Top

Types:

```python
from cloudflare.types.radar.dns import TopAsesResponse, TopLocationsResponse
```

Methods:

- <code title="get /radar/dns/top/ases">client.radar.dns.top.<a href="./src/cloudflare/resources/radar/dns/top.py">ases</a>(\*\*<a href="src/cloudflare/types/radar/dns/top_ases_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/dns/top_ases_response.py">TopAsesResponse</a></code>
- <code title="get /radar/dns/top/locations">client.radar.dns.top.<a href="./src/cloudflare/resources/radar/dns/top.py">locations</a>(\*\*<a href="src/cloudflare/types/radar/dns/top_locations_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/dns/top_locations_response.py">TopLocationsResponse</a></code>

## Netflows

Types:

```python
from cloudflare.types.radar import NetflowTimeseriesResponse
```

Methods:

- <code title="get /radar/netflows/timeseries">client.radar.netflows.<a href="./src/cloudflare/resources/radar/netflows/netflows.py">timeseries</a>(\*\*<a href="src/cloudflare/types/radar/netflow_timeseries_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/netflow_timeseries_response.py">NetflowTimeseriesResponse</a></code>

### Top

Types:

```python
from cloudflare.types.radar.netflows import TopAsesResponse, TopLocationsResponse
```

Methods:

- <code title="get /radar/netflows/top/ases">client.radar.netflows.top.<a href="./src/cloudflare/resources/radar/netflows/top.py">ases</a>(\*\*<a href="src/cloudflare/types/radar/netflows/top_ases_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/netflows/top_ases_response.py">TopAsesResponse</a></code>
- <code title="get /radar/netflows/top/locations">client.radar.netflows.top.<a href="./src/cloudflare/resources/radar/netflows/top.py">locations</a>(\*\*<a href="src/cloudflare/types/radar/netflows/top_locations_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/netflows/top_locations_response.py">TopLocationsResponse</a></code>

## Search

Types:

```python
from cloudflare.types.radar import SearchGlobalResponse
```

Methods:

- <code title="get /radar/search/global">client.radar.search.<a href="./src/cloudflare/resources/radar/search.py">global\_</a>(\*\*<a href="src/cloudflare/types/radar/search_global_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/search_global_response.py">SearchGlobalResponse</a></code>

## VerifiedBots

### Top

Types:

```python
from cloudflare.types.radar.verified_bots import TopBotsResponse, TopCategoriesResponse
```

Methods:

- <code title="get /radar/verified_bots/top/bots">client.radar.verified_bots.top.<a href="./src/cloudflare/resources/radar/verified_bots/top.py">bots</a>(\*\*<a href="src/cloudflare/types/radar/verified_bots/top_bots_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/verified_bots/top_bots_response.py">TopBotsResponse</a></code>
- <code title="get /radar/verified_bots/top/categories">client.radar.verified_bots.top.<a href="./src/cloudflare/resources/radar/verified_bots/top.py">categories</a>(\*\*<a href="src/cloudflare/types/radar/verified_bots/top_categories_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/verified_bots/top_categories_response.py">TopCategoriesResponse</a></code>

## AS112

Types:

```python
from cloudflare.types.radar import AS112TimeseriesResponse
```

Methods:

- <code title="get /radar/as112/timeseries">client.radar.as112.<a href="./src/cloudflare/resources/radar/as112/as112.py">timeseries</a>(\*\*<a href="src/cloudflare/types/radar/as112_timeseries_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/as112_timeseries_response.py">AS112TimeseriesResponse</a></code>

### Summary

Types:

```python
from cloudflare.types.radar.as112 import (
    SummaryDNSSECResponse,
    SummaryEdnsResponse,
    SummaryIPVersionResponse,
    SummaryProtocolResponse,
    SummaryQueryTypeResponse,
    SummaryResponseCodesResponse,
)
```

Methods:

- <code title="get /radar/as112/summary/dnssec">client.radar.as112.summary.<a href="./src/cloudflare/resources/radar/as112/summary.py">dnssec</a>(\*\*<a href="src/cloudflare/types/radar/as112/summary_dnssec_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/as112/summary_dnssec_response.py">SummaryDNSSECResponse</a></code>
- <code title="get /radar/as112/summary/edns">client.radar.as112.summary.<a href="./src/cloudflare/resources/radar/as112/summary.py">edns</a>(\*\*<a href="src/cloudflare/types/radar/as112/summary_edns_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/as112/summary_edns_response.py">SummaryEdnsResponse</a></code>
- <code title="get /radar/as112/summary/ip_version">client.radar.as112.summary.<a href="./src/cloudflare/resources/radar/as112/summary.py">ip_version</a>(\*\*<a href="src/cloudflare/types/radar/as112/summary_ip_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/as112/summary_ip_version_response.py">SummaryIPVersionResponse</a></code>
- <code title="get /radar/as112/summary/protocol">client.radar.as112.summary.<a href="./src/cloudflare/resources/radar/as112/summary.py">protocol</a>(\*\*<a href="src/cloudflare/types/radar/as112/summary_protocol_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/as112/summary_protocol_response.py">SummaryProtocolResponse</a></code>
- <code title="get /radar/as112/summary/query_type">client.radar.as112.summary.<a href="./src/cloudflare/resources/radar/as112/summary.py">query_type</a>(\*\*<a href="src/cloudflare/types/radar/as112/summary_query_type_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/as112/summary_query_type_response.py">SummaryQueryTypeResponse</a></code>
- <code title="get /radar/as112/summary/response_codes">client.radar.as112.summary.<a href="./src/cloudflare/resources/radar/as112/summary.py">response_codes</a>(\*\*<a href="src/cloudflare/types/radar/as112/summary_response_codes_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/as112/summary_response_codes_response.py">SummaryResponseCodesResponse</a></code>

### TimeseriesGroups

Types:

```python
from cloudflare.types.radar.as112 import (
    TimeseriesGroupDNSSECResponse,
    TimeseriesGroupEdnsResponse,
    TimeseriesGroupIPVersionResponse,
    TimeseriesGroupProtocolResponse,
    TimeseriesGroupQueryTypeResponse,
    TimeseriesGroupResponseCodesResponse,
)
```

Methods:

- <code title="get /radar/as112/timeseries_groups/dnssec">client.radar.as112.timeseries_groups.<a href="./src/cloudflare/resources/radar/as112/timeseries_groups.py">dnssec</a>(\*\*<a href="src/cloudflare/types/radar/as112/timeseries_group_dnssec_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/as112/timeseries_group_dnssec_response.py">TimeseriesGroupDNSSECResponse</a></code>
- <code title="get /radar/as112/timeseries_groups/edns">client.radar.as112.timeseries_groups.<a href="./src/cloudflare/resources/radar/as112/timeseries_groups.py">edns</a>(\*\*<a href="src/cloudflare/types/radar/as112/timeseries_group_edns_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/as112/timeseries_group_edns_response.py">TimeseriesGroupEdnsResponse</a></code>
- <code title="get /radar/as112/timeseries_groups/ip_version">client.radar.as112.timeseries_groups.<a href="./src/cloudflare/resources/radar/as112/timeseries_groups.py">ip_version</a>(\*\*<a href="src/cloudflare/types/radar/as112/timeseries_group_ip_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/as112/timeseries_group_ip_version_response.py">TimeseriesGroupIPVersionResponse</a></code>
- <code title="get /radar/as112/timeseries_groups/protocol">client.radar.as112.timeseries_groups.<a href="./src/cloudflare/resources/radar/as112/timeseries_groups.py">protocol</a>(\*\*<a href="src/cloudflare/types/radar/as112/timeseries_group_protocol_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/as112/timeseries_group_protocol_response.py">TimeseriesGroupProtocolResponse</a></code>
- <code title="get /radar/as112/timeseries_groups/query_type">client.radar.as112.timeseries_groups.<a href="./src/cloudflare/resources/radar/as112/timeseries_groups.py">query_type</a>(\*\*<a href="src/cloudflare/types/radar/as112/timeseries_group_query_type_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/as112/timeseries_group_query_type_response.py">TimeseriesGroupQueryTypeResponse</a></code>
- <code title="get /radar/as112/timeseries_groups/response_codes">client.radar.as112.timeseries_groups.<a href="./src/cloudflare/resources/radar/as112/timeseries_groups.py">response_codes</a>(\*\*<a href="src/cloudflare/types/radar/as112/timeseries_group_response_codes_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/as112/timeseries_group_response_codes_response.py">TimeseriesGroupResponseCodesResponse</a></code>

### Top

Types:

```python
from cloudflare.types.radar.as112 import (
    TopDNSSECResponse,
    TopEdnsResponse,
    TopIPVersionResponse,
    TopLocationsResponse,
)
```

Methods:

- <code title="get /radar/as112/top/locations/dnssec/{dnssec}">client.radar.as112.top.<a href="./src/cloudflare/resources/radar/as112/top.py">dnssec</a>(dnssec, \*\*<a href="src/cloudflare/types/radar/as112/top_dnssec_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/as112/top_dnssec_response.py">TopDNSSECResponse</a></code>
- <code title="get /radar/as112/top/locations/edns/{edns}">client.radar.as112.top.<a href="./src/cloudflare/resources/radar/as112/top.py">edns</a>(edns, \*\*<a href="src/cloudflare/types/radar/as112/top_edns_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/as112/top_edns_response.py">TopEdnsResponse</a></code>
- <code title="get /radar/as112/top/locations/ip_version/{ip_version}">client.radar.as112.top.<a href="./src/cloudflare/resources/radar/as112/top.py">ip_version</a>(ip_version, \*\*<a href="src/cloudflare/types/radar/as112/top_ip_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/as112/top_ip_version_response.py">TopIPVersionResponse</a></code>
- <code title="get /radar/as112/top/locations">client.radar.as112.top.<a href="./src/cloudflare/resources/radar/as112/top.py">locations</a>(\*\*<a href="src/cloudflare/types/radar/as112/top_locations_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/as112/top_locations_response.py">TopLocationsResponse</a></code>

## ConnectionTampering

Types:

```python
from cloudflare.types.radar import (
    ConnectionTamperingSummaryResponse,
    ConnectionTamperingTimeseriesGroupsResponse,
)
```

Methods:

- <code title="get /radar/connection_tampering/summary">client.radar.connection_tampering.<a href="./src/cloudflare/resources/radar/connection_tampering.py">summary</a>(\*\*<a href="src/cloudflare/types/radar/connection_tampering_summary_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/connection_tampering_summary_response.py">ConnectionTamperingSummaryResponse</a></code>
- <code title="get /radar/connection_tampering/timeseries_groups">client.radar.connection_tampering.<a href="./src/cloudflare/resources/radar/connection_tampering.py">timeseries_groups</a>(\*\*<a href="src/cloudflare/types/radar/connection_tampering_timeseries_groups_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/connection_tampering_timeseries_groups_response.py">ConnectionTamperingTimeseriesGroupsResponse</a></code>

## Email

### Routing

#### Summary

Types:

```python
from cloudflare.types.radar.email.routing import (
    SummaryARCResponse,
    SummaryDKIMResponse,
    SummaryDMARCResponse,
    SummaryEncryptedResponse,
    SummaryIPVersionResponse,
    SummarySPFResponse,
)
```

Methods:

- <code title="get /radar/email/routing/summary/arc">client.radar.email.routing.summary.<a href="./src/cloudflare/resources/radar/email/routing/summary.py">arc</a>(\*\*<a href="src/cloudflare/types/radar/email/routing/summary_arc_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/routing/summary_arc_response.py">SummaryARCResponse</a></code>
- <code title="get /radar/email/routing/summary/dkim">client.radar.email.routing.summary.<a href="./src/cloudflare/resources/radar/email/routing/summary.py">dkim</a>(\*\*<a href="src/cloudflare/types/radar/email/routing/summary_dkim_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/routing/summary_dkim_response.py">SummaryDKIMResponse</a></code>
- <code title="get /radar/email/routing/summary/dmarc">client.radar.email.routing.summary.<a href="./src/cloudflare/resources/radar/email/routing/summary.py">dmarc</a>(\*\*<a href="src/cloudflare/types/radar/email/routing/summary_dmarc_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/routing/summary_dmarc_response.py">SummaryDMARCResponse</a></code>
- <code title="get /radar/email/routing/summary/encrypted">client.radar.email.routing.summary.<a href="./src/cloudflare/resources/radar/email/routing/summary.py">encrypted</a>(\*\*<a href="src/cloudflare/types/radar/email/routing/summary_encrypted_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/routing/summary_encrypted_response.py">SummaryEncryptedResponse</a></code>
- <code title="get /radar/email/routing/summary/ip_version">client.radar.email.routing.summary.<a href="./src/cloudflare/resources/radar/email/routing/summary.py">ip_version</a>(\*\*<a href="src/cloudflare/types/radar/email/routing/summary_ip_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/routing/summary_ip_version_response.py">SummaryIPVersionResponse</a></code>
- <code title="get /radar/email/routing/summary/spf">client.radar.email.routing.summary.<a href="./src/cloudflare/resources/radar/email/routing/summary.py">spf</a>(\*\*<a href="src/cloudflare/types/radar/email/routing/summary_spf_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/routing/summary_spf_response.py">SummarySPFResponse</a></code>

#### TimeseriesGroups

Types:

```python
from cloudflare.types.radar.email.routing import (
    TimeseriesGroupARCResponse,
    TimeseriesGroupDKIMResponse,
    TimeseriesGroupDMARCResponse,
    TimeseriesGroupEncryptedResponse,
    TimeseriesGroupIPVersionResponse,
    TimeseriesGroupSPFResponse,
)
```

Methods:

- <code title="get /radar/email/routing/timeseries_groups/arc">client.radar.email.routing.timeseries_groups.<a href="./src/cloudflare/resources/radar/email/routing/timeseries_groups.py">arc</a>(\*\*<a href="src/cloudflare/types/radar/email/routing/timeseries_group_arc_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/routing/timeseries_group_arc_response.py">TimeseriesGroupARCResponse</a></code>
- <code title="get /radar/email/routing/timeseries_groups/dkim">client.radar.email.routing.timeseries_groups.<a href="./src/cloudflare/resources/radar/email/routing/timeseries_groups.py">dkim</a>(\*\*<a href="src/cloudflare/types/radar/email/routing/timeseries_group_dkim_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/routing/timeseries_group_dkim_response.py">TimeseriesGroupDKIMResponse</a></code>
- <code title="get /radar/email/routing/timeseries_groups/dmarc">client.radar.email.routing.timeseries_groups.<a href="./src/cloudflare/resources/radar/email/routing/timeseries_groups.py">dmarc</a>(\*\*<a href="src/cloudflare/types/radar/email/routing/timeseries_group_dmarc_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/routing/timeseries_group_dmarc_response.py">TimeseriesGroupDMARCResponse</a></code>
- <code title="get /radar/email/routing/timeseries_groups/encrypted">client.radar.email.routing.timeseries_groups.<a href="./src/cloudflare/resources/radar/email/routing/timeseries_groups.py">encrypted</a>(\*\*<a href="src/cloudflare/types/radar/email/routing/timeseries_group_encrypted_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/routing/timeseries_group_encrypted_response.py">TimeseriesGroupEncryptedResponse</a></code>
- <code title="get /radar/email/routing/timeseries_groups/ip_version">client.radar.email.routing.timeseries_groups.<a href="./src/cloudflare/resources/radar/email/routing/timeseries_groups.py">ip_version</a>(\*\*<a href="src/cloudflare/types/radar/email/routing/timeseries_group_ip_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/routing/timeseries_group_ip_version_response.py">TimeseriesGroupIPVersionResponse</a></code>
- <code title="get /radar/email/routing/timeseries_groups/spf">client.radar.email.routing.timeseries_groups.<a href="./src/cloudflare/resources/radar/email/routing/timeseries_groups.py">spf</a>(\*\*<a href="src/cloudflare/types/radar/email/routing/timeseries_group_spf_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/routing/timeseries_group_spf_response.py">TimeseriesGroupSPFResponse</a></code>

### Security

#### Top

##### Tlds

Types:

```python
from cloudflare.types.radar.email.security.top import TldGetResponse
```

Methods:

- <code title="get /radar/email/security/top/tlds">client.radar.email.security.top.tlds.<a href="./src/cloudflare/resources/radar/email/security/top/tlds/tlds.py">get</a>(\*\*<a href="src/cloudflare/types/radar/email/security/top/tld_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/top/tld_get_response.py">TldGetResponse</a></code>

###### Malicious

Types:

```python
from cloudflare.types.radar.email.security.top.tlds import MaliciousGetResponse
```

Methods:

- <code title="get /radar/email/security/top/tlds/malicious/{malicious}">client.radar.email.security.top.tlds.malicious.<a href="./src/cloudflare/resources/radar/email/security/top/tlds/malicious.py">get</a>(malicious, \*\*<a href="src/cloudflare/types/radar/email/security/top/tlds/malicious_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/top/tlds/malicious_get_response.py">MaliciousGetResponse</a></code>

###### Spam

Types:

```python
from cloudflare.types.radar.email.security.top.tlds import SpamGetResponse
```

Methods:

- <code title="get /radar/email/security/top/tlds/spam/{spam}">client.radar.email.security.top.tlds.spam.<a href="./src/cloudflare/resources/radar/email/security/top/tlds/spam.py">get</a>(spam, \*\*<a href="src/cloudflare/types/radar/email/security/top/tlds/spam_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/top/tlds/spam_get_response.py">SpamGetResponse</a></code>

###### Spoof

Types:

```python
from cloudflare.types.radar.email.security.top.tlds import SpoofGetResponse
```

Methods:

- <code title="get /radar/email/security/top/tlds/spoof/{spoof}">client.radar.email.security.top.tlds.spoof.<a href="./src/cloudflare/resources/radar/email/security/top/tlds/spoof.py">get</a>(spoof, \*\*<a href="src/cloudflare/types/radar/email/security/top/tlds/spoof_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/top/tlds/spoof_get_response.py">SpoofGetResponse</a></code>

#### Summary

Types:

```python
from cloudflare.types.radar.email.security import (
    SummaryARCResponse,
    SummaryDKIMResponse,
    SummaryDMARCResponse,
    SummaryMaliciousResponse,
    SummarySpamResponse,
    SummarySPFResponse,
    SummarySpoofResponse,
    SummaryThreatCategoryResponse,
    SummaryTLSVersionResponse,
)
```

Methods:

- <code title="get /radar/email/security/summary/arc">client.radar.email.security.summary.<a href="./src/cloudflare/resources/radar/email/security/summary.py">arc</a>(\*\*<a href="src/cloudflare/types/radar/email/security/summary_arc_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/summary_arc_response.py">SummaryARCResponse</a></code>
- <code title="get /radar/email/security/summary/dkim">client.radar.email.security.summary.<a href="./src/cloudflare/resources/radar/email/security/summary.py">dkim</a>(\*\*<a href="src/cloudflare/types/radar/email/security/summary_dkim_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/summary_dkim_response.py">SummaryDKIMResponse</a></code>
- <code title="get /radar/email/security/summary/dmarc">client.radar.email.security.summary.<a href="./src/cloudflare/resources/radar/email/security/summary.py">dmarc</a>(\*\*<a href="src/cloudflare/types/radar/email/security/summary_dmarc_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/summary_dmarc_response.py">SummaryDMARCResponse</a></code>
- <code title="get /radar/email/security/summary/malicious">client.radar.email.security.summary.<a href="./src/cloudflare/resources/radar/email/security/summary.py">malicious</a>(\*\*<a href="src/cloudflare/types/radar/email/security/summary_malicious_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/summary_malicious_response.py">SummaryMaliciousResponse</a></code>
- <code title="get /radar/email/security/summary/spam">client.radar.email.security.summary.<a href="./src/cloudflare/resources/radar/email/security/summary.py">spam</a>(\*\*<a href="src/cloudflare/types/radar/email/security/summary_spam_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/summary_spam_response.py">SummarySpamResponse</a></code>
- <code title="get /radar/email/security/summary/spf">client.radar.email.security.summary.<a href="./src/cloudflare/resources/radar/email/security/summary.py">spf</a>(\*\*<a href="src/cloudflare/types/radar/email/security/summary_spf_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/summary_spf_response.py">SummarySPFResponse</a></code>
- <code title="get /radar/email/security/summary/spoof">client.radar.email.security.summary.<a href="./src/cloudflare/resources/radar/email/security/summary.py">spoof</a>(\*\*<a href="src/cloudflare/types/radar/email/security/summary_spoof_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/summary_spoof_response.py">SummarySpoofResponse</a></code>
- <code title="get /radar/email/security/summary/threat_category">client.radar.email.security.summary.<a href="./src/cloudflare/resources/radar/email/security/summary.py">threat_category</a>(\*\*<a href="src/cloudflare/types/radar/email/security/summary_threat_category_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/summary_threat_category_response.py">SummaryThreatCategoryResponse</a></code>
- <code title="get /radar/email/security/summary/tls_version">client.radar.email.security.summary.<a href="./src/cloudflare/resources/radar/email/security/summary.py">tls_version</a>(\*\*<a href="src/cloudflare/types/radar/email/security/summary_tls_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/summary_tls_version_response.py">SummaryTLSVersionResponse</a></code>

#### TimeseriesGroups

Types:

```python
from cloudflare.types.radar.email.security import (
    TimeseriesGroupARCResponse,
    TimeseriesGroupDKIMResponse,
    TimeseriesGroupDMARCResponse,
    TimeseriesGroupMaliciousResponse,
    TimeseriesGroupSpamResponse,
    TimeseriesGroupSPFResponse,
    TimeseriesGroupSpoofResponse,
    TimeseriesGroupThreatCategoryResponse,
    TimeseriesGroupTLSVersionResponse,
)
```

Methods:

- <code title="get /radar/email/security/timeseries_groups/arc">client.radar.email.security.timeseries_groups.<a href="./src/cloudflare/resources/radar/email/security/timeseries_groups.py">arc</a>(\*\*<a href="src/cloudflare/types/radar/email/security/timeseries_group_arc_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/timeseries_group_arc_response.py">TimeseriesGroupARCResponse</a></code>
- <code title="get /radar/email/security/timeseries_groups/dkim">client.radar.email.security.timeseries_groups.<a href="./src/cloudflare/resources/radar/email/security/timeseries_groups.py">dkim</a>(\*\*<a href="src/cloudflare/types/radar/email/security/timeseries_group_dkim_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/timeseries_group_dkim_response.py">TimeseriesGroupDKIMResponse</a></code>
- <code title="get /radar/email/security/timeseries_groups/dmarc">client.radar.email.security.timeseries_groups.<a href="./src/cloudflare/resources/radar/email/security/timeseries_groups.py">dmarc</a>(\*\*<a href="src/cloudflare/types/radar/email/security/timeseries_group_dmarc_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/timeseries_group_dmarc_response.py">TimeseriesGroupDMARCResponse</a></code>
- <code title="get /radar/email/security/timeseries_groups/malicious">client.radar.email.security.timeseries_groups.<a href="./src/cloudflare/resources/radar/email/security/timeseries_groups.py">malicious</a>(\*\*<a href="src/cloudflare/types/radar/email/security/timeseries_group_malicious_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/timeseries_group_malicious_response.py">TimeseriesGroupMaliciousResponse</a></code>
- <code title="get /radar/email/security/timeseries_groups/spam">client.radar.email.security.timeseries_groups.<a href="./src/cloudflare/resources/radar/email/security/timeseries_groups.py">spam</a>(\*\*<a href="src/cloudflare/types/radar/email/security/timeseries_group_spam_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/timeseries_group_spam_response.py">TimeseriesGroupSpamResponse</a></code>
- <code title="get /radar/email/security/timeseries_groups/spf">client.radar.email.security.timeseries_groups.<a href="./src/cloudflare/resources/radar/email/security/timeseries_groups.py">spf</a>(\*\*<a href="src/cloudflare/types/radar/email/security/timeseries_group_spf_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/timeseries_group_spf_response.py">TimeseriesGroupSPFResponse</a></code>
- <code title="get /radar/email/security/timeseries_groups/spoof">client.radar.email.security.timeseries_groups.<a href="./src/cloudflare/resources/radar/email/security/timeseries_groups.py">spoof</a>(\*\*<a href="src/cloudflare/types/radar/email/security/timeseries_group_spoof_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/timeseries_group_spoof_response.py">TimeseriesGroupSpoofResponse</a></code>
- <code title="get /radar/email/security/timeseries_groups/threat_category">client.radar.email.security.timeseries_groups.<a href="./src/cloudflare/resources/radar/email/security/timeseries_groups.py">threat_category</a>(\*\*<a href="src/cloudflare/types/radar/email/security/timeseries_group_threat_category_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/timeseries_group_threat_category_response.py">TimeseriesGroupThreatCategoryResponse</a></code>
- <code title="get /radar/email/security/timeseries_groups/tls_version">client.radar.email.security.timeseries_groups.<a href="./src/cloudflare/resources/radar/email/security/timeseries_groups.py">tls_version</a>(\*\*<a href="src/cloudflare/types/radar/email/security/timeseries_group_tls_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/timeseries_group_tls_version_response.py">TimeseriesGroupTLSVersionResponse</a></code>

## Attacks

### Layer3

Types:

```python
from cloudflare.types.radar.attacks import Layer3TimeseriesResponse
```

Methods:

- <code title="get /radar/attacks/layer3/timeseries">client.radar.attacks.layer3.<a href="./src/cloudflare/resources/radar/attacks/layer3/layer3.py">timeseries</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3_timeseries_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3_timeseries_response.py">Layer3TimeseriesResponse</a></code>

#### Summary

Types:

```python
from cloudflare.types.radar.attacks.layer3 import (
    SummaryBitrateResponse,
    SummaryDurationResponse,
    SummaryGetResponse,
    SummaryIPVersionResponse,
    SummaryProtocolResponse,
    SummaryVectorResponse,
)
```

Methods:

- <code title="get /radar/attacks/layer3/summary/bitrate">client.radar.attacks.layer3.summary.<a href="./src/cloudflare/resources/radar/attacks/layer3/summary.py">bitrate</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/summary_bitrate_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/summary_bitrate_response.py">SummaryBitrateResponse</a></code>
- <code title="get /radar/attacks/layer3/summary/duration">client.radar.attacks.layer3.summary.<a href="./src/cloudflare/resources/radar/attacks/layer3/summary.py">duration</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/summary_duration_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/summary_duration_response.py">SummaryDurationResponse</a></code>
- <code title="get /radar/attacks/layer3/summary">client.radar.attacks.layer3.summary.<a href="./src/cloudflare/resources/radar/attacks/layer3/summary.py">get</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/summary_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/summary_get_response.py">SummaryGetResponse</a></code>
- <code title="get /radar/attacks/layer3/summary/ip_version">client.radar.attacks.layer3.summary.<a href="./src/cloudflare/resources/radar/attacks/layer3/summary.py">ip_version</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/summary_ip_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/summary_ip_version_response.py">SummaryIPVersionResponse</a></code>
- <code title="get /radar/attacks/layer3/summary/protocol">client.radar.attacks.layer3.summary.<a href="./src/cloudflare/resources/radar/attacks/layer3/summary.py">protocol</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/summary_protocol_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/summary_protocol_response.py">SummaryProtocolResponse</a></code>
- <code title="get /radar/attacks/layer3/summary/vector">client.radar.attacks.layer3.summary.<a href="./src/cloudflare/resources/radar/attacks/layer3/summary.py">vector</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/summary_vector_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/summary_vector_response.py">SummaryVectorResponse</a></code>

#### TimeseriesGroups

Types:

```python
from cloudflare.types.radar.attacks.layer3 import (
    TimeseriesGroupBitrateResponse,
    TimeseriesGroupDurationResponse,
    TimeseriesGroupGetResponse,
    TimeseriesGroupIndustryResponse,
    TimeseriesGroupIPVersionResponse,
    TimeseriesGroupProtocolResponse,
    TimeseriesGroupVectorResponse,
    TimeseriesGroupVerticalResponse,
)
```

Methods:

- <code title="get /radar/attacks/layer3/timeseries_groups/bitrate">client.radar.attacks.layer3.timeseries_groups.<a href="./src/cloudflare/resources/radar/attacks/layer3/timeseries_groups.py">bitrate</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/timeseries_group_bitrate_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/timeseries_group_bitrate_response.py">TimeseriesGroupBitrateResponse</a></code>
- <code title="get /radar/attacks/layer3/timeseries_groups/duration">client.radar.attacks.layer3.timeseries_groups.<a href="./src/cloudflare/resources/radar/attacks/layer3/timeseries_groups.py">duration</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/timeseries_group_duration_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/timeseries_group_duration_response.py">TimeseriesGroupDurationResponse</a></code>
- <code title="get /radar/attacks/layer3/timeseries_groups">client.radar.attacks.layer3.timeseries_groups.<a href="./src/cloudflare/resources/radar/attacks/layer3/timeseries_groups.py">get</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/timeseries_group_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/timeseries_group_get_response.py">TimeseriesGroupGetResponse</a></code>
- <code title="get /radar/attacks/layer3/timeseries_groups/industry">client.radar.attacks.layer3.timeseries_groups.<a href="./src/cloudflare/resources/radar/attacks/layer3/timeseries_groups.py">industry</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/timeseries_group_industry_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/timeseries_group_industry_response.py">TimeseriesGroupIndustryResponse</a></code>
- <code title="get /radar/attacks/layer3/timeseries_groups/ip_version">client.radar.attacks.layer3.timeseries_groups.<a href="./src/cloudflare/resources/radar/attacks/layer3/timeseries_groups.py">ip_version</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/timeseries_group_ip_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/timeseries_group_ip_version_response.py">TimeseriesGroupIPVersionResponse</a></code>
- <code title="get /radar/attacks/layer3/timeseries_groups/protocol">client.radar.attacks.layer3.timeseries_groups.<a href="./src/cloudflare/resources/radar/attacks/layer3/timeseries_groups.py">protocol</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/timeseries_group_protocol_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/timeseries_group_protocol_response.py">TimeseriesGroupProtocolResponse</a></code>
- <code title="get /radar/attacks/layer3/timeseries_groups/vector">client.radar.attacks.layer3.timeseries_groups.<a href="./src/cloudflare/resources/radar/attacks/layer3/timeseries_groups.py">vector</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/timeseries_group_vector_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/timeseries_group_vector_response.py">TimeseriesGroupVectorResponse</a></code>
- <code title="get /radar/attacks/layer3/timeseries_groups/vertical">client.radar.attacks.layer3.timeseries_groups.<a href="./src/cloudflare/resources/radar/attacks/layer3/timeseries_groups.py">vertical</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/timeseries_group_vertical_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/timeseries_group_vertical_response.py">TimeseriesGroupVerticalResponse</a></code>

#### Top

Types:

```python
from cloudflare.types.radar.attacks.layer3 import (
    TopAttacksResponse,
    TopIndustryResponse,
    TopVerticalResponse,
)
```

Methods:

- <code title="get /radar/attacks/layer3/top/attacks">client.radar.attacks.layer3.top.<a href="./src/cloudflare/resources/radar/attacks/layer3/top/top.py">attacks</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/top_attacks_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/top_attacks_response.py">TopAttacksResponse</a></code>
- <code title="get /radar/attacks/layer3/top/industry">client.radar.attacks.layer3.top.<a href="./src/cloudflare/resources/radar/attacks/layer3/top/top.py">industry</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/top_industry_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/top_industry_response.py">TopIndustryResponse</a></code>
- <code title="get /radar/attacks/layer3/top/vertical">client.radar.attacks.layer3.top.<a href="./src/cloudflare/resources/radar/attacks/layer3/top/top.py">vertical</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/top_vertical_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/top_vertical_response.py">TopVerticalResponse</a></code>

##### Locations

Types:

```python
from cloudflare.types.radar.attacks.layer3.top import LocationOriginResponse, LocationTargetResponse
```

Methods:

- <code title="get /radar/attacks/layer3/top/locations/origin">client.radar.attacks.layer3.top.locations.<a href="./src/cloudflare/resources/radar/attacks/layer3/top/locations.py">origin</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/top/location_origin_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/top/location_origin_response.py">LocationOriginResponse</a></code>
- <code title="get /radar/attacks/layer3/top/locations/target">client.radar.attacks.layer3.top.locations.<a href="./src/cloudflare/resources/radar/attacks/layer3/top/locations.py">target</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/top/location_target_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/top/location_target_response.py">LocationTargetResponse</a></code>

### Layer7

Types:

```python
from cloudflare.types.radar.attacks import Layer7TimeseriesResponse
```

Methods:

- <code title="get /radar/attacks/layer7/timeseries">client.radar.attacks.layer7.<a href="./src/cloudflare/resources/radar/attacks/layer7/layer7.py">timeseries</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7_timeseries_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7_timeseries_response.py">Layer7TimeseriesResponse</a></code>

#### Summary

Types:

```python
from cloudflare.types.radar.attacks.layer7 import (
    SummaryGetResponse,
    SummaryHTTPMethodResponse,
    SummaryHTTPVersionResponse,
    SummaryIPVersionResponse,
    SummaryManagedRulesResponse,
    SummaryMitigationProductResponse,
)
```

Methods:

- <code title="get /radar/attacks/layer7/summary">client.radar.attacks.layer7.summary.<a href="./src/cloudflare/resources/radar/attacks/layer7/summary.py">get</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7/summary_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7/summary_get_response.py">SummaryGetResponse</a></code>
- <code title="get /radar/attacks/layer7/summary/http_method">client.radar.attacks.layer7.summary.<a href="./src/cloudflare/resources/radar/attacks/layer7/summary.py">http_method</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7/summary_http_method_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7/summary_http_method_response.py">SummaryHTTPMethodResponse</a></code>
- <code title="get /radar/attacks/layer7/summary/http_version">client.radar.attacks.layer7.summary.<a href="./src/cloudflare/resources/radar/attacks/layer7/summary.py">http_version</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7/summary_http_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7/summary_http_version_response.py">SummaryHTTPVersionResponse</a></code>
- <code title="get /radar/attacks/layer7/summary/ip_version">client.radar.attacks.layer7.summary.<a href="./src/cloudflare/resources/radar/attacks/layer7/summary.py">ip_version</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7/summary_ip_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7/summary_ip_version_response.py">SummaryIPVersionResponse</a></code>
- <code title="get /radar/attacks/layer7/summary/managed_rules">client.radar.attacks.layer7.summary.<a href="./src/cloudflare/resources/radar/attacks/layer7/summary.py">managed_rules</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7/summary_managed_rules_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7/summary_managed_rules_response.py">SummaryManagedRulesResponse</a></code>
- <code title="get /radar/attacks/layer7/summary/mitigation_product">client.radar.attacks.layer7.summary.<a href="./src/cloudflare/resources/radar/attacks/layer7/summary.py">mitigation_product</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7/summary_mitigation_product_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7/summary_mitigation_product_response.py">SummaryMitigationProductResponse</a></code>

#### TimeseriesGroups

Types:

```python
from cloudflare.types.radar.attacks.layer7 import (
    TimeseriesGroupGetResponse,
    TimeseriesGroupHTTPMethodResponse,
    TimeseriesGroupHTTPVersionResponse,
    TimeseriesGroupIndustryResponse,
    TimeseriesGroupIPVersionResponse,
    TimeseriesGroupManagedRulesResponse,
    TimeseriesGroupMitigationProductResponse,
    TimeseriesGroupVerticalResponse,
)
```

Methods:

- <code title="get /radar/attacks/layer7/timeseries_groups">client.radar.attacks.layer7.timeseries_groups.<a href="./src/cloudflare/resources/radar/attacks/layer7/timeseries_groups.py">get</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7/timeseries_group_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7/timeseries_group_get_response.py">TimeseriesGroupGetResponse</a></code>
- <code title="get /radar/attacks/layer7/timeseries_groups/http_method">client.radar.attacks.layer7.timeseries_groups.<a href="./src/cloudflare/resources/radar/attacks/layer7/timeseries_groups.py">http_method</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7/timeseries_group_http_method_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7/timeseries_group_http_method_response.py">TimeseriesGroupHTTPMethodResponse</a></code>
- <code title="get /radar/attacks/layer7/timeseries_groups/http_version">client.radar.attacks.layer7.timeseries_groups.<a href="./src/cloudflare/resources/radar/attacks/layer7/timeseries_groups.py">http_version</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7/timeseries_group_http_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7/timeseries_group_http_version_response.py">TimeseriesGroupHTTPVersionResponse</a></code>
- <code title="get /radar/attacks/layer7/timeseries_groups/industry">client.radar.attacks.layer7.timeseries_groups.<a href="./src/cloudflare/resources/radar/attacks/layer7/timeseries_groups.py">industry</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7/timeseries_group_industry_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7/timeseries_group_industry_response.py">TimeseriesGroupIndustryResponse</a></code>
- <code title="get /radar/attacks/layer7/timeseries_groups/ip_version">client.radar.attacks.layer7.timeseries_groups.<a href="./src/cloudflare/resources/radar/attacks/layer7/timeseries_groups.py">ip_version</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7/timeseries_group_ip_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7/timeseries_group_ip_version_response.py">TimeseriesGroupIPVersionResponse</a></code>
- <code title="get /radar/attacks/layer7/timeseries_groups/managed_rules">client.radar.attacks.layer7.timeseries_groups.<a href="./src/cloudflare/resources/radar/attacks/layer7/timeseries_groups.py">managed_rules</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7/timeseries_group_managed_rules_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7/timeseries_group_managed_rules_response.py">TimeseriesGroupManagedRulesResponse</a></code>
- <code title="get /radar/attacks/layer7/timeseries_groups/mitigation_product">client.radar.attacks.layer7.timeseries_groups.<a href="./src/cloudflare/resources/radar/attacks/layer7/timeseries_groups.py">mitigation_product</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7/timeseries_group_mitigation_product_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7/timeseries_group_mitigation_product_response.py">TimeseriesGroupMitigationProductResponse</a></code>
- <code title="get /radar/attacks/layer7/timeseries_groups/vertical">client.radar.attacks.layer7.timeseries_groups.<a href="./src/cloudflare/resources/radar/attacks/layer7/timeseries_groups.py">vertical</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7/timeseries_group_vertical_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7/timeseries_group_vertical_response.py">TimeseriesGroupVerticalResponse</a></code>

#### Top

Types:

```python
from cloudflare.types.radar.attacks.layer7 import (
    TopAttacksResponse,
    TopIndustryResponse,
    TopVerticalResponse,
)
```

Methods:

- <code title="get /radar/attacks/layer7/top/attacks">client.radar.attacks.layer7.top.<a href="./src/cloudflare/resources/radar/attacks/layer7/top/top.py">attacks</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7/top_attacks_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7/top_attacks_response.py">TopAttacksResponse</a></code>
- <code title="get /radar/attacks/layer7/top/industry">client.radar.attacks.layer7.top.<a href="./src/cloudflare/resources/radar/attacks/layer7/top/top.py">industry</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7/top_industry_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7/top_industry_response.py">TopIndustryResponse</a></code>
- <code title="get /radar/attacks/layer7/top/vertical">client.radar.attacks.layer7.top.<a href="./src/cloudflare/resources/radar/attacks/layer7/top/top.py">vertical</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7/top_vertical_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7/top_vertical_response.py">TopVerticalResponse</a></code>

##### Locations

Types:

```python
from cloudflare.types.radar.attacks.layer7.top import LocationOriginResponse, LocationTargetResponse
```

Methods:

- <code title="get /radar/attacks/layer7/top/locations/origin">client.radar.attacks.layer7.top.locations.<a href="./src/cloudflare/resources/radar/attacks/layer7/top/locations.py">origin</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7/top/location_origin_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7/top/location_origin_response.py">LocationOriginResponse</a></code>
- <code title="get /radar/attacks/layer7/top/locations/target">client.radar.attacks.layer7.top.locations.<a href="./src/cloudflare/resources/radar/attacks/layer7/top/locations.py">target</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7/top/location_target_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7/top/location_target_response.py">LocationTargetResponse</a></code>

##### Ases

Types:

```python
from cloudflare.types.radar.attacks.layer7.top import AseOriginResponse
```

Methods:

- <code title="get /radar/attacks/layer7/top/ases/origin">client.radar.attacks.layer7.top.ases.<a href="./src/cloudflare/resources/radar/attacks/layer7/top/ases.py">origin</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7/top/ase_origin_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7/top/ase_origin_response.py">AseOriginResponse</a></code>

## Entities

Types:

```python
from cloudflare.types.radar import EntityGetResponse
```

Methods:

- <code title="get /radar/entities/ip">client.radar.entities.<a href="./src/cloudflare/resources/radar/entities/entities.py">get</a>(\*\*<a href="src/cloudflare/types/radar/entity_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/entity_get_response.py">EntityGetResponse</a></code>

### ASNs

Types:

```python
from cloudflare.types.radar.entities import (
    ASNListResponse,
    ASNGetResponse,
    ASNIPResponse,
    ASNRelResponse,
)
```

Methods:

- <code title="get /radar/entities/asns">client.radar.entities.asns.<a href="./src/cloudflare/resources/radar/entities/asns.py">list</a>(\*\*<a href="src/cloudflare/types/radar/entities/asn_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/entities/asn_list_response.py">ASNListResponse</a></code>
- <code title="get /radar/entities/asns/{asn}">client.radar.entities.asns.<a href="./src/cloudflare/resources/radar/entities/asns.py">get</a>(asn, \*\*<a href="src/cloudflare/types/radar/entities/asn_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/entities/asn_get_response.py">ASNGetResponse</a></code>
- <code title="get /radar/entities/asns/ip">client.radar.entities.asns.<a href="./src/cloudflare/resources/radar/entities/asns.py">ip</a>(\*\*<a href="src/cloudflare/types/radar/entities/asn_ip_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/entities/asn_ip_response.py">ASNIPResponse</a></code>
- <code title="get /radar/entities/asns/{asn}/rel">client.radar.entities.asns.<a href="./src/cloudflare/resources/radar/entities/asns.py">rel</a>(asn, \*\*<a href="src/cloudflare/types/radar/entities/asn_rel_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/entities/asn_rel_response.py">ASNRelResponse</a></code>

### Locations

Types:

```python
from cloudflare.types.radar.entities import LocationListResponse, LocationGetResponse
```

Methods:

- <code title="get /radar/entities/locations">client.radar.entities.locations.<a href="./src/cloudflare/resources/radar/entities/locations.py">list</a>(\*\*<a href="src/cloudflare/types/radar/entities/location_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/entities/location_list_response.py">LocationListResponse</a></code>
- <code title="get /radar/entities/locations/{location}">client.radar.entities.locations.<a href="./src/cloudflare/resources/radar/entities/locations.py">get</a>(location, \*\*<a href="src/cloudflare/types/radar/entities/location_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/entities/location_get_response.py">LocationGetResponse</a></code>

## HTTP

### Top

Types:

```python
from cloudflare.types.radar.http import TopBrowserFamiliesResponse, TopBrowsersResponse
```

Methods:

- <code title="get /radar/http/top/browser_families">client.radar.http.top.<a href="./src/cloudflare/resources/radar/http/top.py">browser_families</a>(\*\*<a href="src/cloudflare/types/radar/http/top_browser_families_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/top_browser_families_response.py">TopBrowserFamiliesResponse</a></code>
- <code title="get /radar/http/top/browsers">client.radar.http.top.<a href="./src/cloudflare/resources/radar/http/top.py">browsers</a>(\*\*<a href="src/cloudflare/types/radar/http/top_browsers_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/top_browsers_response.py">TopBrowsersResponse</a></code>

### Locations

Types:

```python
from cloudflare.types.radar.http import LocationGetResponse
```

Methods:

- <code title="get /radar/http/top/locations">client.radar.http.locations.<a href="./src/cloudflare/resources/radar/http/locations/locations.py">get</a>(\*\*<a href="src/cloudflare/types/radar/http/location_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/location_get_response.py">LocationGetResponse</a></code>

#### BotClass

Types:

```python
from cloudflare.types.radar.http.locations import BotClassGetResponse
```

Methods:

- <code title="get /radar/http/top/locations/bot_class/{bot_class}">client.radar.http.locations.bot_class.<a href="./src/cloudflare/resources/radar/http/locations/bot_class.py">get</a>(bot_class, \*\*<a href="src/cloudflare/types/radar/http/locations/bot_class_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/locations/bot_class_get_response.py">BotClassGetResponse</a></code>

#### DeviceType

Types:

```python
from cloudflare.types.radar.http.locations import DeviceTypeGetResponse
```

Methods:

- <code title="get /radar/http/top/locations/device_type/{device_type}">client.radar.http.locations.device_type.<a href="./src/cloudflare/resources/radar/http/locations/device_type.py">get</a>(device_type, \*\*<a href="src/cloudflare/types/radar/http/locations/device_type_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/locations/device_type_get_response.py">DeviceTypeGetResponse</a></code>

#### HTTPProtocol

Types:

```python
from cloudflare.types.radar.http.locations import HTTPProtocolGetResponse
```

Methods:

- <code title="get /radar/http/top/locations/http_protocol/{http_protocol}">client.radar.http.locations.http_protocol.<a href="./src/cloudflare/resources/radar/http/locations/http_protocol.py">get</a>(http_protocol, \*\*<a href="src/cloudflare/types/radar/http/locations/http_protocol_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/locations/http_protocol_get_response.py">HTTPProtocolGetResponse</a></code>

#### HTTPMethod

Types:

```python
from cloudflare.types.radar.http.locations import HTTPMethodGetResponse
```

Methods:

- <code title="get /radar/http/top/locations/http_version/{http_version}">client.radar.http.locations.http_method.<a href="./src/cloudflare/resources/radar/http/locations/http_method.py">get</a>(http_version, \*\*<a href="src/cloudflare/types/radar/http/locations/http_method_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/locations/http_method_get_response.py">HTTPMethodGetResponse</a></code>

#### IPVersion

Types:

```python
from cloudflare.types.radar.http.locations import IPVersionGetResponse
```

Methods:

- <code title="get /radar/http/top/locations/ip_version/{ip_version}">client.radar.http.locations.ip_version.<a href="./src/cloudflare/resources/radar/http/locations/ip_version.py">get</a>(ip_version, \*\*<a href="src/cloudflare/types/radar/http/locations/ip_version_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/locations/ip_version_get_response.py">IPVersionGetResponse</a></code>

#### OS

Types:

```python
from cloudflare.types.radar.http.locations import OSGetResponse
```

Methods:

- <code title="get /radar/http/top/locations/os/{os}">client.radar.http.locations.os.<a href="./src/cloudflare/resources/radar/http/locations/os.py">get</a>(os, \*\*<a href="src/cloudflare/types/radar/http/locations/os_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/locations/os_get_response.py">OSGetResponse</a></code>

#### TLSVersion

Types:

```python
from cloudflare.types.radar.http.locations import TLSVersionGetResponse
```

Methods:

- <code title="get /radar/http/top/locations/tls_version/{tls_version}">client.radar.http.locations.tls_version.<a href="./src/cloudflare/resources/radar/http/locations/tls_version.py">get</a>(tls_version, \*\*<a href="src/cloudflare/types/radar/http/locations/tls_version_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/locations/tls_version_get_response.py">TLSVersionGetResponse</a></code>

### Ases

Types:

```python
from cloudflare.types.radar.http import AseGetResponse
```

Methods:

- <code title="get /radar/http/top/ases">client.radar.http.ases.<a href="./src/cloudflare/resources/radar/http/ases/ases.py">get</a>(\*\*<a href="src/cloudflare/types/radar/http/ase_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/ase_get_response.py">AseGetResponse</a></code>

#### BotClass

Types:

```python
from cloudflare.types.radar.http.ases import BotClassGetResponse
```

Methods:

- <code title="get /radar/http/top/ases/bot_class/{bot_class}">client.radar.http.ases.bot_class.<a href="./src/cloudflare/resources/radar/http/ases/bot_class.py">get</a>(bot_class, \*\*<a href="src/cloudflare/types/radar/http/ases/bot_class_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/ases/bot_class_get_response.py">BotClassGetResponse</a></code>

#### DeviceType

Types:

```python
from cloudflare.types.radar.http.ases import DeviceTypeGetResponse
```

Methods:

- <code title="get /radar/http/top/ases/device_type/{device_type}">client.radar.http.ases.device_type.<a href="./src/cloudflare/resources/radar/http/ases/device_type.py">get</a>(device_type, \*\*<a href="src/cloudflare/types/radar/http/ases/device_type_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/ases/device_type_get_response.py">DeviceTypeGetResponse</a></code>

#### HTTPProtocol

Types:

```python
from cloudflare.types.radar.http.ases import HTTPProtocolGetResponse
```

Methods:

- <code title="get /radar/http/top/ases/http_protocol/{http_protocol}">client.radar.http.ases.http_protocol.<a href="./src/cloudflare/resources/radar/http/ases/http_protocol.py">get</a>(http_protocol, \*\*<a href="src/cloudflare/types/radar/http/ases/http_protocol_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/ases/http_protocol_get_response.py">HTTPProtocolGetResponse</a></code>

#### HTTPMethod

Types:

```python
from cloudflare.types.radar.http.ases import HTTPMethodGetResponse
```

Methods:

- <code title="get /radar/http/top/ases/http_version/{http_version}">client.radar.http.ases.http_method.<a href="./src/cloudflare/resources/radar/http/ases/http_method.py">get</a>(http_version, \*\*<a href="src/cloudflare/types/radar/http/ases/http_method_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/ases/http_method_get_response.py">HTTPMethodGetResponse</a></code>

#### IPVersion

Types:

```python
from cloudflare.types.radar.http.ases import IPVersionGetResponse
```

Methods:

- <code title="get /radar/http/top/ases/ip_version/{ip_version}">client.radar.http.ases.ip_version.<a href="./src/cloudflare/resources/radar/http/ases/ip_version.py">get</a>(ip_version, \*\*<a href="src/cloudflare/types/radar/http/ases/ip_version_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/ases/ip_version_get_response.py">IPVersionGetResponse</a></code>

#### OS

Types:

```python
from cloudflare.types.radar.http.ases import OSGetResponse
```

Methods:

- <code title="get /radar/http/top/ases/os/{os}">client.radar.http.ases.os.<a href="./src/cloudflare/resources/radar/http/ases/os.py">get</a>(os, \*\*<a href="src/cloudflare/types/radar/http/ases/os_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/ases/os_get_response.py">OSGetResponse</a></code>

#### TLSVersion

Types:

```python
from cloudflare.types.radar.http.ases import TLSVersionGetResponse
```

Methods:

- <code title="get /radar/http/top/ases/tls_version/{tls_version}">client.radar.http.ases.tls_version.<a href="./src/cloudflare/resources/radar/http/ases/tls_version.py">get</a>(tls_version, \*\*<a href="src/cloudflare/types/radar/http/ases/tls_version_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/ases/tls_version_get_response.py">TLSVersionGetResponse</a></code>

### Summary

Types:

```python
from cloudflare.types.radar.http import (
    SummaryBotClassResponse,
    SummaryDeviceTypeResponse,
    SummaryHTTPProtocolResponse,
    SummaryHTTPVersionResponse,
    SummaryIPVersionResponse,
    SummaryOSResponse,
    SummaryTLSVersionResponse,
)
```

Methods:

- <code title="get /radar/http/summary/bot_class">client.radar.http.summary.<a href="./src/cloudflare/resources/radar/http/summary.py">bot_class</a>(\*\*<a href="src/cloudflare/types/radar/http/summary_bot_class_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/summary_bot_class_response.py">SummaryBotClassResponse</a></code>
- <code title="get /radar/http/summary/device_type">client.radar.http.summary.<a href="./src/cloudflare/resources/radar/http/summary.py">device_type</a>(\*\*<a href="src/cloudflare/types/radar/http/summary_device_type_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/summary_device_type_response.py">SummaryDeviceTypeResponse</a></code>
- <code title="get /radar/http/summary/http_protocol">client.radar.http.summary.<a href="./src/cloudflare/resources/radar/http/summary.py">http_protocol</a>(\*\*<a href="src/cloudflare/types/radar/http/summary_http_protocol_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/summary_http_protocol_response.py">SummaryHTTPProtocolResponse</a></code>
- <code title="get /radar/http/summary/http_version">client.radar.http.summary.<a href="./src/cloudflare/resources/radar/http/summary.py">http_version</a>(\*\*<a href="src/cloudflare/types/radar/http/summary_http_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/summary_http_version_response.py">SummaryHTTPVersionResponse</a></code>
- <code title="get /radar/http/summary/ip_version">client.radar.http.summary.<a href="./src/cloudflare/resources/radar/http/summary.py">ip_version</a>(\*\*<a href="src/cloudflare/types/radar/http/summary_ip_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/summary_ip_version_response.py">SummaryIPVersionResponse</a></code>
- <code title="get /radar/http/summary/os">client.radar.http.summary.<a href="./src/cloudflare/resources/radar/http/summary.py">os</a>(\*\*<a href="src/cloudflare/types/radar/http/summary_os_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/summary_os_response.py">SummaryOSResponse</a></code>
- <code title="get /radar/http/summary/tls_version">client.radar.http.summary.<a href="./src/cloudflare/resources/radar/http/summary.py">tls_version</a>(\*\*<a href="src/cloudflare/types/radar/http/summary_tls_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/summary_tls_version_response.py">SummaryTLSVersionResponse</a></code>

### TimeseriesGroups

Types:

```python
from cloudflare.types.radar.http import (
    TimeseriesGroupBotClassResponse,
    TimeseriesGroupBrowserResponse,
    TimeseriesGroupBrowserFamilyResponse,
    TimeseriesGroupDeviceTypeResponse,
    TimeseriesGroupHTTPProtocolResponse,
    TimeseriesGroupHTTPVersionResponse,
    TimeseriesGroupIPVersionResponse,
    TimeseriesGroupOSResponse,
    TimeseriesGroupTLSVersionResponse,
)
```

Methods:

- <code title="get /radar/http/timeseries_groups/bot_class">client.radar.http.timeseries_groups.<a href="./src/cloudflare/resources/radar/http/timeseries_groups.py">bot_class</a>(\*\*<a href="src/cloudflare/types/radar/http/timeseries_group_bot_class_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/timeseries_group_bot_class_response.py">TimeseriesGroupBotClassResponse</a></code>
- <code title="get /radar/http/timeseries_groups/browser">client.radar.http.timeseries_groups.<a href="./src/cloudflare/resources/radar/http/timeseries_groups.py">browser</a>(\*\*<a href="src/cloudflare/types/radar/http/timeseries_group_browser_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/timeseries_group_browser_response.py">TimeseriesGroupBrowserResponse</a></code>
- <code title="get /radar/http/timeseries_groups/browser_family">client.radar.http.timeseries_groups.<a href="./src/cloudflare/resources/radar/http/timeseries_groups.py">browser_family</a>(\*\*<a href="src/cloudflare/types/radar/http/timeseries_group_browser_family_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/timeseries_group_browser_family_response.py">TimeseriesGroupBrowserFamilyResponse</a></code>
- <code title="get /radar/http/timeseries_groups/device_type">client.radar.http.timeseries_groups.<a href="./src/cloudflare/resources/radar/http/timeseries_groups.py">device_type</a>(\*\*<a href="src/cloudflare/types/radar/http/timeseries_group_device_type_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/timeseries_group_device_type_response.py">TimeseriesGroupDeviceTypeResponse</a></code>
- <code title="get /radar/http/timeseries_groups/http_protocol">client.radar.http.timeseries_groups.<a href="./src/cloudflare/resources/radar/http/timeseries_groups.py">http_protocol</a>(\*\*<a href="src/cloudflare/types/radar/http/timeseries_group_http_protocol_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/timeseries_group_http_protocol_response.py">TimeseriesGroupHTTPProtocolResponse</a></code>
- <code title="get /radar/http/timeseries_groups/http_version">client.radar.http.timeseries_groups.<a href="./src/cloudflare/resources/radar/http/timeseries_groups.py">http_version</a>(\*\*<a href="src/cloudflare/types/radar/http/timeseries_group_http_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/timeseries_group_http_version_response.py">TimeseriesGroupHTTPVersionResponse</a></code>
- <code title="get /radar/http/timeseries_groups/ip_version">client.radar.http.timeseries_groups.<a href="./src/cloudflare/resources/radar/http/timeseries_groups.py">ip_version</a>(\*\*<a href="src/cloudflare/types/radar/http/timeseries_group_ip_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/timeseries_group_ip_version_response.py">TimeseriesGroupIPVersionResponse</a></code>
- <code title="get /radar/http/timeseries_groups/os">client.radar.http.timeseries_groups.<a href="./src/cloudflare/resources/radar/http/timeseries_groups.py">os</a>(\*\*<a href="src/cloudflare/types/radar/http/timeseries_group_os_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/timeseries_group_os_response.py">TimeseriesGroupOSResponse</a></code>
- <code title="get /radar/http/timeseries_groups/tls_version">client.radar.http.timeseries_groups.<a href="./src/cloudflare/resources/radar/http/timeseries_groups.py">tls_version</a>(\*\*<a href="src/cloudflare/types/radar/http/timeseries_group_tls_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/timeseries_group_tls_version_response.py">TimeseriesGroupTLSVersionResponse</a></code>

## Quality

### IQI

Types:

```python
from cloudflare.types.radar.quality import IQISummaryResponse, IQITimeseriesGroupsResponse
```

Methods:

- <code title="get /radar/quality/iqi/summary">client.radar.quality.iqi.<a href="./src/cloudflare/resources/radar/quality/iqi.py">summary</a>(\*\*<a href="src/cloudflare/types/radar/quality/iqi_summary_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/quality/iqi_summary_response.py">IQISummaryResponse</a></code>
- <code title="get /radar/quality/iqi/timeseries_groups">client.radar.quality.iqi.<a href="./src/cloudflare/resources/radar/quality/iqi.py">timeseries_groups</a>(\*\*<a href="src/cloudflare/types/radar/quality/iqi_timeseries_groups_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/quality/iqi_timeseries_groups_response.py">IQITimeseriesGroupsResponse</a></code>

### Speed

Types:

```python
from cloudflare.types.radar.quality import SpeedHistogramResponse, SpeedSummaryResponse
```

Methods:

- <code title="get /radar/quality/speed/histogram">client.radar.quality.speed.<a href="./src/cloudflare/resources/radar/quality/speed/speed.py">histogram</a>(\*\*<a href="src/cloudflare/types/radar/quality/speed_histogram_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/quality/speed_histogram_response.py">SpeedHistogramResponse</a></code>
- <code title="get /radar/quality/speed/summary">client.radar.quality.speed.<a href="./src/cloudflare/resources/radar/quality/speed/speed.py">summary</a>(\*\*<a href="src/cloudflare/types/radar/quality/speed_summary_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/quality/speed_summary_response.py">SpeedSummaryResponse</a></code>

#### Top

Types:

```python
from cloudflare.types.radar.quality.speed import TopAsesResponse, TopLocationsResponse
```

Methods:

- <code title="get /radar/quality/speed/top/ases">client.radar.quality.speed.top.<a href="./src/cloudflare/resources/radar/quality/speed/top.py">ases</a>(\*\*<a href="src/cloudflare/types/radar/quality/speed/top_ases_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/quality/speed/top_ases_response.py">TopAsesResponse</a></code>
- <code title="get /radar/quality/speed/top/locations">client.radar.quality.speed.top.<a href="./src/cloudflare/resources/radar/quality/speed/top.py">locations</a>(\*\*<a href="src/cloudflare/types/radar/quality/speed/top_locations_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/quality/speed/top_locations_response.py">TopLocationsResponse</a></code>

## Ranking

Types:

```python
from cloudflare.types.radar import RankingTimeseriesGroupsResponse, RankingTopResponse
```

Methods:

- <code title="get /radar/ranking/timeseries_groups">client.radar.ranking.<a href="./src/cloudflare/resources/radar/ranking/ranking.py">timeseries_groups</a>(\*\*<a href="src/cloudflare/types/radar/ranking_timeseries_groups_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/ranking_timeseries_groups_response.py">RankingTimeseriesGroupsResponse</a></code>
- <code title="get /radar/ranking/top">client.radar.ranking.<a href="./src/cloudflare/resources/radar/ranking/ranking.py">top</a>(\*\*<a href="src/cloudflare/types/radar/ranking_top_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/ranking_top_response.py">RankingTopResponse</a></code>

### Domain

Types:

```python
from cloudflare.types.radar.ranking import DomainGetResponse
```

Methods:

- <code title="get /radar/ranking/domain/{domain}">client.radar.ranking.domain.<a href="./src/cloudflare/resources/radar/ranking/domain.py">get</a>(domain, \*\*<a href="src/cloudflare/types/radar/ranking/domain_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/ranking/domain_get_response.py">DomainGetResponse</a></code>

## TrafficAnomalies

Types:

```python
from cloudflare.types.radar import TrafficAnomalyGetResponse
```

Methods:

- <code title="get /radar/traffic_anomalies">client.radar.traffic_anomalies.<a href="./src/cloudflare/resources/radar/traffic_anomalies/traffic_anomalies.py">get</a>(\*\*<a href="src/cloudflare/types/radar/traffic_anomaly_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/traffic_anomaly_get_response.py">TrafficAnomalyGetResponse</a></code>

### Locations

Types:

```python
from cloudflare.types.radar.traffic_anomalies import LocationGetResponse
```

Methods:

- <code title="get /radar/traffic_anomalies/locations">client.radar.traffic_anomalies.locations.<a href="./src/cloudflare/resources/radar/traffic_anomalies/locations.py">get</a>(\*\*<a href="src/cloudflare/types/radar/traffic_anomalies/location_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/traffic_anomalies/location_get_response.py">LocationGetResponse</a></code>

# BotManagement

Types:

```python
from cloudflare.types import BotManagementUpdateResponse, BotManagementGetResponse
```

Methods:

- <code title="put /zones/{zone_id}/bot_management">client.bot_management.<a href="./src/cloudflare/resources/bot_management.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/bot_management_update_params.py">params</a>) -> <a href="./src/cloudflare/types/bot_management_update_response.py">BotManagementUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/bot_management">client.bot_management.<a href="./src/cloudflare/resources/bot_management.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/bot_management_get_response.py">BotManagementGetResponse</a></code>

# OriginPostQuantumEncryption

Types:

```python
from cloudflare.types import (
    OriginPostQuantumEncryptionUpdateResponse,
    OriginPostQuantumEncryptionGetResponse,
)
```

Methods:

- <code title="put /zones/{zone_id}/cache/origin_post_quantum_encryption">client.origin_post_quantum_encryption.<a href="./src/cloudflare/resources/origin_post_quantum_encryption.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/origin_post_quantum_encryption_update_params.py">params</a>) -> <a href="./src/cloudflare/types/origin_post_quantum_encryption_update_response.py">OriginPostQuantumEncryptionUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/cache/origin_post_quantum_encryption">client.origin_post_quantum_encryption.<a href="./src/cloudflare/resources/origin_post_quantum_encryption.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/origin_post_quantum_encryption_get_response.py">OriginPostQuantumEncryptionGetResponse</a></code>

# Speed

Types:

```python
from cloudflare.types import SpeedDeleteResponse, SpeedScheduleGetResponse, SpeedTrendsListResponse
```

Methods:

- <code title="delete /zones/{zone_id}/speed_api/schedule/{url}">client.speed.<a href="./src/cloudflare/resources/speed/speed.py">delete</a>(url, \*, zone_id, \*\*<a href="src/cloudflare/types/speed_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/speed_delete_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/speed_api/schedule/{url}">client.speed.<a href="./src/cloudflare/resources/speed/speed.py">schedule_get</a>(url, \*, zone_id, \*\*<a href="src/cloudflare/types/speed_schedule_get_params.py">params</a>) -> <a href="./src/cloudflare/types/speed_schedule_get_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/speed_api/pages/{url}/trend">client.speed.<a href="./src/cloudflare/resources/speed/speed.py">trends_list</a>(url, \*, zone_id, \*\*<a href="src/cloudflare/types/speed_trends_list_params.py">params</a>) -> <a href="./src/cloudflare/types/speed_trends_list_response.py">Optional</a></code>

## Tests

Types:

```python
from cloudflare.types.speed import (
    TestCreateResponse,
    TestListResponse,
    TestDeleteResponse,
    TestGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/speed_api/pages/{url}/tests">client.speed.tests.<a href="./src/cloudflare/resources/speed/tests.py">create</a>(url, \*, zone_id, \*\*<a href="src/cloudflare/types/speed/test_create_params.py">params</a>) -> <a href="./src/cloudflare/types/speed/test_create_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/speed_api/pages/{url}/tests">client.speed.tests.<a href="./src/cloudflare/resources/speed/tests.py">list</a>(url, \*, zone_id, \*\*<a href="src/cloudflare/types/speed/test_list_params.py">params</a>) -> <a href="./src/cloudflare/types/speed/test_list_response.py">TestListResponse</a></code>
- <code title="delete /zones/{zone_id}/speed_api/pages/{url}/tests">client.speed.tests.<a href="./src/cloudflare/resources/speed/tests.py">delete</a>(url, \*, zone_id, \*\*<a href="src/cloudflare/types/speed/test_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/speed/test_delete_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/speed_api/pages/{url}/tests/{test_id}">client.speed.tests.<a href="./src/cloudflare/resources/speed/tests.py">get</a>(test_id, \*, zone_id, url) -> <a href="./src/cloudflare/types/speed/test_get_response.py">Optional</a></code>

## Schedule

Types:

```python
from cloudflare.types.speed import ScheduleCreateResponse
```

Methods:

- <code title="post /zones/{zone_id}/speed_api/schedule/{url}">client.speed.schedule.<a href="./src/cloudflare/resources/speed/schedule.py">create</a>(url, \*, zone_id, \*\*<a href="src/cloudflare/types/speed/schedule_create_params.py">params</a>) -> <a href="./src/cloudflare/types/speed/schedule_create_response.py">Optional</a></code>

## Availabilities

Types:

```python
from cloudflare.types.speed import AvailabilityListResponse
```

Methods:

- <code title="get /zones/{zone_id}/speed_api/availabilities">client.speed.availabilities.<a href="./src/cloudflare/resources/speed/availabilities.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/speed/availability_list_response.py">Optional</a></code>

## Pages

Types:

```python
from cloudflare.types.speed import PageListResponse
```

Methods:

- <code title="get /zones/{zone_id}/speed_api/pages">client.speed.pages.<a href="./src/cloudflare/resources/speed/pages.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/speed/page_list_response.py">Optional</a></code>

# DCVDelegation

## UUID

Types:

```python
from cloudflare.types.dcv_delegation import UUIDGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/dcv_delegation/uuid">client.dcv_delegation.uuid.<a href="./src/cloudflare/resources/dcv_delegation/uuid.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/dcv_delegation/uuid_get_response.py">UUIDGetResponse</a></code>

# Hostnames

## Settings

### TLS

Types:

```python
from cloudflare.types.hostnames.settings import TLSUpdateResponse, TLSDeleteResponse, TLSGetResponse
```

Methods:

- <code title="put /zones/{zone_id}/hostnames/settings/{setting_id}/{hostname}">client.hostnames.settings.tls.<a href="./src/cloudflare/resources/hostnames/settings/tls.py">update</a>(hostname, \*, zone_id, setting_id, \*\*<a href="src/cloudflare/types/hostnames/settings/tls_update_params.py">params</a>) -> <a href="./src/cloudflare/types/hostnames/settings/tls_update_response.py">TLSUpdateResponse</a></code>
- <code title="delete /zones/{zone_id}/hostnames/settings/{setting_id}/{hostname}">client.hostnames.settings.tls.<a href="./src/cloudflare/resources/hostnames/settings/tls.py">delete</a>(hostname, \*, zone_id, setting_id) -> <a href="./src/cloudflare/types/hostnames/settings/tls_delete_response.py">TLSDeleteResponse</a></code>
- <code title="get /zones/{zone_id}/hostnames/settings/{setting_id}">client.hostnames.settings.tls.<a href="./src/cloudflare/resources/hostnames/settings/tls.py">get</a>(setting_id, \*, zone_id) -> <a href="./src/cloudflare/types/hostnames/settings/tls_get_response.py">Optional</a></code>

# Snippets

Types:

```python
from cloudflare.types import (
    SnippetUpdateResponse,
    SnippetListResponse,
    SnippetDeleteResponse,
    SnippetGetResponse,
)
```

Methods:

- <code title="put /zones/{zone_identifier}/snippets/{snippet_name}">client.snippets.<a href="./src/cloudflare/resources/snippets/snippets.py">update</a>(snippet_name, \*, zone_identifier, \*\*<a href="src/cloudflare/types/snippet_update_params.py">params</a>) -> <a href="./src/cloudflare/types/snippet_update_response.py">SnippetUpdateResponse</a></code>
- <code title="get /zones/{zone_identifier}/snippets">client.snippets.<a href="./src/cloudflare/resources/snippets/snippets.py">list</a>(zone_identifier) -> <a href="./src/cloudflare/types/snippet_list_response.py">SnippetListResponse</a></code>
- <code title="delete /zones/{zone_identifier}/snippets/{snippet_name}">client.snippets.<a href="./src/cloudflare/resources/snippets/snippets.py">delete</a>(snippet_name, \*, zone_identifier) -> <a href="./src/cloudflare/types/snippet_delete_response.py">SnippetDeleteResponse</a></code>
- <code title="get /zones/{zone_identifier}/snippets/{snippet_name}">client.snippets.<a href="./src/cloudflare/resources/snippets/snippets.py">get</a>(snippet_name, \*, zone_identifier) -> <a href="./src/cloudflare/types/snippet_get_response.py">SnippetGetResponse</a></code>

## Content

Methods:

- <code title="get /zones/{zone_identifier}/snippets/{snippet_name}/content">client.snippets.content.<a href="./src/cloudflare/resources/snippets/content.py">get</a>(snippet_name, \*, zone_identifier) -> BinaryAPIResponse</code>

## Rules

Types:

```python
from cloudflare.types.snippets import RuleUpdateResponse, RuleListResponse
```

Methods:

- <code title="put /zones/{zone_identifier}/snippets/snippet_rules">client.snippets.rules.<a href="./src/cloudflare/resources/snippets/rules.py">update</a>(zone_identifier, \*\*<a href="src/cloudflare/types/snippets/rule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/snippets/rule_update_response.py">RuleUpdateResponse</a></code>
- <code title="get /zones/{zone_identifier}/snippets/snippet_rules">client.snippets.rules.<a href="./src/cloudflare/resources/snippets/rules.py">list</a>(zone_identifier) -> <a href="./src/cloudflare/types/snippets/rule_list_response.py">RuleListResponse</a></code>

# Calls

Types:

```python
from cloudflare.types import (
    CallCreateResponse,
    CallUpdateResponse,
    CallListResponse,
    CallDeleteResponse,
    CallGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/calls/apps">client.calls.<a href="./src/cloudflare/resources/calls.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/call_create_params.py">params</a>) -> <a href="./src/cloudflare/types/call_create_response.py">CallCreateResponse</a></code>
- <code title="put /accounts/{account_id}/calls/apps/{app_id}">client.calls.<a href="./src/cloudflare/resources/calls.py">update</a>(app_id, \*, account_id, \*\*<a href="src/cloudflare/types/call_update_params.py">params</a>) -> <a href="./src/cloudflare/types/call_update_response.py">CallUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/calls/apps">client.calls.<a href="./src/cloudflare/resources/calls.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/call_list_response.py">CallListResponse</a></code>
- <code title="delete /accounts/{account_id}/calls/apps/{app_id}">client.calls.<a href="./src/cloudflare/resources/calls.py">delete</a>(app_id, \*, account_id) -> <a href="./src/cloudflare/types/call_delete_response.py">CallDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/calls/apps/{app_id}">client.calls.<a href="./src/cloudflare/resources/calls.py">get</a>(app_id, \*, account_id) -> <a href="./src/cloudflare/types/call_get_response.py">CallGetResponse</a></code>

# CloudforceOne

## Requests

Types:

```python
from cloudflare.types.cloudforce_one import (
    RequestCreateResponse,
    RequestUpdateResponse,
    RequestListResponse,
    RequestDeleteResponse,
    RequestConstantsResponse,
    RequestGetResponse,
    RequestQuotaResponse,
    RequestTypesResponse,
)
```

Methods:

- <code title="post /accounts/{account_identifier}/cloudforce-one/requests/new">client.cloudforce_one.requests.<a href="./src/cloudflare/resources/cloudforce_one/requests/requests.py">create</a>(account_identifier, \*\*<a href="src/cloudflare/types/cloudforce_one/request_create_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/request_create_response.py">RequestCreateResponse</a></code>
- <code title="put /accounts/{account_identifier}/cloudforce-one/requests/{request_identifier}">client.cloudforce_one.requests.<a href="./src/cloudflare/resources/cloudforce_one/requests/requests.py">update</a>(request_identifier, \*, account_identifier, \*\*<a href="src/cloudflare/types/cloudforce_one/request_update_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/request_update_response.py">RequestUpdateResponse</a></code>
- <code title="post /accounts/{account_identifier}/cloudforce-one/requests">client.cloudforce_one.requests.<a href="./src/cloudflare/resources/cloudforce_one/requests/requests.py">list</a>(account_identifier, \*\*<a href="src/cloudflare/types/cloudforce_one/request_list_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/request_list_response.py">SyncV4PagePaginationArray[RequestListResponse]</a></code>
- <code title="delete /accounts/{account_identifier}/cloudforce-one/requests/{request_identifier}">client.cloudforce_one.requests.<a href="./src/cloudflare/resources/cloudforce_one/requests/requests.py">delete</a>(request_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/cloudforce_one/request_delete_response.py">RequestDeleteResponse</a></code>
- <code title="get /accounts/{account_identifier}/cloudforce-one/requests/constants">client.cloudforce_one.requests.<a href="./src/cloudflare/resources/cloudforce_one/requests/requests.py">constants</a>(account_identifier) -> <a href="./src/cloudflare/types/cloudforce_one/request_constants_response.py">RequestConstantsResponse</a></code>
- <code title="get /accounts/{account_identifier}/cloudforce-one/requests/{request_identifier}">client.cloudforce_one.requests.<a href="./src/cloudflare/resources/cloudforce_one/requests/requests.py">get</a>(request_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/cloudforce_one/request_get_response.py">RequestGetResponse</a></code>
- <code title="get /accounts/{account_identifier}/cloudforce-one/requests/quota">client.cloudforce_one.requests.<a href="./src/cloudflare/resources/cloudforce_one/requests/requests.py">quota</a>(account_identifier) -> <a href="./src/cloudflare/types/cloudforce_one/request_quota_response.py">RequestQuotaResponse</a></code>
- <code title="get /accounts/{account_identifier}/cloudforce-one/requests/types">client.cloudforce_one.requests.<a href="./src/cloudflare/resources/cloudforce_one/requests/requests.py">types</a>(account_identifier) -> <a href="./src/cloudflare/types/cloudforce_one/request_types_response.py">RequestTypesResponse</a></code>

### Message

Types:

```python
from cloudflare.types.cloudforce_one.requests import (
    MessageCreateResponse,
    MessageUpdateResponse,
    MessageDeleteResponse,
    MessageGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_identifier}/cloudforce-one/requests/{request_identifier}/message/new">client.cloudforce_one.requests.message.<a href="./src/cloudflare/resources/cloudforce_one/requests/message.py">create</a>(request_identifier, \*, account_identifier, \*\*<a href="src/cloudflare/types/cloudforce_one/requests/message_create_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/requests/message_create_response.py">MessageCreateResponse</a></code>
- <code title="put /accounts/{account_identifier}/cloudforce-one/requests/{request_identifier}/message/{message_identifer}">client.cloudforce_one.requests.message.<a href="./src/cloudflare/resources/cloudforce_one/requests/message.py">update</a>(message_identifer, \*, account_identifier, request_identifier, \*\*<a href="src/cloudflare/types/cloudforce_one/requests/message_update_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/requests/message_update_response.py">MessageUpdateResponse</a></code>
- <code title="delete /accounts/{account_identifier}/cloudforce-one/requests/{request_identifier}/message/{message_identifer}">client.cloudforce_one.requests.message.<a href="./src/cloudflare/resources/cloudforce_one/requests/message.py">delete</a>(message_identifer, \*, account_identifier, request_identifier) -> <a href="./src/cloudflare/types/cloudforce_one/requests/message_delete_response.py">MessageDeleteResponse</a></code>
- <code title="post /accounts/{account_identifier}/cloudforce-one/requests/{request_identifier}/message">client.cloudforce_one.requests.message.<a href="./src/cloudflare/resources/cloudforce_one/requests/message.py">get</a>(request_identifier, \*, account_identifier, \*\*<a href="src/cloudflare/types/cloudforce_one/requests/message_get_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/requests/message_get_response.py">MessageGetResponse</a></code>

### Priority

Types:

```python
from cloudflare.types.cloudforce_one.requests import (
    PriorityCreateResponse,
    PriorityUpdateResponse,
    PriorityDeleteResponse,
    PriorityDoSomethingUnknownResponse,
    PriorityGetResponse,
    PriorityQuotaResponse,
)
```

Methods:

- <code title="post /accounts/{account_identifier}/cloudforce-one/requests/priority/new">client.cloudforce_one.requests.priority.<a href="./src/cloudflare/resources/cloudforce_one/requests/priority.py">create</a>(account_identifier, \*\*<a href="src/cloudflare/types/cloudforce_one/requests/priority_create_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/requests/priority_create_response.py">PriorityCreateResponse</a></code>
- <code title="put /accounts/{account_identifier}/cloudforce-one/requests/priority/{priority_identifer}">client.cloudforce_one.requests.priority.<a href="./src/cloudflare/resources/cloudforce_one/requests/priority.py">update</a>(priority_identifer, \*, account_identifier, \*\*<a href="src/cloudflare/types/cloudforce_one/requests/priority_update_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/requests/priority_update_response.py">PriorityUpdateResponse</a></code>
- <code title="delete /accounts/{account_identifier}/cloudforce-one/requests/priority/{priority_identifer}">client.cloudforce_one.requests.priority.<a href="./src/cloudflare/resources/cloudforce_one/requests/priority.py">delete</a>(priority_identifer, \*, account_identifier) -> <a href="./src/cloudflare/types/cloudforce_one/requests/priority_delete_response.py">PriorityDeleteResponse</a></code>
- <code title="post /accounts/{account_identifier}/cloudforce-one/requests/priority">client.cloudforce_one.requests.priority.<a href="./src/cloudflare/resources/cloudforce_one/requests/priority.py">do_something_unknown</a>(account_identifier, \*\*<a href="src/cloudflare/types/cloudforce_one/requests/priority_do_something_unknown_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/requests/priority_do_something_unknown_response.py">PriorityDoSomethingUnknownResponse</a></code>
- <code title="get /accounts/{account_identifier}/cloudforce-one/requests/priority/{priority_identifer}">client.cloudforce_one.requests.priority.<a href="./src/cloudflare/resources/cloudforce_one/requests/priority.py">get</a>(priority_identifer, \*, account_identifier) -> <a href="./src/cloudflare/types/cloudforce_one/requests/priority_get_response.py">PriorityGetResponse</a></code>
- <code title="get /accounts/{account_identifier}/cloudforce-one/requests/priority/quota">client.cloudforce_one.requests.priority.<a href="./src/cloudflare/resources/cloudforce_one/requests/priority.py">quota</a>(account_identifier) -> <a href="./src/cloudflare/types/cloudforce_one/requests/priority_quota_response.py">PriorityQuotaResponse</a></code>
