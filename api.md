# Accounts

Types:

```python
from cloudflare.types import AccountUpdateResponse, AccountListResponse, AccountGetResponse
```

Methods:

- <code title="put /accounts/{account_id}">client.accounts.<a href="./src/cloudflare/resources/accounts.py">update</a>(account_id, \*\*<a href="src/cloudflare/types/account_update_params.py">params</a>) -> <a href="./src/cloudflare/types/account_update_response.py">AccountUpdateResponse</a></code>
- <code title="get /accounts">client.accounts.<a href="./src/cloudflare/resources/accounts.py">list</a>(\*\*<a href="src/cloudflare/types/account_list_params.py">params</a>) -> <a href="./src/cloudflare/types/account_list_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}">client.accounts.<a href="./src/cloudflare/resources/accounts.py">get</a>(account_id) -> <a href="./src/cloudflare/types/account_get_response.py">AccountGetResponse</a></code>

# Certificates

Types:

```python
from cloudflare.types import (
    CertificateDeleteResponse,
    CertificateGetResponse,
    CertificateOriginCaCreateCertificateResponse,
    CertificateOriginCaListCertificatesResponse,
)
```

Methods:

- <code title="delete /certificates/{certificate_id}">client.certificates.<a href="./src/cloudflare/resources/certificates.py">delete</a>(certificate_id) -> <a href="./src/cloudflare/types/certificate_delete_response.py">CertificateDeleteResponse</a></code>
- <code title="get /certificates/{certificate_id}">client.certificates.<a href="./src/cloudflare/resources/certificates.py">get</a>(certificate_id) -> <a href="./src/cloudflare/types/certificate_get_response.py">CertificateGetResponse</a></code>
- <code title="post /certificates">client.certificates.<a href="./src/cloudflare/resources/certificates.py">origin_ca_create_certificate</a>(\*\*<a href="src/cloudflare/types/certificate_origin_ca_create_certificate_params.py">params</a>) -> <a href="./src/cloudflare/types/certificate_origin_ca_create_certificate_response.py">CertificateOriginCaCreateCertificateResponse</a></code>
- <code title="get /certificates">client.certificates.<a href="./src/cloudflare/resources/certificates.py">origin_ca_list_certificates</a>() -> <a href="./src/cloudflare/types/certificate_origin_ca_list_certificates_response.py">Optional</a></code>

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
    MembershipDeleteResponse,
    MembershipGetResponse,
    MembershipUserSAccountMembershipsListMembershipsResponse,
)
```

Methods:

- <code title="put /memberships/{membership_id}">client.memberships.<a href="./src/cloudflare/resources/memberships.py">update</a>(membership_id, \*\*<a href="src/cloudflare/types/membership_update_params.py">params</a>) -> <a href="./src/cloudflare/types/membership_update_response.py">MembershipUpdateResponse</a></code>
- <code title="delete /memberships/{membership_id}">client.memberships.<a href="./src/cloudflare/resources/memberships.py">delete</a>(membership_id) -> <a href="./src/cloudflare/types/membership_delete_response.py">MembershipDeleteResponse</a></code>
- <code title="get /memberships/{membership_id}">client.memberships.<a href="./src/cloudflare/resources/memberships.py">get</a>(membership_id) -> <a href="./src/cloudflare/types/membership_get_response.py">MembershipGetResponse</a></code>
- <code title="get /memberships">client.memberships.<a href="./src/cloudflare/resources/memberships.py">user_s_account_memberships_list_memberships</a>(\*\*<a href="src/cloudflare/types/membership_user_s_account_memberships_list_memberships_params.py">params</a>) -> <a href="./src/cloudflare/types/membership_user_s_account_memberships_list_memberships_response.py">Optional</a></code>

# Users

Types:

```python
from cloudflare.types import UserUserEditUserResponse, UserUserUserDetailsResponse
```

Methods:

- <code title="patch /user">client.users.<a href="./src/cloudflare/resources/users/users.py">user_edit_user</a>(\*\*<a href="src/cloudflare/types/user_user_edit_user_params.py">params</a>) -> <a href="./src/cloudflare/types/user_user_edit_user_response.py">UserUserEditUserResponse</a></code>
- <code title="get /user">client.users.<a href="./src/cloudflare/resources/users/users.py">user_user_details</a>() -> <a href="./src/cloudflare/types/user_user_user_details_response.py">UserUserUserDetailsResponse</a></code>

## AuditLogs

Types:

```python
from cloudflare.types.users import AuditLogAuditLogsGetUserAuditLogsResponse
```

Methods:

- <code title="get /user/audit_logs">client.users.audit_logs.<a href="./src/cloudflare/resources/users/audit_logs.py">audit_logs_get_user_audit_logs</a>(\*\*<a href="src/cloudflare/types/users/audit_log_audit_logs_get_user_audit_logs_params.py">params</a>) -> <a href="./src/cloudflare/types/users/audit_log_audit_logs_get_user_audit_logs_response.py">AuditLogAuditLogsGetUserAuditLogsResponse</a></code>

## Billings

### Histories

Types:

```python
from cloudflare.types.users.billings import HistoryUserBillingHistoryBillingHistoryDetailsResponse
```

Methods:

- <code title="get /user/billing/history">client.users.billings.histories.<a href="./src/cloudflare/resources/users/billings/histories.py">user_billing_history_billing_history_details</a>(\*\*<a href="src/cloudflare/types/users/billings/history_user_billing_history_billing_history_details_params.py">params</a>) -> <a href="./src/cloudflare/types/users/billings/history_user_billing_history_billing_history_details_response.py">Optional</a></code>

### Profiles

Types:

```python
from cloudflare.types.users.billings import ProfileUserBillingProfileBillingProfileDetailsResponse
```

Methods:

- <code title="get /user/billing/profile">client.users.billings.profiles.<a href="./src/cloudflare/resources/users/billings/profiles.py">user_billing_profile_billing_profile_details</a>() -> <a href="./src/cloudflare/types/users/billings/profile_user_billing_profile_billing_profile_details_response.py">ProfileUserBillingProfileBillingProfileDetailsResponse</a></code>

## Firewalls

### AccessRules

#### Rules

Types:

```python
from cloudflare.types.users.firewalls.access_rules import (
    RuleUpdateResponse,
    RuleDeleteResponse,
    RuleIPAccessRulesForAUserCreateAnIPAccessRuleResponse,
    RuleIPAccessRulesForAUserListIPAccessRulesResponse,
)
```

Methods:

- <code title="patch /user/firewall/access_rules/rules/{identifier}">client.users.firewalls.access_rules.rules.<a href="./src/cloudflare/resources/users/firewalls/access_rules/rules.py">update</a>(identifier, \*\*<a href="src/cloudflare/types/users/firewalls/access_rules/rule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/users/firewalls/access_rules/rule_update_response.py">Optional</a></code>
- <code title="delete /user/firewall/access_rules/rules/{identifier}">client.users.firewalls.access_rules.rules.<a href="./src/cloudflare/resources/users/firewalls/access_rules/rules.py">delete</a>(identifier) -> <a href="./src/cloudflare/types/users/firewalls/access_rules/rule_delete_response.py">Optional</a></code>
- <code title="post /user/firewall/access_rules/rules">client.users.firewalls.access_rules.rules.<a href="./src/cloudflare/resources/users/firewalls/access_rules/rules.py">ip_access_rules_for_a_user_create_an_ip_access_rule</a>(\*\*<a href="src/cloudflare/types/users/firewalls/access_rules/rule_ip_access_rules_for_a_user_create_an_ip_access_rule_params.py">params</a>) -> <a href="./src/cloudflare/types/users/firewalls/access_rules/rule_ip_access_rules_for_a_user_create_an_ip_access_rule_response.py">Optional</a></code>
- <code title="get /user/firewall/access_rules/rules">client.users.firewalls.access_rules.rules.<a href="./src/cloudflare/resources/users/firewalls/access_rules/rules.py">ip_access_rules_for_a_user_list_ip_access_rules</a>(\*\*<a href="src/cloudflare/types/users/firewalls/access_rules/rule_ip_access_rules_for_a_user_list_ip_access_rules_params.py">params</a>) -> <a href="./src/cloudflare/types/users/firewalls/access_rules/rule_ip_access_rules_for_a_user_list_ip_access_rules_response.py">Optional</a></code>

## Invites

Types:

```python
from cloudflare.types.users import (
    InviteUpdateResponse,
    InviteGetResponse,
    InviteUserSInvitesListInvitationsResponse,
)
```

Methods:

- <code title="patch /user/invites/{invite_id}">client.users.invites.<a href="./src/cloudflare/resources/users/invites.py">update</a>(invite_id, \*\*<a href="src/cloudflare/types/users/invite_update_params.py">params</a>) -> <a href="./src/cloudflare/types/users/invite_update_response.py">InviteUpdateResponse</a></code>
- <code title="get /user/invites/{invite_id}">client.users.invites.<a href="./src/cloudflare/resources/users/invites.py">get</a>(invite_id) -> <a href="./src/cloudflare/types/users/invite_get_response.py">InviteGetResponse</a></code>
- <code title="get /user/invites">client.users.invites.<a href="./src/cloudflare/resources/users/invites.py">user_s_invites_list_invitations</a>() -> <a href="./src/cloudflare/types/users/invite_user_s_invites_list_invitations_response.py">Optional</a></code>

## LoadBalancers

### Monitors

Types:

```python
from cloudflare.types.users.load_balancers import (
    MonitorUpdateResponse,
    MonitorDeleteResponse,
    MonitorGetResponse,
    MonitorLoadBalancerMonitorsCreateMonitorResponse,
    MonitorLoadBalancerMonitorsListMonitorsResponse,
)
```

Methods:

- <code title="put /user/load_balancers/monitors/{identifier}">client.users.load_balancers.monitors.<a href="./src/cloudflare/resources/users/load_balancers/monitors/monitors.py">update</a>(identifier, \*\*<a href="src/cloudflare/types/users/load_balancers/monitor_update_params.py">params</a>) -> <a href="./src/cloudflare/types/users/load_balancers/monitor_update_response.py">MonitorUpdateResponse</a></code>
- <code title="delete /user/load_balancers/monitors/{identifier}">client.users.load_balancers.monitors.<a href="./src/cloudflare/resources/users/load_balancers/monitors/monitors.py">delete</a>(identifier) -> <a href="./src/cloudflare/types/users/load_balancers/monitor_delete_response.py">MonitorDeleteResponse</a></code>
- <code title="get /user/load_balancers/monitors/{identifier}">client.users.load_balancers.monitors.<a href="./src/cloudflare/resources/users/load_balancers/monitors/monitors.py">get</a>(identifier) -> <a href="./src/cloudflare/types/users/load_balancers/monitor_get_response.py">MonitorGetResponse</a></code>
- <code title="post /user/load_balancers/monitors">client.users.load_balancers.monitors.<a href="./src/cloudflare/resources/users/load_balancers/monitors/monitors.py">load_balancer_monitors_create_monitor</a>(\*\*<a href="src/cloudflare/types/users/load_balancers/monitor_load_balancer_monitors_create_monitor_params.py">params</a>) -> <a href="./src/cloudflare/types/users/load_balancers/monitor_load_balancer_monitors_create_monitor_response.py">MonitorLoadBalancerMonitorsCreateMonitorResponse</a></code>
- <code title="get /user/load_balancers/monitors">client.users.load_balancers.monitors.<a href="./src/cloudflare/resources/users/load_balancers/monitors/monitors.py">load_balancer_monitors_list_monitors</a>() -> <a href="./src/cloudflare/types/users/load_balancers/monitor_load_balancer_monitors_list_monitors_response.py">Optional</a></code>

#### Previews

Types:

```python
from cloudflare.types.users.load_balancers.monitors import (
    PreviewLoadBalancerMonitorsPreviewMonitorResponse,
)
```

Methods:

- <code title="post /user/load_balancers/monitors/{identifier}/preview">client.users.load_balancers.monitors.previews.<a href="./src/cloudflare/resources/users/load_balancers/monitors/previews.py">load_balancer_monitors_preview_monitor</a>(identifier, \*\*<a href="src/cloudflare/types/users/load_balancers/monitors/preview_load_balancer_monitors_preview_monitor_params.py">params</a>) -> <a href="./src/cloudflare/types/users/load_balancers/monitors/preview_load_balancer_monitors_preview_monitor_response.py">PreviewLoadBalancerMonitorsPreviewMonitorResponse</a></code>

#### References

Types:

```python
from cloudflare.types.users.load_balancers.monitors import (
    ReferenceLoadBalancerMonitorsListMonitorReferencesResponse,
)
```

Methods:

- <code title="get /user/load_balancers/monitors/{identifier}/references">client.users.load_balancers.monitors.references.<a href="./src/cloudflare/resources/users/load_balancers/monitors/references.py">load_balancer_monitors_list_monitor_references</a>(identifier) -> <a href="./src/cloudflare/types/users/load_balancers/monitors/reference_load_balancer_monitors_list_monitor_references_response.py">Optional</a></code>

### Pools

Types:

```python
from cloudflare.types.users.load_balancers import (
    PoolUpdateResponse,
    PoolDeleteResponse,
    PoolGetResponse,
    PoolLoadBalancerPoolsCreatePoolResponse,
    PoolLoadBalancerPoolsListPoolsResponse,
    PoolLoadBalancerPoolsPatchPoolsResponse,
)
```

Methods:

- <code title="put /user/load_balancers/pools/{identifier}">client.users.load_balancers.pools.<a href="./src/cloudflare/resources/users/load_balancers/pools/pools.py">update</a>(identifier, \*\*<a href="src/cloudflare/types/users/load_balancers/pool_update_params.py">params</a>) -> <a href="./src/cloudflare/types/users/load_balancers/pool_update_response.py">PoolUpdateResponse</a></code>
- <code title="delete /user/load_balancers/pools/{identifier}">client.users.load_balancers.pools.<a href="./src/cloudflare/resources/users/load_balancers/pools/pools.py">delete</a>(identifier) -> <a href="./src/cloudflare/types/users/load_balancers/pool_delete_response.py">PoolDeleteResponse</a></code>
- <code title="get /user/load_balancers/pools/{identifier}">client.users.load_balancers.pools.<a href="./src/cloudflare/resources/users/load_balancers/pools/pools.py">get</a>(identifier) -> <a href="./src/cloudflare/types/users/load_balancers/pool_get_response.py">PoolGetResponse</a></code>
- <code title="post /user/load_balancers/pools">client.users.load_balancers.pools.<a href="./src/cloudflare/resources/users/load_balancers/pools/pools.py">load_balancer_pools_create_pool</a>(\*\*<a href="src/cloudflare/types/users/load_balancers/pool_load_balancer_pools_create_pool_params.py">params</a>) -> <a href="./src/cloudflare/types/users/load_balancers/pool_load_balancer_pools_create_pool_response.py">PoolLoadBalancerPoolsCreatePoolResponse</a></code>
- <code title="get /user/load_balancers/pools">client.users.load_balancers.pools.<a href="./src/cloudflare/resources/users/load_balancers/pools/pools.py">load_balancer_pools_list_pools</a>(\*\*<a href="src/cloudflare/types/users/load_balancers/pool_load_balancer_pools_list_pools_params.py">params</a>) -> <a href="./src/cloudflare/types/users/load_balancers/pool_load_balancer_pools_list_pools_response.py">Optional</a></code>
- <code title="patch /user/load_balancers/pools">client.users.load_balancers.pools.<a href="./src/cloudflare/resources/users/load_balancers/pools/pools.py">load_balancer_pools_patch_pools</a>(\*\*<a href="src/cloudflare/types/users/load_balancers/pool_load_balancer_pools_patch_pools_params.py">params</a>) -> <a href="./src/cloudflare/types/users/load_balancers/pool_load_balancer_pools_patch_pools_response.py">Optional</a></code>

#### Health

Types:

```python
from cloudflare.types.users.load_balancers.pools import (
    HealthLoadBalancerPoolsPoolHealthDetailsResponse,
)
```

Methods:

- <code title="get /user/load_balancers/pools/{identifier}/health">client.users.load_balancers.pools.health.<a href="./src/cloudflare/resources/users/load_balancers/pools/health.py">load_balancer_pools_pool_health_details</a>(identifier) -> <a href="./src/cloudflare/types/users/load_balancers/pools/health_load_balancer_pools_pool_health_details_response.py">HealthLoadBalancerPoolsPoolHealthDetailsResponse</a></code>

#### Previews

Types:

```python
from cloudflare.types.users.load_balancers.pools import PreviewLoadBalancerPoolsPreviewPoolResponse
```

Methods:

- <code title="post /user/load_balancers/pools/{identifier}/preview">client.users.load_balancers.pools.previews.<a href="./src/cloudflare/resources/users/load_balancers/pools/previews.py">load_balancer_pools_preview_pool</a>(identifier, \*\*<a href="src/cloudflare/types/users/load_balancers/pools/preview_load_balancer_pools_preview_pool_params.py">params</a>) -> <a href="./src/cloudflare/types/users/load_balancers/pools/preview_load_balancer_pools_preview_pool_response.py">PreviewLoadBalancerPoolsPreviewPoolResponse</a></code>

#### References

Types:

```python
from cloudflare.types.users.load_balancers.pools import (
    ReferenceLoadBalancerPoolsListPoolReferencesResponse,
)
```

Methods:

- <code title="get /user/load_balancers/pools/{identifier}/references">client.users.load_balancers.pools.references.<a href="./src/cloudflare/resources/users/load_balancers/pools/references.py">load_balancer_pools_list_pool_references</a>(identifier) -> <a href="./src/cloudflare/types/users/load_balancers/pools/reference_load_balancer_pools_list_pool_references_response.py">Optional</a></code>

### Previews

Types:

```python
from cloudflare.types.users.load_balancers import PreviewGetResponse
```

Methods:

- <code title="get /user/load_balancers/preview/{preview_id}">client.users.load_balancers.previews.<a href="./src/cloudflare/resources/users/load_balancers/previews.py">get</a>(preview_id) -> <a href="./src/cloudflare/types/users/load_balancers/preview_get_response.py">PreviewGetResponse</a></code>

## LoadBalancingAnalytics

### Events

Types:

```python
from cloudflare.types.users.load_balancing_analytics import (
    EventLoadBalancerHealthcheckEventsListHealthcheckEventsResponse,
)
```

Methods:

- <code title="get /user/load_balancing_analytics/events">client.users.load_balancing_analytics.events.<a href="./src/cloudflare/resources/users/load_balancing_analytics/events.py">load_balancer_healthcheck_events_list_healthcheck_events</a>(\*\*<a href="src/cloudflare/types/users/load_balancing_analytics/event_load_balancer_healthcheck_events_list_healthcheck_events_params.py">params</a>) -> <a href="./src/cloudflare/types/users/load_balancing_analytics/event_load_balancer_healthcheck_events_list_healthcheck_events_response.py">Optional</a></code>

## Organizations

Types:

```python
from cloudflare.types.users import (
    OrganizationDeleteResponse,
    OrganizationGetResponse,
    OrganizationUserSOrganizationsListOrganizationsResponse,
)
```

Methods:

- <code title="delete /user/organizations/{organization_id}">client.users.organizations.<a href="./src/cloudflare/resources/users/organizations.py">delete</a>(organization_id) -> <a href="./src/cloudflare/types/users/organization_delete_response.py">OrganizationDeleteResponse</a></code>
- <code title="get /user/organizations/{organization_id}">client.users.organizations.<a href="./src/cloudflare/resources/users/organizations.py">get</a>(organization_id) -> <a href="./src/cloudflare/types/users/organization_get_response.py">OrganizationGetResponse</a></code>
- <code title="get /user/organizations">client.users.organizations.<a href="./src/cloudflare/resources/users/organizations.py">user_s_organizations_list_organizations</a>(\*\*<a href="src/cloudflare/types/users/organization_user_s_organizations_list_organizations_params.py">params</a>) -> <a href="./src/cloudflare/types/users/organization_user_s_organizations_list_organizations_response.py">Optional</a></code>

## Subscriptions

Types:

```python
from cloudflare.types.users import (
    SubscriptionUpdateResponse,
    SubscriptionDeleteResponse,
    SubscriptionUserSubscriptionGetUserSubscriptionsResponse,
)
```

Methods:

- <code title="put /user/subscriptions/{identifier}">client.users.subscriptions.<a href="./src/cloudflare/resources/users/subscriptions.py">update</a>(identifier, \*\*<a href="src/cloudflare/types/users/subscription_update_params.py">params</a>) -> <a href="./src/cloudflare/types/users/subscription_update_response.py">SubscriptionUpdateResponse</a></code>
- <code title="delete /user/subscriptions/{identifier}">client.users.subscriptions.<a href="./src/cloudflare/resources/users/subscriptions.py">delete</a>(identifier) -> <a href="./src/cloudflare/types/users/subscription_delete_response.py">SubscriptionDeleteResponse</a></code>
- <code title="get /user/subscriptions">client.users.subscriptions.<a href="./src/cloudflare/resources/users/subscriptions.py">user_subscription_get_user_subscriptions</a>() -> <a href="./src/cloudflare/types/users/subscription_user_subscription_get_user_subscriptions_response.py">Optional</a></code>

## Tokens

Types:

```python
from cloudflare.types.users import (
    TokenUpdateResponse,
    TokenDeleteResponse,
    TokenGetResponse,
    TokenUserAPITokensCreateTokenResponse,
    TokenUserAPITokensListTokensResponse,
)
```

Methods:

- <code title="put /user/tokens/{token_id}">client.users.tokens.<a href="./src/cloudflare/resources/users/tokens/tokens.py">update</a>(token_id, \*\*<a href="src/cloudflare/types/users/token_update_params.py">params</a>) -> <a href="./src/cloudflare/types/users/token_update_response.py">TokenUpdateResponse</a></code>
- <code title="delete /user/tokens/{token_id}">client.users.tokens.<a href="./src/cloudflare/resources/users/tokens/tokens.py">delete</a>(token_id) -> <a href="./src/cloudflare/types/users/token_delete_response.py">Optional</a></code>
- <code title="get /user/tokens/{token_id}">client.users.tokens.<a href="./src/cloudflare/resources/users/tokens/tokens.py">get</a>(token_id) -> <a href="./src/cloudflare/types/users/token_get_response.py">TokenGetResponse</a></code>
- <code title="post /user/tokens">client.users.tokens.<a href="./src/cloudflare/resources/users/tokens/tokens.py">user_api_tokens_create_token</a>(\*\*<a href="src/cloudflare/types/users/token_user_api_tokens_create_token_params.py">params</a>) -> <a href="./src/cloudflare/types/users/token_user_api_tokens_create_token_response.py">TokenUserAPITokensCreateTokenResponse</a></code>
- <code title="get /user/tokens">client.users.tokens.<a href="./src/cloudflare/resources/users/tokens/tokens.py">user_api_tokens_list_tokens</a>(\*\*<a href="src/cloudflare/types/users/token_user_api_tokens_list_tokens_params.py">params</a>) -> <a href="./src/cloudflare/types/users/token_user_api_tokens_list_tokens_response.py">Optional</a></code>

### PermissionGroups

Types:

```python
from cloudflare.types.users.tokens import (
    PermissionGroupPermissionGroupsListPermissionGroupsResponse,
)
```

Methods:

- <code title="get /user/tokens/permission_groups">client.users.tokens.permission_groups.<a href="./src/cloudflare/resources/users/tokens/permission_groups.py">permission_groups_list_permission_groups</a>() -> <a href="./src/cloudflare/types/users/tokens/permission_group_permission_groups_list_permission_groups_response.py">Optional</a></code>

### Verifies

Types:

```python
from cloudflare.types.users.tokens import VerifyUserAPITokensVerifyTokenResponse
```

Methods:

- <code title="get /user/tokens/verify">client.users.tokens.verifies.<a href="./src/cloudflare/resources/users/tokens/verifies.py">user_api_tokens_verify_token</a>() -> <a href="./src/cloudflare/types/users/tokens/verify_user_api_tokens_verify_token_response.py">VerifyUserAPITokensVerifyTokenResponse</a></code>

### Values

Types:

```python
from cloudflare.types.users.tokens import ValueUserAPITokensRollTokenResponse
```

Methods:

- <code title="put /user/tokens/{token_id}/value">client.users.tokens.values.<a href="./src/cloudflare/resources/users/tokens/values.py">user_api_tokens_roll_token</a>(token_id, \*\*<a href="src/cloudflare/types/users/tokens/value_user_api_tokens_roll_token_params.py">params</a>) -> <a href="./src/cloudflare/types/users/tokens/value_user_api_tokens_roll_token_response.py">str</a></code>

# Zones

Types:

```python
from cloudflare.types import (
    ZoneCreateResponse,
    ZoneUpdateResponse,
    ZoneListResponse,
    ZoneDeleteResponse,
    ZoneGetResponse,
)
```

Methods:

- <code title="post /zones">client.zones.<a href="./src/cloudflare/resources/zones/zones.py">create</a>(\*\*<a href="src/cloudflare/types/zone_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zone_create_response.py">Optional</a></code>
- <code title="patch /zones/{zone_id}">client.zones.<a href="./src/cloudflare/resources/zones/zones.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/zone_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zone_update_response.py">Optional</a></code>
- <code title="get /zones">client.zones.<a href="./src/cloudflare/resources/zones/zones.py">list</a>(\*\*<a href="src/cloudflare/types/zone_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zone_list_response.py">Optional</a></code>
- <code title="delete /zones/{zone_id}">client.zones.<a href="./src/cloudflare/resources/zones/zones.py">delete</a>(zone_id) -> <a href="./src/cloudflare/types/zone_delete_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}">client.zones.<a href="./src/cloudflare/resources/zones/zones.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/zone_get_response.py">Optional</a></code>

## Hold

Types:

```python
from cloudflare.types.zones import HoldEnforceResponse, HoldGetResponse, HoldRemoveResponse
```

Methods:

- <code title="post /zones/{zone_id}/hold">client.zones.hold.<a href="./src/cloudflare/resources/zones/hold.py">enforce</a>(zone_id, \*\*<a href="src/cloudflare/types/zones/hold_enforce_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/hold_enforce_response.py">HoldEnforceResponse</a></code>
- <code title="get /zones/{zone_id}/hold">client.zones.hold.<a href="./src/cloudflare/resources/zones/hold.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/zones/hold_get_response.py">HoldGetResponse</a></code>
- <code title="delete /zones/{zone_id}/hold">client.zones.hold.<a href="./src/cloudflare/resources/zones/hold.py">remove</a>(zone_id, \*\*<a href="src/cloudflare/types/zones/hold_remove_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/hold_remove_response.py">Optional</a></code>

# AI

Types:

```python
from cloudflare.types import AIRunResponse
```

Methods:

- <code title="post /accounts/{account_id}/ai/run/{model_name}">client.ai.<a href="./src/cloudflare/resources/ai.py">run</a>(model_name, \*, account_id, \*\*<a href="src/cloudflare/types/ai_run_params.py">params</a>) -> <a href="./src/cloudflare/types/ai_run_response.py">object</a></code>

# LoadBalancers

Types:

```python
from cloudflare.types import (
    LoadBalancerCreateResponse,
    LoadBalancerUpdateResponse,
    LoadBalancerListResponse,
    LoadBalancerDeleteResponse,
    LoadBalancerGetResponse,
)
```

Methods:

- <code title="post /zones/{identifier}/load_balancers">client.load_balancers.<a href="./src/cloudflare/resources/load_balancers/load_balancers.py">create</a>(identifier, \*\*<a href="src/cloudflare/types/load_balancer_create_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancer_create_response.py">LoadBalancerCreateResponse</a></code>
- <code title="put /zones/{identifier1}/load_balancers/{identifier}">client.load_balancers.<a href="./src/cloudflare/resources/load_balancers/load_balancers.py">update</a>(identifier, \*, identifier1, \*\*<a href="src/cloudflare/types/load_balancer_update_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancer_update_response.py">LoadBalancerUpdateResponse</a></code>
- <code title="get /zones/{identifier}/load_balancers">client.load_balancers.<a href="./src/cloudflare/resources/load_balancers/load_balancers.py">list</a>(identifier) -> <a href="./src/cloudflare/types/load_balancer_list_response.py">Optional</a></code>
- <code title="delete /zones/{identifier1}/load_balancers/{identifier}">client.load_balancers.<a href="./src/cloudflare/resources/load_balancers/load_balancers.py">delete</a>(identifier, \*, identifier1) -> <a href="./src/cloudflare/types/load_balancer_delete_response.py">LoadBalancerDeleteResponse</a></code>
- <code title="get /zones/{identifier1}/load_balancers/{identifier}">client.load_balancers.<a href="./src/cloudflare/resources/load_balancers/load_balancers.py">get</a>(identifier, \*, identifier1) -> <a href="./src/cloudflare/types/load_balancer_get_response.py">LoadBalancerGetResponse</a></code>

## Monitors

Types:

```python
from cloudflare.types.load_balancers import (
    MonitorUpdateResponse,
    MonitorDeleteResponse,
    MonitorAccountLoadBalancerMonitorsCreateMonitorResponse,
    MonitorAccountLoadBalancerMonitorsListMonitorsResponse,
    MonitorGetResponse,
)
```

Methods:

- <code title="put /accounts/{account_identifier}/load_balancers/monitors/{identifier}">client.load_balancers.monitors.<a href="./src/cloudflare/resources/load_balancers/monitors/monitors.py">update</a>(identifier, \*, account_identifier, \*\*<a href="src/cloudflare/types/load_balancers/monitor_update_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancers/monitor_update_response.py">MonitorUpdateResponse</a></code>
- <code title="delete /accounts/{account_identifier}/load_balancers/monitors/{identifier}">client.load_balancers.monitors.<a href="./src/cloudflare/resources/load_balancers/monitors/monitors.py">delete</a>(identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/load_balancers/monitor_delete_response.py">MonitorDeleteResponse</a></code>
- <code title="post /accounts/{account_identifier}/load_balancers/monitors">client.load_balancers.monitors.<a href="./src/cloudflare/resources/load_balancers/monitors/monitors.py">account_load_balancer_monitors_create_monitor</a>(account_identifier, \*\*<a href="src/cloudflare/types/load_balancers/monitor_account_load_balancer_monitors_create_monitor_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancers/monitor_account_load_balancer_monitors_create_monitor_response.py">MonitorAccountLoadBalancerMonitorsCreateMonitorResponse</a></code>
- <code title="get /accounts/{account_identifier}/load_balancers/monitors">client.load_balancers.monitors.<a href="./src/cloudflare/resources/load_balancers/monitors/monitors.py">account_load_balancer_monitors_list_monitors</a>(account_identifier) -> <a href="./src/cloudflare/types/load_balancers/monitor_account_load_balancer_monitors_list_monitors_response.py">Optional</a></code>
- <code title="get /accounts/{account_identifier}/load_balancers/monitors/{identifier}">client.load_balancers.monitors.<a href="./src/cloudflare/resources/load_balancers/monitors/monitors.py">get</a>(identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/load_balancers/monitor_get_response.py">MonitorGetResponse</a></code>

### Previews

Types:

```python
from cloudflare.types.load_balancers.monitors import (
    PreviewAccountLoadBalancerMonitorsPreviewMonitorResponse,
)
```

Methods:

- <code title="post /accounts/{account_identifier}/load_balancers/monitors/{identifier}/preview">client.load_balancers.monitors.previews.<a href="./src/cloudflare/resources/load_balancers/monitors/previews.py">account_load_balancer_monitors_preview_monitor</a>(identifier, \*, account_identifier, \*\*<a href="src/cloudflare/types/load_balancers/monitors/preview_account_load_balancer_monitors_preview_monitor_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancers/monitors/preview_account_load_balancer_monitors_preview_monitor_response.py">PreviewAccountLoadBalancerMonitorsPreviewMonitorResponse</a></code>

### References

Types:

```python
from cloudflare.types.load_balancers.monitors import (
    ReferenceAccountLoadBalancerMonitorsListMonitorReferencesResponse,
)
```

Methods:

- <code title="get /accounts/{account_identifier}/load_balancers/monitors/{identifier}/references">client.load_balancers.monitors.references.<a href="./src/cloudflare/resources/load_balancers/monitors/references.py">account_load_balancer_monitors_list_monitor_references</a>(identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/load_balancers/monitors/reference_account_load_balancer_monitors_list_monitor_references_response.py">Optional</a></code>

## Pools

Types:

```python
from cloudflare.types.load_balancers import (
    PoolUpdateResponse,
    PoolDeleteResponse,
    PoolAccountLoadBalancerPoolsCreatePoolResponse,
    PoolAccountLoadBalancerPoolsListPoolsResponse,
    PoolAccountLoadBalancerPoolsPatchPoolsResponse,
    PoolGetResponse,
)
```

Methods:

- <code title="put /accounts/{account_identifier}/load_balancers/pools/{identifier}">client.load_balancers.pools.<a href="./src/cloudflare/resources/load_balancers/pools/pools.py">update</a>(identifier, \*, account_identifier, \*\*<a href="src/cloudflare/types/load_balancers/pool_update_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancers/pool_update_response.py">PoolUpdateResponse</a></code>
- <code title="delete /accounts/{account_identifier}/load_balancers/pools/{identifier}">client.load_balancers.pools.<a href="./src/cloudflare/resources/load_balancers/pools/pools.py">delete</a>(identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/load_balancers/pool_delete_response.py">PoolDeleteResponse</a></code>
- <code title="post /accounts/{account_identifier}/load_balancers/pools">client.load_balancers.pools.<a href="./src/cloudflare/resources/load_balancers/pools/pools.py">account_load_balancer_pools_create_pool</a>(account_identifier, \*\*<a href="src/cloudflare/types/load_balancers/pool_account_load_balancer_pools_create_pool_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancers/pool_account_load_balancer_pools_create_pool_response.py">PoolAccountLoadBalancerPoolsCreatePoolResponse</a></code>
- <code title="get /accounts/{account_identifier}/load_balancers/pools">client.load_balancers.pools.<a href="./src/cloudflare/resources/load_balancers/pools/pools.py">account_load_balancer_pools_list_pools</a>(account_identifier, \*\*<a href="src/cloudflare/types/load_balancers/pool_account_load_balancer_pools_list_pools_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancers/pool_account_load_balancer_pools_list_pools_response.py">Optional</a></code>
- <code title="patch /accounts/{account_identifier}/load_balancers/pools">client.load_balancers.pools.<a href="./src/cloudflare/resources/load_balancers/pools/pools.py">account_load_balancer_pools_patch_pools</a>(account_identifier, \*\*<a href="src/cloudflare/types/load_balancers/pool_account_load_balancer_pools_patch_pools_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancers/pool_account_load_balancer_pools_patch_pools_response.py">Optional</a></code>
- <code title="get /accounts/{account_identifier}/load_balancers/pools/{identifier}">client.load_balancers.pools.<a href="./src/cloudflare/resources/load_balancers/pools/pools.py">get</a>(identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/load_balancers/pool_get_response.py">PoolGetResponse</a></code>

### Health

Types:

```python
from cloudflare.types.load_balancers.pools import (
    HealthAccountLoadBalancerPoolsPoolHealthDetailsResponse,
)
```

Methods:

- <code title="get /accounts/{account_identifier}/load_balancers/pools/{identifier}/health">client.load_balancers.pools.health.<a href="./src/cloudflare/resources/load_balancers/pools/health.py">account_load_balancer_pools_pool_health_details</a>(identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/load_balancers/pools/health_account_load_balancer_pools_pool_health_details_response.py">HealthAccountLoadBalancerPoolsPoolHealthDetailsResponse</a></code>

### Previews

Types:

```python
from cloudflare.types.load_balancers.pools import PreviewAccountLoadBalancerPoolsPreviewPoolResponse
```

Methods:

- <code title="post /accounts/{account_identifier}/load_balancers/pools/{identifier}/preview">client.load_balancers.pools.previews.<a href="./src/cloudflare/resources/load_balancers/pools/previews.py">account_load_balancer_pools_preview_pool</a>(identifier, \*, account_identifier, \*\*<a href="src/cloudflare/types/load_balancers/pools/preview_account_load_balancer_pools_preview_pool_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancers/pools/preview_account_load_balancer_pools_preview_pool_response.py">PreviewAccountLoadBalancerPoolsPreviewPoolResponse</a></code>

### References

Types:

```python
from cloudflare.types.load_balancers.pools import (
    ReferenceAccountLoadBalancerPoolsListPoolReferencesResponse,
)
```

Methods:

- <code title="get /accounts/{account_identifier}/load_balancers/pools/{identifier}/references">client.load_balancers.pools.references.<a href="./src/cloudflare/resources/load_balancers/pools/references.py">account_load_balancer_pools_list_pool_references</a>(identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/load_balancers/pools/reference_account_load_balancer_pools_list_pool_references_response.py">Optional</a></code>

## Previews

Types:

```python
from cloudflare.types.load_balancers import PreviewGetResponse
```

Methods:

- <code title="get /accounts/{account_identifier}/load_balancers/preview/{preview_id}">client.load_balancers.previews.<a href="./src/cloudflare/resources/load_balancers/previews.py">get</a>(preview_id, \*, account_identifier) -> <a href="./src/cloudflare/types/load_balancers/preview_get_response.py">PreviewGetResponse</a></code>

## Regions

Types:

```python
from cloudflare.types.load_balancers import (
    RegionGetResponse,
    RegionLoadBalancerRegionsListRegionsResponse,
)
```

Methods:

- <code title="get /accounts/{account_identifier}/load_balancers/regions/{region_code}">client.load_balancers.regions.<a href="./src/cloudflare/resources/load_balancers/regions.py">get</a>(region_code, \*, account_identifier) -> <a href="./src/cloudflare/types/load_balancers/region_get_response.py">RegionGetResponse</a></code>
- <code title="get /accounts/{account_identifier}/load_balancers/regions">client.load_balancers.regions.<a href="./src/cloudflare/resources/load_balancers/regions.py">load_balancer_regions_list_regions</a>(account_identifier, \*\*<a href="src/cloudflare/types/load_balancers/region_load_balancer_regions_list_regions_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancers/region_load_balancer_regions_list_regions_response.py">RegionLoadBalancerRegionsListRegionsResponse</a></code>

## Searches

Types:

```python
from cloudflare.types.load_balancers import SearchListResponse
```

Methods:

- <code title="get /accounts/{account_identifier}/load_balancers/search">client.load_balancers.searches.<a href="./src/cloudflare/resources/load_balancers/searches.py">list</a>(account_identifier, \*\*<a href="src/cloudflare/types/load_balancers/search_list_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancers/search_list_response.py">Optional</a></code>

# Access

## Apps

Types:

```python
from cloudflare.types.access import (
    AppCreateResponse,
    AppUpdateResponse,
    AppListResponse,
    AppDeleteResponse,
    AppGetResponse,
)
```

Methods:

- <code title="post /{account_or_zone}/{account_or_zone_id}/access/apps">client.access.apps.<a href="./src/cloudflare/resources/access/apps/apps.py">create</a>(account_or_zone_id, \*, account_or_zone, \*\*<a href="src/cloudflare/types/access/app_create_params.py">params</a>) -> <a href="./src/cloudflare/types/access/app_create_response.py">AppCreateResponse</a></code>
- <code title="put /{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}">client.access.apps.<a href="./src/cloudflare/resources/access/apps/apps.py">update</a>(app_id, \*, account_or_zone, account_or_zone_id, \*\*<a href="src/cloudflare/types/access/app_update_params.py">params</a>) -> <a href="./src/cloudflare/types/access/app_update_response.py">AppUpdateResponse</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/apps">client.access.apps.<a href="./src/cloudflare/resources/access/apps/apps.py">list</a>(account_or_zone_id, \*, account_or_zone) -> <a href="./src/cloudflare/types/access/app_list_response.py">Optional</a></code>
- <code title="delete /{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}">client.access.apps.<a href="./src/cloudflare/resources/access/apps/apps.py">delete</a>(app_id, \*, account_or_zone, account_or_zone_id) -> <a href="./src/cloudflare/types/access/app_delete_response.py">AppDeleteResponse</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}">client.access.apps.<a href="./src/cloudflare/resources/access/apps/apps.py">get</a>(app_id, \*, account_or_zone, account_or_zone_id) -> <a href="./src/cloudflare/types/access/app_get_response.py">AppGetResponse</a></code>

### Cas

Types:

```python
from cloudflare.types.access.apps import (
    CaCreateResponse,
    CaListResponse,
    CaDeleteResponse,
    CaGetResponse,
)
```

Methods:

- <code title="post /{account_or_zone}/{account_or_zone_id}/access/apps/{uuid}/ca">client.access.apps.cas.<a href="./src/cloudflare/resources/access/apps/cas.py">create</a>(uuid, \*, account_or_zone, account_or_zone_id) -> <a href="./src/cloudflare/types/access/apps/ca_create_response.py">CaCreateResponse</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/apps/ca">client.access.apps.cas.<a href="./src/cloudflare/resources/access/apps/cas.py">list</a>(account_or_zone_id, \*, account_or_zone) -> <a href="./src/cloudflare/types/access/apps/ca_list_response.py">Optional</a></code>
- <code title="delete /{account_or_zone}/{account_or_zone_id}/access/apps/{uuid}/ca">client.access.apps.cas.<a href="./src/cloudflare/resources/access/apps/cas.py">delete</a>(uuid, \*, account_or_zone, account_or_zone_id) -> <a href="./src/cloudflare/types/access/apps/ca_delete_response.py">CaDeleteResponse</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/apps/{uuid}/ca">client.access.apps.cas.<a href="./src/cloudflare/resources/access/apps/cas.py">get</a>(uuid, \*, account_or_zone, account_or_zone_id) -> <a href="./src/cloudflare/types/access/apps/ca_get_response.py">CaGetResponse</a></code>

### RevokeTokens

Types:

```python
from cloudflare.types.access.apps import RevokeTokenAccessApplicationsRevokeServiceTokensResponse
```

Methods:

- <code title="post /{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}/revoke_tokens">client.access.apps.revoke_tokens.<a href="./src/cloudflare/resources/access/apps/revoke_tokens.py">access_applications_revoke_service_tokens</a>(app_id, \*, account_or_zone, account_or_zone_id) -> <a href="./src/cloudflare/types/access/apps/revoke_token_access_applications_revoke_service_tokens_response.py">object</a></code>

### UserPolicyChecks

Types:

```python
from cloudflare.types.access.apps import UserPolicyCheckAccessApplicationsTestAccessPoliciesResponse
```

Methods:

- <code title="get /{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}/user_policy_checks">client.access.apps.user_policy_checks.<a href="./src/cloudflare/resources/access/apps/user_policy_checks.py">access_applications_test_access_policies</a>(app_id, \*, account_or_zone, account_or_zone_id) -> <a href="./src/cloudflare/types/access/apps/user_policy_check_access_applications_test_access_policies_response.py">UserPolicyCheckAccessApplicationsTestAccessPoliciesResponse</a></code>

### Policies

Types:

```python
from cloudflare.types.access.apps import (
    PolicyCreateResponse,
    PolicyUpdateResponse,
    PolicyDeleteResponse,
    PolicyAccessPoliciesCreateAnAccessPolicyResponse,
    PolicyAccessPoliciesListAccessPoliciesResponse,
    PolicyGetResponse,
)
```

Methods:

- <code title="post /{account_or_zone}/{account_or_zone_id}/access/apps/{uuid}/policies">client.access.apps.policies.<a href="./src/cloudflare/resources/access/apps/policies.py">create</a>(uuid, \*, account_or_zone, account_or_zone_id, \*\*<a href="src/cloudflare/types/access/apps/policy_create_params.py">params</a>) -> <a href="./src/cloudflare/types/access/apps/policy_create_response.py">PolicyCreateResponse</a></code>
- <code title="put /{account_or_zone}/{account_or_zone_id}/access/apps/{uuid1}/policies/{uuid}">client.access.apps.policies.<a href="./src/cloudflare/resources/access/apps/policies.py">update</a>(uuid, \*, account_or_zone, account_or_zone_id, uuid1, \*\*<a href="src/cloudflare/types/access/apps/policy_update_params.py">params</a>) -> <a href="./src/cloudflare/types/access/apps/policy_update_response.py">PolicyUpdateResponse</a></code>
- <code title="delete /{account_or_zone}/{account_or_zone_id}/access/apps/{uuid1}/policies/{uuid}">client.access.apps.policies.<a href="./src/cloudflare/resources/access/apps/policies.py">delete</a>(uuid, \*, account_or_zone, account_or_zone_id, uuid1) -> <a href="./src/cloudflare/types/access/apps/policy_delete_response.py">PolicyDeleteResponse</a></code>
- <code title="post /{account_or_zone}/{account_or_zone_id}/access/apps/{uuid}/policies">client.access.apps.policies.<a href="./src/cloudflare/resources/access/apps/policies.py">access_policies_create_an_access_policy</a>(uuid, \*, account_or_zone, account_or_zone_id, \*\*<a href="src/cloudflare/types/access/apps/policy_access_policies_create_an_access_policy_params.py">params</a>) -> <a href="./src/cloudflare/types/access/apps/policy_access_policies_create_an_access_policy_response.py">PolicyAccessPoliciesCreateAnAccessPolicyResponse</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/apps/{uuid}/policies">client.access.apps.policies.<a href="./src/cloudflare/resources/access/apps/policies.py">access_policies_list_access_policies</a>(uuid, \*, account_or_zone, account_or_zone_id) -> <a href="./src/cloudflare/types/access/apps/policy_access_policies_list_access_policies_response.py">Optional</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/apps/{uuid1}/policies/{uuid}">client.access.apps.policies.<a href="./src/cloudflare/resources/access/apps/policies.py">get</a>(uuid, \*, account_or_zone, account_or_zone_id, uuid1) -> <a href="./src/cloudflare/types/access/apps/policy_get_response.py">PolicyGetResponse</a></code>

## Certificates

Types:

```python
from cloudflare.types.access import (
    CertificateUpdateResponse,
    CertificateDeleteResponse,
    CertificateAccessMTLSAuthenticationAddAnMTLSCertificateResponse,
    CertificateAccessMTLSAuthenticationListMTLSCertificatesResponse,
    CertificateGetResponse,
)
```

Methods:

- <code title="put /{account_or_zone}/{account_or_zone_id}/access/certificates/{uuid}">client.access.certificates.<a href="./src/cloudflare/resources/access/certificates/certificates.py">update</a>(uuid, \*, account_or_zone, account_or_zone_id, \*\*<a href="src/cloudflare/types/access/certificate_update_params.py">params</a>) -> <a href="./src/cloudflare/types/access/certificate_update_response.py">CertificateUpdateResponse</a></code>
- <code title="delete /{account_or_zone}/{account_or_zone_id}/access/certificates/{uuid}">client.access.certificates.<a href="./src/cloudflare/resources/access/certificates/certificates.py">delete</a>(uuid, \*, account_or_zone, account_or_zone_id) -> <a href="./src/cloudflare/types/access/certificate_delete_response.py">CertificateDeleteResponse</a></code>
- <code title="post /{account_or_zone}/{account_or_zone_id}/access/certificates">client.access.certificates.<a href="./src/cloudflare/resources/access/certificates/certificates.py">access_m_tls_authentication_add_an_m_tls_certificate</a>(account_or_zone_id, \*, account_or_zone, \*\*<a href="src/cloudflare/types/access/certificate_access_m_tls_authentication_add_an_m_tls_certificate_params.py">params</a>) -> <a href="./src/cloudflare/types/access/certificate_access_m_tls_authentication_add_an_m_tls_certificate_response.py">CertificateAccessMTLSAuthenticationAddAnMTLSCertificateResponse</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/certificates">client.access.certificates.<a href="./src/cloudflare/resources/access/certificates/certificates.py">access_m_tls_authentication_list_m_tls_certificates</a>(account_or_zone_id, \*, account_or_zone) -> <a href="./src/cloudflare/types/access/certificate_access_m_tls_authentication_list_m_tls_certificates_response.py">Optional</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/certificates/{uuid}">client.access.certificates.<a href="./src/cloudflare/resources/access/certificates/certificates.py">get</a>(uuid, \*, account_or_zone, account_or_zone_id) -> <a href="./src/cloudflare/types/access/certificate_get_response.py">CertificateGetResponse</a></code>

### Settings

Types:

```python
from cloudflare.types.access.certificates import SettingUpdateResponse, SettingListResponse
```

Methods:

- <code title="put /{account_or_zone}/{account_or_zone_id}/access/certificates/settings">client.access.certificates.settings.<a href="./src/cloudflare/resources/access/certificates/settings.py">update</a>(account_or_zone_id, \*, account_or_zone, \*\*<a href="src/cloudflare/types/access/certificates/setting_update_params.py">params</a>) -> <a href="./src/cloudflare/types/access/certificates/setting_update_response.py">Optional</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/certificates/settings">client.access.certificates.settings.<a href="./src/cloudflare/resources/access/certificates/settings.py">list</a>(account_or_zone_id, \*, account_or_zone) -> <a href="./src/cloudflare/types/access/certificates/setting_list_response.py">Optional</a></code>

## Groups

Types:

```python
from cloudflare.types.access import (
    GroupUpdateResponse,
    GroupDeleteResponse,
    GroupAccessGroupsCreateAnAccessGroupResponse,
    GroupAccessGroupsListAccessGroupsResponse,
    GroupGetResponse,
)
```

Methods:

- <code title="put /{account_or_zone}/{account_or_zone_id}/access/groups/{uuid}">client.access.groups.<a href="./src/cloudflare/resources/access/groups.py">update</a>(uuid, \*, account_or_zone, account_or_zone_id, \*\*<a href="src/cloudflare/types/access/group_update_params.py">params</a>) -> <a href="./src/cloudflare/types/access/group_update_response.py">GroupUpdateResponse</a></code>
- <code title="delete /{account_or_zone}/{account_or_zone_id}/access/groups/{uuid}">client.access.groups.<a href="./src/cloudflare/resources/access/groups.py">delete</a>(uuid, \*, account_or_zone, account_or_zone_id) -> <a href="./src/cloudflare/types/access/group_delete_response.py">GroupDeleteResponse</a></code>
- <code title="post /{account_or_zone}/{account_or_zone_id}/access/groups">client.access.groups.<a href="./src/cloudflare/resources/access/groups.py">access_groups_create_an_access_group</a>(account_or_zone_id, \*, account_or_zone, \*\*<a href="src/cloudflare/types/access/group_access_groups_create_an_access_group_params.py">params</a>) -> <a href="./src/cloudflare/types/access/group_access_groups_create_an_access_group_response.py">GroupAccessGroupsCreateAnAccessGroupResponse</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/groups">client.access.groups.<a href="./src/cloudflare/resources/access/groups.py">access_groups_list_access_groups</a>(account_or_zone_id, \*, account_or_zone) -> <a href="./src/cloudflare/types/access/group_access_groups_list_access_groups_response.py">Optional</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/groups/{uuid}">client.access.groups.<a href="./src/cloudflare/resources/access/groups.py">get</a>(uuid, \*, account_or_zone, account_or_zone_id) -> <a href="./src/cloudflare/types/access/group_get_response.py">GroupGetResponse</a></code>

## IdentityProviders

Types:

```python
from cloudflare.types.access import (
    IdentityProviderUpdateResponse,
    IdentityProviderDeleteResponse,
    IdentityProviderAccessIdentityProvidersAddAnAccessIdentityProviderResponse,
    IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponse,
    IdentityProviderGetResponse,
)
```

Methods:

- <code title="put /{account_or_zone}/{account_or_zone_id}/access/identity_providers/{uuid}">client.access.identity_providers.<a href="./src/cloudflare/resources/access/identity_providers.py">update</a>(uuid, \*, account_or_zone, account_or_zone_id, \*\*<a href="src/cloudflare/types/access/identity_provider_update_params.py">params</a>) -> <a href="./src/cloudflare/types/access/identity_provider_update_response.py">IdentityProviderUpdateResponse</a></code>
- <code title="delete /{account_or_zone}/{account_or_zone_id}/access/identity_providers/{uuid}">client.access.identity_providers.<a href="./src/cloudflare/resources/access/identity_providers.py">delete</a>(uuid, \*, account_or_zone, account_or_zone_id) -> <a href="./src/cloudflare/types/access/identity_provider_delete_response.py">IdentityProviderDeleteResponse</a></code>
- <code title="post /{account_or_zone}/{account_or_zone_id}/access/identity_providers">client.access.identity_providers.<a href="./src/cloudflare/resources/access/identity_providers.py">access_identity_providers_add_an_access_identity_provider</a>(account_or_zone_id, \*, account_or_zone, \*\*<a href="src/cloudflare/types/access/identity_provider_access_identity_providers_add_an_access_identity_provider_params.py">params</a>) -> <a href="./src/cloudflare/types/access/identity_provider_access_identity_providers_add_an_access_identity_provider_response.py">IdentityProviderAccessIdentityProvidersAddAnAccessIdentityProviderResponse</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/identity_providers">client.access.identity_providers.<a href="./src/cloudflare/resources/access/identity_providers.py">access_identity_providers_list_access_identity_providers</a>(account_or_zone_id, \*, account_or_zone) -> <a href="./src/cloudflare/types/access/identity_provider_access_identity_providers_list_access_identity_providers_response.py">Optional</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/identity_providers/{uuid}">client.access.identity_providers.<a href="./src/cloudflare/resources/access/identity_providers.py">get</a>(uuid, \*, account_or_zone, account_or_zone_id) -> <a href="./src/cloudflare/types/access/identity_provider_get_response.py">IdentityProviderGetResponse</a></code>

## Organizations

Types:

```python
from cloudflare.types.access import (
    OrganizationZeroTrustOrganizationCreateYourZeroTrustOrganizationResponse,
    OrganizationZeroTrustOrganizationGetYourZeroTrustOrganizationResponse,
    OrganizationZeroTrustOrganizationUpdateYourZeroTrustOrganizationResponse,
)
```

Methods:

- <code title="post /{account_or_zone}/{account_or_zone_id}/access/organizations">client.access.organizations.<a href="./src/cloudflare/resources/access/organizations/organizations.py">zero_trust_organization_create_your_zero_trust_organization</a>(account_or_zone_id, \*, account_or_zone, \*\*<a href="src/cloudflare/types/access/organization_zero_trust_organization_create_your_zero_trust_organization_params.py">params</a>) -> <a href="./src/cloudflare/types/access/organization_zero_trust_organization_create_your_zero_trust_organization_response.py">OrganizationZeroTrustOrganizationCreateYourZeroTrustOrganizationResponse</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/organizations">client.access.organizations.<a href="./src/cloudflare/resources/access/organizations/organizations.py">zero_trust_organization_get_your_zero_trust_organization</a>(account_or_zone_id, \*, account_or_zone) -> <a href="./src/cloudflare/types/access/organization_zero_trust_organization_get_your_zero_trust_organization_response.py">OrganizationZeroTrustOrganizationGetYourZeroTrustOrganizationResponse</a></code>
- <code title="put /{account_or_zone}/{account_or_zone_id}/access/organizations">client.access.organizations.<a href="./src/cloudflare/resources/access/organizations/organizations.py">zero_trust_organization_update_your_zero_trust_organization</a>(account_or_zone_id, \*, account_or_zone, \*\*<a href="src/cloudflare/types/access/organization_zero_trust_organization_update_your_zero_trust_organization_params.py">params</a>) -> <a href="./src/cloudflare/types/access/organization_zero_trust_organization_update_your_zero_trust_organization_response.py">OrganizationZeroTrustOrganizationUpdateYourZeroTrustOrganizationResponse</a></code>

### RevokeUsers

Types:

```python
from cloudflare.types.access.organizations import (
    RevokeUserZeroTrustOrganizationRevokeAllAccessTokensForAUserResponse,
)
```

Methods:

- <code title="post /{account_or_zone}/{account_or_zone_id}/access/organizations/revoke_user">client.access.organizations.revoke_users.<a href="./src/cloudflare/resources/access/organizations/revoke_users.py">zero_trust_organization_revoke_all_access_tokens_for_a_user</a>(account_or_zone_id, \*, account_or_zone, \*\*<a href="src/cloudflare/types/access/organizations/revoke_user_zero_trust_organization_revoke_all_access_tokens_for_a_user_params.py">params</a>) -> <a href="./src/cloudflare/types/access/organizations/revoke_user_zero_trust_organization_revoke_all_access_tokens_for_a_user_response.py">Optional</a></code>

## ServiceTokens

Types:

```python
from cloudflare.types.access import (
    ServiceTokenUpdateResponse,
    ServiceTokenDeleteResponse,
    ServiceTokenAccessServiceTokensCreateAServiceTokenResponse,
    ServiceTokenAccessServiceTokensListServiceTokensResponse,
)
```

Methods:

- <code title="put /{account_or_zone}/{account_or_zone_id}/access/service_tokens/{uuid}">client.access.service_tokens.<a href="./src/cloudflare/resources/access/service_tokens/service_tokens.py">update</a>(uuid, \*, account_or_zone, account_or_zone_id, \*\*<a href="src/cloudflare/types/access/service_token_update_params.py">params</a>) -> <a href="./src/cloudflare/types/access/service_token_update_response.py">ServiceTokenUpdateResponse</a></code>
- <code title="delete /{account_or_zone}/{account_or_zone_id}/access/service_tokens/{uuid}">client.access.service_tokens.<a href="./src/cloudflare/resources/access/service_tokens/service_tokens.py">delete</a>(uuid, \*, account_or_zone, account_or_zone_id) -> <a href="./src/cloudflare/types/access/service_token_delete_response.py">ServiceTokenDeleteResponse</a></code>
- <code title="post /{account_or_zone}/{account_or_zone_id}/access/service_tokens">client.access.service_tokens.<a href="./src/cloudflare/resources/access/service_tokens/service_tokens.py">access_service_tokens_create_a_service_token</a>(account_or_zone_id, \*, account_or_zone, \*\*<a href="src/cloudflare/types/access/service_token_access_service_tokens_create_a_service_token_params.py">params</a>) -> <a href="./src/cloudflare/types/access/service_token_access_service_tokens_create_a_service_token_response.py">ServiceTokenAccessServiceTokensCreateAServiceTokenResponse</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/service_tokens">client.access.service_tokens.<a href="./src/cloudflare/resources/access/service_tokens/service_tokens.py">access_service_tokens_list_service_tokens</a>(account_or_zone_id, \*, account_or_zone) -> <a href="./src/cloudflare/types/access/service_token_access_service_tokens_list_service_tokens_response.py">Optional</a></code>

### Refreshes

Types:

```python
from cloudflare.types.access.service_tokens import (
    RefreshAccessServiceTokensRefreshAServiceTokenResponse,
)
```

Methods:

- <code title="post /accounts/{identifier}/access/service_tokens/{uuid}/refresh">client.access.service_tokens.refreshes.<a href="./src/cloudflare/resources/access/service_tokens/refreshes.py">access_service_tokens_refresh_a_service_token</a>(uuid, \*, identifier) -> <a href="./src/cloudflare/types/access/service_tokens/refresh_access_service_tokens_refresh_a_service_token_response.py">RefreshAccessServiceTokensRefreshAServiceTokenResponse</a></code>

### Rotates

Types:

```python
from cloudflare.types.access.service_tokens import (
    RotateAccessServiceTokensRotateAServiceTokenResponse,
)
```

Methods:

- <code title="post /accounts/{identifier}/access/service_tokens/{uuid}/rotate">client.access.service_tokens.rotates.<a href="./src/cloudflare/resources/access/service_tokens/rotates.py">access_service_tokens_rotate_a_service_token</a>(uuid, \*, identifier) -> <a href="./src/cloudflare/types/access/service_tokens/rotate_access_service_tokens_rotate_a_service_token_response.py">RotateAccessServiceTokensRotateAServiceTokenResponse</a></code>

## Bookmarks

Types:

```python
from cloudflare.types.access import (
    BookmarkUpdateResponse,
    BookmarkDeleteResponse,
    BookmarkAccessBookmarkApplicationsDeprecatedListBookmarkApplicationsResponse,
    BookmarkGetResponse,
)
```

Methods:

- <code title="put /accounts/{identifier}/access/bookmarks/{uuid}">client.access.bookmarks.<a href="./src/cloudflare/resources/access/bookmarks.py">update</a>(uuid, \*, identifier) -> <a href="./src/cloudflare/types/access/bookmark_update_response.py">BookmarkUpdateResponse</a></code>
- <code title="delete /accounts/{identifier}/access/bookmarks/{uuid}">client.access.bookmarks.<a href="./src/cloudflare/resources/access/bookmarks.py">delete</a>(uuid, \*, identifier) -> <a href="./src/cloudflare/types/access/bookmark_delete_response.py">BookmarkDeleteResponse</a></code>
- <code title="get /accounts/{identifier}/access/bookmarks">client.access.bookmarks.<a href="./src/cloudflare/resources/access/bookmarks.py">access_bookmark_applications_deprecated_list_bookmark_applications</a>(identifier) -> <a href="./src/cloudflare/types/access/bookmark_access_bookmark_applications_deprecated_list_bookmark_applications_response.py">Optional</a></code>
- <code title="get /accounts/{identifier}/access/bookmarks/{uuid}">client.access.bookmarks.<a href="./src/cloudflare/resources/access/bookmarks.py">get</a>(uuid, \*, identifier) -> <a href="./src/cloudflare/types/access/bookmark_get_response.py">BookmarkGetResponse</a></code>

## Keys

Types:

```python
from cloudflare.types.access import (
    KeyAccessKeyConfigurationGetTheAccessKeyConfigurationResponse,
    KeyAccessKeyConfigurationUpdateTheAccessKeyConfigurationResponse,
)
```

Methods:

- <code title="get /accounts/{identifier}/access/keys">client.access.keys.<a href="./src/cloudflare/resources/access/keys/keys.py">access_key_configuration_get_the_access_key_configuration</a>(identifier) -> <a href="./src/cloudflare/types/access/key_access_key_configuration_get_the_access_key_configuration_response.py">KeyAccessKeyConfigurationGetTheAccessKeyConfigurationResponse</a></code>
- <code title="put /accounts/{identifier}/access/keys">client.access.keys.<a href="./src/cloudflare/resources/access/keys/keys.py">access_key_configuration_update_the_access_key_configuration</a>(identifier, \*\*<a href="src/cloudflare/types/access/key_access_key_configuration_update_the_access_key_configuration_params.py">params</a>) -> <a href="./src/cloudflare/types/access/key_access_key_configuration_update_the_access_key_configuration_response.py">KeyAccessKeyConfigurationUpdateTheAccessKeyConfigurationResponse</a></code>

### Rotates

Types:

```python
from cloudflare.types.access.keys import RotateAccessKeyConfigurationRotateAccessKeysResponse
```

Methods:

- <code title="post /accounts/{identifier}/access/keys/rotate">client.access.keys.rotates.<a href="./src/cloudflare/resources/access/keys/rotates.py">access_key_configuration_rotate_access_keys</a>(identifier) -> <a href="./src/cloudflare/types/access/keys/rotate_access_key_configuration_rotate_access_keys_response.py">RotateAccessKeyConfigurationRotateAccessKeysResponse</a></code>

## Logs

### AccessRequests

Types:

```python
from cloudflare.types.access.logs import (
    AccessRequestAccessAuthenticationLogsGetAccessAuthenticationLogsResponse,
)
```

Methods:

- <code title="get /accounts/{identifier}/access/logs/access_requests">client.access.logs.access_requests.<a href="./src/cloudflare/resources/access/logs/access_requests.py">access_authentication_logs_get_access_authentication_logs</a>(identifier) -> <a href="./src/cloudflare/types/access/logs/access_request_access_authentication_logs_get_access_authentication_logs_response.py">Optional</a></code>

## Seats

Types:

```python
from cloudflare.types.access import SeatZeroTrustSeatsUpdateAUserSeatResponse
```

Methods:

- <code title="patch /accounts/{identifier}/access/seats">client.access.seats.<a href="./src/cloudflare/resources/access/seats.py">zero_trust_seats_update_a_user_seat</a>(identifier, \*\*<a href="src/cloudflare/types/access/seat_zero_trust_seats_update_a_user_seat_params.py">params</a>) -> <a href="./src/cloudflare/types/access/seat_zero_trust_seats_update_a_user_seat_response.py">Optional</a></code>

## Users

Types:

```python
from cloudflare.types.access import UserListResponse
```

Methods:

- <code title="get /accounts/{identifier}/access/users">client.access.users.<a href="./src/cloudflare/resources/access/users/users.py">list</a>(identifier) -> <a href="./src/cloudflare/types/access/user_list_response.py">Optional</a></code>

### ActiveSessions

Types:

```python
from cloudflare.types.access.users import ActiveSessionListResponse, ActiveSessionGetResponse
```

Methods:

- <code title="get /accounts/{identifier}/access/users/{id}/active_sessions">client.access.users.active_sessions.<a href="./src/cloudflare/resources/access/users/active_sessions.py">list</a>(id, \*, identifier) -> <a href="./src/cloudflare/types/access/users/active_session_list_response.py">Optional</a></code>
- <code title="get /accounts/{identifier}/access/users/{id}/active_sessions/{nonce}">client.access.users.active_sessions.<a href="./src/cloudflare/resources/access/users/active_sessions.py">get</a>(nonce, \*, identifier, id) -> <a href="./src/cloudflare/types/access/users/active_session_get_response.py">ActiveSessionGetResponse</a></code>

### LastSeenIdentity

Types:

```python
from cloudflare.types.access.users import LastSeenIdentityGetResponse
```

Methods:

- <code title="get /accounts/{identifier}/access/users/{id}/last_seen_identity">client.access.users.last_seen_identity.<a href="./src/cloudflare/resources/access/users/last_seen_identity.py">get</a>(id, \*, identifier) -> <a href="./src/cloudflare/types/access/users/last_seen_identity_get_response.py">LastSeenIdentityGetResponse</a></code>

### FailedLogins

Types:

```python
from cloudflare.types.access.users import FailedLoginZeroTrustUsersGetFailedLoginsResponse
```

Methods:

- <code title="get /accounts/{identifier}/access/users/{id}/failed_logins">client.access.users.failed_logins.<a href="./src/cloudflare/resources/access/users/failed_logins.py">zero_trust_users_get_failed_logins</a>(id, \*, identifier) -> <a href="./src/cloudflare/types/access/users/failed_login_zero_trust_users_get_failed_logins_response.py">Optional</a></code>

## CustomPages

Types:

```python
from cloudflare.types.access import (
    CustomPageCreateResponse,
    CustomPageUpdateResponse,
    CustomPageListResponse,
    CustomPageDeleteResponse,
    CustomPageGetResponse,
)
```

Methods:

- <code title="post /accounts/{identifier}/access/custom_pages">client.access.custom_pages.<a href="./src/cloudflare/resources/access/custom_pages.py">create</a>(identifier, \*\*<a href="src/cloudflare/types/access/custom_page_create_params.py">params</a>) -> <a href="./src/cloudflare/types/access/custom_page_create_response.py">CustomPageCreateResponse</a></code>
- <code title="put /accounts/{identifier}/access/custom_pages/{uuid}">client.access.custom_pages.<a href="./src/cloudflare/resources/access/custom_pages.py">update</a>(uuid, \*, identifier, \*\*<a href="src/cloudflare/types/access/custom_page_update_params.py">params</a>) -> <a href="./src/cloudflare/types/access/custom_page_update_response.py">CustomPageUpdateResponse</a></code>
- <code title="get /accounts/{identifier}/access/custom_pages">client.access.custom_pages.<a href="./src/cloudflare/resources/access/custom_pages.py">list</a>(identifier) -> <a href="./src/cloudflare/types/access/custom_page_list_response.py">Optional</a></code>
- <code title="delete /accounts/{identifier}/access/custom_pages/{uuid}">client.access.custom_pages.<a href="./src/cloudflare/resources/access/custom_pages.py">delete</a>(uuid, \*, identifier) -> <a href="./src/cloudflare/types/access/custom_page_delete_response.py">CustomPageDeleteResponse</a></code>
- <code title="get /accounts/{identifier}/access/custom_pages/{uuid}">client.access.custom_pages.<a href="./src/cloudflare/resources/access/custom_pages.py">get</a>(uuid, \*, identifier) -> <a href="./src/cloudflare/types/access/custom_page_get_response.py">CustomPageGetResponse</a></code>

## Tags

Types:

```python
from cloudflare.types.access import TagListResponse
```

Methods:

- <code title="get /accounts/{identifier}/access/tags">client.access.tags.<a href="./src/cloudflare/resources/access/tags.py">list</a>(identifier) -> <a href="./src/cloudflare/types/access/tag_list_response.py">Optional</a></code>

# DNSAnalytics

## Reports

Types:

```python
from cloudflare.types.dns_analytics import ReportListResponse
```

Methods:

- <code title="get /zones/{identifier}/dns_analytics/report">client.dns_analytics.reports.<a href="./src/cloudflare/resources/dns_analytics/reports/reports.py">list</a>(identifier, \*\*<a href="src/cloudflare/types/dns_analytics/report_list_params.py">params</a>) -> <a href="./src/cloudflare/types/dns_analytics/report_list_response.py">ReportListResponse</a></code>

### Bytimes

Types:

```python
from cloudflare.types.dns_analytics.reports import BytimeListResponse
```

Methods:

- <code title="get /zones/{identifier}/dns_analytics/report/bytime">client.dns_analytics.reports.bytimes.<a href="./src/cloudflare/resources/dns_analytics/reports/bytimes.py">list</a>(identifier, \*\*<a href="src/cloudflare/types/dns_analytics/reports/bytime_list_params.py">params</a>) -> <a href="./src/cloudflare/types/dns_analytics/reports/bytime_list_response.py">BytimeListResponse</a></code>

# PurgeCaches

Types:

```python
from cloudflare.types import PurgeCachZonePurgeResponse
```

Methods:

- <code title="post /zones/{identifier}/purge_cache">client.purge_caches.<a href="./src/cloudflare/resources/purge_caches.py">zone_purge</a>(identifier, \*\*<a href="src/cloudflare/types/purge_cach_zone_purge_params.py">params</a>) -> <a href="./src/cloudflare/types/purge_cach_zone_purge_response.py">Optional</a></code>

# SSLs

## Analyzes

Types:

```python
from cloudflare.types.ssls import AnalyzeAnalyzeCertificateAnalyzeCertificateResponse
```

Methods:

- <code title="post /zones/{zone_id}/ssl/analyze">client.ssls.analyzes.<a href="./src/cloudflare/resources/ssls/analyzes.py">analyze_certificate_analyze_certificate</a>(zone_id, \*\*<a href="src/cloudflare/types/ssls/analyze_analyze_certificate_analyze_certificate_params.py">params</a>) -> <a href="./src/cloudflare/types/ssls/analyze_analyze_certificate_analyze_certificate_response.py">AnalyzeAnalyzeCertificateAnalyzeCertificateResponse</a></code>

## CertificatePacks

Types:

```python
from cloudflare.types.ssls import (
    CertificatePackUpdateResponse,
    CertificatePackDeleteResponse,
    CertificatePackCertificatePacksListCertificatePacksResponse,
    CertificatePackGetResponse,
)
```

Methods:

- <code title="patch /zones/{zone_id}/ssl/certificate_packs/{certificate_pack_id}">client.ssls.certificate_packs.<a href="./src/cloudflare/resources/ssls/certificate_packs/certificate_packs.py">update</a>(certificate_pack_id, \*, zone_id) -> <a href="./src/cloudflare/types/ssls/certificate_pack_update_response.py">CertificatePackUpdateResponse</a></code>
- <code title="delete /zones/{zone_id}/ssl/certificate_packs/{certificate_pack_id}">client.ssls.certificate_packs.<a href="./src/cloudflare/resources/ssls/certificate_packs/certificate_packs.py">delete</a>(certificate_pack_id, \*, zone_id) -> <a href="./src/cloudflare/types/ssls/certificate_pack_delete_response.py">CertificatePackDeleteResponse</a></code>
- <code title="get /zones/{zone_id}/ssl/certificate_packs">client.ssls.certificate_packs.<a href="./src/cloudflare/resources/ssls/certificate_packs/certificate_packs.py">certificate_packs_list_certificate_packs</a>(zone_id, \*\*<a href="src/cloudflare/types/ssls/certificate_pack_certificate_packs_list_certificate_packs_params.py">params</a>) -> <a href="./src/cloudflare/types/ssls/certificate_pack_certificate_packs_list_certificate_packs_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/ssl/certificate_packs/{certificate_pack_id}">client.ssls.certificate_packs.<a href="./src/cloudflare/resources/ssls/certificate_packs/certificate_packs.py">get</a>(certificate_pack_id, \*, zone_id) -> <a href="./src/cloudflare/types/ssls/certificate_pack_get_response.py">CertificatePackGetResponse</a></code>

### Orders

Types:

```python
from cloudflare.types.ssls.certificate_packs import (
    OrderCertificatePacksOrderAdvancedCertificateManagerCertificatePackResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/ssl/certificate_packs/order">client.ssls.certificate_packs.orders.<a href="./src/cloudflare/resources/ssls/certificate_packs/orders.py">certificate_packs_order_advanced_certificate_manager_certificate_pack</a>(zone_id, \*\*<a href="src/cloudflare/types/ssls/certificate_packs/order_certificate_packs_order_advanced_certificate_manager_certificate_pack_params.py">params</a>) -> <a href="./src/cloudflare/types/ssls/certificate_packs/order_certificate_packs_order_advanced_certificate_manager_certificate_pack_response.py">OrderCertificatePacksOrderAdvancedCertificateManagerCertificatePackResponse</a></code>

### Quotas

Types:

```python
from cloudflare.types.ssls.certificate_packs import (
    QuotaCertificatePacksGetCertificatePackQuotasResponse,
)
```

Methods:

- <code title="get /zones/{zone_id}/ssl/certificate_packs/quota">client.ssls.certificate_packs.quotas.<a href="./src/cloudflare/resources/ssls/certificate_packs/quotas.py">certificate_packs_get_certificate_pack_quotas</a>(zone_id) -> <a href="./src/cloudflare/types/ssls/certificate_packs/quota_certificate_packs_get_certificate_pack_quotas_response.py">QuotaCertificatePacksGetCertificatePackQuotasResponse</a></code>

## Recommendations

Types:

```python
from cloudflare.types.ssls import RecommendationListResponse
```

Methods:

- <code title="get /zones/{zone_identifier}/ssl/recommendation">client.ssls.recommendations.<a href="./src/cloudflare/resources/ssls/recommendations.py">list</a>(zone_identifier) -> <a href="./src/cloudflare/types/ssls/recommendation_list_response.py">Optional</a></code>

## Universals

### Settings

Types:

```python
from cloudflare.types.ssls.universals import SettingUpdateResponse, SettingGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/ssl/universal/settings">client.ssls.universals.settings.<a href="./src/cloudflare/resources/ssls/universals/settings.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/ssls/universals/setting_update_params.py">params</a>) -> <a href="./src/cloudflare/types/ssls/universals/setting_update_response.py">SettingUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/ssl/universal/settings">client.ssls.universals.settings.<a href="./src/cloudflare/resources/ssls/universals/settings.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/ssls/universals/setting_get_response.py">SettingGetResponse</a></code>

## Verifications

Types:

```python
from cloudflare.types.ssls import (
    VerificationUpdateResponse,
    VerificationSSLVerificationSSLVerificationDetailsResponse,
)
```

Methods:

- <code title="patch /zones/{zone_id}/ssl/verification/{certificate_pack_id}">client.ssls.verifications.<a href="./src/cloudflare/resources/ssls/verifications.py">update</a>(certificate_pack_id, \*, zone_id, \*\*<a href="src/cloudflare/types/ssls/verification_update_params.py">params</a>) -> <a href="./src/cloudflare/types/ssls/verification_update_response.py">VerificationUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/ssl/verification">client.ssls.verifications.<a href="./src/cloudflare/resources/ssls/verifications.py">ssl_verification_ssl_verification_details</a>(zone_id, \*\*<a href="src/cloudflare/types/ssls/verification_ssl_verification_ssl_verification_details_params.py">params</a>) -> <a href="./src/cloudflare/types/ssls/verification_ssl_verification_ssl_verification_details_response.py">Optional</a></code>

# Subscriptions

Types:

```python
from cloudflare.types import (
    SubscriptionUpdateResponse,
    SubscriptionDeleteResponse,
    SubscriptionAccountSubscriptionsCreateSubscriptionResponse,
    SubscriptionAccountSubscriptionsListSubscriptionsResponse,
    SubscriptionZoneSubscriptionCreateZoneSubscriptionResponse,
    SubscriptionZoneSubscriptionUpdateZoneSubscriptionResponse,
    SubscriptionZoneSubscriptionZoneSubscriptionDetailsResponse,
)
```

Methods:

- <code title="put /accounts/{account_identifier}/subscriptions/{subscription_identifier}">client.subscriptions.<a href="./src/cloudflare/resources/subscriptions.py">update</a>(subscription_identifier, \*, account_identifier, \*\*<a href="src/cloudflare/types/subscription_update_params.py">params</a>) -> <a href="./src/cloudflare/types/subscription_update_response.py">SubscriptionUpdateResponse</a></code>
- <code title="delete /accounts/{account_identifier}/subscriptions/{subscription_identifier}">client.subscriptions.<a href="./src/cloudflare/resources/subscriptions.py">delete</a>(subscription_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/subscription_delete_response.py">SubscriptionDeleteResponse</a></code>
- <code title="post /accounts/{account_identifier}/subscriptions">client.subscriptions.<a href="./src/cloudflare/resources/subscriptions.py">account_subscriptions_create_subscription</a>(account_identifier, \*\*<a href="src/cloudflare/types/subscription_account_subscriptions_create_subscription_params.py">params</a>) -> <a href="./src/cloudflare/types/subscription_account_subscriptions_create_subscription_response.py">SubscriptionAccountSubscriptionsCreateSubscriptionResponse</a></code>
- <code title="get /accounts/{account_identifier}/subscriptions">client.subscriptions.<a href="./src/cloudflare/resources/subscriptions.py">account_subscriptions_list_subscriptions</a>(account_identifier) -> <a href="./src/cloudflare/types/subscription_account_subscriptions_list_subscriptions_response.py">Optional</a></code>
- <code title="post /zones/{identifier}/subscription">client.subscriptions.<a href="./src/cloudflare/resources/subscriptions.py">zone_subscription_create_zone_subscription</a>(identifier, \*\*<a href="src/cloudflare/types/subscription_zone_subscription_create_zone_subscription_params.py">params</a>) -> <a href="./src/cloudflare/types/subscription_zone_subscription_create_zone_subscription_response.py">SubscriptionZoneSubscriptionCreateZoneSubscriptionResponse</a></code>
- <code title="put /zones/{identifier}/subscription">client.subscriptions.<a href="./src/cloudflare/resources/subscriptions.py">zone_subscription_update_zone_subscription</a>(identifier, \*\*<a href="src/cloudflare/types/subscription_zone_subscription_update_zone_subscription_params.py">params</a>) -> <a href="./src/cloudflare/types/subscription_zone_subscription_update_zone_subscription_response.py">SubscriptionZoneSubscriptionUpdateZoneSubscriptionResponse</a></code>
- <code title="get /zones/{identifier}/subscription">client.subscriptions.<a href="./src/cloudflare/resources/subscriptions.py">zone_subscription_zone_subscription_details</a>(identifier) -> <a href="./src/cloudflare/types/subscription_zone_subscription_zone_subscription_details_response.py">SubscriptionZoneSubscriptionZoneSubscriptionDetailsResponse</a></code>

# Acms

## TotalTLS

Types:

```python
from cloudflare.types.acms import TotalTLSUpdateResponse, TotalTLSGetResponse
```

Methods:

- <code title="post /zones/{zone_id}/acm/total_tls">client.acms.total_tls.<a href="./src/cloudflare/resources/acms/total_tls.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/acms/total_tls_update_params.py">params</a>) -> <a href="./src/cloudflare/types/acms/total_tls_update_response.py">TotalTLSUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/acm/total_tls">client.acms.total_tls.<a href="./src/cloudflare/resources/acms/total_tls.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/acms/total_tls_get_response.py">TotalTLSGetResponse</a></code>

# Analytics

## Colo

Types:

```python
from cloudflare.types.analytics import ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponse
```

Methods:

- <code title="get /zones/{zone_identifier}/analytics/colos">client.analytics.colo.<a href="./src/cloudflare/resources/analytics/colo.py">zone_analytics_deprecated_get_analytics_by_co_locations</a>(zone_identifier, \*\*<a href="src/cloudflare/types/analytics/colo_zone_analytics_deprecated_get_analytics_by_co_locations_params.py">params</a>) -> <a href="./src/cloudflare/types/analytics/colo_zone_analytics_deprecated_get_analytics_by_co_locations_response.py">ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponse</a></code>

## Dashboards

Types:

```python
from cloudflare.types.analytics import DashboardZoneAnalyticsDeprecatedGetDashboardResponse
```

Methods:

- <code title="get /zones/{zone_identifier}/analytics/dashboard">client.analytics.dashboards.<a href="./src/cloudflare/resources/analytics/dashboards.py">zone_analytics_deprecated_get_dashboard</a>(zone_identifier, \*\*<a href="src/cloudflare/types/analytics/dashboard_zone_analytics_deprecated_get_dashboard_params.py">params</a>) -> <a href="./src/cloudflare/types/analytics/dashboard_zone_analytics_deprecated_get_dashboard_response.py">DashboardZoneAnalyticsDeprecatedGetDashboardResponse</a></code>

## Latencies

Types:

```python
from cloudflare.types.analytics import LatencyArgoAnalyticsForZoneArgoAnalyticsForAZoneResponse
```

Methods:

- <code title="get /zones/{zone_id}/analytics/latency">client.analytics.latencies.<a href="./src/cloudflare/resources/analytics/latencies/latencies.py">argo_analytics_for_zone_argo_analytics_for_a_zone</a>(zone_id, \*\*<a href="src/cloudflare/types/analytics/latency_argo_analytics_for_zone_argo_analytics_for_a_zone_params.py">params</a>) -> <a href="./src/cloudflare/types/analytics/latency_argo_analytics_for_zone_argo_analytics_for_a_zone_response.py">LatencyArgoAnalyticsForZoneArgoAnalyticsForAZoneResponse</a></code>

### Colos

Types:

```python
from cloudflare.types.analytics.latencies import (
    ColoArgoAnalyticsForGeolocationArgoAnalyticsForAZoneAtDifferentPoPsResponse,
)
```

Methods:

- <code title="get /zones/{zone_id}/analytics/latency/colos">client.analytics.latencies.colos.<a href="./src/cloudflare/resources/analytics/latencies/colos.py">argo_analytics_for_geolocation_argo_analytics_for_a_zone_at_different_po_ps</a>(zone_id) -> <a href="./src/cloudflare/types/analytics/latencies/colo_argo_analytics_for_geolocation_argo_analytics_for_a_zone_at_different_po_ps_response.py">ColoArgoAnalyticsForGeolocationArgoAnalyticsForAZoneAtDifferentPoPsResponse</a></code>

# Argo

## SmartRouting

Types:

```python
from cloudflare.types.argo import SmartRoutingUpdateResponse, SmartRoutingGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/argo/smart_routing">client.argo.smart_routing.<a href="./src/cloudflare/resources/argo/smart_routing.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/argo/smart_routing_update_params.py">params</a>) -> <a href="./src/cloudflare/types/argo/smart_routing_update_response.py">SmartRoutingUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/argo/smart_routing">client.argo.smart_routing.<a href="./src/cloudflare/resources/argo/smart_routing.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/argo/smart_routing_get_response.py">SmartRoutingGetResponse</a></code>

## TieredCaching

Types:

```python
from cloudflare.types.argo import (
    TieredCachingTieredCachingGetTieredCachingSettingResponse,
    TieredCachingTieredCachingPatchTieredCachingSettingResponse,
)
```

Methods:

- <code title="get /zones/{zone_id}/argo/tiered_caching">client.argo.tiered_caching.<a href="./src/cloudflare/resources/argo/tiered_caching.py">tiered_caching_get_tiered_caching_setting</a>(zone_id) -> <a href="./src/cloudflare/types/argo/tiered_caching_tiered_caching_get_tiered_caching_setting_response.py">TieredCachingTieredCachingGetTieredCachingSettingResponse</a></code>
- <code title="patch /zones/{zone_id}/argo/tiered_caching">client.argo.tiered_caching.<a href="./src/cloudflare/resources/argo/tiered_caching.py">tiered_caching_patch_tiered_caching_setting</a>(zone_id, \*\*<a href="src/cloudflare/types/argo/tiered_caching_tiered_caching_patch_tiered_caching_setting_params.py">params</a>) -> <a href="./src/cloudflare/types/argo/tiered_caching_tiered_caching_patch_tiered_caching_setting_response.py">TieredCachingTieredCachingPatchTieredCachingSettingResponse</a></code>

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
from cloudflare.types import AvailableRatePlanZoneRatePlanListAvailableRatePlansResponse
```

Methods:

- <code title="get /zones/{zone_identifier}/available_rate_plans">client.available_rate_plans.<a href="./src/cloudflare/resources/available_rate_plans.py">zone_rate_plan_list_available_rate_plans</a>(zone_identifier) -> <a href="./src/cloudflare/types/available_rate_plan_zone_rate_plan_list_available_rate_plans_response.py">Optional</a></code>

# Caches

## CacheReserves

Types:

```python
from cloudflare.types.caches import (
    CacheReserveListResponse,
    CacheReserveZoneCacheSettingsChangeCacheReserveSettingResponse,
)
```

Methods:

- <code title="get /zones/{zone_id}/cache/cache_reserve">client.caches.cache_reserves.<a href="./src/cloudflare/resources/caches/cache_reserves.py">list</a>(zone_id) -> <a href="./src/cloudflare/types/caches/cache_reserve_list_response.py">CacheReserveListResponse</a></code>
- <code title="patch /zones/{zone_id}/cache/cache_reserve">client.caches.cache_reserves.<a href="./src/cloudflare/resources/caches/cache_reserves.py">zone_cache_settings_change_cache_reserve_setting</a>(zone_id, \*\*<a href="src/cloudflare/types/caches/cache_reserve_zone_cache_settings_change_cache_reserve_setting_params.py">params</a>) -> <a href="./src/cloudflare/types/caches/cache_reserve_zone_cache_settings_change_cache_reserve_setting_response.py">CacheReserveZoneCacheSettingsChangeCacheReserveSettingResponse</a></code>

## TieredCacheSmartTopologyEnables

Types:

```python
from cloudflare.types.caches import (
    TieredCacheSmartTopologyEnableDeleteResponse,
    TieredCacheSmartTopologyEnableSmartTieredCacheGetSmartTieredCacheSettingResponse,
    TieredCacheSmartTopologyEnableSmartTieredCachePatchSmartTieredCacheSettingResponse,
)
```

Methods:

- <code title="delete /zones/{zone_id}/cache/tiered_cache_smart_topology_enable">client.caches.tiered_cache_smart_topology_enables.<a href="./src/cloudflare/resources/caches/tiered_cache_smart_topology_enables.py">delete</a>(zone_id) -> <a href="./src/cloudflare/types/caches/tiered_cache_smart_topology_enable_delete_response.py">TieredCacheSmartTopologyEnableDeleteResponse</a></code>
- <code title="get /zones/{zone_id}/cache/tiered_cache_smart_topology_enable">client.caches.tiered_cache_smart_topology_enables.<a href="./src/cloudflare/resources/caches/tiered_cache_smart_topology_enables.py">smart_tiered_cache_get_smart_tiered_cache_setting</a>(zone_id) -> <a href="./src/cloudflare/types/caches/tiered_cache_smart_topology_enable_smart_tiered_cache_get_smart_tiered_cache_setting_response.py">TieredCacheSmartTopologyEnableSmartTieredCacheGetSmartTieredCacheSettingResponse</a></code>
- <code title="patch /zones/{zone_id}/cache/tiered_cache_smart_topology_enable">client.caches.tiered_cache_smart_topology_enables.<a href="./src/cloudflare/resources/caches/tiered_cache_smart_topology_enables.py">smart_tiered_cache_patch_smart_tiered_cache_setting</a>(zone_id, \*\*<a href="src/cloudflare/types/caches/tiered_cache_smart_topology_enable_smart_tiered_cache_patch_smart_tiered_cache_setting_params.py">params</a>) -> <a href="./src/cloudflare/types/caches/tiered_cache_smart_topology_enable_smart_tiered_cache_patch_smart_tiered_cache_setting_response.py">TieredCacheSmartTopologyEnableSmartTieredCachePatchSmartTieredCacheSettingResponse</a></code>

## Variants

Types:

```python
from cloudflare.types.caches import (
    VariantListResponse,
    VariantDeleteResponse,
    VariantZoneCacheSettingsChangeVariantsSettingResponse,
)
```

Methods:

- <code title="get /zones/{zone_id}/cache/variants">client.caches.variants.<a href="./src/cloudflare/resources/caches/variants.py">list</a>(zone_id) -> <a href="./src/cloudflare/types/caches/variant_list_response.py">VariantListResponse</a></code>
- <code title="delete /zones/{zone_id}/cache/variants">client.caches.variants.<a href="./src/cloudflare/resources/caches/variants.py">delete</a>(zone_id) -> <a href="./src/cloudflare/types/caches/variant_delete_response.py">VariantDeleteResponse</a></code>
- <code title="patch /zones/{zone_id}/cache/variants">client.caches.variants.<a href="./src/cloudflare/resources/caches/variants.py">zone_cache_settings_change_variants_setting</a>(zone_id, \*\*<a href="src/cloudflare/types/caches/variant_zone_cache_settings_change_variants_setting_params.py">params</a>) -> <a href="./src/cloudflare/types/caches/variant_zone_cache_settings_change_variants_setting_response.py">VariantZoneCacheSettingsChangeVariantsSettingResponse</a></code>

# CertificateAuthorities

## HostnameAssociations

Types:

```python
from cloudflare.types.certificate_authorities import (
    HostnameAssociationClientCertificateForAZoneListHostnameAssociationsResponse,
    HostnameAssociationClientCertificateForAZonePutHostnameAssociationsResponse,
)
```

Methods:

- <code title="get /zones/{zone_id}/certificate_authorities/hostname_associations">client.certificate_authorities.hostname_associations.<a href="./src/cloudflare/resources/certificate_authorities/hostname_associations.py">client_certificate_for_a_zone_list_hostname_associations</a>(zone_id, \*\*<a href="src/cloudflare/types/certificate_authorities/hostname_association_client_certificate_for_a_zone_list_hostname_associations_params.py">params</a>) -> <a href="./src/cloudflare/types/certificate_authorities/hostname_association_client_certificate_for_a_zone_list_hostname_associations_response.py">HostnameAssociationClientCertificateForAZoneListHostnameAssociationsResponse</a></code>
- <code title="put /zones/{zone_id}/certificate_authorities/hostname_associations">client.certificate_authorities.hostname_associations.<a href="./src/cloudflare/resources/certificate_authorities/hostname_associations.py">client_certificate_for_a_zone_put_hostname_associations</a>(zone_id, \*\*<a href="src/cloudflare/types/certificate_authorities/hostname_association_client_certificate_for_a_zone_put_hostname_associations_params.py">params</a>) -> <a href="./src/cloudflare/types/certificate_authorities/hostname_association_client_certificate_for_a_zone_put_hostname_associations_response.py">HostnameAssociationClientCertificateForAZonePutHostnameAssociationsResponse</a></code>

# ClientCertificates

Types:

```python
from cloudflare.types import (
    ClientCertificateUpdateResponse,
    ClientCertificateDeleteResponse,
    ClientCertificateClientCertificateForAZoneCreateClientCertificateResponse,
    ClientCertificateClientCertificateForAZoneListClientCertificatesResponse,
    ClientCertificateGetResponse,
)
```

Methods:

- <code title="patch /zones/{zone_id}/client_certificates/{client_certificate_id}">client.client_certificates.<a href="./src/cloudflare/resources/client_certificates.py">update</a>(client_certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/client_certificate_update_response.py">ClientCertificateUpdateResponse</a></code>
- <code title="delete /zones/{zone_id}/client_certificates/{client_certificate_id}">client.client_certificates.<a href="./src/cloudflare/resources/client_certificates.py">delete</a>(client_certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/client_certificate_delete_response.py">ClientCertificateDeleteResponse</a></code>
- <code title="post /zones/{zone_id}/client_certificates">client.client_certificates.<a href="./src/cloudflare/resources/client_certificates.py">client_certificate_for_a_zone_create_client_certificate</a>(zone_id, \*\*<a href="src/cloudflare/types/client_certificate_client_certificate_for_a_zone_create_client_certificate_params.py">params</a>) -> <a href="./src/cloudflare/types/client_certificate_client_certificate_for_a_zone_create_client_certificate_response.py">ClientCertificateClientCertificateForAZoneCreateClientCertificateResponse</a></code>
- <code title="get /zones/{zone_id}/client_certificates">client.client_certificates.<a href="./src/cloudflare/resources/client_certificates.py">client_certificate_for_a_zone_list_client_certificates</a>(zone_id, \*\*<a href="src/cloudflare/types/client_certificate_client_certificate_for_a_zone_list_client_certificates_params.py">params</a>) -> <a href="./src/cloudflare/types/client_certificate_client_certificate_for_a_zone_list_client_certificates_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/client_certificates/{client_certificate_id}">client.client_certificates.<a href="./src/cloudflare/resources/client_certificates.py">get</a>(client_certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/client_certificate_get_response.py">ClientCertificateGetResponse</a></code>

# CustomCertificates

Types:

```python
from cloudflare.types import (
    CustomCertificateCreateResponse,
    CustomCertificateUpdateResponse,
    CustomCertificateListResponse,
    CustomCertificateDeleteResponse,
    CustomCertificateGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/custom_certificates">client.custom_certificates.<a href="./src/cloudflare/resources/custom_certificates/custom_certificates.py">create</a>(zone_id, \*\*<a href="src/cloudflare/types/custom_certificate_create_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_certificate_create_response.py">CustomCertificateCreateResponse</a></code>
- <code title="patch /zones/{zone_id}/custom_certificates/{custom_certificate_id}">client.custom_certificates.<a href="./src/cloudflare/resources/custom_certificates/custom_certificates.py">update</a>(custom_certificate_id, \*, zone_id, \*\*<a href="src/cloudflare/types/custom_certificate_update_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_certificate_update_response.py">CustomCertificateUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/custom_certificates">client.custom_certificates.<a href="./src/cloudflare/resources/custom_certificates/custom_certificates.py">list</a>(zone_id, \*\*<a href="src/cloudflare/types/custom_certificate_list_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_certificate_list_response.py">Optional</a></code>
- <code title="delete /zones/{zone_id}/custom_certificates/{custom_certificate_id}">client.custom_certificates.<a href="./src/cloudflare/resources/custom_certificates/custom_certificates.py">delete</a>(custom_certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/custom_certificate_delete_response.py">CustomCertificateDeleteResponse</a></code>
- <code title="get /zones/{zone_id}/custom_certificates/{custom_certificate_id}">client.custom_certificates.<a href="./src/cloudflare/resources/custom_certificates/custom_certificates.py">get</a>(custom_certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/custom_certificate_get_response.py">CustomCertificateGetResponse</a></code>

## Prioritizes

Types:

```python
from cloudflare.types.custom_certificates import (
    PrioritizeCustomSSLForAZoneRePrioritizeSSLCertificatesResponse,
)
```

Methods:

- <code title="put /zones/{zone_id}/custom_certificates/prioritize">client.custom_certificates.prioritizes.<a href="./src/cloudflare/resources/custom_certificates/prioritizes.py">custom_ssl_for_a_zone_re_prioritize_ssl_certificates</a>(zone_id, \*\*<a href="src/cloudflare/types/custom_certificates/prioritize_custom_ssl_for_a_zone_re_prioritize_ssl_certificates_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_certificates/prioritize_custom_ssl_for_a_zone_re_prioritize_ssl_certificates_response.py">Optional</a></code>

# CustomHostnames

Types:

```python
from cloudflare.types import (
    CustomHostnameUpdateResponse,
    CustomHostnameDeleteResponse,
    CustomHostnameCustomHostnameForAZoneCreateCustomHostnameResponse,
    CustomHostnameCustomHostnameForAZoneListCustomHostnamesResponse,
    CustomHostnameGetResponse,
)
```

Methods:

- <code title="patch /zones/{zone_id}/custom_hostnames/{custom_hostname_id}">client.custom_hostnames.<a href="./src/cloudflare/resources/custom_hostnames/custom_hostnames.py">update</a>(custom_hostname_id, \*, zone_id, \*\*<a href="src/cloudflare/types/custom_hostname_update_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_hostname_update_response.py">CustomHostnameUpdateResponse</a></code>
- <code title="delete /zones/{zone_id}/custom_hostnames/{custom_hostname_id}">client.custom_hostnames.<a href="./src/cloudflare/resources/custom_hostnames/custom_hostnames.py">delete</a>(custom_hostname_id, \*, zone_id) -> <a href="./src/cloudflare/types/custom_hostname_delete_response.py">CustomHostnameDeleteResponse</a></code>
- <code title="post /zones/{zone_id}/custom_hostnames">client.custom_hostnames.<a href="./src/cloudflare/resources/custom_hostnames/custom_hostnames.py">custom_hostname_for_a_zone_create_custom_hostname</a>(zone_id, \*\*<a href="src/cloudflare/types/custom_hostname_custom_hostname_for_a_zone_create_custom_hostname_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_hostname_custom_hostname_for_a_zone_create_custom_hostname_response.py">CustomHostnameCustomHostnameForAZoneCreateCustomHostnameResponse</a></code>
- <code title="get /zones/{zone_id}/custom_hostnames">client.custom_hostnames.<a href="./src/cloudflare/resources/custom_hostnames/custom_hostnames.py">custom_hostname_for_a_zone_list_custom_hostnames</a>(zone_id, \*\*<a href="src/cloudflare/types/custom_hostname_custom_hostname_for_a_zone_list_custom_hostnames_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_hostname_custom_hostname_for_a_zone_list_custom_hostnames_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/custom_hostnames/{custom_hostname_id}">client.custom_hostnames.<a href="./src/cloudflare/resources/custom_hostnames/custom_hostnames.py">get</a>(custom_hostname_id, \*, zone_id) -> <a href="./src/cloudflare/types/custom_hostname_get_response.py">CustomHostnameGetResponse</a></code>

## FallbackOrigins

Types:

```python
from cloudflare.types.custom_hostnames import (
    FallbackOriginUpdateResponse,
    FallbackOriginDeleteResponse,
    FallbackOriginGetResponse,
)
```

Methods:

- <code title="put /zones/{zone_id}/custom_hostnames/fallback_origin">client.custom_hostnames.fallback_origins.<a href="./src/cloudflare/resources/custom_hostnames/fallback_origins.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/custom_hostnames/fallback_origin_update_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_hostnames/fallback_origin_update_response.py">FallbackOriginUpdateResponse</a></code>
- <code title="delete /zones/{zone_id}/custom_hostnames/fallback_origin">client.custom_hostnames.fallback_origins.<a href="./src/cloudflare/resources/custom_hostnames/fallback_origins.py">delete</a>(zone_id) -> <a href="./src/cloudflare/types/custom_hostnames/fallback_origin_delete_response.py">FallbackOriginDeleteResponse</a></code>
- <code title="get /zones/{zone_id}/custom_hostnames/fallback_origin">client.custom_hostnames.fallback_origins.<a href="./src/cloudflare/resources/custom_hostnames/fallback_origins.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/custom_hostnames/fallback_origin_get_response.py">FallbackOriginGetResponse</a></code>

# CustomNs

## Availabilities

Types:

```python
from cloudflare.types.custom_ns import AvailabilityGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/custom_ns/availability">client.custom_ns.availabilities.<a href="./src/cloudflare/resources/custom_ns/availabilities.py">get</a>(account_id) -> <a href="./src/cloudflare/types/custom_ns/availability_get_response.py">Optional</a></code>

## Verifies

Types:

```python
from cloudflare.types.custom_ns import VerifyUpdateResponse
```

Methods:

- <code title="post /accounts/{account_id}/custom_ns/verify">client.custom_ns.verifies.<a href="./src/cloudflare/resources/custom_ns/verifies.py">update</a>(account_id) -> <a href="./src/cloudflare/types/custom_ns/verify_update_response.py">Optional</a></code>

# DNSRecords

Types:

```python
from cloudflare.types import (
    DNSRecordCreateResponse,
    DNSRecordUpdateResponse,
    DNSRecordListResponse,
    DNSRecordDeleteResponse,
    DNSRecordExportResponse,
    DNSRecordGetResponse,
    DNSRecordImportResponse,
    DNSRecordScanResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/dns_records">client.dns_records.<a href="./src/cloudflare/resources/dns_records.py">create</a>(zone_id, \*\*<a href="src/cloudflare/types/dns_record_create_params.py">params</a>) -> <a href="./src/cloudflare/types/dns_record_create_response.py">DNSRecordCreateResponse</a></code>
- <code title="put /zones/{zone_id}/dns_records/{dns_record_id}">client.dns_records.<a href="./src/cloudflare/resources/dns_records.py">update</a>(dns_record_id, \*, zone_id, \*\*<a href="src/cloudflare/types/dns_record_update_params.py">params</a>) -> <a href="./src/cloudflare/types/dns_record_update_response.py">DNSRecordUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/dns_records">client.dns_records.<a href="./src/cloudflare/resources/dns_records.py">list</a>(zone_id, \*\*<a href="src/cloudflare/types/dns_record_list_params.py">params</a>) -> <a href="./src/cloudflare/types/dns_record_list_response.py">Optional</a></code>
- <code title="delete /zones/{zone_id}/dns_records/{dns_record_id}">client.dns_records.<a href="./src/cloudflare/resources/dns_records.py">delete</a>(dns_record_id, \*, zone_id) -> <a href="./src/cloudflare/types/dns_record_delete_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/dns_records/export">client.dns_records.<a href="./src/cloudflare/resources/dns_records.py">export</a>(zone_id) -> str</code>
- <code title="get /zones/{zone_id}/dns_records/{dns_record_id}">client.dns_records.<a href="./src/cloudflare/resources/dns_records.py">get</a>(dns_record_id, \*, zone_id) -> <a href="./src/cloudflare/types/dns_record_get_response.py">DNSRecordGetResponse</a></code>
- <code title="post /zones/{zone_id}/dns_records/import">client.dns*records.<a href="./src/cloudflare/resources/dns_records.py">import*</a>(zone_id, \*\*<a href="src/cloudflare/types/dns_record_import_params.py">params</a>) -> <a href="./src/cloudflare/types/dns_record_import_response.py">DNSRecordImportResponse</a></code>
- <code title="post /zones/{zone_id}/dns_records/scan">client.dns_records.<a href="./src/cloudflare/resources/dns_records.py">scan</a>(zone_id) -> <a href="./src/cloudflare/types/dns_record_scan_response.py">DNSRecordScanResponse</a></code>

# DNSSECs

Types:

```python
from cloudflare.types import DNSSECUpdateResponse, DNSSECGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/dnssec">client.dnssecs.<a href="./src/cloudflare/resources/dnssecs.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/dnssec_update_params.py">params</a>) -> <a href="./src/cloudflare/types/dnssec_update_response.py">DNSSECUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/dnssec">client.dnssecs.<a href="./src/cloudflare/resources/dnssecs.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/dnssec_get_response.py">DNSSECGetResponse</a></code>

# Emails

## Routings

Types:

```python
from cloudflare.types.emails import RoutingEmailRoutingSettingsGetEmailRoutingSettingsResponse
```

Methods:

- <code title="get /zones/{zone_identifier}/email/routing">client.emails.routings.<a href="./src/cloudflare/resources/emails/routings/routings.py">email_routing_settings_get_email_routing_settings</a>(zone_identifier) -> <a href="./src/cloudflare/types/emails/routing_email_routing_settings_get_email_routing_settings_response.py">RoutingEmailRoutingSettingsGetEmailRoutingSettingsResponse</a></code>

### Disables

Types:

```python
from cloudflare.types.emails.routings import DisableEmailRoutingSettingsDisableEmailRoutingResponse
```

Methods:

- <code title="post /zones/{zone_identifier}/email/routing/disable">client.emails.routings.disables.<a href="./src/cloudflare/resources/emails/routings/disables.py">email_routing_settings_disable_email_routing</a>(zone_identifier) -> <a href="./src/cloudflare/types/emails/routings/disable_email_routing_settings_disable_email_routing_response.py">DisableEmailRoutingSettingsDisableEmailRoutingResponse</a></code>

### DNS

Types:

```python
from cloudflare.types.emails.routings import DNSEmailRoutingSettingsEmailRoutingDNSSettingsResponse
```

Methods:

- <code title="get /zones/{zone_identifier}/email/routing/dns">client.emails.routings.dns.<a href="./src/cloudflare/resources/emails/routings/dns.py">email_routing_settings_email_routing_dns_settings</a>(zone_identifier) -> <a href="./src/cloudflare/types/emails/routings/dns_email_routing_settings_email_routing_dns_settings_response.py">Optional</a></code>

### Enables

Types:

```python
from cloudflare.types.emails.routings import EnableEmailRoutingSettingsEnableEmailRoutingResponse
```

Methods:

- <code title="post /zones/{zone_identifier}/email/routing/enable">client.emails.routings.enables.<a href="./src/cloudflare/resources/emails/routings/enables.py">email_routing_settings_enable_email_routing</a>(zone_identifier) -> <a href="./src/cloudflare/types/emails/routings/enable_email_routing_settings_enable_email_routing_response.py">EnableEmailRoutingSettingsEnableEmailRoutingResponse</a></code>

### Rules

Types:

```python
from cloudflare.types.emails.routings import (
    RuleUpdateResponse,
    RuleDeleteResponse,
    RuleEmailRoutingRoutingRulesCreateRoutingRuleResponse,
    RuleEmailRoutingRoutingRulesListRoutingRulesResponse,
    RuleGetResponse,
)
```

Methods:

- <code title="put /zones/{zone_identifier}/email/routing/rules/{rule_identifier}">client.emails.routings.rules.<a href="./src/cloudflare/resources/emails/routings/rules/rules.py">update</a>(rule_identifier, \*, zone_identifier, \*\*<a href="src/cloudflare/types/emails/routings/rule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/emails/routings/rule_update_response.py">RuleUpdateResponse</a></code>
- <code title="delete /zones/{zone_identifier}/email/routing/rules/{rule_identifier}">client.emails.routings.rules.<a href="./src/cloudflare/resources/emails/routings/rules/rules.py">delete</a>(rule_identifier, \*, zone_identifier) -> <a href="./src/cloudflare/types/emails/routings/rule_delete_response.py">RuleDeleteResponse</a></code>
- <code title="post /zones/{zone_identifier}/email/routing/rules">client.emails.routings.rules.<a href="./src/cloudflare/resources/emails/routings/rules/rules.py">email_routing_routing_rules_create_routing_rule</a>(zone_identifier, \*\*<a href="src/cloudflare/types/emails/routings/rule_email_routing_routing_rules_create_routing_rule_params.py">params</a>) -> <a href="./src/cloudflare/types/emails/routings/rule_email_routing_routing_rules_create_routing_rule_response.py">RuleEmailRoutingRoutingRulesCreateRoutingRuleResponse</a></code>
- <code title="get /zones/{zone_identifier}/email/routing/rules">client.emails.routings.rules.<a href="./src/cloudflare/resources/emails/routings/rules/rules.py">email_routing_routing_rules_list_routing_rules</a>(zone_identifier, \*\*<a href="src/cloudflare/types/emails/routings/rule_email_routing_routing_rules_list_routing_rules_params.py">params</a>) -> <a href="./src/cloudflare/types/emails/routings/rule_email_routing_routing_rules_list_routing_rules_response.py">Optional</a></code>
- <code title="get /zones/{zone_identifier}/email/routing/rules/{rule_identifier}">client.emails.routings.rules.<a href="./src/cloudflare/resources/emails/routings/rules/rules.py">get</a>(rule_identifier, \*, zone_identifier) -> <a href="./src/cloudflare/types/emails/routings/rule_get_response.py">RuleGetResponse</a></code>

#### CatchAlls

Types:

```python
from cloudflare.types.emails.routings.rules import (
    CatchAllEmailRoutingRoutingRulesGetCatchAllRuleResponse,
    CatchAllEmailRoutingRoutingRulesUpdateCatchAllRuleResponse,
)
```

Methods:

- <code title="get /zones/{zone_identifier}/email/routing/rules/catch_all">client.emails.routings.rules.catch_alls.<a href="./src/cloudflare/resources/emails/routings/rules/catch_alls.py">email_routing_routing_rules_get_catch_all_rule</a>(zone_identifier) -> <a href="./src/cloudflare/types/emails/routings/rules/catch_all_email_routing_routing_rules_get_catch_all_rule_response.py">CatchAllEmailRoutingRoutingRulesGetCatchAllRuleResponse</a></code>
- <code title="put /zones/{zone_identifier}/email/routing/rules/catch_all">client.emails.routings.rules.catch_alls.<a href="./src/cloudflare/resources/emails/routings/rules/catch_alls.py">email_routing_routing_rules_update_catch_all_rule</a>(zone_identifier, \*\*<a href="src/cloudflare/types/emails/routings/rules/catch_all_email_routing_routing_rules_update_catch_all_rule_params.py">params</a>) -> <a href="./src/cloudflare/types/emails/routings/rules/catch_all_email_routing_routing_rules_update_catch_all_rule_response.py">CatchAllEmailRoutingRoutingRulesUpdateCatchAllRuleResponse</a></code>

### Addresses

Types:

```python
from cloudflare.types.emails.routings import (
    AddressDeleteResponse,
    AddressEmailRoutingDestinationAddressesCreateADestinationAddressResponse,
    AddressEmailRoutingDestinationAddressesListDestinationAddressesResponse,
    AddressGetResponse,
)
```

Methods:

- <code title="delete /accounts/{account_identifier}/email/routing/addresses/{destination_address_identifier}">client.emails.routings.addresses.<a href="./src/cloudflare/resources/emails/routings/addresses.py">delete</a>(destination_address_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/emails/routings/address_delete_response.py">AddressDeleteResponse</a></code>
- <code title="post /accounts/{account_identifier}/email/routing/addresses">client.emails.routings.addresses.<a href="./src/cloudflare/resources/emails/routings/addresses.py">email_routing_destination_addresses_create_a_destination_address</a>(account_identifier, \*\*<a href="src/cloudflare/types/emails/routings/address_email_routing_destination_addresses_create_a_destination_address_params.py">params</a>) -> <a href="./src/cloudflare/types/emails/routings/address_email_routing_destination_addresses_create_a_destination_address_response.py">AddressEmailRoutingDestinationAddressesCreateADestinationAddressResponse</a></code>
- <code title="get /accounts/{account_identifier}/email/routing/addresses">client.emails.routings.addresses.<a href="./src/cloudflare/resources/emails/routings/addresses.py">email_routing_destination_addresses_list_destination_addresses</a>(account_identifier, \*\*<a href="src/cloudflare/types/emails/routings/address_email_routing_destination_addresses_list_destination_addresses_params.py">params</a>) -> <a href="./src/cloudflare/types/emails/routings/address_email_routing_destination_addresses_list_destination_addresses_response.py">Optional</a></code>
- <code title="get /accounts/{account_identifier}/email/routing/addresses/{destination_address_identifier}">client.emails.routings.addresses.<a href="./src/cloudflare/resources/emails/routings/addresses.py">get</a>(destination_address_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/emails/routings/address_get_response.py">AddressGetResponse</a></code>

# Filters

Types:

```python
from cloudflare.types import (
    FilterUpdateResponse,
    FilterDeleteResponse,
    FilterFiltersCreateFiltersResponse,
    FilterFiltersListFiltersResponse,
    FilterFiltersUpdateFiltersResponse,
    FilterGetResponse,
)
```

Methods:

- <code title="put /zones/{zone_identifier}/filters/{id}">client.filters.<a href="./src/cloudflare/resources/filters.py">update</a>(id, \*, zone_identifier, \*\*<a href="src/cloudflare/types/filter_update_params.py">params</a>) -> <a href="./src/cloudflare/types/filter_update_response.py">Optional</a></code>
- <code title="delete /zones/{zone_identifier}/filters/{id}">client.filters.<a href="./src/cloudflare/resources/filters.py">delete</a>(id, \*, zone_identifier) -> <a href="./src/cloudflare/types/filter_delete_response.py">Optional</a></code>
- <code title="post /zones/{zone_identifier}/filters">client.filters.<a href="./src/cloudflare/resources/filters.py">filters_create_filters</a>(zone_identifier, \*\*<a href="src/cloudflare/types/filter_filters_create_filters_params.py">params</a>) -> <a href="./src/cloudflare/types/filter_filters_create_filters_response.py">Optional</a></code>
- <code title="get /zones/{zone_identifier}/filters">client.filters.<a href="./src/cloudflare/resources/filters.py">filters_list_filters</a>(zone_identifier, \*\*<a href="src/cloudflare/types/filter_filters_list_filters_params.py">params</a>) -> <a href="./src/cloudflare/types/filter_filters_list_filters_response.py">Optional</a></code>
- <code title="put /zones/{zone_identifier}/filters">client.filters.<a href="./src/cloudflare/resources/filters.py">filters_update_filters</a>(zone_identifier, \*\*<a href="src/cloudflare/types/filter_filters_update_filters_params.py">params</a>) -> <a href="./src/cloudflare/types/filter_filters_update_filters_response.py">Optional</a></code>
- <code title="get /zones/{zone_identifier}/filters/{id}">client.filters.<a href="./src/cloudflare/resources/filters.py">get</a>(id, \*, zone_identifier) -> <a href="./src/cloudflare/types/filter_get_response.py">Optional</a></code>

# Firewalls

## Lockdowns

Types:

```python
from cloudflare.types.firewalls import (
    LockdownUpdateResponse,
    LockdownDeleteResponse,
    LockdownGetResponse,
    LockdownZoneLockdownCreateAZoneLockdownRuleResponse,
    LockdownZoneLockdownListZoneLockdownRulesResponse,
)
```

Methods:

- <code title="put /zones/{zone_identifier}/firewall/lockdowns/{id}">client.firewalls.lockdowns.<a href="./src/cloudflare/resources/firewalls/lockdowns.py">update</a>(id, \*, zone_identifier, \*\*<a href="src/cloudflare/types/firewalls/lockdown_update_params.py">params</a>) -> <a href="./src/cloudflare/types/firewalls/lockdown_update_response.py">Optional</a></code>
- <code title="delete /zones/{zone_identifier}/firewall/lockdowns/{id}">client.firewalls.lockdowns.<a href="./src/cloudflare/resources/firewalls/lockdowns.py">delete</a>(id, \*, zone_identifier) -> <a href="./src/cloudflare/types/firewalls/lockdown_delete_response.py">Optional</a></code>
- <code title="get /zones/{zone_identifier}/firewall/lockdowns/{id}">client.firewalls.lockdowns.<a href="./src/cloudflare/resources/firewalls/lockdowns.py">get</a>(id, \*, zone_identifier) -> <a href="./src/cloudflare/types/firewalls/lockdown_get_response.py">Optional</a></code>
- <code title="post /zones/{zone_identifier}/firewall/lockdowns">client.firewalls.lockdowns.<a href="./src/cloudflare/resources/firewalls/lockdowns.py">zone_lockdown_create_a_zone_lockdown_rule</a>(zone_identifier, \*\*<a href="src/cloudflare/types/firewalls/lockdown_zone_lockdown_create_a_zone_lockdown_rule_params.py">params</a>) -> <a href="./src/cloudflare/types/firewalls/lockdown_zone_lockdown_create_a_zone_lockdown_rule_response.py">Optional</a></code>
- <code title="get /zones/{zone_identifier}/firewall/lockdowns">client.firewalls.lockdowns.<a href="./src/cloudflare/resources/firewalls/lockdowns.py">zone_lockdown_list_zone_lockdown_rules</a>(zone_identifier, \*\*<a href="src/cloudflare/types/firewalls/lockdown_zone_lockdown_list_zone_lockdown_rules_params.py">params</a>) -> <a href="./src/cloudflare/types/firewalls/lockdown_zone_lockdown_list_zone_lockdown_rules_response.py">Optional</a></code>

## Rules

Types:

```python
from cloudflare.types.firewalls import (
    RuleUpdateResponse,
    RuleDeleteResponse,
    RuleFirewallRulesCreateFirewallRulesResponse,
    RuleFirewallRulesListFirewallRulesResponse,
    RuleFirewallRulesUpdateFirewallRulesResponse,
    RuleFirewallRulesUpdatePriorityOfFirewallRulesResponse,
    RuleGetResponse,
)
```

Methods:

- <code title="put /zones/{zone_identifier}/firewall/rules/{id}">client.firewalls.rules.<a href="./src/cloudflare/resources/firewalls/rules.py">update</a>(id, \*, zone_identifier, \*\*<a href="src/cloudflare/types/firewalls/rule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/firewalls/rule_update_response.py">Optional</a></code>
- <code title="delete /zones/{zone_identifier}/firewall/rules/{id}">client.firewalls.rules.<a href="./src/cloudflare/resources/firewalls/rules.py">delete</a>(id, \*, zone_identifier, \*\*<a href="src/cloudflare/types/firewalls/rule_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/firewalls/rule_delete_response.py">Optional</a></code>
- <code title="post /zones/{zone_identifier}/firewall/rules">client.firewalls.rules.<a href="./src/cloudflare/resources/firewalls/rules.py">firewall_rules_create_firewall_rules</a>(zone_identifier, \*\*<a href="src/cloudflare/types/firewalls/rule_firewall_rules_create_firewall_rules_params.py">params</a>) -> <a href="./src/cloudflare/types/firewalls/rule_firewall_rules_create_firewall_rules_response.py">Optional</a></code>
- <code title="get /zones/{zone_identifier}/firewall/rules">client.firewalls.rules.<a href="./src/cloudflare/resources/firewalls/rules.py">firewall_rules_list_firewall_rules</a>(zone_identifier, \*\*<a href="src/cloudflare/types/firewalls/rule_firewall_rules_list_firewall_rules_params.py">params</a>) -> <a href="./src/cloudflare/types/firewalls/rule_firewall_rules_list_firewall_rules_response.py">Optional</a></code>
- <code title="put /zones/{zone_identifier}/firewall/rules">client.firewalls.rules.<a href="./src/cloudflare/resources/firewalls/rules.py">firewall_rules_update_firewall_rules</a>(zone_identifier, \*\*<a href="src/cloudflare/types/firewalls/rule_firewall_rules_update_firewall_rules_params.py">params</a>) -> <a href="./src/cloudflare/types/firewalls/rule_firewall_rules_update_firewall_rules_response.py">Optional</a></code>
- <code title="patch /zones/{zone_identifier}/firewall/rules">client.firewalls.rules.<a href="./src/cloudflare/resources/firewalls/rules.py">firewall_rules_update_priority_of_firewall_rules</a>(zone_identifier, \*\*<a href="src/cloudflare/types/firewalls/rule_firewall_rules_update_priority_of_firewall_rules_params.py">params</a>) -> <a href="./src/cloudflare/types/firewalls/rule_firewall_rules_update_priority_of_firewall_rules_response.py">Optional</a></code>
- <code title="get /zones/{zone_identifier}/firewall/rules/{id}">client.firewalls.rules.<a href="./src/cloudflare/resources/firewalls/rules.py">get</a>(id, \*, zone_identifier) -> <a href="./src/cloudflare/types/firewalls/rule_get_response.py">Optional</a></code>

## AccessRules

Types:

```python
from cloudflare.types.firewalls import (
    AccessRuleCreateResponse,
    AccessRuleUpdateResponse,
    AccessRuleListResponse,
    AccessRuleDeleteResponse,
    AccessRuleGetResponse,
)
```

Methods:

- <code title="post /{account_or_zone}/{account_or_zone_id}/firewall/access_rules/rules">client.firewalls.access_rules.<a href="./src/cloudflare/resources/firewalls/access_rules.py">create</a>(account_or_zone_id, \*, account_or_zone, \*\*<a href="src/cloudflare/types/firewalls/access_rule_create_params.py">params</a>) -> <a href="./src/cloudflare/types/firewalls/access_rule_create_response.py">Optional</a></code>
- <code title="patch /{account_or_zone}/{account_or_zone_id}/firewall/access_rules/rules/{identifier}">client.firewalls.access_rules.<a href="./src/cloudflare/resources/firewalls/access_rules.py">update</a>(identifier, \*, account_identifier, \*\*<a href="src/cloudflare/types/firewalls/access_rule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/firewalls/access_rule_update_response.py">Optional</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/firewall/access_rules/rules">client.firewalls.access_rules.<a href="./src/cloudflare/resources/firewalls/access_rules.py">list</a>(account_or_zone_id, \*, account_or_zone, \*\*<a href="src/cloudflare/types/firewalls/access_rule_list_params.py">params</a>) -> <a href="./src/cloudflare/types/firewalls/access_rule_list_response.py">Optional</a></code>
- <code title="delete /{account_or_zone}/{account_or_zone_id}/firewall/access_rules/rules/{identifier}">client.firewalls.access_rules.<a href="./src/cloudflare/resources/firewalls/access_rules.py">delete</a>(identifier, \*, account_or_zone, account_or_zone_id) -> <a href="./src/cloudflare/types/firewalls/access_rule_delete_response.py">Optional</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/firewall/access_rules/rules/{identifier}">client.firewalls.access_rules.<a href="./src/cloudflare/resources/firewalls/access_rules.py">get</a>(identifier, \*, account_or_zone, account_or_zone_id) -> <a href="./src/cloudflare/types/firewalls/access_rule_get_response.py">Optional</a></code>

## UaRules

Types:

```python
from cloudflare.types.firewalls import (
    UaRuleUpdateResponse,
    UaRuleDeleteResponse,
    UaRuleGetResponse,
    UaRuleUserAgentBlockingRulesCreateAUserAgentBlockingRuleResponse,
    UaRuleUserAgentBlockingRulesListUserAgentBlockingRulesResponse,
)
```

Methods:

- <code title="put /zones/{zone_identifier}/firewall/ua_rules/{id}">client.firewalls.ua_rules.<a href="./src/cloudflare/resources/firewalls/ua_rules.py">update</a>(id, \*, zone_identifier, \*\*<a href="src/cloudflare/types/firewalls/ua_rule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/firewalls/ua_rule_update_response.py">Optional</a></code>
- <code title="delete /zones/{zone_identifier}/firewall/ua_rules/{id}">client.firewalls.ua_rules.<a href="./src/cloudflare/resources/firewalls/ua_rules.py">delete</a>(id, \*, zone_identifier) -> <a href="./src/cloudflare/types/firewalls/ua_rule_delete_response.py">Optional</a></code>
- <code title="get /zones/{zone_identifier}/firewall/ua_rules/{id}">client.firewalls.ua_rules.<a href="./src/cloudflare/resources/firewalls/ua_rules.py">get</a>(id, \*, zone_identifier) -> <a href="./src/cloudflare/types/firewalls/ua_rule_get_response.py">Optional</a></code>
- <code title="post /zones/{zone_identifier}/firewall/ua_rules">client.firewalls.ua_rules.<a href="./src/cloudflare/resources/firewalls/ua_rules.py">user_agent_blocking_rules_create_a_user_agent_blocking_rule</a>(zone_identifier, \*\*<a href="src/cloudflare/types/firewalls/ua_rule_user_agent_blocking_rules_create_a_user_agent_blocking_rule_params.py">params</a>) -> <a href="./src/cloudflare/types/firewalls/ua_rule_user_agent_blocking_rules_create_a_user_agent_blocking_rule_response.py">Optional</a></code>
- <code title="get /zones/{zone_identifier}/firewall/ua_rules">client.firewalls.ua_rules.<a href="./src/cloudflare/resources/firewalls/ua_rules.py">user_agent_blocking_rules_list_user_agent_blocking_rules</a>(zone_identifier, \*\*<a href="src/cloudflare/types/firewalls/ua_rule_user_agent_blocking_rules_list_user_agent_blocking_rules_params.py">params</a>) -> <a href="./src/cloudflare/types/firewalls/ua_rule_user_agent_blocking_rules_list_user_agent_blocking_rules_response.py">Optional</a></code>

## WAF

### Overrides

Types:

```python
from cloudflare.types.firewalls.waf import (
    OverrideUpdateResponse,
    OverrideDeleteResponse,
    OverrideGetResponse,
    OverrideWAFOverridesCreateAWAFOverrideResponse,
    OverrideWAFOverridesListWAFOverridesResponse,
)
```

Methods:

- <code title="put /zones/{zone_identifier}/firewall/waf/overrides/{id}">client.firewalls.waf.overrides.<a href="./src/cloudflare/resources/firewalls/waf/overrides.py">update</a>(id, \*, zone_identifier, \*\*<a href="src/cloudflare/types/firewalls/waf/override_update_params.py">params</a>) -> <a href="./src/cloudflare/types/firewalls/waf/override_update_response.py">Optional</a></code>
- <code title="delete /zones/{zone_identifier}/firewall/waf/overrides/{id}">client.firewalls.waf.overrides.<a href="./src/cloudflare/resources/firewalls/waf/overrides.py">delete</a>(id, \*, zone_identifier) -> <a href="./src/cloudflare/types/firewalls/waf/override_delete_response.py">Optional</a></code>
- <code title="get /zones/{zone_identifier}/firewall/waf/overrides/{id}">client.firewalls.waf.overrides.<a href="./src/cloudflare/resources/firewalls/waf/overrides.py">get</a>(id, \*, zone_identifier) -> <a href="./src/cloudflare/types/firewalls/waf/override_get_response.py">Optional</a></code>
- <code title="post /zones/{zone_identifier}/firewall/waf/overrides">client.firewalls.waf.overrides.<a href="./src/cloudflare/resources/firewalls/waf/overrides.py">waf_overrides_create_a_waf_override</a>(zone_identifier, \*\*<a href="src/cloudflare/types/firewalls/waf/override_waf_overrides_create_a_waf_override_params.py">params</a>) -> <a href="./src/cloudflare/types/firewalls/waf/override_waf_overrides_create_a_waf_override_response.py">Optional</a></code>
- <code title="get /zones/{zone_identifier}/firewall/waf/overrides">client.firewalls.waf.overrides.<a href="./src/cloudflare/resources/firewalls/waf/overrides.py">waf_overrides_list_waf_overrides</a>(zone_identifier, \*\*<a href="src/cloudflare/types/firewalls/waf/override_waf_overrides_list_waf_overrides_params.py">params</a>) -> <a href="./src/cloudflare/types/firewalls/waf/override_waf_overrides_list_waf_overrides_response.py">Optional</a></code>

### Packages

Types:

```python
from cloudflare.types.firewalls.waf import PackageListResponse, PackageGetResponse
```

Methods:

- <code title="get /zones/{zone_identifier}/firewall/waf/packages">client.firewalls.waf.packages.<a href="./src/cloudflare/resources/firewalls/waf/packages/packages.py">list</a>(zone_identifier, \*\*<a href="src/cloudflare/types/firewalls/waf/package_list_params.py">params</a>) -> <a href="./src/cloudflare/types/firewalls/waf/package_list_response.py">PackageListResponse</a></code>
- <code title="get /zones/{zone_identifier}/firewall/waf/packages/{identifier}">client.firewalls.waf.packages.<a href="./src/cloudflare/resources/firewalls/waf/packages/packages.py">get</a>(identifier, \*, zone_identifier) -> <a href="./src/cloudflare/types/firewalls/waf/package_get_response.py">PackageGetResponse</a></code>

#### Groups

Types:

```python
from cloudflare.types.firewalls.waf.packages import (
    GroupUpdateResponse,
    GroupGetResponse,
    GroupWAFRuleGroupsListWAFRuleGroupsResponse,
)
```

Methods:

- <code title="patch /zones/{zone_id}/firewall/waf/packages/{package_id}/groups/{group_id}">client.firewalls.waf.packages.groups.<a href="./src/cloudflare/resources/firewalls/waf/packages/groups.py">update</a>(group_id, \*, zone_id, package_id, \*\*<a href="src/cloudflare/types/firewalls/waf/packages/group_update_params.py">params</a>) -> <a href="./src/cloudflare/types/firewalls/waf/packages/group_update_response.py">GroupUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/firewall/waf/packages/{package_id}/groups/{group_id}">client.firewalls.waf.packages.groups.<a href="./src/cloudflare/resources/firewalls/waf/packages/groups.py">get</a>(group_id, \*, zone_id, package_id) -> <a href="./src/cloudflare/types/firewalls/waf/packages/group_get_response.py">GroupGetResponse</a></code>
- <code title="get /zones/{zone_id}/firewall/waf/packages/{package_id}/groups">client.firewalls.waf.packages.groups.<a href="./src/cloudflare/resources/firewalls/waf/packages/groups.py">waf_rule_groups_list_waf_rule_groups</a>(package_id, \*, zone_id, \*\*<a href="src/cloudflare/types/firewalls/waf/packages/group_waf_rule_groups_list_waf_rule_groups_params.py">params</a>) -> <a href="./src/cloudflare/types/firewalls/waf/packages/group_waf_rule_groups_list_waf_rule_groups_response.py">Optional</a></code>

#### Rules

Types:

```python
from cloudflare.types.firewalls.waf.packages import (
    RuleUpdateResponse,
    RuleGetResponse,
    RuleWAFRulesListWAFRulesResponse,
)
```

Methods:

- <code title="patch /zones/{zone_id}/firewall/waf/packages/{package_id}/rules/{rule_id}">client.firewalls.waf.packages.rules.<a href="./src/cloudflare/resources/firewalls/waf/packages/rules.py">update</a>(rule_id, \*, zone_id, package_id, \*\*<a href="src/cloudflare/types/firewalls/waf/packages/rule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/firewalls/waf/packages/rule_update_response.py">RuleUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/firewall/waf/packages/{package_id}/rules/{rule_id}">client.firewalls.waf.packages.rules.<a href="./src/cloudflare/resources/firewalls/waf/packages/rules.py">get</a>(rule_id, \*, zone_id, package_id) -> <a href="./src/cloudflare/types/firewalls/waf/packages/rule_get_response.py">RuleGetResponse</a></code>
- <code title="get /zones/{zone_id}/firewall/waf/packages/{package_id}/rules">client.firewalls.waf.packages.rules.<a href="./src/cloudflare/resources/firewalls/waf/packages/rules.py">waf_rules_list_waf_rules</a>(package_id, \*, zone_id, \*\*<a href="src/cloudflare/types/firewalls/waf/packages/rule_waf_rules_list_waf_rules_params.py">params</a>) -> <a href="./src/cloudflare/types/firewalls/waf/packages/rule_waf_rules_list_waf_rules_response.py">Optional</a></code>

# Healthchecks

Types:

```python
from cloudflare.types import (
    HealthcheckUpdateResponse,
    HealthcheckDeleteResponse,
    HealthcheckGetResponse,
    HealthcheckHealthChecksCreateHealthCheckResponse,
    HealthcheckHealthChecksListHealthChecksResponse,
)
```

Methods:

- <code title="put /zones/{zone_identifier}/healthchecks/{identifier}">client.healthchecks.<a href="./src/cloudflare/resources/healthchecks/healthchecks.py">update</a>(identifier, \*, zone_identifier, \*\*<a href="src/cloudflare/types/healthcheck_update_params.py">params</a>) -> <a href="./src/cloudflare/types/healthcheck_update_response.py">HealthcheckUpdateResponse</a></code>
- <code title="delete /zones/{zone_identifier}/healthchecks/{identifier}">client.healthchecks.<a href="./src/cloudflare/resources/healthchecks/healthchecks.py">delete</a>(identifier, \*, zone_identifier) -> <a href="./src/cloudflare/types/healthcheck_delete_response.py">HealthcheckDeleteResponse</a></code>
- <code title="get /zones/{zone_identifier}/healthchecks/{identifier}">client.healthchecks.<a href="./src/cloudflare/resources/healthchecks/healthchecks.py">get</a>(identifier, \*, zone_identifier) -> <a href="./src/cloudflare/types/healthcheck_get_response.py">HealthcheckGetResponse</a></code>
- <code title="post /zones/{zone_identifier}/healthchecks">client.healthchecks.<a href="./src/cloudflare/resources/healthchecks/healthchecks.py">health_checks_create_health_check</a>(zone_identifier, \*\*<a href="src/cloudflare/types/healthcheck_health_checks_create_health_check_params.py">params</a>) -> <a href="./src/cloudflare/types/healthcheck_health_checks_create_health_check_response.py">HealthcheckHealthChecksCreateHealthCheckResponse</a></code>
- <code title="get /zones/{zone_identifier}/healthchecks">client.healthchecks.<a href="./src/cloudflare/resources/healthchecks/healthchecks.py">health_checks_list_health_checks</a>(zone_identifier) -> <a href="./src/cloudflare/types/healthcheck_health_checks_list_health_checks_response.py">Optional</a></code>

## Previews

Types:

```python
from cloudflare.types.healthchecks import (
    PreviewDeleteResponse,
    PreviewGetResponse,
    PreviewHealthChecksCreatePreviewHealthCheckResponse,
)
```

Methods:

- <code title="delete /zones/{zone_identifier}/healthchecks/preview/{identifier}">client.healthchecks.previews.<a href="./src/cloudflare/resources/healthchecks/previews.py">delete</a>(identifier, \*, zone_identifier) -> <a href="./src/cloudflare/types/healthchecks/preview_delete_response.py">PreviewDeleteResponse</a></code>
- <code title="get /zones/{zone_identifier}/healthchecks/preview/{identifier}">client.healthchecks.previews.<a href="./src/cloudflare/resources/healthchecks/previews.py">get</a>(identifier, \*, zone_identifier) -> <a href="./src/cloudflare/types/healthchecks/preview_get_response.py">PreviewGetResponse</a></code>
- <code title="post /zones/{zone_identifier}/healthchecks/preview">client.healthchecks.previews.<a href="./src/cloudflare/resources/healthchecks/previews.py">health_checks_create_preview_health_check</a>(zone_identifier, \*\*<a href="src/cloudflare/types/healthchecks/preview_health_checks_create_preview_health_check_params.py">params</a>) -> <a href="./src/cloudflare/types/healthchecks/preview_health_checks_create_preview_health_check_response.py">PreviewHealthChecksCreatePreviewHealthCheckResponse</a></code>

# KeylessCertificates

Types:

```python
from cloudflare.types import (
    KeylessCertificateCreateResponse,
    KeylessCertificateUpdateResponse,
    KeylessCertificateListResponse,
    KeylessCertificateDeleteResponse,
    KeylessCertificateGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/keyless_certificates">client.keyless_certificates.<a href="./src/cloudflare/resources/keyless_certificates.py">create</a>(zone_id, \*\*<a href="src/cloudflare/types/keyless_certificate_create_params.py">params</a>) -> <a href="./src/cloudflare/types/keyless_certificate_create_response.py">KeylessCertificateCreateResponse</a></code>
- <code title="patch /zones/{zone_id}/keyless_certificates/{keyless_certificate_id}">client.keyless_certificates.<a href="./src/cloudflare/resources/keyless_certificates.py">update</a>(keyless_certificate_id, \*, zone_id, \*\*<a href="src/cloudflare/types/keyless_certificate_update_params.py">params</a>) -> <a href="./src/cloudflare/types/keyless_certificate_update_response.py">KeylessCertificateUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/keyless_certificates">client.keyless_certificates.<a href="./src/cloudflare/resources/keyless_certificates.py">list</a>(zone_id) -> <a href="./src/cloudflare/types/keyless_certificate_list_response.py">Optional</a></code>
- <code title="delete /zones/{zone_id}/keyless_certificates/{keyless_certificate_id}">client.keyless_certificates.<a href="./src/cloudflare/resources/keyless_certificates.py">delete</a>(keyless_certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/keyless_certificate_delete_response.py">KeylessCertificateDeleteResponse</a></code>
- <code title="get /zones/{zone_id}/keyless_certificates/{keyless_certificate_id}">client.keyless_certificates.<a href="./src/cloudflare/resources/keyless_certificates.py">get</a>(keyless_certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/keyless_certificate_get_response.py">KeylessCertificateGetResponse</a></code>

# Logpush

## Datasets

### Fields

Types:

```python
from cloudflare.types.logpush.datasets import FieldListResponse
```

Methods:

- <code title="get /{account_or_zone}/{account_or_zone_id}/logpush/datasets/{dataset_id}/fields">client.logpush.datasets.fields.<a href="./src/cloudflare/resources/logpush/datasets/fields.py">list</a>(dataset_id, \*, account_or_zone, account_or_zone_id) -> <a href="./src/cloudflare/types/logpush/datasets/field_list_response.py">object</a></code>

### Jobs

Types:

```python
from cloudflare.types.logpush.datasets import JobListResponse
```

Methods:

- <code title="get /{account_or_zone}/{account_or_zone_id}/logpush/datasets/{dataset_id}/jobs">client.logpush.datasets.jobs.<a href="./src/cloudflare/resources/logpush/datasets/jobs.py">list</a>(dataset_id, \*, account_or_zone, account_or_zone_id) -> <a href="./src/cloudflare/types/logpush/datasets/job_list_response.py">JobListResponse</a></code>

## Edges

Types:

```python
from cloudflare.types.logpush import EdgeUpdateResponse, EdgeGetResponse
```

Methods:

- <code title="post /zones/{zone_id}/logpush/edge">client.logpush.edges.<a href="./src/cloudflare/resources/logpush/edges.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/logpush/edge_update_params.py">params</a>) -> <a href="./src/cloudflare/types/logpush/edge_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/logpush/edge">client.logpush.edges.<a href="./src/cloudflare/resources/logpush/edges.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/logpush/edge_get_response.py">EdgeGetResponse</a></code>

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

- <code title="post /{account_or_zone}/{account_or_zone_id}/logpush/jobs">client.logpush.jobs.<a href="./src/cloudflare/resources/logpush/jobs.py">create</a>(account_or_zone_id, \*, account_or_zone, \*\*<a href="src/cloudflare/types/logpush/job_create_params.py">params</a>) -> <a href="./src/cloudflare/types/logpush/job_create_response.py">Optional</a></code>
- <code title="put /{account_or_zone}/{account_or_zone_id}/logpush/jobs/{job_id}">client.logpush.jobs.<a href="./src/cloudflare/resources/logpush/jobs.py">update</a>(job_id, \*, account_or_zone, account_or_zone_id, \*\*<a href="src/cloudflare/types/logpush/job_update_params.py">params</a>) -> <a href="./src/cloudflare/types/logpush/job_update_response.py">Optional</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/logpush/jobs">client.logpush.jobs.<a href="./src/cloudflare/resources/logpush/jobs.py">list</a>(account_or_zone_id, \*, account_or_zone) -> <a href="./src/cloudflare/types/logpush/job_list_response.py">JobListResponse</a></code>
- <code title="delete /{account_or_zone}/{account_or_zone_id}/logpush/jobs/{job_id}">client.logpush.jobs.<a href="./src/cloudflare/resources/logpush/jobs.py">delete</a>(job_id, \*, account_or_zone, account_or_zone_id) -> <a href="./src/cloudflare/types/logpush/job_delete_response.py">Optional</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/logpush/jobs/{job_id}">client.logpush.jobs.<a href="./src/cloudflare/resources/logpush/jobs.py">get</a>(job_id, \*, account_or_zone, account_or_zone_id) -> <a href="./src/cloudflare/types/logpush/job_get_response.py">Optional</a></code>

## Ownerships

Types:

```python
from cloudflare.types.logpush import OwnershipPostAccountsAccountIdentifierLogpushOwnershipResponse
```

Methods:

- <code title="post /{account_or_zone}/{account_or_zone_id}/logpush/ownership">client.logpush.ownerships.<a href="./src/cloudflare/resources/logpush/ownerships/ownerships.py">post_accounts_account_identifier_logpush_ownership</a>(account_or_zone_id, \*, account_or_zone, \*\*<a href="src/cloudflare/types/logpush/ownership_post_accounts_account_identifier_logpush_ownership_params.py">params</a>) -> <a href="./src/cloudflare/types/logpush/ownership_post_accounts_account_identifier_logpush_ownership_response.py">Optional</a></code>

### Validates

Types:

```python
from cloudflare.types.logpush.ownerships import (
    ValidatePostAccountsAccountIdentifierLogpushOwnershipValidateResponse,
)
```

Methods:

- <code title="post /{account_or_zone}/{account_or_zone_id}/logpush/ownership/validate">client.logpush.ownerships.validates.<a href="./src/cloudflare/resources/logpush/ownerships/validates.py">post_accounts_account_identifier_logpush_ownership_validate</a>(account_or_zone_id, \*, account_or_zone, \*\*<a href="src/cloudflare/types/logpush/ownerships/validate_post_accounts_account_identifier_logpush_ownership_validate_params.py">params</a>) -> <a href="./src/cloudflare/types/logpush/ownerships/validate_post_accounts_account_identifier_logpush_ownership_validate_response.py">Optional</a></code>

## Validates

### Destinations

#### Exists

Types:

```python
from cloudflare.types.logpush.validates.destinations import (
    ExistDeleteAccountsAccountIdentifierLogpushValidateDestinationExistsResponse,
)
```

Methods:

- <code title="post /{account_or_zone}/{account_or_zone_id}/logpush/validate/destination/exists">client.logpush.validates.destinations.exists.<a href="./src/cloudflare/resources/logpush/validates/destinations/exists.py">delete_accounts_account_identifier_logpush_validate_destination_exists</a>(account_or_zone_id, \*, account_or_zone, \*\*<a href="src/cloudflare/types/logpush/validates/destinations/exist_delete_accounts_account_identifier_logpush_validate_destination_exists_params.py">params</a>) -> <a href="./src/cloudflare/types/logpush/validates/destinations/exist_delete_accounts_account_identifier_logpush_validate_destination_exists_response.py">Optional</a></code>

### Origins

Types:

```python
from cloudflare.types.logpush.validates import (
    OriginPostAccountsAccountIdentifierLogpushValidateOriginResponse,
)
```

Methods:

- <code title="post /{account_or_zone}/{account_or_zone_id}/logpush/validate/origin">client.logpush.validates.origins.<a href="./src/cloudflare/resources/logpush/validates/origins.py">post_accounts_account_identifier_logpush_validate_origin</a>(account_or_zone_id, \*, account_or_zone, \*\*<a href="src/cloudflare/types/logpush/validates/origin_post_accounts_account_identifier_logpush_validate_origin_params.py">params</a>) -> <a href="./src/cloudflare/types/logpush/validates/origin_post_accounts_account_identifier_logpush_validate_origin_response.py">Optional</a></code>

# Logs

## Controls

### Retentions

#### Flags

Types:

```python
from cloudflare.types.logs.controls.retentions import (
    FlagLogsReceivedGetLogRetentionFlagResponse,
    FlagLogsReceivedUpdateLogRetentionFlagResponse,
)
```

Methods:

- <code title="get /zones/{zone_identifier}/logs/control/retention/flag">client.logs.controls.retentions.flags.<a href="./src/cloudflare/resources/logs/controls/retentions/flags.py">logs_received_get_log_retention_flag</a>(zone_identifier) -> <a href="./src/cloudflare/types/logs/controls/retentions/flag_logs_received_get_log_retention_flag_response.py">FlagLogsReceivedGetLogRetentionFlagResponse</a></code>
- <code title="post /zones/{zone_identifier}/logs/control/retention/flag">client.logs.controls.retentions.flags.<a href="./src/cloudflare/resources/logs/controls/retentions/flags.py">logs_received_update_log_retention_flag</a>(zone_identifier, \*\*<a href="src/cloudflare/types/logs/controls/retentions/flag_logs_received_update_log_retention_flag_params.py">params</a>) -> <a href="./src/cloudflare/types/logs/controls/retentions/flag_logs_received_update_log_retention_flag_response.py">FlagLogsReceivedUpdateLogRetentionFlagResponse</a></code>

### Cmb

#### Configs

Types:

```python
from cloudflare.types.logs.controls.cmb import (
    ConfigDeleteResponse,
    ConfigGetAccountsAccountIdentifierLogsControlCmbConfigResponse,
    ConfigPutAccountsAccountIdentifierLogsControlCmbConfigResponse,
)
```

Methods:

- <code title="delete /accounts/{account_id}/logs/control/cmb/config">client.logs.controls.cmb.configs.<a href="./src/cloudflare/resources/logs/controls/cmb/configs.py">delete</a>(account_id) -> <a href="./src/cloudflare/types/logs/controls/cmb/config_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/logs/control/cmb/config">client.logs.controls.cmb.configs.<a href="./src/cloudflare/resources/logs/controls/cmb/configs.py">get_accounts_account_identifier_logs_control_cmb_config</a>(account_id) -> <a href="./src/cloudflare/types/logs/controls/cmb/config_get_accounts_account_identifier_logs_control_cmb_config_response.py">Optional</a></code>
- <code title="post /accounts/{account_id}/logs/control/cmb/config">client.logs.controls.cmb.configs.<a href="./src/cloudflare/resources/logs/controls/cmb/configs.py">put_accounts_account_identifier_logs_control_cmb_config</a>(account_id, \*\*<a href="src/cloudflare/types/logs/controls/cmb/config_put_accounts_account_identifier_logs_control_cmb_config_params.py">params</a>) -> <a href="./src/cloudflare/types/logs/controls/cmb/config_put_accounts_account_identifier_logs_control_cmb_config_response.py">Optional</a></code>

## Rayids

Types:

```python
from cloudflare.types.logs import RayidGetResponse
```

Methods:

- <code title="get /zones/{zone_identifier}/logs/rayids/{ray_identifier}">client.logs.rayids.<a href="./src/cloudflare/resources/logs/rayids.py">get</a>(ray_identifier, \*, zone_identifier, \*\*<a href="src/cloudflare/types/logs/rayid_get_params.py">params</a>) -> <a href="./src/cloudflare/types/logs/rayid_get_response.py">RayidGetResponse</a></code>

## Receiveds

Types:

```python
from cloudflare.types.logs import ReceivedReceivedGetLogsReceivedResponse
```

Methods:

- <code title="get /zones/{zone_identifier}/logs/received">client.logs.receiveds.<a href="./src/cloudflare/resources/logs/receiveds/receiveds.py">received_get_logs_received</a>(zone_identifier, \*\*<a href="src/cloudflare/types/logs/received_received_get_logs_received_params.py">params</a>) -> <a href="./src/cloudflare/types/logs/received_received_get_logs_received_response.py">ReceivedReceivedGetLogsReceivedResponse</a></code>

### Fields

Types:

```python
from cloudflare.types.logs.receiveds import FieldLogsReceivedListFieldsResponse
```

Methods:

- <code title="get /zones/{zone_identifier}/logs/received/fields">client.logs.receiveds.fields.<a href="./src/cloudflare/resources/logs/receiveds/fields.py">logs_received_list_fields</a>(zone_identifier) -> <a href="./src/cloudflare/types/logs/receiveds/field_logs_received_list_fields_response.py">FieldLogsReceivedListFieldsResponse</a></code>

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

- <code title="post /zones/{zone_id}/origin_tls_client_auth">client.origin_tls_client_auth.<a href="./src/cloudflare/resources/origin_tls_client_auth/origin_tls_client_auth.py">create</a>(zone_id, \*\*<a href="src/cloudflare/types/origin_tls_client_auth_create_params.py">params</a>) -> <a href="./src/cloudflare/types/origin_tls_client_auth_create_response.py">OriginTLSClientAuthCreateResponse</a></code>
- <code title="get /zones/{zone_id}/origin_tls_client_auth">client.origin_tls_client_auth.<a href="./src/cloudflare/resources/origin_tls_client_auth/origin_tls_client_auth.py">list</a>(zone_id) -> <a href="./src/cloudflare/types/origin_tls_client_auth_list_response.py">Optional</a></code>
- <code title="delete /zones/{zone_id}/origin_tls_client_auth/{certificate_id}">client.origin_tls_client_auth.<a href="./src/cloudflare/resources/origin_tls_client_auth/origin_tls_client_auth.py">delete</a>(certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/origin_tls_client_auth_delete_response.py">OriginTLSClientAuthDeleteResponse</a></code>
- <code title="get /zones/{zone_id}/origin_tls_client_auth/{certificate_id}">client.origin_tls_client_auth.<a href="./src/cloudflare/resources/origin_tls_client_auth/origin_tls_client_auth.py">get</a>(certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/origin_tls_client_auth_get_response.py">OriginTLSClientAuthGetResponse</a></code>

## Hostnames

Types:

```python
from cloudflare.types.origin_tls_client_auth import HostnameUpdateResponse, HostnameGetResponse
```

Methods:

- <code title="put /zones/{zone_id}/origin_tls_client_auth/hostnames">client.origin_tls_client_auth.hostnames.<a href="./src/cloudflare/resources/origin_tls_client_auth/hostnames/hostnames.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/origin_tls_client_auth/hostname_update_params.py">params</a>) -> <a href="./src/cloudflare/types/origin_tls_client_auth/hostname_update_response.py">Optional</a></code>
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

- <code title="post /zones/{zone_id}/origin_tls_client_auth/hostnames/certificates">client.origin_tls_client_auth.hostnames.certificates.<a href="./src/cloudflare/resources/origin_tls_client_auth/hostnames/certificates.py">create</a>(zone_id, \*\*<a href="src/cloudflare/types/origin_tls_client_auth/hostnames/certificate_create_params.py">params</a>) -> <a href="./src/cloudflare/types/origin_tls_client_auth/hostnames/certificate_create_response.py">CertificateCreateResponse</a></code>
- <code title="get /zones/{zone_id}/origin_tls_client_auth/hostnames/certificates">client.origin_tls_client_auth.hostnames.certificates.<a href="./src/cloudflare/resources/origin_tls_client_auth/hostnames/certificates.py">list</a>(zone_id) -> <a href="./src/cloudflare/types/origin_tls_client_auth/hostnames/certificate_list_response.py">Optional</a></code>
- <code title="delete /zones/{zone_id}/origin_tls_client_auth/hostnames/certificates/{certificate_id}">client.origin_tls_client_auth.hostnames.certificates.<a href="./src/cloudflare/resources/origin_tls_client_auth/hostnames/certificates.py">delete</a>(certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/origin_tls_client_auth/hostnames/certificate_delete_response.py">CertificateDeleteResponse</a></code>
- <code title="get /zones/{zone_id}/origin_tls_client_auth/hostnames/certificates/{certificate_id}">client.origin_tls_client_auth.hostnames.certificates.<a href="./src/cloudflare/resources/origin_tls_client_auth/hostnames/certificates.py">get</a>(certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/origin_tls_client_auth/hostnames/certificate_get_response.py">CertificateGetResponse</a></code>

## Settings

Types:

```python
from cloudflare.types.origin_tls_client_auth import (
    SettingZoneLevelAuthenticatedOriginPullsGetEnablementSettingForZoneResponse,
    SettingZoneLevelAuthenticatedOriginPullsSetEnablementForZoneResponse,
)
```

Methods:

- <code title="get /zones/{zone_id}/origin_tls_client_auth/settings">client.origin_tls_client_auth.settings.<a href="./src/cloudflare/resources/origin_tls_client_auth/settings.py">zone_level_authenticated_origin_pulls_get_enablement_setting_for_zone</a>(zone_id) -> <a href="./src/cloudflare/types/origin_tls_client_auth/setting_zone_level_authenticated_origin_pulls_get_enablement_setting_for_zone_response.py">SettingZoneLevelAuthenticatedOriginPullsGetEnablementSettingForZoneResponse</a></code>
- <code title="put /zones/{zone_id}/origin_tls_client_auth/settings">client.origin_tls_client_auth.settings.<a href="./src/cloudflare/resources/origin_tls_client_auth/settings.py">zone_level_authenticated_origin_pulls_set_enablement_for_zone</a>(zone_id, \*\*<a href="src/cloudflare/types/origin_tls_client_auth/setting_zone_level_authenticated_origin_pulls_set_enablement_for_zone_params.py">params</a>) -> <a href="./src/cloudflare/types/origin_tls_client_auth/setting_zone_level_authenticated_origin_pulls_set_enablement_for_zone_response.py">SettingZoneLevelAuthenticatedOriginPullsSetEnablementForZoneResponse</a></code>

# Pagerules

Types:

```python
from cloudflare.types import (
    PageruleCreateResponse,
    PageruleUpdateResponse,
    PageruleListResponse,
    PageruleDeleteResponse,
    PageruleGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/pagerules">client.pagerules.<a href="./src/cloudflare/resources/pagerules/pagerules.py">create</a>(zone_id, \*\*<a href="src/cloudflare/types/pagerule_create_params.py">params</a>) -> <a href="./src/cloudflare/types/pagerule_create_response.py">PageruleCreateResponse</a></code>
- <code title="put /zones/{zone_id}/pagerules/{pagerule_id}">client.pagerules.<a href="./src/cloudflare/resources/pagerules/pagerules.py">update</a>(pagerule_id, \*, zone_id, \*\*<a href="src/cloudflare/types/pagerule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/pagerule_update_response.py">PageruleUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/pagerules">client.pagerules.<a href="./src/cloudflare/resources/pagerules/pagerules.py">list</a>(zone_id, \*\*<a href="src/cloudflare/types/pagerule_list_params.py">params</a>) -> <a href="./src/cloudflare/types/pagerule_list_response.py">PageruleListResponse</a></code>
- <code title="delete /zones/{zone_id}/pagerules/{pagerule_id}">client.pagerules.<a href="./src/cloudflare/resources/pagerules/pagerules.py">delete</a>(pagerule_id, \*, zone_id) -> <a href="./src/cloudflare/types/pagerule_delete_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/pagerules/{pagerule_id}">client.pagerules.<a href="./src/cloudflare/resources/pagerules/pagerules.py">get</a>(pagerule_id, \*, zone_id) -> <a href="./src/cloudflare/types/pagerule_get_response.py">PageruleGetResponse</a></code>

## Settings

Types:

```python
from cloudflare.types.pagerules import (
    SettingAvailablePageRulesSettingsListAvailablePageRulesSettingsResponse,
)
```

Methods:

- <code title="get /zones/{zone_id}/pagerules/settings">client.pagerules.settings.<a href="./src/cloudflare/resources/pagerules/settings.py">available_page_rules_settings_list_available_page_rules_settings</a>(zone_id) -> <a href="./src/cloudflare/types/pagerules/setting_available_page_rules_settings_list_available_page_rules_settings_response.py">SettingAvailablePageRulesSettingsListAvailablePageRulesSettingsResponse</a></code>

# RateLimits

Types:

```python
from cloudflare.types import RateLimitUpdateResponse, RateLimitListResponse, RateLimitGetResponse
```

Methods:

- <code title="put /zones/{zone_identifier}/rate_limits/{id}">client.rate_limits.<a href="./src/cloudflare/resources/rate_limits.py">update</a>(id, \*, zone_identifier, \*\*<a href="src/cloudflare/types/rate_limit_update_params.py">params</a>) -> <a href="./src/cloudflare/types/rate_limit_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_identifier}/rate_limits">client.rate_limits.<a href="./src/cloudflare/resources/rate_limits.py">list</a>(zone_identifier, \*\*<a href="src/cloudflare/types/rate_limit_list_params.py">params</a>) -> <a href="./src/cloudflare/types/rate_limit_list_response.py">Optional</a></code>
- <code title="get /zones/{zone_identifier}/rate_limits/{id}">client.rate_limits.<a href="./src/cloudflare/resources/rate_limits.py">get</a>(id, \*, zone_identifier) -> <a href="./src/cloudflare/types/rate_limit_get_response.py">Optional</a></code>

# SecondaryDNS

## ForceAxfrs

Types:

```python
from cloudflare.types.secondary_dns import ForceAxfrSecondaryDNSSecondaryZoneForceAxfrResponse
```

Methods:

- <code title="post /zones/{zone_id}/secondary_dns/force_axfr">client.secondary_dns.force_axfrs.<a href="./src/cloudflare/resources/secondary_dns/force_axfrs.py">secondary_dns_secondary_zone_force_axfr</a>(zone_id) -> <a href="./src/cloudflare/types/secondary_dns/force_axfr_secondary_dns_secondary_zone_force_axfr_response.py">str</a></code>

## Incomings

Types:

```python
from cloudflare.types.secondary_dns import (
    IncomingDeleteResponse,
    IncomingSecondaryDNSSecondaryZoneCreateSecondaryZoneConfigurationResponse,
    IncomingSecondaryDNSSecondaryZoneSecondaryZoneConfigurationDetailsResponse,
    IncomingSecondaryDNSSecondaryZoneUpdateSecondaryZoneConfigurationResponse,
)
```

Methods:

- <code title="delete /zones/{zone_id}/secondary_dns/incoming">client.secondary_dns.incomings.<a href="./src/cloudflare/resources/secondary_dns/incomings.py">delete</a>(zone_id) -> <a href="./src/cloudflare/types/secondary_dns/incoming_delete_response.py">IncomingDeleteResponse</a></code>
- <code title="post /zones/{zone_id}/secondary_dns/incoming">client.secondary_dns.incomings.<a href="./src/cloudflare/resources/secondary_dns/incomings.py">secondary_dns_secondary_zone_create_secondary_zone_configuration</a>(zone_id, \*\*<a href="src/cloudflare/types/secondary_dns/incoming_secondary_dns_secondary_zone_create_secondary_zone_configuration_params.py">params</a>) -> <a href="./src/cloudflare/types/secondary_dns/incoming_secondary_dns_secondary_zone_create_secondary_zone_configuration_response.py">IncomingSecondaryDNSSecondaryZoneCreateSecondaryZoneConfigurationResponse</a></code>
- <code title="get /zones/{zone_id}/secondary_dns/incoming">client.secondary_dns.incomings.<a href="./src/cloudflare/resources/secondary_dns/incomings.py">secondary_dns_secondary_zone_secondary_zone_configuration_details</a>(zone_id) -> <a href="./src/cloudflare/types/secondary_dns/incoming_secondary_dns_secondary_zone_secondary_zone_configuration_details_response.py">IncomingSecondaryDNSSecondaryZoneSecondaryZoneConfigurationDetailsResponse</a></code>
- <code title="put /zones/{zone_id}/secondary_dns/incoming">client.secondary_dns.incomings.<a href="./src/cloudflare/resources/secondary_dns/incomings.py">secondary_dns_secondary_zone_update_secondary_zone_configuration</a>(zone_id, \*\*<a href="src/cloudflare/types/secondary_dns/incoming_secondary_dns_secondary_zone_update_secondary_zone_configuration_params.py">params</a>) -> <a href="./src/cloudflare/types/secondary_dns/incoming_secondary_dns_secondary_zone_update_secondary_zone_configuration_response.py">IncomingSecondaryDNSSecondaryZoneUpdateSecondaryZoneConfigurationResponse</a></code>

## Outgoings

Types:

```python
from cloudflare.types.secondary_dns import (
    OutgoingDeleteResponse,
    OutgoingSecondaryDNSPrimaryZoneCreatePrimaryZoneConfigurationResponse,
    OutgoingSecondaryDNSPrimaryZonePrimaryZoneConfigurationDetailsResponse,
    OutgoingSecondaryDNSPrimaryZoneUpdatePrimaryZoneConfigurationResponse,
)
```

Methods:

- <code title="delete /zones/{zone_id}/secondary_dns/outgoing">client.secondary_dns.outgoings.<a href="./src/cloudflare/resources/secondary_dns/outgoings/outgoings.py">delete</a>(zone_id) -> <a href="./src/cloudflare/types/secondary_dns/outgoing_delete_response.py">OutgoingDeleteResponse</a></code>
- <code title="post /zones/{zone_id}/secondary_dns/outgoing">client.secondary_dns.outgoings.<a href="./src/cloudflare/resources/secondary_dns/outgoings/outgoings.py">secondary_dns_primary_zone_create_primary_zone_configuration</a>(zone_id, \*\*<a href="src/cloudflare/types/secondary_dns/outgoing_secondary_dns_primary_zone_create_primary_zone_configuration_params.py">params</a>) -> <a href="./src/cloudflare/types/secondary_dns/outgoing_secondary_dns_primary_zone_create_primary_zone_configuration_response.py">OutgoingSecondaryDNSPrimaryZoneCreatePrimaryZoneConfigurationResponse</a></code>
- <code title="get /zones/{zone_id}/secondary_dns/outgoing">client.secondary_dns.outgoings.<a href="./src/cloudflare/resources/secondary_dns/outgoings/outgoings.py">secondary_dns_primary_zone_primary_zone_configuration_details</a>(zone_id) -> <a href="./src/cloudflare/types/secondary_dns/outgoing_secondary_dns_primary_zone_primary_zone_configuration_details_response.py">OutgoingSecondaryDNSPrimaryZonePrimaryZoneConfigurationDetailsResponse</a></code>
- <code title="put /zones/{zone_id}/secondary_dns/outgoing">client.secondary_dns.outgoings.<a href="./src/cloudflare/resources/secondary_dns/outgoings/outgoings.py">secondary_dns_primary_zone_update_primary_zone_configuration</a>(zone_id, \*\*<a href="src/cloudflare/types/secondary_dns/outgoing_secondary_dns_primary_zone_update_primary_zone_configuration_params.py">params</a>) -> <a href="./src/cloudflare/types/secondary_dns/outgoing_secondary_dns_primary_zone_update_primary_zone_configuration_response.py">OutgoingSecondaryDNSPrimaryZoneUpdatePrimaryZoneConfigurationResponse</a></code>

### Disables

Types:

```python
from cloudflare.types.secondary_dns.outgoings import (
    DisableSecondaryDNSPrimaryZoneDisableOutgoingZoneTransfersResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/secondary_dns/outgoing/disable">client.secondary_dns.outgoings.disables.<a href="./src/cloudflare/resources/secondary_dns/outgoings/disables.py">secondary_dns_primary_zone_disable_outgoing_zone_transfers</a>(zone_id) -> <a href="./src/cloudflare/types/secondary_dns/outgoings/disable_secondary_dns_primary_zone_disable_outgoing_zone_transfers_response.py">str</a></code>

### Enables

Types:

```python
from cloudflare.types.secondary_dns.outgoings import (
    EnableSecondaryDNSPrimaryZoneEnableOutgoingZoneTransfersResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/secondary_dns/outgoing/enable">client.secondary_dns.outgoings.enables.<a href="./src/cloudflare/resources/secondary_dns/outgoings/enables.py">secondary_dns_primary_zone_enable_outgoing_zone_transfers</a>(zone_id) -> <a href="./src/cloudflare/types/secondary_dns/outgoings/enable_secondary_dns_primary_zone_enable_outgoing_zone_transfers_response.py">str</a></code>

### ForceNotifies

Types:

```python
from cloudflare.types.secondary_dns.outgoings import (
    ForceNotifySecondaryDNSPrimaryZoneForceDNSNotifyResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/secondary_dns/outgoing/force_notify">client.secondary_dns.outgoings.force_notifies.<a href="./src/cloudflare/resources/secondary_dns/outgoings/force_notifies.py">secondary_dns_primary_zone_force_dns_notify</a>(zone_id) -> <a href="./src/cloudflare/types/secondary_dns/outgoings/force_notify_secondary_dns_primary_zone_force_dns_notify_response.py">str</a></code>

### Statuses

Types:

```python
from cloudflare.types.secondary_dns.outgoings import (
    StatusSecondaryDNSPrimaryZoneGetOutgoingZoneTransferStatusResponse,
)
```

Methods:

- <code title="get /zones/{zone_id}/secondary_dns/outgoing/status">client.secondary_dns.outgoings.statuses.<a href="./src/cloudflare/resources/secondary_dns/outgoings/statuses.py">secondary_dns_primary_zone_get_outgoing_zone_transfer_status</a>(zone_id) -> <a href="./src/cloudflare/types/secondary_dns/outgoings/status_secondary_dns_primary_zone_get_outgoing_zone_transfer_status_response.py">str</a></code>

## ACLs

Types:

```python
from cloudflare.types.secondary_dns import (
    ACLUpdateResponse,
    ACLDeleteResponse,
    ACLGetResponse,
    ACLSecondaryDNSACLCreateACLResponse,
    ACLSecondaryDNSACLListACLsResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/secondary_dns/acls/{acl_id}">client.secondary_dns.acls.<a href="./src/cloudflare/resources/secondary_dns/acls.py">update</a>(acl_id, \*, account_id, \*\*<a href="src/cloudflare/types/secondary_dns/acl_update_params.py">params</a>) -> <a href="./src/cloudflare/types/secondary_dns/acl_update_response.py">ACLUpdateResponse</a></code>
- <code title="delete /accounts/{account_id}/secondary_dns/acls/{acl_id}">client.secondary_dns.acls.<a href="./src/cloudflare/resources/secondary_dns/acls.py">delete</a>(acl_id, \*, account_id) -> <a href="./src/cloudflare/types/secondary_dns/acl_delete_response.py">ACLDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/secondary_dns/acls/{acl_id}">client.secondary_dns.acls.<a href="./src/cloudflare/resources/secondary_dns/acls.py">get</a>(acl_id, \*, account_id) -> <a href="./src/cloudflare/types/secondary_dns/acl_get_response.py">ACLGetResponse</a></code>
- <code title="post /accounts/{account_id}/secondary_dns/acls">client.secondary_dns.acls.<a href="./src/cloudflare/resources/secondary_dns/acls.py">secondary_dns_acl_create_acl</a>(account_id, \*\*<a href="src/cloudflare/types/secondary_dns/acl_secondary_dns_acl_create_acl_params.py">params</a>) -> <a href="./src/cloudflare/types/secondary_dns/acl_secondary_dns_acl_create_acl_response.py">ACLSecondaryDNSACLCreateACLResponse</a></code>
- <code title="get /accounts/{account_id}/secondary_dns/acls">client.secondary_dns.acls.<a href="./src/cloudflare/resources/secondary_dns/acls.py">secondary_dns_acl_list_acls</a>(account_id) -> <a href="./src/cloudflare/types/secondary_dns/acl_secondary_dns_acl_list_acls_response.py">Optional</a></code>

## Peers

Types:

```python
from cloudflare.types.secondary_dns import (
    PeerUpdateResponse,
    PeerDeleteResponse,
    PeerGetResponse,
    PeerSecondaryDNSPeerCreatePeerResponse,
    PeerSecondaryDNSPeerListPeersResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/secondary_dns/peers/{peer_id}">client.secondary_dns.peers.<a href="./src/cloudflare/resources/secondary_dns/peers.py">update</a>(peer_id, \*, account_id, \*\*<a href="src/cloudflare/types/secondary_dns/peer_update_params.py">params</a>) -> <a href="./src/cloudflare/types/secondary_dns/peer_update_response.py">PeerUpdateResponse</a></code>
- <code title="delete /accounts/{account_id}/secondary_dns/peers/{peer_id}">client.secondary_dns.peers.<a href="./src/cloudflare/resources/secondary_dns/peers.py">delete</a>(peer_id, \*, account_id) -> <a href="./src/cloudflare/types/secondary_dns/peer_delete_response.py">PeerDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/secondary_dns/peers/{peer_id}">client.secondary_dns.peers.<a href="./src/cloudflare/resources/secondary_dns/peers.py">get</a>(peer_id, \*, account_id) -> <a href="./src/cloudflare/types/secondary_dns/peer_get_response.py">PeerGetResponse</a></code>
- <code title="post /accounts/{account_id}/secondary_dns/peers">client.secondary_dns.peers.<a href="./src/cloudflare/resources/secondary_dns/peers.py">secondary_dns_peer_create_peer</a>(account_id, \*\*<a href="src/cloudflare/types/secondary_dns/peer_secondary_dns_peer_create_peer_params.py">params</a>) -> <a href="./src/cloudflare/types/secondary_dns/peer_secondary_dns_peer_create_peer_response.py">PeerSecondaryDNSPeerCreatePeerResponse</a></code>
- <code title="get /accounts/{account_id}/secondary_dns/peers">client.secondary_dns.peers.<a href="./src/cloudflare/resources/secondary_dns/peers.py">secondary_dns_peer_list_peers</a>(account_id) -> <a href="./src/cloudflare/types/secondary_dns/peer_secondary_dns_peer_list_peers_response.py">Optional</a></code>

## Tsigs

Types:

```python
from cloudflare.types.secondary_dns import (
    TsigUpdateResponse,
    TsigDeleteResponse,
    TsigGetResponse,
    TsigSecondaryDNSTsigCreateTsigResponse,
    TsigSecondaryDNSTsigListTsiGsResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/secondary_dns/tsigs/{tsig_id}">client.secondary_dns.tsigs.<a href="./src/cloudflare/resources/secondary_dns/tsigs.py">update</a>(tsig_id, \*, account_id, \*\*<a href="src/cloudflare/types/secondary_dns/tsig_update_params.py">params</a>) -> <a href="./src/cloudflare/types/secondary_dns/tsig_update_response.py">TsigUpdateResponse</a></code>
- <code title="delete /accounts/{account_id}/secondary_dns/tsigs/{tsig_id}">client.secondary_dns.tsigs.<a href="./src/cloudflare/resources/secondary_dns/tsigs.py">delete</a>(tsig_id, \*, account_id) -> <a href="./src/cloudflare/types/secondary_dns/tsig_delete_response.py">TsigDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/secondary_dns/tsigs/{tsig_id}">client.secondary_dns.tsigs.<a href="./src/cloudflare/resources/secondary_dns/tsigs.py">get</a>(tsig_id, \*, account_id) -> <a href="./src/cloudflare/types/secondary_dns/tsig_get_response.py">TsigGetResponse</a></code>
- <code title="post /accounts/{account_id}/secondary_dns/tsigs">client.secondary_dns.tsigs.<a href="./src/cloudflare/resources/secondary_dns/tsigs.py">secondary_dns_tsig_create_tsig</a>(account_id, \*\*<a href="src/cloudflare/types/secondary_dns/tsig_secondary_dns_tsig_create_tsig_params.py">params</a>) -> <a href="./src/cloudflare/types/secondary_dns/tsig_secondary_dns_tsig_create_tsig_response.py">TsigSecondaryDNSTsigCreateTsigResponse</a></code>
- <code title="get /accounts/{account_id}/secondary_dns/tsigs">client.secondary_dns.tsigs.<a href="./src/cloudflare/resources/secondary_dns/tsigs.py">secondary_dns_tsig_list_tsi_gs</a>(account_id) -> <a href="./src/cloudflare/types/secondary_dns/tsig_secondary_dns_tsig_list_tsi_gs_response.py">Optional</a></code>

# Settings

Types:

```python
from cloudflare.types import SettingListResponse, SettingEditResponse
```

Methods:

- <code title="get /zones/{zone_id}/settings">client.settings.<a href="./src/cloudflare/resources/settings/settings.py">list</a>(zone_id) -> <a href="./src/cloudflare/types/setting_list_response.py">Optional</a></code>
- <code title="patch /zones/{zone_id}/settings">client.settings.<a href="./src/cloudflare/resources/settings/settings.py">edit</a>(zone_id, \*\*<a href="src/cloudflare/types/setting_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/setting_edit_response.py">Optional</a></code>

## ZeroRtt

Types:

```python
from cloudflare.types.settings import (
    ZeroRttGetResponse,
    ZeroRttZoneSettingsChange0RttSessionResumptionSettingResponse,
)
```

Methods:

- <code title="get /zones/{zone_id}/settings/0rtt">client.settings.zero_rtt.<a href="./src/cloudflare/resources/settings/zero_rtt.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/zero_rtt_get_response.py">Optional</a></code>
- <code title="patch /zones/{zone_id}/settings/0rtt">client.settings.zero_rtt.<a href="./src/cloudflare/resources/settings/zero_rtt.py">zone_settings_change_0_rtt_session_resumption_setting</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/zero_rtt_zone_settings_change_0_rtt_session_resumption_setting_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/zero_rtt_zone_settings_change_0_rtt_session_resumption_setting_response.py">Optional</a></code>

## AdvancedDDOS

Types:

```python
from cloudflare.types.settings import AdvancedDDOSGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/settings/advanced_ddos">client.settings.advanced_ddos.<a href="./src/cloudflare/resources/settings/advanced_ddos.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/advanced_ddos_get_response.py">Optional</a></code>

## AlwaysOnline

Types:

```python
from cloudflare.types.settings import AlwaysOnlineUpdateResponse, AlwaysOnlineGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/always_online">client.settings.always_online.<a href="./src/cloudflare/resources/settings/always_online.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/always_online_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/always_online_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/always_online">client.settings.always_online.<a href="./src/cloudflare/resources/settings/always_online.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/always_online_get_response.py">Optional</a></code>

## AlwaysUseHTTPs

Types:

```python
from cloudflare.types.settings import AlwaysUseHTTPUpdateResponse, AlwaysUseHTTPGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/always_use_https">client.settings.always_use_https.<a href="./src/cloudflare/resources/settings/always_use_https.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/always_use_http_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/always_use_http_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/always_use_https">client.settings.always_use_https.<a href="./src/cloudflare/resources/settings/always_use_https.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/always_use_http_get_response.py">Optional</a></code>

## AutomaticHTTPsRewrites

Types:

```python
from cloudflare.types.settings import (
    AutomaticHTTPsRewriteUpdateResponse,
    AutomaticHTTPsRewriteGetResponse,
)
```

Methods:

- <code title="patch /zones/{zone_id}/settings/automatic_https_rewrites">client.settings.automatic_https_rewrites.<a href="./src/cloudflare/resources/settings/automatic_https_rewrites.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/automatic_https_rewrite_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/automatic_https_rewrite_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/automatic_https_rewrites">client.settings.automatic_https_rewrites.<a href="./src/cloudflare/resources/settings/automatic_https_rewrites.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/automatic_https_rewrite_get_response.py">Optional</a></code>

## AutomaticPlatformOptimization

Types:

```python
from cloudflare.types.settings import (
    AutomaticPlatformOptimizationUpdateResponse,
    AutomaticPlatformOptimizationGetResponse,
)
```

Methods:

- <code title="patch /zones/{zone_id}/settings/automatic_platform_optimization">client.settings.automatic_platform_optimization.<a href="./src/cloudflare/resources/settings/automatic_platform_optimization.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/automatic_platform_optimization_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/automatic_platform_optimization_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/automatic_platform_optimization">client.settings.automatic_platform_optimization.<a href="./src/cloudflare/resources/settings/automatic_platform_optimization.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/automatic_platform_optimization_get_response.py">Optional</a></code>

## Brotli

Types:

```python
from cloudflare.types.settings import BrotliUpdateResponse, BrotliGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/brotli">client.settings.brotli.<a href="./src/cloudflare/resources/settings/brotli.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/brotli_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/brotli_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/brotli">client.settings.brotli.<a href="./src/cloudflare/resources/settings/brotli.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/brotli_get_response.py">Optional</a></code>

## BrowserCacheTTL

Types:

```python
from cloudflare.types.settings import BrowserCacheTTLUpdateResponse, BrowserCacheTTLGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/browser_cache_ttl">client.settings.browser_cache_ttl.<a href="./src/cloudflare/resources/settings/browser_cache_ttl.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/browser_cache_ttl_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/browser_cache_ttl_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/browser_cache_ttl">client.settings.browser_cache_ttl.<a href="./src/cloudflare/resources/settings/browser_cache_ttl.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/browser_cache_ttl_get_response.py">Optional</a></code>

## BrowserCheck

Types:

```python
from cloudflare.types.settings import BrowserCheckUpdateResponse, BrowserCheckGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/browser_check">client.settings.browser_check.<a href="./src/cloudflare/resources/settings/browser_check.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/browser_check_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/browser_check_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/browser_check">client.settings.browser_check.<a href="./src/cloudflare/resources/settings/browser_check.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/browser_check_get_response.py">Optional</a></code>

## CacheLevel

Types:

```python
from cloudflare.types.settings import CacheLevelUpdateResponse, CacheLevelGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/cache_level">client.settings.cache_level.<a href="./src/cloudflare/resources/settings/cache_level.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/cache_level_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/cache_level_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/cache_level">client.settings.cache_level.<a href="./src/cloudflare/resources/settings/cache_level.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/cache_level_get_response.py">Optional</a></code>

## ChallengeTTL

Types:

```python
from cloudflare.types.settings import ChallengeTTLUpdateResponse, ChallengeTTLGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/challenge_ttl">client.settings.challenge_ttl.<a href="./src/cloudflare/resources/settings/challenge_ttl.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/challenge_ttl_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/challenge_ttl_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/challenge_ttl">client.settings.challenge_ttl.<a href="./src/cloudflare/resources/settings/challenge_ttl.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/challenge_ttl_get_response.py">Optional</a></code>

## Ciphers

Types:

```python
from cloudflare.types.settings import CipherUpdateResponse, CipherGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/ciphers">client.settings.ciphers.<a href="./src/cloudflare/resources/settings/ciphers.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/cipher_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/cipher_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/ciphers">client.settings.ciphers.<a href="./src/cloudflare/resources/settings/ciphers.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/cipher_get_response.py">Optional</a></code>

## DevelopmentMode

Types:

```python
from cloudflare.types.settings import DevelopmentModeUpdateResponse, DevelopmentModeGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/development_mode">client.settings.development_mode.<a href="./src/cloudflare/resources/settings/development_mode.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/development_mode_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/development_mode_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/development_mode">client.settings.development_mode.<a href="./src/cloudflare/resources/settings/development_mode.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/development_mode_get_response.py">Optional</a></code>

## EarlyHint

Types:

```python
from cloudflare.types.settings import EarlyHintUpdateResponse, EarlyHintGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/early_hints">client.settings.early_hint.<a href="./src/cloudflare/resources/settings/early_hint.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/early_hint_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/early_hint_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/early_hints">client.settings.early_hint.<a href="./src/cloudflare/resources/settings/early_hint.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/early_hint_get_response.py">Optional</a></code>

## EmailObfuscation

Types:

```python
from cloudflare.types.settings import EmailObfuscationUpdateResponse, EmailObfuscationGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/email_obfuscation">client.settings.email_obfuscation.<a href="./src/cloudflare/resources/settings/email_obfuscation.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/email_obfuscation_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/email_obfuscation_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/email_obfuscation">client.settings.email_obfuscation.<a href="./src/cloudflare/resources/settings/email_obfuscation.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/email_obfuscation_get_response.py">Optional</a></code>

## H2Prioritization

Types:

```python
from cloudflare.types.settings import H2PrioritizationUpdateResponse, H2PrioritizationGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/h2_prioritization">client.settings.h2_prioritization.<a href="./src/cloudflare/resources/settings/h2_prioritization.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/h2_prioritization_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/h2_prioritization_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/h2_prioritization">client.settings.h2_prioritization.<a href="./src/cloudflare/resources/settings/h2_prioritization.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/h2_prioritization_get_response.py">Optional</a></code>

## HotlinkProtection

Types:

```python
from cloudflare.types.settings import HotlinkProtectionUpdateResponse, HotlinkProtectionGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/hotlink_protection">client.settings.hotlink_protection.<a href="./src/cloudflare/resources/settings/hotlink_protection.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/hotlink_protection_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/hotlink_protection_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/hotlink_protection">client.settings.hotlink_protection.<a href="./src/cloudflare/resources/settings/hotlink_protection.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/hotlink_protection_get_response.py">Optional</a></code>

## HTTP2

Types:

```python
from cloudflare.types.settings import HTTP2UpdateResponse, HTTP2GetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/http2">client.settings.http2.<a href="./src/cloudflare/resources/settings/http2.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/http2_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/http2_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/http2">client.settings.http2.<a href="./src/cloudflare/resources/settings/http2.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/http2_get_response.py">Optional</a></code>

## HTTP3

Types:

```python
from cloudflare.types.settings import HTTP3UpdateResponse, HTTP3GetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/http3">client.settings.http3.<a href="./src/cloudflare/resources/settings/http3.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/http3_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/http3_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/http3">client.settings.http3.<a href="./src/cloudflare/resources/settings/http3.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/http3_get_response.py">Optional</a></code>

## ImageResizing

Types:

```python
from cloudflare.types.settings import ImageResizingUpdateResponse, ImageResizingGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/image_resizing">client.settings.image_resizing.<a href="./src/cloudflare/resources/settings/image_resizing.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/image_resizing_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/image_resizing_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/image_resizing">client.settings.image_resizing.<a href="./src/cloudflare/resources/settings/image_resizing.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/image_resizing_get_response.py">Optional</a></code>

## IPGeolocation

Types:

```python
from cloudflare.types.settings import IPGeolocationUpdateResponse, IPGeolocationGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/ip_geolocation">client.settings.ip_geolocation.<a href="./src/cloudflare/resources/settings/ip_geolocation.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/ip_geolocation_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/ip_geolocation_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/ip_geolocation">client.settings.ip_geolocation.<a href="./src/cloudflare/resources/settings/ip_geolocation.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/ip_geolocation_get_response.py">Optional</a></code>

## IPV6

Types:

```python
from cloudflare.types.settings import IPV6UpdateResponse, IPV6GetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/ipv6">client.settings.ipv6.<a href="./src/cloudflare/resources/settings/ipv6.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/ipv6_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/ipv6_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/ipv6">client.settings.ipv6.<a href="./src/cloudflare/resources/settings/ipv6.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/ipv6_get_response.py">Optional</a></code>

## MinTLSVersion

Types:

```python
from cloudflare.types.settings import MinTLSVersionUpdateResponse, MinTLSVersionGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/min_tls_version">client.settings.min_tls_version.<a href="./src/cloudflare/resources/settings/min_tls_version.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/min_tls_version_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/min_tls_version_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/min_tls_version">client.settings.min_tls_version.<a href="./src/cloudflare/resources/settings/min_tls_version.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/min_tls_version_get_response.py">Optional</a></code>

## Minify

Types:

```python
from cloudflare.types.settings import MinifyUpdateResponse, MinifyGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/minify">client.settings.minify.<a href="./src/cloudflare/resources/settings/minify.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/minify_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/minify_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/minify">client.settings.minify.<a href="./src/cloudflare/resources/settings/minify.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/minify_get_response.py">Optional</a></code>

## Mirage

Types:

```python
from cloudflare.types.settings import MirageUpdateResponse, MirageGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/mirage">client.settings.mirage.<a href="./src/cloudflare/resources/settings/mirage.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/mirage_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/mirage_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/mirage">client.settings.mirage.<a href="./src/cloudflare/resources/settings/mirage.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/mirage_get_response.py">Optional</a></code>

## MobileRedirect

Types:

```python
from cloudflare.types.settings import MobileRedirectUpdateResponse, MobileRedirectGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/mobile_redirect">client.settings.mobile_redirect.<a href="./src/cloudflare/resources/settings/mobile_redirect.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/mobile_redirect_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/mobile_redirect_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/mobile_redirect">client.settings.mobile_redirect.<a href="./src/cloudflare/resources/settings/mobile_redirect.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/mobile_redirect_get_response.py">Optional</a></code>

## NEL

Types:

```python
from cloudflare.types.settings import NELUpdateResponse, NELGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/nel">client.settings.nel.<a href="./src/cloudflare/resources/settings/nel.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/nel_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/nel_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/nel">client.settings.nel.<a href="./src/cloudflare/resources/settings/nel.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/nel_get_response.py">Optional</a></code>

## OpportunisticEncryption

Types:

```python
from cloudflare.types.settings import (
    OpportunisticEncryptionUpdateResponse,
    OpportunisticEncryptionGetResponse,
)
```

Methods:

- <code title="patch /zones/{zone_id}/settings/opportunistic_encryption">client.settings.opportunistic_encryption.<a href="./src/cloudflare/resources/settings/opportunistic_encryption.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/opportunistic_encryption_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/opportunistic_encryption_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/opportunistic_encryption">client.settings.opportunistic_encryption.<a href="./src/cloudflare/resources/settings/opportunistic_encryption.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/opportunistic_encryption_get_response.py">Optional</a></code>

## OpportunisticOnion

Types:

```python
from cloudflare.types.settings import (
    OpportunisticOnionUpdateResponse,
    OpportunisticOnionGetResponse,
)
```

Methods:

- <code title="patch /zones/{zone_id}/settings/opportunistic_onion">client.settings.opportunistic_onion.<a href="./src/cloudflare/resources/settings/opportunistic_onion.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/opportunistic_onion_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/opportunistic_onion_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/opportunistic_onion">client.settings.opportunistic_onion.<a href="./src/cloudflare/resources/settings/opportunistic_onion.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/opportunistic_onion_get_response.py">Optional</a></code>

## OrangeToOrange

Types:

```python
from cloudflare.types.settings import OrangeToOrangeUpdateResponse, OrangeToOrangeGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/orange_to_orange">client.settings.orange_to_orange.<a href="./src/cloudflare/resources/settings/orange_to_orange.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/orange_to_orange_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/orange_to_orange_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/orange_to_orange">client.settings.orange_to_orange.<a href="./src/cloudflare/resources/settings/orange_to_orange.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/orange_to_orange_get_response.py">Optional</a></code>

## OriginErrorPagePassThru

Types:

```python
from cloudflare.types.settings import (
    OriginErrorPagePassThruUpdateResponse,
    OriginErrorPagePassThruGetResponse,
)
```

Methods:

- <code title="patch /zones/{zone_id}/settings/origin_error_page_pass_thru">client.settings.origin_error_page_pass_thru.<a href="./src/cloudflare/resources/settings/origin_error_page_pass_thru.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/origin_error_page_pass_thru_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/origin_error_page_pass_thru_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/origin_error_page_pass_thru">client.settings.origin_error_page_pass_thru.<a href="./src/cloudflare/resources/settings/origin_error_page_pass_thru.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/origin_error_page_pass_thru_get_response.py">Optional</a></code>

## OriginMaxHTTPVersion

Types:

```python
from cloudflare.types.settings import (
    OriginMaxHTTPVersionUpdateResponse,
    OriginMaxHTTPVersionGetResponse,
)
```

Methods:

- <code title="patch /zones/{zone_id}/settings/origin_max_http_version">client.settings.origin_max_http_version.<a href="./src/cloudflare/resources/settings/origin_max_http_version.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/origin_max_http_version_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/origin_max_http_version_update_response.py">OriginMaxHTTPVersionUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/settings/origin_max_http_version">client.settings.origin_max_http_version.<a href="./src/cloudflare/resources/settings/origin_max_http_version.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/origin_max_http_version_get_response.py">OriginMaxHTTPVersionGetResponse</a></code>

## Polish

Types:

```python
from cloudflare.types.settings import PolishUpdateResponse, PolishGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/polish">client.settings.polish.<a href="./src/cloudflare/resources/settings/polish.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/polish_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/polish_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/polish">client.settings.polish.<a href="./src/cloudflare/resources/settings/polish.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/polish_get_response.py">Optional</a></code>

## PrefetchPreload

Types:

```python
from cloudflare.types.settings import PrefetchPreloadUpdateResponse, PrefetchPreloadGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/prefetch_preload">client.settings.prefetch_preload.<a href="./src/cloudflare/resources/settings/prefetch_preload.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/prefetch_preload_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/prefetch_preload_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/prefetch_preload">client.settings.prefetch_preload.<a href="./src/cloudflare/resources/settings/prefetch_preload.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/prefetch_preload_get_response.py">Optional</a></code>

## ProxyReadTimeout

Types:

```python
from cloudflare.types.settings import ProxyReadTimeoutUpdateResponse, ProxyReadTimeoutGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/proxy_read_timeout">client.settings.proxy_read_timeout.<a href="./src/cloudflare/resources/settings/proxy_read_timeout.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/proxy_read_timeout_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/proxy_read_timeout_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/proxy_read_timeout">client.settings.proxy_read_timeout.<a href="./src/cloudflare/resources/settings/proxy_read_timeout.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/proxy_read_timeout_get_response.py">Optional</a></code>

## PseudoIPV4

Types:

```python
from cloudflare.types.settings import PseudoIPV4UpdateResponse, PseudoIPV4GetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/pseudo_ipv4">client.settings.pseudo_ipv4.<a href="./src/cloudflare/resources/settings/pseudo_ipv4.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/pseudo_ipv4_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/pseudo_ipv4_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/pseudo_ipv4">client.settings.pseudo_ipv4.<a href="./src/cloudflare/resources/settings/pseudo_ipv4.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/pseudo_ipv4_get_response.py">Optional</a></code>

## ResponseBuffering

Types:

```python
from cloudflare.types.settings import ResponseBufferingUpdateResponse, ResponseBufferingGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/response_buffering">client.settings.response_buffering.<a href="./src/cloudflare/resources/settings/response_buffering.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/response_buffering_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/response_buffering_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/response_buffering">client.settings.response_buffering.<a href="./src/cloudflare/resources/settings/response_buffering.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/response_buffering_get_response.py">Optional</a></code>

## RocketLoader

Types:

```python
from cloudflare.types.settings import RocketLoaderUpdateResponse, RocketLoaderGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/rocket_loader">client.settings.rocket_loader.<a href="./src/cloudflare/resources/settings/rocket_loader.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/rocket_loader_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/rocket_loader_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/rocket_loader">client.settings.rocket_loader.<a href="./src/cloudflare/resources/settings/rocket_loader.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/rocket_loader_get_response.py">Optional</a></code>

## SecurityHeaders

Types:

```python
from cloudflare.types.settings import SecurityHeaderUpdateResponse, SecurityHeaderGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/security_header">client.settings.security_headers.<a href="./src/cloudflare/resources/settings/security_headers.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/security_header_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/security_header_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/security_header">client.settings.security_headers.<a href="./src/cloudflare/resources/settings/security_headers.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/security_header_get_response.py">Optional</a></code>

## SecurityLevel

Types:

```python
from cloudflare.types.settings import SecurityLevelUpdateResponse, SecurityLevelGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/security_level">client.settings.security_level.<a href="./src/cloudflare/resources/settings/security_level.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/security_level_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/security_level_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/security_level">client.settings.security_level.<a href="./src/cloudflare/resources/settings/security_level.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/security_level_get_response.py">Optional</a></code>

## ServerSideExcludes

Types:

```python
from cloudflare.types.settings import ServerSideExcludeUpdateResponse, ServerSideExcludeGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/server_side_exclude">client.settings.server_side_excludes.<a href="./src/cloudflare/resources/settings/server_side_excludes.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/server_side_exclude_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/server_side_exclude_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/server_side_exclude">client.settings.server_side_excludes.<a href="./src/cloudflare/resources/settings/server_side_excludes.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/server_side_exclude_get_response.py">Optional</a></code>

## SortQueryStringForCache

Types:

```python
from cloudflare.types.settings import (
    SortQueryStringForCacheUpdateResponse,
    SortQueryStringForCacheGetResponse,
)
```

Methods:

- <code title="patch /zones/{zone_id}/settings/sort_query_string_for_cache">client.settings.sort_query_string_for_cache.<a href="./src/cloudflare/resources/settings/sort_query_string_for_cache.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/sort_query_string_for_cache_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/sort_query_string_for_cache_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/sort_query_string_for_cache">client.settings.sort_query_string_for_cache.<a href="./src/cloudflare/resources/settings/sort_query_string_for_cache.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/sort_query_string_for_cache_get_response.py">Optional</a></code>

## SSL

Types:

```python
from cloudflare.types.settings import SSLUpdateResponse, SSLGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/ssl">client.settings.ssl.<a href="./src/cloudflare/resources/settings/ssl.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/ssl_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/ssl_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/ssl">client.settings.ssl.<a href="./src/cloudflare/resources/settings/ssl.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/ssl_get_response.py">Optional</a></code>

## SSLRecommender

Types:

```python
from cloudflare.types.settings import SSLRecommenderUpdateResponse, SSLRecommenderGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/ssl_recommender">client.settings.ssl_recommender.<a href="./src/cloudflare/resources/settings/ssl_recommender.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/ssl_recommender_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/ssl_recommender_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/ssl_recommender">client.settings.ssl_recommender.<a href="./src/cloudflare/resources/settings/ssl_recommender.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/ssl_recommender_get_response.py">Optional</a></code>

## TLS1_3

Types:

```python
from cloudflare.types.settings import TLS1_3UpdateResponse, TLS1_3GetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/tls_1_3">client.settings.tls_1_3.<a href="./src/cloudflare/resources/settings/tls_1_3.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/tls_1_3_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/tls_1_3_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/tls_1_3">client.settings.tls_1_3.<a href="./src/cloudflare/resources/settings/tls_1_3.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/tls_1_3_get_response.py">Optional</a></code>

## TLSClientAuth

Types:

```python
from cloudflare.types.settings import TLSClientAuthUpdateResponse, TLSClientAuthGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/tls_client_auth">client.settings.tls_client_auth.<a href="./src/cloudflare/resources/settings/tls_client_auth.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/tls_client_auth_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/tls_client_auth_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/tls_client_auth">client.settings.tls_client_auth.<a href="./src/cloudflare/resources/settings/tls_client_auth.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/tls_client_auth_get_response.py">Optional</a></code>

## TrueClientIPHeader

Types:

```python
from cloudflare.types.settings import (
    TrueClientIPHeaderUpdateResponse,
    TrueClientIPHeaderGetResponse,
)
```

Methods:

- <code title="patch /zones/{zone_id}/settings/true_client_ip_header">client.settings.true_client_ip_header.<a href="./src/cloudflare/resources/settings/true_client_ip_header.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/true_client_ip_header_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/true_client_ip_header_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/true_client_ip_header">client.settings.true_client_ip_header.<a href="./src/cloudflare/resources/settings/true_client_ip_header.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/true_client_ip_header_get_response.py">Optional</a></code>

## WAF

Types:

```python
from cloudflare.types.settings import WAFUpdateResponse, WAFGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/waf">client.settings.waf.<a href="./src/cloudflare/resources/settings/waf.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/waf_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/waf_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/waf">client.settings.waf.<a href="./src/cloudflare/resources/settings/waf.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/waf_get_response.py">Optional</a></code>

## Webp

Types:

```python
from cloudflare.types.settings import WebpUpdateResponse, WebpGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/webp">client.settings.webp.<a href="./src/cloudflare/resources/settings/webp.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/webp_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/webp_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/webp">client.settings.webp.<a href="./src/cloudflare/resources/settings/webp.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/webp_get_response.py">Optional</a></code>

## Websocket

Types:

```python
from cloudflare.types.settings import WebsocketUpdateResponse, WebsocketGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/websockets">client.settings.websocket.<a href="./src/cloudflare/resources/settings/websocket.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/settings/websocket_update_params.py">params</a>) -> <a href="./src/cloudflare/types/settings/websocket_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/websockets">client.settings.websocket.<a href="./src/cloudflare/resources/settings/websocket.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/settings/websocket_get_response.py">Optional</a></code>

# WaitingRooms

Types:

```python
from cloudflare.types import (
    WaitingRoomCreateResponse,
    WaitingRoomUpdateResponse,
    WaitingRoomListResponse,
    WaitingRoomDeleteResponse,
    WaitingRoomGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_identifier}/waiting_rooms">client.waiting_rooms.<a href="./src/cloudflare/resources/waiting_rooms/waiting_rooms.py">create</a>(zone_identifier, \*\*<a href="src/cloudflare/types/waiting_room_create_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_room_create_response.py">WaitingRoomCreateResponse</a></code>
- <code title="put /zones/{zone_identifier}/waiting_rooms/{waiting_room_id}">client.waiting_rooms.<a href="./src/cloudflare/resources/waiting_rooms/waiting_rooms.py">update</a>(waiting_room_id, \*, zone_identifier, \*\*<a href="src/cloudflare/types/waiting_room_update_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_room_update_response.py">WaitingRoomUpdateResponse</a></code>
- <code title="get /zones/{zone_identifier}/waiting_rooms">client.waiting_rooms.<a href="./src/cloudflare/resources/waiting_rooms/waiting_rooms.py">list</a>(zone_identifier) -> <a href="./src/cloudflare/types/waiting_room_list_response.py">Optional</a></code>
- <code title="delete /zones/{zone_identifier}/waiting_rooms/{waiting_room_id}">client.waiting_rooms.<a href="./src/cloudflare/resources/waiting_rooms/waiting_rooms.py">delete</a>(waiting_room_id, \*, zone_identifier) -> <a href="./src/cloudflare/types/waiting_room_delete_response.py">WaitingRoomDeleteResponse</a></code>
- <code title="get /zones/{zone_identifier}/waiting_rooms/{waiting_room_id}">client.waiting_rooms.<a href="./src/cloudflare/resources/waiting_rooms/waiting_rooms.py">get</a>(waiting_room_id, \*, zone_identifier) -> <a href="./src/cloudflare/types/waiting_room_get_response.py">WaitingRoomGetResponse</a></code>

## Previews

Types:

```python
from cloudflare.types.waiting_rooms import PreviewCreateResponse
```

Methods:

- <code title="post /zones/{zone_identifier}/waiting_rooms/preview">client.waiting_rooms.previews.<a href="./src/cloudflare/resources/waiting_rooms/previews.py">create</a>(zone_identifier, \*\*<a href="src/cloudflare/types/waiting_rooms/preview_create_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/preview_create_response.py">PreviewCreateResponse</a></code>

## Events

Types:

```python
from cloudflare.types.waiting_rooms import (
    EventUpdateResponse,
    EventDeleteResponse,
    EventGetResponse,
    EventWaitingRoomCreateEventResponse,
    EventWaitingRoomListEventsResponse,
)
```

Methods:

- <code title="put /zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/events/{event_id}">client.waiting_rooms.events.<a href="./src/cloudflare/resources/waiting_rooms/events/events.py">update</a>(event_id, \*, zone_identifier, waiting_room_id, \*\*<a href="src/cloudflare/types/waiting_rooms/event_update_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/event_update_response.py">EventUpdateResponse</a></code>
- <code title="delete /zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/events/{event_id}">client.waiting_rooms.events.<a href="./src/cloudflare/resources/waiting_rooms/events/events.py">delete</a>(event_id, \*, zone_identifier, waiting_room_id) -> <a href="./src/cloudflare/types/waiting_rooms/event_delete_response.py">EventDeleteResponse</a></code>
- <code title="get /zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/events/{event_id}">client.waiting_rooms.events.<a href="./src/cloudflare/resources/waiting_rooms/events/events.py">get</a>(event_id, \*, zone_identifier, waiting_room_id) -> <a href="./src/cloudflare/types/waiting_rooms/event_get_response.py">EventGetResponse</a></code>
- <code title="post /zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/events">client.waiting_rooms.events.<a href="./src/cloudflare/resources/waiting_rooms/events/events.py">waiting_room_create_event</a>(waiting_room_id, \*, zone_identifier, \*\*<a href="src/cloudflare/types/waiting_rooms/event_waiting_room_create_event_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/event_waiting_room_create_event_response.py">EventWaitingRoomCreateEventResponse</a></code>
- <code title="get /zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/events">client.waiting_rooms.events.<a href="./src/cloudflare/resources/waiting_rooms/events/events.py">waiting_room_list_events</a>(waiting_room_id, \*, zone_identifier) -> <a href="./src/cloudflare/types/waiting_rooms/event_waiting_room_list_events_response.py">Optional</a></code>

### Details

Types:

```python
from cloudflare.types.waiting_rooms.events import DetailWaitingRoomPreviewActiveEventDetailsResponse
```

Methods:

- <code title="get /zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/events/{event_id}/details">client.waiting_rooms.events.details.<a href="./src/cloudflare/resources/waiting_rooms/events/details.py">waiting_room_preview_active_event_details</a>(event_id, \*, zone_identifier, waiting_room_id) -> <a href="./src/cloudflare/types/waiting_rooms/events/detail_waiting_room_preview_active_event_details_response.py">DetailWaitingRoomPreviewActiveEventDetailsResponse</a></code>

## Rules

Types:

```python
from cloudflare.types.waiting_rooms import (
    RuleUpdateResponse,
    RuleDeleteResponse,
    RuleWaitingRoomCreateWaitingRoomRuleResponse,
    RuleWaitingRoomListWaitingRoomRulesResponse,
    RuleWaitingRoomReplaceWaitingRoomRulesResponse,
)
```

Methods:

- <code title="patch /zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/rules/{rule_id}">client.waiting_rooms.rules.<a href="./src/cloudflare/resources/waiting_rooms/rules.py">update</a>(rule_id, \*, zone_identifier, waiting_room_id, \*\*<a href="src/cloudflare/types/waiting_rooms/rule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/rule_update_response.py">Optional</a></code>
- <code title="delete /zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/rules/{rule_id}">client.waiting_rooms.rules.<a href="./src/cloudflare/resources/waiting_rooms/rules.py">delete</a>(rule_id, \*, zone_identifier, waiting_room_id) -> <a href="./src/cloudflare/types/waiting_rooms/rule_delete_response.py">Optional</a></code>
- <code title="post /zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/rules">client.waiting_rooms.rules.<a href="./src/cloudflare/resources/waiting_rooms/rules.py">waiting_room_create_waiting_room_rule</a>(waiting_room_id, \*, zone_identifier, \*\*<a href="src/cloudflare/types/waiting_rooms/rule_waiting_room_create_waiting_room_rule_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/rule_waiting_room_create_waiting_room_rule_response.py">Optional</a></code>
- <code title="get /zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/rules">client.waiting_rooms.rules.<a href="./src/cloudflare/resources/waiting_rooms/rules.py">waiting_room_list_waiting_room_rules</a>(waiting_room_id, \*, zone_identifier) -> <a href="./src/cloudflare/types/waiting_rooms/rule_waiting_room_list_waiting_room_rules_response.py">Optional</a></code>
- <code title="put /zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/rules">client.waiting_rooms.rules.<a href="./src/cloudflare/resources/waiting_rooms/rules.py">waiting_room_replace_waiting_room_rules</a>(waiting_room_id, \*, zone_identifier, \*\*<a href="src/cloudflare/types/waiting_rooms/rule_waiting_room_replace_waiting_room_rules_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/rule_waiting_room_replace_waiting_room_rules_response.py">Optional</a></code>

## Statuses

Types:

```python
from cloudflare.types.waiting_rooms import StatusWaitingRoomGetWaitingRoomStatusResponse
```

Methods:

- <code title="get /zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/status">client.waiting_rooms.statuses.<a href="./src/cloudflare/resources/waiting_rooms/statuses.py">waiting_room_get_waiting_room_status</a>(waiting_room_id, \*, zone_identifier) -> <a href="./src/cloudflare/types/waiting_rooms/status_waiting_room_get_waiting_room_status_response.py">StatusWaitingRoomGetWaitingRoomStatusResponse</a></code>

## Settings

Types:

```python
from cloudflare.types.waiting_rooms import (
    WaitingroomZoneSettingsResponse,
    SettingUpdateResponse,
    SettingGetResponse,
)
```

Methods:

- <code title="patch /zones/{zone_identifier}/waiting_rooms/settings">client.waiting_rooms.settings.<a href="./src/cloudflare/resources/waiting_rooms/settings.py">update</a>(zone_identifier, \*\*<a href="src/cloudflare/types/waiting_rooms/setting_update_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/setting_update_response.py">SettingUpdateResponse</a></code>
- <code title="get /zones/{zone_identifier}/waiting_rooms/settings">client.waiting_rooms.settings.<a href="./src/cloudflare/resources/waiting_rooms/settings.py">get</a>(zone_identifier) -> <a href="./src/cloudflare/types/waiting_rooms/setting_get_response.py">SettingGetResponse</a></code>

# Web3s

## Hostnames

Types:

```python
from cloudflare.types.web3s import (
    HostnameUpdateResponse,
    HostnameDeleteResponse,
    HostnameGetResponse,
    HostnameWeb3HostnameCreateWeb3HostnameResponse,
    HostnameWeb3HostnameListWeb3HostnamesResponse,
)
```

Methods:

- <code title="patch /zones/{zone_identifier}/web3/hostnames/{identifier}">client.web3s.hostnames.<a href="./src/cloudflare/resources/web3s/hostnames/hostnames.py">update</a>(identifier, \*, zone_identifier, \*\*<a href="src/cloudflare/types/web3s/hostname_update_params.py">params</a>) -> <a href="./src/cloudflare/types/web3s/hostname_update_response.py">HostnameUpdateResponse</a></code>
- <code title="delete /zones/{zone_identifier}/web3/hostnames/{identifier}">client.web3s.hostnames.<a href="./src/cloudflare/resources/web3s/hostnames/hostnames.py">delete</a>(identifier, \*, zone_identifier) -> <a href="./src/cloudflare/types/web3s/hostname_delete_response.py">Optional</a></code>
- <code title="get /zones/{zone_identifier}/web3/hostnames/{identifier}">client.web3s.hostnames.<a href="./src/cloudflare/resources/web3s/hostnames/hostnames.py">get</a>(identifier, \*, zone_identifier) -> <a href="./src/cloudflare/types/web3s/hostname_get_response.py">HostnameGetResponse</a></code>
- <code title="post /zones/{zone_identifier}/web3/hostnames">client.web3s.hostnames.<a href="./src/cloudflare/resources/web3s/hostnames/hostnames.py">web3_hostname_create_web3_hostname</a>(zone_identifier, \*\*<a href="src/cloudflare/types/web3s/hostname_web3_hostname_create_web3_hostname_params.py">params</a>) -> <a href="./src/cloudflare/types/web3s/hostname_web3_hostname_create_web3_hostname_response.py">HostnameWeb3HostnameCreateWeb3HostnameResponse</a></code>
- <code title="get /zones/{zone_identifier}/web3/hostnames">client.web3s.hostnames.<a href="./src/cloudflare/resources/web3s/hostnames/hostnames.py">web3_hostname_list_web3_hostnames</a>(zone_identifier) -> <a href="./src/cloudflare/types/web3s/hostname_web3_hostname_list_web3_hostnames_response.py">Optional</a></code>

### IpfsUniversalPaths

#### ContentLists

Types:

```python
from cloudflare.types.web3s.hostnames.ipfs_universal_paths import (
    ContentListWeb3HostnameIpfsUniversalPathGatewayContentListDetailsResponse,
    ContentListWeb3HostnameUpdateIpfsUniversalPathGatewayContentListResponse,
)
```

Methods:

- <code title="get /zones/{zone_identifier}/web3/hostnames/{identifier}/ipfs_universal_path/content_list">client.web3s.hostnames.ipfs_universal_paths.content_lists.<a href="./src/cloudflare/resources/web3s/hostnames/ipfs_universal_paths/content_lists/content_lists.py">web3_hostname_ipfs_universal_path_gateway_content_list_details</a>(identifier, \*, zone_identifier) -> <a href="./src/cloudflare/types/web3s/hostnames/ipfs_universal_paths/content_list_web3_hostname_ipfs_universal_path_gateway_content_list_details_response.py">ContentListWeb3HostnameIpfsUniversalPathGatewayContentListDetailsResponse</a></code>
- <code title="put /zones/{zone_identifier}/web3/hostnames/{identifier}/ipfs_universal_path/content_list">client.web3s.hostnames.ipfs_universal_paths.content_lists.<a href="./src/cloudflare/resources/web3s/hostnames/ipfs_universal_paths/content_lists/content_lists.py">web3_hostname_update_ipfs_universal_path_gateway_content_list</a>(identifier, \*, zone_identifier, \*\*<a href="src/cloudflare/types/web3s/hostnames/ipfs_universal_paths/content_list_web3_hostname_update_ipfs_universal_path_gateway_content_list_params.py">params</a>) -> <a href="./src/cloudflare/types/web3s/hostnames/ipfs_universal_paths/content_list_web3_hostname_update_ipfs_universal_path_gateway_content_list_response.py">ContentListWeb3HostnameUpdateIpfsUniversalPathGatewayContentListResponse</a></code>

##### Entries

Types:

```python
from cloudflare.types.web3s.hostnames.ipfs_universal_paths.content_lists import (
    EntryUpdateResponse,
    EntryDeleteResponse,
    EntryGetResponse,
    EntryWeb3HostnameCreateIpfsUniversalPathGatewayContentListEntryResponse,
    EntryWeb3HostnameListIpfsUniversalPathGatewayContentListEntriesResponse,
)
```

Methods:

- <code title="put /zones/{zone_identifier}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries/{content_list_entry_identifier}">client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.<a href="./src/cloudflare/resources/web3s/hostnames/ipfs_universal_paths/content_lists/entries.py">update</a>(content_list_entry_identifier, \*, zone_identifier, identifier, \*\*<a href="src/cloudflare/types/web3s/hostnames/ipfs_universal_paths/content_lists/entry_update_params.py">params</a>) -> <a href="./src/cloudflare/types/web3s/hostnames/ipfs_universal_paths/content_lists/entry_update_response.py">EntryUpdateResponse</a></code>
- <code title="delete /zones/{zone_identifier}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries/{content_list_entry_identifier}">client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.<a href="./src/cloudflare/resources/web3s/hostnames/ipfs_universal_paths/content_lists/entries.py">delete</a>(content_list_entry_identifier, \*, zone_identifier, identifier) -> <a href="./src/cloudflare/types/web3s/hostnames/ipfs_universal_paths/content_lists/entry_delete_response.py">Optional</a></code>
- <code title="get /zones/{zone_identifier}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries/{content_list_entry_identifier}">client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.<a href="./src/cloudflare/resources/web3s/hostnames/ipfs_universal_paths/content_lists/entries.py">get</a>(content_list_entry_identifier, \*, zone_identifier, identifier) -> <a href="./src/cloudflare/types/web3s/hostnames/ipfs_universal_paths/content_lists/entry_get_response.py">EntryGetResponse</a></code>
- <code title="post /zones/{zone_identifier}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries">client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.<a href="./src/cloudflare/resources/web3s/hostnames/ipfs_universal_paths/content_lists/entries.py">web3_hostname_create_ipfs_universal_path_gateway_content_list_entry</a>(identifier, \*, zone_identifier, \*\*<a href="src/cloudflare/types/web3s/hostnames/ipfs_universal_paths/content_lists/entry_web3_hostname_create_ipfs_universal_path_gateway_content_list_entry_params.py">params</a>) -> <a href="./src/cloudflare/types/web3s/hostnames/ipfs_universal_paths/content_lists/entry_web3_hostname_create_ipfs_universal_path_gateway_content_list_entry_response.py">EntryWeb3HostnameCreateIpfsUniversalPathGatewayContentListEntryResponse</a></code>
- <code title="get /zones/{zone_identifier}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries">client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.<a href="./src/cloudflare/resources/web3s/hostnames/ipfs_universal_paths/content_lists/entries.py">web3_hostname_list_ipfs_universal_path_gateway_content_list_entries</a>(identifier, \*, zone_identifier) -> <a href="./src/cloudflare/types/web3s/hostnames/ipfs_universal_paths/content_lists/entry_web3_hostname_list_ipfs_universal_path_gateway_content_list_entries_response.py">Optional</a></code>

# Workers

## Scripts

Types:

```python
from cloudflare.types.workers import ScriptCreateResponse, ScriptUpdateResponse, ScriptListResponse
```

Methods:

- <code title="put /zones/{zone_id}/workers/script">client.workers.scripts.<a href="./src/cloudflare/resources/workers/scripts/scripts.py">create</a>(zone_id) -> <a href="./src/cloudflare/types/workers/script_create_response.py">ScriptCreateResponse</a></code>
- <code title="put /accounts/{account_id}/workers/scripts/{script_name}">client.workers.scripts.<a href="./src/cloudflare/resources/workers/scripts/scripts.py">update</a>(script_name, \*, account_id, \*\*<a href="src/cloudflare/types/workers/script_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/script_update_response.py">ScriptUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/workers/scripts">client.workers.scripts.<a href="./src/cloudflare/resources/workers/scripts/scripts.py">list</a>(account_id) -> <a href="./src/cloudflare/types/workers/script_list_response.py">ScriptListResponse</a></code>
- <code title="delete /accounts/{account_id}/workers/scripts/{script_name}">client.workers.scripts.<a href="./src/cloudflare/resources/workers/scripts/scripts.py">delete</a>(script_name, \*, account_id, \*\*<a href="src/cloudflare/types/workers/script_delete_params.py">params</a>) -> None</code>
- <code title="get /accounts/{account_id}/workers/scripts/{script_name}">client.workers.scripts.<a href="./src/cloudflare/resources/workers/scripts/scripts.py">get</a>(script_name, \*, account_id) -> BinaryAPIResponse</code>

### Bindings

Types:

```python
from cloudflare.types.workers.scripts import BindingListResponse
```

Methods:

- <code title="get /zones/{zone_id}/workers/script/bindings">client.workers.scripts.bindings.<a href="./src/cloudflare/resources/workers/scripts/bindings.py">list</a>(zone_id) -> <a href="./src/cloudflare/types/workers/scripts/binding_list_response.py">BindingListResponse</a></code>

### Schedules

Types:

```python
from cloudflare.types.workers.scripts import (
    ScheduleWorkerCronTriggerGetCronTriggersResponse,
    ScheduleWorkerCronTriggerUpdateCronTriggersResponse,
)
```

Methods:

- <code title="get /accounts/{account_id}/workers/scripts/{script_name}/schedules">client.workers.scripts.schedules.<a href="./src/cloudflare/resources/workers/scripts/schedules.py">worker_cron_trigger_get_cron_triggers</a>(script_name, \*, account_id) -> <a href="./src/cloudflare/types/workers/scripts/schedule_worker_cron_trigger_get_cron_triggers_response.py">ScheduleWorkerCronTriggerGetCronTriggersResponse</a></code>
- <code title="put /accounts/{account_id}/workers/scripts/{script_name}/schedules">client.workers.scripts.schedules.<a href="./src/cloudflare/resources/workers/scripts/schedules.py">worker_cron_trigger_update_cron_triggers</a>(script_name, \*, account_id, \*\*<a href="src/cloudflare/types/workers/scripts/schedule_worker_cron_trigger_update_cron_triggers_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/scripts/schedule_worker_cron_trigger_update_cron_triggers_response.py">ScheduleWorkerCronTriggerUpdateCronTriggersResponse</a></code>

### Tails

Types:

```python
from cloudflare.types.workers.scripts import (
    TailDeleteResponse,
    TailWorkerTailLogsListTailsResponse,
    TailWorkerTailLogsStartTailResponse,
)
```

Methods:

- <code title="delete /accounts/{account_id}/workers/scripts/{script_name}/tails/{id}">client.workers.scripts.tails.<a href="./src/cloudflare/resources/workers/scripts/tails.py">delete</a>(id, \*, account_id, script_name) -> <a href="./src/cloudflare/types/workers/scripts/tail_delete_response.py">TailDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/workers/scripts/{script_name}/tails">client.workers.scripts.tails.<a href="./src/cloudflare/resources/workers/scripts/tails.py">worker_tail_logs_list_tails</a>(script_name, \*, account_id) -> <a href="./src/cloudflare/types/workers/scripts/tail_worker_tail_logs_list_tails_response.py">TailWorkerTailLogsListTailsResponse</a></code>
- <code title="post /accounts/{account_id}/workers/scripts/{script_name}/tails">client.workers.scripts.tails.<a href="./src/cloudflare/resources/workers/scripts/tails.py">worker_tail_logs_start_tail</a>(script_name, \*, account_id) -> <a href="./src/cloudflare/types/workers/scripts/tail_worker_tail_logs_start_tail_response.py">TailWorkerTailLogsStartTailResponse</a></code>

### UsageModels

Types:

```python
from cloudflare.types.workers.scripts import (
    UsageModelWorkerScriptFetchUsageModelResponse,
    UsageModelWorkerScriptUpdateUsageModelResponse,
)
```

Methods:

- <code title="get /accounts/{account_id}/workers/scripts/{script_name}/usage-model">client.workers.scripts.usage_models.<a href="./src/cloudflare/resources/workers/scripts/usage_models.py">worker_script_fetch_usage_model</a>(script_name, \*, account_id) -> <a href="./src/cloudflare/types/workers/scripts/usage_model_worker_script_fetch_usage_model_response.py">UsageModelWorkerScriptFetchUsageModelResponse</a></code>
- <code title="put /accounts/{account_id}/workers/scripts/{script_name}/usage-model">client.workers.scripts.usage_models.<a href="./src/cloudflare/resources/workers/scripts/usage_models.py">worker_script_update_usage_model</a>(script_name, \*, account_id, \*\*<a href="src/cloudflare/types/workers/scripts/usage_model_worker_script_update_usage_model_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/scripts/usage_model_worker_script_update_usage_model_response.py">UsageModelWorkerScriptUpdateUsageModelResponse</a></code>

## Filters

Types:

```python
from cloudflare.types.workers import (
    FilterUpdateResponse,
    FilterDeleteResponse,
    FilterWorkerFiltersDeprecatedCreateFilterResponse,
    FilterWorkerFiltersDeprecatedListFiltersResponse,
)
```

Methods:

- <code title="put /zones/{zone_id}/workers/filters/{filter_id}">client.workers.filters.<a href="./src/cloudflare/resources/workers/filters.py">update</a>(filter_id, \*, zone_id, \*\*<a href="src/cloudflare/types/workers/filter_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/filter_update_response.py">FilterUpdateResponse</a></code>
- <code title="delete /zones/{zone_id}/workers/filters/{filter_id}">client.workers.filters.<a href="./src/cloudflare/resources/workers/filters.py">delete</a>(filter_id, \*, zone_id) -> <a href="./src/cloudflare/types/workers/filter_delete_response.py">Optional</a></code>
- <code title="post /zones/{zone_id}/workers/filters">client.workers.filters.<a href="./src/cloudflare/resources/workers/filters.py">worker_filters_deprecated_create_filter</a>(zone_id, \*\*<a href="src/cloudflare/types/workers/filter_worker_filters_deprecated_create_filter_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/filter_worker_filters_deprecated_create_filter_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/workers/filters">client.workers.filters.<a href="./src/cloudflare/resources/workers/filters.py">worker_filters_deprecated_list_filters</a>(zone_id) -> <a href="./src/cloudflare/types/workers/filter_worker_filters_deprecated_list_filters_response.py">FilterWorkerFiltersDeprecatedListFiltersResponse</a></code>

## Routes

Types:

```python
from cloudflare.types.workers import (
    RouteUpdateResponse,
    RouteDeleteResponse,
    RouteGetResponse,
    RouteWorkerRoutesCreateRouteResponse,
    RouteWorkerRoutesListRoutesResponse,
)
```

Methods:

- <code title="put /zones/{zone_id}/workers/routes/{route_id}">client.workers.routes.<a href="./src/cloudflare/resources/workers/routes.py">update</a>(route_id, \*, zone_id, \*\*<a href="src/cloudflare/types/workers/route_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/route_update_response.py">RouteUpdateResponse</a></code>
- <code title="delete /zones/{zone_id}/workers/routes/{route_id}">client.workers.routes.<a href="./src/cloudflare/resources/workers/routes.py">delete</a>(route_id, \*, zone_id) -> <a href="./src/cloudflare/types/workers/route_delete_response.py">RouteDeleteResponse</a></code>
- <code title="get /zones/{zone_id}/workers/routes/{route_id}">client.workers.routes.<a href="./src/cloudflare/resources/workers/routes.py">get</a>(route_id, \*, zone_id) -> <a href="./src/cloudflare/types/workers/route_get_response.py">RouteGetResponse</a></code>
- <code title="post /zones/{zone_id}/workers/routes">client.workers.routes.<a href="./src/cloudflare/resources/workers/routes.py">worker_routes_create_route</a>(zone_id, \*\*<a href="src/cloudflare/types/workers/route_worker_routes_create_route_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/route_worker_routes_create_route_response.py">RouteWorkerRoutesCreateRouteResponse</a></code>
- <code title="get /zones/{zone_id}/workers/routes">client.workers.routes.<a href="./src/cloudflare/resources/workers/routes.py">worker_routes_list_routes</a>(zone_id) -> <a href="./src/cloudflare/types/workers/route_worker_routes_list_routes_response.py">RouteWorkerRoutesListRoutesResponse</a></code>

## AccountSettings

Types:

```python
from cloudflare.types.workers import (
    AccountSettingWorkerAccountSettingsCreateWorkerAccountSettingsResponse,
    AccountSettingWorkerAccountSettingsFetchWorkerAccountSettingsResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/workers/account-settings">client.workers.account_settings.<a href="./src/cloudflare/resources/workers/account_settings.py">worker_account_settings_create_worker_account_settings</a>(account_id, \*\*<a href="src/cloudflare/types/workers/account_setting_worker_account_settings_create_worker_account_settings_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/account_setting_worker_account_settings_create_worker_account_settings_response.py">AccountSettingWorkerAccountSettingsCreateWorkerAccountSettingsResponse</a></code>
- <code title="get /accounts/{account_id}/workers/account-settings">client.workers.account_settings.<a href="./src/cloudflare/resources/workers/account_settings.py">worker_account_settings_fetch_worker_account_settings</a>(account_id) -> <a href="./src/cloudflare/types/workers/account_setting_worker_account_settings_fetch_worker_account_settings_response.py">AccountSettingWorkerAccountSettingsFetchWorkerAccountSettingsResponse</a></code>

## Deployments

### ByScripts

Types:

```python
from cloudflare.types.workers.deployments import ByScriptWorkerDeploymentsListDeploymentsResponse
```

Methods:

- <code title="get /accounts/{account_id}/workers/deployments/by-script/{script_id}">client.workers.deployments.by_scripts.<a href="./src/cloudflare/resources/workers/deployments/by_scripts/by_scripts.py">worker_deployments_list_deployments</a>(script_id, \*, account_id) -> <a href="./src/cloudflare/types/workers/deployments/by_script_worker_deployments_list_deployments_response.py">ByScriptWorkerDeploymentsListDeploymentsResponse</a></code>

#### Details

Types:

```python
from cloudflare.types.workers.deployments.by_scripts import DetailGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/workers/deployments/by-script/{script_id}/detail/{deployment_id}">client.workers.deployments.by_scripts.details.<a href="./src/cloudflare/resources/workers/deployments/by_scripts/details.py">get</a>(deployment_id, \*, account_id, script_id) -> <a href="./src/cloudflare/types/workers/deployments/by_scripts/detail_get_response.py">DetailGetResponse</a></code>

## Domains

Types:

```python
from cloudflare.types.workers import (
    DomainGetResponse,
    DomainWorkerDomainAttachToDomainResponse,
    DomainWorkerDomainListDomainsResponse,
)
```

Methods:

- <code title="delete /accounts/{account_id}/workers/domains/{domain_id}">client.workers.domains.<a href="./src/cloudflare/resources/workers/domains.py">delete</a>(domain_id, \*, account_id) -> None</code>
- <code title="get /accounts/{account_id}/workers/domains/{domain_id}">client.workers.domains.<a href="./src/cloudflare/resources/workers/domains.py">get</a>(domain_id, \*, account_id) -> <a href="./src/cloudflare/types/workers/domain_get_response.py">DomainGetResponse</a></code>
- <code title="put /accounts/{account_id}/workers/domains">client.workers.domains.<a href="./src/cloudflare/resources/workers/domains.py">worker_domain_attach_to_domain</a>(account_id, \*\*<a href="src/cloudflare/types/workers/domain_worker_domain_attach_to_domain_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/domain_worker_domain_attach_to_domain_response.py">DomainWorkerDomainAttachToDomainResponse</a></code>
- <code title="get /accounts/{account_id}/workers/domains">client.workers.domains.<a href="./src/cloudflare/resources/workers/domains.py">worker_domain_list_domains</a>(account_id, \*\*<a href="src/cloudflare/types/workers/domain_worker_domain_list_domains_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/domain_worker_domain_list_domains_response.py">DomainWorkerDomainListDomainsResponse</a></code>

## DurableObjects

### Namespaces

Types:

```python
from cloudflare.types.workers.durable_objects import NamespaceListResponse
```

Methods:

- <code title="get /accounts/{account_id}/workers/durable_objects/namespaces">client.workers.durable_objects.namespaces.<a href="./src/cloudflare/resources/workers/durable_objects/namespaces/namespaces.py">list</a>(account_id) -> <a href="./src/cloudflare/types/workers/durable_objects/namespace_list_response.py">Optional</a></code>

#### Objects

Types:

```python
from cloudflare.types.workers.durable_objects.namespaces import ObjectListResponse
```

Methods:

- <code title="get /accounts/{account_id}/workers/durable_objects/namespaces/{id}/objects">client.workers.durable_objects.namespaces.objects.<a href="./src/cloudflare/resources/workers/durable_objects/namespaces/objects.py">list</a>(id, \*, account_id, \*\*<a href="src/cloudflare/types/workers/durable_objects/namespaces/object_list_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/durable_objects/namespaces/object_list_response.py">Optional</a></code>

## Queues

Types:

```python
from cloudflare.types.workers import (
    QueueUpdateResponse,
    QueueListResponse,
    QueueDeleteResponse,
    QueueGetResponse,
    QueueQueueCreateQueueResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/workers/queues/{name}">client.workers.queues.<a href="./src/cloudflare/resources/workers/queues/queues.py">update</a>(name, \*, account_id, \*\*<a href="src/cloudflare/types/workers/queue_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/queue_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/workers/queues">client.workers.queues.<a href="./src/cloudflare/resources/workers/queues/queues.py">list</a>(account_id) -> <a href="./src/cloudflare/types/workers/queue_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/workers/queues/{name}">client.workers.queues.<a href="./src/cloudflare/resources/workers/queues/queues.py">delete</a>(name, \*, account_id) -> <a href="./src/cloudflare/types/workers/queue_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/workers/queues/{name}">client.workers.queues.<a href="./src/cloudflare/resources/workers/queues/queues.py">get</a>(name, \*, account_id) -> <a href="./src/cloudflare/types/workers/queue_get_response.py">Optional</a></code>
- <code title="post /accounts/{account_id}/workers/queues">client.workers.queues.<a href="./src/cloudflare/resources/workers/queues/queues.py">queue_create_queue</a>(account_id, \*\*<a href="src/cloudflare/types/workers/queue_queue_create_queue_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/queue_queue_create_queue_response.py">Optional</a></code>

### Consumers

Types:

```python
from cloudflare.types.workers.queues import (
    ConsumerUpdateResponse,
    ConsumerListResponse,
    ConsumerDeleteResponse,
    ConsumerQueueCreateQueueConsumerResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/workers/queues/{name}/consumers/{consumer_name}">client.workers.queues.consumers.<a href="./src/cloudflare/resources/workers/queues/consumers.py">update</a>(consumer_name, \*, account_id, name, \*\*<a href="src/cloudflare/types/workers/queues/consumer_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/queues/consumer_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/workers/queues/{name}/consumers">client.workers.queues.consumers.<a href="./src/cloudflare/resources/workers/queues/consumers.py">list</a>(name, \*, account_id) -> <a href="./src/cloudflare/types/workers/queues/consumer_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/workers/queues/{name}/consumers/{consumer_name}">client.workers.queues.consumers.<a href="./src/cloudflare/resources/workers/queues/consumers.py">delete</a>(consumer_name, \*, account_id, name) -> <a href="./src/cloudflare/types/workers/queues/consumer_delete_response.py">Optional</a></code>
- <code title="post /accounts/{account_id}/workers/queues/{name}/consumers">client.workers.queues.consumers.<a href="./src/cloudflare/resources/workers/queues/consumers.py">queue_create_queue_consumer</a>(name, \*, account_id, \*\*<a href="src/cloudflare/types/workers/queues/consumer_queue_create_queue_consumer_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/queues/consumer_queue_create_queue_consumer_response.py">Optional</a></code>

## Subdomains

Types:

```python
from cloudflare.types.workers import (
    SubdomainWorkerSubdomainCreateSubdomainResponse,
    SubdomainWorkerSubdomainGetSubdomainResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/workers/subdomain">client.workers.subdomains.<a href="./src/cloudflare/resources/workers/subdomains.py">worker_subdomain_create_subdomain</a>(account_id, \*\*<a href="src/cloudflare/types/workers/subdomain_worker_subdomain_create_subdomain_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/subdomain_worker_subdomain_create_subdomain_response.py">SubdomainWorkerSubdomainCreateSubdomainResponse</a></code>
- <code title="get /accounts/{account_id}/workers/subdomain">client.workers.subdomains.<a href="./src/cloudflare/resources/workers/subdomains.py">worker_subdomain_get_subdomain</a>(account_id) -> <a href="./src/cloudflare/types/workers/subdomain_worker_subdomain_get_subdomain_response.py">SubdomainWorkerSubdomainGetSubdomainResponse</a></code>

## DeploymentsByScript

Types:

```python
from cloudflare.types.workers import (
    DeploymentsByScriptListResponse,
    DeploymentsByScriptDetailResponse,
)
```

Methods:

- <code title="get /accounts/{account_id}/workers/deployments/by-script/{script_id}">client.workers.deployments_by_script.<a href="./src/cloudflare/resources/workers/deployments_by_script.py">list</a>(script_id, \*, account_id) -> <a href="./src/cloudflare/types/workers/deployments_by_script_list_response.py">DeploymentsByScriptListResponse</a></code>
- <code title="get /accounts/{account_id}/workers/deployments/by-script/{script_id}/detail/{deployment_id}">client.workers.deployments_by_script.<a href="./src/cloudflare/resources/workers/deployments_by_script.py">detail</a>(deployment_id, \*, account_id, script_id) -> <a href="./src/cloudflare/types/workers/deployments_by_script_detail_response.py">DeploymentsByScriptDetailResponse</a></code>

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
from cloudflare.types.workers.services.environments import SettingGetResponse, SettingModifyResponse
```

Methods:

- <code title="get /accounts/{account_id}/workers/services/{service_name}/environments/{environment_name}/settings">client.workers.services.environments.settings.<a href="./src/cloudflare/resources/workers/services/environments/settings.py">get</a>(environment_name, \*, account_id, service_name) -> <a href="./src/cloudflare/types/workers/services/environments/setting_get_response.py">SettingGetResponse</a></code>
- <code title="patch /accounts/{account_id}/workers/services/{service_name}/environments/{environment_name}/settings">client.workers.services.environments.settings.<a href="./src/cloudflare/resources/workers/services/environments/settings.py">modify</a>(environment_name, \*, account_id, service_name, \*\*<a href="src/cloudflare/types/workers/services/environments/setting_modify_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/services/environments/setting_modify_response.py">SettingModifyResponse</a></code>

## Script

Methods:

- <code title="delete /zones/{zone_id}/workers/script">client.workers.script.<a href="./src/cloudflare/resources/workers/script.py">delete</a>(zone_id) -> None</code>

# ActivationChecks

Types:

```python
from cloudflare.types import ActivationCheckPutZonesZoneIDActivationCheckResponse
```

Methods:

- <code title="put /zones/{zone_id}/activation_check">client.activation_checks.<a href="./src/cloudflare/resources/activation_checks.py">put_zones_zone_id_activation_check</a>(zone_id) -> <a href="./src/cloudflare/types/activation_check_put_zones_zone_id_activation_check_response.py">ActivationCheckPutZonesZoneIDActivationCheckResponse</a></code>

# APIGateways

## Configurations

Types:

```python
from cloudflare.types.api_gateways import (
    ConfigurationAPIShieldSettingsGetInformationAboutSpecificConfigurationPropertiesResponse,
    ConfigurationAPIShieldSettingsSetConfigurationPropertiesResponse,
)
```

Methods:

- <code title="get /zones/{zone_id}/api_gateway/configuration">client.api_gateways.configurations.<a href="./src/cloudflare/resources/api_gateways/configurations.py">api_shield_settings_get_information_about_specific_configuration_properties</a>(zone_id, \*\*<a href="src/cloudflare/types/api_gateways/configuration_api_shield_settings_get_information_about_specific_configuration_properties_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateways/configuration_api_shield_settings_get_information_about_specific_configuration_properties_response.py">ConfigurationAPIShieldSettingsGetInformationAboutSpecificConfigurationPropertiesResponse</a></code>
- <code title="put /zones/{zone_id}/api_gateway/configuration">client.api_gateways.configurations.<a href="./src/cloudflare/resources/api_gateways/configurations.py">api_shield_settings_set_configuration_properties</a>(zone_id, \*\*<a href="src/cloudflare/types/api_gateways/configuration_api_shield_settings_set_configuration_properties_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateways/configuration_api_shield_settings_set_configuration_properties_response.py">ConfigurationAPIShieldSettingsSetConfigurationPropertiesResponse</a></code>

## Discoveries

Types:

```python
from cloudflare.types.api_gateways import (
    DiscoveryAPIShieldEndpointManagementGetAPIDiscoveryResultsForAZoneResponse,
)
```

Methods:

- <code title="get /zones/{zone_id}/api_gateway/discovery">client.api_gateways.discoveries.<a href="./src/cloudflare/resources/api_gateways/discoveries.py">api_shield_endpoint_management_get_api_discovery_results_for_a_zone</a>(zone_id) -> <a href="./src/cloudflare/types/api_gateways/discovery_api_shield_endpoint_management_get_api_discovery_results_for_a_zone_response.py">DiscoveryAPIShieldEndpointManagementGetAPIDiscoveryResultsForAZoneResponse</a></code>

## Operations

Types:

```python
from cloudflare.types.api_gateways import (
    OperationUpdateResponse,
    OperationListResponse,
    OperationDeleteResponse,
    OperationAPIShieldEndpointManagementAddOperationsToAZoneResponse,
    OperationAPIShieldEndpointManagementGetInformationAboutAllOperationsOnAZoneResponse,
    OperationGetResponse,
)
```

Methods:

- <code title="patch /zones/{zone_id}/api_gateway/discovery/operations/{operation_id}">client.api_gateways.operations.<a href="./src/cloudflare/resources/api_gateways/operations.py">update</a>(operation_id, \*, zone_id, \*\*<a href="src/cloudflare/types/api_gateways/operation_update_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateways/operation_update_response.py">OperationUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/api_gateway/discovery/operations">client.api_gateways.operations.<a href="./src/cloudflare/resources/api_gateways/operations.py">list</a>(zone_id, \*\*<a href="src/cloudflare/types/api_gateways/operation_list_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateways/operation_list_response.py">Optional</a></code>
- <code title="delete /zones/{zone_id}/api_gateway/operations/{operation_id}">client.api_gateways.operations.<a href="./src/cloudflare/resources/api_gateways/operations.py">delete</a>(operation_id, \*, zone_id) -> <a href="./src/cloudflare/types/api_gateways/operation_delete_response.py">OperationDeleteResponse</a></code>
- <code title="post /zones/{zone_id}/api_gateway/operations">client.api_gateways.operations.<a href="./src/cloudflare/resources/api_gateways/operations.py">api_shield_endpoint_management_add_operations_to_a_zone</a>(zone_id, \*\*<a href="src/cloudflare/types/api_gateways/operation_api_shield_endpoint_management_add_operations_to_a_zone_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateways/operation_api_shield_endpoint_management_add_operations_to_a_zone_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/api_gateway/operations">client.api_gateways.operations.<a href="./src/cloudflare/resources/api_gateways/operations.py">api_shield_endpoint_management_get_information_about_all_operations_on_a_zone</a>(zone_id, \*\*<a href="src/cloudflare/types/api_gateways/operation_api_shield_endpoint_management_get_information_about_all_operations_on_a_zone_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateways/operation_api_shield_endpoint_management_get_information_about_all_operations_on_a_zone_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/api_gateway/operations/{operation_id}">client.api_gateways.operations.<a href="./src/cloudflare/resources/api_gateways/operations.py">get</a>(operation_id, \*, zone_id, \*\*<a href="src/cloudflare/types/api_gateways/operation_get_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateways/operation_get_response.py">OperationGetResponse</a></code>

## Schemas

Types:

```python
from cloudflare.types.api_gateways import (
    SchemaUpdateResponse,
    SchemaAPIShieldEndpointManagementGetOperationsAndFeaturesAsOpenAPISchemasResponse,
    SchemaGetResponse,
    SchemaUpdateMultipleResponse,
)
```

Methods:

- <code title="put /zones/{zone_id}/api_gateway/operations/{operation_id}/schema_validation">client.api_gateways.schemas.<a href="./src/cloudflare/resources/api_gateways/schemas.py">update</a>(operation_id, \*, zone_id, \*\*<a href="src/cloudflare/types/api_gateways/schema_update_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateways/schema_update_response.py">SchemaUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/api_gateway/schemas">client.api_gateways.schemas.<a href="./src/cloudflare/resources/api_gateways/schemas.py">api_shield_endpoint_management_get_operations_and_features_as_open_api_schemas</a>(zone_id, \*\*<a href="src/cloudflare/types/api_gateways/schema_api_shield_endpoint_management_get_operations_and_features_as_open_api_schemas_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateways/schema_api_shield_endpoint_management_get_operations_and_features_as_open_api_schemas_response.py">SchemaAPIShieldEndpointManagementGetOperationsAndFeaturesAsOpenAPISchemasResponse</a></code>
- <code title="get /zones/{zone_id}/api_gateway/operations/{operation_id}/schema_validation">client.api_gateways.schemas.<a href="./src/cloudflare/resources/api_gateways/schemas.py">get</a>(operation_id, \*, zone_id) -> <a href="./src/cloudflare/types/api_gateways/schema_get_response.py">SchemaGetResponse</a></code>
- <code title="get /zones/{zone_id}/api_gateway/settings/schema_validation">client.api_gateways.schemas.<a href="./src/cloudflare/resources/api_gateways/schemas.py">get_incremental</a>(zone_id) -> <a href="./src/cloudflare/types/api_gateways/settings/api_shield_zone_schema_validation_settings.py">APIShieldZoneSchemaValidationSettings</a></code>
- <code title="patch /zones/{zone_id}/api_gateway/operations/schema_validation">client.api_gateways.schemas.<a href="./src/cloudflare/resources/api_gateways/schemas.py">update_multiple</a>(zone_id, \*\*<a href="src/cloudflare/types/api_gateways/schema_update_multiple_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateways/schema_update_multiple_response.py">SchemaUpdateMultipleResponse</a></code>

## Settings

### SchemaValidation

Types:

```python
from cloudflare.types.api_gateways.settings import APIShieldZoneSchemaValidationSettings
```

Methods:

- <code title="put /zones/{zone_id}/api_gateway/settings/schema_validation">client.api_gateways.settings.schema_validation.<a href="./src/cloudflare/resources/api_gateways/settings/schema_validation.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/api_gateways/settings/schema_validation_update_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateways/settings/api_shield_zone_schema_validation_settings.py">APIShieldZoneSchemaValidationSettings</a></code>

## UserSchemas

Types:

```python
from cloudflare.types.api_gateways import (
    APIShieldAPIResponseSingle,
    APIShieldMessages,
    APIShieldPublicSchema,
    APIShieldSchemaUploadResponse,
    UserSchemaListResponse,
    UserSchemaDeleteResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/api_gateway/user_schemas">client.api_gateways.user_schemas.<a href="./src/cloudflare/resources/api_gateways/user_schemas/user_schemas.py">create</a>(zone_id, \*\*<a href="src/cloudflare/types/api_gateways/user_schema_create_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateways/api_shield_schema_upload_response.py">APIShieldSchemaUploadResponse</a></code>
- <code title="patch /zones/{zone_id}/api_gateway/user_schemas/{schema_id}">client.api_gateways.user_schemas.<a href="./src/cloudflare/resources/api_gateways/user_schemas/user_schemas.py">update</a>(schema_id, \*, zone_id, \*\*<a href="src/cloudflare/types/api_gateways/user_schema_update_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateways/api_shield_public_schema.py">APIShieldPublicSchema</a></code>
- <code title="get /zones/{zone_id}/api_gateway/user_schemas">client.api_gateways.user_schemas.<a href="./src/cloudflare/resources/api_gateways/user_schemas/user_schemas.py">list</a>(zone_id, \*\*<a href="src/cloudflare/types/api_gateways/user_schema_list_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateways/user_schema_list_response.py">Optional</a></code>
- <code title="delete /zones/{zone_id}/api_gateway/user_schemas/{schema_id}">client.api_gateways.user_schemas.<a href="./src/cloudflare/resources/api_gateways/user_schemas/user_schemas.py">delete</a>(schema_id, \*, zone_id) -> <a href="./src/cloudflare/types/api_gateways/user_schema_delete_response.py">UserSchemaDeleteResponse</a></code>
- <code title="get /zones/{zone_id}/api_gateway/user_schemas/{schema_id}">client.api_gateways.user_schemas.<a href="./src/cloudflare/resources/api_gateways/user_schemas/user_schemas.py">get</a>(schema_id, \*, zone_id, \*\*<a href="src/cloudflare/types/api_gateways/user_schema_get_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateways/api_shield_public_schema.py">APIShieldPublicSchema</a></code>

### Operations

Types:

```python
from cloudflare.types.api_gateways.user_schemas import OperationListResponse
```

Methods:

- <code title="get /zones/{zone_id}/api_gateway/user_schemas/{schema_id}/operations">client.api_gateways.user_schemas.operations.<a href="./src/cloudflare/resources/api_gateways/user_schemas/operations.py">list</a>(schema_id, \*, zone_id, \*\*<a href="src/cloudflare/types/api_gateways/user_schemas/operation_list_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateways/user_schemas/operation_list_response.py">Optional</a></code>

## Discovery

### Operations

Types:

```python
from cloudflare.types.api_gateways.discovery import OperationUpdateResponse
```

Methods:

- <code title="patch /zones/{zone_id}/api_gateway/discovery/operations">client.api_gateways.discovery.operations.<a href="./src/cloudflare/resources/api_gateways/discovery/operations.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/api_gateways/discovery/operation_update_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateways/discovery/operation_update_response.py">OperationUpdateResponse</a></code>

## SchemaValidation

Methods:

- <code title="patch /zones/{zone_id}/api_gateway/settings/schema_validation">client.api_gateways.schema_validation.<a href="./src/cloudflare/resources/api_gateways/schema_validation.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/api_gateways/schema_validation_update_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateways/settings/api_shield_zone_schema_validation_settings.py">APIShieldZoneSchemaValidationSettings</a></code>

# ManagedHeaders

Types:

```python
from cloudflare.types import (
    ManagedHeaderListResponse,
    ManagedHeaderManagedTransformsUpdateStatusOfManagedTransformsResponse,
)
```

Methods:

- <code title="get /zones/{zone_id}/managed_headers">client.managed_headers.<a href="./src/cloudflare/resources/managed_headers.py">list</a>(zone_id) -> <a href="./src/cloudflare/types/managed_header_list_response.py">ManagedHeaderListResponse</a></code>
- <code title="patch /zones/{zone_id}/managed_headers">client.managed_headers.<a href="./src/cloudflare/resources/managed_headers.py">managed_transforms_update_status_of_managed_transforms</a>(zone_id, \*\*<a href="src/cloudflare/types/managed_header_managed_transforms_update_status_of_managed_transforms_params.py">params</a>) -> <a href="./src/cloudflare/types/managed_header_managed_transforms_update_status_of_managed_transforms_response.py">ManagedHeaderManagedTransformsUpdateStatusOfManagedTransformsResponse</a></code>

# PageShields

Types:

```python
from cloudflare.types import (
    PageShieldListResponse,
    PageShieldPageShieldUpdatePageShieldSettingsResponse,
)
```

Methods:

- <code title="get /zones/{zone_id}/page_shield">client.page_shields.<a href="./src/cloudflare/resources/page_shields/page_shields.py">list</a>(zone_id) -> <a href="./src/cloudflare/types/page_shield_list_response.py">PageShieldListResponse</a></code>
- <code title="put /zones/{zone_id}/page_shield">client.page_shields.<a href="./src/cloudflare/resources/page_shields/page_shields.py">page_shield_update_page_shield_settings</a>(zone_id, \*\*<a href="src/cloudflare/types/page_shield_page_shield_update_page_shield_settings_params.py">params</a>) -> <a href="./src/cloudflare/types/page_shield_page_shield_update_page_shield_settings_response.py">PageShieldPageShieldUpdatePageShieldSettingsResponse</a></code>

## Connections

Types:

```python
from cloudflare.types.page_shields import (
    ConnectionGetResponse,
    ConnectionPageShieldListPageShieldConnectionsResponse,
)
```

Methods:

- <code title="get /zones/{zone_id}/page_shield/connections/{connection_id}">client.page_shields.connections.<a href="./src/cloudflare/resources/page_shields/connections.py">get</a>(connection_id, \*, zone_id) -> <a href="./src/cloudflare/types/page_shields/connection_get_response.py">ConnectionGetResponse</a></code>
- <code title="get /zones/{zone_id}/page_shield/connections">client.page_shields.connections.<a href="./src/cloudflare/resources/page_shields/connections.py">page_shield_list_page_shield_connections</a>(zone_id, \*\*<a href="src/cloudflare/types/page_shields/connection_page_shield_list_page_shield_connections_params.py">params</a>) -> <a href="./src/cloudflare/types/page_shields/connection_page_shield_list_page_shield_connections_response.py">Optional</a></code>

## Scripts

Types:

```python
from cloudflare.types.page_shields import (
    ScriptGetResponse,
    ScriptPageShieldListPageShieldScriptsResponse,
)
```

Methods:

- <code title="get /zones/{zone_id}/page_shield/scripts/{script_id}">client.page_shields.scripts.<a href="./src/cloudflare/resources/page_shields/scripts.py">get</a>(script_id, \*, zone_id) -> <a href="./src/cloudflare/types/page_shields/script_get_response.py">ScriptGetResponse</a></code>
- <code title="get /zones/{zone_id}/page_shield/scripts">client.page_shields.scripts.<a href="./src/cloudflare/resources/page_shields/scripts.py">page_shield_list_page_shield_scripts</a>(zone_id, \*\*<a href="src/cloudflare/types/page_shields/script_page_shield_list_page_shield_scripts_params.py">params</a>) -> <a href="./src/cloudflare/types/page_shields/script_page_shield_list_page_shield_scripts_response.py">Optional</a></code>

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

- <code title="post /{account_or_zone}/{account_or_zone_id}/rulesets">client.rulesets.<a href="./src/cloudflare/resources/rulesets/rulesets.py">create</a>(account_or_zone_id, \*, account_or_zone, \*\*<a href="src/cloudflare/types/ruleset_create_params.py">params</a>) -> <a href="./src/cloudflare/types/ruleset_create_response.py">RulesetCreateResponse</a></code>
- <code title="put /{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}">client.rulesets.<a href="./src/cloudflare/resources/rulesets/rulesets.py">update</a>(ruleset_id, \*, account_or_zone, account_or_zone_id, \*\*<a href="src/cloudflare/types/ruleset_update_params.py">params</a>) -> <a href="./src/cloudflare/types/ruleset_update_response.py">RulesetUpdateResponse</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/rulesets">client.rulesets.<a href="./src/cloudflare/resources/rulesets/rulesets.py">list</a>(account_or_zone_id, \*, account_or_zone) -> <a href="./src/cloudflare/types/ruleset_list_response.py">RulesetListResponse</a></code>
- <code title="delete /{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}">client.rulesets.<a href="./src/cloudflare/resources/rulesets/rulesets.py">delete</a>(ruleset_id, \*, account_or_zone, account_or_zone_id) -> None</code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}">client.rulesets.<a href="./src/cloudflare/resources/rulesets/rulesets.py">get</a>(ruleset_id, \*, account_or_zone, account_or_zone_id) -> <a href="./src/cloudflare/types/ruleset_get_response.py">RulesetGetResponse</a></code>

## Phases

Types:

```python
from cloudflare.types.rulesets import PhaseGetResponse
```

Methods:

- <code title="get /{account_or_zone}/{account_or_zone_id}/rulesets/phases/{ruleset_phase}/entrypoint">client.rulesets.phases.<a href="./src/cloudflare/resources/rulesets/phases.py">get</a>(ruleset_phase, \*, account_or_zone, account_or_zone_id) -> <a href="./src/cloudflare/types/rulesets/phase_get_response.py">PhaseGetResponse</a></code>

## Rules

Types:

```python
from cloudflare.types.rulesets import (
    RuleUpdateResponse,
    RuleDeleteResponse,
    RuleAccountRulesetsCreateAnAccountRulesetRuleResponse,
)
```

Methods:

- <code title="patch /{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/rules/{rule_id}">client.rulesets.rules.<a href="./src/cloudflare/resources/rulesets/rules.py">update</a>(rule_id, \*, account_id, ruleset_id, \*\*<a href="src/cloudflare/types/rulesets/rule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/rulesets/rule_update_response.py">RuleUpdateResponse</a></code>
- <code title="delete /{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/rules/{rule_id}">client.rulesets.rules.<a href="./src/cloudflare/resources/rulesets/rules.py">delete</a>(rule_id, \*, account_or_zone, account_or_zone_id, ruleset_id) -> <a href="./src/cloudflare/types/rulesets/rule_delete_response.py">RuleDeleteResponse</a></code>
- <code title="post /{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/rules">client.rulesets.rules.<a href="./src/cloudflare/resources/rulesets/rules.py">account_rulesets_create_an_account_ruleset_rule</a>(ruleset_id, \*, account_or_zone, account_or_zone_id, \*\*<a href="src/cloudflare/types/rulesets/rule_account_rulesets_create_an_account_ruleset_rule_params.py">params</a>) -> <a href="./src/cloudflare/types/rulesets/rule_account_rulesets_create_an_account_ruleset_rule_response.py">RuleAccountRulesetsCreateAnAccountRulesetRuleResponse</a></code>

## Versions

Types:

```python
from cloudflare.types.rulesets import (
    VersionAccountRulesetsListAnAccountRulesetSVersionsResponse,
    VersionGetResponse,
)
```

Methods:

- <code title="delete /{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/versions/{ruleset_version}">client.rulesets.versions.<a href="./src/cloudflare/resources/rulesets/versions/versions.py">delete</a>(ruleset_version, \*, account_or_zone, account_or_zone_id, ruleset_id) -> None</code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/versions">client.rulesets.versions.<a href="./src/cloudflare/resources/rulesets/versions/versions.py">account_rulesets_list_an_account_ruleset_s_versions</a>(ruleset_id, \*, account_or_zone, account_or_zone_id) -> <a href="./src/cloudflare/types/rulesets/version_account_rulesets_list_an_account_ruleset_s_versions_response.py">VersionAccountRulesetsListAnAccountRulesetSVersionsResponse</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/versions/{ruleset_version}">client.rulesets.versions.<a href="./src/cloudflare/resources/rulesets/versions/versions.py">get</a>(ruleset_version, \*, account_or_zone, account_or_zone_id, ruleset_id) -> <a href="./src/cloudflare/types/rulesets/version_get_response.py">VersionGetResponse</a></code>

### ByTags

Types:

```python
from cloudflare.types.rulesets.versions import ByTagGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/rulesets/{ruleset_id}/versions/{ruleset_version}/by_tag/{rule_tag}">client.rulesets.versions.by_tags.<a href="./src/cloudflare/resources/rulesets/versions/by_tags.py">get</a>(rule_tag, \*, account_id, ruleset_id, ruleset_version) -> <a href="./src/cloudflare/types/rulesets/versions/by_tag_get_response.py">ByTagGetResponse</a></code>

# URLNormalizations

Types:

```python
from cloudflare.types import (
    URLNormalizationURLNormalizationGetURLNormalizationSettingsResponse,
    URLNormalizationURLNormalizationUpdateURLNormalizationSettingsResponse,
)
```

Methods:

- <code title="get /zones/{zone_id}/url_normalization">client.url_normalizations.<a href="./src/cloudflare/resources/url_normalizations.py">url_normalization_get_url_normalization_settings</a>(zone_id) -> <a href="./src/cloudflare/types/url_normalization_url_normalization_get_url_normalization_settings_response.py">URLNormalizationURLNormalizationGetURLNormalizationSettingsResponse</a></code>
- <code title="put /zones/{zone_id}/url_normalization">client.url_normalizations.<a href="./src/cloudflare/resources/url_normalizations.py">url_normalization_update_url_normalization_settings</a>(zone_id, \*\*<a href="src/cloudflare/types/url_normalization_url_normalization_update_url_normalization_settings_params.py">params</a>) -> <a href="./src/cloudflare/types/url_normalization_url_normalization_update_url_normalization_settings_response.py">URLNormalizationURLNormalizationUpdateURLNormalizationSettingsResponse</a></code>

# Spectrums

## Analytics

### Aggregates

#### Currents

Types:

```python
from cloudflare.types.spectrums.analytics.aggregates import (
    CurrentSpectrumAggregateAnalyticsGetCurrentAggregatedAnalyticsResponse,
)
```

Methods:

- <code title="get /zones/{zone}/spectrum/analytics/aggregate/current">client.spectrums.analytics.aggregates.currents.<a href="./src/cloudflare/resources/spectrums/analytics/aggregates/currents.py">spectrum_aggregate_analytics_get_current_aggregated_analytics</a>(zone, \*\*<a href="src/cloudflare/types/spectrums/analytics/aggregates/current_spectrum_aggregate_analytics_get_current_aggregated_analytics_params.py">params</a>) -> <a href="./src/cloudflare/types/spectrums/analytics/aggregates/current_spectrum_aggregate_analytics_get_current_aggregated_analytics_response.py">CurrentSpectrumAggregateAnalyticsGetCurrentAggregatedAnalyticsResponse</a></code>

### Events

#### Bytimes

Types:

```python
from cloudflare.types.spectrums.analytics.events import (
    BytimeSpectrumAnalyticsByTimeGetAnalyticsByTimeResponse,
)
```

Methods:

- <code title="get /zones/{zone}/spectrum/analytics/events/bytime">client.spectrums.analytics.events.bytimes.<a href="./src/cloudflare/resources/spectrums/analytics/events/bytimes.py">spectrum_analytics_by_time_get_analytics_by_time</a>(zone, \*\*<a href="src/cloudflare/types/spectrums/analytics/events/bytime_spectrum_analytics_by_time_get_analytics_by_time_params.py">params</a>) -> <a href="./src/cloudflare/types/spectrums/analytics/events/bytime_spectrum_analytics_by_time_get_analytics_by_time_response.py">Optional</a></code>

#### Summaries

Types:

```python
from cloudflare.types.spectrums.analytics.events import (
    SummarySpectrumAnalyticsSummaryGetAnalyticsSummaryResponse,
)
```

Methods:

- <code title="get /zones/{zone}/spectrum/analytics/events/summary">client.spectrums.analytics.events.summaries.<a href="./src/cloudflare/resources/spectrums/analytics/events/summaries.py">spectrum_analytics_summary_get_analytics_summary</a>(zone, \*\*<a href="src/cloudflare/types/spectrums/analytics/events/summary_spectrum_analytics_summary_get_analytics_summary_params.py">params</a>) -> <a href="./src/cloudflare/types/spectrums/analytics/events/summary_spectrum_analytics_summary_get_analytics_summary_response.py">Optional</a></code>

## Apps

Types:

```python
from cloudflare.types.spectrums import (
    AppUpdateResponse,
    AppDeleteResponse,
    AppGetResponse,
    AppSpectrumApplicationsCreateSpectrumApplicationUsingANameForTheOriginResponse,
    AppSpectrumApplicationsListSpectrumApplicationsResponse,
)
```

Methods:

- <code title="put /zones/{zone}/spectrum/apps/{app_id}">client.spectrums.apps.<a href="./src/cloudflare/resources/spectrums/apps.py">update</a>(app_id, \*, zone, \*\*<a href="src/cloudflare/types/spectrums/app_update_params.py">params</a>) -> <a href="./src/cloudflare/types/spectrums/app_update_response.py">Optional</a></code>
- <code title="delete /zones/{zone}/spectrum/apps/{app_id}">client.spectrums.apps.<a href="./src/cloudflare/resources/spectrums/apps.py">delete</a>(app_id, \*, zone) -> <a href="./src/cloudflare/types/spectrums/app_delete_response.py">Optional</a></code>
- <code title="get /zones/{zone}/spectrum/apps/{app_id}">client.spectrums.apps.<a href="./src/cloudflare/resources/spectrums/apps.py">get</a>(app_id, \*, zone) -> <a href="./src/cloudflare/types/spectrums/app_get_response.py">Optional</a></code>
- <code title="post /zones/{zone}/spectrum/apps">client.spectrums.apps.<a href="./src/cloudflare/resources/spectrums/apps.py">spectrum_applications_create_spectrum_application_using_a_name_for_the_origin</a>(zone, \*\*<a href="src/cloudflare/types/spectrums/app_spectrum_applications_create_spectrum_application_using_a_name_for_the_origin_params.py">params</a>) -> <a href="./src/cloudflare/types/spectrums/app_spectrum_applications_create_spectrum_application_using_a_name_for_the_origin_response.py">Optional</a></code>
- <code title="get /zones/{zone}/spectrum/apps">client.spectrums.apps.<a href="./src/cloudflare/resources/spectrums/apps.py">spectrum_applications_list_spectrum_applications</a>(zone, \*\*<a href="src/cloudflare/types/spectrums/app_spectrum_applications_list_spectrum_applications_params.py">params</a>) -> <a href="./src/cloudflare/types/spectrums/app_spectrum_applications_list_spectrum_applications_response.py">Optional</a></code>

# Addresses

## AddressMaps

Types:

```python
from cloudflare.types.addresses import (
    AddressMapCreateResponse,
    AddressMapUpdateResponse,
    AddressMapListResponse,
    AddressMapDeleteResponse,
    AddressMapGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_identifier}/addressing/address_maps">client.addresses.address_maps.<a href="./src/cloudflare/resources/addresses/address_maps/address_maps.py">create</a>(account_identifier, \*\*<a href="src/cloudflare/types/addresses/address_map_create_params.py">params</a>) -> <a href="./src/cloudflare/types/addresses/address_map_create_response.py">AddressMapCreateResponse</a></code>
- <code title="patch /accounts/{account_identifier}/addressing/address_maps/{address_map_identifier}">client.addresses.address_maps.<a href="./src/cloudflare/resources/addresses/address_maps/address_maps.py">update</a>(address_map_identifier, \*, account_identifier, \*\*<a href="src/cloudflare/types/addresses/address_map_update_params.py">params</a>) -> <a href="./src/cloudflare/types/addresses/address_map_update_response.py">AddressMapUpdateResponse</a></code>
- <code title="get /accounts/{account_identifier}/addressing/address_maps">client.addresses.address_maps.<a href="./src/cloudflare/resources/addresses/address_maps/address_maps.py">list</a>(account_identifier) -> <a href="./src/cloudflare/types/addresses/address_map_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_identifier}/addressing/address_maps/{address_map_identifier}">client.addresses.address_maps.<a href="./src/cloudflare/resources/addresses/address_maps/address_maps.py">delete</a>(address_map_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/addresses/address_map_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_identifier}/addressing/address_maps/{address_map_identifier}">client.addresses.address_maps.<a href="./src/cloudflare/resources/addresses/address_maps/address_maps.py">get</a>(address_map_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/addresses/address_map_get_response.py">AddressMapGetResponse</a></code>

### Accounts

Types:

```python
from cloudflare.types.addresses.address_maps import AccountUpdateResponse, AccountDeleteResponse
```

Methods:

- <code title="put /accounts/{account_identifier1}/addressing/address_maps/{address_map_identifier}/accounts/{account_identifier}">client.addresses.address_maps.accounts.<a href="./src/cloudflare/resources/addresses/address_maps/accounts.py">update</a>(account_identifier, \*, account_identifier1, address_map_identifier) -> <a href="./src/cloudflare/types/addresses/address_maps/account_update_response.py">Optional</a></code>
- <code title="delete /accounts/{account_identifier1}/addressing/address_maps/{address_map_identifier}/accounts/{account_identifier}">client.addresses.address_maps.accounts.<a href="./src/cloudflare/resources/addresses/address_maps/accounts.py">delete</a>(account_identifier, \*, account_identifier1, address_map_identifier) -> <a href="./src/cloudflare/types/addresses/address_maps/account_delete_response.py">Optional</a></code>

### IPs

Types:

```python
from cloudflare.types.addresses.address_maps import IPUpdateResponse, IPDeleteResponse
```

Methods:

- <code title="put /accounts/{account_identifier}/addressing/address_maps/{address_map_identifier}/ips/{ip_address}">client.addresses.address_maps.ips.<a href="./src/cloudflare/resources/addresses/address_maps/ips.py">update</a>(ip_address, \*, account_identifier, address_map_identifier) -> <a href="./src/cloudflare/types/addresses/address_maps/ip_update_response.py">Optional</a></code>
- <code title="delete /accounts/{account_identifier}/addressing/address_maps/{address_map_identifier}/ips/{ip_address}">client.addresses.address_maps.ips.<a href="./src/cloudflare/resources/addresses/address_maps/ips.py">delete</a>(ip_address, \*, account_identifier, address_map_identifier) -> <a href="./src/cloudflare/types/addresses/address_maps/ip_delete_response.py">Optional</a></code>

### Zones

Types:

```python
from cloudflare.types.addresses.address_maps import ZoneUpdateResponse, ZoneDeleteResponse
```

Methods:

- <code title="put /accounts/{account_identifier}/addressing/address_maps/{address_map_identifier}/zones/{zone_identifier}">client.addresses.address_maps.zones.<a href="./src/cloudflare/resources/addresses/address_maps/zones.py">update</a>(zone_identifier, \*, account_identifier, address_map_identifier) -> <a href="./src/cloudflare/types/addresses/address_maps/zone_update_response.py">Optional</a></code>
- <code title="delete /accounts/{account_identifier}/addressing/address_maps/{address_map_identifier}/zones/{zone_identifier}">client.addresses.address_maps.zones.<a href="./src/cloudflare/resources/addresses/address_maps/zones.py">delete</a>(zone_identifier, \*, account_identifier, address_map_identifier) -> <a href="./src/cloudflare/types/addresses/address_maps/zone_delete_response.py">Optional</a></code>

## LoaDocuments

Types:

```python
from cloudflare.types.addresses import (
    LoaDocumentIPAddressManagementPrefixesUploadLoaDocumentResponse,
)
```

Methods:

- <code title="post /accounts/{account_identifier}/addressing/loa_documents">client.addresses.loa_documents.<a href="./src/cloudflare/resources/addresses/loa_documents/loa_documents.py">ip_address_management_prefixes_upload_loa_document</a>(account_identifier, \*\*<a href="src/cloudflare/types/addresses/loa_document_ip_address_management_prefixes_upload_loa_document_params.py">params</a>) -> <a href="./src/cloudflare/types/addresses/loa_document_ip_address_management_prefixes_upload_loa_document_response.py">LoaDocumentIPAddressManagementPrefixesUploadLoaDocumentResponse</a></code>

### Downloads

Types:

```python
from cloudflare.types.addresses.loa_documents import DownloadListResponse
```

Methods:

- <code title="get /accounts/{account_identifier}/addressing/loa_documents/{loa_document_identifier}/download">client.addresses.loa_documents.downloads.<a href="./src/cloudflare/resources/addresses/loa_documents/downloads.py">list</a>(loa_document_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/addresses/loa_documents/download_list_response.py">object</a></code>

## Prefixes

Types:

```python
from cloudflare.types.addresses import (
    PrefixUpdateResponse,
    PrefixDeleteResponse,
    PrefixGetResponse,
    PrefixIPAddressManagementPrefixesAddPrefixResponse,
    PrefixIPAddressManagementPrefixesListPrefixesResponse,
)
```

Methods:

- <code title="patch /accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}">client.addresses.prefixes.<a href="./src/cloudflare/resources/addresses/prefixes/prefixes.py">update</a>(prefix_identifier, \*, account_identifier, \*\*<a href="src/cloudflare/types/addresses/prefix_update_params.py">params</a>) -> <a href="./src/cloudflare/types/addresses/prefix_update_response.py">PrefixUpdateResponse</a></code>
- <code title="delete /accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}">client.addresses.prefixes.<a href="./src/cloudflare/resources/addresses/prefixes/prefixes.py">delete</a>(prefix_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/addresses/prefix_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}">client.addresses.prefixes.<a href="./src/cloudflare/resources/addresses/prefixes/prefixes.py">get</a>(prefix_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/addresses/prefix_get_response.py">PrefixGetResponse</a></code>
- <code title="post /accounts/{account_identifier}/addressing/prefixes">client.addresses.prefixes.<a href="./src/cloudflare/resources/addresses/prefixes/prefixes.py">ip_address_management_prefixes_add_prefix</a>(account_identifier, \*\*<a href="src/cloudflare/types/addresses/prefix_ip_address_management_prefixes_add_prefix_params.py">params</a>) -> <a href="./src/cloudflare/types/addresses/prefix_ip_address_management_prefixes_add_prefix_response.py">PrefixIPAddressManagementPrefixesAddPrefixResponse</a></code>
- <code title="get /accounts/{account_identifier}/addressing/prefixes">client.addresses.prefixes.<a href="./src/cloudflare/resources/addresses/prefixes/prefixes.py">ip_address_management_prefixes_list_prefixes</a>(account_identifier) -> <a href="./src/cloudflare/types/addresses/prefix_ip_address_management_prefixes_list_prefixes_response.py">Optional</a></code>

### BGPs

#### Statuses

Types:

```python
from cloudflare.types.addresses.prefixes.bgps import (
    StatusIPAddressManagementDynamicAdvertisementGetAdvertisementStatusResponse,
    StatusIPAddressManagementDynamicAdvertisementUpdatePrefixDynamicAdvertisementStatusResponse,
)
```

Methods:

- <code title="get /accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}/bgp/status">client.addresses.prefixes.bgps.statuses.<a href="./src/cloudflare/resources/addresses/prefixes/bgps/statuses.py">ip_address_management_dynamic_advertisement_get_advertisement_status</a>(prefix_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/addresses/prefixes/bgps/status_ip_address_management_dynamic_advertisement_get_advertisement_status_response.py">StatusIPAddressManagementDynamicAdvertisementGetAdvertisementStatusResponse</a></code>
- <code title="patch /accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}/bgp/status">client.addresses.prefixes.bgps.statuses.<a href="./src/cloudflare/resources/addresses/prefixes/bgps/statuses.py">ip_address_management_dynamic_advertisement_update_prefix_dynamic_advertisement_status</a>(prefix_identifier, \*, account_identifier, \*\*<a href="src/cloudflare/types/addresses/prefixes/bgps/status_ip_address_management_dynamic_advertisement_update_prefix_dynamic_advertisement_status_params.py">params</a>) -> <a href="./src/cloudflare/types/addresses/prefixes/bgps/status_ip_address_management_dynamic_advertisement_update_prefix_dynamic_advertisement_status_response.py">StatusIPAddressManagementDynamicAdvertisementUpdatePrefixDynamicAdvertisementStatusResponse</a></code>

### Delegations

Types:

```python
from cloudflare.types.addresses.prefixes import (
    DelegationDeleteResponse,
    DelegationIPAddressManagementPrefixDelegationCreatePrefixDelegationResponse,
    DelegationIPAddressManagementPrefixDelegationListPrefixDelegationsResponse,
)
```

Methods:

- <code title="delete /accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}/delegations/{delegation_identifier}">client.addresses.prefixes.delegations.<a href="./src/cloudflare/resources/addresses/prefixes/delegations.py">delete</a>(delegation_identifier, \*, account_identifier, prefix_identifier) -> <a href="./src/cloudflare/types/addresses/prefixes/delegation_delete_response.py">DelegationDeleteResponse</a></code>
- <code title="post /accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}/delegations">client.addresses.prefixes.delegations.<a href="./src/cloudflare/resources/addresses/prefixes/delegations.py">ip_address_management_prefix_delegation_create_prefix_delegation</a>(prefix_identifier, \*, account_identifier, \*\*<a href="src/cloudflare/types/addresses/prefixes/delegation_ip_address_management_prefix_delegation_create_prefix_delegation_params.py">params</a>) -> <a href="./src/cloudflare/types/addresses/prefixes/delegation_ip_address_management_prefix_delegation_create_prefix_delegation_response.py">DelegationIPAddressManagementPrefixDelegationCreatePrefixDelegationResponse</a></code>
- <code title="get /accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}/delegations">client.addresses.prefixes.delegations.<a href="./src/cloudflare/resources/addresses/prefixes/delegations.py">ip_address_management_prefix_delegation_list_prefix_delegations</a>(prefix_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/addresses/prefixes/delegation_ip_address_management_prefix_delegation_list_prefix_delegations_response.py">Optional</a></code>

# AuditLogs

Types:

```python
from cloudflare.types import AuditLogAuditLogsGetAccountAuditLogsResponse
```

Methods:

- <code title="get /accounts/{account_identifier}/audit_logs">client.audit_logs.<a href="./src/cloudflare/resources/audit_logs.py">audit_logs_get_account_audit_logs</a>(account_identifier, \*\*<a href="src/cloudflare/types/audit_log_audit_logs_get_account_audit_logs_params.py">params</a>) -> <a href="./src/cloudflare/types/audit_log_audit_logs_get_account_audit_logs_response.py">AuditLogAuditLogsGetAccountAuditLogsResponse</a></code>

# Billings

## Profiles

Types:

```python
from cloudflare.types.billings import ProfileAccountBillingProfileBillingProfileDetailsResponse
```

Methods:

- <code title="get /accounts/{account_identifier}/billing/profile">client.billings.profiles.<a href="./src/cloudflare/resources/billings/profiles.py">account_billing_profile_billing_profile_details</a>(account_identifier) -> <a href="./src/cloudflare/types/billings/profile_account_billing_profile_billing_profile_details_response.py">ProfileAccountBillingProfileBillingProfileDetailsResponse</a></code>

# BrandProtections

## Submits

Types:

```python
from cloudflare.types.brand_protections import (
    SubmitPhishingURLScannerSubmitSuspiciousURLForScanningResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/brand-protection/submit">client.brand_protections.submits.<a href="./src/cloudflare/resources/brand_protections/submits.py">phishing_url_scanner_submit_suspicious_url_for_scanning</a>(account_id, \*\*<a href="src/cloudflare/types/brand_protections/submit_phishing_url_scanner_submit_suspicious_url_for_scanning_params.py">params</a>) -> <a href="./src/cloudflare/types/brand_protections/submit_phishing_url_scanner_submit_suspicious_url_for_scanning_response.py">SubmitPhishingURLScannerSubmitSuspiciousURLForScanningResponse</a></code>

## URLInfos

Types:

```python
from cloudflare.types.brand_protections import (
    URLInfoPhishingURLInformationGetResultsForAURLScanResponse,
)
```

Methods:

- <code title="get /accounts/{account_id}/brand-protection/url-info">client.brand_protections.url_infos.<a href="./src/cloudflare/resources/brand_protections/url_infos.py">phishing_url_information_get_results_for_a_url_scan</a>(account_id, \*\*<a href="src/cloudflare/types/brand_protections/url_info_phishing_url_information_get_results_for_a_url_scan_params.py">params</a>) -> <a href="./src/cloudflare/types/brand_protections/url_info_phishing_url_information_get_results_for_a_url_scan_response.py">URLInfoPhishingURLInformationGetResultsForAURLScanResponse</a></code>

# CfdTunnels

Types:

```python
from cloudflare.types import (
    CfdTunnelUpdateResponse,
    CfdTunnelDeleteResponse,
    CfdTunnelCloudflareTunnelCreateACloudflareTunnelResponse,
    CfdTunnelCloudflareTunnelListCloudflareTunnelsResponse,
    CfdTunnelGetResponse,
)
```

Methods:

- <code title="patch /accounts/{account_id}/cfd_tunnel/{tunnel_id}">client.cfd_tunnels.<a href="./src/cloudflare/resources/cfd_tunnels/cfd_tunnels.py">update</a>(tunnel_id, \*, account_id, \*\*<a href="src/cloudflare/types/cfd_tunnel_update_params.py">params</a>) -> <a href="./src/cloudflare/types/cfd_tunnel_update_response.py">CfdTunnelUpdateResponse</a></code>
- <code title="delete /accounts/{account_id}/cfd_tunnel/{tunnel_id}">client.cfd_tunnels.<a href="./src/cloudflare/resources/cfd_tunnels/cfd_tunnels.py">delete</a>(tunnel_id, \*, account_id, \*\*<a href="src/cloudflare/types/cfd_tunnel_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/cfd_tunnel_delete_response.py">CfdTunnelDeleteResponse</a></code>
- <code title="post /accounts/{account_id}/cfd_tunnel">client.cfd_tunnels.<a href="./src/cloudflare/resources/cfd_tunnels/cfd_tunnels.py">cloudflare_tunnel_create_a_cloudflare_tunnel</a>(account_id, \*\*<a href="src/cloudflare/types/cfd_tunnel_cloudflare_tunnel_create_a_cloudflare_tunnel_params.py">params</a>) -> <a href="./src/cloudflare/types/cfd_tunnel_cloudflare_tunnel_create_a_cloudflare_tunnel_response.py">CfdTunnelCloudflareTunnelCreateACloudflareTunnelResponse</a></code>
- <code title="get /accounts/{account_id}/cfd_tunnel">client.cfd_tunnels.<a href="./src/cloudflare/resources/cfd_tunnels/cfd_tunnels.py">cloudflare_tunnel_list_cloudflare_tunnels</a>(account_id, \*\*<a href="src/cloudflare/types/cfd_tunnel_cloudflare_tunnel_list_cloudflare_tunnels_params.py">params</a>) -> <a href="./src/cloudflare/types/cfd_tunnel_cloudflare_tunnel_list_cloudflare_tunnels_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/cfd_tunnel/{tunnel_id}">client.cfd_tunnels.<a href="./src/cloudflare/resources/cfd_tunnels/cfd_tunnels.py">get</a>(tunnel_id, \*, account_id) -> <a href="./src/cloudflare/types/cfd_tunnel_get_response.py">CfdTunnelGetResponse</a></code>

## Configurations

Types:

```python
from cloudflare.types.cfd_tunnels import (
    ConfigurationCloudflareTunnelConfigurationGetConfigurationResponse,
    ConfigurationCloudflareTunnelConfigurationPutConfigurationResponse,
)
```

Methods:

- <code title="get /accounts/{account_id}/cfd_tunnel/{tunnel_id}/configurations">client.cfd_tunnels.configurations.<a href="./src/cloudflare/resources/cfd_tunnels/configurations.py">cloudflare_tunnel_configuration_get_configuration</a>(tunnel_id, \*, account_id) -> <a href="./src/cloudflare/types/cfd_tunnels/configuration_cloudflare_tunnel_configuration_get_configuration_response.py">ConfigurationCloudflareTunnelConfigurationGetConfigurationResponse</a></code>
- <code title="put /accounts/{account_id}/cfd_tunnel/{tunnel_id}/configurations">client.cfd_tunnels.configurations.<a href="./src/cloudflare/resources/cfd_tunnels/configurations.py">cloudflare_tunnel_configuration_put_configuration</a>(tunnel_id, \*, account_id, \*\*<a href="src/cloudflare/types/cfd_tunnels/configuration_cloudflare_tunnel_configuration_put_configuration_params.py">params</a>) -> <a href="./src/cloudflare/types/cfd_tunnels/configuration_cloudflare_tunnel_configuration_put_configuration_response.py">ConfigurationCloudflareTunnelConfigurationPutConfigurationResponse</a></code>

## Connections

Types:

```python
from cloudflare.types.cfd_tunnels import (
    ConnectionDeleteResponse,
    ConnectionCloudflareTunnelListCloudflareTunnelConnectionsResponse,
)
```

Methods:

- <code title="delete /accounts/{account_id}/cfd_tunnel/{tunnel_id}/connections">client.cfd_tunnels.connections.<a href="./src/cloudflare/resources/cfd_tunnels/connections.py">delete</a>(tunnel_id, \*, account_id, \*\*<a href="src/cloudflare/types/cfd_tunnels/connection_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/cfd_tunnels/connection_delete_response.py">ConnectionDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/cfd_tunnel/{tunnel_id}/connections">client.cfd_tunnels.connections.<a href="./src/cloudflare/resources/cfd_tunnels/connections.py">cloudflare_tunnel_list_cloudflare_tunnel_connections</a>(tunnel_id, \*, account_id) -> <a href="./src/cloudflare/types/cfd_tunnels/connection_cloudflare_tunnel_list_cloudflare_tunnel_connections_response.py">Optional</a></code>

## Tokens

Types:

```python
from cloudflare.types.cfd_tunnels import TokenCloudflareTunnelGetACloudflareTunnelTokenResponse
```

Methods:

- <code title="get /accounts/{account_id}/cfd_tunnel/{tunnel_id}/token">client.cfd_tunnels.tokens.<a href="./src/cloudflare/resources/cfd_tunnels/tokens.py">cloudflare_tunnel_get_a_cloudflare_tunnel_token</a>(tunnel_id, \*, account_id) -> <a href="./src/cloudflare/types/cfd_tunnels/token_cloudflare_tunnel_get_a_cloudflare_tunnel_token_response.py">TokenCloudflareTunnelGetACloudflareTunnelTokenResponse</a></code>

## Connectors

Types:

```python
from cloudflare.types.cfd_tunnels import ConnectorGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/cfd_tunnel/{tunnel_id}/connectors/{connector_id}">client.cfd_tunnels.connectors.<a href="./src/cloudflare/resources/cfd_tunnels/connectors.py">get</a>(connector_id, \*, account_id, tunnel_id) -> <a href="./src/cloudflare/types/cfd_tunnels/connector_get_response.py">ConnectorGetResponse</a></code>

## Management

Types:

```python
from cloudflare.types.cfd_tunnels import ManagementCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/cfd_tunnel/{tunnel_id}/management">client.cfd_tunnels.management.<a href="./src/cloudflare/resources/cfd_tunnels/management.py">create</a>(tunnel_id, \*, account_id, \*\*<a href="src/cloudflare/types/cfd_tunnels/management_create_params.py">params</a>) -> <a href="./src/cloudflare/types/cfd_tunnels/management_create_response.py">ManagementCreateResponse</a></code>

# Diagnostics

## Traceroutes

Types:

```python
from cloudflare.types.diagnostics import TracerouteDiagnosticsTracerouteResponse
```

Methods:

- <code title="post /accounts/{account_identifier}/diagnostics/traceroute">client.diagnostics.traceroutes.<a href="./src/cloudflare/resources/diagnostics/traceroutes.py">diagnostics_traceroute</a>(account_identifier, \*\*<a href="src/cloudflare/types/diagnostics/traceroute_diagnostics_traceroute_params.py">params</a>) -> <a href="./src/cloudflare/types/diagnostics/traceroute_diagnostics_traceroute_response.py">Optional</a></code>

# DLPs

## Patterns

### Validates

Types:

```python
from cloudflare.types.dlps.patterns import ValidateDLPPatternValidationValidatePatternResponse
```

Methods:

- <code title="post /accounts/{account_id}/dlp/patterns/validate">client.dlps.patterns.validates.<a href="./src/cloudflare/resources/dlps/patterns/validates.py">dlp_pattern_validation_validate_pattern</a>(account_id, \*\*<a href="src/cloudflare/types/dlps/patterns/validate_dlp_pattern_validation_validate_pattern_params.py">params</a>) -> <a href="./src/cloudflare/types/dlps/patterns/validate_dlp_pattern_validation_validate_pattern_response.py">ValidateDLPPatternValidationValidatePatternResponse</a></code>

## PayloadLogs

Types:

```python
from cloudflare.types.dlps import (
    PayloadLogDLPPayloadLogSettingsGetSettingsResponse,
    PayloadLogDLPPayloadLogSettingsUpdateSettingsResponse,
)
```

Methods:

- <code title="get /accounts/{account_id}/dlp/payload_log">client.dlps.payload_logs.<a href="./src/cloudflare/resources/dlps/payload_logs.py">dlp_payload_log_settings_get_settings</a>(account_id) -> <a href="./src/cloudflare/types/dlps/payload_log_dlp_payload_log_settings_get_settings_response.py">PayloadLogDLPPayloadLogSettingsGetSettingsResponse</a></code>
- <code title="put /accounts/{account_id}/dlp/payload_log">client.dlps.payload_logs.<a href="./src/cloudflare/resources/dlps/payload_logs.py">dlp_payload_log_settings_update_settings</a>(account_id, \*\*<a href="src/cloudflare/types/dlps/payload_log_dlp_payload_log_settings_update_settings_params.py">params</a>) -> <a href="./src/cloudflare/types/dlps/payload_log_dlp_payload_log_settings_update_settings_response.py">PayloadLogDLPPayloadLogSettingsUpdateSettingsResponse</a></code>

## Profiles

Types:

```python
from cloudflare.types.dlps import ProfileDLPProfilesListAllProfilesResponse, ProfileGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/dlp/profiles">client.dlps.profiles.<a href="./src/cloudflare/resources/dlps/profiles/profiles.py">dlp_profiles_list_all_profiles</a>(account_id) -> <a href="./src/cloudflare/types/dlps/profile_dlp_profiles_list_all_profiles_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/dlp/profiles/{profile_id}">client.dlps.profiles.<a href="./src/cloudflare/resources/dlps/profiles/profiles.py">get</a>(profile_id, \*, account_id) -> <a href="./src/cloudflare/types/dlps/profile_get_response.py">ProfileGetResponse</a></code>

### Customs

Types:

```python
from cloudflare.types.dlps.profiles import (
    CustomUpdateResponse,
    CustomDeleteResponse,
    CustomDLPProfilesCreateCustomProfilesResponse,
    CustomGetResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/dlp/profiles/custom/{profile_id}">client.dlps.profiles.customs.<a href="./src/cloudflare/resources/dlps/profiles/customs.py">update</a>(profile_id, \*, account_id, \*\*<a href="src/cloudflare/types/dlps/profiles/custom_update_params.py">params</a>) -> <a href="./src/cloudflare/types/dlps/profiles/custom_update_response.py">CustomUpdateResponse</a></code>
- <code title="delete /accounts/{account_id}/dlp/profiles/custom/{profile_id}">client.dlps.profiles.customs.<a href="./src/cloudflare/resources/dlps/profiles/customs.py">delete</a>(profile_id, \*, account_id) -> <a href="./src/cloudflare/types/dlps/profiles/custom_delete_response.py">CustomDeleteResponse</a></code>
- <code title="post /accounts/{account_id}/dlp/profiles/custom">client.dlps.profiles.customs.<a href="./src/cloudflare/resources/dlps/profiles/customs.py">dlp_profiles_create_custom_profiles</a>(account_id, \*\*<a href="src/cloudflare/types/dlps/profiles/custom_dlp_profiles_create_custom_profiles_params.py">params</a>) -> <a href="./src/cloudflare/types/dlps/profiles/custom_dlp_profiles_create_custom_profiles_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/dlp/profiles/custom/{profile_id}">client.dlps.profiles.customs.<a href="./src/cloudflare/resources/dlps/profiles/customs.py">get</a>(profile_id, \*, account_id) -> <a href="./src/cloudflare/types/dlps/profiles/custom_get_response.py">CustomGetResponse</a></code>

### Predefineds

Types:

```python
from cloudflare.types.dlps.profiles import PredefinedUpdateResponse, PredefinedGetResponse
```

Methods:

- <code title="put /accounts/{account_id}/dlp/profiles/predefined/{profile_id}">client.dlps.profiles.predefineds.<a href="./src/cloudflare/resources/dlps/profiles/predefineds.py">update</a>(profile_id, \*, account_id, \*\*<a href="src/cloudflare/types/dlps/profiles/predefined_update_params.py">params</a>) -> <a href="./src/cloudflare/types/dlps/profiles/predefined_update_response.py">PredefinedUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/dlp/profiles/predefined/{profile_id}">client.dlps.profiles.predefineds.<a href="./src/cloudflare/resources/dlps/profiles/predefineds.py">get</a>(profile_id, \*, account_id) -> <a href="./src/cloudflare/types/dlps/profiles/predefined_get_response.py">PredefinedGetResponse</a></code>

# DNSFirewalls

Types:

```python
from cloudflare.types import (
    DNSFirewallCreateResponse,
    DNSFirewallUpdateResponse,
    DNSFirewallListResponse,
    DNSFirewallDeleteResponse,
    DNSFirewallGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/dns_firewall">client.dns_firewalls.<a href="./src/cloudflare/resources/dns_firewalls/dns_firewalls.py">create</a>(account_id, \*\*<a href="src/cloudflare/types/dns_firewall_create_params.py">params</a>) -> <a href="./src/cloudflare/types/dns_firewall_create_response.py">DNSFirewallCreateResponse</a></code>
- <code title="patch /accounts/{account_id}/dns_firewall/{dns_firewall_id}">client.dns_firewalls.<a href="./src/cloudflare/resources/dns_firewalls/dns_firewalls.py">update</a>(dns_firewall_id, \*, account_id, \*\*<a href="src/cloudflare/types/dns_firewall_update_params.py">params</a>) -> <a href="./src/cloudflare/types/dns_firewall_update_response.py">DNSFirewallUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/dns_firewall">client.dns_firewalls.<a href="./src/cloudflare/resources/dns_firewalls/dns_firewalls.py">list</a>(account_id, \*\*<a href="src/cloudflare/types/dns_firewall_list_params.py">params</a>) -> <a href="./src/cloudflare/types/dns_firewall_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/dns_firewall/{dns_firewall_id}">client.dns_firewalls.<a href="./src/cloudflare/resources/dns_firewalls/dns_firewalls.py">delete</a>(dns_firewall_id, \*, account_id) -> <a href="./src/cloudflare/types/dns_firewall_delete_response.py">DNSFirewallDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/dns_firewall/{dns_firewall_id}">client.dns_firewalls.<a href="./src/cloudflare/resources/dns_firewalls/dns_firewalls.py">get</a>(dns_firewall_id, \*, account_id) -> <a href="./src/cloudflare/types/dns_firewall_get_response.py">DNSFirewallGetResponse</a></code>

## DNSAnalytics

### Reports

Types:

```python
from cloudflare.types.dns_firewalls.dns_analytics import ReportListResponse
```

Methods:

- <code title="get /accounts/{account_identifier}/dns_firewall/{identifier}/dns_analytics/report">client.dns_firewalls.dns_analytics.reports.<a href="./src/cloudflare/resources/dns_firewalls/dns_analytics/reports/reports.py">list</a>(identifier, \*, account_identifier, \*\*<a href="src/cloudflare/types/dns_firewalls/dns_analytics/report_list_params.py">params</a>) -> <a href="./src/cloudflare/types/dns_firewalls/dns_analytics/report_list_response.py">ReportListResponse</a></code>

#### Bytimes

Types:

```python
from cloudflare.types.dns_firewalls.dns_analytics.reports import BytimeListResponse
```

Methods:

- <code title="get /accounts/{account_identifier}/dns_firewall/{identifier}/dns_analytics/report/bytime">client.dns_firewalls.dns_analytics.reports.bytimes.<a href="./src/cloudflare/resources/dns_firewalls/dns_analytics/reports/bytimes.py">list</a>(identifier, \*, account_identifier, \*\*<a href="src/cloudflare/types/dns_firewalls/dns_analytics/reports/bytime_list_params.py">params</a>) -> <a href="./src/cloudflare/types/dns_firewalls/dns_analytics/reports/bytime_list_response.py">BytimeListResponse</a></code>

# Images

## V1s

Types:

```python
from cloudflare.types.images import (
    V1UpdateResponse,
    V1DeleteResponse,
    V1CloudflareImagesListImagesResponse,
    V1CloudflareImagesUploadAnImageViaURLResponse,
    V1GetResponse,
)
```

Methods:

- <code title="patch /accounts/{account_id}/images/v1/{image_id}">client.images.v1s.<a href="./src/cloudflare/resources/images/v1s/v1s.py">update</a>(image_id, \*, account_id, \*\*<a href="src/cloudflare/types/images/v1_update_params.py">params</a>) -> <a href="./src/cloudflare/types/images/v1_update_response.py">V1UpdateResponse</a></code>
- <code title="delete /accounts/{account_id}/images/v1/{image_id}">client.images.v1s.<a href="./src/cloudflare/resources/images/v1s/v1s.py">delete</a>(image_id, \*, account_id) -> <a href="./src/cloudflare/types/images/v1_delete_response.py">V1DeleteResponse</a></code>
- <code title="get /accounts/{account_id}/images/v1">client.images.v1s.<a href="./src/cloudflare/resources/images/v1s/v1s.py">cloudflare_images_list_images</a>(account_id, \*\*<a href="src/cloudflare/types/images/v1_cloudflare_images_list_images_params.py">params</a>) -> <a href="./src/cloudflare/types/images/v1_cloudflare_images_list_images_response.py">V1CloudflareImagesListImagesResponse</a></code>
- <code title="post /accounts/{account_id}/images/v1">client.images.v1s.<a href="./src/cloudflare/resources/images/v1s/v1s.py">cloudflare_images_upload_an_image_via_url</a>(account_id, \*\*<a href="src/cloudflare/types/images/v1_cloudflare_images_upload_an_image_via_url_params.py">params</a>) -> <a href="./src/cloudflare/types/images/v1_cloudflare_images_upload_an_image_via_url_response.py">V1CloudflareImagesUploadAnImageViaURLResponse</a></code>
- <code title="get /accounts/{account_id}/images/v1/{image_id}">client.images.v1s.<a href="./src/cloudflare/resources/images/v1s/v1s.py">get</a>(image_id, \*, account_id) -> <a href="./src/cloudflare/types/images/v1_get_response.py">V1GetResponse</a></code>

### Keys

Types:

```python
from cloudflare.types.images.v1s import KeyCloudflareImagesKeysListSigningKeysResponse
```

Methods:

- <code title="get /accounts/{account_id}/images/v1/keys">client.images.v1s.keys.<a href="./src/cloudflare/resources/images/v1s/keys.py">cloudflare_images_keys_list_signing_keys</a>(account_id) -> <a href="./src/cloudflare/types/images/v1s/key_cloudflare_images_keys_list_signing_keys_response.py">KeyCloudflareImagesKeysListSigningKeysResponse</a></code>

### Stats

Types:

```python
from cloudflare.types.images.v1s import StatCloudflareImagesImagesUsageStatisticsResponse
```

Methods:

- <code title="get /accounts/{account_id}/images/v1/stats">client.images.v1s.stats.<a href="./src/cloudflare/resources/images/v1s/stats.py">cloudflare_images_images_usage_statistics</a>(account_id) -> <a href="./src/cloudflare/types/images/v1s/stat_cloudflare_images_images_usage_statistics_response.py">StatCloudflareImagesImagesUsageStatisticsResponse</a></code>

### Variants

Types:

```python
from cloudflare.types.images.v1s import (
    VariantUpdateResponse,
    VariantDeleteResponse,
    VariantCloudflareImagesVariantsCreateAVariantResponse,
    VariantCloudflareImagesVariantsListVariantsResponse,
    VariantGetResponse,
)
```

Methods:

- <code title="patch /accounts/{account_id}/images/v1/variants/{variant_id}">client.images.v1s.variants.<a href="./src/cloudflare/resources/images/v1s/variants.py">update</a>(variant_id, \*, account_id, \*\*<a href="src/cloudflare/types/images/v1s/variant_update_params.py">params</a>) -> <a href="./src/cloudflare/types/images/v1s/variant_update_response.py">VariantUpdateResponse</a></code>
- <code title="delete /accounts/{account_id}/images/v1/variants/{variant_id}">client.images.v1s.variants.<a href="./src/cloudflare/resources/images/v1s/variants.py">delete</a>(variant_id, \*, account_id) -> <a href="./src/cloudflare/types/images/v1s/variant_delete_response.py">VariantDeleteResponse</a></code>
- <code title="post /accounts/{account_id}/images/v1/variants">client.images.v1s.variants.<a href="./src/cloudflare/resources/images/v1s/variants.py">cloudflare_images_variants_create_a_variant</a>(account_id, \*\*<a href="src/cloudflare/types/images/v1s/variant_cloudflare_images_variants_create_a_variant_params.py">params</a>) -> <a href="./src/cloudflare/types/images/v1s/variant_cloudflare_images_variants_create_a_variant_response.py">VariantCloudflareImagesVariantsCreateAVariantResponse</a></code>
- <code title="get /accounts/{account_id}/images/v1/variants">client.images.v1s.variants.<a href="./src/cloudflare/resources/images/v1s/variants.py">cloudflare_images_variants_list_variants</a>(account_id) -> <a href="./src/cloudflare/types/images/v1s/variant_cloudflare_images_variants_list_variants_response.py">VariantCloudflareImagesVariantsListVariantsResponse</a></code>
- <code title="get /accounts/{account_id}/images/v1/variants/{variant_id}">client.images.v1s.variants.<a href="./src/cloudflare/resources/images/v1s/variants.py">get</a>(variant_id, \*, account_id) -> <a href="./src/cloudflare/types/images/v1s/variant_get_response.py">VariantGetResponse</a></code>

### Blobs

Methods:

- <code title="get /accounts/{account_id}/images/v1/{image_id}/blob">client.images.v1s.blobs.<a href="./src/cloudflare/resources/images/v1s/blobs.py">cloudflare_images_base_image</a>(image_id, \*, account_id) -> BinaryAPIResponse</code>

## V2s

Types:

```python
from cloudflare.types.images import ImagesImagesListResponseV2, V2ListResponse
```

Methods:

- <code title="get /accounts/{account_id}/images/v2">client.images.v2s.<a href="./src/cloudflare/resources/images/v2s/v2s.py">list</a>(account_id, \*\*<a href="src/cloudflare/types/images/v2_list_params.py">params</a>) -> <a href="./src/cloudflare/types/images/v2_list_response.py">V2ListResponse</a></code>

### DirectUploads

Types:

```python
from cloudflare.types.images.v2s import (
    DirectUploadCloudflareImagesCreateAuthenticatedDirectUploadURLV2Response,
)
```

Methods:

- <code title="post /accounts/{account_id}/images/v2/direct_upload">client.images.v2s.direct_uploads.<a href="./src/cloudflare/resources/images/v2s/direct_uploads.py">cloudflare_images_create_authenticated_direct_upload_url_v_2</a>(account_id, \*\*<a href="src/cloudflare/types/images/v2s/direct_upload_cloudflare_images_create_authenticated_direct_upload_url_v_2_params.py">params</a>) -> <a href="./src/cloudflare/types/images/v2s/direct_upload_cloudflare_images_create_authenticated_direct_upload_url_v_2_response.py">DirectUploadCloudflareImagesCreateAuthenticatedDirectUploadURLV2Response</a></code>

# Intels

## Asn

Types:

```python
from cloudflare.types.intels import AsnGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/intel/asn/{asn}">client.intels.asn.<a href="./src/cloudflare/resources/intels/asn/asn.py">get</a>(asn, \*, account_id) -> <a href="./src/cloudflare/types/intels/asn_get_response.py">AsnGetResponse</a></code>

### Subnets

Types:

```python
from cloudflare.types.intels.asn import SubnetListResponse
```

Methods:

- <code title="get /accounts/{account_id}/intel/asn/{asn}/subnets">client.intels.asn.subnets.<a href="./src/cloudflare/resources/intels/asn/subnets.py">list</a>(asn, \*, account_id) -> <a href="./src/cloudflare/types/intels/asn/subnet_list_response.py">SubnetListResponse</a></code>

## DNS

Types:

```python
from cloudflare.types.intels import DNSPassiveDNSByIPGetPassiveDNSByIPResponse
```

Methods:

- <code title="get /accounts/{account_id}/intel/dns">client.intels.dns.<a href="./src/cloudflare/resources/intels/dns.py">passive_dns_by_ip_get_passive_dns_by_ip</a>(account_id, \*\*<a href="src/cloudflare/types/intels/dns_passive_dns_by_ip_get_passive_dns_by_ip_params.py">params</a>) -> <a href="./src/cloudflare/types/intels/dns_passive_dns_by_ip_get_passive_dns_by_ip_response.py">DNSPassiveDNSByIPGetPassiveDNSByIPResponse</a></code>

## Domains

Types:

```python
from cloudflare.types.intels import DomainDomainIntelligenceGetDomainDetailsResponse
```

Methods:

- <code title="get /accounts/{account_id}/intel/domain">client.intels.domains.<a href="./src/cloudflare/resources/intels/domains/domains.py">domain_intelligence_get_domain_details</a>(account_id, \*\*<a href="src/cloudflare/types/intels/domain_domain_intelligence_get_domain_details_params.py">params</a>) -> <a href="./src/cloudflare/types/intels/domain_domain_intelligence_get_domain_details_response.py">DomainDomainIntelligenceGetDomainDetailsResponse</a></code>

### Bulks

Types:

```python
from cloudflare.types.intels.domains import BulkDomainIntelligenceGetMultipleDomainDetailsResponse
```

Methods:

- <code title="get /accounts/{account_id}/intel/domain/bulk">client.intels.domains.bulks.<a href="./src/cloudflare/resources/intels/domains/bulks.py">domain_intelligence_get_multiple_domain_details</a>(account_id, \*\*<a href="src/cloudflare/types/intels/domains/bulk_domain_intelligence_get_multiple_domain_details_params.py">params</a>) -> <a href="./src/cloudflare/types/intels/domains/bulk_domain_intelligence_get_multiple_domain_details_response.py">Optional</a></code>

## DomainHistories

Types:

```python
from cloudflare.types.intels import DomainHistoryListResponse
```

Methods:

- <code title="get /accounts/{account_id}/intel/domain-history">client.intels.domain_histories.<a href="./src/cloudflare/resources/intels/domain_histories.py">list</a>(account_id, \*\*<a href="src/cloudflare/types/intels/domain_history_list_params.py">params</a>) -> <a href="./src/cloudflare/types/intels/domain_history_list_response.py">Optional</a></code>

## IPs

Types:

```python
from cloudflare.types.intels import IPIPIntelligenceGetIPOverviewResponse
```

Methods:

- <code title="get /accounts/{account_id}/intel/ip">client.intels.ips.<a href="./src/cloudflare/resources/intels/ips.py">ip_intelligence_get_ip_overview</a>(account_id, \*\*<a href="src/cloudflare/types/intels/ip_ip_intelligence_get_ip_overview_params.py">params</a>) -> <a href="./src/cloudflare/types/intels/ip_ip_intelligence_get_ip_overview_response.py">Optional</a></code>

## IPLists

Types:

```python
from cloudflare.types.intels import IPListIPListGetIPListsResponse
```

Methods:

- <code title="get /accounts/{account_id}/intel/ip-list">client.intels.ip_lists.<a href="./src/cloudflare/resources/intels/ip_lists.py">ip_list_get_ip_lists</a>(account_id) -> <a href="./src/cloudflare/types/intels/ip_list_ip_list_get_ip_lists_response.py">Optional</a></code>

## Miscategorizations

Types:

```python
from cloudflare.types.intels import (
    MiscategorizationMiscategorizationCreateMiscategorizationResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/intel/miscategorization">client.intels.miscategorizations.<a href="./src/cloudflare/resources/intels/miscategorizations.py">miscategorization_create_miscategorization</a>(account_id, \*\*<a href="src/cloudflare/types/intels/miscategorization_miscategorization_create_miscategorization_params.py">params</a>) -> <a href="./src/cloudflare/types/intels/miscategorization_miscategorization_create_miscategorization_response.py">MiscategorizationMiscategorizationCreateMiscategorizationResponse</a></code>

## Whois

Types:

```python
from cloudflare.types.intels import WhoisWhoisRecordGetWhoisRecordResponse
```

Methods:

- <code title="get /accounts/{account_id}/intel/whois">client.intels.whois.<a href="./src/cloudflare/resources/intels/whois.py">whois_record_get_whois_record</a>(account_id, \*\*<a href="src/cloudflare/types/intels/whois_whois_record_get_whois_record_params.py">params</a>) -> <a href="./src/cloudflare/types/intels/whois_whois_record_get_whois_record_response.py">WhoisWhoisRecordGetWhoisRecordResponse</a></code>

# Magics

## CfInterconnects

Types:

```python
from cloudflare.types.magics import (
    CfInterconnectUpdateResponse,
    CfInterconnectGetResponse,
    CfInterconnectMagicInterconnectsListInterconnectsResponse,
    CfInterconnectMagicInterconnectsUpdateMultipleInterconnectsResponse,
)
```

Methods:

- <code title="put /accounts/{account_identifier}/magic/cf_interconnects/{tunnel_identifier}">client.magics.cf_interconnects.<a href="./src/cloudflare/resources/magics/cf_interconnects.py">update</a>(tunnel_identifier, \*, account_identifier, \*\*<a href="src/cloudflare/types/magics/cf_interconnect_update_params.py">params</a>) -> <a href="./src/cloudflare/types/magics/cf_interconnect_update_response.py">CfInterconnectUpdateResponse</a></code>
- <code title="get /accounts/{account_identifier}/magic/cf_interconnects/{tunnel_identifier}">client.magics.cf_interconnects.<a href="./src/cloudflare/resources/magics/cf_interconnects.py">get</a>(tunnel_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/magics/cf_interconnect_get_response.py">CfInterconnectGetResponse</a></code>
- <code title="get /accounts/{account_identifier}/magic/cf_interconnects">client.magics.cf_interconnects.<a href="./src/cloudflare/resources/magics/cf_interconnects.py">magic_interconnects_list_interconnects</a>(account_identifier) -> <a href="./src/cloudflare/types/magics/cf_interconnect_magic_interconnects_list_interconnects_response.py">CfInterconnectMagicInterconnectsListInterconnectsResponse</a></code>
- <code title="put /accounts/{account_identifier}/magic/cf_interconnects">client.magics.cf_interconnects.<a href="./src/cloudflare/resources/magics/cf_interconnects.py">magic_interconnects_update_multiple_interconnects</a>(account_identifier, \*\*<a href="src/cloudflare/types/magics/cf_interconnect_magic_interconnects_update_multiple_interconnects_params.py">params</a>) -> <a href="./src/cloudflare/types/magics/cf_interconnect_magic_interconnects_update_multiple_interconnects_response.py">CfInterconnectMagicInterconnectsUpdateMultipleInterconnectsResponse</a></code>

## GreTunnels

Types:

```python
from cloudflare.types.magics import (
    GreTunnelUpdateResponse,
    GreTunnelDeleteResponse,
    GreTunnelGetResponse,
    GreTunnelMagicGreTunnelsCreateGreTunnelsResponse,
    GreTunnelMagicGreTunnelsListGreTunnelsResponse,
    GreTunnelMagicGreTunnelsUpdateMultipleGreTunnelsResponse,
)
```

Methods:

- <code title="put /accounts/{account_identifier}/magic/gre_tunnels/{tunnel_identifier}">client.magics.gre_tunnels.<a href="./src/cloudflare/resources/magics/gre_tunnels.py">update</a>(tunnel_identifier, \*, account_identifier, \*\*<a href="src/cloudflare/types/magics/gre_tunnel_update_params.py">params</a>) -> <a href="./src/cloudflare/types/magics/gre_tunnel_update_response.py">GreTunnelUpdateResponse</a></code>
- <code title="delete /accounts/{account_identifier}/magic/gre_tunnels/{tunnel_identifier}">client.magics.gre_tunnels.<a href="./src/cloudflare/resources/magics/gre_tunnels.py">delete</a>(tunnel_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/magics/gre_tunnel_delete_response.py">GreTunnelDeleteResponse</a></code>
- <code title="get /accounts/{account_identifier}/magic/gre_tunnels/{tunnel_identifier}">client.magics.gre_tunnels.<a href="./src/cloudflare/resources/magics/gre_tunnels.py">get</a>(tunnel_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/magics/gre_tunnel_get_response.py">GreTunnelGetResponse</a></code>
- <code title="post /accounts/{account_identifier}/magic/gre_tunnels">client.magics.gre_tunnels.<a href="./src/cloudflare/resources/magics/gre_tunnels.py">magic_gre_tunnels_create_gre_tunnels</a>(account_identifier, \*\*<a href="src/cloudflare/types/magics/gre_tunnel_magic_gre_tunnels_create_gre_tunnels_params.py">params</a>) -> <a href="./src/cloudflare/types/magics/gre_tunnel_magic_gre_tunnels_create_gre_tunnels_response.py">GreTunnelMagicGreTunnelsCreateGreTunnelsResponse</a></code>
- <code title="get /accounts/{account_identifier}/magic/gre_tunnels">client.magics.gre_tunnels.<a href="./src/cloudflare/resources/magics/gre_tunnels.py">magic_gre_tunnels_list_gre_tunnels</a>(account_identifier) -> <a href="./src/cloudflare/types/magics/gre_tunnel_magic_gre_tunnels_list_gre_tunnels_response.py">GreTunnelMagicGreTunnelsListGreTunnelsResponse</a></code>
- <code title="put /accounts/{account_identifier}/magic/gre_tunnels">client.magics.gre_tunnels.<a href="./src/cloudflare/resources/magics/gre_tunnels.py">magic_gre_tunnels_update_multiple_gre_tunnels</a>(account_identifier, \*\*<a href="src/cloudflare/types/magics/gre_tunnel_magic_gre_tunnels_update_multiple_gre_tunnels_params.py">params</a>) -> <a href="./src/cloudflare/types/magics/gre_tunnel_magic_gre_tunnels_update_multiple_gre_tunnels_response.py">GreTunnelMagicGreTunnelsUpdateMultipleGreTunnelsResponse</a></code>

## IpsecTunnels

Types:

```python
from cloudflare.types.magics import (
    IpsecTunnelUpdateResponse,
    IpsecTunnelDeleteResponse,
    IpsecTunnelGetResponse,
    IpsecTunnelMagicIPsecTunnelsCreateIPsecTunnelsResponse,
    IpsecTunnelMagicIPsecTunnelsListIPsecTunnelsResponse,
    IpsecTunnelMagicIPsecTunnelsUpdateMultipleIPsecTunnelsResponse,
)
```

Methods:

- <code title="put /accounts/{account_identifier}/magic/ipsec_tunnels/{tunnel_identifier}">client.magics.ipsec_tunnels.<a href="./src/cloudflare/resources/magics/ipsec_tunnels/ipsec_tunnels.py">update</a>(tunnel_identifier, \*, account_identifier, \*\*<a href="src/cloudflare/types/magics/ipsec_tunnel_update_params.py">params</a>) -> <a href="./src/cloudflare/types/magics/ipsec_tunnel_update_response.py">IpsecTunnelUpdateResponse</a></code>
- <code title="delete /accounts/{account_identifier}/magic/ipsec_tunnels/{tunnel_identifier}">client.magics.ipsec_tunnels.<a href="./src/cloudflare/resources/magics/ipsec_tunnels/ipsec_tunnels.py">delete</a>(tunnel_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/magics/ipsec_tunnel_delete_response.py">IpsecTunnelDeleteResponse</a></code>
- <code title="get /accounts/{account_identifier}/magic/ipsec_tunnels/{tunnel_identifier}">client.magics.ipsec_tunnels.<a href="./src/cloudflare/resources/magics/ipsec_tunnels/ipsec_tunnels.py">get</a>(tunnel_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/magics/ipsec_tunnel_get_response.py">IpsecTunnelGetResponse</a></code>
- <code title="post /accounts/{account_identifier}/magic/ipsec_tunnels">client.magics.ipsec_tunnels.<a href="./src/cloudflare/resources/magics/ipsec_tunnels/ipsec_tunnels.py">magic_i_psec_tunnels_create_i_psec_tunnels</a>(account_identifier, \*\*<a href="src/cloudflare/types/magics/ipsec_tunnel_magic_i_psec_tunnels_create_i_psec_tunnels_params.py">params</a>) -> <a href="./src/cloudflare/types/magics/ipsec_tunnel_magic_i_psec_tunnels_create_i_psec_tunnels_response.py">IpsecTunnelMagicIPsecTunnelsCreateIPsecTunnelsResponse</a></code>
- <code title="get /accounts/{account_identifier}/magic/ipsec_tunnels">client.magics.ipsec_tunnels.<a href="./src/cloudflare/resources/magics/ipsec_tunnels/ipsec_tunnels.py">magic_i_psec_tunnels_list_i_psec_tunnels</a>(account_identifier) -> <a href="./src/cloudflare/types/magics/ipsec_tunnel_magic_i_psec_tunnels_list_i_psec_tunnels_response.py">IpsecTunnelMagicIPsecTunnelsListIPsecTunnelsResponse</a></code>
- <code title="put /accounts/{account_identifier}/magic/ipsec_tunnels">client.magics.ipsec_tunnels.<a href="./src/cloudflare/resources/magics/ipsec_tunnels/ipsec_tunnels.py">magic_i_psec_tunnels_update_multiple_i_psec_tunnels</a>(account_identifier, \*\*<a href="src/cloudflare/types/magics/ipsec_tunnel_magic_i_psec_tunnels_update_multiple_i_psec_tunnels_params.py">params</a>) -> <a href="./src/cloudflare/types/magics/ipsec_tunnel_magic_i_psec_tunnels_update_multiple_i_psec_tunnels_response.py">IpsecTunnelMagicIPsecTunnelsUpdateMultipleIPsecTunnelsResponse</a></code>

### PskGenerates

Types:

```python
from cloudflare.types.magics.ipsec_tunnels import (
    PskGenerateMagicIPsecTunnelsGeneratePreSharedKeyPskForIPsecTunnelsResponse,
)
```

Methods:

- <code title="post /accounts/{account_identifier}/magic/ipsec_tunnels/{tunnel_identifier}/psk_generate">client.magics.ipsec_tunnels.psk_generates.<a href="./src/cloudflare/resources/magics/ipsec_tunnels/psk_generates.py">magic_i_psec_tunnels_generate_pre_shared_key_psk_for_i_psec_tunnels</a>(tunnel_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/magics/ipsec_tunnels/psk_generate_magic_i_psec_tunnels_generate_pre_shared_key_psk_for_i_psec_tunnels_response.py">PskGenerateMagicIPsecTunnelsGeneratePreSharedKeyPskForIPsecTunnelsResponse</a></code>

## Routes

Types:

```python
from cloudflare.types.magics import (
    RouteUpdateResponse,
    RouteDeleteResponse,
    RouteGetResponse,
    RouteMagicStaticRoutesCreateRoutesResponse,
    RouteMagicStaticRoutesListRoutesResponse,
    RouteMagicStaticRoutesUpdateManyRoutesResponse,
)
```

Methods:

- <code title="put /accounts/{account_identifier}/magic/routes/{route_identifier}">client.magics.routes.<a href="./src/cloudflare/resources/magics/routes.py">update</a>(route_identifier, \*, account_identifier, \*\*<a href="src/cloudflare/types/magics/route_update_params.py">params</a>) -> <a href="./src/cloudflare/types/magics/route_update_response.py">RouteUpdateResponse</a></code>
- <code title="delete /accounts/{account_identifier}/magic/routes/{route_identifier}">client.magics.routes.<a href="./src/cloudflare/resources/magics/routes.py">delete</a>(route_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/magics/route_delete_response.py">RouteDeleteResponse</a></code>
- <code title="get /accounts/{account_identifier}/magic/routes/{route_identifier}">client.magics.routes.<a href="./src/cloudflare/resources/magics/routes.py">get</a>(route_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/magics/route_get_response.py">RouteGetResponse</a></code>
- <code title="post /accounts/{account_identifier}/magic/routes">client.magics.routes.<a href="./src/cloudflare/resources/magics/routes.py">magic_static_routes_create_routes</a>(account_identifier, \*\*<a href="src/cloudflare/types/magics/route_magic_static_routes_create_routes_params.py">params</a>) -> <a href="./src/cloudflare/types/magics/route_magic_static_routes_create_routes_response.py">RouteMagicStaticRoutesCreateRoutesResponse</a></code>
- <code title="get /accounts/{account_identifier}/magic/routes">client.magics.routes.<a href="./src/cloudflare/resources/magics/routes.py">magic_static_routes_list_routes</a>(account_identifier) -> <a href="./src/cloudflare/types/magics/route_magic_static_routes_list_routes_response.py">RouteMagicStaticRoutesListRoutesResponse</a></code>
- <code title="put /accounts/{account_identifier}/magic/routes">client.magics.routes.<a href="./src/cloudflare/resources/magics/routes.py">magic_static_routes_update_many_routes</a>(account_identifier, \*\*<a href="src/cloudflare/types/magics/route_magic_static_routes_update_many_routes_params.py">params</a>) -> <a href="./src/cloudflare/types/magics/route_magic_static_routes_update_many_routes_response.py">RouteMagicStaticRoutesUpdateManyRoutesResponse</a></code>

# AccountMembers

Types:

```python
from cloudflare.types import (
    AccountMemberCreateResponse,
    AccountMemberUpdateResponse,
    AccountMemberListResponse,
    AccountMemberDeleteResponse,
    AccountMemberGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/members">client.account_members.<a href="./src/cloudflare/resources/account_members.py">create</a>(account_id, \*\*<a href="src/cloudflare/types/account_member_create_params.py">params</a>) -> <a href="./src/cloudflare/types/account_member_create_response.py">AccountMemberCreateResponse</a></code>
- <code title="put /accounts/{account_id}/members/{member_id}">client.account_members.<a href="./src/cloudflare/resources/account_members.py">update</a>(member_id, \*, account_id, \*\*<a href="src/cloudflare/types/account_member_update_params.py">params</a>) -> <a href="./src/cloudflare/types/account_member_update_response.py">AccountMemberUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/members">client.account_members.<a href="./src/cloudflare/resources/account_members.py">list</a>(account_id, \*\*<a href="src/cloudflare/types/account_member_list_params.py">params</a>) -> <a href="./src/cloudflare/types/account_member_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/members/{member_id}">client.account_members.<a href="./src/cloudflare/resources/account_members.py">delete</a>(member_id, \*, account_id) -> <a href="./src/cloudflare/types/account_member_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/members/{member_id}">client.account_members.<a href="./src/cloudflare/resources/account_members.py">get</a>(member_id, \*, account_id) -> <a href="./src/cloudflare/types/account_member_get_response.py">AccountMemberGetResponse</a></code>

# Mnms

## Configs

Types:

```python
from cloudflare.types.mnms import (
    ConfigDeleteResponse,
    ConfigMagicNetworkMonitoringConfigurationCreateAccountConfigurationResponse,
    ConfigMagicNetworkMonitoringConfigurationListAccountConfigurationResponse,
    ConfigMagicNetworkMonitoringConfigurationUpdateAccountConfigurationFieldsResponse,
    ConfigMagicNetworkMonitoringConfigurationUpdateAnEntireAccountConfigurationResponse,
)
```

Methods:

- <code title="delete /accounts/{account_identifier}/mnm/config">client.mnms.configs.<a href="./src/cloudflare/resources/mnms/configs/configs.py">delete</a>(account_identifier) -> <a href="./src/cloudflare/types/mnms/config_delete_response.py">ConfigDeleteResponse</a></code>
- <code title="post /accounts/{account_identifier}/mnm/config">client.mnms.configs.<a href="./src/cloudflare/resources/mnms/configs/configs.py">magic_network_monitoring_configuration_create_account_configuration</a>(account_identifier) -> <a href="./src/cloudflare/types/mnms/config_magic_network_monitoring_configuration_create_account_configuration_response.py">ConfigMagicNetworkMonitoringConfigurationCreateAccountConfigurationResponse</a></code>
- <code title="get /accounts/{account_identifier}/mnm/config">client.mnms.configs.<a href="./src/cloudflare/resources/mnms/configs/configs.py">magic_network_monitoring_configuration_list_account_configuration</a>(account_identifier) -> <a href="./src/cloudflare/types/mnms/config_magic_network_monitoring_configuration_list_account_configuration_response.py">ConfigMagicNetworkMonitoringConfigurationListAccountConfigurationResponse</a></code>
- <code title="patch /accounts/{account_identifier}/mnm/config">client.mnms.configs.<a href="./src/cloudflare/resources/mnms/configs/configs.py">magic_network_monitoring_configuration_update_account_configuration_fields</a>(account_identifier) -> <a href="./src/cloudflare/types/mnms/config_magic_network_monitoring_configuration_update_account_configuration_fields_response.py">ConfigMagicNetworkMonitoringConfigurationUpdateAccountConfigurationFieldsResponse</a></code>
- <code title="put /accounts/{account_identifier}/mnm/config">client.mnms.configs.<a href="./src/cloudflare/resources/mnms/configs/configs.py">magic_network_monitoring_configuration_update_an_entire_account_configuration</a>(account_identifier) -> <a href="./src/cloudflare/types/mnms/config_magic_network_monitoring_configuration_update_an_entire_account_configuration_response.py">ConfigMagicNetworkMonitoringConfigurationUpdateAnEntireAccountConfigurationResponse</a></code>

### Fulls

Types:

```python
from cloudflare.types.mnms.configs import (
    FullMagicNetworkMonitoringConfigurationListRulesAndAccountConfigurationResponse,
)
```

Methods:

- <code title="get /accounts/{account_identifier}/mnm/config/full">client.mnms.configs.fulls.<a href="./src/cloudflare/resources/mnms/configs/fulls.py">magic_network_monitoring_configuration_list_rules_and_account_configuration</a>(account_identifier) -> <a href="./src/cloudflare/types/mnms/configs/full_magic_network_monitoring_configuration_list_rules_and_account_configuration_response.py">FullMagicNetworkMonitoringConfigurationListRulesAndAccountConfigurationResponse</a></code>

## Rules

Types:

```python
from cloudflare.types.mnms import (
    RuleUpdateResponse,
    RuleDeleteResponse,
    RuleGetResponse,
    RuleMagicNetworkMonitoringRulesCreateRulesResponse,
    RuleMagicNetworkMonitoringRulesListRulesResponse,
    RuleMagicNetworkMonitoringRulesUpdateRulesResponse,
)
```

Methods:

- <code title="patch /accounts/{account_identifier}/mnm/rules/{rule_identifier}">client.mnms.rules.<a href="./src/cloudflare/resources/mnms/rules/rules.py">update</a>(rule_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/mnms/rule_update_response.py">Optional</a></code>
- <code title="delete /accounts/{account_identifier}/mnm/rules/{rule_identifier}">client.mnms.rules.<a href="./src/cloudflare/resources/mnms/rules/rules.py">delete</a>(rule_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/mnms/rule_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_identifier}/mnm/rules/{rule_identifier}">client.mnms.rules.<a href="./src/cloudflare/resources/mnms/rules/rules.py">get</a>(rule_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/mnms/rule_get_response.py">Optional</a></code>
- <code title="post /accounts/{account_identifier}/mnm/rules">client.mnms.rules.<a href="./src/cloudflare/resources/mnms/rules/rules.py">magic_network_monitoring_rules_create_rules</a>(account_identifier) -> <a href="./src/cloudflare/types/mnms/rule_magic_network_monitoring_rules_create_rules_response.py">Optional</a></code>
- <code title="get /accounts/{account_identifier}/mnm/rules">client.mnms.rules.<a href="./src/cloudflare/resources/mnms/rules/rules.py">magic_network_monitoring_rules_list_rules</a>(account_identifier) -> <a href="./src/cloudflare/types/mnms/rule_magic_network_monitoring_rules_list_rules_response.py">Optional</a></code>
- <code title="put /accounts/{account_identifier}/mnm/rules">client.mnms.rules.<a href="./src/cloudflare/resources/mnms/rules/rules.py">magic_network_monitoring_rules_update_rules</a>(account_identifier) -> <a href="./src/cloudflare/types/mnms/rule_magic_network_monitoring_rules_update_rules_response.py">Optional</a></code>

### Advertisements

Types:

```python
from cloudflare.types.mnms.rules import (
    AdvertisementMagicNetworkMonitoringRulesUpdateAdvertisementForRuleResponse,
)
```

Methods:

- <code title="patch /accounts/{account_identifier}/mnm/rules/{rule_identifier}/advertisement">client.mnms.rules.advertisements.<a href="./src/cloudflare/resources/mnms/rules/advertisements.py">magic_network_monitoring_rules_update_advertisement_for_rule</a>(rule_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/mnms/rules/advertisement_magic_network_monitoring_rules_update_advertisement_for_rule_response.py">Optional</a></code>

# MtlsCertificates

Types:

```python
from cloudflare.types import (
    MtlsCertificateUpdateResponse,
    MtlsCertificateListResponse,
    MtlsCertificateDeleteResponse,
    MtlsCertificateGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/mtls_certificates">client.mtls_certificates.<a href="./src/cloudflare/resources/mtls_certificates/mtls_certificates.py">update</a>(account_id, \*\*<a href="src/cloudflare/types/mtls_certificate_update_params.py">params</a>) -> <a href="./src/cloudflare/types/mtls_certificate_update_response.py">MtlsCertificateUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/mtls_certificates">client.mtls_certificates.<a href="./src/cloudflare/resources/mtls_certificates/mtls_certificates.py">list</a>(account_id) -> <a href="./src/cloudflare/types/mtls_certificate_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/mtls_certificates/{mtls_certificate_id}">client.mtls_certificates.<a href="./src/cloudflare/resources/mtls_certificates/mtls_certificates.py">delete</a>(mtls_certificate_id, \*, account_id) -> <a href="./src/cloudflare/types/mtls_certificate_delete_response.py">MtlsCertificateDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/mtls_certificates/{mtls_certificate_id}">client.mtls_certificates.<a href="./src/cloudflare/resources/mtls_certificates/mtls_certificates.py">get</a>(mtls_certificate_id, \*, account_id) -> <a href="./src/cloudflare/types/mtls_certificate_get_response.py">MtlsCertificateGetResponse</a></code>

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
    ProjectUpdateResponse,
    ProjectListResponse,
    ProjectDeleteResponse,
    ProjectGetResponse,
    ProjectPurgeBuildCacheResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/pages/projects">client.pages.projects.<a href="./src/cloudflare/resources/pages/projects/projects.py">create</a>(account_id, \*\*<a href="src/cloudflare/types/pages/project_create_params.py">params</a>) -> <a href="./src/cloudflare/types/pages/project_create_response.py">ProjectCreateResponse</a></code>
- <code title="patch /accounts/{account_id}/pages/projects/{project_name}">client.pages.projects.<a href="./src/cloudflare/resources/pages/projects/projects.py">update</a>(project_name, \*, account_id, \*\*<a href="src/cloudflare/types/pages/project_update_params.py">params</a>) -> <a href="./src/cloudflare/types/pages/project_update_response.py">ProjectUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/pages/projects">client.pages.projects.<a href="./src/cloudflare/resources/pages/projects/projects.py">list</a>(account_id) -> <a href="./src/cloudflare/types/pages/project_list_response.py">ProjectListResponse</a></code>
- <code title="delete /accounts/{account_id}/pages/projects/{project_name}">client.pages.projects.<a href="./src/cloudflare/resources/pages/projects/projects.py">delete</a>(project_name, \*, account_id) -> <a href="./src/cloudflare/types/pages/project_delete_response.py">object</a></code>
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
)
```

Methods:

- <code title="post /accounts/{account_id}/pages/projects/{project_name}/deployments">client.pages.projects.deployments.<a href="./src/cloudflare/resources/pages/projects/deployments/deployments.py">create</a>(project_name, \*, account_id, \*\*<a href="src/cloudflare/types/pages/projects/deployment_create_params.py">params</a>) -> <a href="./src/cloudflare/types/pages/projects/deployment_create_response.py">DeploymentCreateResponse</a></code>
- <code title="get /accounts/{account_id}/pages/projects/{project_name}/deployments">client.pages.projects.deployments.<a href="./src/cloudflare/resources/pages/projects/deployments/deployments.py">list</a>(project_name, \*, account_id) -> <a href="./src/cloudflare/types/pages/projects/deployment_list_response.py">DeploymentListResponse</a></code>
- <code title="delete /accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}">client.pages.projects.deployments.<a href="./src/cloudflare/resources/pages/projects/deployments/deployments.py">delete</a>(deployment_id, \*, account_id, project_name) -> <a href="./src/cloudflare/types/pages/projects/deployment_delete_response.py">object</a></code>
- <code title="get /accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}">client.pages.projects.deployments.<a href="./src/cloudflare/resources/pages/projects/deployments/deployments.py">get</a>(deployment_id, \*, account_id, project_name) -> <a href="./src/cloudflare/types/pages/projects/deployment_get_response.py">DeploymentGetResponse</a></code>

#### Histories

##### Logs

Types:

```python
from cloudflare.types.pages.projects.deployments.histories import (
    LogPagesDeploymentGetDeploymentLogsResponse,
)
```

Methods:

- <code title="get /accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}/history/logs">client.pages.projects.deployments.histories.logs.<a href="./src/cloudflare/resources/pages/projects/deployments/histories/logs.py">pages_deployment_get_deployment_logs</a>(deployment_id, \*, account_id, project_name) -> <a href="./src/cloudflare/types/pages/projects/deployments/histories/log_pages_deployment_get_deployment_logs_response.py">LogPagesDeploymentGetDeploymentLogsResponse</a></code>

#### Retries

Types:

```python
from cloudflare.types.pages.projects.deployments import RetryPagesDeploymentRetryDeploymentResponse
```

Methods:

- <code title="post /accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}/retry">client.pages.projects.deployments.retries.<a href="./src/cloudflare/resources/pages/projects/deployments/retries.py">pages_deployment_retry_deployment</a>(deployment_id, \*, account_id, project_name) -> <a href="./src/cloudflare/types/pages/projects/deployments/retry_pages_deployment_retry_deployment_response.py">RetryPagesDeploymentRetryDeploymentResponse</a></code>

#### Rollbacks

Types:

```python
from cloudflare.types.pages.projects.deployments import (
    RollbackPagesDeploymentRollbackDeploymentResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}/rollback">client.pages.projects.deployments.rollbacks.<a href="./src/cloudflare/resources/pages/projects/deployments/rollbacks.py">pages_deployment_rollback_deployment</a>(deployment_id, \*, account_id, project_name) -> <a href="./src/cloudflare/types/pages/projects/deployments/rollback_pages_deployment_rollback_deployment_response.py">RollbackPagesDeploymentRollbackDeploymentResponse</a></code>

### Domains

Types:

```python
from cloudflare.types.pages.projects import (
    DomainUpdateResponse,
    DomainDeleteResponse,
    DomainGetResponse,
    DomainPagesDomainsAddDomainResponse,
    DomainPagesDomainsGetDomainsResponse,
)
```

Methods:

- <code title="patch /accounts/{account_id}/pages/projects/{project_name}/domains/{domain_name}">client.pages.projects.domains.<a href="./src/cloudflare/resources/pages/projects/domains.py">update</a>(domain_name, \*, account_id, project_name) -> <a href="./src/cloudflare/types/pages/projects/domain_update_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/pages/projects/{project_name}/domains/{domain_name}">client.pages.projects.domains.<a href="./src/cloudflare/resources/pages/projects/domains.py">delete</a>(domain_name, \*, account_id, project_name) -> <a href="./src/cloudflare/types/pages/projects/domain_delete_response.py">object</a></code>
- <code title="get /accounts/{account_id}/pages/projects/{project_name}/domains/{domain_name}">client.pages.projects.domains.<a href="./src/cloudflare/resources/pages/projects/domains.py">get</a>(domain_name, \*, account_id, project_name) -> <a href="./src/cloudflare/types/pages/projects/domain_get_response.py">Optional</a></code>
- <code title="post /accounts/{account_id}/pages/projects/{project_name}/domains">client.pages.projects.domains.<a href="./src/cloudflare/resources/pages/projects/domains.py">pages_domains_add_domain</a>(project_name, \*, account_id, \*\*<a href="src/cloudflare/types/pages/projects/domain_pages_domains_add_domain_params.py">params</a>) -> <a href="./src/cloudflare/types/pages/projects/domain_pages_domains_add_domain_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/pages/projects/{project_name}/domains">client.pages.projects.domains.<a href="./src/cloudflare/resources/pages/projects/domains.py">pages_domains_get_domains</a>(project_name, \*, account_id) -> <a href="./src/cloudflare/types/pages/projects/domain_pages_domains_get_domains_response.py">DomainPagesDomainsGetDomainsResponse</a></code>

# Pcaps

Types:

```python
from cloudflare.types import (
    PcapGetResponse,
    PcapMagicPcapCollectionCreatePcapRequestResponse,
    PcapMagicPcapCollectionListPacketCaptureRequestsResponse,
)
```

Methods:

- <code title="get /accounts/{account_identifier}/pcaps/{identifier}">client.pcaps.<a href="./src/cloudflare/resources/pcaps/pcaps.py">get</a>(identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/pcap_get_response.py">PcapGetResponse</a></code>
- <code title="post /accounts/{account_identifier}/pcaps">client.pcaps.<a href="./src/cloudflare/resources/pcaps/pcaps.py">magic_pcap_collection_create_pcap_request</a>(account_identifier, \*\*<a href="src/cloudflare/types/pcap_magic_pcap_collection_create_pcap_request_params.py">params</a>) -> <a href="./src/cloudflare/types/pcap_magic_pcap_collection_create_pcap_request_response.py">PcapMagicPcapCollectionCreatePcapRequestResponse</a></code>
- <code title="get /accounts/{account_identifier}/pcaps">client.pcaps.<a href="./src/cloudflare/resources/pcaps/pcaps.py">magic_pcap_collection_list_packet_capture_requests</a>(account_identifier) -> <a href="./src/cloudflare/types/pcap_magic_pcap_collection_list_packet_capture_requests_response.py">Optional</a></code>

## Ownerships

Types:

```python
from cloudflare.types.pcaps import (
    OwnershipMagicPcapCollectionAddBucketsForFullPacketCapturesResponse,
    OwnershipMagicPcapCollectionListPcaPsBucketOwnershipResponse,
)
```

Methods:

- <code title="delete /accounts/{account_identifier}/pcaps/ownership/{identifier}">client.pcaps.ownerships.<a href="./src/cloudflare/resources/pcaps/ownerships/ownerships.py">delete</a>(identifier, \*, account_identifier) -> None</code>
- <code title="post /accounts/{account_identifier}/pcaps/ownership">client.pcaps.ownerships.<a href="./src/cloudflare/resources/pcaps/ownerships/ownerships.py">magic_pcap_collection_add_buckets_for_full_packet_captures</a>(account_identifier, \*\*<a href="src/cloudflare/types/pcaps/ownership_magic_pcap_collection_add_buckets_for_full_packet_captures_params.py">params</a>) -> <a href="./src/cloudflare/types/pcaps/ownership_magic_pcap_collection_add_buckets_for_full_packet_captures_response.py">OwnershipMagicPcapCollectionAddBucketsForFullPacketCapturesResponse</a></code>
- <code title="get /accounts/{account_identifier}/pcaps/ownership">client.pcaps.ownerships.<a href="./src/cloudflare/resources/pcaps/ownerships/ownerships.py">magic_pcap_collection_list_pca_ps_bucket_ownership</a>(account_identifier) -> <a href="./src/cloudflare/types/pcaps/ownership_magic_pcap_collection_list_pca_ps_bucket_ownership_response.py">Optional</a></code>

### Validates

Types:

```python
from cloudflare.types.pcaps.ownerships import (
    ValidateMagicPcapCollectionValidateBucketsForFullPacketCapturesResponse,
)
```

Methods:

- <code title="post /accounts/{account_identifier}/pcaps/ownership/validate">client.pcaps.ownerships.validates.<a href="./src/cloudflare/resources/pcaps/ownerships/validates.py">magic_pcap_collection_validate_buckets_for_full_packet_captures</a>(account_identifier, \*\*<a href="src/cloudflare/types/pcaps/ownerships/validate_magic_pcap_collection_validate_buckets_for_full_packet_captures_params.py">params</a>) -> <a href="./src/cloudflare/types/pcaps/ownerships/validate_magic_pcap_collection_validate_buckets_for_full_packet_captures_response.py">ValidateMagicPcapCollectionValidateBucketsForFullPacketCapturesResponse</a></code>

## Downloads

Methods:

- <code title="get /accounts/{account_identifier}/pcaps/{identifier}/download">client.pcaps.downloads.<a href="./src/cloudflare/resources/pcaps/downloads.py">list</a>(identifier, \*, account_identifier) -> BinaryAPIResponse</code>

# Registrar

## Domains

Types:

```python
from cloudflare.types.registrar import DomainUpdateResponse, DomainListResponse, DomainGetResponse
```

Methods:

- <code title="put /accounts/{account_id}/registrar/domains/{domain_name}">client.registrar.domains.<a href="./src/cloudflare/resources/registrar/domains.py">update</a>(domain_name, \*, account_id, \*\*<a href="src/cloudflare/types/registrar/domain_update_params.py">params</a>) -> <a href="./src/cloudflare/types/registrar/domain_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/registrar/domains">client.registrar.domains.<a href="./src/cloudflare/resources/registrar/domains.py">list</a>(account_id) -> <a href="./src/cloudflare/types/registrar/domain_list_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/registrar/domains/{domain_name}">client.registrar.domains.<a href="./src/cloudflare/resources/registrar/domains.py">get</a>(domain_name, \*, account_id) -> <a href="./src/cloudflare/types/registrar/domain_get_response.py">Optional</a></code>

# RequestTracers

## Traces

Types:

```python
from cloudflare.types.request_tracers import TraceCreateResponse
```

Methods:

- <code title="post /accounts/{account_identifier}/request-tracer/trace">client.request_tracers.traces.<a href="./src/cloudflare/resources/request_tracers/traces.py">create</a>(account_identifier, \*\*<a href="src/cloudflare/types/request_tracers/trace_create_params.py">params</a>) -> <a href="./src/cloudflare/types/request_tracers/trace_create_response.py">TraceCreateResponse</a></code>

# Roles

Types:

```python
from cloudflare.types import RoleAccountRolesListRolesResponse, RoleGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/roles">client.roles.<a href="./src/cloudflare/resources/roles.py">account_roles_list_roles</a>(account_id) -> <a href="./src/cloudflare/types/role_account_roles_list_roles_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/roles/{role_id}">client.roles.<a href="./src/cloudflare/resources/roles.py">get</a>(role_id, \*, account_id) -> <a href="./src/cloudflare/types/role_get_response.py">RoleGetResponse</a></code>

# Rules

## Lists

Types:

```python
from cloudflare.types.rules import (
    ListUpdateResponse,
    ListDeleteResponse,
    ListGetResponse,
    ListListsCreateAListResponse,
    ListListsGetListsResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/rules/lists/{list_id}">client.rules.lists.<a href="./src/cloudflare/resources/rules/lists/lists.py">update</a>(list_id, \*, account_id, \*\*<a href="src/cloudflare/types/rules/list_update_params.py">params</a>) -> <a href="./src/cloudflare/types/rules/list_update_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/rules/lists/{list_id}">client.rules.lists.<a href="./src/cloudflare/resources/rules/lists/lists.py">delete</a>(list_id, \*, account_id) -> <a href="./src/cloudflare/types/rules/list_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/rules/lists/{list_id}">client.rules.lists.<a href="./src/cloudflare/resources/rules/lists/lists.py">get</a>(list_id, \*, account_id) -> <a href="./src/cloudflare/types/rules/list_get_response.py">Optional</a></code>
- <code title="post /accounts/{account_id}/rules/lists">client.rules.lists.<a href="./src/cloudflare/resources/rules/lists/lists.py">lists_create_a_list</a>(account_id, \*\*<a href="src/cloudflare/types/rules/list_lists_create_a_list_params.py">params</a>) -> <a href="./src/cloudflare/types/rules/list_lists_create_a_list_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/rules/lists">client.rules.lists.<a href="./src/cloudflare/resources/rules/lists/lists.py">lists_get_lists</a>(account_id) -> <a href="./src/cloudflare/types/rules/list_lists_get_lists_response.py">Optional</a></code>

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
    ItemDeleteResponse,
    ItemGetResponse,
    ItemListsCreateListItemsResponse,
    ItemListsGetListItemsResponse,
    ItemListsUpdateAllListItemsResponse,
)
```

Methods:

- <code title="delete /accounts/{account_id}/rules/lists/{list_id}/items">client.rules.lists.items.<a href="./src/cloudflare/resources/rules/lists/items.py">delete</a>(list_id, \*, account_id, \*\*<a href="src/cloudflare/types/rules/lists/item_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/rules/lists/item_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_identifier}/rules/lists/{list_id}/items/{item_id}">client.rules.lists.items.<a href="./src/cloudflare/resources/rules/lists/items.py">get</a>(item_id, \*, account_identifier, list_id) -> <a href="./src/cloudflare/types/rules/lists/item_get_response.py">Optional</a></code>
- <code title="post /accounts/{account_id}/rules/lists/{list_id}/items">client.rules.lists.items.<a href="./src/cloudflare/resources/rules/lists/items.py">lists_create_list_items</a>(list_id, \*, account_id, \*\*<a href="src/cloudflare/types/rules/lists/item_lists_create_list_items_params.py">params</a>) -> <a href="./src/cloudflare/types/rules/lists/item_lists_create_list_items_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/rules/lists/{list_id}/items">client.rules.lists.items.<a href="./src/cloudflare/resources/rules/lists/items.py">lists_get_list_items</a>(list_id, \*, account_id, \*\*<a href="src/cloudflare/types/rules/lists/item_lists_get_list_items_params.py">params</a>) -> <a href="./src/cloudflare/types/rules/lists/item_lists_get_list_items_response.py">Optional</a></code>
- <code title="put /accounts/{account_id}/rules/lists/{list_id}/items">client.rules.lists.items.<a href="./src/cloudflare/resources/rules/lists/items.py">lists_update_all_list_items</a>(list_id, \*, account_id, \*\*<a href="src/cloudflare/types/rules/lists/item_lists_update_all_list_items_params.py">params</a>) -> <a href="./src/cloudflare/types/rules/lists/item_lists_update_all_list_items_response.py">Optional</a></code>

# Storage

## Analytics

Types:

```python
from cloudflare.types.storage import AnalyticsListResponse, AnalyticsStoredResponse
```

Methods:

- <code title="get /accounts/{account_id}/storage/analytics">client.storage.analytics.<a href="./src/cloudflare/resources/storage/analytics.py">list</a>(account_id, \*\*<a href="src/cloudflare/types/storage/analytics_list_params.py">params</a>) -> <a href="./src/cloudflare/types/storage/analytics_list_response.py">AnalyticsListResponse</a></code>
- <code title="get /accounts/{account_id}/storage/analytics/stored">client.storage.analytics.<a href="./src/cloudflare/resources/storage/analytics.py">stored</a>(account_id, \*\*<a href="src/cloudflare/types/storage/analytics_stored_params.py">params</a>) -> <a href="./src/cloudflare/types/storage/analytics_stored_response.py">AnalyticsStoredResponse</a></code>

## Kv

### Namespaces

Types:

```python
from cloudflare.types.storage.kv import (
    NamespaceUpdateResponse,
    NamespaceListResponse,
    NamespaceDeleteResponse,
    NamespaceWorkersKvNamespaceCreateANamespaceResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/storage/kv/namespaces/{namespace_id}">client.storage.kv.namespaces.<a href="./src/cloudflare/resources/storage/kv/namespaces/namespaces.py">update</a>(namespace_id, \*, account_id, \*\*<a href="src/cloudflare/types/storage/kv/namespace_update_params.py">params</a>) -> <a href="./src/cloudflare/types/storage/kv/namespace_update_response.py">NamespaceUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/storage/kv/namespaces">client.storage.kv.namespaces.<a href="./src/cloudflare/resources/storage/kv/namespaces/namespaces.py">list</a>(account_id, \*\*<a href="src/cloudflare/types/storage/kv/namespace_list_params.py">params</a>) -> <a href="./src/cloudflare/types/storage/kv/namespace_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/storage/kv/namespaces/{namespace_id}">client.storage.kv.namespaces.<a href="./src/cloudflare/resources/storage/kv/namespaces/namespaces.py">delete</a>(namespace_id, \*, account_id) -> <a href="./src/cloudflare/types/storage/kv/namespace_delete_response.py">NamespaceDeleteResponse</a></code>
- <code title="post /accounts/{account_id}/storage/kv/namespaces">client.storage.kv.namespaces.<a href="./src/cloudflare/resources/storage/kv/namespaces/namespaces.py">workers_kv_namespace_create_a_namespace</a>(account_id, \*\*<a href="src/cloudflare/types/storage/kv/namespace_workers_kv_namespace_create_a_namespace_params.py">params</a>) -> <a href="./src/cloudflare/types/storage/kv/namespace_workers_kv_namespace_create_a_namespace_response.py">NamespaceWorkersKvNamespaceCreateANamespaceResponse</a></code>

#### Bulks

Types:

```python
from cloudflare.types.storage.kv.namespaces import (
    BulkDeleteResponse,
    BulkWorkersKvNamespaceWriteMultipleKeyValuePairsResponse,
)
```

Methods:

- <code title="delete /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk">client.storage.kv.namespaces.bulks.<a href="./src/cloudflare/resources/storage/kv/namespaces/bulks.py">delete</a>(namespace_id, \*, account_id, \*\*<a href="src/cloudflare/types/storage/kv/namespaces/bulk_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/storage/kv/namespaces/bulk_delete_response.py">BulkDeleteResponse</a></code>
- <code title="put /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk">client.storage.kv.namespaces.bulks.<a href="./src/cloudflare/resources/storage/kv/namespaces/bulks.py">workers_kv_namespace_write_multiple_key_value_pairs</a>(namespace_id, \*, account_id, \*\*<a href="src/cloudflare/types/storage/kv/namespaces/bulk_workers_kv_namespace_write_multiple_key_value_pairs_params.py">params</a>) -> <a href="./src/cloudflare/types/storage/kv/namespaces/bulk_workers_kv_namespace_write_multiple_key_value_pairs_response.py">BulkWorkersKvNamespaceWriteMultipleKeyValuePairsResponse</a></code>

#### Keys

Types:

```python
from cloudflare.types.storage.kv.namespaces import KeyListResponse
```

Methods:

- <code title="get /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/keys">client.storage.kv.namespaces.keys.<a href="./src/cloudflare/resources/storage/kv/namespaces/keys.py">list</a>(namespace_id, \*, account_id, \*\*<a href="src/cloudflare/types/storage/kv/namespaces/key_list_params.py">params</a>) -> <a href="./src/cloudflare/types/storage/kv/namespaces/key_list_response.py">KeyListResponse</a></code>

#### Metadata

Types:

```python
from cloudflare.types.storage.kv.namespaces import MetadataGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/metadata/{key_name}">client.storage.kv.namespaces.metadata.<a href="./src/cloudflare/resources/storage/kv/namespaces/metadata.py">get</a>(key_name, \*, account_id, namespace_id) -> <a href="./src/cloudflare/types/storage/kv/namespaces/metadata_get_response.py">object</a></code>

#### Values

Types:

```python
from cloudflare.types.storage.kv.namespaces import (
    ValueUpdateResponse,
    ValueDeleteResponse,
    ValueGetResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}">client.storage.kv.namespaces.values.<a href="./src/cloudflare/resources/storage/kv/namespaces/values.py">update</a>(key_name, \*, account_id, namespace_id, \*\*<a href="src/cloudflare/types/storage/kv/namespaces/value_update_params.py">params</a>) -> <a href="./src/cloudflare/types/storage/kv/namespaces/value_update_response.py">ValueUpdateResponse</a></code>
- <code title="delete /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}">client.storage.kv.namespaces.values.<a href="./src/cloudflare/resources/storage/kv/namespaces/values.py">delete</a>(key_name, \*, account_id, namespace_id) -> <a href="./src/cloudflare/types/storage/kv/namespaces/value_delete_response.py">ValueDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}">client.storage.kv.namespaces.values.<a href="./src/cloudflare/resources/storage/kv/namespaces/values.py">get</a>(key_name, \*, account_id, namespace_id) -> str</code>

# Stream

Types:

```python
from cloudflare.types import (
    StreamUpdateResponse,
    StreamGetResponse,
    StreamStreamVideosListVideosResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/stream/{identifier}">client.stream.<a href="./src/cloudflare/resources/stream/stream.py">update</a>(identifier, \*, account_id, \*\*<a href="src/cloudflare/types/stream_update_params.py">params</a>) -> <a href="./src/cloudflare/types/stream_update_response.py">StreamUpdateResponse</a></code>
- <code title="delete /accounts/{account_id}/stream/{identifier}">client.stream.<a href="./src/cloudflare/resources/stream/stream.py">delete</a>(identifier, \*, account_id) -> None</code>
- <code title="get /accounts/{account_id}/stream/{identifier}">client.stream.<a href="./src/cloudflare/resources/stream/stream.py">get</a>(identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream_get_response.py">StreamGetResponse</a></code>
- <code title="post /accounts/{account_id}/stream">client.stream.<a href="./src/cloudflare/resources/stream/stream.py">stream_videos_initiate_video_uploads_using_tus</a>(account_id) -> None</code>
- <code title="get /accounts/{account_id}/stream">client.stream.<a href="./src/cloudflare/resources/stream/stream.py">stream_videos_list_videos</a>(account_id, \*\*<a href="src/cloudflare/types/stream_stream_videos_list_videos_params.py">params</a>) -> <a href="./src/cloudflare/types/stream_stream_videos_list_videos_response.py">StreamStreamVideosListVideosResponse</a></code>

## AudioTracks

Types:

```python
from cloudflare.types.stream import (
    AudioTrackUpdateResponse,
    AudioTrackListResponse,
    AudioTrackDeleteResponse,
    AudioTrackCopyResponse,
)
```

Methods:

- <code title="patch /accounts/{account_id}/stream/{identifier}/audio/{audio_identifier}">client.stream.audio_tracks.<a href="./src/cloudflare/resources/stream/audio_tracks.py">update</a>(audio_identifier, \*, account_id, identifier, \*\*<a href="src/cloudflare/types/stream/audio_track_update_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/audio_track_update_response.py">AudioTrackUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/stream/{identifier}/audio">client.stream.audio_tracks.<a href="./src/cloudflare/resources/stream/audio_tracks.py">list</a>(identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/audio_track_list_response.py">AudioTrackListResponse</a></code>
- <code title="delete /accounts/{account_id}/stream/{identifier}/audio/{audio_identifier}">client.stream.audio_tracks.<a href="./src/cloudflare/resources/stream/audio_tracks.py">delete</a>(audio_identifier, \*, account_id, identifier) -> <a href="./src/cloudflare/types/stream/audio_track_delete_response.py">AudioTrackDeleteResponse</a></code>
- <code title="post /accounts/{account_id}/stream/{identifier}/audio/copy">client.stream.audio_tracks.<a href="./src/cloudflare/resources/stream/audio_tracks.py">copy</a>(identifier, \*, account_id, \*\*<a href="src/cloudflare/types/stream/audio_track_copy_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/audio_track_copy_response.py">AudioTrackCopyResponse</a></code>

## Videos

Types:

```python
from cloudflare.types.stream import VideoStorageUsageResponse
```

Methods:

- <code title="get /accounts/{account_id}/stream/storage-usage">client.stream.videos.<a href="./src/cloudflare/resources/stream/videos.py">storage_usage</a>(account_id, \*\*<a href="src/cloudflare/types/stream/video_storage_usage_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/video_storage_usage_response.py">VideoStorageUsageResponse</a></code>

## Clips

Types:

```python
from cloudflare.types.stream import ClipStreamVideoClippingClipVideosGivenAStartAndEndTimeResponse
```

Methods:

- <code title="post /accounts/{account_id}/stream/clip">client.stream.clips.<a href="./src/cloudflare/resources/stream/clips.py">stream_video_clipping_clip_videos_given_a_start_and_end_time</a>(account_id, \*\*<a href="src/cloudflare/types/stream/clip_stream_video_clipping_clip_videos_given_a_start_and_end_time_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/clip_stream_video_clipping_clip_videos_given_a_start_and_end_time_response.py">ClipStreamVideoClippingClipVideosGivenAStartAndEndTimeResponse</a></code>

## Copies

Types:

```python
from cloudflare.types.stream import CopyStreamVideosUploadVideosFromAURLResponse
```

Methods:

- <code title="post /accounts/{account_id}/stream/copy">client.stream.copies.<a href="./src/cloudflare/resources/stream/copies.py">stream_videos_upload_videos_from_a_url</a>(account_id, \*\*<a href="src/cloudflare/types/stream/copy_stream_videos_upload_videos_from_a_url_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/copy_stream_videos_upload_videos_from_a_url_response.py">CopyStreamVideosUploadVideosFromAURLResponse</a></code>

## DirectUploads

Types:

```python
from cloudflare.types.stream import DirectUploadStreamVideosUploadVideosViaDirectUploadURLsResponse
```

Methods:

- <code title="post /accounts/{account_id}/stream/direct_upload">client.stream.direct_uploads.<a href="./src/cloudflare/resources/stream/direct_uploads.py">stream_videos_upload_videos_via_direct_upload_urls</a>(account_id, \*\*<a href="src/cloudflare/types/stream/direct_upload_stream_videos_upload_videos_via_direct_upload_urls_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/direct_upload_stream_videos_upload_videos_via_direct_upload_urls_response.py">DirectUploadStreamVideosUploadVideosViaDirectUploadURLsResponse</a></code>

## Keys

Types:

```python
from cloudflare.types.stream import (
    KeyDeleteResponse,
    KeyStreamSigningKeysCreateSigningKeysResponse,
    KeyStreamSigningKeysListSigningKeysResponse,
)
```

Methods:

- <code title="delete /accounts/{account_id}/stream/keys/{identifier}">client.stream.keys.<a href="./src/cloudflare/resources/stream/keys.py">delete</a>(identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/key_delete_response.py">KeyDeleteResponse</a></code>
- <code title="post /accounts/{account_id}/stream/keys">client.stream.keys.<a href="./src/cloudflare/resources/stream/keys.py">stream_signing_keys_create_signing_keys</a>(account_id) -> <a href="./src/cloudflare/types/stream/key_stream_signing_keys_create_signing_keys_response.py">KeyStreamSigningKeysCreateSigningKeysResponse</a></code>
- <code title="get /accounts/{account_id}/stream/keys">client.stream.keys.<a href="./src/cloudflare/resources/stream/keys.py">stream_signing_keys_list_signing_keys</a>(account_id) -> <a href="./src/cloudflare/types/stream/key_stream_signing_keys_list_signing_keys_response.py">KeyStreamSigningKeysListSigningKeysResponse</a></code>

## LiveInputs

Types:

```python
from cloudflare.types.stream import (
    LiveInputUpdateResponse,
    LiveInputGetResponse,
    LiveInputStreamLiveInputsCreateALiveInputResponse,
    LiveInputStreamLiveInputsListLiveInputsResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/stream/live_inputs/{live_input_identifier}">client.stream.live_inputs.<a href="./src/cloudflare/resources/stream/live_inputs/live_inputs.py">update</a>(live_input_identifier, \*, account_id, \*\*<a href="src/cloudflare/types/stream/live_input_update_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/live_input_update_response.py">LiveInputUpdateResponse</a></code>
- <code title="delete /accounts/{account_id}/stream/live_inputs/{live_input_identifier}">client.stream.live_inputs.<a href="./src/cloudflare/resources/stream/live_inputs/live_inputs.py">delete</a>(live_input_identifier, \*, account_id) -> None</code>
- <code title="get /accounts/{account_id}/stream/live_inputs/{live_input_identifier}">client.stream.live_inputs.<a href="./src/cloudflare/resources/stream/live_inputs/live_inputs.py">get</a>(live_input_identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/live_input_get_response.py">LiveInputGetResponse</a></code>
- <code title="post /accounts/{account_id}/stream/live_inputs">client.stream.live_inputs.<a href="./src/cloudflare/resources/stream/live_inputs/live_inputs.py">stream_live_inputs_create_a_live_input</a>(account_id, \*\*<a href="src/cloudflare/types/stream/live_input_stream_live_inputs_create_a_live_input_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/live_input_stream_live_inputs_create_a_live_input_response.py">LiveInputStreamLiveInputsCreateALiveInputResponse</a></code>
- <code title="get /accounts/{account_id}/stream/live_inputs">client.stream.live_inputs.<a href="./src/cloudflare/resources/stream/live_inputs/live_inputs.py">stream_live_inputs_list_live_inputs</a>(account_id, \*\*<a href="src/cloudflare/types/stream/live_input_stream_live_inputs_list_live_inputs_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/live_input_stream_live_inputs_list_live_inputs_response.py">LiveInputStreamLiveInputsListLiveInputsResponse</a></code>

### Outputs

Types:

```python
from cloudflare.types.stream.live_inputs import (
    OutputUpdateResponse,
    OutputStreamLiveInputsCreateANewOutputConnectedToALiveInputResponse,
    OutputStreamLiveInputsListAllOutputsAssociatedWithASpecifiedLiveInputResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs/{output_identifier}">client.stream.live_inputs.outputs.<a href="./src/cloudflare/resources/stream/live_inputs/outputs.py">update</a>(output_identifier, \*, account_id, live_input_identifier, \*\*<a href="src/cloudflare/types/stream/live_inputs/output_update_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/live_inputs/output_update_response.py">OutputUpdateResponse</a></code>
- <code title="delete /accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs/{output_identifier}">client.stream.live_inputs.outputs.<a href="./src/cloudflare/resources/stream/live_inputs/outputs.py">delete</a>(output_identifier, \*, account_id, live_input_identifier) -> None</code>
- <code title="post /accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs">client.stream.live_inputs.outputs.<a href="./src/cloudflare/resources/stream/live_inputs/outputs.py">stream_live_inputs_create_a_new_output_connected_to_a_live_input</a>(live_input_identifier, \*, account_id, \*\*<a href="src/cloudflare/types/stream/live_inputs/output_stream_live_inputs_create_a_new_output_connected_to_a_live_input_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/live_inputs/output_stream_live_inputs_create_a_new_output_connected_to_a_live_input_response.py">OutputStreamLiveInputsCreateANewOutputConnectedToALiveInputResponse</a></code>
- <code title="get /accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs">client.stream.live_inputs.outputs.<a href="./src/cloudflare/resources/stream/live_inputs/outputs.py">stream_live_inputs_list_all_outputs_associated_with_a_specified_live_input</a>(live_input_identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/live_inputs/output_stream_live_inputs_list_all_outputs_associated_with_a_specified_live_input_response.py">OutputStreamLiveInputsListAllOutputsAssociatedWithASpecifiedLiveInputResponse</a></code>

## Watermarks

Types:

```python
from cloudflare.types.stream import (
    WatermarkDeleteResponse,
    WatermarkGetResponse,
    WatermarkStreamWatermarkProfileCreateWatermarkProfilesViaBasicUploadResponse,
    WatermarkStreamWatermarkProfileListWatermarkProfilesResponse,
)
```

Methods:

- <code title="delete /accounts/{account_id}/stream/watermarks/{identifier}">client.stream.watermarks.<a href="./src/cloudflare/resources/stream/watermarks.py">delete</a>(identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/watermark_delete_response.py">WatermarkDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/stream/watermarks/{identifier}">client.stream.watermarks.<a href="./src/cloudflare/resources/stream/watermarks.py">get</a>(identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/watermark_get_response.py">WatermarkGetResponse</a></code>
- <code title="post /accounts/{account_id}/stream/watermarks">client.stream.watermarks.<a href="./src/cloudflare/resources/stream/watermarks.py">stream_watermark_profile_create_watermark_profiles_via_basic_upload</a>(account_id, \*\*<a href="src/cloudflare/types/stream/watermark_stream_watermark_profile_create_watermark_profiles_via_basic_upload_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/watermark_stream_watermark_profile_create_watermark_profiles_via_basic_upload_response.py">WatermarkStreamWatermarkProfileCreateWatermarkProfilesViaBasicUploadResponse</a></code>
- <code title="get /accounts/{account_id}/stream/watermarks">client.stream.watermarks.<a href="./src/cloudflare/resources/stream/watermarks.py">stream_watermark_profile_list_watermark_profiles</a>(account_id) -> <a href="./src/cloudflare/types/stream/watermark_stream_watermark_profile_list_watermark_profiles_response.py">WatermarkStreamWatermarkProfileListWatermarkProfilesResponse</a></code>

## Webhooks

Types:

```python
from cloudflare.types.stream import (
    WebhookDeleteResponse,
    WebhookStreamWebhookCreateWebhooksResponse,
    WebhookStreamWebhookViewWebhooksResponse,
)
```

Methods:

- <code title="delete /accounts/{account_id}/stream/webhook">client.stream.webhooks.<a href="./src/cloudflare/resources/stream/webhooks.py">delete</a>(account_id) -> <a href="./src/cloudflare/types/stream/webhook_delete_response.py">WebhookDeleteResponse</a></code>
- <code title="put /accounts/{account_id}/stream/webhook">client.stream.webhooks.<a href="./src/cloudflare/resources/stream/webhooks.py">stream_webhook_create_webhooks</a>(account_id, \*\*<a href="src/cloudflare/types/stream/webhook_stream_webhook_create_webhooks_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/webhook_stream_webhook_create_webhooks_response.py">WebhookStreamWebhookCreateWebhooksResponse</a></code>
- <code title="get /accounts/{account_id}/stream/webhook">client.stream.webhooks.<a href="./src/cloudflare/resources/stream/webhooks.py">stream_webhook_view_webhooks</a>(account_id) -> <a href="./src/cloudflare/types/stream/webhook_stream_webhook_view_webhooks_response.py">WebhookStreamWebhookViewWebhooksResponse</a></code>

## Captions

Types:

```python
from cloudflare.types.stream import (
    CaptionUpdateResponse,
    CaptionDeleteResponse,
    CaptionStreamSubtitlesCaptionsListCaptionsOrSubtitlesResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/stream/{identifier}/captions/{language}">client.stream.captions.<a href="./src/cloudflare/resources/stream/captions.py">update</a>(language, \*, account_id, identifier, \*\*<a href="src/cloudflare/types/stream/caption_update_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/caption_update_response.py">CaptionUpdateResponse</a></code>
- <code title="delete /accounts/{account_id}/stream/{identifier}/captions/{language}">client.stream.captions.<a href="./src/cloudflare/resources/stream/captions.py">delete</a>(language, \*, account_id, identifier) -> <a href="./src/cloudflare/types/stream/caption_delete_response.py">CaptionDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/stream/{identifier}/captions">client.stream.captions.<a href="./src/cloudflare/resources/stream/captions.py">stream_subtitles_captions_list_captions_or_subtitles</a>(identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/caption_stream_subtitles_captions_list_captions_or_subtitles_response.py">CaptionStreamSubtitlesCaptionsListCaptionsOrSubtitlesResponse</a></code>

## Downloads

Types:

```python
from cloudflare.types.stream import (
    DownloadDeleteResponse,
    DownloadStreamMP4DownloadsCreateDownloadsResponse,
    DownloadStreamMP4DownloadsListDownloadsResponse,
)
```

Methods:

- <code title="delete /accounts/{account_id}/stream/{identifier}/downloads">client.stream.downloads.<a href="./src/cloudflare/resources/stream/downloads.py">delete</a>(identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/download_delete_response.py">DownloadDeleteResponse</a></code>
- <code title="post /accounts/{account_id}/stream/{identifier}/downloads">client.stream.downloads.<a href="./src/cloudflare/resources/stream/downloads.py">stream_m_p_4_downloads_create_downloads</a>(identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/download_stream_m_p_4_downloads_create_downloads_response.py">DownloadStreamMP4DownloadsCreateDownloadsResponse</a></code>
- <code title="get /accounts/{account_id}/stream/{identifier}/downloads">client.stream.downloads.<a href="./src/cloudflare/resources/stream/downloads.py">stream_m_p_4_downloads_list_downloads</a>(identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/download_stream_m_p_4_downloads_list_downloads_response.py">DownloadStreamMP4DownloadsListDownloadsResponse</a></code>

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
from cloudflare.types.stream import TokenStreamVideosCreateSignedURLTokensForVideosResponse
```

Methods:

- <code title="post /accounts/{account_id}/stream/{identifier}/token">client.stream.tokens.<a href="./src/cloudflare/resources/stream/tokens.py">stream_videos_create_signed_url_tokens_for_videos</a>(identifier, \*, account_id, \*\*<a href="src/cloudflare/types/stream/token_stream_videos_create_signed_url_tokens_for_videos_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/token_stream_videos_create_signed_url_tokens_for_videos_response.py">TokenStreamVideosCreateSignedURLTokensForVideosResponse</a></code>

# Teamnets

## Routes

Types:

```python
from cloudflare.types.teamnets import RouteTunnelRouteListTunnelRoutesResponse
```

Methods:

- <code title="get /accounts/{account_id}/teamnet/routes">client.teamnets.routes.<a href="./src/cloudflare/resources/teamnets/routes/routes.py">tunnel_route_list_tunnel_routes</a>(account_id, \*\*<a href="src/cloudflare/types/teamnets/route_tunnel_route_list_tunnel_routes_params.py">params</a>) -> <a href="./src/cloudflare/types/teamnets/route_tunnel_route_list_tunnel_routes_response.py">Optional</a></code>

### IPs

Types:

```python
from cloudflare.types.teamnets.routes import IPGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/teamnet/routes/ip/{ip}">client.teamnets.routes.ips.<a href="./src/cloudflare/resources/teamnets/routes/ips.py">get</a>(ip, \*, account_id, \*\*<a href="src/cloudflare/types/teamnets/routes/ip_get_params.py">params</a>) -> <a href="./src/cloudflare/types/teamnets/routes/ip_get_response.py">IPGetResponse</a></code>

### Networks

Types:

```python
from cloudflare.types.teamnets.routes import NetworkUpdateResponse, NetworkDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}">client.teamnets.routes.networks.<a href="./src/cloudflare/resources/teamnets/routes/networks.py">update</a>(ip_network_encoded, \*, account_id, \*\*<a href="src/cloudflare/types/teamnets/routes/network_update_params.py">params</a>) -> <a href="./src/cloudflare/types/teamnets/routes/network_update_response.py">NetworkUpdateResponse</a></code>
- <code title="delete /accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}">client.teamnets.routes.networks.<a href="./src/cloudflare/resources/teamnets/routes/networks.py">delete</a>(ip_network_encoded, \*, account_id, \*\*<a href="src/cloudflare/types/teamnets/routes/network_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/teamnets/routes/network_delete_response.py">NetworkDeleteResponse</a></code>

## VirtualNetworks

Types:

```python
from cloudflare.types.teamnets import (
    VirtualNetworkUpdateResponse,
    VirtualNetworkDeleteResponse,
    VirtualNetworkTunnelVirtualNetworkCreateAVirtualNetworkResponse,
    VirtualNetworkTunnelVirtualNetworkListVirtualNetworksResponse,
)
```

Methods:

- <code title="patch /accounts/{account_id}/teamnet/virtual_networks/{virtual_network_id}">client.teamnets.virtual_networks.<a href="./src/cloudflare/resources/teamnets/virtual_networks.py">update</a>(virtual_network_id, \*, account_id, \*\*<a href="src/cloudflare/types/teamnets/virtual_network_update_params.py">params</a>) -> <a href="./src/cloudflare/types/teamnets/virtual_network_update_response.py">VirtualNetworkUpdateResponse</a></code>
- <code title="delete /accounts/{account_id}/teamnet/virtual_networks/{virtual_network_id}">client.teamnets.virtual_networks.<a href="./src/cloudflare/resources/teamnets/virtual_networks.py">delete</a>(virtual_network_id, \*, account_id) -> <a href="./src/cloudflare/types/teamnets/virtual_network_delete_response.py">VirtualNetworkDeleteResponse</a></code>
- <code title="post /accounts/{account_id}/teamnet/virtual_networks">client.teamnets.virtual_networks.<a href="./src/cloudflare/resources/teamnets/virtual_networks.py">tunnel_virtual_network_create_a_virtual_network</a>(account_id, \*\*<a href="src/cloudflare/types/teamnets/virtual_network_tunnel_virtual_network_create_a_virtual_network_params.py">params</a>) -> <a href="./src/cloudflare/types/teamnets/virtual_network_tunnel_virtual_network_create_a_virtual_network_response.py">VirtualNetworkTunnelVirtualNetworkCreateAVirtualNetworkResponse</a></code>
- <code title="get /accounts/{account_id}/teamnet/virtual_networks">client.teamnets.virtual_networks.<a href="./src/cloudflare/resources/teamnets/virtual_networks.py">tunnel_virtual_network_list_virtual_networks</a>(account_id, \*\*<a href="src/cloudflare/types/teamnets/virtual_network_tunnel_virtual_network_list_virtual_networks_params.py">params</a>) -> <a href="./src/cloudflare/types/teamnets/virtual_network_tunnel_virtual_network_list_virtual_networks_response.py">Optional</a></code>

# Tunnels

Types:

```python
from cloudflare.types import (
    TunnelDeleteResponse,
    TunnelArgoTunnelCreateAnArgoTunnelResponse,
    TunnelArgoTunnelListArgoTunnelsResponse,
    TunnelGetResponse,
)
```

Methods:

- <code title="delete /accounts/{account_id}/tunnels/{tunnel_id}">client.tunnels.<a href="./src/cloudflare/resources/tunnels/tunnels.py">delete</a>(tunnel_id, \*, account_id, \*\*<a href="src/cloudflare/types/tunnel_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/tunnel_delete_response.py">TunnelDeleteResponse</a></code>
- <code title="post /accounts/{account_id}/tunnels">client.tunnels.<a href="./src/cloudflare/resources/tunnels/tunnels.py">argo_tunnel_create_an_argo_tunnel</a>(account_id, \*\*<a href="src/cloudflare/types/tunnel_argo_tunnel_create_an_argo_tunnel_params.py">params</a>) -> <a href="./src/cloudflare/types/tunnel_argo_tunnel_create_an_argo_tunnel_response.py">TunnelArgoTunnelCreateAnArgoTunnelResponse</a></code>
- <code title="get /accounts/{account_id}/tunnels">client.tunnels.<a href="./src/cloudflare/resources/tunnels/tunnels.py">argo_tunnel_list_argo_tunnels</a>(account_id, \*\*<a href="src/cloudflare/types/tunnel_argo_tunnel_list_argo_tunnels_params.py">params</a>) -> <a href="./src/cloudflare/types/tunnel_argo_tunnel_list_argo_tunnels_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/tunnels/{tunnel_id}">client.tunnels.<a href="./src/cloudflare/resources/tunnels/tunnels.py">get</a>(tunnel_id, \*, account_id) -> <a href="./src/cloudflare/types/tunnel_get_response.py">TunnelGetResponse</a></code>

## Connections

Types:

```python
from cloudflare.types.tunnels import ConnectionDeleteResponse
```

Methods:

- <code title="delete /accounts/{account_id}/tunnels/{tunnel_id}/connections">client.tunnels.connections.<a href="./src/cloudflare/resources/tunnels/connections.py">delete</a>(tunnel_id, \*, account_id, \*\*<a href="src/cloudflare/types/tunnels/connection_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/tunnels/connection_delete_response.py">ConnectionDeleteResponse</a></code>

# Gateways

Types:

```python
from cloudflare.types import (
    GatewayZeroTrustAccountsCreateZeroTrustAccountResponse,
    GatewayZeroTrustAccountsGetZeroTrustAccountInformationResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/gateway">client.gateways.<a href="./src/cloudflare/resources/gateways/gateways.py">zero_trust_accounts_create_zero_trust_account</a>(account_id) -> <a href="./src/cloudflare/types/gateway_zero_trust_accounts_create_zero_trust_account_response.py">GatewayZeroTrustAccountsCreateZeroTrustAccountResponse</a></code>
- <code title="get /accounts/{account_id}/gateway">client.gateways.<a href="./src/cloudflare/resources/gateways/gateways.py">zero_trust_accounts_get_zero_trust_account_information</a>(account_id) -> <a href="./src/cloudflare/types/gateway_zero_trust_accounts_get_zero_trust_account_information_response.py">GatewayZeroTrustAccountsGetZeroTrustAccountInformationResponse</a></code>

## Categories

Types:

```python
from cloudflare.types.gateways import CategoryZeroTrustGatewayCategoriesListCategoriesResponse
```

Methods:

- <code title="get /accounts/{account_id}/gateway/categories">client.gateways.categories.<a href="./src/cloudflare/resources/gateways/categories.py">zero_trust_gateway_categories_list_categories</a>(account_id) -> <a href="./src/cloudflare/types/gateways/category_zero_trust_gateway_categories_list_categories_response.py">Optional</a></code>

## AppTypes

Types:

```python
from cloudflare.types.gateways import (
    AppTypeZeroTrustGatewayApplicationAndApplicationTypeMappingsListApplicationAndApplicationTypeMappingsResponse,
)
```

Methods:

- <code title="get /accounts/{account_id}/gateway/app_types">client.gateways.app_types.<a href="./src/cloudflare/resources/gateways/app_types.py">zero_trust_gateway_application_and_application_type_mappings_list_application_and_application_type_mappings</a>(account_id) -> <a href="./src/cloudflare/types/gateways/app_type_zero_trust_gateway_application_and_application_type_mappings_list_application_and_application_type_mappings_response.py">Optional</a></code>

## Configurations

Types:

```python
from cloudflare.types.gateways import (
    ConfigurationZeroTrustAccountsGetZeroTrustAccountConfigurationResponse,
    ConfigurationZeroTrustAccountsPatchZeroTrustAccountConfigurationResponse,
    ConfigurationZeroTrustAccountsUpdateZeroTrustAccountConfigurationResponse,
)
```

Methods:

- <code title="get /accounts/{account_id}/gateway/configuration">client.gateways.configurations.<a href="./src/cloudflare/resources/gateways/configurations.py">zero_trust_accounts_get_zero_trust_account_configuration</a>(account_id) -> <a href="./src/cloudflare/types/gateways/configuration_zero_trust_accounts_get_zero_trust_account_configuration_response.py">ConfigurationZeroTrustAccountsGetZeroTrustAccountConfigurationResponse</a></code>
- <code title="patch /accounts/{account_id}/gateway/configuration">client.gateways.configurations.<a href="./src/cloudflare/resources/gateways/configurations.py">zero_trust_accounts_patch_zero_trust_account_configuration</a>(account_id, \*\*<a href="src/cloudflare/types/gateways/configuration_zero_trust_accounts_patch_zero_trust_account_configuration_params.py">params</a>) -> <a href="./src/cloudflare/types/gateways/configuration_zero_trust_accounts_patch_zero_trust_account_configuration_response.py">ConfigurationZeroTrustAccountsPatchZeroTrustAccountConfigurationResponse</a></code>
- <code title="put /accounts/{account_id}/gateway/configuration">client.gateways.configurations.<a href="./src/cloudflare/resources/gateways/configurations.py">zero_trust_accounts_update_zero_trust_account_configuration</a>(account_id, \*\*<a href="src/cloudflare/types/gateways/configuration_zero_trust_accounts_update_zero_trust_account_configuration_params.py">params</a>) -> <a href="./src/cloudflare/types/gateways/configuration_zero_trust_accounts_update_zero_trust_account_configuration_response.py">ConfigurationZeroTrustAccountsUpdateZeroTrustAccountConfigurationResponse</a></code>

## Lists

Types:

```python
from cloudflare.types.gateways import (
    ListUpdateResponse,
    ListDeleteResponse,
    ListGetResponse,
    ListZeroTrustListsCreateZeroTrustListResponse,
    ListZeroTrustListsListZeroTrustListsResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/gateway/lists/{list_id}">client.gateways.lists.<a href="./src/cloudflare/resources/gateways/lists/lists.py">update</a>(list_id, \*, account_id, \*\*<a href="src/cloudflare/types/gateways/list_update_params.py">params</a>) -> <a href="./src/cloudflare/types/gateways/list_update_response.py">ListUpdateResponse</a></code>
- <code title="delete /accounts/{account_id}/gateway/lists/{list_id}">client.gateways.lists.<a href="./src/cloudflare/resources/gateways/lists/lists.py">delete</a>(list_id, \*, account_id) -> <a href="./src/cloudflare/types/gateways/list_delete_response.py">ListDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/gateway/lists/{list_id}">client.gateways.lists.<a href="./src/cloudflare/resources/gateways/lists/lists.py">get</a>(list_id, \*, account_id) -> <a href="./src/cloudflare/types/gateways/list_get_response.py">ListGetResponse</a></code>
- <code title="post /accounts/{account_id}/gateway/lists">client.gateways.lists.<a href="./src/cloudflare/resources/gateways/lists/lists.py">zero_trust_lists_create_zero_trust_list</a>(account_id, \*\*<a href="src/cloudflare/types/gateways/list_zero_trust_lists_create_zero_trust_list_params.py">params</a>) -> <a href="./src/cloudflare/types/gateways/list_zero_trust_lists_create_zero_trust_list_response.py">ListZeroTrustListsCreateZeroTrustListResponse</a></code>
- <code title="get /accounts/{account_id}/gateway/lists">client.gateways.lists.<a href="./src/cloudflare/resources/gateways/lists/lists.py">zero_trust_lists_list_zero_trust_lists</a>(account_id) -> <a href="./src/cloudflare/types/gateways/list_zero_trust_lists_list_zero_trust_lists_response.py">Optional</a></code>

### Items

Types:

```python
from cloudflare.types.gateways.lists import ItemZeroTrustListsZeroTrustListItemsResponse
```

Methods:

- <code title="get /accounts/{account_id}/gateway/lists/{list_id}/items">client.gateways.lists.items.<a href="./src/cloudflare/resources/gateways/lists/items.py">zero_trust_lists_zero_trust_list_items</a>(list_id, \*, account_id) -> <a href="./src/cloudflare/types/gateways/lists/item_zero_trust_lists_zero_trust_list_items_response.py">Optional</a></code>

## Locations

Types:

```python
from cloudflare.types.gateways import (
    LocationUpdateResponse,
    LocationDeleteResponse,
    LocationGetResponse,
    LocationZeroTrustGatewayLocationsCreateZeroTrustGatewayLocationResponse,
    LocationZeroTrustGatewayLocationsListZeroTrustGatewayLocationsResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/gateway/locations/{location_id}">client.gateways.locations.<a href="./src/cloudflare/resources/gateways/locations.py">update</a>(location_id, \*, account_id, \*\*<a href="src/cloudflare/types/gateways/location_update_params.py">params</a>) -> <a href="./src/cloudflare/types/gateways/location_update_response.py">LocationUpdateResponse</a></code>
- <code title="delete /accounts/{account_id}/gateway/locations/{location_id}">client.gateways.locations.<a href="./src/cloudflare/resources/gateways/locations.py">delete</a>(location_id, \*, account_id) -> <a href="./src/cloudflare/types/gateways/location_delete_response.py">LocationDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/gateway/locations/{location_id}">client.gateways.locations.<a href="./src/cloudflare/resources/gateways/locations.py">get</a>(location_id, \*, account_id) -> <a href="./src/cloudflare/types/gateways/location_get_response.py">LocationGetResponse</a></code>
- <code title="post /accounts/{account_id}/gateway/locations">client.gateways.locations.<a href="./src/cloudflare/resources/gateways/locations.py">zero_trust_gateway_locations_create_zero_trust_gateway_location</a>(account_id, \*\*<a href="src/cloudflare/types/gateways/location_zero_trust_gateway_locations_create_zero_trust_gateway_location_params.py">params</a>) -> <a href="./src/cloudflare/types/gateways/location_zero_trust_gateway_locations_create_zero_trust_gateway_location_response.py">LocationZeroTrustGatewayLocationsCreateZeroTrustGatewayLocationResponse</a></code>
- <code title="get /accounts/{account_id}/gateway/locations">client.gateways.locations.<a href="./src/cloudflare/resources/gateways/locations.py">zero_trust_gateway_locations_list_zero_trust_gateway_locations</a>(account_id) -> <a href="./src/cloudflare/types/gateways/location_zero_trust_gateway_locations_list_zero_trust_gateway_locations_response.py">Optional</a></code>

## Loggings

Types:

```python
from cloudflare.types.gateways import (
    LoggingZeroTrustAccountsGetLoggingSettingsForTheZeroTrustAccountResponse,
    LoggingZeroTrustAccountsUpdateLoggingSettingsForTheZeroTrustAccountResponse,
)
```

Methods:

- <code title="get /accounts/{account_id}/gateway/logging">client.gateways.loggings.<a href="./src/cloudflare/resources/gateways/loggings.py">zero_trust_accounts_get_logging_settings_for_the_zero_trust_account</a>(account_id) -> <a href="./src/cloudflare/types/gateways/logging_zero_trust_accounts_get_logging_settings_for_the_zero_trust_account_response.py">LoggingZeroTrustAccountsGetLoggingSettingsForTheZeroTrustAccountResponse</a></code>
- <code title="put /accounts/{account_id}/gateway/logging">client.gateways.loggings.<a href="./src/cloudflare/resources/gateways/loggings.py">zero_trust_accounts_update_logging_settings_for_the_zero_trust_account</a>(account_id, \*\*<a href="src/cloudflare/types/gateways/logging_zero_trust_accounts_update_logging_settings_for_the_zero_trust_account_params.py">params</a>) -> <a href="./src/cloudflare/types/gateways/logging_zero_trust_accounts_update_logging_settings_for_the_zero_trust_account_response.py">LoggingZeroTrustAccountsUpdateLoggingSettingsForTheZeroTrustAccountResponse</a></code>

## ProxyEndpoints

Types:

```python
from cloudflare.types.gateways import (
    ProxyEndpointUpdateResponse,
    ProxyEndpointListResponse,
    ProxyEndpointDeleteResponse,
    ProxyEndpointGetResponse,
    ProxyEndpointZeroTrustGatewayProxyEndpointsCreateProxyEndpointResponse,
    ProxyEndpointZeroTrustGatewayProxyEndpointsListProxyEndpointsResponse,
)
```

Methods:

- <code title="patch /accounts/{account_id}/gateway/proxy_endpoints/{proxy_endpoint_id}">client.gateways.proxy_endpoints.<a href="./src/cloudflare/resources/gateways/proxy_endpoints.py">update</a>(proxy_endpoint_id, \*, account_id, \*\*<a href="src/cloudflare/types/gateways/proxy_endpoint_update_params.py">params</a>) -> <a href="./src/cloudflare/types/gateways/proxy_endpoint_update_response.py">ProxyEndpointUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/gateway/proxy_endpoints/{proxy_endpoint_id}">client.gateways.proxy_endpoints.<a href="./src/cloudflare/resources/gateways/proxy_endpoints.py">list</a>(proxy_endpoint_id, \*, account_id) -> <a href="./src/cloudflare/types/gateways/proxy_endpoint_list_response.py">ProxyEndpointListResponse</a></code>
- <code title="delete /accounts/{account_id}/gateway/proxy_endpoints/{proxy_endpoint_id}">client.gateways.proxy_endpoints.<a href="./src/cloudflare/resources/gateways/proxy_endpoints.py">delete</a>(proxy_endpoint_id, \*, account_id) -> <a href="./src/cloudflare/types/gateways/proxy_endpoint_delete_response.py">ProxyEndpointDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/gateway/proxy_endpoints/{proxy_endpoint_id}">client.gateways.proxy_endpoints.<a href="./src/cloudflare/resources/gateways/proxy_endpoints.py">get</a>(proxy_endpoint_id, \*, account_id) -> <a href="./src/cloudflare/types/gateways/proxy_endpoint_get_response.py">ProxyEndpointGetResponse</a></code>
- <code title="post /accounts/{account_id}/gateway/proxy_endpoints">client.gateways.proxy_endpoints.<a href="./src/cloudflare/resources/gateways/proxy_endpoints.py">zero_trust_gateway_proxy_endpoints_create_proxy_endpoint</a>(account_id, \*\*<a href="src/cloudflare/types/gateways/proxy_endpoint_zero_trust_gateway_proxy_endpoints_create_proxy_endpoint_params.py">params</a>) -> <a href="./src/cloudflare/types/gateways/proxy_endpoint_zero_trust_gateway_proxy_endpoints_create_proxy_endpoint_response.py">ProxyEndpointZeroTrustGatewayProxyEndpointsCreateProxyEndpointResponse</a></code>
- <code title="get /accounts/{account_id}/gateway/proxy_endpoints">client.gateways.proxy_endpoints.<a href="./src/cloudflare/resources/gateways/proxy_endpoints.py">zero_trust_gateway_proxy_endpoints_list_proxy_endpoints</a>(account_id) -> <a href="./src/cloudflare/types/gateways/proxy_endpoint_zero_trust_gateway_proxy_endpoints_list_proxy_endpoints_response.py">Optional</a></code>

## Rules

Types:

```python
from cloudflare.types.gateways import (
    RuleUpdateResponse,
    RuleDeleteResponse,
    RuleGetResponse,
    RuleZeroTrustGatewayRulesCreateZeroTrustGatewayRuleResponse,
    RuleZeroTrustGatewayRulesListZeroTrustGatewayRulesResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/gateway/rules/{rule_id}">client.gateways.rules.<a href="./src/cloudflare/resources/gateways/rules.py">update</a>(rule_id, \*, account_id, \*\*<a href="src/cloudflare/types/gateways/rule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/gateways/rule_update_response.py">RuleUpdateResponse</a></code>
- <code title="delete /accounts/{account_id}/gateway/rules/{rule_id}">client.gateways.rules.<a href="./src/cloudflare/resources/gateways/rules.py">delete</a>(rule_id, \*, account_id) -> <a href="./src/cloudflare/types/gateways/rule_delete_response.py">RuleDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/gateway/rules/{rule_id}">client.gateways.rules.<a href="./src/cloudflare/resources/gateways/rules.py">get</a>(rule_id, \*, account_id) -> <a href="./src/cloudflare/types/gateways/rule_get_response.py">RuleGetResponse</a></code>
- <code title="post /accounts/{account_id}/gateway/rules">client.gateways.rules.<a href="./src/cloudflare/resources/gateways/rules.py">zero_trust_gateway_rules_create_zero_trust_gateway_rule</a>(account_id, \*\*<a href="src/cloudflare/types/gateways/rule_zero_trust_gateway_rules_create_zero_trust_gateway_rule_params.py">params</a>) -> <a href="./src/cloudflare/types/gateways/rule_zero_trust_gateway_rules_create_zero_trust_gateway_rule_response.py">RuleZeroTrustGatewayRulesCreateZeroTrustGatewayRuleResponse</a></code>
- <code title="get /accounts/{account_id}/gateway/rules">client.gateways.rules.<a href="./src/cloudflare/resources/gateways/rules.py">zero_trust_gateway_rules_list_zero_trust_gateway_rules</a>(account_id) -> <a href="./src/cloudflare/types/gateways/rule_zero_trust_gateway_rules_list_zero_trust_gateway_rules_response.py">Optional</a></code>

# Alerting

## V3s

### Destinations

#### Eligibles

Types:

```python
from cloudflare.types.alerting.v3s.destinations import (
    EligibleNotificationMechanismEligibilityGetDeliveryMechanismEligibilityResponse,
)
```

Methods:

- <code title="get /accounts/{account_id}/alerting/v3/destinations/eligible">client.alerting.v3s.destinations.eligibles.<a href="./src/cloudflare/resources/alerting/v3s/destinations/eligibles.py">notification_mechanism_eligibility_get_delivery_mechanism_eligibility</a>(account_id) -> <a href="./src/cloudflare/types/alerting/v3s/destinations/eligible_notification_mechanism_eligibility_get_delivery_mechanism_eligibility_response.py">Optional</a></code>

#### Pagerduties

Types:

```python
from cloudflare.types.alerting.v3s.destinations import (
    PagerdutyNotificationDestinationsWithPagerDutyListPagerDutyServicesResponse,
)
```

Methods:

- <code title="get /accounts/{account_id}/alerting/v3/destinations/pagerduty">client.alerting.v3s.destinations.pagerduties.<a href="./src/cloudflare/resources/alerting/v3s/destinations/pagerduties.py">notification_destinations_with_pager_duty_list_pager_duty_services</a>(account_id) -> <a href="./src/cloudflare/types/alerting/v3s/destinations/pagerduty_notification_destinations_with_pager_duty_list_pager_duty_services_response.py">Optional</a></code>

#### Webhooks

Types:

```python
from cloudflare.types.alerting.v3s.destinations import (
    WebhookUpdateResponse,
    WebhookDeleteResponse,
    WebhookGetResponse,
    WebhookNotificationWebhooksCreateAWebhookResponse,
    WebhookNotificationWebhooksListWebhooksResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/alerting/v3/destinations/webhooks/{webhook_id}">client.alerting.v3s.destinations.webhooks.<a href="./src/cloudflare/resources/alerting/v3s/destinations/webhooks.py">update</a>(webhook_id, \*, account_id, \*\*<a href="src/cloudflare/types/alerting/v3s/destinations/webhook_update_params.py">params</a>) -> <a href="./src/cloudflare/types/alerting/v3s/destinations/webhook_update_response.py">WebhookUpdateResponse</a></code>
- <code title="delete /accounts/{account_id}/alerting/v3/destinations/webhooks/{webhook_id}">client.alerting.v3s.destinations.webhooks.<a href="./src/cloudflare/resources/alerting/v3s/destinations/webhooks.py">delete</a>(webhook_id, \*, account_id) -> <a href="./src/cloudflare/types/alerting/v3s/destinations/webhook_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/alerting/v3/destinations/webhooks/{webhook_id}">client.alerting.v3s.destinations.webhooks.<a href="./src/cloudflare/resources/alerting/v3s/destinations/webhooks.py">get</a>(webhook_id, \*, account_id) -> <a href="./src/cloudflare/types/alerting/v3s/destinations/webhook_get_response.py">WebhookGetResponse</a></code>
- <code title="post /accounts/{account_id}/alerting/v3/destinations/webhooks">client.alerting.v3s.destinations.webhooks.<a href="./src/cloudflare/resources/alerting/v3s/destinations/webhooks.py">notification_webhooks_create_a_webhook</a>(account_id, \*\*<a href="src/cloudflare/types/alerting/v3s/destinations/webhook_notification_webhooks_create_a_webhook_params.py">params</a>) -> <a href="./src/cloudflare/types/alerting/v3s/destinations/webhook_notification_webhooks_create_a_webhook_response.py">WebhookNotificationWebhooksCreateAWebhookResponse</a></code>
- <code title="get /accounts/{account_id}/alerting/v3/destinations/webhooks">client.alerting.v3s.destinations.webhooks.<a href="./src/cloudflare/resources/alerting/v3s/destinations/webhooks.py">notification_webhooks_list_webhooks</a>(account_id) -> <a href="./src/cloudflare/types/alerting/v3s/destinations/webhook_notification_webhooks_list_webhooks_response.py">Optional</a></code>

### Histories

Types:

```python
from cloudflare.types.alerting.v3s import HistoryNotificationHistoryListHistoryResponse
```

Methods:

- <code title="get /accounts/{account_id}/alerting/v3/history">client.alerting.v3s.histories.<a href="./src/cloudflare/resources/alerting/v3s/histories.py">notification_history_list_history</a>(account_id, \*\*<a href="src/cloudflare/types/alerting/v3s/history_notification_history_list_history_params.py">params</a>) -> <a href="./src/cloudflare/types/alerting/v3s/history_notification_history_list_history_response.py">Optional</a></code>

### Policies

Types:

```python
from cloudflare.types.alerting.v3s import (
    PolicyUpdateResponse,
    PolicyDeleteResponse,
    PolicyGetResponse,
    PolicyNotificationPoliciesCreateANotificationPolicyResponse,
    PolicyNotificationPoliciesListNotificationPoliciesResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/alerting/v3/policies/{policy_id}">client.alerting.v3s.policies.<a href="./src/cloudflare/resources/alerting/v3s/policies.py">update</a>(policy_id, \*, account_id, \*\*<a href="src/cloudflare/types/alerting/v3s/policy_update_params.py">params</a>) -> <a href="./src/cloudflare/types/alerting/v3s/policy_update_response.py">PolicyUpdateResponse</a></code>
- <code title="delete /accounts/{account_id}/alerting/v3/policies/{policy_id}">client.alerting.v3s.policies.<a href="./src/cloudflare/resources/alerting/v3s/policies.py">delete</a>(policy_id, \*, account_id) -> <a href="./src/cloudflare/types/alerting/v3s/policy_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/alerting/v3/policies/{policy_id}">client.alerting.v3s.policies.<a href="./src/cloudflare/resources/alerting/v3s/policies.py">get</a>(policy_id, \*, account_id) -> <a href="./src/cloudflare/types/alerting/v3s/policy_get_response.py">PolicyGetResponse</a></code>
- <code title="post /accounts/{account_id}/alerting/v3/policies">client.alerting.v3s.policies.<a href="./src/cloudflare/resources/alerting/v3s/policies.py">notification_policies_create_a_notification_policy</a>(account_id, \*\*<a href="src/cloudflare/types/alerting/v3s/policy_notification_policies_create_a_notification_policy_params.py">params</a>) -> <a href="./src/cloudflare/types/alerting/v3s/policy_notification_policies_create_a_notification_policy_response.py">PolicyNotificationPoliciesCreateANotificationPolicyResponse</a></code>
- <code title="get /accounts/{account_id}/alerting/v3/policies">client.alerting.v3s.policies.<a href="./src/cloudflare/resources/alerting/v3s/policies.py">notification_policies_list_notification_policies</a>(account_id) -> <a href="./src/cloudflare/types/alerting/v3s/policy_notification_policies_list_notification_policies_response.py">Optional</a></code>

## V3

### AvailableAlerts

Types:

```python
from cloudflare.types.alerting.v3 import AvailableAlertListResponse
```

Methods:

- <code title="get /accounts/{account_id}/alerting/v3/available_alerts">client.alerting.v3.available_alerts.<a href="./src/cloudflare/resources/alerting/v3/available_alerts.py">list</a>(account_id) -> <a href="./src/cloudflare/types/alerting/v3/available_alert_list_response.py">Optional</a></code>

### Destinations

#### Pagerduty

Types:

```python
from cloudflare.types.alerting.v3.destinations import (
    PagerdutyCreateTokenResponse,
    PagerdutyDeleteAllResponse,
    PagerdutyLinkResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/alerting/v3/destinations/pagerduty/connect">client.alerting.v3.destinations.pagerduty.<a href="./src/cloudflare/resources/alerting/v3/destinations/pagerduty.py">create_token</a>(account_id) -> <a href="./src/cloudflare/types/alerting/v3/destinations/pagerduty_create_token_response.py">PagerdutyCreateTokenResponse</a></code>
- <code title="delete /accounts/{account_id}/alerting/v3/destinations/pagerduty">client.alerting.v3.destinations.pagerduty.<a href="./src/cloudflare/resources/alerting/v3/destinations/pagerduty.py">delete_all</a>(account_id) -> <a href="./src/cloudflare/types/alerting/v3/destinations/pagerduty_delete_all_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/alerting/v3/destinations/pagerduty/connect/{token_id}">client.alerting.v3.destinations.pagerduty.<a href="./src/cloudflare/resources/alerting/v3/destinations/pagerduty.py">link</a>(token_id, \*, account_id) -> <a href="./src/cloudflare/types/alerting/v3/destinations/pagerduty_link_response.py">PagerdutyLinkResponse</a></code>

# Devices

Types:

```python
from cloudflare.types import DeviceDevicesListDevicesResponse, DeviceGetResponse
```

Methods:

- <code title="get /accounts/{identifier}/devices">client.devices.<a href="./src/cloudflare/resources/devices/devices.py">devices_list_devices</a>(identifier) -> <a href="./src/cloudflare/types/device_devices_list_devices_response.py">Optional</a></code>
- <code title="get /accounts/{identifier}/devices/{uuid}">client.devices.<a href="./src/cloudflare/resources/devices/devices.py">get</a>(uuid, \*, identifier) -> <a href="./src/cloudflare/types/device_get_response.py">Optional</a></code>

## DEXTests

Types:

```python
from cloudflare.types.devices import (
    DEXTestUpdateResponse,
    DEXTestDeleteResponse,
    DEXTestDeviceDEXTestCreateDeviceDEXTestResponse,
    DEXTestDeviceDEXTestDetailsResponse,
    DEXTestGetResponse,
)
```

Methods:

- <code title="put /accounts/{identifier}/devices/dex_tests/{uuid}">client.devices.dex_tests.<a href="./src/cloudflare/resources/devices/dex_tests.py">update</a>(uuid, \*, identifier, \*\*<a href="src/cloudflare/types/devices/dex_test_update_params.py">params</a>) -> <a href="./src/cloudflare/types/devices/dex_test_update_response.py">Optional</a></code>
- <code title="delete /accounts/{identifier}/devices/dex_tests/{uuid}">client.devices.dex_tests.<a href="./src/cloudflare/resources/devices/dex_tests.py">delete</a>(uuid, \*, identifier) -> <a href="./src/cloudflare/types/devices/dex_test_delete_response.py">Optional</a></code>
- <code title="post /accounts/{identifier}/devices/dex_tests">client.devices.dex_tests.<a href="./src/cloudflare/resources/devices/dex_tests.py">device_dex_test_create_device_dex_test</a>(identifier, \*\*<a href="src/cloudflare/types/devices/dex_test_device_dex_test_create_device_dex_test_params.py">params</a>) -> <a href="./src/cloudflare/types/devices/dex_test_device_dex_test_create_device_dex_test_response.py">Optional</a></code>
- <code title="get /accounts/{identifier}/devices/dex_tests">client.devices.dex_tests.<a href="./src/cloudflare/resources/devices/dex_tests.py">device_dex_test_details</a>(identifier) -> <a href="./src/cloudflare/types/devices/dex_test_device_dex_test_details_response.py">Optional</a></code>
- <code title="get /accounts/{identifier}/devices/dex_tests/{uuid}">client.devices.dex_tests.<a href="./src/cloudflare/resources/devices/dex_tests.py">get</a>(uuid, \*, identifier) -> <a href="./src/cloudflare/types/devices/dex_test_get_response.py">Optional</a></code>

## Networks

Types:

```python
from cloudflare.types.devices import (
    NetworkUpdateResponse,
    NetworkDeleteResponse,
    NetworkDeviceManagedNetworksCreateDeviceManagedNetworkResponse,
    NetworkDeviceManagedNetworksListDeviceManagedNetworksResponse,
    NetworkGetResponse,
)
```

Methods:

- <code title="put /accounts/{identifier}/devices/networks/{uuid}">client.devices.networks.<a href="./src/cloudflare/resources/devices/networks.py">update</a>(uuid, \*, identifier, \*\*<a href="src/cloudflare/types/devices/network_update_params.py">params</a>) -> <a href="./src/cloudflare/types/devices/network_update_response.py">Optional</a></code>
- <code title="delete /accounts/{identifier}/devices/networks/{uuid}">client.devices.networks.<a href="./src/cloudflare/resources/devices/networks.py">delete</a>(uuid, \*, identifier) -> <a href="./src/cloudflare/types/devices/network_delete_response.py">Optional</a></code>
- <code title="post /accounts/{identifier}/devices/networks">client.devices.networks.<a href="./src/cloudflare/resources/devices/networks.py">device_managed_networks_create_device_managed_network</a>(identifier, \*\*<a href="src/cloudflare/types/devices/network_device_managed_networks_create_device_managed_network_params.py">params</a>) -> <a href="./src/cloudflare/types/devices/network_device_managed_networks_create_device_managed_network_response.py">Optional</a></code>
- <code title="get /accounts/{identifier}/devices/networks">client.devices.networks.<a href="./src/cloudflare/resources/devices/networks.py">device_managed_networks_list_device_managed_networks</a>(identifier) -> <a href="./src/cloudflare/types/devices/network_device_managed_networks_list_device_managed_networks_response.py">Optional</a></code>
- <code title="get /accounts/{identifier}/devices/networks/{uuid}">client.devices.networks.<a href="./src/cloudflare/resources/devices/networks.py">get</a>(uuid, \*, identifier) -> <a href="./src/cloudflare/types/devices/network_get_response.py">Optional</a></code>

## Policies

Types:

```python
from cloudflare.types.devices import (
    PolicyUpdateResponse,
    PolicyDeleteResponse,
    PolicyDevicesCreateDeviceSettingsPolicyResponse,
    PolicyDevicesGetDefaultDeviceSettingsPolicyResponse,
    PolicyDevicesListDeviceSettingsPoliciesResponse,
    PolicyDevicesUpdateDefaultDeviceSettingsPolicyResponse,
    PolicyGetResponse,
)
```

Methods:

- <code title="patch /accounts/{identifier}/devices/policy/{uuid}">client.devices.policies.<a href="./src/cloudflare/resources/devices/policies/policies.py">update</a>(uuid, \*, identifier, \*\*<a href="src/cloudflare/types/devices/policy_update_params.py">params</a>) -> <a href="./src/cloudflare/types/devices/policy_update_response.py">Optional</a></code>
- <code title="delete /accounts/{identifier}/devices/policy/{uuid}">client.devices.policies.<a href="./src/cloudflare/resources/devices/policies/policies.py">delete</a>(uuid, \*, identifier) -> <a href="./src/cloudflare/types/devices/policy_delete_response.py">Optional</a></code>
- <code title="post /accounts/{identifier}/devices/policy">client.devices.policies.<a href="./src/cloudflare/resources/devices/policies/policies.py">devices_create_device_settings_policy</a>(identifier, \*\*<a href="src/cloudflare/types/devices/policy_devices_create_device_settings_policy_params.py">params</a>) -> <a href="./src/cloudflare/types/devices/policy_devices_create_device_settings_policy_response.py">Optional</a></code>
- <code title="get /accounts/{identifier}/devices/policy">client.devices.policies.<a href="./src/cloudflare/resources/devices/policies/policies.py">devices_get_default_device_settings_policy</a>(identifier) -> <a href="./src/cloudflare/types/devices/policy_devices_get_default_device_settings_policy_response.py">Optional</a></code>
- <code title="get /accounts/{identifier}/devices/policies">client.devices.policies.<a href="./src/cloudflare/resources/devices/policies/policies.py">devices_list_device_settings_policies</a>(identifier) -> <a href="./src/cloudflare/types/devices/policy_devices_list_device_settings_policies_response.py">Optional</a></code>
- <code title="patch /accounts/{identifier}/devices/policy">client.devices.policies.<a href="./src/cloudflare/resources/devices/policies/policies.py">devices_update_default_device_settings_policy</a>(identifier, \*\*<a href="src/cloudflare/types/devices/policy_devices_update_default_device_settings_policy_params.py">params</a>) -> <a href="./src/cloudflare/types/devices/policy_devices_update_default_device_settings_policy_response.py">Optional</a></code>
- <code title="get /accounts/{identifier}/devices/policy/{uuid}">client.devices.policies.<a href="./src/cloudflare/resources/devices/policies/policies.py">get</a>(uuid, \*, identifier) -> <a href="./src/cloudflare/types/devices/policy_get_response.py">Optional</a></code>

### Excludes

Types:

```python
from cloudflare.types.devices.policies import (
    ExcludeDevicesGetSplitTunnelExcludeListResponse,
    ExcludeDevicesGetSplitTunnelExcludeListForADeviceSettingsPolicyResponse,
    ExcludeDevicesSetSplitTunnelExcludeListResponse,
    ExcludeDevicesSetSplitTunnelExcludeListForADeviceSettingsPolicyResponse,
)
```

Methods:

- <code title="get /accounts/{identifier}/devices/policy/exclude">client.devices.policies.excludes.<a href="./src/cloudflare/resources/devices/policies/excludes.py">devices_get_split_tunnel_exclude_list</a>(identifier) -> <a href="./src/cloudflare/types/devices/policies/exclude_devices_get_split_tunnel_exclude_list_response.py">Optional</a></code>
- <code title="get /accounts/{identifier}/devices/policy/{uuid}/exclude">client.devices.policies.excludes.<a href="./src/cloudflare/resources/devices/policies/excludes.py">devices_get_split_tunnel_exclude_list_for_a_device_settings_policy</a>(uuid, \*, identifier) -> <a href="./src/cloudflare/types/devices/policies/exclude_devices_get_split_tunnel_exclude_list_for_a_device_settings_policy_response.py">Optional</a></code>
- <code title="put /accounts/{identifier}/devices/policy/exclude">client.devices.policies.excludes.<a href="./src/cloudflare/resources/devices/policies/excludes.py">devices_set_split_tunnel_exclude_list</a>(identifier, \*\*<a href="src/cloudflare/types/devices/policies/exclude_devices_set_split_tunnel_exclude_list_params.py">params</a>) -> <a href="./src/cloudflare/types/devices/policies/exclude_devices_set_split_tunnel_exclude_list_response.py">Optional</a></code>
- <code title="put /accounts/{identifier}/devices/policy/{uuid}/exclude">client.devices.policies.excludes.<a href="./src/cloudflare/resources/devices/policies/excludes.py">devices_set_split_tunnel_exclude_list_for_a_device_settings_policy</a>(uuid, \*, identifier, \*\*<a href="src/cloudflare/types/devices/policies/exclude_devices_set_split_tunnel_exclude_list_for_a_device_settings_policy_params.py">params</a>) -> <a href="./src/cloudflare/types/devices/policies/exclude_devices_set_split_tunnel_exclude_list_for_a_device_settings_policy_response.py">Optional</a></code>

### FallbackDomains

Types:

```python
from cloudflare.types.devices.policies import (
    FallbackDomainDevicesGetLocalDomainFallbackListResponse,
    FallbackDomainDevicesGetLocalDomainFallbackListForADeviceSettingsPolicyResponse,
    FallbackDomainDevicesSetLocalDomainFallbackListResponse,
    FallbackDomainDevicesSetLocalDomainFallbackListForADeviceSettingsPolicyResponse,
)
```

Methods:

- <code title="get /accounts/{identifier}/devices/policy/fallback_domains">client.devices.policies.fallback_domains.<a href="./src/cloudflare/resources/devices/policies/fallback_domains.py">devices_get_local_domain_fallback_list</a>(identifier) -> <a href="./src/cloudflare/types/devices/policies/fallback_domain_devices_get_local_domain_fallback_list_response.py">Optional</a></code>
- <code title="get /accounts/{identifier}/devices/policy/{uuid}/fallback_domains">client.devices.policies.fallback_domains.<a href="./src/cloudflare/resources/devices/policies/fallback_domains.py">devices_get_local_domain_fallback_list_for_a_device_settings_policy</a>(uuid, \*, identifier) -> <a href="./src/cloudflare/types/devices/policies/fallback_domain_devices_get_local_domain_fallback_list_for_a_device_settings_policy_response.py">Optional</a></code>
- <code title="put /accounts/{identifier}/devices/policy/fallback_domains">client.devices.policies.fallback_domains.<a href="./src/cloudflare/resources/devices/policies/fallback_domains.py">devices_set_local_domain_fallback_list</a>(identifier, \*\*<a href="src/cloudflare/types/devices/policies/fallback_domain_devices_set_local_domain_fallback_list_params.py">params</a>) -> <a href="./src/cloudflare/types/devices/policies/fallback_domain_devices_set_local_domain_fallback_list_response.py">Optional</a></code>
- <code title="put /accounts/{identifier}/devices/policy/{uuid}/fallback_domains">client.devices.policies.fallback_domains.<a href="./src/cloudflare/resources/devices/policies/fallback_domains.py">devices_set_local_domain_fallback_list_for_a_device_settings_policy</a>(uuid, \*, identifier, \*\*<a href="src/cloudflare/types/devices/policies/fallback_domain_devices_set_local_domain_fallback_list_for_a_device_settings_policy_params.py">params</a>) -> <a href="./src/cloudflare/types/devices/policies/fallback_domain_devices_set_local_domain_fallback_list_for_a_device_settings_policy_response.py">Optional</a></code>

### Includes

Types:

```python
from cloudflare.types.devices.policies import (
    IncludeDevicesGetSplitTunnelIncludeListResponse,
    IncludeDevicesGetSplitTunnelIncludeListForADeviceSettingsPolicyResponse,
    IncludeDevicesSetSplitTunnelIncludeListResponse,
    IncludeDevicesSetSplitTunnelIncludeListForADeviceSettingsPolicyResponse,
)
```

Methods:

- <code title="get /accounts/{identifier}/devices/policy/include">client.devices.policies.includes.<a href="./src/cloudflare/resources/devices/policies/includes.py">devices_get_split_tunnel_include_list</a>(identifier) -> <a href="./src/cloudflare/types/devices/policies/include_devices_get_split_tunnel_include_list_response.py">Optional</a></code>
- <code title="get /accounts/{identifier}/devices/policy/{uuid}/include">client.devices.policies.includes.<a href="./src/cloudflare/resources/devices/policies/includes.py">devices_get_split_tunnel_include_list_for_a_device_settings_policy</a>(uuid, \*, identifier) -> <a href="./src/cloudflare/types/devices/policies/include_devices_get_split_tunnel_include_list_for_a_device_settings_policy_response.py">Optional</a></code>
- <code title="put /accounts/{identifier}/devices/policy/include">client.devices.policies.includes.<a href="./src/cloudflare/resources/devices/policies/includes.py">devices_set_split_tunnel_include_list</a>(identifier, \*\*<a href="src/cloudflare/types/devices/policies/include_devices_set_split_tunnel_include_list_params.py">params</a>) -> <a href="./src/cloudflare/types/devices/policies/include_devices_set_split_tunnel_include_list_response.py">Optional</a></code>
- <code title="put /accounts/{identifier}/devices/policy/{uuid}/include">client.devices.policies.includes.<a href="./src/cloudflare/resources/devices/policies/includes.py">devices_set_split_tunnel_include_list_for_a_device_settings_policy</a>(uuid, \*, identifier, \*\*<a href="src/cloudflare/types/devices/policies/include_devices_set_split_tunnel_include_list_for_a_device_settings_policy_params.py">params</a>) -> <a href="./src/cloudflare/types/devices/policies/include_devices_set_split_tunnel_include_list_for_a_device_settings_policy_response.py">Optional</a></code>

## Postures

Types:

```python
from cloudflare.types.devices import (
    PostureUpdateResponse,
    PostureDeleteResponse,
    PostureDevicePostureRulesCreateDevicePostureRuleResponse,
    PostureDevicePostureRulesListDevicePostureRulesResponse,
    PostureGetResponse,
)
```

Methods:

- <code title="put /accounts/{identifier}/devices/posture/{uuid}">client.devices.postures.<a href="./src/cloudflare/resources/devices/postures/postures.py">update</a>(uuid, \*, identifier, \*\*<a href="src/cloudflare/types/devices/posture_update_params.py">params</a>) -> <a href="./src/cloudflare/types/devices/posture_update_response.py">Optional</a></code>
- <code title="delete /accounts/{identifier}/devices/posture/{uuid}">client.devices.postures.<a href="./src/cloudflare/resources/devices/postures/postures.py">delete</a>(uuid, \*, identifier) -> <a href="./src/cloudflare/types/devices/posture_delete_response.py">Optional</a></code>
- <code title="post /accounts/{identifier}/devices/posture">client.devices.postures.<a href="./src/cloudflare/resources/devices/postures/postures.py">device_posture_rules_create_device_posture_rule</a>(identifier, \*\*<a href="src/cloudflare/types/devices/posture_device_posture_rules_create_device_posture_rule_params.py">params</a>) -> <a href="./src/cloudflare/types/devices/posture_device_posture_rules_create_device_posture_rule_response.py">Optional</a></code>
- <code title="get /accounts/{identifier}/devices/posture">client.devices.postures.<a href="./src/cloudflare/resources/devices/postures/postures.py">device_posture_rules_list_device_posture_rules</a>(identifier) -> <a href="./src/cloudflare/types/devices/posture_device_posture_rules_list_device_posture_rules_response.py">Optional</a></code>
- <code title="get /accounts/{identifier}/devices/posture/{uuid}">client.devices.postures.<a href="./src/cloudflare/resources/devices/postures/postures.py">get</a>(uuid, \*, identifier) -> <a href="./src/cloudflare/types/devices/posture_get_response.py">Optional</a></code>

### Integrations

Types:

```python
from cloudflare.types.devices.postures import (
    IntegrationUpdateResponse,
    IntegrationDeleteResponse,
    IntegrationDevicePostureIntegrationsCreateDevicePostureIntegrationResponse,
    IntegrationDevicePostureIntegrationsListDevicePostureIntegrationsResponse,
    IntegrationGetResponse,
)
```

Methods:

- <code title="patch /accounts/{identifier}/devices/posture/integration/{uuid}">client.devices.postures.integrations.<a href="./src/cloudflare/resources/devices/postures/integrations.py">update</a>(uuid, \*, identifier, \*\*<a href="src/cloudflare/types/devices/postures/integration_update_params.py">params</a>) -> <a href="./src/cloudflare/types/devices/postures/integration_update_response.py">Optional</a></code>
- <code title="delete /accounts/{identifier}/devices/posture/integration/{uuid}">client.devices.postures.integrations.<a href="./src/cloudflare/resources/devices/postures/integrations.py">delete</a>(uuid, \*, identifier) -> <a href="./src/cloudflare/types/devices/postures/integration_delete_response.py">Optional</a></code>
- <code title="post /accounts/{identifier}/devices/posture/integration">client.devices.postures.integrations.<a href="./src/cloudflare/resources/devices/postures/integrations.py">device_posture_integrations_create_device_posture_integration</a>(identifier, \*\*<a href="src/cloudflare/types/devices/postures/integration_device_posture_integrations_create_device_posture_integration_params.py">params</a>) -> <a href="./src/cloudflare/types/devices/postures/integration_device_posture_integrations_create_device_posture_integration_response.py">Optional</a></code>
- <code title="get /accounts/{identifier}/devices/posture/integration">client.devices.postures.integrations.<a href="./src/cloudflare/resources/devices/postures/integrations.py">device_posture_integrations_list_device_posture_integrations</a>(identifier) -> <a href="./src/cloudflare/types/devices/postures/integration_device_posture_integrations_list_device_posture_integrations_response.py">Optional</a></code>
- <code title="get /accounts/{identifier}/devices/posture/integration/{uuid}">client.devices.postures.integrations.<a href="./src/cloudflare/resources/devices/postures/integrations.py">get</a>(uuid, \*, identifier) -> <a href="./src/cloudflare/types/devices/postures/integration_get_response.py">Optional</a></code>

## Revokes

Types:

```python
from cloudflare.types.devices import RevokeDevicesRevokeDevicesResponse
```

Methods:

- <code title="post /accounts/{identifier}/devices/revoke">client.devices.revokes.<a href="./src/cloudflare/resources/devices/revokes.py">devices_revoke_devices</a>(identifier, \*\*<a href="src/cloudflare/types/devices/revoke_devices_revoke_devices_params.py">params</a>) -> <a href="./src/cloudflare/types/devices/revoke_devices_revoke_devices_response.py">Optional</a></code>

## Settings

Types:

```python
from cloudflare.types.devices import (
    SettingZeroTrustAccountsGetDeviceSettingsForZeroTrustAccountResponse,
    SettingZeroTrustAccountsUpdateDeviceSettingsForTheZeroTrustAccountResponse,
)
```

Methods:

- <code title="get /accounts/{identifier}/devices/settings">client.devices.settings.<a href="./src/cloudflare/resources/devices/settings.py">zero_trust_accounts_get_device_settings_for_zero_trust_account</a>(identifier) -> <a href="./src/cloudflare/types/devices/setting_zero_trust_accounts_get_device_settings_for_zero_trust_account_response.py">Optional</a></code>
- <code title="put /accounts/{identifier}/devices/settings">client.devices.settings.<a href="./src/cloudflare/resources/devices/settings.py">zero_trust_accounts_update_device_settings_for_the_zero_trust_account</a>(identifier, \*\*<a href="src/cloudflare/types/devices/setting_zero_trust_accounts_update_device_settings_for_the_zero_trust_account_params.py">params</a>) -> <a href="./src/cloudflare/types/devices/setting_zero_trust_accounts_update_device_settings_for_the_zero_trust_account_response.py">Optional</a></code>

## Unrevokes

Types:

```python
from cloudflare.types.devices import UnrevokeDevicesUnrevokeDevicesResponse
```

Methods:

- <code title="post /accounts/{identifier}/devices/unrevoke">client.devices.unrevokes.<a href="./src/cloudflare/resources/devices/unrevokes.py">devices_unrevoke_devices</a>(identifier, \*\*<a href="src/cloudflare/types/devices/unrevoke_devices_unrevoke_devices_params.py">params</a>) -> <a href="./src/cloudflare/types/devices/unrevoke_devices_unrevoke_devices_response.py">Optional</a></code>

## OverrideCodes

Types:

```python
from cloudflare.types.devices import OverrideCodeDevicesListAdminOverrideCodeForDeviceResponse
```

Methods:

- <code title="get /accounts/{identifier}/devices/{uuid}/override_codes">client.devices.override_codes.<a href="./src/cloudflare/resources/devices/override_codes.py">devices_list_admin_override_code_for_device</a>(uuid, \*, identifier) -> <a href="./src/cloudflare/types/devices/override_code_devices_list_admin_override_code_for_device_response.py">Optional</a></code>

# D1

## Databases

Types:

```python
from cloudflare.types.d1 import DatabaseCreateResponse, DatabaseListResponse
```

Methods:

- <code title="post /accounts/{account_id}/d1/database">client.d1.databases.<a href="./src/cloudflare/resources/d1/databases.py">create</a>(account_id, \*\*<a href="src/cloudflare/types/d1/database_create_params.py">params</a>) -> <a href="./src/cloudflare/types/d1/database_create_response.py">DatabaseCreateResponse</a></code>
- <code title="get /accounts/{account_id}/d1/database">client.d1.databases.<a href="./src/cloudflare/resources/d1/databases.py">list</a>(account_id, \*\*<a href="src/cloudflare/types/d1/database_list_params.py">params</a>) -> <a href="./src/cloudflare/types/d1/database_list_response.py">DatabaseListResponse</a></code>

## Database

Types:

```python
from cloudflare.types.d1 import DatabaseDeleteResponse, DatabaseGetResponse, DatabaseQueryResponse
```

Methods:

- <code title="delete /accounts/{account_identifier}/d1/database/{database_identifier}">client.d1.database.<a href="./src/cloudflare/resources/d1/database.py">delete</a>(database_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/d1/database_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_identifier}/d1/database/{database_identifier}">client.d1.database.<a href="./src/cloudflare/resources/d1/database.py">get</a>(database_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/d1/database_get_response.py">DatabaseGetResponse</a></code>
- <code title="post /accounts/{account_identifier}/d1/database/{database_identifier}/query">client.d1.database.<a href="./src/cloudflare/resources/d1/database.py">query</a>(database_identifier, \*, account_identifier, \*\*<a href="src/cloudflare/types/d1/database_query_params.py">params</a>) -> <a href="./src/cloudflare/types/d1/database_query_response.py">DatabaseQueryResponse</a></code>

# DEX

## Colos

Types:

```python
from cloudflare.types.dex import ColoListResponse
```

Methods:

- <code title="get /accounts/{account_id}/dex/colos">client.dex.colos.<a href="./src/cloudflare/resources/dex/colos.py">list</a>(account_id, \*\*<a href="src/cloudflare/types/dex/colo_list_params.py">params</a>) -> <a href="./src/cloudflare/types/dex/colo_list_response.py">Optional</a></code>

## FleetStatus

### Devices

Types:

```python
from cloudflare.types.dex.fleet_status import DeviceListResponse
```

Methods:

- <code title="get /accounts/{account_id}/dex/fleet-status/devices">client.dex.fleet_status.devices.<a href="./src/cloudflare/resources/dex/fleet_status/devices.py">list</a>(account_id, \*\*<a href="src/cloudflare/types/dex/fleet_status/device_list_params.py">params</a>) -> <a href="./src/cloudflare/types/dex/fleet_status/device_list_response.py">Optional</a></code>

### Live

Types:

```python
from cloudflare.types.dex.fleet_status import LiveListResponse
```

Methods:

- <code title="get /accounts/{account_id}/dex/fleet-status/live">client.dex.fleet_status.live.<a href="./src/cloudflare/resources/dex/fleet_status/live.py">list</a>(account_id, \*\*<a href="src/cloudflare/types/dex/fleet_status/live_list_params.py">params</a>) -> <a href="./src/cloudflare/types/dex/fleet_status/live_list_response.py">LiveListResponse</a></code>

### OverTime

Methods:

- <code title="get /accounts/{account_id}/dex/fleet-status/over-time">client.dex.fleet_status.over_time.<a href="./src/cloudflare/resources/dex/fleet_status/over_time.py">list</a>(account_id, \*\*<a href="src/cloudflare/types/dex/fleet_status/over_time_list_params.py">params</a>) -> None</code>

## HTTPTests

Types:

```python
from cloudflare.types.dex import HTTPTestGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/dex/http-tests/{test_id}">client.dex.http_tests.<a href="./src/cloudflare/resources/dex/http_tests/http_tests.py">get</a>(test_id, \*, account_id, \*\*<a href="src/cloudflare/types/dex/http_test_get_params.py">params</a>) -> <a href="./src/cloudflare/types/dex/http_test_get_response.py">HTTPTestGetResponse</a></code>

### Percentiles

Types:

```python
from cloudflare.types.dex.http_tests import PercentileListResponse
```

Methods:

- <code title="get /accounts/{account_id}/dex/http-tests/{test_id}/percentiles">client.dex.http_tests.percentiles.<a href="./src/cloudflare/resources/dex/http_tests/percentiles.py">list</a>(test_id, \*, account_id, \*\*<a href="src/cloudflare/types/dex/http_tests/percentile_list_params.py">params</a>) -> <a href="./src/cloudflare/types/dex/http_tests/percentile_list_response.py">PercentileListResponse</a></code>

## Tests

Types:

```python
from cloudflare.types.dex import TestListResponse
```

Methods:

- <code title="get /accounts/{account_id}/dex/tests">client.dex.tests.<a href="./src/cloudflare/resources/dex/tests/tests.py">list</a>(account_id, \*\*<a href="src/cloudflare/types/dex/test_list_params.py">params</a>) -> <a href="./src/cloudflare/types/dex/test_list_response.py">TestListResponse</a></code>

### UniqueDevices

Types:

```python
from cloudflare.types.dex.tests import UniqueDeviceListResponse
```

Methods:

- <code title="get /accounts/{account_id}/dex/tests/unique-devices">client.dex.tests.unique_devices.<a href="./src/cloudflare/resources/dex/tests/unique_devices.py">list</a>(account_id, \*\*<a href="src/cloudflare/types/dex/tests/unique_device_list_params.py">params</a>) -> <a href="./src/cloudflare/types/dex/tests/unique_device_list_response.py">UniqueDeviceListResponse</a></code>

## TracerouteTestResults

### NetworkPath

Types:

```python
from cloudflare.types.dex.traceroute_test_results import NetworkPathListResponse
```

Methods:

- <code title="get /accounts/{account_id}/dex/traceroute-test-results/{test_result_id}/network-path">client.dex.traceroute_test_results.network_path.<a href="./src/cloudflare/resources/dex/traceroute_test_results/network_path.py">list</a>(test_result_id, \*, account_id) -> <a href="./src/cloudflare/types/dex/traceroute_test_results/network_path_list_response.py">NetworkPathListResponse</a></code>

## TracerouteTests

Types:

```python
from cloudflare.types.dex import (
    TracerouteTestGetResponse,
    TracerouteTestNetworkPathResponse,
    TracerouteTestPercentilesResponse,
)
```

Methods:

- <code title="get /accounts/{account_id}/dex/traceroute-tests/{test_id}">client.dex.traceroute_tests.<a href="./src/cloudflare/resources/dex/traceroute_tests.py">get</a>(test_id, \*, account_id, \*\*<a href="src/cloudflare/types/dex/traceroute_test_get_params.py">params</a>) -> <a href="./src/cloudflare/types/dex/traceroute_test_get_response.py">TracerouteTestGetResponse</a></code>
- <code title="get /accounts/{account_id}/dex/traceroute-tests/{test_id}/network-path">client.dex.traceroute_tests.<a href="./src/cloudflare/resources/dex/traceroute_tests.py">network_path</a>(test_id, \*, account_id, \*\*<a href="src/cloudflare/types/dex/traceroute_test_network_path_params.py">params</a>) -> <a href="./src/cloudflare/types/dex/traceroute_test_network_path_response.py">TracerouteTestNetworkPathResponse</a></code>
- <code title="get /accounts/{account_id}/dex/traceroute-tests/{test_id}/percentiles">client.dex.traceroute_tests.<a href="./src/cloudflare/resources/dex/traceroute_tests.py">percentiles</a>(test_id, \*, account_id, \*\*<a href="src/cloudflare/types/dex/traceroute_test_percentiles_params.py">params</a>) -> <a href="./src/cloudflare/types/dex/traceroute_test_percentiles_response.py">TracerouteTestPercentilesResponse</a></code>

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

- <code title="post /accounts/{account_id}/r2/buckets">client.r2.buckets.<a href="./src/cloudflare/resources/r2/buckets.py">create</a>(account_id, \*\*<a href="src/cloudflare/types/r2/bucket_create_params.py">params</a>) -> <a href="./src/cloudflare/types/r2/bucket_create_response.py">BucketCreateResponse</a></code>
- <code title="get /accounts/{account_id}/r2/buckets">client.r2.buckets.<a href="./src/cloudflare/resources/r2/buckets.py">list</a>(account_id, \*\*<a href="src/cloudflare/types/r2/bucket_list_params.py">params</a>) -> <a href="./src/cloudflare/types/r2/bucket_list_response.py">BucketListResponse</a></code>
- <code title="delete /accounts/{account_id}/r2/buckets/{bucket_name}">client.r2.buckets.<a href="./src/cloudflare/resources/r2/buckets.py">delete</a>(bucket_name, \*, account_id) -> <a href="./src/cloudflare/types/r2/bucket_delete_response.py">object</a></code>
- <code title="get /accounts/{account_id}/r2/buckets/{bucket_name}">client.r2.buckets.<a href="./src/cloudflare/resources/r2/buckets.py">get</a>(bucket_name, \*, account_id) -> <a href="./src/cloudflare/types/r2/bucket_get_response.py">BucketGetResponse</a></code>

# Teamnet

## Routes

Types:

```python
from cloudflare.types.teamnet import RouteCreateResponse, RouteUpdateResponse, RouteDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/teamnet/routes">client.teamnet.routes.<a href="./src/cloudflare/resources/teamnet/routes.py">create</a>(account_id, \*\*<a href="src/cloudflare/types/teamnet/route_create_params.py">params</a>) -> <a href="./src/cloudflare/types/teamnet/route_create_response.py">RouteCreateResponse</a></code>
- <code title="patch /accounts/{account_id}/teamnet/routes/{route_id}">client.teamnet.routes.<a href="./src/cloudflare/resources/teamnet/routes.py">update</a>(route_id, \*, account_id, \*\*<a href="src/cloudflare/types/teamnet/route_update_params.py">params</a>) -> <a href="./src/cloudflare/types/teamnet/route_update_response.py">RouteUpdateResponse</a></code>
- <code title="delete /accounts/{account_id}/teamnet/routes/{route_id}">client.teamnet.routes.<a href="./src/cloudflare/resources/teamnet/routes.py">delete</a>(route_id, \*, account_id) -> <a href="./src/cloudflare/types/teamnet/route_delete_response.py">RouteDeleteResponse</a></code>

# WarpConnector

Types:

```python
from cloudflare.types import (
    WarpConnectorCreateResponse,
    WarpConnectorUpdateResponse,
    WarpConnectorListResponse,
    WarpConnectorDeleteResponse,
    WarpConnectorGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/warp_connector">client.warp_connector.<a href="./src/cloudflare/resources/warp_connector.py">create</a>(account_id, \*\*<a href="src/cloudflare/types/warp_connector_create_params.py">params</a>) -> <a href="./src/cloudflare/types/warp_connector_create_response.py">WarpConnectorCreateResponse</a></code>
- <code title="patch /accounts/{account_id}/warp_connector/{tunnel_id}">client.warp_connector.<a href="./src/cloudflare/resources/warp_connector.py">update</a>(tunnel_id, \*, account_id, \*\*<a href="src/cloudflare/types/warp_connector_update_params.py">params</a>) -> <a href="./src/cloudflare/types/warp_connector_update_response.py">WarpConnectorUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/warp_connector">client.warp_connector.<a href="./src/cloudflare/resources/warp_connector.py">list</a>(account_id, \*\*<a href="src/cloudflare/types/warp_connector_list_params.py">params</a>) -> <a href="./src/cloudflare/types/warp_connector_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/warp_connector/{tunnel_id}">client.warp_connector.<a href="./src/cloudflare/resources/warp_connector.py">delete</a>(tunnel_id, \*, account_id, \*\*<a href="src/cloudflare/types/warp_connector_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/warp_connector_delete_response.py">WarpConnectorDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/warp_connector/{tunnel_id}">client.warp_connector.<a href="./src/cloudflare/resources/warp_connector.py">get</a>(tunnel_id, \*, account_id) -> <a href="./src/cloudflare/types/warp_connector_get_response.py">WarpConnectorGetResponse</a></code>

# Dispatchers

## Scripts

Types:

```python
from cloudflare.types.dispatchers import ScriptUpdateResponse, ScriptGetResponse
```

Methods:

- <code title="put /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}">client.dispatchers.scripts.<a href="./src/cloudflare/resources/dispatchers/scripts.py">update</a>(script_name, \*, account_id, dispatch_namespace, \*\*<a href="src/cloudflare/types/dispatchers/script_update_params.py">params</a>) -> <a href="./src/cloudflare/types/dispatchers/script_update_response.py">ScriptUpdateResponse</a></code>
- <code title="delete /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}">client.dispatchers.scripts.<a href="./src/cloudflare/resources/dispatchers/scripts.py">delete</a>(script_name, \*, account_id, dispatch_namespace, \*\*<a href="src/cloudflare/types/dispatchers/script_delete_params.py">params</a>) -> None</code>
- <code title="get /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}">client.dispatchers.scripts.<a href="./src/cloudflare/resources/dispatchers/scripts.py">get</a>(script_name, \*, account_id, dispatch_namespace) -> <a href="./src/cloudflare/types/dispatchers/script_get_response.py">ScriptGetResponse</a></code>

# WorkersForPlatforms

## Dispatch

### Namespaces

#### Scripts

##### Content

Types:

```python
from cloudflare.types.workers_for_platforms.dispatch.namespaces.scripts import ContentUpdateResponse
```

Methods:

- <code title="put /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/content">client.workers_for_platforms.dispatch.namespaces.scripts.content.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/content.py">update</a>(script_name, \*, account_id, dispatch_namespace, \*\*<a href="src/cloudflare/types/workers_for_platforms/dispatch/namespaces/scripts/content_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers_for_platforms/dispatch/namespaces/scripts/content_update_response.py">ContentUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/content">client.workers_for_platforms.dispatch.namespaces.scripts.content.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/content.py">get</a>(script_name, \*, account_id, dispatch_namespace) -> BinaryAPIResponse</code>

##### Settings

Types:

```python
from cloudflare.types.workers_for_platforms.dispatch.namespaces.scripts import (
    SettingUpdateResponse,
    SettingGetResponse,
)
```

Methods:

- <code title="patch /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/settings">client.workers_for_platforms.dispatch.namespaces.scripts.settings.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/settings.py">update</a>(script_name, \*, account_id, dispatch_namespace, \*\*<a href="src/cloudflare/types/workers_for_platforms/dispatch/namespaces/scripts/setting_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers_for_platforms/dispatch/namespaces/scripts/setting_update_response.py">SettingUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/settings">client.workers_for_platforms.dispatch.namespaces.scripts.settings.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/settings.py">get</a>(script_name, \*, account_id, dispatch_namespace) -> <a href="./src/cloudflare/types/workers_for_platforms/dispatch/namespaces/scripts/setting_get_response.py">SettingGetResponse</a></code>

# WorkerDomains

Types:

```python
from cloudflare.types import WorkerDomainGetResponse
```

Methods:

- <code title="delete /accounts/{account_id}/workers/domains/{domain_id}">client.worker_domains.<a href="./src/cloudflare/resources/worker_domains.py">delete</a>(domain_id, \*, account_id) -> None</code>
- <code title="get /accounts/{account_id}/workers/domains/{domain_id}">client.worker_domains.<a href="./src/cloudflare/resources/worker_domains.py">get</a>(domain_id, \*, account_id) -> <a href="./src/cloudflare/types/worker_domain_get_response.py">WorkerDomainGetResponse</a></code>

# WorkerScripts

## Content

Types:

```python
from cloudflare.types.worker_scripts import ContentUpdateResponse
```

Methods:

- <code title="put /accounts/{account_id}/workers/scripts/{script_name}/content">client.worker_scripts.content.<a href="./src/cloudflare/resources/worker_scripts/content.py">update</a>(script_name, \*, account_id, \*\*<a href="src/cloudflare/types/worker_scripts/content_update_params.py">params</a>) -> <a href="./src/cloudflare/types/worker_scripts/content_update_response.py">ContentUpdateResponse</a></code>

## ContentV2

Methods:

- <code title="get /accounts/{account_id}/workers/scripts/{script_name}/content/v2">client.worker_scripts.content_v2.<a href="./src/cloudflare/resources/worker_scripts/content_v2.py">get</a>(script_name, \*, account_id) -> BinaryAPIResponse</code>

## Settings

Types:

```python
from cloudflare.types.worker_scripts import SettingUpdateResponse, SettingGetResponse
```

Methods:

- <code title="patch /accounts/{account_id}/workers/scripts/{script_name}/settings">client.worker_scripts.settings.<a href="./src/cloudflare/resources/worker_scripts/settings.py">update</a>(script_name, \*, account_id, \*\*<a href="src/cloudflare/types/worker_scripts/setting_update_params.py">params</a>) -> <a href="./src/cloudflare/types/worker_scripts/setting_update_response.py">SettingUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/workers/scripts/{script_name}/settings">client.worker_scripts.settings.<a href="./src/cloudflare/resources/worker_scripts/settings.py">get</a>(script_name, \*, account_id) -> <a href="./src/cloudflare/types/worker_scripts/setting_get_response.py">SettingGetResponse</a></code>

# Zerotrust

## ConnectivitySettings

Types:

```python
from cloudflare.types.zerotrust import (
    ConnectivitySettingUpdateResponse,
    ConnectivitySettingGetResponse,
)
```

Methods:

- <code title="patch /accounts/{account_id}/zerotrust/connectivity_settings">client.zerotrust.connectivity_settings.<a href="./src/cloudflare/resources/zerotrust/connectivity_settings.py">update</a>(account_id, \*\*<a href="src/cloudflare/types/zerotrust/connectivity_setting_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zerotrust/connectivity_setting_update_response.py">ConnectivitySettingUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/zerotrust/connectivity_settings">client.zerotrust.connectivity_settings.<a href="./src/cloudflare/resources/zerotrust/connectivity_settings.py">get</a>(account_id) -> <a href="./src/cloudflare/types/zerotrust/connectivity_setting_get_response.py">ConnectivitySettingGetResponse</a></code>

# Addressing

## Prefixes

### BGPPrefixes

Types:

```python
from cloudflare.types.addressing.prefixes import (
    BGPPrefixUpdateResponse,
    BGPPrefixListResponse,
    BGPPrefixGetResponse,
)
```

Methods:

- <code title="patch /accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}/bgp/prefixes/{bgp_prefix_identifier}">client.addressing.prefixes.bgp_prefixes.<a href="./src/cloudflare/resources/addressing/prefixes/bgp_prefixes.py">update</a>(bgp_prefix_identifier, \*, account_identifier, prefix_identifier, \*\*<a href="src/cloudflare/types/addressing/prefixes/bgp_prefix_update_params.py">params</a>) -> <a href="./src/cloudflare/types/addressing/prefixes/bgp_prefix_update_response.py">BGPPrefixUpdateResponse</a></code>
- <code title="get /accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}/bgp/prefixes">client.addressing.prefixes.bgp_prefixes.<a href="./src/cloudflare/resources/addressing/prefixes/bgp_prefixes.py">list</a>(prefix_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/addressing/prefixes/bgp_prefix_list_response.py">Optional</a></code>
- <code title="get /accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}/bgp/prefixes/{bgp_prefix_identifier}">client.addressing.prefixes.bgp_prefixes.<a href="./src/cloudflare/resources/addressing/prefixes/bgp_prefixes.py">get</a>(bgp_prefix_identifier, \*, account_identifier, prefix_identifier) -> <a href="./src/cloudflare/types/addressing/prefixes/bgp_prefix_get_response.py">BGPPrefixGetResponse</a></code>

### Bindings

Types:

```python
from cloudflare.types.addressing.prefixes import (
    BindingCreateResponse,
    BindingListResponse,
    BindingDeleteResponse,
    BindingGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}/bindings">client.addressing.prefixes.bindings.<a href="./src/cloudflare/resources/addressing/prefixes/bindings.py">create</a>(prefix_identifier, \*, account_identifier, \*\*<a href="src/cloudflare/types/addressing/prefixes/binding_create_params.py">params</a>) -> <a href="./src/cloudflare/types/addressing/prefixes/binding_create_response.py">BindingCreateResponse</a></code>
- <code title="get /accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}/bindings">client.addressing.prefixes.bindings.<a href="./src/cloudflare/resources/addressing/prefixes/bindings.py">list</a>(prefix_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/addressing/prefixes/binding_list_response.py">BindingListResponse</a></code>
- <code title="delete /accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}/bindings/{binding_identifier}">client.addressing.prefixes.bindings.<a href="./src/cloudflare/resources/addressing/prefixes/bindings.py">delete</a>(binding_identifier, \*, account_identifier, prefix_identifier) -> <a href="./src/cloudflare/types/addressing/prefixes/binding_delete_response.py">BindingDeleteResponse</a></code>
- <code title="get /accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}/bindings/{binding_identifier}">client.addressing.prefixes.bindings.<a href="./src/cloudflare/resources/addressing/prefixes/bindings.py">get</a>(binding_identifier, \*, account_identifier, prefix_identifier) -> <a href="./src/cloudflare/types/addressing/prefixes/binding_get_response.py">BindingGetResponse</a></code>

## Services

Types:

```python
from cloudflare.types.addressing import ServiceListResponse
```

Methods:

- <code title="get /accounts/{account_identifier}/addressing/services">client.addressing.services.<a href="./src/cloudflare/resources/addressing/services.py">list</a>(account_identifier) -> <a href="./src/cloudflare/types/addressing/service_list_response.py">ServiceListResponse</a></code>

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
- <code title="get /accounts/{account_identifier}/challenges/widgets">client.challenges.widgets.<a href="./src/cloudflare/resources/challenges/widgets.py">list</a>(account_identifier, \*\*<a href="src/cloudflare/types/challenges/widget_list_params.py">params</a>) -> <a href="./src/cloudflare/types/challenges/widget_list_response.py">Optional</a></code>
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
    ConfigGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/hyperdrive/configs">client.hyperdrive.configs.<a href="./src/cloudflare/resources/hyperdrive/configs.py">create</a>(account_id, \*\*<a href="src/cloudflare/types/hyperdrive/config_create_params.py">params</a>) -> <a href="./src/cloudflare/types/hyperdrive/config_create_response.py">Optional</a></code>
- <code title="put /accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}">client.hyperdrive.configs.<a href="./src/cloudflare/resources/hyperdrive/configs.py">update</a>(hyperdrive_id, \*, account_id, \*\*<a href="src/cloudflare/types/hyperdrive/config_update_params.py">params</a>) -> <a href="./src/cloudflare/types/hyperdrive/config_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/hyperdrive/configs">client.hyperdrive.configs.<a href="./src/cloudflare/resources/hyperdrive/configs.py">list</a>(account_id) -> <a href="./src/cloudflare/types/hyperdrive/config_list_response.py">ConfigListResponse</a></code>
- <code title="delete /accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}">client.hyperdrive.configs.<a href="./src/cloudflare/resources/hyperdrive/configs.py">delete</a>(hyperdrive_id, \*, account_id) -> <a href="./src/cloudflare/types/hyperdrive/config_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}">client.hyperdrive.configs.<a href="./src/cloudflare/resources/hyperdrive/configs.py">get</a>(hyperdrive_id, \*, account_id) -> <a href="./src/cloudflare/types/hyperdrive/config_get_response.py">Optional</a></code>

# Intel

## IndicatorFeeds

Types:

```python
from cloudflare.types.intel import (
    IndicatorFeedCreateResponse,
    IndicatorFeedListResponse,
    IndicatorFeedDataResponse,
    IndicatorFeedGetResponse,
    IndicatorFeedPermissionsAddResponse,
    IndicatorFeedPermissionsRemoveResponse,
    IndicatorFeedPermissionsViewResponse,
    IndicatorFeedSnapshotResponse,
)
```

Methods:

- <code title="post /accounts/{account_identifier}/intel/indicator-feeds">client.intel.indicator_feeds.<a href="./src/cloudflare/resources/intel/indicator_feeds.py">create</a>(account_identifier, \*\*<a href="src/cloudflare/types/intel/indicator_feed_create_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/indicator_feed_create_response.py">IndicatorFeedCreateResponse</a></code>
- <code title="get /accounts/{account_identifier}/intel/indicator-feeds">client.intel.indicator_feeds.<a href="./src/cloudflare/resources/intel/indicator_feeds.py">list</a>(account_identifier) -> <a href="./src/cloudflare/types/intel/indicator_feed_list_response.py">IndicatorFeedListResponse</a></code>
- <code title="get /accounts/{account_identifier}/intel/indicator-feeds/{feed_id}/data">client.intel.indicator_feeds.<a href="./src/cloudflare/resources/intel/indicator_feeds.py">data</a>(feed_id, \*, account_identifier) -> str</code>
- <code title="get /accounts/{account_identifier}/intel/indicator-feeds/{feed_id}">client.intel.indicator_feeds.<a href="./src/cloudflare/resources/intel/indicator_feeds.py">get</a>(feed_id, \*, account_identifier) -> <a href="./src/cloudflare/types/intel/indicator_feed_get_response.py">IndicatorFeedGetResponse</a></code>
- <code title="put /accounts/{account_identifier}/intel/indicator-feeds/permissions/add">client.intel.indicator_feeds.<a href="./src/cloudflare/resources/intel/indicator_feeds.py">permissions_add</a>(account_identifier, \*\*<a href="src/cloudflare/types/intel/indicator_feed_permissions_add_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/indicator_feed_permissions_add_response.py">IndicatorFeedPermissionsAddResponse</a></code>
- <code title="put /accounts/{account_identifier}/intel/indicator-feeds/permissions/remove">client.intel.indicator_feeds.<a href="./src/cloudflare/resources/intel/indicator_feeds.py">permissions_remove</a>(account_identifier, \*\*<a href="src/cloudflare/types/intel/indicator_feed_permissions_remove_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/indicator_feed_permissions_remove_response.py">IndicatorFeedPermissionsRemoveResponse</a></code>
- <code title="get /accounts/{account_identifier}/intel/indicator-feeds/permissions/view">client.intel.indicator_feeds.<a href="./src/cloudflare/resources/intel/indicator_feeds.py">permissions_view</a>(account_identifier) -> <a href="./src/cloudflare/types/intel/indicator_feed_permissions_view_response.py">IndicatorFeedPermissionsViewResponse</a></code>
- <code title="put /accounts/{account_identifier}/intel/indicator-feeds/{feed_id}/snapshot">client.intel.indicator_feeds.<a href="./src/cloudflare/resources/intel/indicator_feeds.py">snapshot</a>(feed_id, \*, account_identifier, \*\*<a href="src/cloudflare/types/intel/indicator_feed_snapshot_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/indicator_feed_snapshot_response.py">IndicatorFeedSnapshotResponse</a></code>

## Sinkholes

Types:

```python
from cloudflare.types.intel import SinkholeListResponse
```

Methods:

- <code title="get /accounts/{account_identifier}/intel/sinkholes">client.intel.sinkholes.<a href="./src/cloudflare/resources/intel/sinkholes.py">list</a>(account_identifier) -> <a href="./src/cloudflare/types/intel/sinkhole_list_response.py">SinkholeListResponse</a></code>

# Rum

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

- <code title="post /accounts/{account_id}/rum/site_info">client.rum.site_infos.<a href="./src/cloudflare/resources/rum/site_infos.py">create</a>(account_id, \*\*<a href="src/cloudflare/types/rum/site_info_create_params.py">params</a>) -> <a href="./src/cloudflare/types/rum/site_info_create_response.py">Optional</a></code>
- <code title="put /accounts/{account_id}/rum/site_info/{site_id}">client.rum.site_infos.<a href="./src/cloudflare/resources/rum/site_infos.py">update</a>(site_id, \*, account_id, \*\*<a href="src/cloudflare/types/rum/site_info_update_params.py">params</a>) -> <a href="./src/cloudflare/types/rum/site_info_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/rum/site_info/list">client.rum.site_infos.<a href="./src/cloudflare/resources/rum/site_infos.py">list</a>(account_id, \*\*<a href="src/cloudflare/types/rum/site_info_list_params.py">params</a>) -> <a href="./src/cloudflare/types/rum/site_info_list_response.py">Optional</a></code>
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
from cloudflare.types.radar.annotations import OutageListResponse
```

Methods:

- <code title="get /radar/annotations/outages">client.radar.annotations.outages.<a href="./src/cloudflare/resources/radar/annotations/outages/outages.py">list</a>(\*\*<a href="src/cloudflare/types/radar/annotations/outage_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/annotations/outage_list_response.py">OutageListResponse</a></code>

#### Locations

Types:

```python
from cloudflare.types.radar.annotations.outages import LocationListResponse
```

Methods:

- <code title="get /radar/annotations/outages/locations">client.radar.annotations.outages.locations.<a href="./src/cloudflare/resources/radar/annotations/outages/locations.py">list</a>(\*\*<a href="src/cloudflare/types/radar/annotations/outages/location_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/annotations/outages/location_list_response.py">LocationListResponse</a></code>

## BGP

### Leaks

#### Events

Types:

```python
from cloudflare.types.radar.bgp.leaks import EventListResponse
```

Methods:

- <code title="get /radar/bgp/leaks/events">client.radar.bgp.leaks.events.<a href="./src/cloudflare/resources/radar/bgp/leaks/events.py">list</a>(\*\*<a href="src/cloudflare/types/radar/bgp/leaks/event_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bgp/leaks/event_list_response.py">EventListResponse</a></code>

### Timeseries

Types:

```python
from cloudflare.types.radar.bgp import TimeseryListResponse
```

Methods:

- <code title="get /radar/bgp/timeseries">client.radar.bgp.timeseries.<a href="./src/cloudflare/resources/radar/bgp/timeseries.py">list</a>(\*\*<a href="src/cloudflare/types/radar/bgp/timesery_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bgp/timesery_list_response.py">TimeseryListResponse</a></code>

### Tops

#### Ases

Types:

```python
from cloudflare.types.radar.bgp.tops import AseListResponse, AsePrefixesResponse
```

Methods:

- <code title="get /radar/bgp/top/ases">client.radar.bgp.tops.ases.<a href="./src/cloudflare/resources/radar/bgp/tops/ases.py">list</a>(\*\*<a href="src/cloudflare/types/radar/bgp/tops/ase_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bgp/tops/ase_list_response.py">AseListResponse</a></code>
- <code title="get /radar/bgp/top/ases/prefixes">client.radar.bgp.tops.ases.<a href="./src/cloudflare/resources/radar/bgp/tops/ases.py">prefixes</a>(\*\*<a href="src/cloudflare/types/radar/bgp/tops/ase_prefixes_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bgp/tops/ase_prefixes_response.py">AsePrefixesResponse</a></code>

#### Prefixes

Types:

```python
from cloudflare.types.radar.bgp.tops import PrefixListResponse
```

Methods:

- <code title="get /radar/bgp/top/prefixes">client.radar.bgp.tops.prefixes.<a href="./src/cloudflare/resources/radar/bgp/tops/prefixes.py">list</a>(\*\*<a href="src/cloudflare/types/radar/bgp/tops/prefix_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bgp/tops/prefix_list_response.py">PrefixListResponse</a></code>

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
from cloudflare.types.radar.bgp import RouteMoasResponse, RoutePfx2asResponse, RouteStatsResponse
```

Methods:

- <code title="get /radar/bgp/routes/moas">client.radar.bgp.routes.<a href="./src/cloudflare/resources/radar/bgp/routes.py">moas</a>(\*\*<a href="src/cloudflare/types/radar/bgp/route_moas_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bgp/route_moas_response.py">RouteMoasResponse</a></code>
- <code title="get /radar/bgp/routes/pfx2as">client.radar.bgp.routes.<a href="./src/cloudflare/resources/radar/bgp/routes.py">pfx2as</a>(\*\*<a href="src/cloudflare/types/radar/bgp/route_pfx2as_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bgp/route_pfx2as_response.py">RoutePfx2asResponse</a></code>
- <code title="get /radar/bgp/routes/stats">client.radar.bgp.routes.<a href="./src/cloudflare/resources/radar/bgp/routes.py">stats</a>(\*\*<a href="src/cloudflare/types/radar/bgp/route_stats_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bgp/route_stats_response.py">RouteStatsResponse</a></code>

## Datasets

Types:

```python
from cloudflare.types.radar import DatasetListResponse, DatasetGetResponse
```

Methods:

- <code title="get /radar/datasets">client.radar.datasets.<a href="./src/cloudflare/resources/radar/datasets/datasets.py">list</a>(\*\*<a href="src/cloudflare/types/radar/dataset_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/dataset_list_response.py">DatasetListResponse</a></code>
- <code title="get /radar/datasets/{alias}">client.radar.datasets.<a href="./src/cloudflare/resources/radar/datasets/datasets.py">get</a>(alias, \*\*<a href="src/cloudflare/types/radar/dataset_get_params.py">params</a>) -> str</code>

### Downloads

Types:

```python
from cloudflare.types.radar.datasets import DownloadRadarPostDatasetDownloadResponse
```

Methods:

- <code title="post /radar/datasets/download">client.radar.datasets.downloads.<a href="./src/cloudflare/resources/radar/datasets/downloads.py">radar_post_dataset_download</a>(\*\*<a href="src/cloudflare/types/radar/datasets/download_radar_post_dataset_download_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/datasets/download_radar_post_dataset_download_response.py">DownloadRadarPostDatasetDownloadResponse</a></code>

## DNS

### Tops

#### Ases

Types:

```python
from cloudflare.types.radar.dns.tops import AseListResponse
```

Methods:

- <code title="get /radar/dns/top/ases">client.radar.dns.tops.ases.<a href="./src/cloudflare/resources/radar/dns/tops/ases.py">list</a>(\*\*<a href="src/cloudflare/types/radar/dns/tops/ase_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/dns/tops/ase_list_response.py">AseListResponse</a></code>

#### Locations

Types:

```python
from cloudflare.types.radar.dns.tops import LocationListResponse
```

Methods:

- <code title="get /radar/dns/top/locations">client.radar.dns.tops.locations.<a href="./src/cloudflare/resources/radar/dns/tops/locations.py">list</a>(\*\*<a href="src/cloudflare/types/radar/dns/tops/location_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/dns/tops/location_list_response.py">LocationListResponse</a></code>

## Netflows

### Timeseries

Types:

```python
from cloudflare.types.radar.netflows import TimeseryListResponse
```

Methods:

- <code title="get /radar/netflows/timeseries">client.radar.netflows.timeseries.<a href="./src/cloudflare/resources/radar/netflows/timeseries.py">list</a>(\*\*<a href="src/cloudflare/types/radar/netflows/timesery_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/netflows/timesery_list_response.py">TimeseryListResponse</a></code>

### Tops

#### Ases

Types:

```python
from cloudflare.types.radar.netflows.tops import AseListResponse
```

Methods:

- <code title="get /radar/netflows/top/ases">client.radar.netflows.tops.ases.<a href="./src/cloudflare/resources/radar/netflows/tops/ases.py">list</a>(\*\*<a href="src/cloudflare/types/radar/netflows/tops/ase_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/netflows/tops/ase_list_response.py">AseListResponse</a></code>

#### Locations

Types:

```python
from cloudflare.types.radar.netflows.tops import LocationListResponse
```

Methods:

- <code title="get /radar/netflows/top/locations">client.radar.netflows.tops.locations.<a href="./src/cloudflare/resources/radar/netflows/tops/locations.py">list</a>(\*\*<a href="src/cloudflare/types/radar/netflows/tops/location_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/netflows/tops/location_list_response.py">LocationListResponse</a></code>

## Searches

### Globals

Types:

```python
from cloudflare.types.radar.searches import GlobalListResponse
```

Methods:

- <code title="get /radar/search/global">client.radar.searches.globals.<a href="./src/cloudflare/resources/radar/searches/globals.py">list</a>(\*\*<a href="src/cloudflare/types/radar/searches/global_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/searches/global_list_response.py">GlobalListResponse</a></code>

## VerifiedBots

### Tops

#### Bots

Types:

```python
from cloudflare.types.radar.verified_bots.tops import BotListResponse
```

Methods:

- <code title="get /radar/verified_bots/top/bots">client.radar.verified_bots.tops.bots.<a href="./src/cloudflare/resources/radar/verified_bots/tops/bots.py">list</a>(\*\*<a href="src/cloudflare/types/radar/verified_bots/tops/bot_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/verified_bots/tops/bot_list_response.py">BotListResponse</a></code>

#### Categories

Types:

```python
from cloudflare.types.radar.verified_bots.tops import CategoryListResponse
```

Methods:

- <code title="get /radar/verified_bots/top/categories">client.radar.verified_bots.tops.categories.<a href="./src/cloudflare/resources/radar/verified_bots/tops/categories.py">list</a>(\*\*<a href="src/cloudflare/types/radar/verified_bots/tops/category_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/verified_bots/tops/category_list_response.py">CategoryListResponse</a></code>

## As112

### TimeseriesGroups

#### DNSSEC

Types:

```python
from cloudflare.types.radar.as112.timeseries_groups import DNSSECListResponse
```

Methods:

- <code title="get /radar/as112/timeseries_groups/dnssec">client.radar.as112.timeseries_groups.dnssec.<a href="./src/cloudflare/resources/radar/as112/timeseries_groups/dnssec.py">list</a>(\*\*<a href="src/cloudflare/types/radar/as112/timeseries_groups/dnssec_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/as112/timeseries_groups/dnssec_list_response.py">DNSSECListResponse</a></code>

#### Edns

Types:

```python
from cloudflare.types.radar.as112.timeseries_groups import EdnListResponse
```

Methods:

- <code title="get /radar/as112/timeseries_groups/edns">client.radar.as112.timeseries_groups.edns.<a href="./src/cloudflare/resources/radar/as112/timeseries_groups/edns.py">list</a>(\*\*<a href="src/cloudflare/types/radar/as112/timeseries_groups/edn_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/as112/timeseries_groups/edn_list_response.py">EdnListResponse</a></code>

#### IPVersion

Types:

```python
from cloudflare.types.radar.as112.timeseries_groups import IPVersionListResponse
```

Methods:

- <code title="get /radar/as112/timeseries_groups/ip_version">client.radar.as112.timeseries_groups.ip_version.<a href="./src/cloudflare/resources/radar/as112/timeseries_groups/ip_version.py">list</a>(\*\*<a href="src/cloudflare/types/radar/as112/timeseries_groups/ip_version_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/as112/timeseries_groups/ip_version_list_response.py">IPVersionListResponse</a></code>

## ConnectionTampering

Types:

```python
from cloudflare.types.radar import ConnectionTamperingSummaryResponse
```

Methods:

- <code title="get /radar/connection_tampering/summary">client.radar.connection_tampering.<a href="./src/cloudflare/resources/radar/connection_tampering/connection_tampering.py">summary</a>(\*\*<a href="src/cloudflare/types/radar/connection_tampering_summary_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/connection_tampering_summary_response.py">ConnectionTamperingSummaryResponse</a></code>

### TimeseriesGroups

Types:

```python
from cloudflare.types.radar.connection_tampering import TimeseriesGroupListResponse
```

Methods:

- <code title="get /radar/connection_tampering/timeseries_groups">client.radar.connection_tampering.timeseries_groups.<a href="./src/cloudflare/resources/radar/connection_tampering/timeseries_groups.py">list</a>(\*\*<a href="src/cloudflare/types/radar/connection_tampering/timeseries_group_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/connection_tampering/timeseries_group_list_response.py">TimeseriesGroupListResponse</a></code>

## Email

### Security

#### Summaries

##### Arcs

Types:

```python
from cloudflare.types.radar.email.security.summaries import ArcListResponse
```

Methods:

- <code title="get /radar/email/security/summary/arc">client.radar.email.security.summaries.arcs.<a href="./src/cloudflare/resources/radar/email/security/summaries/arcs.py">list</a>(\*\*<a href="src/cloudflare/types/radar/email/security/summaries/arc_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/summaries/arc_list_response.py">ArcListResponse</a></code>

##### DKIMs

Types:

```python
from cloudflare.types.radar.email.security.summaries import DKIMListResponse
```

Methods:

- <code title="get /radar/email/security/summary/dkim">client.radar.email.security.summaries.dkims.<a href="./src/cloudflare/resources/radar/email/security/summaries/dkims.py">list</a>(\*\*<a href="src/cloudflare/types/radar/email/security/summaries/dkim_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/summaries/dkim_list_response.py">DKIMListResponse</a></code>

##### Dmarcs

Types:

```python
from cloudflare.types.radar.email.security.summaries import DmarcListResponse
```

Methods:

- <code title="get /radar/email/security/summary/dmarc">client.radar.email.security.summaries.dmarcs.<a href="./src/cloudflare/resources/radar/email/security/summaries/dmarcs.py">list</a>(\*\*<a href="src/cloudflare/types/radar/email/security/summaries/dmarc_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/summaries/dmarc_list_response.py">DmarcListResponse</a></code>

##### Malicious

Types:

```python
from cloudflare.types.radar.email.security.summaries import MaliciousListResponse
```

Methods:

- <code title="get /radar/email/security/summary/malicious">client.radar.email.security.summaries.malicious.<a href="./src/cloudflare/resources/radar/email/security/summaries/malicious.py">list</a>(\*\*<a href="src/cloudflare/types/radar/email/security/summaries/malicious_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/summaries/malicious_list_response.py">MaliciousListResponse</a></code>

##### Spams

Types:

```python
from cloudflare.types.radar.email.security.summaries import SpamGetResponse
```

Methods:

- <code title="get /radar/email/security/summary/spam">client.radar.email.security.summaries.spams.<a href="./src/cloudflare/resources/radar/email/security/summaries/spams.py">get</a>(\*\*<a href="src/cloudflare/types/radar/email/security/summaries/spam_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/summaries/spam_get_response.py">SpamGetResponse</a></code>

##### SPFs

Types:

```python
from cloudflare.types.radar.email.security.summaries import SPFListResponse
```

Methods:

- <code title="get /radar/email/security/summary/spf">client.radar.email.security.summaries.spfs.<a href="./src/cloudflare/resources/radar/email/security/summaries/spfs.py">list</a>(\*\*<a href="src/cloudflare/types/radar/email/security/summaries/spf_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/summaries/spf_list_response.py">SPFListResponse</a></code>

##### ThreatCategories

Types:

```python
from cloudflare.types.radar.email.security.summaries import ThreatCategoryListResponse
```

Methods:

- <code title="get /radar/email/security/summary/threat_category">client.radar.email.security.summaries.threat_categories.<a href="./src/cloudflare/resources/radar/email/security/summaries/threat_categories.py">list</a>(\*\*<a href="src/cloudflare/types/radar/email/security/summaries/threat_category_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/summaries/threat_category_list_response.py">ThreatCategoryListResponse</a></code>

#### TimeseriesGroups

##### Arcs

Types:

```python
from cloudflare.types.radar.email.security.timeseries_groups import ArcListResponse
```

Methods:

- <code title="get /radar/email/security/timeseries_groups/arc">client.radar.email.security.timeseries_groups.arcs.<a href="./src/cloudflare/resources/radar/email/security/timeseries_groups/arcs.py">list</a>(\*\*<a href="src/cloudflare/types/radar/email/security/timeseries_groups/arc_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/timeseries_groups/arc_list_response.py">ArcListResponse</a></code>

##### DKIMs

Types:

```python
from cloudflare.types.radar.email.security.timeseries_groups import DKIMListResponse
```

Methods:

- <code title="get /radar/email/security/timeseries_groups/dkim">client.radar.email.security.timeseries_groups.dkims.<a href="./src/cloudflare/resources/radar/email/security/timeseries_groups/dkims.py">list</a>(\*\*<a href="src/cloudflare/types/radar/email/security/timeseries_groups/dkim_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/timeseries_groups/dkim_list_response.py">DKIMListResponse</a></code>

## Attacks

### Layer3

#### TimeseriesGroups

##### Industry

Types:

```python
from cloudflare.types.radar.attacks.layer3.timeseries_groups import IndustryListResponse
```

Methods:

- <code title="get /radar/attacks/layer3/timeseries_groups/industry">client.radar.attacks.layer3.timeseries_groups.industry.<a href="./src/cloudflare/resources/radar/attacks/layer3/timeseries_groups/industry.py">list</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/timeseries_groups/industry_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/timeseries_groups/industry_list_response.py">IndustryListResponse</a></code>

##### IPVersion

Types:

```python
from cloudflare.types.radar.attacks.layer3.timeseries_groups import IPVersionListResponse
```

Methods:

- <code title="get /radar/attacks/layer3/timeseries_groups/ip_version">client.radar.attacks.layer3.timeseries_groups.ip_version.<a href="./src/cloudflare/resources/radar/attacks/layer3/timeseries_groups/ip_version.py">list</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/timeseries_groups/ip_version_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/timeseries_groups/ip_version_list_response.py">IPVersionListResponse</a></code>

##### Protocol

Types:

```python
from cloudflare.types.radar.attacks.layer3.timeseries_groups import ProtocolListResponse
```

Methods:

- <code title="get /radar/attacks/layer3/timeseries_groups/protocol">client.radar.attacks.layer3.timeseries_groups.protocol.<a href="./src/cloudflare/resources/radar/attacks/layer3/timeseries_groups/protocol.py">list</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/timeseries_groups/protocol_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/timeseries_groups/protocol_list_response.py">ProtocolListResponse</a></code>

##### Vector

Types:

```python
from cloudflare.types.radar.attacks.layer3.timeseries_groups import VectorListResponse
```

Methods:

- <code title="get /radar/attacks/layer3/timeseries_groups/vector">client.radar.attacks.layer3.timeseries_groups.vector.<a href="./src/cloudflare/resources/radar/attacks/layer3/timeseries_groups/vector.py">list</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/timeseries_groups/vector_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/timeseries_groups/vector_list_response.py">VectorListResponse</a></code>

##### Vertical

Types:

```python
from cloudflare.types.radar.attacks.layer3.timeseries_groups import VerticalListResponse
```

Methods:

- <code title="get /radar/attacks/layer3/timeseries_groups/vertical">client.radar.attacks.layer3.timeseries_groups.vertical.<a href="./src/cloudflare/resources/radar/attacks/layer3/timeseries_groups/vertical.py">list</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/timeseries_groups/vertical_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/timeseries_groups/vertical_list_response.py">VerticalListResponse</a></code>

#### Top

##### Attacks

Types:

```python
from cloudflare.types.radar.attacks.layer3.top import AttackListResponse
```

Methods:

- <code title="get /radar/attacks/layer3/top/attacks">client.radar.attacks.layer3.top.attacks.<a href="./src/cloudflare/resources/radar/attacks/layer3/top/attacks.py">list</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/top/attack_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/top/attack_list_response.py">AttackListResponse</a></code>

##### Industry

Types:

```python
from cloudflare.types.radar.attacks.layer3.top import IndustryListResponse
```

Methods:

- <code title="get /radar/attacks/layer3/top/industry">client.radar.attacks.layer3.top.industry.<a href="./src/cloudflare/resources/radar/attacks/layer3/top/industry.py">list</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/top/industry_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/top/industry_list_response.py">IndustryListResponse</a></code>

##### Locations

###### Origin

Types:

```python
from cloudflare.types.radar.attacks.layer3.top.locations import OriginListResponse
```

Methods:

- <code title="get /radar/attacks/layer3/top/locations/origin">client.radar.attacks.layer3.top.locations.origin.<a href="./src/cloudflare/resources/radar/attacks/layer3/top/locations/origin.py">list</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/top/locations/origin_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/top/locations/origin_list_response.py">OriginListResponse</a></code>

###### Target

Types:

```python
from cloudflare.types.radar.attacks.layer3.top.locations import TargetListResponse
```

Methods:

- <code title="get /radar/attacks/layer3/top/locations/target">client.radar.attacks.layer3.top.locations.target.<a href="./src/cloudflare/resources/radar/attacks/layer3/top/locations/target.py">list</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/top/locations/target_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/top/locations/target_list_response.py">TargetListResponse</a></code>

##### Vertical

Types:

```python
from cloudflare.types.radar.attacks.layer3.top import VerticalListResponse
```

Methods:

- <code title="get /radar/attacks/layer3/top/vertical">client.radar.attacks.layer3.top.vertical.<a href="./src/cloudflare/resources/radar/attacks/layer3/top/vertical.py">list</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/top/vertical_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/top/vertical_list_response.py">VerticalListResponse</a></code>

## Emails

### Security

#### Dmarc

Types:

```python
from cloudflare.types.radar.emails.security import DmarcListResponse
```

Methods:

- <code title="get /radar/email/security/timeseries_groups/dmarc">client.radar.emails.security.dmarc.<a href="./src/cloudflare/resources/radar/emails/security/dmarc.py">list</a>(\*\*<a href="src/cloudflare/types/radar/emails/security/dmarc_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/emails/security/dmarc_list_response.py">DmarcListResponse</a></code>

#### Malicious

Types:

```python
from cloudflare.types.radar.emails.security import MaliciousListResponse
```

Methods:

- <code title="get /radar/email/security/timeseries_groups/malicious">client.radar.emails.security.malicious.<a href="./src/cloudflare/resources/radar/emails/security/malicious.py">list</a>(\*\*<a href="src/cloudflare/types/radar/emails/security/malicious_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/emails/security/malicious_list_response.py">MaliciousListResponse</a></code>

#### Spam

Types:

```python
from cloudflare.types.radar.emails.security import SpamListResponse
```

Methods:

- <code title="get /radar/email/security/timeseries_groups/spam">client.radar.emails.security.spam.<a href="./src/cloudflare/resources/radar/emails/security/spam.py">list</a>(\*\*<a href="src/cloudflare/types/radar/emails/security/spam_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/emails/security/spam_list_response.py">SpamListResponse</a></code>

#### SPF

Types:

```python
from cloudflare.types.radar.emails.security import SPFListResponse
```

Methods:

- <code title="get /radar/email/security/timeseries_groups/spf">client.radar.emails.security.spf.<a href="./src/cloudflare/resources/radar/emails/security/spf.py">list</a>(\*\*<a href="src/cloudflare/types/radar/emails/security/spf_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/emails/security/spf_list_response.py">SPFListResponse</a></code>

#### ThreatCategory

Types:

```python
from cloudflare.types.radar.emails.security import ThreatCategoryListResponse
```

Methods:

- <code title="get /radar/email/security/timeseries_groups/threat_category">client.radar.emails.security.threat_category.<a href="./src/cloudflare/resources/radar/emails/security/threat_category.py">list</a>(\*\*<a href="src/cloudflare/types/radar/emails/security/threat_category_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/emails/security/threat_category_list_response.py">ThreatCategoryListResponse</a></code>

#### Top

##### Ases

Types:

```python
from cloudflare.types.radar.emails.security.top import AseListResponse
```

Methods:

- <code title="get /radar/email/security/top/ases">client.radar.emails.security.top.ases.<a href="./src/cloudflare/resources/radar/emails/security/top/ases/ases.py">list</a>(\*\*<a href="src/cloudflare/types/radar/emails/security/top/ase_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/emails/security/top/ase_list_response.py">AseListResponse</a></code>

###### Arc

Types:

```python
from cloudflare.types.radar.emails.security.top.ases import ArcGetResponse
```

Methods:

- <code title="get /radar/email/security/top/ases/arc/{arc}">client.radar.emails.security.top.ases.arc.<a href="./src/cloudflare/resources/radar/emails/security/top/ases/arc.py">get</a>(arc, \*\*<a href="src/cloudflare/types/radar/emails/security/top/ases/arc_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/emails/security/top/ases/arc_get_response.py">ArcGetResponse</a></code>

###### DKIM

Types:

```python
from cloudflare.types.radar.emails.security.top.ases import DKIMGetResponse
```

Methods:

- <code title="get /radar/email/security/top/ases/dkim/{dkim}">client.radar.emails.security.top.ases.dkim.<a href="./src/cloudflare/resources/radar/emails/security/top/ases/dkim.py">get</a>(dkim, \*\*<a href="src/cloudflare/types/radar/emails/security/top/ases/dkim_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/emails/security/top/ases/dkim_get_response.py">DKIMGetResponse</a></code>

###### Dmarc

Types:

```python
from cloudflare.types.radar.emails.security.top.ases import DmarcGetResponse
```

Methods:

- <code title="get /radar/email/security/top/ases/dmarc/{dmarc}">client.radar.emails.security.top.ases.dmarc.<a href="./src/cloudflare/resources/radar/emails/security/top/ases/dmarc.py">get</a>(dmarc, \*\*<a href="src/cloudflare/types/radar/emails/security/top/ases/dmarc_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/emails/security/top/ases/dmarc_get_response.py">DmarcGetResponse</a></code>

## Entities

Types:

```python
from cloudflare.types.radar import EntityIPsResponse
```

Methods:

- <code title="get /radar/entities/ip">client.radar.entities.<a href="./src/cloudflare/resources/radar/entities/entities.py">ips</a>(\*\*<a href="src/cloudflare/types/radar/entity_ips_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/entity_ips_response.py">EntityIPsResponse</a></code>

### Asns

Types:

```python
from cloudflare.types.radar.entities import AsnRelResponse
```

Methods:

- <code title="get /radar/entities/asns/{asn}/rel">client.radar.entities.asns.<a href="./src/cloudflare/resources/radar/entities/asns.py">rel</a>(asn, \*\*<a href="src/cloudflare/types/radar/entities/asn_rel_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/entities/asn_rel_response.py">AsnRelResponse</a></code>

## HTTP

Types:

```python
from cloudflare.types.radar import (
    HTTPBotClassesResponse,
    HTTPBrowserFamiliesResponse,
    HTTPBrowsersResponse,
    HTTPDeviceTypesResponse,
    HTTPHTTPProtocolsResponse,
    HTTPHTTPVersionsResponse,
    HTTPIPVersionsResponse,
    HTTPOssResponse,
)
```

Methods:

- <code title="get /radar/http/timeseries_groups/bot_class">client.radar.http.<a href="./src/cloudflare/resources/radar/http/http.py">bot_classes</a>(\*\*<a href="src/cloudflare/types/radar/http_bot_classes_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http_bot_classes_response.py">HTTPBotClassesResponse</a></code>
- <code title="get /radar/http/timeseries_groups/browser_family">client.radar.http.<a href="./src/cloudflare/resources/radar/http/http.py">browser_families</a>(\*\*<a href="src/cloudflare/types/radar/http_browser_families_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http_browser_families_response.py">HTTPBrowserFamiliesResponse</a></code>
- <code title="get /radar/http/timeseries_groups/browser">client.radar.http.<a href="./src/cloudflare/resources/radar/http/http.py">browsers</a>(\*\*<a href="src/cloudflare/types/radar/http_browsers_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http_browsers_response.py">HTTPBrowsersResponse</a></code>
- <code title="get /radar/http/timeseries_groups/device_type">client.radar.http.<a href="./src/cloudflare/resources/radar/http/http.py">device_types</a>(\*\*<a href="src/cloudflare/types/radar/http_device_types_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http_device_types_response.py">HTTPDeviceTypesResponse</a></code>
- <code title="get /radar/http/timeseries_groups/http_protocol">client.radar.http.<a href="./src/cloudflare/resources/radar/http/http.py">http_protocols</a>(\*\*<a href="src/cloudflare/types/radar/http_http_protocols_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http_http_protocols_response.py">HTTPHTTPProtocolsResponse</a></code>
- <code title="get /radar/http/timeseries_groups/http_version">client.radar.http.<a href="./src/cloudflare/resources/radar/http/http.py">http_versions</a>(\*\*<a href="src/cloudflare/types/radar/http_http_versions_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http_http_versions_response.py">HTTPHTTPVersionsResponse</a></code>
- <code title="get /radar/http/timeseries_groups/ip_version">client.radar.http.<a href="./src/cloudflare/resources/radar/http/http.py">ip_versions</a>(\*\*<a href="src/cloudflare/types/radar/http_ip_versions_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http_ip_versions_response.py">HTTPIPVersionsResponse</a></code>
- <code title="get /radar/http/timeseries_groups/os">client.radar.http.<a href="./src/cloudflare/resources/radar/http/http.py">oss</a>(\*\*<a href="src/cloudflare/types/radar/http_oss_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http_oss_response.py">HTTPOssResponse</a></code>

### TLSVersion

Types:

```python
from cloudflare.types.radar.http import TLSVersionListResponse
```

Methods:

- <code title="get /radar/http/timeseries_groups/tls_version">client.radar.http.tls_version.<a href="./src/cloudflare/resources/radar/http/tls_version.py">list</a>(\*\*<a href="src/cloudflare/types/radar/http/tls_version_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/tls_version_list_response.py">TLSVersionListResponse</a></code>

## Quality

### Iqi

Types:

```python
from cloudflare.types.radar.quality import IqiGetResponse
```

Methods:

- <code title="get /radar/quality/iqi/summary">client.radar.quality.iqi.<a href="./src/cloudflare/resources/radar/quality/iqi/iqi.py">get</a>(\*\*<a href="src/cloudflare/types/radar/quality/iqi_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/quality/iqi_get_response.py">IqiGetResponse</a></code>

#### TimeseriesGroups

Types:

```python
from cloudflare.types.radar.quality.iqi import TimeseriesGroupListResponse
```

Methods:

- <code title="get /radar/quality/iqi/timeseries_groups">client.radar.quality.iqi.timeseries_groups.<a href="./src/cloudflare/resources/radar/quality/iqi/timeseries_groups.py">list</a>(\*\*<a href="src/cloudflare/types/radar/quality/iqi/timeseries_group_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/quality/iqi/timeseries_group_list_response.py">TimeseriesGroupListResponse</a></code>

### Speed

#### Histogram

Types:

```python
from cloudflare.types.radar.quality.speed import HistogramGetResponse
```

Methods:

- <code title="get /radar/quality/speed/histogram">client.radar.quality.speed.histogram.<a href="./src/cloudflare/resources/radar/quality/speed/histogram.py">get</a>(\*\*<a href="src/cloudflare/types/radar/quality/speed/histogram_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/quality/speed/histogram_get_response.py">HistogramGetResponse</a></code>

#### Summary

Types:

```python
from cloudflare.types.radar.quality.speed import SummaryGetResponse
```

Methods:

- <code title="get /radar/quality/speed/summary">client.radar.quality.speed.summary.<a href="./src/cloudflare/resources/radar/quality/speed/summary.py">get</a>(\*\*<a href="src/cloudflare/types/radar/quality/speed/summary_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/quality/speed/summary_get_response.py">SummaryGetResponse</a></code>

#### Top

##### Ases

Types:

```python
from cloudflare.types.radar.quality.speed.top import AseListResponse
```

Methods:

- <code title="get /radar/quality/speed/top/ases">client.radar.quality.speed.top.ases.<a href="./src/cloudflare/resources/radar/quality/speed/top/ases.py">list</a>(\*\*<a href="src/cloudflare/types/radar/quality/speed/top/ase_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/quality/speed/top/ase_list_response.py">AseListResponse</a></code>

##### Locations

Types:

```python
from cloudflare.types.radar.quality.speed.top import LocationListResponse
```

Methods:

- <code title="get /radar/quality/speed/top/locations">client.radar.quality.speed.top.locations.<a href="./src/cloudflare/resources/radar/quality/speed/top/locations.py">list</a>(\*\*<a href="src/cloudflare/types/radar/quality/speed/top/location_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/quality/speed/top/location_list_response.py">LocationListResponse</a></code>

## Ranking

### TimeseriesGroups

Types:

```python
from cloudflare.types.radar.ranking import TimeseriesGroupListResponse
```

Methods:

- <code title="get /radar/ranking/timeseries_groups">client.radar.ranking.timeseries_groups.<a href="./src/cloudflare/resources/radar/ranking/timeseries_groups.py">list</a>(\*\*<a href="src/cloudflare/types/radar/ranking/timeseries_group_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/ranking/timeseries_group_list_response.py">TimeseriesGroupListResponse</a></code>

## TrafficAnomalies

Types:

```python
from cloudflare.types.radar import TrafficAnomalyListResponse
```

Methods:

- <code title="get /radar/traffic_anomalies">client.radar.traffic_anomalies.<a href="./src/cloudflare/resources/radar/traffic_anomalies/traffic_anomalies.py">list</a>(\*\*<a href="src/cloudflare/types/radar/traffic_anomaly_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/traffic_anomaly_list_response.py">TrafficAnomalyListResponse</a></code>

### Locations

Types:

```python
from cloudflare.types.radar.traffic_anomalies import LocationListResponse
```

Methods:

- <code title="get /radar/traffic_anomalies/locations">client.radar.traffic_anomalies.locations.<a href="./src/cloudflare/resources/radar/traffic_anomalies/locations.py">list</a>(\*\*<a href="src/cloudflare/types/radar/traffic_anomalies/location_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/traffic_anomalies/location_list_response.py">LocationListResponse</a></code>

# BotManagements

Types:

```python
from cloudflare.types import BotManagementUpdateResponse, BotManagementGetResponse
```

Methods:

- <code title="put /zones/{zone_id}/bot_management">client.bot_managements.<a href="./src/cloudflare/resources/bot_managements.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/bot_management_update_params.py">params</a>) -> <a href="./src/cloudflare/types/bot_management_update_response.py">BotManagementUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/bot_management">client.bot_managements.<a href="./src/cloudflare/resources/bot_managements.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/bot_management_get_response.py">BotManagementGetResponse</a></code>

# CacheReserves

Types:

```python
from cloudflare.types import CacheReserveCreateResponse, CacheReserveClearResponse
```

Methods:

- <code title="post /zones/{zone_id}/cache/cache_reserve_clear">client.cache_reserves.<a href="./src/cloudflare/resources/cache_reserves.py">create</a>(zone_id) -> <a href="./src/cloudflare/types/cache_reserve_create_response.py">CacheReserveCreateResponse</a></code>
- <code title="get /zones/{zone_id}/cache/cache_reserve_clear">client.cache_reserves.<a href="./src/cloudflare/resources/cache_reserves.py">clear</a>(zone_id) -> <a href="./src/cloudflare/types/cache_reserve_clear_response.py">CacheReserveClearResponse</a></code>

# OriginPostQuantumEncryptions

Types:

```python
from cloudflare.types import (
    OriginPostQuantumEncryptionUpdateResponse,
    OriginPostQuantumEncryptionGetResponse,
)
```

Methods:

- <code title="put /zones/{zone_id}/cache/origin_post_quantum_encryption">client.origin_post_quantum_encryptions.<a href="./src/cloudflare/resources/origin_post_quantum_encryptions.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/origin_post_quantum_encryption_update_params.py">params</a>) -> <a href="./src/cloudflare/types/origin_post_quantum_encryption_update_response.py">OriginPostQuantumEncryptionUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/cache/origin_post_quantum_encryption">client.origin_post_quantum_encryptions.<a href="./src/cloudflare/resources/origin_post_quantum_encryptions.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/origin_post_quantum_encryption_get_response.py">OriginPostQuantumEncryptionGetResponse</a></code>

# Cache

Types:

```python
from cloudflare.types import (
    CacheRegionalTieredCachesResponse,
    CacheUpdateRegionalTieredCacheResponse,
)
```

Methods:

- <code title="get /zones/{zone_id}/cache/regional_tiered_cache">client.cache.<a href="./src/cloudflare/resources/cache.py">regional_tiered_caches</a>(zone_id) -> <a href="./src/cloudflare/types/cache_regional_tiered_caches_response.py">CacheRegionalTieredCachesResponse</a></code>
- <code title="patch /zones/{zone_id}/cache/regional_tiered_cache">client.cache.<a href="./src/cloudflare/resources/cache.py">update_regional_tiered_cache</a>(zone_id, \*\*<a href="src/cloudflare/types/cache_update_regional_tiered_cache_params.py">params</a>) -> <a href="./src/cloudflare/types/cache_update_regional_tiered_cache_response.py">CacheUpdateRegionalTieredCacheResponse</a></code>

# Firewall

## WAF

### Packages

#### Groups

Types:

```python
from cloudflare.types.firewall.waf.packages import (
    GroupUpdateResponse,
    GroupListResponse,
    GroupGetResponse,
)
```

Methods:

- <code title="patch /zones/{zone_id}/firewall/waf/packages/{package_id}/groups/{group_id}">client.firewall.waf.packages.groups.<a href="./src/cloudflare/resources/firewall/waf/packages/groups.py">update</a>(group_id, \*, zone_id, package_id, \*\*<a href="src/cloudflare/types/firewall/waf/packages/group_update_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/waf/packages/group_update_response.py">GroupUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/firewall/waf/packages/{package_id}/groups">client.firewall.waf.packages.groups.<a href="./src/cloudflare/resources/firewall/waf/packages/groups.py">list</a>(package_id, \*, zone_id, \*\*<a href="src/cloudflare/types/firewall/waf/packages/group_list_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/waf/packages/group_list_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/firewall/waf/packages/{package_id}/groups/{group_id}">client.firewall.waf.packages.groups.<a href="./src/cloudflare/resources/firewall/waf/packages/groups.py">get</a>(group_id, \*, zone_id, package_id) -> <a href="./src/cloudflare/types/firewall/waf/packages/group_get_response.py">GroupGetResponse</a></code>

#### Rules

Types:

```python
from cloudflare.types.firewall.waf.packages import RuleUpdateResponse, RuleGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/firewall/waf/packages/{package_id}/rules/{rule_id}">client.firewall.waf.packages.rules.<a href="./src/cloudflare/resources/firewall/waf/packages/rules.py">update</a>(rule_id, \*, zone_id, package_id, \*\*<a href="src/cloudflare/types/firewall/waf/packages/rule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/waf/packages/rule_update_response.py">RuleUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/firewall/waf/packages/{package_id}/rules/{rule_id}">client.firewall.waf.packages.rules.<a href="./src/cloudflare/resources/firewall/waf/packages/rules.py">get</a>(rule_id, \*, zone_id, package_id) -> <a href="./src/cloudflare/types/firewall/waf/packages/rule_get_response.py">RuleGetResponse</a></code>

# Zaraz

Types:

```python
from cloudflare.types import ZarazWorkflowUpdateResponse
```

Methods:

- <code title="put /zones/{zone_id}/settings/zaraz/workflow">client.zaraz.<a href="./src/cloudflare/resources/zaraz/zaraz.py">workflow_update</a>(zone_id, \*\*<a href="src/cloudflare/types/zaraz_workflow_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zaraz_workflow_update_response.py">ZarazWorkflowUpdateResponse</a></code>

## Config

Types:

```python
from cloudflare.types.zaraz import ConfigUpdateResponse, ConfigGetResponse
```

Methods:

- <code title="put /zones/{zone_id}/settings/zaraz/config">client.zaraz.config.<a href="./src/cloudflare/resources/zaraz/config.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/zaraz/config_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zaraz/config_update_response.py">ConfigUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/settings/zaraz/config">client.zaraz.config.<a href="./src/cloudflare/resources/zaraz/config.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/zaraz/config_get_response.py">ConfigGetResponse</a></code>

## Default

Types:

```python
from cloudflare.types.zaraz import DefaultGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/settings/zaraz/default">client.zaraz.default.<a href="./src/cloudflare/resources/zaraz/default.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/zaraz/default_get_response.py">DefaultGetResponse</a></code>

## Export

Types:

```python
from cloudflare.types.zaraz import ExportGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/settings/zaraz/export">client.zaraz.export.<a href="./src/cloudflare/resources/zaraz/export.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/zaraz/export_get_response.py">ExportGetResponse</a></code>

## History

Types:

```python
from cloudflare.types.zaraz import HistoryUpdateResponse, HistoryListResponse
```

Methods:

- <code title="put /zones/{zone_id}/settings/zaraz/history">client.zaraz.history.<a href="./src/cloudflare/resources/zaraz/history/history.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/zaraz/history_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zaraz/history_update_response.py">HistoryUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/settings/zaraz/history">client.zaraz.history.<a href="./src/cloudflare/resources/zaraz/history/history.py">list</a>(zone_id, \*\*<a href="src/cloudflare/types/zaraz/history_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zaraz/history_list_response.py">HistoryListResponse</a></code>

### Configs

Types:

```python
from cloudflare.types.zaraz.history import ConfigGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/settings/zaraz/history/configs">client.zaraz.history.configs.<a href="./src/cloudflare/resources/zaraz/history/configs.py">get</a>(zone_id, \*\*<a href="src/cloudflare/types/zaraz/history/config_get_params.py">params</a>) -> <a href="./src/cloudflare/types/zaraz/history/config_get_response.py">ConfigGetResponse</a></code>

## Publish

Types:

```python
from cloudflare.types.zaraz import PublishCreateResponse
```

Methods:

- <code title="post /zones/{zone_id}/settings/zaraz/publish">client.zaraz.publish.<a href="./src/cloudflare/resources/zaraz/publish.py">create</a>(zone_id, \*\*<a href="src/cloudflare/types/zaraz/publish_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zaraz/publish_create_response.py">str</a></code>

## Workflow

Types:

```python
from cloudflare.types.zaraz import WorkflowGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/settings/zaraz/workflow">client.zaraz.workflow.<a href="./src/cloudflare/resources/zaraz/workflow.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/zaraz/workflow_get_response.py">WorkflowGetResponse</a></code>

# SpeedAPI

Types:

```python
from cloudflare.types import (
    SpeedAPIAvailabilitiesListResponse,
    SpeedAPIPagesListResponse,
    SpeedAPIScheduleDeleteResponse,
    SpeedAPIScheduleGetResponse,
    SpeedAPITestsCreateResponse,
    SpeedAPITestsDeleteResponse,
    SpeedAPITestsGetResponse,
    SpeedAPITestsListResponse,
    SpeedAPITrendsListResponse,
)
```

Methods:

- <code title="get /zones/{zone_id}/speed_api/availabilities">client.speed_api.<a href="./src/cloudflare/resources/speed_api/speed_api.py">availabilities_list</a>(zone_id) -> <a href="./src/cloudflare/types/speed_api_availabilities_list_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/speed_api/pages">client.speed_api.<a href="./src/cloudflare/resources/speed_api/speed_api.py">pages_list</a>(zone_id) -> <a href="./src/cloudflare/types/speed_api_pages_list_response.py">Optional</a></code>
- <code title="delete /zones/{zone_id}/speed_api/schedule/{url}">client.speed_api.<a href="./src/cloudflare/resources/speed_api/speed_api.py">schedule_delete</a>(url, \*, zone_id, \*\*<a href="src/cloudflare/types/speed_api_schedule_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/speed_api_schedule_delete_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/speed_api/schedule/{url}">client.speed_api.<a href="./src/cloudflare/resources/speed_api/speed_api.py">schedule_get</a>(url, \*, zone_id, \*\*<a href="src/cloudflare/types/speed_api_schedule_get_params.py">params</a>) -> <a href="./src/cloudflare/types/speed_api_schedule_get_response.py">Optional</a></code>
- <code title="post /zones/{zone_id}/speed_api/pages/{url}/tests">client.speed_api.<a href="./src/cloudflare/resources/speed_api/speed_api.py">tests_create</a>(url, \*, zone_id, \*\*<a href="src/cloudflare/types/speed_api_tests_create_params.py">params</a>) -> <a href="./src/cloudflare/types/speed_api_tests_create_response.py">Optional</a></code>
- <code title="delete /zones/{zone_id}/speed_api/pages/{url}/tests">client.speed_api.<a href="./src/cloudflare/resources/speed_api/speed_api.py">tests_delete</a>(url, \*, zone_id, \*\*<a href="src/cloudflare/types/speed_api_tests_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/speed_api_tests_delete_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/speed_api/pages/{url}/tests/{test_id}">client.speed_api.<a href="./src/cloudflare/resources/speed_api/speed_api.py">tests_get</a>(test_id, \*, zone_id, url) -> <a href="./src/cloudflare/types/speed_api_tests_get_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/speed_api/pages/{url}/tests">client.speed_api.<a href="./src/cloudflare/resources/speed_api/speed_api.py">tests_list</a>(url, \*, zone_id, \*\*<a href="src/cloudflare/types/speed_api_tests_list_params.py">params</a>) -> <a href="./src/cloudflare/types/speed_api_tests_list_response.py">SpeedAPITestsListResponse</a></code>
- <code title="get /zones/{zone_id}/speed_api/pages/{url}/trend">client.speed_api.<a href="./src/cloudflare/resources/speed_api/speed_api.py">trends_list</a>(url, \*, zone_id, \*\*<a href="src/cloudflare/types/speed_api_trends_list_params.py">params</a>) -> <a href="./src/cloudflare/types/speed_api_trends_list_response.py">Optional</a></code>

## Schedule

Types:

```python
from cloudflare.types.speed_api import ScheduleCreateResponse
```

Methods:

- <code title="post /zones/{zone_id}/speed_api/schedule/{url}">client.speed_api.schedule.<a href="./src/cloudflare/resources/speed_api/schedule.py">create</a>(url, \*, zone_id, \*\*<a href="src/cloudflare/types/speed_api/schedule_create_params.py">params</a>) -> <a href="./src/cloudflare/types/speed_api/schedule_create_response.py">Optional</a></code>

# DcvDelegation

## Uuid

Types:

```python
from cloudflare.types.dcv_delegation import UuidGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/dcv_delegation/uuid">client.dcv_delegation.uuid.<a href="./src/cloudflare/resources/dcv_delegation/uuid.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/dcv_delegation/uuid_get_response.py">UuidGetResponse</a></code>

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

# PageShield

## Connections

Types:

```python
from cloudflare.types.page_shield import ConnectionGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/page_shield/connections/{connection_id}">client.page_shield.connections.<a href="./src/cloudflare/resources/page_shield/connections.py">get</a>(connection_id, \*, zone_id) -> <a href="./src/cloudflare/types/page_shield/connection_get_response.py">ConnectionGetResponse</a></code>

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

- <code title="post /zones/{zone_id}/page_shield/policies">client.page_shield.policies.<a href="./src/cloudflare/resources/page_shield/policies.py">create</a>(zone_id, \*\*<a href="src/cloudflare/types/page_shield/policy_create_params.py">params</a>) -> <a href="./src/cloudflare/types/page_shield/policy_create_response.py">PolicyCreateResponse</a></code>
- <code title="put /zones/{zone_id}/page_shield/policies/{policy_id}">client.page_shield.policies.<a href="./src/cloudflare/resources/page_shield/policies.py">update</a>(policy_id, \*, zone_id, \*\*<a href="src/cloudflare/types/page_shield/policy_update_params.py">params</a>) -> <a href="./src/cloudflare/types/page_shield/policy_update_response.py">PolicyUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/page_shield/policies">client.page_shield.policies.<a href="./src/cloudflare/resources/page_shield/policies.py">list</a>(zone_id) -> <a href="./src/cloudflare/types/page_shield/policy_list_response.py">Optional</a></code>
- <code title="delete /zones/{zone_id}/page_shield/policies/{policy_id}">client.page_shield.policies.<a href="./src/cloudflare/resources/page_shield/policies.py">delete</a>(policy_id, \*, zone_id) -> None</code>
- <code title="get /zones/{zone_id}/page_shield/policies/{policy_id}">client.page_shield.policies.<a href="./src/cloudflare/resources/page_shield/policies.py">get</a>(policy_id, \*, zone_id) -> <a href="./src/cloudflare/types/page_shield/policy_get_response.py">PolicyGetResponse</a></code>

# FontSettings

Types:

```python
from cloudflare.types import FontSettingUpdateResponse, FontSettingGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/settings/fonts">client.font_settings.<a href="./src/cloudflare/resources/font_settings.py">update</a>(zone_id, \*\*<a href="src/cloudflare/types/font_setting_update_params.py">params</a>) -> <a href="./src/cloudflare/types/font_setting_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/fonts">client.font_settings.<a href="./src/cloudflare/resources/font_settings.py">get</a>(zone_id) -> <a href="./src/cloudflare/types/font_setting_get_response.py">Optional</a></code>

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

## SnippetRules

Types:

```python
from cloudflare.types.snippets import SnippetRuleUpdateResponse, SnippetRuleListResponse
```

Methods:

- <code title="put /zones/{zone_identifier}/snippets/snippet_rules">client.snippets.snippet_rules.<a href="./src/cloudflare/resources/snippets/snippet_rules.py">update</a>(zone_identifier, \*\*<a href="src/cloudflare/types/snippets/snippet_rule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/snippets/snippet_rule_update_response.py">SnippetRuleUpdateResponse</a></code>
- <code title="get /zones/{zone_identifier}/snippets/snippet_rules">client.snippets.snippet_rules.<a href="./src/cloudflare/resources/snippets/snippet_rules.py">list</a>(zone_identifier) -> <a href="./src/cloudflare/types/snippets/snippet_rule_list_response.py">SnippetRuleListResponse</a></code>

# DLP

## Datasets

Types:

```python
from cloudflare.types.dlp import (
    DatasetCreateResponse,
    DatasetUpdateResponse,
    DatasetListResponse,
    DatasetGetResponse,
    DatasetUploadResponse,
    DatasetUploadPrepareResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/dlp/datasets">client.dlp.datasets.<a href="./src/cloudflare/resources/dlp/datasets.py">create</a>(account_id, \*\*<a href="src/cloudflare/types/dlp/dataset_create_params.py">params</a>) -> <a href="./src/cloudflare/types/dlp/dataset_create_response.py">Optional</a></code>
- <code title="put /accounts/{account_id}/dlp/datasets/{dataset_id}">client.dlp.datasets.<a href="./src/cloudflare/resources/dlp/datasets.py">update</a>(dataset_id, \*, account_id, \*\*<a href="src/cloudflare/types/dlp/dataset_update_params.py">params</a>) -> <a href="./src/cloudflare/types/dlp/dataset_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/dlp/datasets">client.dlp.datasets.<a href="./src/cloudflare/resources/dlp/datasets.py">list</a>(account_id) -> <a href="./src/cloudflare/types/dlp/dataset_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/dlp/datasets/{dataset_id}">client.dlp.datasets.<a href="./src/cloudflare/resources/dlp/datasets.py">delete</a>(dataset_id, \*, account_id) -> None</code>
- <code title="get /accounts/{account_id}/dlp/datasets/{dataset_id}">client.dlp.datasets.<a href="./src/cloudflare/resources/dlp/datasets.py">get</a>(dataset_id, \*, account_id) -> <a href="./src/cloudflare/types/dlp/dataset_get_response.py">Optional</a></code>
- <code title="post /accounts/{account_id}/dlp/datasets/{dataset_id}/upload/{version}">client.dlp.datasets.<a href="./src/cloudflare/resources/dlp/datasets.py">upload</a>(version, \*, account_id, dataset_id) -> <a href="./src/cloudflare/types/dlp/dataset_upload_response.py">Optional</a></code>
- <code title="post /accounts/{account_id}/dlp/datasets/{dataset_id}/upload">client.dlp.datasets.<a href="./src/cloudflare/resources/dlp/datasets.py">upload_prepare</a>(dataset_id, \*, account_id) -> <a href="./src/cloudflare/types/dlp/dataset_upload_prepare_response.py">Optional</a></code>

# Gateway

## AuditSSHSettings

Types:

```python
from cloudflare.types.gateway import AuditSSHSettingUpdateResponse, AuditSSHSettingGetResponse
```

Methods:

- <code title="put /accounts/{account_id}/gateway/audit_ssh_settings">client.gateway.audit_ssh_settings.<a href="./src/cloudflare/resources/gateway/audit_ssh_settings.py">update</a>(account_id, \*\*<a href="src/cloudflare/types/gateway/audit_ssh_setting_update_params.py">params</a>) -> <a href="./src/cloudflare/types/gateway/audit_ssh_setting_update_response.py">AuditSSHSettingUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/gateway/audit_ssh_settings">client.gateway.audit_ssh_settings.<a href="./src/cloudflare/resources/gateway/audit_ssh_settings.py">get</a>(account_id) -> <a href="./src/cloudflare/types/gateway/audit_ssh_setting_get_response.py">AuditSSHSettingGetResponse</a></code>

# AccessTags

Types:

```python
from cloudflare.types import (
    AccessTagCreateResponse,
    AccessTagUpdateResponse,
    AccessTagDeleteResponse,
    AccessTagGetResponse,
)
```

Methods:

- <code title="post /accounts/{identifier}/access/tags">client.access_tags.<a href="./src/cloudflare/resources/access_tags.py">create</a>(identifier, \*\*<a href="src/cloudflare/types/access_tag_create_params.py">params</a>) -> <a href="./src/cloudflare/types/access_tag_create_response.py">AccessTagCreateResponse</a></code>
- <code title="put /accounts/{identifier}/access/tags/{name}">client.access_tags.<a href="./src/cloudflare/resources/access_tags.py">update</a>(tag_name, \*, identifier, \*\*<a href="src/cloudflare/types/access_tag_update_params.py">params</a>) -> <a href="./src/cloudflare/types/access_tag_update_response.py">AccessTagUpdateResponse</a></code>
- <code title="delete /accounts/{identifier}/access/tags/{name}">client.access_tags.<a href="./src/cloudflare/resources/access_tags.py">delete</a>(name, \*, identifier) -> <a href="./src/cloudflare/types/access_tag_delete_response.py">AccessTagDeleteResponse</a></code>
- <code title="get /accounts/{identifier}/access/tags/{name}">client.access_tags.<a href="./src/cloudflare/resources/access_tags.py">get</a>(name, \*, identifier) -> <a href="./src/cloudflare/types/access_tag_get_response.py">AccessTagGetResponse</a></code>
