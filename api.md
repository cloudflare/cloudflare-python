# Shared Types

```python
from cloudflare.types import (
    ASN,
    AuditLog,
    CertificateCA,
    CertificateRequestType,
    CloudflareTunnel,
    ErrorData,
    Identifier,
    LoadBalancerPreview,
    Member,
    PaginationInfo,
    Permission,
    PermissionGrant,
    ResponseInfo,
    Result,
    Role,
    SortDirection,
)
```

# Accounts

Types:

```python
from cloudflare.types.accounts import Account, AccountDeleteResponse
```

Methods:

- <code title="post /accounts">client.accounts.<a href="./src/cloudflare/resources/accounts/accounts.py">create</a>(\*\*<a href="src/cloudflare/types/accounts/account_create_params.py">params</a>) -> <a href="./src/cloudflare/types/accounts/account.py">Optional</a></code>
- <code title="put /accounts/{account_id}">client.accounts.<a href="./src/cloudflare/resources/accounts/accounts.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/accounts/account_update_params.py">params</a>) -> <a href="./src/cloudflare/types/accounts/account.py">Optional</a></code>
- <code title="get /accounts">client.accounts.<a href="./src/cloudflare/resources/accounts/accounts.py">list</a>(\*\*<a href="src/cloudflare/types/accounts/account_list_params.py">params</a>) -> <a href="./src/cloudflare/types/accounts/account.py">SyncV4PagePaginationArray[Account]</a></code>
- <code title="delete /accounts/{account_id}">client.accounts.<a href="./src/cloudflare/resources/accounts/accounts.py">delete</a>(\*, account_id) -> <a href="./src/cloudflare/types/accounts/account_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}">client.accounts.<a href="./src/cloudflare/resources/accounts/accounts.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/accounts/account.py">Optional</a></code>

## Members

Types:

```python
from cloudflare.types.accounts import (
    Status,
    UserWithInviteCode,
    MemberCreateResponse,
    MemberUpdateResponse,
    MemberListResponse,
    MemberDeleteResponse,
    MemberGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/members">client.accounts.members.<a href="./src/cloudflare/resources/accounts/members.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/accounts/member_create_params.py">params</a>) -> <a href="./src/cloudflare/types/accounts/member_create_response.py">Optional</a></code>
- <code title="put /accounts/{account_id}/members/{member_id}">client.accounts.members.<a href="./src/cloudflare/resources/accounts/members.py">update</a>(member_id, \*, account_id, \*\*<a href="src/cloudflare/types/accounts/member_update_params.py">params</a>) -> <a href="./src/cloudflare/types/accounts/member_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/members">client.accounts.members.<a href="./src/cloudflare/resources/accounts/members.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/accounts/member_list_params.py">params</a>) -> <a href="./src/cloudflare/types/accounts/member_list_response.py">SyncV4PagePaginationArray[MemberListResponse]</a></code>
- <code title="delete /accounts/{account_id}/members/{member_id}">client.accounts.members.<a href="./src/cloudflare/resources/accounts/members.py">delete</a>(member_id, \*, account_id) -> <a href="./src/cloudflare/types/accounts/member_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/members/{member_id}">client.accounts.members.<a href="./src/cloudflare/resources/accounts/members.py">get</a>(member_id, \*, account_id) -> <a href="./src/cloudflare/types/accounts/member_get_response.py">Optional</a></code>

## Roles

Types:

```python
from cloudflare.types.accounts import RoleGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/roles">client.accounts.roles.<a href="./src/cloudflare/resources/accounts/roles.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/shared/role.py">SyncSinglePage[Role]</a></code>
- <code title="get /accounts/{account_id}/roles/{role_id}">client.accounts.roles.<a href="./src/cloudflare/resources/accounts/roles.py">get</a>(role_id, \*, account_id) -> <a href="./src/cloudflare/types/accounts/role_get_response.py">object</a></code>

# OriginCACertificates

Types:

```python
from cloudflare.types.origin_ca_certificates import (
    OriginCACertificate,
    OriginCACertificateDeleteResponse,
)
```

Methods:

- <code title="post /certificates">client.origin_ca_certificates.<a href="./src/cloudflare/resources/origin_ca_certificates.py">create</a>(\*\*<a href="src/cloudflare/types/origin_ca_certificates/origin_ca_certificate_create_params.py">params</a>) -> <a href="./src/cloudflare/types/origin_ca_certificates/origin_ca_certificate.py">Optional</a></code>
- <code title="get /certificates">client.origin_ca_certificates.<a href="./src/cloudflare/resources/origin_ca_certificates.py">list</a>(\*\*<a href="src/cloudflare/types/origin_ca_certificates/origin_ca_certificate_list_params.py">params</a>) -> <a href="./src/cloudflare/types/origin_ca_certificates/origin_ca_certificate.py">SyncSinglePage[OriginCACertificate]</a></code>
- <code title="delete /certificates/{certificate_id}">client.origin_ca_certificates.<a href="./src/cloudflare/resources/origin_ca_certificates.py">delete</a>(certificate_id) -> <a href="./src/cloudflare/types/origin_ca_certificates/origin_ca_certificate_delete_response.py">Optional</a></code>
- <code title="get /certificates/{certificate_id}">client.origin_ca_certificates.<a href="./src/cloudflare/resources/origin_ca_certificates.py">get</a>(certificate_id) -> <a href="./src/cloudflare/types/origin_ca_certificates/origin_ca_certificate.py">Optional</a></code>

# IPs

Types:

```python
from cloudflare.types.ips import IPs, JDCloudIPs, IPListResponse
```

Methods:

- <code title="get /ips">client.ips.<a href="./src/cloudflare/resources/ips.py">list</a>(\*\*<a href="src/cloudflare/types/ips/ip_list_params.py">params</a>) -> <a href="./src/cloudflare/types/ips/ip_list_response.py">Optional</a></code>

# Memberships

Types:

```python
from cloudflare.types.memberships import (
    Membership,
    MembershipUpdateResponse,
    MembershipDeleteResponse,
    MembershipGetResponse,
)
```

Methods:

- <code title="put /memberships/{membership_id}">client.memberships.<a href="./src/cloudflare/resources/memberships.py">update</a>(membership_id, \*\*<a href="src/cloudflare/types/memberships/membership_update_params.py">params</a>) -> <a href="./src/cloudflare/types/memberships/membership_update_response.py">Optional</a></code>
- <code title="get /memberships">client.memberships.<a href="./src/cloudflare/resources/memberships.py">list</a>(\*\*<a href="src/cloudflare/types/memberships/membership_list_params.py">params</a>) -> <a href="./src/cloudflare/types/memberships/membership.py">SyncV4PagePaginationArray[Membership]</a></code>
- <code title="delete /memberships/{membership_id}">client.memberships.<a href="./src/cloudflare/resources/memberships.py">delete</a>(membership_id) -> <a href="./src/cloudflare/types/memberships/membership_delete_response.py">Optional</a></code>
- <code title="get /memberships/{membership_id}">client.memberships.<a href="./src/cloudflare/resources/memberships.py">get</a>(membership_id) -> <a href="./src/cloudflare/types/memberships/membership_get_response.py">Optional</a></code>

# User

Types:

```python
from cloudflare.types.user import UserEditResponse, UserGetResponse
```

Methods:

- <code title="patch /user">client.user.<a href="./src/cloudflare/resources/user/user.py">edit</a>(\*\*<a href="src/cloudflare/types/user/user_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/user/user_edit_response.py">object</a></code>
- <code title="get /user">client.user.<a href="./src/cloudflare/resources/user/user.py">get</a>() -> <a href="./src/cloudflare/types/user/user_get_response.py">object</a></code>

## AuditLogs

Methods:

- <code title="get /user/audit_logs">client.user.audit_logs.<a href="./src/cloudflare/resources/user/audit_logs.py">list</a>(\*\*<a href="src/cloudflare/types/user/audit_log_list_params.py">params</a>) -> <a href="./src/cloudflare/types/shared/audit_log.py">SyncV4PagePaginationArray[AuditLog]</a></code>

## Billing

### History

Types:

```python
from cloudflare.types.user.billing import BillingHistory
```

Methods:

- <code title="get /user/billing/history">client.user.billing.history.<a href="./src/cloudflare/resources/user/billing/history.py">list</a>(\*\*<a href="src/cloudflare/types/user/billing/history_list_params.py">params</a>) -> <a href="./src/cloudflare/types/user/billing/billing_history.py">SyncV4PagePaginationArray[BillingHistory]</a></code>

### Profile

Types:

```python
from cloudflare.types.user.billing import ProfileGetResponse
```

Methods:

- <code title="get /user/billing/profile">client.user.billing.profile.<a href="./src/cloudflare/resources/user/billing/profile.py">get</a>() -> <a href="./src/cloudflare/types/user/billing/profile_get_response.py">ProfileGetResponse</a></code>

## Invites

Types:

```python
from cloudflare.types.user import Invite, InviteEditResponse, InviteGetResponse
```

Methods:

- <code title="get /user/invites">client.user.invites.<a href="./src/cloudflare/resources/user/invites.py">list</a>() -> <a href="./src/cloudflare/types/user/invite.py">SyncSinglePage[Invite]</a></code>
- <code title="patch /user/invites/{invite_id}">client.user.invites.<a href="./src/cloudflare/resources/user/invites.py">edit</a>(invite_id, \*\*<a href="src/cloudflare/types/user/invite_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/user/invite_edit_response.py">object</a></code>
- <code title="get /user/invites/{invite_id}">client.user.invites.<a href="./src/cloudflare/resources/user/invites.py">get</a>(invite_id) -> <a href="./src/cloudflare/types/user/invite_get_response.py">object</a></code>

## Organizations

Types:

```python
from cloudflare.types.user import Organization, OrganizationDeleteResponse, OrganizationGetResponse
```

Methods:

- <code title="get /user/organizations">client.user.organizations.<a href="./src/cloudflare/resources/user/organizations.py">list</a>(\*\*<a href="src/cloudflare/types/user/organization_list_params.py">params</a>) -> <a href="./src/cloudflare/types/user/organization.py">SyncV4PagePaginationArray[Organization]</a></code>
- <code title="delete /user/organizations/{organization_id}">client.user.organizations.<a href="./src/cloudflare/resources/user/organizations.py">delete</a>(organization_id) -> <a href="./src/cloudflare/types/user/organization_delete_response.py">OrganizationDeleteResponse</a></code>
- <code title="get /user/organizations/{organization_id}">client.user.organizations.<a href="./src/cloudflare/resources/user/organizations.py">get</a>(organization_id) -> <a href="./src/cloudflare/types/user/organization_get_response.py">object</a></code>

## Subscriptions

Types:

```python
from cloudflare.types.user import (
    RatePlan,
    Subscription,
    SubscriptionComponent,
    SubscriptionZone,
    SubscriptionUpdateResponse,
    SubscriptionDeleteResponse,
    SubscriptionGetResponse,
)
```

Methods:

- <code title="put /user/subscriptions/{identifier}">client.user.subscriptions.<a href="./src/cloudflare/resources/user/subscriptions.py">update</a>(identifier, \*\*<a href="src/cloudflare/types/user/subscription_update_params.py">params</a>) -> <a href="./src/cloudflare/types/user/subscription_update_response.py">SubscriptionUpdateResponse</a></code>
- <code title="delete /user/subscriptions/{identifier}">client.user.subscriptions.<a href="./src/cloudflare/resources/user/subscriptions.py">delete</a>(identifier) -> <a href="./src/cloudflare/types/user/subscription_delete_response.py">SubscriptionDeleteResponse</a></code>
- <code title="get /user/subscriptions">client.user.subscriptions.<a href="./src/cloudflare/resources/user/subscriptions.py">get</a>() -> <a href="./src/cloudflare/types/user/subscription_get_response.py">Optional</a></code>

## Tokens

Types:

```python
from cloudflare.types.user import (
    CIDRList,
    Policy,
    Token,
    TokenCreateResponse,
    TokenUpdateResponse,
    TokenListResponse,
    TokenDeleteResponse,
    TokenGetResponse,
    TokenVerifyResponse,
)
```

Methods:

- <code title="post /user/tokens">client.user.tokens.<a href="./src/cloudflare/resources/user/tokens/tokens.py">create</a>(\*\*<a href="src/cloudflare/types/user/token_create_params.py">params</a>) -> <a href="./src/cloudflare/types/user/token_create_response.py">Optional</a></code>
- <code title="put /user/tokens/{token_id}">client.user.tokens.<a href="./src/cloudflare/resources/user/tokens/tokens.py">update</a>(token_id, \*\*<a href="src/cloudflare/types/user/token_update_params.py">params</a>) -> <a href="./src/cloudflare/types/user/token_update_response.py">Optional</a></code>
- <code title="get /user/tokens">client.user.tokens.<a href="./src/cloudflare/resources/user/tokens/tokens.py">list</a>(\*\*<a href="src/cloudflare/types/user/token_list_params.py">params</a>) -> <a href="./src/cloudflare/types/user/token_list_response.py">SyncV4PagePaginationArray[TokenListResponse]</a></code>
- <code title="delete /user/tokens/{token_id}">client.user.tokens.<a href="./src/cloudflare/resources/user/tokens/tokens.py">delete</a>(token_id) -> <a href="./src/cloudflare/types/user/token_delete_response.py">Optional</a></code>
- <code title="get /user/tokens/{token_id}">client.user.tokens.<a href="./src/cloudflare/resources/user/tokens/tokens.py">get</a>(token_id) -> <a href="./src/cloudflare/types/user/token_get_response.py">Optional</a></code>
- <code title="get /user/tokens/verify">client.user.tokens.<a href="./src/cloudflare/resources/user/tokens/tokens.py">verify</a>() -> <a href="./src/cloudflare/types/user/token_verify_response.py">Optional</a></code>

### PermissionGroups

Types:

```python
from cloudflare.types.user.tokens import PermissionGroupListResponse
```

Methods:

- <code title="get /user/tokens/permission_groups">client.user.tokens.permission_groups.<a href="./src/cloudflare/resources/user/tokens/permission_groups.py">list</a>() -> <a href="./src/cloudflare/types/user/tokens/permission_group_list_response.py">SyncSinglePage[object]</a></code>

### Value

Types:

```python
from cloudflare.types.user.tokens import Value
```

Methods:

- <code title="put /user/tokens/{token_id}/value">client.user.tokens.value.<a href="./src/cloudflare/resources/user/tokens/value.py">update</a>(token_id, \*\*<a href="src/cloudflare/types/user/tokens/value_update_params.py">params</a>) -> <a href="./src/cloudflare/types/user/tokens/value.py">str</a></code>

# Zones

Types:

```python
from cloudflare.types.zones import Type, Zone, ZoneDeleteResponse
```

Methods:

- <code title="post /zones">client.zones.<a href="./src/cloudflare/resources/zones/zones.py">create</a>(\*\*<a href="src/cloudflare/types/zones/zone_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/zone.py">Optional</a></code>
- <code title="get /zones">client.zones.<a href="./src/cloudflare/resources/zones/zones.py">list</a>(\*\*<a href="src/cloudflare/types/zones/zone_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/zone.py">SyncV4PagePaginationArray[Zone]</a></code>
- <code title="delete /zones/{zone_id}">client.zones.<a href="./src/cloudflare/resources/zones/zones.py">delete</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/zone_delete_response.py">Optional</a></code>
- <code title="patch /zones/{zone_id}">client.zones.<a href="./src/cloudflare/resources/zones/zones.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/zone_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/zone.py">Optional</a></code>
- <code title="get /zones/{zone_id}">client.zones.<a href="./src/cloudflare/resources/zones/zones.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/zone.py">Optional</a></code>

## ActivationCheck

Types:

```python
from cloudflare.types.zones import ActivationCheckTriggerResponse
```

Methods:

- <code title="put /zones/{zone_id}/activation_check">client.zones.activation_check.<a href="./src/cloudflare/resources/zones/activation_check.py">trigger</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/activation_check_trigger_response.py">Optional</a></code>

## Settings

Types:

```python
from cloudflare.types.zones import (
    AdvancedDDoS,
    AlwaysOnline,
    AlwaysUseHTTPS,
    AutomaticHTTPSRewrites,
    AutomaticPlatformOptimization,
    Brotli,
    BrowserCacheTTL,
    BrowserCheck,
    CacheLevel,
    ChallengeTTL,
    Ciphers,
    DevelopmentMode,
    EarlyHints,
    EmailObfuscation,
    FontSettings,
    H2Prioritization,
    HotlinkProtection,
    HTTP2,
    HTTP3,
    ImageResizing,
    IPGeolocation,
    IPV6,
    MinTLSVersion,
    Mirage,
    NEL,
    OpportunisticEncryption,
    OpportunisticOnion,
    OrangeToOrange,
    OriginErrorPagePassThru,
    OriginMaxHTTPVersion,
    Polish,
    PrefetchPreload,
    ProxyReadTimeout,
    PseudoIPV4,
    ResponseBuffering,
    RocketLoader,
    SecurityHeaders,
    SecurityLevel,
    ServerSideExcludes,
    SortQueryStringForCache,
    SSL,
    SSLRecommender,
    TLS1_3,
    TLSClientAuth,
    TrueClientIPHeader,
    WAF,
    WebP,
    Websocket,
    ZeroRTT,
    SettingEditResponse,
    SettingGetResponse,
)
```

Methods:

- <code title="patch /zones/{zone_id}/settings/{setting_id}">client.zones.settings.<a href="./src/cloudflare/resources/zones/settings.py">edit</a>(setting_id, \*, zone_id, \*\*<a href="src/cloudflare/types/zones/setting_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/setting_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/settings/{setting_id}">client.zones.settings.<a href="./src/cloudflare/resources/zones/settings.py">get</a>(setting_id, \*, zone_id) -> <a href="./src/cloudflare/types/zones/setting_get_response.py">Optional</a></code>

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
from cloudflare.types.zones import ZoneHold
```

Methods:

- <code title="post /zones/{zone_id}/hold">client.zones.holds.<a href="./src/cloudflare/resources/zones/holds.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/hold_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/zone_hold.py">ZoneHold</a></code>
- <code title="delete /zones/{zone_id}/hold">client.zones.holds.<a href="./src/cloudflare/resources/zones/holds.py">delete</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/hold_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/zone_hold.py">Optional</a></code>
- <code title="get /zones/{zone_id}/hold">client.zones.holds.<a href="./src/cloudflare/resources/zones/holds.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/zone_hold.py">ZoneHold</a></code>

## Subscriptions

Types:

```python
from cloudflare.types.zones import (
    SubscriptionCreateResponse,
    SubscriptionUpdateResponse,
    SubscriptionGetResponse,
)
```

Methods:

- <code title="post /zones/{identifier}/subscription">client.zones.subscriptions.<a href="./src/cloudflare/resources/zones/subscriptions.py">create</a>(identifier, \*\*<a href="src/cloudflare/types/zones/subscription_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/subscription_create_response.py">SubscriptionCreateResponse</a></code>
- <code title="put /zones/{identifier}/subscription">client.zones.subscriptions.<a href="./src/cloudflare/resources/zones/subscriptions.py">update</a>(identifier, \*\*<a href="src/cloudflare/types/zones/subscription_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/subscription_update_response.py">SubscriptionUpdateResponse</a></code>
- <code title="get /zones/{identifier}/subscription">client.zones.subscriptions.<a href="./src/cloudflare/resources/zones/subscriptions.py">get</a>(identifier) -> <a href="./src/cloudflare/types/zones/subscription_get_response.py">SubscriptionGetResponse</a></code>

# LoadBalancers

Types:

```python
from cloudflare.types.load_balancers import (
    AdaptiveRouting,
    CheckRegion,
    DefaultPools,
    FilterOptions,
    Header,
    Host,
    LoadBalancer,
    LoadShedding,
    LocationStrategy,
    NotificationFilter,
    Origin,
    OriginSteering,
    RandomSteering,
    Rules,
    SessionAffinity,
    SessionAffinityAttributes,
    SteeringPolicy,
    LoadBalancerDeleteResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/load_balancers">client.load_balancers.<a href="./src/cloudflare/resources/load_balancers/load_balancers.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/load_balancers/load_balancer_create_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancers/load_balancer.py">LoadBalancer</a></code>
- <code title="put /zones/{zone_id}/load_balancers/{load_balancer_id}">client.load_balancers.<a href="./src/cloudflare/resources/load_balancers/load_balancers.py">update</a>(load_balancer_id, \*, zone_id, \*\*<a href="src/cloudflare/types/load_balancers/load_balancer_update_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancers/load_balancer.py">LoadBalancer</a></code>
- <code title="get /zones/{zone_id}/load_balancers">client.load_balancers.<a href="./src/cloudflare/resources/load_balancers/load_balancers.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/load_balancers/load_balancer.py">SyncSinglePage[LoadBalancer]</a></code>
- <code title="delete /zones/{zone_id}/load_balancers/{load_balancer_id}">client.load_balancers.<a href="./src/cloudflare/resources/load_balancers/load_balancers.py">delete</a>(load_balancer_id, \*, zone_id) -> <a href="./src/cloudflare/types/load_balancers/load_balancer_delete_response.py">LoadBalancerDeleteResponse</a></code>
- <code title="patch /zones/{zone_id}/load_balancers/{load_balancer_id}">client.load_balancers.<a href="./src/cloudflare/resources/load_balancers/load_balancers.py">edit</a>(load_balancer_id, \*, zone_id, \*\*<a href="src/cloudflare/types/load_balancers/load_balancer_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancers/load_balancer.py">LoadBalancer</a></code>
- <code title="get /zones/{zone_id}/load_balancers/{load_balancer_id}">client.load_balancers.<a href="./src/cloudflare/resources/load_balancers/load_balancers.py">get</a>(load_balancer_id, \*, zone_id) -> <a href="./src/cloudflare/types/load_balancers/load_balancer.py">LoadBalancer</a></code>

## Monitors

Types:

```python
from cloudflare.types.load_balancers import Monitor, MonitorDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/load_balancers/monitors">client.load_balancers.monitors.<a href="./src/cloudflare/resources/load_balancers/monitors/monitors.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/load_balancers/monitor_create_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancers/monitor.py">Monitor</a></code>
- <code title="put /accounts/{account_id}/load_balancers/monitors/{monitor_id}">client.load_balancers.monitors.<a href="./src/cloudflare/resources/load_balancers/monitors/monitors.py">update</a>(monitor_id, \*, account_id, \*\*<a href="src/cloudflare/types/load_balancers/monitor_update_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancers/monitor.py">Monitor</a></code>
- <code title="get /accounts/{account_id}/load_balancers/monitors">client.load_balancers.monitors.<a href="./src/cloudflare/resources/load_balancers/monitors/monitors.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/load_balancers/monitor.py">SyncSinglePage[Monitor]</a></code>
- <code title="delete /accounts/{account_id}/load_balancers/monitors/{monitor_id}">client.load_balancers.monitors.<a href="./src/cloudflare/resources/load_balancers/monitors/monitors.py">delete</a>(monitor_id, \*, account_id) -> <a href="./src/cloudflare/types/load_balancers/monitor_delete_response.py">MonitorDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/load_balancers/monitors/{monitor_id}">client.load_balancers.monitors.<a href="./src/cloudflare/resources/load_balancers/monitors/monitors.py">edit</a>(monitor_id, \*, account_id, \*\*<a href="src/cloudflare/types/load_balancers/monitor_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancers/monitor.py">Monitor</a></code>
- <code title="get /accounts/{account_id}/load_balancers/monitors/{monitor_id}">client.load_balancers.monitors.<a href="./src/cloudflare/resources/load_balancers/monitors/monitors.py">get</a>(monitor_id, \*, account_id) -> <a href="./src/cloudflare/types/load_balancers/monitor.py">Monitor</a></code>

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
from cloudflare.types.load_balancers.monitors import ReferenceGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/load_balancers/monitors/{monitor_id}/references">client.load_balancers.monitors.references.<a href="./src/cloudflare/resources/load_balancers/monitors/references.py">get</a>(monitor_id, \*, account_id) -> <a href="./src/cloudflare/types/load_balancers/monitors/reference_get_response.py">ReferenceGetResponse</a></code>

## Pools

Types:

```python
from cloudflare.types.load_balancers import Pool, PoolDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/load_balancers/pools">client.load_balancers.pools.<a href="./src/cloudflare/resources/load_balancers/pools/pools.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/load_balancers/pool_create_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancers/pool.py">Pool</a></code>
- <code title="put /accounts/{account_id}/load_balancers/pools/{pool_id}">client.load_balancers.pools.<a href="./src/cloudflare/resources/load_balancers/pools/pools.py">update</a>(pool_id, \*, account_id, \*\*<a href="src/cloudflare/types/load_balancers/pool_update_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancers/pool.py">Pool</a></code>
- <code title="get /accounts/{account_id}/load_balancers/pools">client.load_balancers.pools.<a href="./src/cloudflare/resources/load_balancers/pools/pools.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/load_balancers/pool_list_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancers/pool.py">SyncSinglePage[Pool]</a></code>
- <code title="delete /accounts/{account_id}/load_balancers/pools/{pool_id}">client.load_balancers.pools.<a href="./src/cloudflare/resources/load_balancers/pools/pools.py">delete</a>(pool_id, \*, account_id) -> <a href="./src/cloudflare/types/load_balancers/pool_delete_response.py">PoolDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/load_balancers/pools/{pool_id}">client.load_balancers.pools.<a href="./src/cloudflare/resources/load_balancers/pools/pools.py">edit</a>(pool_id, \*, account_id, \*\*<a href="src/cloudflare/types/load_balancers/pool_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancers/pool.py">Pool</a></code>
- <code title="get /accounts/{account_id}/load_balancers/pools/{pool_id}">client.load_balancers.pools.<a href="./src/cloudflare/resources/load_balancers/pools/pools.py">get</a>(pool_id, \*, account_id) -> <a href="./src/cloudflare/types/load_balancers/pool.py">Pool</a></code>

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
from cloudflare.types.load_balancers.pools import ReferenceGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/load_balancers/pools/{pool_id}/references">client.load_balancers.pools.references.<a href="./src/cloudflare/resources/load_balancers/pools/references.py">get</a>(pool_id, \*, account_id) -> <a href="./src/cloudflare/types/load_balancers/pools/reference_get_response.py">ReferenceGetResponse</a></code>

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
from cloudflare.types.load_balancers import SearchGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/load_balancers/search">client.load_balancers.searches.<a href="./src/cloudflare/resources/load_balancers/searches.py">get</a>(\*, account_id, \*\*<a href="src/cloudflare/types/load_balancers/search_get_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancers/search_get_response.py">SearchGetResponse</a></code>

# Cache

Types:

```python
from cloudflare.types.cache import CachePurgeResponse
```

Methods:

- <code title="post /zones/{zone_id}/purge_cache">client.cache.<a href="./src/cloudflare/resources/cache/cache.py">purge</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/cache/cache_purge_params.py">params</a>) -> <a href="./src/cloudflare/types/cache/cache_purge_response.py">Optional</a></code>

## CacheReserve

Types:

```python
from cloudflare.types.cache import (
    CacheReserve,
    CacheReserveClear,
    State,
    CacheReserveClearResponse,
    CacheReserveEditResponse,
    CacheReserveGetResponse,
    CacheReserveStatusResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/cache/cache_reserve_clear">client.cache.cache_reserve.<a href="./src/cloudflare/resources/cache/cache_reserve.py">clear</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/cache/cache_reserve_clear_params.py">params</a>) -> <a href="./src/cloudflare/types/cache/cache_reserve_clear_response.py">Optional</a></code>
- <code title="patch /zones/{zone_id}/cache/cache_reserve">client.cache.cache_reserve.<a href="./src/cloudflare/resources/cache/cache_reserve.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/cache/cache_reserve_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/cache/cache_reserve_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/cache/cache_reserve">client.cache.cache_reserve.<a href="./src/cloudflare/resources/cache/cache_reserve.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/cache/cache_reserve_get_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/cache/cache_reserve_clear">client.cache.cache_reserve.<a href="./src/cloudflare/resources/cache/cache_reserve.py">status</a>(\*, zone_id) -> <a href="./src/cloudflare/types/cache/cache_reserve_status_response.py">Optional</a></code>

## SmartTieredCache

Types:

```python
from cloudflare.types.cache import (
    SmartTieredCacheDeleteResponse,
    SmartTieredCacheEditResponse,
    SmartTieredCacheGetResponse,
)
```

Methods:

- <code title="delete /zones/{zone_id}/cache/tiered_cache_smart_topology_enable">client.cache.smart_tiered_cache.<a href="./src/cloudflare/resources/cache/smart_tiered_cache.py">delete</a>(\*, zone_id) -> <a href="./src/cloudflare/types/cache/smart_tiered_cache_delete_response.py">Optional</a></code>
- <code title="patch /zones/{zone_id}/cache/tiered_cache_smart_topology_enable">client.cache.smart_tiered_cache.<a href="./src/cloudflare/resources/cache/smart_tiered_cache.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/cache/smart_tiered_cache_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/cache/smart_tiered_cache_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/cache/tiered_cache_smart_topology_enable">client.cache.smart_tiered_cache.<a href="./src/cloudflare/resources/cache/smart_tiered_cache.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/cache/smart_tiered_cache_get_response.py">Optional</a></code>

## Variants

Types:

```python
from cloudflare.types.cache import (
    CacheVariant,
    CacheVariantIdentifier,
    VariantEditResponse,
    VariantGetResponse,
)
```

Methods:

- <code title="delete /zones/{zone_id}/cache/variants">client.cache.variants.<a href="./src/cloudflare/resources/cache/variants.py">delete</a>(\*, zone_id) -> <a href="./src/cloudflare/types/cache/cache_variant.py">Optional</a></code>
- <code title="patch /zones/{zone_id}/cache/variants">client.cache.variants.<a href="./src/cloudflare/resources/cache/variants.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/cache/variant_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/cache/variant_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/cache/variants">client.cache.variants.<a href="./src/cloudflare/resources/cache/variants.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/cache/variant_get_response.py">Optional</a></code>

## RegionalTieredCache

Types:

```python
from cloudflare.types.cache import (
    RegionalTieredCache,
    RegionalTieredCacheEditResponse,
    RegionalTieredCacheGetResponse,
)
```

Methods:

- <code title="patch /zones/{zone_id}/cache/regional_tiered_cache">client.cache.regional_tiered_cache.<a href="./src/cloudflare/resources/cache/regional_tiered_cache.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/cache/regional_tiered_cache_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/cache/regional_tiered_cache_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/cache/regional_tiered_cache">client.cache.regional_tiered_cache.<a href="./src/cloudflare/resources/cache/regional_tiered_cache.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/cache/regional_tiered_cache_get_response.py">Optional</a></code>

# SSL

## Analyze

Types:

```python
from cloudflare.types.ssl import AnalyzeCreateResponse
```

Methods:

- <code title="post /zones/{zone_id}/ssl/analyze">client.ssl.analyze.<a href="./src/cloudflare/resources/ssl/analyze.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/ssl/analyze_create_params.py">params</a>) -> <a href="./src/cloudflare/types/ssl/analyze_create_response.py">object</a></code>

## CertificatePacks

Types:

```python
from cloudflare.types.ssl import (
    Host,
    RequestValidity,
    Status,
    ValidationMethod,
    CertificatePackListResponse,
    CertificatePackDeleteResponse,
    CertificatePackEditResponse,
    CertificatePackGetResponse,
)
```

Methods:

- <code title="get /zones/{zone_id}/ssl/certificate_packs">client.ssl.certificate_packs.<a href="./src/cloudflare/resources/ssl/certificate_packs/certificate_packs.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/ssl/certificate_pack_list_params.py">params</a>) -> <a href="./src/cloudflare/types/ssl/certificate_pack_list_response.py">SyncSinglePage[object]</a></code>
- <code title="delete /zones/{zone_id}/ssl/certificate_packs/{certificate_pack_id}">client.ssl.certificate_packs.<a href="./src/cloudflare/resources/ssl/certificate_packs/certificate_packs.py">delete</a>(certificate_pack_id, \*, zone_id) -> <a href="./src/cloudflare/types/ssl/certificate_pack_delete_response.py">Optional</a></code>
- <code title="patch /zones/{zone_id}/ssl/certificate_packs/{certificate_pack_id}">client.ssl.certificate_packs.<a href="./src/cloudflare/resources/ssl/certificate_packs/certificate_packs.py">edit</a>(certificate_pack_id, \*, zone_id, \*\*<a href="src/cloudflare/types/ssl/certificate_pack_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/ssl/certificate_pack_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/ssl/certificate_packs/{certificate_pack_id}">client.ssl.certificate_packs.<a href="./src/cloudflare/resources/ssl/certificate_packs/certificate_packs.py">get</a>(certificate_pack_id, \*, zone_id) -> <a href="./src/cloudflare/types/ssl/certificate_pack_get_response.py">object</a></code>

### Order

Types:

```python
from cloudflare.types.ssl.certificate_packs import OrderCreateResponse
```

Methods:

- <code title="post /zones/{zone_id}/ssl/certificate_packs/order">client.ssl.certificate_packs.order.<a href="./src/cloudflare/resources/ssl/certificate_packs/order.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/ssl/certificate_packs/order_create_params.py">params</a>) -> <a href="./src/cloudflare/types/ssl/certificate_packs/order_create_response.py">Optional</a></code>

### Quota

Types:

```python
from cloudflare.types.ssl.certificate_packs import QuotaGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/ssl/certificate_packs/quota">client.ssl.certificate_packs.quota.<a href="./src/cloudflare/resources/ssl/certificate_packs/quota.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/ssl/certificate_packs/quota_get_response.py">Optional</a></code>

## Recommendations

Types:

```python
from cloudflare.types.ssl import RecommendationGetResponse
```

Methods:

- <code title="get /zones/{zone_identifier}/ssl/recommendation">client.ssl.recommendations.<a href="./src/cloudflare/resources/ssl/recommendations.py">get</a>(zone_identifier) -> <a href="./src/cloudflare/types/ssl/recommendation_get_response.py">Optional</a></code>

## Universal

### Settings

Types:

```python
from cloudflare.types.ssl.universal import UniversalSSLSettings
```

Methods:

- <code title="patch /zones/{zone_id}/ssl/universal/settings">client.ssl.universal.settings.<a href="./src/cloudflare/resources/ssl/universal/settings.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/ssl/universal/setting_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/ssl/universal/universal_ssl_settings.py">Optional</a></code>
- <code title="get /zones/{zone_id}/ssl/universal/settings">client.ssl.universal.settings.<a href="./src/cloudflare/resources/ssl/universal/settings.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/ssl/universal/universal_ssl_settings.py">Optional</a></code>

## Verification

Types:

```python
from cloudflare.types.ssl import Verification, VerificationEditResponse, VerificationGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/ssl/verification/{certificate_pack_id}">client.ssl.verification.<a href="./src/cloudflare/resources/ssl/verification.py">edit</a>(certificate_pack_id, \*, zone_id, \*\*<a href="src/cloudflare/types/ssl/verification_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/ssl/verification_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/ssl/verification">client.ssl.verification.<a href="./src/cloudflare/resources/ssl/verification.py">get</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/ssl/verification_get_params.py">params</a>) -> <a href="./src/cloudflare/types/ssl/verification_get_response.py">Optional</a></code>

# Subscriptions

Types:

```python
from cloudflare.types.subscriptions import (
    SubscriptionCreateResponse,
    SubscriptionUpdateResponse,
    SubscriptionDeleteResponse,
    SubscriptionGetResponse,
)
```

Methods:

- <code title="post /zones/{identifier}/subscription">client.subscriptions.<a href="./src/cloudflare/resources/subscriptions.py">create</a>(identifier, \*\*<a href="src/cloudflare/types/subscriptions/subscription_create_params.py">params</a>) -> <a href="./src/cloudflare/types/subscriptions/subscription_create_response.py">SubscriptionCreateResponse</a></code>
- <code title="put /accounts/{account_id}/subscriptions/{subscription_identifier}">client.subscriptions.<a href="./src/cloudflare/resources/subscriptions.py">update</a>(subscription_identifier, \*, account_id, \*\*<a href="src/cloudflare/types/subscriptions/subscription_update_params.py">params</a>) -> <a href="./src/cloudflare/types/subscriptions/subscription_update_response.py">SubscriptionUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/subscriptions">client.subscriptions.<a href="./src/cloudflare/resources/subscriptions.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/user/subscription.py">SyncSinglePage[Subscription]</a></code>
- <code title="delete /accounts/{account_id}/subscriptions/{subscription_identifier}">client.subscriptions.<a href="./src/cloudflare/resources/subscriptions.py">delete</a>(subscription_identifier, \*, account_id) -> <a href="./src/cloudflare/types/subscriptions/subscription_delete_response.py">SubscriptionDeleteResponse</a></code>
- <code title="get /zones/{identifier}/subscription">client.subscriptions.<a href="./src/cloudflare/resources/subscriptions.py">get</a>(identifier) -> <a href="./src/cloudflare/types/subscriptions/subscription_get_response.py">SubscriptionGetResponse</a></code>

# ACM

## TotalTLS

Types:

```python
from cloudflare.types.acm import CertificateAuthority, TotalTLSCreateResponse, TotalTLSGetResponse
```

Methods:

- <code title="post /zones/{zone_id}/acm/total_tls">client.acm.total_tls.<a href="./src/cloudflare/resources/acm/total_tls.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/acm/total_tls_create_params.py">params</a>) -> <a href="./src/cloudflare/types/acm/total_tls_create_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/acm/total_tls">client.acm.total_tls.<a href="./src/cloudflare/resources/acm/total_tls.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/acm/total_tls_get_response.py">Optional</a></code>

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

- <code title="patch /zones/{zone_id}/argo/tiered_caching">client.argo.tiered_caching.<a href="./src/cloudflare/resources/argo/tiered_caching.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/argo/tiered_caching_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/argo/tiered_caching_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/argo/tiered_caching">client.argo.tiered_caching.<a href="./src/cloudflare/resources/argo/tiered_caching.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/argo/tiered_caching_get_response.py">Optional</a></code>

# Plans

Types:

```python
from cloudflare.types.plans import AvailableRatePlan
```

Methods:

- <code title="get /zones/{zone_id}/available_plans">client.plans.<a href="./src/cloudflare/resources/plans.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/plans/available_rate_plan.py">SyncSinglePage[AvailableRatePlan]</a></code>
- <code title="get /zones/{zone_id}/available_plans/{plan_identifier}">client.plans.<a href="./src/cloudflare/resources/plans.py">get</a>(plan_identifier, \*, zone_id) -> <a href="./src/cloudflare/types/plans/available_rate_plan.py">AvailableRatePlan</a></code>

# RatePlans

Types:

```python
from cloudflare.types.rate_plans import RatePlan, RatePlanGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/available_rate_plans">client.rate_plans.<a href="./src/cloudflare/resources/rate_plans.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/rate_plans/rate_plan_get_response.py">Optional</a></code>

# CertificateAuthorities

## HostnameAssociations

Types:

```python
from cloudflare.types.certificate_authorities import (
    HostnameAssociation,
    TLSHostnameAssociation,
    HostnameAssociationUpdateResponse,
    HostnameAssociationGetResponse,
)
```

Methods:

- <code title="put /zones/{zone_id}/certificate_authorities/hostname_associations">client.certificate_authorities.hostname_associations.<a href="./src/cloudflare/resources/certificate_authorities/hostname_associations.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/certificate_authorities/hostname_association_update_params.py">params</a>) -> <a href="./src/cloudflare/types/certificate_authorities/hostname_association_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/certificate_authorities/hostname_associations">client.certificate_authorities.hostname_associations.<a href="./src/cloudflare/resources/certificate_authorities/hostname_associations.py">get</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/certificate_authorities/hostname_association_get_params.py">params</a>) -> <a href="./src/cloudflare/types/certificate_authorities/hostname_association_get_response.py">Optional</a></code>

# ClientCertificates

Types:

```python
from cloudflare.types.client_certificates import ClientCertificate
```

Methods:

- <code title="post /zones/{zone_id}/client_certificates">client.client_certificates.<a href="./src/cloudflare/resources/client_certificates.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/client_certificates/client_certificate_create_params.py">params</a>) -> <a href="./src/cloudflare/types/client_certificates/client_certificate.py">Optional</a></code>
- <code title="get /zones/{zone_id}/client_certificates">client.client_certificates.<a href="./src/cloudflare/resources/client_certificates.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/client_certificates/client_certificate_list_params.py">params</a>) -> <a href="./src/cloudflare/types/client_certificates/client_certificate.py">SyncV4PagePaginationArray[ClientCertificate]</a></code>
- <code title="delete /zones/{zone_id}/client_certificates/{client_certificate_id}">client.client_certificates.<a href="./src/cloudflare/resources/client_certificates.py">delete</a>(client_certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/client_certificates/client_certificate.py">Optional</a></code>
- <code title="patch /zones/{zone_id}/client_certificates/{client_certificate_id}">client.client_certificates.<a href="./src/cloudflare/resources/client_certificates.py">edit</a>(client_certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/client_certificates/client_certificate.py">Optional</a></code>
- <code title="get /zones/{zone_id}/client_certificates/{client_certificate_id}">client.client_certificates.<a href="./src/cloudflare/resources/client_certificates.py">get</a>(client_certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/client_certificates/client_certificate.py">Optional</a></code>

# CustomCertificates

Types:

```python
from cloudflare.types.custom_certificates import (
    CustomCertificate,
    GeoRestrictions,
    Status,
    CustomCertificateDeleteResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/custom_certificates">client.custom_certificates.<a href="./src/cloudflare/resources/custom_certificates/custom_certificates.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/custom_certificates/custom_certificate_create_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_certificates/custom_certificate.py">Optional</a></code>
- <code title="get /zones/{zone_id}/custom_certificates">client.custom_certificates.<a href="./src/cloudflare/resources/custom_certificates/custom_certificates.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/custom_certificates/custom_certificate_list_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_certificates/custom_certificate.py">SyncV4PagePaginationArray[CustomCertificate]</a></code>
- <code title="delete /zones/{zone_id}/custom_certificates/{custom_certificate_id}">client.custom_certificates.<a href="./src/cloudflare/resources/custom_certificates/custom_certificates.py">delete</a>(custom_certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/custom_certificates/custom_certificate_delete_response.py">Optional</a></code>
- <code title="patch /zones/{zone_id}/custom_certificates/{custom_certificate_id}">client.custom_certificates.<a href="./src/cloudflare/resources/custom_certificates/custom_certificates.py">edit</a>(custom_certificate_id, \*, zone_id, \*\*<a href="src/cloudflare/types/custom_certificates/custom_certificate_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_certificates/custom_certificate.py">Optional</a></code>
- <code title="get /zones/{zone_id}/custom_certificates/{custom_certificate_id}">client.custom_certificates.<a href="./src/cloudflare/resources/custom_certificates/custom_certificates.py">get</a>(custom_certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/custom_certificates/custom_certificate.py">Optional</a></code>

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
from cloudflare.types.custom_hostnames import (
    BundleMethod,
    CustomHostname,
    DCVMethod,
    DomainValidationType,
    CustomHostnameCreateResponse,
    CustomHostnameListResponse,
    CustomHostnameDeleteResponse,
    CustomHostnameEditResponse,
    CustomHostnameGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/custom_hostnames">client.custom_hostnames.<a href="./src/cloudflare/resources/custom_hostnames/custom_hostnames.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/custom_hostnames/custom_hostname_create_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_hostnames/custom_hostname_create_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/custom_hostnames">client.custom_hostnames.<a href="./src/cloudflare/resources/custom_hostnames/custom_hostnames.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/custom_hostnames/custom_hostname_list_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_hostnames/custom_hostname_list_response.py">SyncV4PagePaginationArray[CustomHostnameListResponse]</a></code>
- <code title="delete /zones/{zone_id}/custom_hostnames/{custom_hostname_id}">client.custom_hostnames.<a href="./src/cloudflare/resources/custom_hostnames/custom_hostnames.py">delete</a>(custom_hostname_id, \*, zone_id) -> <a href="./src/cloudflare/types/custom_hostnames/custom_hostname_delete_response.py">CustomHostnameDeleteResponse</a></code>
- <code title="patch /zones/{zone_id}/custom_hostnames/{custom_hostname_id}">client.custom_hostnames.<a href="./src/cloudflare/resources/custom_hostnames/custom_hostnames.py">edit</a>(custom_hostname_id, \*, zone_id, \*\*<a href="src/cloudflare/types/custom_hostnames/custom_hostname_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_hostnames/custom_hostname_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/custom_hostnames/{custom_hostname_id}">client.custom_hostnames.<a href="./src/cloudflare/resources/custom_hostnames/custom_hostnames.py">get</a>(custom_hostname_id, \*, zone_id) -> <a href="./src/cloudflare/types/custom_hostnames/custom_hostname_get_response.py">Optional</a></code>

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

- <code title="put /zones/{zone_id}/custom_hostnames/fallback_origin">client.custom_hostnames.fallback_origin.<a href="./src/cloudflare/resources/custom_hostnames/fallback_origin.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/custom_hostnames/fallback_origin_update_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_hostnames/fallback_origin_update_response.py">Optional</a></code>
- <code title="delete /zones/{zone_id}/custom_hostnames/fallback_origin">client.custom_hostnames.fallback_origin.<a href="./src/cloudflare/resources/custom_hostnames/fallback_origin.py">delete</a>(\*, zone_id) -> <a href="./src/cloudflare/types/custom_hostnames/fallback_origin_delete_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/custom_hostnames/fallback_origin">client.custom_hostnames.fallback_origin.<a href="./src/cloudflare/resources/custom_hostnames/fallback_origin.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/custom_hostnames/fallback_origin_get_response.py">Optional</a></code>

# CustomNameservers

Types:

```python
from cloudflare.types.custom_nameservers import (
    CustomNameserver,
    CustomNameserverDeleteResponse,
    CustomNameserverAvailabiltyResponse,
    CustomNameserverGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/custom_ns">client.custom_nameservers.<a href="./src/cloudflare/resources/custom_nameservers.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/custom_nameservers/custom_nameserver_create_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_nameservers/custom_nameserver.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/custom_ns/{custom_ns_id}">client.custom_nameservers.<a href="./src/cloudflare/resources/custom_nameservers.py">delete</a>(custom_ns_id, \*, account_id) -> <a href="./src/cloudflare/types/custom_nameservers/custom_nameserver_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/custom_ns/availability">client.custom_nameservers.<a href="./src/cloudflare/resources/custom_nameservers.py">availabilty</a>(\*, account_id) -> <a href="./src/cloudflare/types/custom_nameservers/custom_nameserver_availabilty_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/custom_ns">client.custom_nameservers.<a href="./src/cloudflare/resources/custom_nameservers.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/custom_nameservers/custom_nameserver_get_response.py">Optional</a></code>

# DNS

Types:

```python
from cloudflare.types.dns import DNSAnalyticsNominalMetric, DNSAnalyticsQuery
```

## Records

Types:

```python
from cloudflare.types.dns import (
    ARecord,
    AAAARecord,
    CAARecord,
    CERTRecord,
    CNAMERecord,
    DNSKEYRecord,
    DSRecord,
    HTTPSRecord,
    LOCRecord,
    MXRecord,
    NAPTRRecord,
    NSRecord,
    PTRRecord,
    Record,
    RecordProcessTiming,
    RecordTags,
    SMIMEARecord,
    SRVRecord,
    SSHFPRecord,
    SVCBRecord,
    TLSARecord,
    TTL,
    TXTRecord,
    URIRecord,
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

- <code title="post /zones/{zone_id}/dns_records">client.dns.records.<a href="./src/cloudflare/resources/dns/records.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/dns/record_create_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/record_create_response.py">Optional</a></code>
- <code title="put /zones/{zone_id}/dns_records/{dns_record_id}">client.dns.records.<a href="./src/cloudflare/resources/dns/records.py">update</a>(dns_record_id, \*, zone_id, \*\*<a href="src/cloudflare/types/dns/record_update_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/record_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/dns_records">client.dns.records.<a href="./src/cloudflare/resources/dns/records.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/dns/record_list_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/record_list_response.py">SyncV4PagePaginationArray[RecordListResponse]</a></code>
- <code title="delete /zones/{zone_id}/dns_records/{dns_record_id}">client.dns.records.<a href="./src/cloudflare/resources/dns/records.py">delete</a>(dns_record_id, \*, zone_id) -> <a href="./src/cloudflare/types/dns/record_delete_response.py">Optional</a></code>
- <code title="patch /zones/{zone_id}/dns_records/{dns_record_id}">client.dns.records.<a href="./src/cloudflare/resources/dns/records.py">edit</a>(dns_record_id, \*, zone_id, \*\*<a href="src/cloudflare/types/dns/record_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/record_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/dns_records/export">client.dns.records.<a href="./src/cloudflare/resources/dns/records.py">export</a>(\*, zone_id) -> str</code>
- <code title="get /zones/{zone_id}/dns_records/{dns_record_id}">client.dns.records.<a href="./src/cloudflare/resources/dns/records.py">get</a>(dns_record_id, \*, zone_id) -> <a href="./src/cloudflare/types/dns/record_get_response.py">Optional</a></code>
- <code title="post /zones/{zone_id}/dns_records/import">client.dns.records.<a href="./src/cloudflare/resources/dns/records.py">import\_</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/dns/record_import_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/record_import_response.py">Optional</a></code>
- <code title="post /zones/{zone_id}/dns_records/scan">client.dns.records.<a href="./src/cloudflare/resources/dns/records.py">scan</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/dns/record_scan_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/record_scan_response.py">Optional</a></code>

## Settings

Types:

```python
from cloudflare.types.dns import DNSSetting, Nameserver, SettingEditResponse, SettingGetResponse
```

Methods:

- <code title="patch /{account_or_zone}/{account_or_zone_id}/dns_settings">client.dns.settings.<a href="./src/cloudflare/resources/dns/settings.py">edit</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/dns/setting_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/setting_edit_response.py">Optional</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/dns_settings">client.dns.settings.<a href="./src/cloudflare/resources/dns/settings.py">get</a>(\*, account_id, zone_id) -> <a href="./src/cloudflare/types/dns/setting_get_response.py">Optional</a></code>

## Analytics

### Reports

Types:

```python
from cloudflare.types.dns.analytics import Report
```

Methods:

- <code title="get /zones/{zone_id}/dns_analytics/report">client.dns.analytics.reports.<a href="./src/cloudflare/resources/dns/analytics/reports/reports.py">get</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/dns/analytics/report_get_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/analytics/report.py">Optional</a></code>

#### Bytimes

Types:

```python
from cloudflare.types.dns.analytics.reports import ByTime
```

Methods:

- <code title="get /zones/{zone_id}/dns_analytics/report/bytime">client.dns.analytics.reports.bytimes.<a href="./src/cloudflare/resources/dns/analytics/reports/bytimes.py">get</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/dns/analytics/reports/bytime_get_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/analytics/reports/by_time.py">Optional</a></code>

## Firewall

Types:

```python
from cloudflare.types.dns import (
    AttackMitigation,
    FirewallIPs,
    UpstreamIPs,
    FirewallCreateResponse,
    FirewallListResponse,
    FirewallDeleteResponse,
    FirewallEditResponse,
    FirewallGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/dns_firewall">client.dns.firewall.<a href="./src/cloudflare/resources/dns/firewall/firewall.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/dns/firewall_create_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/firewall_create_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/dns_firewall">client.dns.firewall.<a href="./src/cloudflare/resources/dns/firewall/firewall.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/dns/firewall_list_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/firewall_list_response.py">SyncV4PagePaginationArray[FirewallListResponse]</a></code>
- <code title="delete /accounts/{account_id}/dns_firewall/{dns_firewall_id}">client.dns.firewall.<a href="./src/cloudflare/resources/dns/firewall/firewall.py">delete</a>(dns_firewall_id, \*, account_id) -> <a href="./src/cloudflare/types/dns/firewall_delete_response.py">Optional</a></code>
- <code title="patch /accounts/{account_id}/dns_firewall/{dns_firewall_id}">client.dns.firewall.<a href="./src/cloudflare/resources/dns/firewall/firewall.py">edit</a>(dns_firewall_id, \*, account_id, \*\*<a href="src/cloudflare/types/dns/firewall_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/firewall_edit_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/dns_firewall/{dns_firewall_id}">client.dns.firewall.<a href="./src/cloudflare/resources/dns/firewall/firewall.py">get</a>(dns_firewall_id, \*, account_id) -> <a href="./src/cloudflare/types/dns/firewall_get_response.py">Optional</a></code>

### Analytics

Types:

```python
from cloudflare.types.dns.firewall import Delta
```

#### Reports

Methods:

- <code title="get /accounts/{account_id}/dns_firewall/{dns_firewall_id}/dns_analytics/report">client.dns.firewall.analytics.reports.<a href="./src/cloudflare/resources/dns/firewall/analytics/reports/reports.py">get</a>(dns_firewall_id, \*, account_id, \*\*<a href="src/cloudflare/types/dns/firewall/analytics/report_get_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/analytics/report.py">Optional</a></code>

##### Bytimes

Methods:

- <code title="get /accounts/{account_id}/dns_firewall/{dns_firewall_id}/dns_analytics/report/bytime">client.dns.firewall.analytics.reports.bytimes.<a href="./src/cloudflare/resources/dns/firewall/analytics/reports/bytimes.py">get</a>(dns_firewall_id, \*, account_id, \*\*<a href="src/cloudflare/types/dns/firewall/analytics/reports/bytime_get_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/analytics/reports/by_time.py">Optional</a></code>

# DNSSEC

Types:

```python
from cloudflare.types.dnssec import DNSSEC, DNSSECDeleteResponse
```

Methods:

- <code title="delete /zones/{zone_id}/dnssec">client.dnssec.<a href="./src/cloudflare/resources/dnssec.py">delete</a>(\*, zone_id) -> <a href="./src/cloudflare/types/dnssec/dnssec_delete_response.py">Optional</a></code>
- <code title="patch /zones/{zone_id}/dnssec">client.dnssec.<a href="./src/cloudflare/resources/dnssec.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/dnssec/dnssec_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/dnssec/dnssec.py">Optional</a></code>
- <code title="get /zones/{zone_id}/dnssec">client.dnssec.<a href="./src/cloudflare/resources/dnssec.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/dnssec/dnssec.py">Optional</a></code>

# EmailSecurity

## Investigate

Types:

```python
from cloudflare.types.email_security import (
    InvestigateListResponse,
    InvestigateDetectionsResponse,
    InvestigateGetResponse,
    InvestigatePreviewResponse,
    InvestigateRawResponse,
    InvestigateTraceResponse,
)
```

Methods:

- <code title="get /accounts/{account_id}/email-security/investigate">client.email_security.investigate.<a href="./src/cloudflare/resources/email_security/investigate.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/email_security/investigate_list_params.py">params</a>) -> <a href="./src/cloudflare/types/email_security/investigate_list_response.py">SyncV4PagePaginationArray[InvestigateListResponse]</a></code>
- <code title="get /accounts/{account_id}/email-security/investigate/{postfix_id}/detections">client.email_security.investigate.<a href="./src/cloudflare/resources/email_security/investigate.py">detections</a>(postfix_id, \*, account_id) -> <a href="./src/cloudflare/types/email_security/investigate_detections_response.py">InvestigateDetectionsResponse</a></code>
- <code title="get /accounts/{account_id}/email-security/investigate/{postfix_id}">client.email_security.investigate.<a href="./src/cloudflare/resources/email_security/investigate.py">get</a>(postfix_id, \*, account_id) -> <a href="./src/cloudflare/types/email_security/investigate_get_response.py">InvestigateGetResponse</a></code>
- <code title="get /accounts/{account_id}/email-security/investigate/{postfix_id}/preview">client.email_security.investigate.<a href="./src/cloudflare/resources/email_security/investigate.py">preview</a>(postfix_id, \*, account_id) -> <a href="./src/cloudflare/types/email_security/investigate_preview_response.py">InvestigatePreviewResponse</a></code>
- <code title="get /accounts/{account_id}/email-security/investigate/{postfix_id}/raw">client.email_security.investigate.<a href="./src/cloudflare/resources/email_security/investigate.py">raw</a>(postfix_id, \*, account_id) -> <a href="./src/cloudflare/types/email_security/investigate_raw_response.py">InvestigateRawResponse</a></code>
- <code title="get /accounts/{account_id}/email-security/investigate/{postfix_id}/trace">client.email_security.investigate.<a href="./src/cloudflare/resources/email_security/investigate.py">trace</a>(postfix_id, \*, account_id) -> <a href="./src/cloudflare/types/email_security/investigate_trace_response.py">InvestigateTraceResponse</a></code>

## Phishguard

Types:

```python
from cloudflare.types.email_security import PhishguardListResponse
```

Methods:

- <code title="get /accounts/{account_id}/email-security/phishguard/reports">client.email_security.phishguard.<a href="./src/cloudflare/resources/email_security/phishguard.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/email_security/phishguard_list_params.py">params</a>) -> <a href="./src/cloudflare/types/email_security/phishguard_list_response.py">SyncSinglePage[PhishguardListResponse]</a></code>

## Settings

### AllowPatterns

Types:

```python
from cloudflare.types.email_security.settings import (
    AllowPatternCreateResponse,
    AllowPatternListResponse,
    AllowPatternDeleteResponse,
    AllowPatternEditResponse,
    AllowPatternGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/email-security/settings/allow_patterns">client.email_security.settings.allow_patterns.<a href="./src/cloudflare/resources/email_security/settings/allow_patterns.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/email_security/settings/allow_pattern_create_params.py">params</a>) -> <a href="./src/cloudflare/types/email_security/settings/allow_pattern_create_response.py">AllowPatternCreateResponse</a></code>
- <code title="get /accounts/{account_id}/email-security/settings/allow_patterns">client.email_security.settings.allow_patterns.<a href="./src/cloudflare/resources/email_security/settings/allow_patterns.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/email_security/settings/allow_pattern_list_params.py">params</a>) -> <a href="./src/cloudflare/types/email_security/settings/allow_pattern_list_response.py">SyncV4PagePaginationArray[AllowPatternListResponse]</a></code>
- <code title="delete /accounts/{account_id}/email-security/settings/allow_patterns/{pattern_id}">client.email_security.settings.allow_patterns.<a href="./src/cloudflare/resources/email_security/settings/allow_patterns.py">delete</a>(pattern_id, \*, account_id) -> <a href="./src/cloudflare/types/email_security/settings/allow_pattern_delete_response.py">AllowPatternDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/email-security/settings/allow_patterns/{pattern_id}">client.email_security.settings.allow_patterns.<a href="./src/cloudflare/resources/email_security/settings/allow_patterns.py">edit</a>(pattern_id, \*, account_id, \*\*<a href="src/cloudflare/types/email_security/settings/allow_pattern_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/email_security/settings/allow_pattern_edit_response.py">AllowPatternEditResponse</a></code>
- <code title="get /accounts/{account_id}/email-security/settings/allow_patterns/{pattern_id}">client.email_security.settings.allow_patterns.<a href="./src/cloudflare/resources/email_security/settings/allow_patterns.py">get</a>(pattern_id, \*, account_id) -> <a href="./src/cloudflare/types/email_security/settings/allow_pattern_get_response.py">AllowPatternGetResponse</a></code>

### BlockSenders

Types:

```python
from cloudflare.types.email_security.settings import (
    BlockSenderCreateResponse,
    BlockSenderListResponse,
    BlockSenderDeleteResponse,
    BlockSenderEditResponse,
    BlockSenderGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/email-security/settings/block_senders">client.email_security.settings.block_senders.<a href="./src/cloudflare/resources/email_security/settings/block_senders.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/email_security/settings/block_sender_create_params.py">params</a>) -> <a href="./src/cloudflare/types/email_security/settings/block_sender_create_response.py">BlockSenderCreateResponse</a></code>
- <code title="get /accounts/{account_id}/email-security/settings/block_senders">client.email_security.settings.block_senders.<a href="./src/cloudflare/resources/email_security/settings/block_senders.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/email_security/settings/block_sender_list_params.py">params</a>) -> <a href="./src/cloudflare/types/email_security/settings/block_sender_list_response.py">SyncV4PagePaginationArray[BlockSenderListResponse]</a></code>
- <code title="delete /accounts/{account_id}/email-security/settings/block_senders/{pattern_id}">client.email_security.settings.block_senders.<a href="./src/cloudflare/resources/email_security/settings/block_senders.py">delete</a>(pattern_id, \*, account_id) -> <a href="./src/cloudflare/types/email_security/settings/block_sender_delete_response.py">BlockSenderDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/email-security/settings/block_senders/{pattern_id}">client.email_security.settings.block_senders.<a href="./src/cloudflare/resources/email_security/settings/block_senders.py">edit</a>(pattern_id, \*, account_id, \*\*<a href="src/cloudflare/types/email_security/settings/block_sender_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/email_security/settings/block_sender_edit_response.py">BlockSenderEditResponse</a></code>
- <code title="get /accounts/{account_id}/email-security/settings/block_senders/{pattern_id}">client.email_security.settings.block_senders.<a href="./src/cloudflare/resources/email_security/settings/block_senders.py">get</a>(pattern_id, \*, account_id) -> <a href="./src/cloudflare/types/email_security/settings/block_sender_get_response.py">BlockSenderGetResponse</a></code>

### Domains

Types:

```python
from cloudflare.types.email_security.settings import (
    DomainListResponse,
    DomainDeleteResponse,
    DomainEditResponse,
)
```

Methods:

- <code title="get /accounts/{account_id}/email-security/settings/domains">client.email_security.settings.domains.<a href="./src/cloudflare/resources/email_security/settings/domains.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/email_security/settings/domain_list_params.py">params</a>) -> <a href="./src/cloudflare/types/email_security/settings/domain_list_response.py">SyncV4PagePaginationArray[DomainListResponse]</a></code>
- <code title="delete /accounts/{account_id}/email-security/settings/domains/{domain_id}">client.email_security.settings.domains.<a href="./src/cloudflare/resources/email_security/settings/domains.py">delete</a>(domain_id, \*, account_id) -> <a href="./src/cloudflare/types/email_security/settings/domain_delete_response.py">DomainDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/email-security/settings/domains/{domain_id}">client.email_security.settings.domains.<a href="./src/cloudflare/resources/email_security/settings/domains.py">edit</a>(domain_id, \*, account_id, \*\*<a href="src/cloudflare/types/email_security/settings/domain_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/email_security/settings/domain_edit_response.py">DomainEditResponse</a></code>

### ImpersonationRegistry

Types:

```python
from cloudflare.types.email_security.settings import (
    ImpersonationRegistryCreateResponse,
    ImpersonationRegistryListResponse,
    ImpersonationRegistryDeleteResponse,
    ImpersonationRegistryEditResponse,
    ImpersonationRegistryGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/email-security/settings/impersonation_registry">client.email_security.settings.impersonation_registry.<a href="./src/cloudflare/resources/email_security/settings/impersonation_registry.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/email_security/settings/impersonation_registry_create_params.py">params</a>) -> <a href="./src/cloudflare/types/email_security/settings/impersonation_registry_create_response.py">ImpersonationRegistryCreateResponse</a></code>
- <code title="get /accounts/{account_id}/email-security/settings/impersonation_registry">client.email_security.settings.impersonation_registry.<a href="./src/cloudflare/resources/email_security/settings/impersonation_registry.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/email_security/settings/impersonation_registry_list_params.py">params</a>) -> <a href="./src/cloudflare/types/email_security/settings/impersonation_registry_list_response.py">SyncV4PagePaginationArray[ImpersonationRegistryListResponse]</a></code>
- <code title="delete /accounts/{account_id}/email-security/settings/impersonation_registry/{display_name_id}">client.email_security.settings.impersonation_registry.<a href="./src/cloudflare/resources/email_security/settings/impersonation_registry.py">delete</a>(display_name_id, \*, account_id) -> <a href="./src/cloudflare/types/email_security/settings/impersonation_registry_delete_response.py">ImpersonationRegistryDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/email-security/settings/impersonation_registry/{display_name_id}">client.email_security.settings.impersonation_registry.<a href="./src/cloudflare/resources/email_security/settings/impersonation_registry.py">edit</a>(display_name_id, \*, account_id, \*\*<a href="src/cloudflare/types/email_security/settings/impersonation_registry_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/email_security/settings/impersonation_registry_edit_response.py">ImpersonationRegistryEditResponse</a></code>
- <code title="get /accounts/{account_id}/email-security/settings/impersonation_registry/{display_name_id}">client.email_security.settings.impersonation_registry.<a href="./src/cloudflare/resources/email_security/settings/impersonation_registry.py">get</a>(display_name_id, \*, account_id) -> <a href="./src/cloudflare/types/email_security/settings/impersonation_registry_get_response.py">ImpersonationRegistryGetResponse</a></code>

### TrustedDomains

Types:

```python
from cloudflare.types.email_security.settings import (
    TrustedDomainCreateResponse,
    TrustedDomainListResponse,
    TrustedDomainDeleteResponse,
    TrustedDomainEditResponse,
    TrustedDomainGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/email-security/settings/trusted_domains">client.email_security.settings.trusted_domains.<a href="./src/cloudflare/resources/email_security/settings/trusted_domains.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/email_security/settings/trusted_domain_create_params.py">params</a>) -> <a href="./src/cloudflare/types/email_security/settings/trusted_domain_create_response.py">TrustedDomainCreateResponse</a></code>
- <code title="get /accounts/{account_id}/email-security/settings/trusted_domains">client.email_security.settings.trusted_domains.<a href="./src/cloudflare/resources/email_security/settings/trusted_domains.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/email_security/settings/trusted_domain_list_params.py">params</a>) -> <a href="./src/cloudflare/types/email_security/settings/trusted_domain_list_response.py">SyncV4PagePaginationArray[TrustedDomainListResponse]</a></code>
- <code title="delete /accounts/{account_id}/email-security/settings/trusted_domains/{pattern_id}">client.email_security.settings.trusted_domains.<a href="./src/cloudflare/resources/email_security/settings/trusted_domains.py">delete</a>(pattern_id, \*, account_id) -> <a href="./src/cloudflare/types/email_security/settings/trusted_domain_delete_response.py">TrustedDomainDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/email-security/settings/trusted_domains/{pattern_id}">client.email_security.settings.trusted_domains.<a href="./src/cloudflare/resources/email_security/settings/trusted_domains.py">edit</a>(pattern_id, \*, account_id, \*\*<a href="src/cloudflare/types/email_security/settings/trusted_domain_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/email_security/settings/trusted_domain_edit_response.py">TrustedDomainEditResponse</a></code>
- <code title="get /accounts/{account_id}/email-security/settings/trusted_domains/{pattern_id}">client.email_security.settings.trusted_domains.<a href="./src/cloudflare/resources/email_security/settings/trusted_domains.py">get</a>(pattern_id, \*, account_id) -> <a href="./src/cloudflare/types/email_security/settings/trusted_domain_get_response.py">TrustedDomainGetResponse</a></code>

# EmailRouting

Types:

```python
from cloudflare.types.email_routing import Settings
```

Methods:

- <code title="post /zones/{zone_id}/email/routing/disable">client.email_routing.<a href="./src/cloudflare/resources/email_routing/email_routing.py">disable</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/email_routing/email_routing_disable_params.py">params</a>) -> <a href="./src/cloudflare/types/email_routing/settings.py">Optional</a></code>
- <code title="post /zones/{zone_id}/email/routing/enable">client.email_routing.<a href="./src/cloudflare/resources/email_routing/email_routing.py">enable</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/email_routing/email_routing_enable_params.py">params</a>) -> <a href="./src/cloudflare/types/email_routing/settings.py">Optional</a></code>
- <code title="get /zones/{zone_id}/email/routing">client.email_routing.<a href="./src/cloudflare/resources/email_routing/email_routing.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/email_routing/settings.py">Optional</a></code>

## DNS

Types:

```python
from cloudflare.types.email_routing import DNSRecord, DNSGetResponse
```

Methods:

- <code title="post /zones/{zone_id}/email/routing/dns">client.email_routing.dns.<a href="./src/cloudflare/resources/email_routing/dns.py">create</a>(\*, zone_id) -> <a href="./src/cloudflare/types/email_routing/settings.py">Optional</a></code>
- <code title="delete /zones/{zone_id}/email/routing/dns">client.email_routing.dns.<a href="./src/cloudflare/resources/email_routing/dns.py">delete</a>(\*, zone_id) -> <a href="./src/cloudflare/types/email_routing/settings.py">Optional</a></code>
- <code title="patch /zones/{zone_id}/email/routing/dns">client.email_routing.dns.<a href="./src/cloudflare/resources/email_routing/dns.py">edit</a>(\*, zone_id) -> <a href="./src/cloudflare/types/email_routing/settings.py">Optional</a></code>
- <code title="get /zones/{zone_id}/email/routing/dns">client.email_routing.dns.<a href="./src/cloudflare/resources/email_routing/dns.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/email_routing/dns_get_response.py">Optional</a></code>

## Rules

Types:

```python
from cloudflare.types.email_routing import Action, EmailRoutingRule, Matcher
```

Methods:

- <code title="post /zones/{zone_id}/email/routing/rules">client.email_routing.rules.<a href="./src/cloudflare/resources/email_routing/rules/rules.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/email_routing/rule_create_params.py">params</a>) -> <a href="./src/cloudflare/types/email_routing/email_routing_rule.py">Optional</a></code>
- <code title="put /zones/{zone_id}/email/routing/rules/{rule_identifier}">client.email_routing.rules.<a href="./src/cloudflare/resources/email_routing/rules/rules.py">update</a>(rule_identifier, \*, zone_id, \*\*<a href="src/cloudflare/types/email_routing/rule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/email_routing/email_routing_rule.py">Optional</a></code>
- <code title="get /zones/{zone_id}/email/routing/rules">client.email_routing.rules.<a href="./src/cloudflare/resources/email_routing/rules/rules.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/email_routing/rule_list_params.py">params</a>) -> <a href="./src/cloudflare/types/email_routing/email_routing_rule.py">SyncV4PagePaginationArray[EmailRoutingRule]</a></code>
- <code title="delete /zones/{zone_id}/email/routing/rules/{rule_identifier}">client.email_routing.rules.<a href="./src/cloudflare/resources/email_routing/rules/rules.py">delete</a>(rule_identifier, \*, zone_id) -> <a href="./src/cloudflare/types/email_routing/email_routing_rule.py">Optional</a></code>
- <code title="get /zones/{zone_id}/email/routing/rules/{rule_identifier}">client.email_routing.rules.<a href="./src/cloudflare/resources/email_routing/rules/rules.py">get</a>(rule_identifier, \*, zone_id) -> <a href="./src/cloudflare/types/email_routing/email_routing_rule.py">Optional</a></code>

### CatchAlls

Types:

```python
from cloudflare.types.email_routing.rules import (
    CatchAllAction,
    CatchAllMatcher,
    CatchAllUpdateResponse,
    CatchAllGetResponse,
)
```

Methods:

- <code title="put /zones/{zone_id}/email/routing/rules/catch_all">client.email_routing.rules.catch_alls.<a href="./src/cloudflare/resources/email_routing/rules/catch_alls.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/email_routing/rules/catch_all_update_params.py">params</a>) -> <a href="./src/cloudflare/types/email_routing/rules/catch_all_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/email/routing/rules/catch_all">client.email_routing.rules.catch_alls.<a href="./src/cloudflare/resources/email_routing/rules/catch_alls.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/email_routing/rules/catch_all_get_response.py">Optional</a></code>

## Addresses

Types:

```python
from cloudflare.types.email_routing import Address
```

Methods:

- <code title="post /accounts/{account_id}/email/routing/addresses">client.email_routing.addresses.<a href="./src/cloudflare/resources/email_routing/addresses.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/email_routing/address_create_params.py">params</a>) -> <a href="./src/cloudflare/types/email_routing/address.py">Optional</a></code>
- <code title="get /accounts/{account_id}/email/routing/addresses">client.email_routing.addresses.<a href="./src/cloudflare/resources/email_routing/addresses.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/email_routing/address_list_params.py">params</a>) -> <a href="./src/cloudflare/types/email_routing/address.py">SyncV4PagePaginationArray[Address]</a></code>
- <code title="delete /accounts/{account_id}/email/routing/addresses/{destination_address_identifier}">client.email_routing.addresses.<a href="./src/cloudflare/resources/email_routing/addresses.py">delete</a>(destination_address_identifier, \*, account_id) -> <a href="./src/cloudflare/types/email_routing/address.py">Optional</a></code>
- <code title="get /accounts/{account_id}/email/routing/addresses/{destination_address_identifier}">client.email_routing.addresses.<a href="./src/cloudflare/resources/email_routing/addresses.py">get</a>(destination_address_identifier, \*, account_id) -> <a href="./src/cloudflare/types/email_routing/address.py">Optional</a></code>

# Filters

Types:

```python
from cloudflare.types.filters import FirewallFilter, FilterCreateResponse
```

Methods:

- <code title="post /zones/{zone_identifier}/filters">client.filters.<a href="./src/cloudflare/resources/filters.py">create</a>(zone_identifier, \*\*<a href="src/cloudflare/types/filters/filter_create_params.py">params</a>) -> <a href="./src/cloudflare/types/filters/filter_create_response.py">Optional</a></code>
- <code title="put /zones/{zone_identifier}/filters/{id}">client.filters.<a href="./src/cloudflare/resources/filters.py">update</a>(id, \*, zone_identifier, \*\*<a href="src/cloudflare/types/filters/filter_update_params.py">params</a>) -> <a href="./src/cloudflare/types/filters/firewall_filter.py">FirewallFilter</a></code>
- <code title="get /zones/{zone_identifier}/filters">client.filters.<a href="./src/cloudflare/resources/filters.py">list</a>(zone_identifier, \*\*<a href="src/cloudflare/types/filters/filter_list_params.py">params</a>) -> <a href="./src/cloudflare/types/filters/firewall_filter.py">SyncV4PagePaginationArray[FirewallFilter]</a></code>
- <code title="delete /zones/{zone_identifier}/filters/{id}">client.filters.<a href="./src/cloudflare/resources/filters.py">delete</a>(id, \*, zone_identifier) -> <a href="./src/cloudflare/types/filters/firewall_filter.py">FirewallFilter</a></code>
- <code title="get /zones/{zone_identifier}/filters/{id}">client.filters.<a href="./src/cloudflare/resources/filters.py">get</a>(id, \*, zone_identifier) -> <a href="./src/cloudflare/types/filters/firewall_filter.py">FirewallFilter</a></code>

# Firewall

## Lockdowns

Types:

```python
from cloudflare.types.firewall import (
    Configuration,
    Lockdown,
    LockdownCIDRConfiguration,
    LockdownIPConfiguration,
    LockdownURL,
    LockdownDeleteResponse,
)
```

Methods:

- <code title="post /zones/{zone_identifier}/firewall/lockdowns">client.firewall.lockdowns.<a href="./src/cloudflare/resources/firewall/lockdowns.py">create</a>(zone_identifier, \*\*<a href="src/cloudflare/types/firewall/lockdown_create_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/lockdown.py">Lockdown</a></code>
- <code title="put /zones/{zone_identifier}/firewall/lockdowns/{id}">client.firewall.lockdowns.<a href="./src/cloudflare/resources/firewall/lockdowns.py">update</a>(id, \*, zone_identifier, \*\*<a href="src/cloudflare/types/firewall/lockdown_update_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/lockdown.py">Lockdown</a></code>
- <code title="get /zones/{zone_identifier}/firewall/lockdowns">client.firewall.lockdowns.<a href="./src/cloudflare/resources/firewall/lockdowns.py">list</a>(zone_identifier, \*\*<a href="src/cloudflare/types/firewall/lockdown_list_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/lockdown.py">SyncV4PagePaginationArray[Lockdown]</a></code>
- <code title="delete /zones/{zone_identifier}/firewall/lockdowns/{id}">client.firewall.lockdowns.<a href="./src/cloudflare/resources/firewall/lockdowns.py">delete</a>(id, \*, zone_identifier) -> <a href="./src/cloudflare/types/firewall/lockdown_delete_response.py">Optional</a></code>
- <code title="get /zones/{zone_identifier}/firewall/lockdowns/{id}">client.firewall.lockdowns.<a href="./src/cloudflare/resources/firewall/lockdowns.py">get</a>(id, \*, zone_identifier) -> <a href="./src/cloudflare/types/firewall/lockdown.py">Lockdown</a></code>

## Rules

Types:

```python
from cloudflare.types.firewall import (
    FirewallRule,
    Product,
    DeletedFilter,
    RuleCreateResponse,
    RuleEditResponse,
)
```

Methods:

- <code title="post /zones/{zone_identifier}/firewall/rules">client.firewall.rules.<a href="./src/cloudflare/resources/firewall/rules.py">create</a>(zone_identifier, \*\*<a href="src/cloudflare/types/firewall/rule_create_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/rule_create_response.py">Optional</a></code>
- <code title="put /zones/{zone_identifier}/firewall/rules/{id}">client.firewall.rules.<a href="./src/cloudflare/resources/firewall/rules.py">update</a>(id, \*, zone_identifier, \*\*<a href="src/cloudflare/types/firewall/rule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/firewall_rule.py">FirewallRule</a></code>
- <code title="get /zones/{zone_identifier}/firewall/rules">client.firewall.rules.<a href="./src/cloudflare/resources/firewall/rules.py">list</a>(zone_identifier, \*\*<a href="src/cloudflare/types/firewall/rule_list_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/firewall_rule.py">SyncV4PagePaginationArray[FirewallRule]</a></code>
- <code title="delete /zones/{zone_identifier}/firewall/rules/{id}">client.firewall.rules.<a href="./src/cloudflare/resources/firewall/rules.py">delete</a>(id, \*, zone_identifier) -> <a href="./src/cloudflare/types/firewall/firewall_rule.py">FirewallRule</a></code>
- <code title="patch /zones/{zone_identifier}/firewall/rules/{id}">client.firewall.rules.<a href="./src/cloudflare/resources/firewall/rules.py">edit</a>(id, \*, zone_identifier) -> <a href="./src/cloudflare/types/firewall/rule_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_identifier}/firewall/rules/{id}">client.firewall.rules.<a href="./src/cloudflare/resources/firewall/rules.py">get</a>(zone_identifier, \*, path_id, \*\*<a href="src/cloudflare/types/firewall/rule_get_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/firewall_rule.py">FirewallRule</a></code>

## AccessRules

Types:

```python
from cloudflare.types.firewall import (
    AccessRuleCIDRConfiguration,
    AccessRuleIPConfiguration,
    ASNConfiguration,
    CountryConfiguration,
    IPV6Configuration,
    AccessRuleCreateResponse,
    AccessRuleListResponse,
    AccessRuleDeleteResponse,
    AccessRuleEditResponse,
    AccessRuleGetResponse,
)
```

Methods:

- <code title="post /{account_or_zone}/{account_or_zone_id}/firewall/access_rules/rules">client.firewall.access_rules.<a href="./src/cloudflare/resources/firewall/access_rules.py">create</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/firewall/access_rule_create_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/access_rule_create_response.py">AccessRuleCreateResponse</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/firewall/access_rules/rules">client.firewall.access_rules.<a href="./src/cloudflare/resources/firewall/access_rules.py">list</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/firewall/access_rule_list_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/access_rule_list_response.py">SyncV4PagePaginationArray[object]</a></code>
- <code title="delete /{account_or_zone}/{account_or_zone_id}/firewall/access_rules/rules/{identifier}">client.firewall.access_rules.<a href="./src/cloudflare/resources/firewall/access_rules.py">delete</a>(identifier, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/firewall/access_rule_delete_response.py">Optional</a></code>
- <code title="patch /{account_or_zone}/{account_or_zone_id}/firewall/access_rules/rules/{identifier}">client.firewall.access_rules.<a href="./src/cloudflare/resources/firewall/access_rules.py">edit</a>(identifier, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/firewall/access_rule_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/access_rule_edit_response.py">AccessRuleEditResponse</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/firewall/access_rules/rules/{identifier}">client.firewall.access_rules.<a href="./src/cloudflare/resources/firewall/access_rules.py">get</a>(identifier, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/firewall/access_rule_get_response.py">AccessRuleGetResponse</a></code>

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

- <code title="post /zones/{zone_identifier}/firewall/ua_rules">client.firewall.ua_rules.<a href="./src/cloudflare/resources/firewall/ua_rules.py">create</a>(zone_identifier, \*\*<a href="src/cloudflare/types/firewall/ua_rule_create_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/ua_rule_create_response.py">UARuleCreateResponse</a></code>
- <code title="put /zones/{zone_identifier}/firewall/ua_rules/{id}">client.firewall.ua_rules.<a href="./src/cloudflare/resources/firewall/ua_rules.py">update</a>(id, \*, zone_identifier, \*\*<a href="src/cloudflare/types/firewall/ua_rule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/ua_rule_update_response.py">UARuleUpdateResponse</a></code>
- <code title="get /zones/{zone_identifier}/firewall/ua_rules">client.firewall.ua_rules.<a href="./src/cloudflare/resources/firewall/ua_rules.py">list</a>(zone_identifier, \*\*<a href="src/cloudflare/types/firewall/ua_rule_list_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/ua_rule_list_response.py">SyncV4PagePaginationArray[UARuleListResponse]</a></code>
- <code title="delete /zones/{zone_identifier}/firewall/ua_rules/{id}">client.firewall.ua_rules.<a href="./src/cloudflare/resources/firewall/ua_rules.py">delete</a>(id, \*, zone_identifier) -> <a href="./src/cloudflare/types/firewall/ua_rule_delete_response.py">UARuleDeleteResponse</a></code>
- <code title="get /zones/{zone_identifier}/firewall/ua_rules/{id}">client.firewall.ua_rules.<a href="./src/cloudflare/resources/firewall/ua_rules.py">get</a>(id, \*, zone_identifier) -> <a href="./src/cloudflare/types/firewall/ua_rule_get_response.py">UARuleGetResponse</a></code>

## WAF

### Overrides

Types:

```python
from cloudflare.types.firewall.waf import (
    Override,
    OverrideURL,
    RewriteAction,
    WAFRule,
    OverrideDeleteResponse,
)
```

Methods:

- <code title="post /zones/{zone_identifier}/firewall/waf/overrides">client.firewall.waf.overrides.<a href="./src/cloudflare/resources/firewall/waf/overrides.py">create</a>(zone_identifier, \*\*<a href="src/cloudflare/types/firewall/waf/override_create_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/waf/override.py">Override</a></code>
- <code title="put /zones/{zone_identifier}/firewall/waf/overrides/{id}">client.firewall.waf.overrides.<a href="./src/cloudflare/resources/firewall/waf/overrides.py">update</a>(zone_identifier, \*, path_id, \*\*<a href="src/cloudflare/types/firewall/waf/override_update_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/waf/override.py">Override</a></code>
- <code title="get /zones/{zone_identifier}/firewall/waf/overrides">client.firewall.waf.overrides.<a href="./src/cloudflare/resources/firewall/waf/overrides.py">list</a>(zone_identifier, \*\*<a href="src/cloudflare/types/firewall/waf/override_list_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/waf/override.py">SyncV4PagePaginationArray[Override]</a></code>
- <code title="delete /zones/{zone_identifier}/firewall/waf/overrides/{id}">client.firewall.waf.overrides.<a href="./src/cloudflare/resources/firewall/waf/overrides.py">delete</a>(id, \*, zone_identifier) -> <a href="./src/cloudflare/types/firewall/waf/override_delete_response.py">Optional</a></code>
- <code title="get /zones/{zone_identifier}/firewall/waf/overrides/{id}">client.firewall.waf.overrides.<a href="./src/cloudflare/resources/firewall/waf/overrides.py">get</a>(id, \*, zone_identifier) -> <a href="./src/cloudflare/types/firewall/waf/override.py">Override</a></code>

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
from cloudflare.types.firewall.waf.packages import Group, GroupEditResponse, GroupGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/firewall/waf/packages/{package_id}/groups">client.firewall.waf.packages.groups.<a href="./src/cloudflare/resources/firewall/waf/packages/groups.py">list</a>(package_id, \*, zone_id, \*\*<a href="src/cloudflare/types/firewall/waf/packages/group_list_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/waf/packages/group.py">SyncV4PagePaginationArray[Group]</a></code>
- <code title="patch /zones/{zone_id}/firewall/waf/packages/{package_id}/groups/{group_id}">client.firewall.waf.packages.groups.<a href="./src/cloudflare/resources/firewall/waf/packages/groups.py">edit</a>(group_id, \*, zone_id, package_id, \*\*<a href="src/cloudflare/types/firewall/waf/packages/group_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/waf/packages/group_edit_response.py">GroupEditResponse</a></code>
- <code title="get /zones/{zone_id}/firewall/waf/packages/{package_id}/groups/{group_id}">client.firewall.waf.packages.groups.<a href="./src/cloudflare/resources/firewall/waf/packages/groups.py">get</a>(group_id, \*, zone_id, package_id) -> <a href="./src/cloudflare/types/firewall/waf/packages/group_get_response.py">GroupGetResponse</a></code>

#### Rules

Types:

```python
from cloudflare.types.firewall.waf.packages import (
    AllowedModesAnomaly,
    WAFRuleGroup,
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
from cloudflare.types.healthchecks import (
    CheckRegion,
    Healthcheck,
    HTTPConfiguration,
    QueryHealthcheck,
    TCPConfiguration,
    HealthcheckDeleteResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/healthchecks">client.healthchecks.<a href="./src/cloudflare/resources/healthchecks/healthchecks.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/healthchecks/healthcheck_create_params.py">params</a>) -> <a href="./src/cloudflare/types/healthchecks/healthcheck.py">Healthcheck</a></code>
- <code title="put /zones/{zone_id}/healthchecks/{healthcheck_id}">client.healthchecks.<a href="./src/cloudflare/resources/healthchecks/healthchecks.py">update</a>(healthcheck_id, \*, zone_id, \*\*<a href="src/cloudflare/types/healthchecks/healthcheck_update_params.py">params</a>) -> <a href="./src/cloudflare/types/healthchecks/healthcheck.py">Healthcheck</a></code>
- <code title="get /zones/{zone_id}/healthchecks">client.healthchecks.<a href="./src/cloudflare/resources/healthchecks/healthchecks.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/healthchecks/healthcheck_list_params.py">params</a>) -> <a href="./src/cloudflare/types/healthchecks/healthcheck.py">SyncV4PagePaginationArray[Healthcheck]</a></code>
- <code title="delete /zones/{zone_id}/healthchecks/{healthcheck_id}">client.healthchecks.<a href="./src/cloudflare/resources/healthchecks/healthchecks.py">delete</a>(healthcheck_id, \*, zone_id) -> <a href="./src/cloudflare/types/healthchecks/healthcheck_delete_response.py">HealthcheckDeleteResponse</a></code>
- <code title="patch /zones/{zone_id}/healthchecks/{healthcheck_id}">client.healthchecks.<a href="./src/cloudflare/resources/healthchecks/healthchecks.py">edit</a>(healthcheck_id, \*, zone_id, \*\*<a href="src/cloudflare/types/healthchecks/healthcheck_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/healthchecks/healthcheck.py">Healthcheck</a></code>
- <code title="get /zones/{zone_id}/healthchecks/{healthcheck_id}">client.healthchecks.<a href="./src/cloudflare/resources/healthchecks/healthchecks.py">get</a>(healthcheck_id, \*, zone_id) -> <a href="./src/cloudflare/types/healthchecks/healthcheck.py">Healthcheck</a></code>

## Previews

Types:

```python
from cloudflare.types.healthchecks import PreviewDeleteResponse
```

Methods:

- <code title="post /zones/{zone_id}/healthchecks/preview">client.healthchecks.previews.<a href="./src/cloudflare/resources/healthchecks/previews.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/healthchecks/preview_create_params.py">params</a>) -> <a href="./src/cloudflare/types/healthchecks/healthcheck.py">Healthcheck</a></code>
- <code title="delete /zones/{zone_id}/healthchecks/preview/{healthcheck_id}">client.healthchecks.previews.<a href="./src/cloudflare/resources/healthchecks/previews.py">delete</a>(healthcheck_id, \*, zone_id) -> <a href="./src/cloudflare/types/healthchecks/preview_delete_response.py">PreviewDeleteResponse</a></code>
- <code title="get /zones/{zone_id}/healthchecks/preview/{healthcheck_id}">client.healthchecks.previews.<a href="./src/cloudflare/resources/healthchecks/previews.py">get</a>(healthcheck_id, \*, zone_id) -> <a href="./src/cloudflare/types/healthchecks/healthcheck.py">Healthcheck</a></code>

# KeylessCertificates

Types:

```python
from cloudflare.types.keyless_certificates import (
    KeylessCertificate,
    Tunnel,
    KeylessCertificateDeleteResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/keyless_certificates">client.keyless_certificates.<a href="./src/cloudflare/resources/keyless_certificates.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/keyless_certificates/keyless_certificate_create_params.py">params</a>) -> <a href="./src/cloudflare/types/keyless_certificates/keyless_certificate.py">Optional</a></code>
- <code title="get /zones/{zone_id}/keyless_certificates">client.keyless_certificates.<a href="./src/cloudflare/resources/keyless_certificates.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/keyless_certificates/keyless_certificate.py">SyncSinglePage[KeylessCertificate]</a></code>
- <code title="delete /zones/{zone_id}/keyless_certificates/{keyless_certificate_id}">client.keyless_certificates.<a href="./src/cloudflare/resources/keyless_certificates.py">delete</a>(keyless_certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/keyless_certificates/keyless_certificate_delete_response.py">Optional</a></code>
- <code title="patch /zones/{zone_id}/keyless_certificates/{keyless_certificate_id}">client.keyless_certificates.<a href="./src/cloudflare/resources/keyless_certificates.py">edit</a>(keyless_certificate_id, \*, zone_id, \*\*<a href="src/cloudflare/types/keyless_certificates/keyless_certificate_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/keyless_certificates/keyless_certificate.py">Optional</a></code>
- <code title="get /zones/{zone_id}/keyless_certificates/{keyless_certificate_id}">client.keyless_certificates.<a href="./src/cloudflare/resources/keyless_certificates.py">get</a>(keyless_certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/keyless_certificates/keyless_certificate.py">Optional</a></code>

# Logpush

## Datasets

### Fields

Types:

```python
from cloudflare.types.logpush.datasets import FieldGetResponse
```

Methods:

- <code title="get /{account_or_zone}/{account_or_zone_id}/logpush/datasets/{dataset_id}/fields">client.logpush.datasets.fields.<a href="./src/cloudflare/resources/logpush/datasets/fields.py">get</a>(dataset_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/logpush/datasets/field_get_response.py">object</a></code>

### Jobs

Types:

```python
from cloudflare.types.logpush.datasets import JobGetResponse
```

Methods:

- <code title="get /{account_or_zone}/{account_or_zone_id}/logpush/datasets/{dataset_id}/jobs">client.logpush.datasets.jobs.<a href="./src/cloudflare/resources/logpush/datasets/jobs.py">get</a>(dataset_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/logpush/datasets/job_get_response.py">Optional</a></code>

## Edge

Types:

```python
from cloudflare.types.logpush import InstantLogpushJob, EdgeGetResponse
```

Methods:

- <code title="post /zones/{zone_id}/logpush/edge">client.logpush.edge.<a href="./src/cloudflare/resources/logpush/edge.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/logpush/edge_create_params.py">params</a>) -> <a href="./src/cloudflare/types/logpush/instant_logpush_job.py">Optional</a></code>
- <code title="get /zones/{zone_id}/logpush/edge">client.logpush.edge.<a href="./src/cloudflare/resources/logpush/edge.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/logpush/edge_get_response.py">Optional</a></code>

## Jobs

Types:

```python
from cloudflare.types.logpush import LogpushJob, OutputOptions, JobDeleteResponse
```

Methods:

- <code title="post /{account_or_zone}/{account_or_zone_id}/logpush/jobs">client.logpush.jobs.<a href="./src/cloudflare/resources/logpush/jobs.py">create</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/logpush/job_create_params.py">params</a>) -> <a href="./src/cloudflare/types/logpush/logpush_job.py">Optional</a></code>
- <code title="put /{account_or_zone}/{account_or_zone_id}/logpush/jobs/{job_id}">client.logpush.jobs.<a href="./src/cloudflare/resources/logpush/jobs.py">update</a>(job_id, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/logpush/job_update_params.py">params</a>) -> <a href="./src/cloudflare/types/logpush/logpush_job.py">Optional</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/logpush/jobs">client.logpush.jobs.<a href="./src/cloudflare/resources/logpush/jobs.py">list</a>(\*, account_id, zone_id) -> <a href="./src/cloudflare/types/logpush/logpush_job.py">SyncSinglePage[Optional]</a></code>
- <code title="delete /{account_or_zone}/{account_or_zone_id}/logpush/jobs/{job_id}">client.logpush.jobs.<a href="./src/cloudflare/resources/logpush/jobs.py">delete</a>(job_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/logpush/job_delete_response.py">Optional</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/logpush/jobs/{job_id}">client.logpush.jobs.<a href="./src/cloudflare/resources/logpush/jobs.py">get</a>(job_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/logpush/logpush_job.py">Optional</a></code>

## Ownership

Types:

```python
from cloudflare.types.logpush import OwnershipValidation, OwnershipCreateResponse
```

Methods:

- <code title="post /{account_or_zone}/{account_or_zone_id}/logpush/ownership">client.logpush.ownership.<a href="./src/cloudflare/resources/logpush/ownership.py">create</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/logpush/ownership_create_params.py">params</a>) -> <a href="./src/cloudflare/types/logpush/ownership_create_response.py">Optional</a></code>
- <code title="post /{account_or_zone}/{account_or_zone_id}/logpush/ownership/validate">client.logpush.ownership.<a href="./src/cloudflare/resources/logpush/ownership.py">validate</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/logpush/ownership_validate_params.py">params</a>) -> <a href="./src/cloudflare/types/logpush/ownership_validation.py">Optional</a></code>

## Validate

Types:

```python
from cloudflare.types.logpush import ValidateDestinationResponse, ValidateOriginResponse
```

Methods:

- <code title="post /{account_or_zone}/{account_or_zone_id}/logpush/validate/destination/exists">client.logpush.validate.<a href="./src/cloudflare/resources/logpush/validate.py">destination</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/logpush/validate_destination_params.py">params</a>) -> <a href="./src/cloudflare/types/logpush/validate_destination_response.py">Optional</a></code>
- <code title="post /{account_or_zone}/{account_or_zone_id}/logpush/validate/origin">client.logpush.validate.<a href="./src/cloudflare/resources/logpush/validate.py">origin</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/logpush/validate_origin_params.py">params</a>) -> <a href="./src/cloudflare/types/logpush/validate_origin_response.py">Optional</a></code>

# Logs

## Control

### Retention

Types:

```python
from cloudflare.types.logs.control import RetentionCreateResponse, RetentionGetResponse
```

Methods:

- <code title="post /zones/{zone_id}/logs/control/retention/flag">client.logs.control.retention.<a href="./src/cloudflare/resources/logs/control/retention.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/logs/control/retention_create_params.py">params</a>) -> <a href="./src/cloudflare/types/logs/control/retention_create_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/logs/control/retention/flag">client.logs.control.retention.<a href="./src/cloudflare/resources/logs/control/retention.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/logs/control/retention_get_response.py">Optional</a></code>

### Cmb

#### Config

Types:

```python
from cloudflare.types.logs.control.cmb import CmbConfig, ConfigDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/logs/control/cmb/config">client.logs.control.cmb.config.<a href="./src/cloudflare/resources/logs/control/cmb/config.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/logs/control/cmb/config_create_params.py">params</a>) -> <a href="./src/cloudflare/types/logs/control/cmb/cmb_config.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/logs/control/cmb/config">client.logs.control.cmb.config.<a href="./src/cloudflare/resources/logs/control/cmb/config.py">delete</a>(\*, account_id) -> <a href="./src/cloudflare/types/logs/control/cmb/config_delete_response.py">object</a></code>
- <code title="get /accounts/{account_id}/logs/control/cmb/config">client.logs.control.cmb.config.<a href="./src/cloudflare/resources/logs/control/cmb/config.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/logs/control/cmb/cmb_config.py">Optional</a></code>

## RayID

Types:

```python
from cloudflare.types.logs import RayIDGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/logs/rayids/{ray_id}">client.logs.rayid.<a href="./src/cloudflare/resources/logs/rayid.py">get</a>(rayid, \*, zone_id, \*\*<a href="src/cloudflare/types/logs/rayid_get_params.py">params</a>) -> <a href="./src/cloudflare/types/logs/rayid_get_response.py">RayIDGetResponse</a></code>

## Received

Types:

```python
from cloudflare.types.logs import ReceivedGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/logs/received">client.logs.received.<a href="./src/cloudflare/resources/logs/received/received.py">get</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/logs/received_get_params.py">params</a>) -> <a href="./src/cloudflare/types/logs/received_get_response.py">ReceivedGetResponse</a></code>

### Fields

Types:

```python
from cloudflare.types.logs.received import FieldGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/logs/received/fields">client.logs.received.fields.<a href="./src/cloudflare/resources/logs/received/fields.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/logs/received/field_get_response.py">FieldGetResponse</a></code>

# OriginTLSClientAuth

Types:

```python
from cloudflare.types.origin_tls_client_auth import ZoneAuthenticatedOriginPull
```

Methods:

- <code title="post /zones/{zone_id}/origin_tls_client_auth">client.origin_tls_client_auth.<a href="./src/cloudflare/resources/origin_tls_client_auth/origin_tls_client_auth.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/origin_tls_client_auth/origin_tls_client_auth_create_params.py">params</a>) -> <a href="./src/cloudflare/types/origin_tls_client_auth/zone_authenticated_origin_pull.py">Optional</a></code>
- <code title="get /zones/{zone_id}/origin_tls_client_auth">client.origin_tls_client_auth.<a href="./src/cloudflare/resources/origin_tls_client_auth/origin_tls_client_auth.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/origin_tls_client_auth/zone_authenticated_origin_pull.py">SyncSinglePage[ZoneAuthenticatedOriginPull]</a></code>
- <code title="delete /zones/{zone_id}/origin_tls_client_auth/{certificate_id}">client.origin_tls_client_auth.<a href="./src/cloudflare/resources/origin_tls_client_auth/origin_tls_client_auth.py">delete</a>(certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/origin_tls_client_auth/zone_authenticated_origin_pull.py">Optional</a></code>
- <code title="get /zones/{zone_id}/origin_tls_client_auth/{certificate_id}">client.origin_tls_client_auth.<a href="./src/cloudflare/resources/origin_tls_client_auth/origin_tls_client_auth.py">get</a>(certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/origin_tls_client_auth/zone_authenticated_origin_pull.py">Optional</a></code>

## Hostnames

Types:

```python
from cloudflare.types.origin_tls_client_auth import AuthenticatedOriginPull, HostnameUpdateResponse
```

Methods:

- <code title="put /zones/{zone_id}/origin_tls_client_auth/hostnames">client.origin_tls_client_auth.hostnames.<a href="./src/cloudflare/resources/origin_tls_client_auth/hostnames/hostnames.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/origin_tls_client_auth/hostname_update_params.py">params</a>) -> <a href="./src/cloudflare/types/origin_tls_client_auth/hostname_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/origin_tls_client_auth/hostnames/{hostname}">client.origin_tls_client_auth.hostnames.<a href="./src/cloudflare/resources/origin_tls_client_auth/hostnames/hostnames.py">get</a>(hostname, \*, zone_id) -> <a href="./src/cloudflare/types/origin_tls_client_auth/authenticated_origin_pull.py">Optional</a></code>

### Certificates

Types:

```python
from cloudflare.types.origin_tls_client_auth.hostnames import (
    Certificate,
    CertificateCreateResponse,
    CertificateDeleteResponse,
    CertificateGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/origin_tls_client_auth/hostnames/certificates">client.origin_tls_client_auth.hostnames.certificates.<a href="./src/cloudflare/resources/origin_tls_client_auth/hostnames/certificates.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/origin_tls_client_auth/hostnames/certificate_create_params.py">params</a>) -> <a href="./src/cloudflare/types/origin_tls_client_auth/hostnames/certificate_create_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/origin_tls_client_auth/hostnames/certificates">client.origin_tls_client_auth.hostnames.certificates.<a href="./src/cloudflare/resources/origin_tls_client_auth/hostnames/certificates.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/origin_tls_client_auth/authenticated_origin_pull.py">SyncSinglePage[AuthenticatedOriginPull]</a></code>
- <code title="delete /zones/{zone_id}/origin_tls_client_auth/hostnames/certificates/{certificate_id}">client.origin_tls_client_auth.hostnames.certificates.<a href="./src/cloudflare/resources/origin_tls_client_auth/hostnames/certificates.py">delete</a>(certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/origin_tls_client_auth/hostnames/certificate_delete_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/origin_tls_client_auth/hostnames/certificates/{certificate_id}">client.origin_tls_client_auth.hostnames.certificates.<a href="./src/cloudflare/resources/origin_tls_client_auth/hostnames/certificates.py">get</a>(certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/origin_tls_client_auth/hostnames/certificate_get_response.py">Optional</a></code>

## Settings

Types:

```python
from cloudflare.types.origin_tls_client_auth import SettingUpdateResponse, SettingGetResponse
```

Methods:

- <code title="put /zones/{zone_id}/origin_tls_client_auth/settings">client.origin_tls_client_auth.settings.<a href="./src/cloudflare/resources/origin_tls_client_auth/settings.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/origin_tls_client_auth/setting_update_params.py">params</a>) -> <a href="./src/cloudflare/types/origin_tls_client_auth/setting_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/origin_tls_client_auth/settings">client.origin_tls_client_auth.settings.<a href="./src/cloudflare/resources/origin_tls_client_auth/settings.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/origin_tls_client_auth/setting_get_response.py">Optional</a></code>

# Pagerules

Types:

```python
from cloudflare.types.pagerules import (
    PageRule,
    Route,
    Target,
    PageruleCreateResponse,
    PageruleUpdateResponse,
    PageruleListResponse,
    PageruleDeleteResponse,
    PageruleEditResponse,
    PageruleGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/pagerules">client.pagerules.<a href="./src/cloudflare/resources/pagerules/pagerules.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/pagerules/pagerule_create_params.py">params</a>) -> <a href="./src/cloudflare/types/pagerules/pagerule_create_response.py">PageruleCreateResponse</a></code>
- <code title="put /zones/{zone_id}/pagerules/{pagerule_id}">client.pagerules.<a href="./src/cloudflare/resources/pagerules/pagerules.py">update</a>(pagerule_id, \*, zone_id, \*\*<a href="src/cloudflare/types/pagerules/pagerule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/pagerules/pagerule_update_response.py">PageruleUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/pagerules">client.pagerules.<a href="./src/cloudflare/resources/pagerules/pagerules.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/pagerules/pagerule_list_params.py">params</a>) -> <a href="./src/cloudflare/types/pagerules/pagerule_list_response.py">PageruleListResponse</a></code>
- <code title="delete /zones/{zone_id}/pagerules/{pagerule_id}">client.pagerules.<a href="./src/cloudflare/resources/pagerules/pagerules.py">delete</a>(pagerule_id, \*, zone_id) -> <a href="./src/cloudflare/types/pagerules/pagerule_delete_response.py">Optional</a></code>
- <code title="patch /zones/{zone_id}/pagerules/{pagerule_id}">client.pagerules.<a href="./src/cloudflare/resources/pagerules/pagerules.py">edit</a>(pagerule_id, \*, zone_id, \*\*<a href="src/cloudflare/types/pagerules/pagerule_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/pagerules/pagerule_edit_response.py">PageruleEditResponse</a></code>
- <code title="get /zones/{zone_id}/pagerules/{pagerule_id}">client.pagerules.<a href="./src/cloudflare/resources/pagerules/pagerules.py">get</a>(pagerule_id, \*, zone_id) -> <a href="./src/cloudflare/types/pagerules/pagerule_get_response.py">PageruleGetResponse</a></code>

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
from cloudflare.types.rate_limits import (
    Action,
    Methods,
    RateLimit,
    RateLimitCreateResponse,
    RateLimitDeleteResponse,
    RateLimitEditResponse,
    RateLimitGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_identifier}/rate_limits">client.rate_limits.<a href="./src/cloudflare/resources/rate_limits.py">create</a>(zone_identifier, \*\*<a href="src/cloudflare/types/rate_limits/rate_limit_create_params.py">params</a>) -> <a href="./src/cloudflare/types/rate_limits/rate_limit_create_response.py">RateLimitCreateResponse</a></code>
- <code title="get /zones/{zone_identifier}/rate_limits">client.rate_limits.<a href="./src/cloudflare/resources/rate_limits.py">list</a>(zone_identifier, \*\*<a href="src/cloudflare/types/rate_limits/rate_limit_list_params.py">params</a>) -> <a href="./src/cloudflare/types/rate_limits/rate_limit.py">SyncV4PagePaginationArray[RateLimit]</a></code>
- <code title="delete /zones/{zone_identifier}/rate_limits/{id}">client.rate_limits.<a href="./src/cloudflare/resources/rate_limits.py">delete</a>(id, \*, zone_identifier) -> <a href="./src/cloudflare/types/rate_limits/rate_limit_delete_response.py">RateLimitDeleteResponse</a></code>
- <code title="put /zones/{zone_identifier}/rate_limits/{id}">client.rate_limits.<a href="./src/cloudflare/resources/rate_limits.py">edit</a>(id, \*, zone_identifier, \*\*<a href="src/cloudflare/types/rate_limits/rate_limit_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/rate_limits/rate_limit_edit_response.py">RateLimitEditResponse</a></code>
- <code title="get /zones/{zone_identifier}/rate_limits/{id}">client.rate_limits.<a href="./src/cloudflare/resources/rate_limits.py">get</a>(id, \*, zone_identifier) -> <a href="./src/cloudflare/types/rate_limits/rate_limit_get_response.py">RateLimitGetResponse</a></code>

# SecondaryDNS

## ForceAXFR

Types:

```python
from cloudflare.types.secondary_dns import ForceAXFR
```

Methods:

- <code title="post /zones/{zone_id}/secondary_dns/force_axfr">client.secondary_dns.force_axfr.<a href="./src/cloudflare/resources/secondary_dns/force_axfr.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/secondary_dns/force_axfr_create_params.py">params</a>) -> <a href="./src/cloudflare/types/secondary_dns/force_axfr.py">str</a></code>

## Incoming

Types:

```python
from cloudflare.types.secondary_dns import (
    Incoming,
    IncomingCreateResponse,
    IncomingUpdateResponse,
    IncomingDeleteResponse,
    IncomingGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/secondary_dns/incoming">client.secondary_dns.incoming.<a href="./src/cloudflare/resources/secondary_dns/incoming.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/secondary_dns/incoming_create_params.py">params</a>) -> <a href="./src/cloudflare/types/secondary_dns/incoming_create_response.py">Optional</a></code>
- <code title="put /zones/{zone_id}/secondary_dns/incoming">client.secondary_dns.incoming.<a href="./src/cloudflare/resources/secondary_dns/incoming.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/secondary_dns/incoming_update_params.py">params</a>) -> <a href="./src/cloudflare/types/secondary_dns/incoming_update_response.py">Optional</a></code>
- <code title="delete /zones/{zone_id}/secondary_dns/incoming">client.secondary_dns.incoming.<a href="./src/cloudflare/resources/secondary_dns/incoming.py">delete</a>(\*, zone_id) -> <a href="./src/cloudflare/types/secondary_dns/incoming_delete_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/secondary_dns/incoming">client.secondary_dns.incoming.<a href="./src/cloudflare/resources/secondary_dns/incoming.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/secondary_dns/incoming_get_response.py">Optional</a></code>

## Outgoing

Types:

```python
from cloudflare.types.secondary_dns import (
    DisableTransfer,
    EnableTransfer,
    Outgoing,
    OutgoingStatus,
    OutgoingCreateResponse,
    OutgoingUpdateResponse,
    OutgoingDeleteResponse,
    OutgoingForceNotifyResponse,
    OutgoingGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/secondary_dns/outgoing">client.secondary_dns.outgoing.<a href="./src/cloudflare/resources/secondary_dns/outgoing/outgoing.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/secondary_dns/outgoing_create_params.py">params</a>) -> <a href="./src/cloudflare/types/secondary_dns/outgoing_create_response.py">Optional</a></code>
- <code title="put /zones/{zone_id}/secondary_dns/outgoing">client.secondary_dns.outgoing.<a href="./src/cloudflare/resources/secondary_dns/outgoing/outgoing.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/secondary_dns/outgoing_update_params.py">params</a>) -> <a href="./src/cloudflare/types/secondary_dns/outgoing_update_response.py">Optional</a></code>
- <code title="delete /zones/{zone_id}/secondary_dns/outgoing">client.secondary_dns.outgoing.<a href="./src/cloudflare/resources/secondary_dns/outgoing/outgoing.py">delete</a>(\*, zone_id) -> <a href="./src/cloudflare/types/secondary_dns/outgoing_delete_response.py">Optional</a></code>
- <code title="post /zones/{zone_id}/secondary_dns/outgoing/disable">client.secondary_dns.outgoing.<a href="./src/cloudflare/resources/secondary_dns/outgoing/outgoing.py">disable</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/secondary_dns/outgoing_disable_params.py">params</a>) -> <a href="./src/cloudflare/types/secondary_dns/disable_transfer.py">str</a></code>
- <code title="post /zones/{zone_id}/secondary_dns/outgoing/enable">client.secondary_dns.outgoing.<a href="./src/cloudflare/resources/secondary_dns/outgoing/outgoing.py">enable</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/secondary_dns/outgoing_enable_params.py">params</a>) -> <a href="./src/cloudflare/types/secondary_dns/enable_transfer.py">str</a></code>
- <code title="post /zones/{zone_id}/secondary_dns/outgoing/force_notify">client.secondary_dns.outgoing.<a href="./src/cloudflare/resources/secondary_dns/outgoing/outgoing.py">force_notify</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/secondary_dns/outgoing_force_notify_params.py">params</a>) -> <a href="./src/cloudflare/types/secondary_dns/outgoing_force_notify_response.py">str</a></code>
- <code title="get /zones/{zone_id}/secondary_dns/outgoing">client.secondary_dns.outgoing.<a href="./src/cloudflare/resources/secondary_dns/outgoing/outgoing.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/secondary_dns/outgoing_get_response.py">Optional</a></code>

### Status

Methods:

- <code title="get /zones/{zone_id}/secondary_dns/outgoing/status">client.secondary_dns.outgoing.status.<a href="./src/cloudflare/resources/secondary_dns/outgoing/status.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/secondary_dns/enable_transfer.py">str</a></code>

## ACLs

Types:

```python
from cloudflare.types.secondary_dns import ACL, ACLDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/secondary_dns/acls">client.secondary_dns.acls.<a href="./src/cloudflare/resources/secondary_dns/acls.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/secondary_dns/acl_create_params.py">params</a>) -> <a href="./src/cloudflare/types/secondary_dns/acl.py">Optional</a></code>
- <code title="put /accounts/{account_id}/secondary_dns/acls/{acl_id}">client.secondary_dns.acls.<a href="./src/cloudflare/resources/secondary_dns/acls.py">update</a>(acl_id, \*, account_id, \*\*<a href="src/cloudflare/types/secondary_dns/acl_update_params.py">params</a>) -> <a href="./src/cloudflare/types/secondary_dns/acl.py">Optional</a></code>
- <code title="get /accounts/{account_id}/secondary_dns/acls">client.secondary_dns.acls.<a href="./src/cloudflare/resources/secondary_dns/acls.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/secondary_dns/acl.py">SyncSinglePage[ACL]</a></code>
- <code title="delete /accounts/{account_id}/secondary_dns/acls/{acl_id}">client.secondary_dns.acls.<a href="./src/cloudflare/resources/secondary_dns/acls.py">delete</a>(acl_id, \*, account_id) -> <a href="./src/cloudflare/types/secondary_dns/acl_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/secondary_dns/acls/{acl_id}">client.secondary_dns.acls.<a href="./src/cloudflare/resources/secondary_dns/acls.py">get</a>(acl_id, \*, account_id) -> <a href="./src/cloudflare/types/secondary_dns/acl.py">Optional</a></code>

## Peers

Types:

```python
from cloudflare.types.secondary_dns import Peer, PeerDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/secondary_dns/peers">client.secondary_dns.peers.<a href="./src/cloudflare/resources/secondary_dns/peers.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/secondary_dns/peer_create_params.py">params</a>) -> <a href="./src/cloudflare/types/secondary_dns/peer.py">Optional</a></code>
- <code title="put /accounts/{account_id}/secondary_dns/peers/{peer_id}">client.secondary_dns.peers.<a href="./src/cloudflare/resources/secondary_dns/peers.py">update</a>(peer_id, \*, account_id, \*\*<a href="src/cloudflare/types/secondary_dns/peer_update_params.py">params</a>) -> <a href="./src/cloudflare/types/secondary_dns/peer.py">Optional</a></code>
- <code title="get /accounts/{account_id}/secondary_dns/peers">client.secondary_dns.peers.<a href="./src/cloudflare/resources/secondary_dns/peers.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/secondary_dns/peer.py">SyncSinglePage[Peer]</a></code>
- <code title="delete /accounts/{account_id}/secondary_dns/peers/{peer_id}">client.secondary_dns.peers.<a href="./src/cloudflare/resources/secondary_dns/peers.py">delete</a>(peer_id, \*, account_id) -> <a href="./src/cloudflare/types/secondary_dns/peer_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/secondary_dns/peers/{peer_id}">client.secondary_dns.peers.<a href="./src/cloudflare/resources/secondary_dns/peers.py">get</a>(peer_id, \*, account_id) -> <a href="./src/cloudflare/types/secondary_dns/peer.py">Optional</a></code>

## TSIGs

Types:

```python
from cloudflare.types.secondary_dns import TSIG, TSIGDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/secondary_dns/tsigs">client.secondary_dns.tsigs.<a href="./src/cloudflare/resources/secondary_dns/tsigs.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/secondary_dns/tsig_create_params.py">params</a>) -> <a href="./src/cloudflare/types/secondary_dns/tsig.py">Optional</a></code>
- <code title="put /accounts/{account_id}/secondary_dns/tsigs/{tsig_id}">client.secondary_dns.tsigs.<a href="./src/cloudflare/resources/secondary_dns/tsigs.py">update</a>(tsig_id, \*, account_id, \*\*<a href="src/cloudflare/types/secondary_dns/tsig_update_params.py">params</a>) -> <a href="./src/cloudflare/types/secondary_dns/tsig.py">Optional</a></code>
- <code title="get /accounts/{account_id}/secondary_dns/tsigs">client.secondary_dns.tsigs.<a href="./src/cloudflare/resources/secondary_dns/tsigs.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/secondary_dns/tsig.py">SyncSinglePage[TSIG]</a></code>
- <code title="delete /accounts/{account_id}/secondary_dns/tsigs/{tsig_id}">client.secondary_dns.tsigs.<a href="./src/cloudflare/resources/secondary_dns/tsigs.py">delete</a>(tsig_id, \*, account_id) -> <a href="./src/cloudflare/types/secondary_dns/tsig_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/secondary_dns/tsigs/{tsig_id}">client.secondary_dns.tsigs.<a href="./src/cloudflare/resources/secondary_dns/tsigs.py">get</a>(tsig_id, \*, account_id) -> <a href="./src/cloudflare/types/secondary_dns/tsig.py">Optional</a></code>

# WaitingRooms

Types:

```python
from cloudflare.types.waiting_rooms import (
    AdditionalRoutes,
    CookieAttributes,
    Query,
    WaitingRoom,
    WaitingRoomDeleteResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/waiting_rooms">client.waiting_rooms.<a href="./src/cloudflare/resources/waiting_rooms/waiting_rooms.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/waiting_rooms/waiting_room_create_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/waiting_room.py">WaitingRoom</a></code>
- <code title="put /zones/{zone_id}/waiting_rooms/{waiting_room_id}">client.waiting_rooms.<a href="./src/cloudflare/resources/waiting_rooms/waiting_rooms.py">update</a>(waiting_room_id, \*, zone_id, \*\*<a href="src/cloudflare/types/waiting_rooms/waiting_room_update_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/waiting_room.py">WaitingRoom</a></code>
- <code title="get /zones/{zone_id}/waiting_rooms">client.waiting_rooms.<a href="./src/cloudflare/resources/waiting_rooms/waiting_rooms.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/waiting_rooms/waiting_room_list_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/waiting_room.py">SyncV4PagePaginationArray[WaitingRoom]</a></code>
- <code title="delete /zones/{zone_id}/waiting_rooms/{waiting_room_id}">client.waiting_rooms.<a href="./src/cloudflare/resources/waiting_rooms/waiting_rooms.py">delete</a>(waiting_room_id, \*, zone_id) -> <a href="./src/cloudflare/types/waiting_rooms/waiting_room_delete_response.py">WaitingRoomDeleteResponse</a></code>
- <code title="patch /zones/{zone_id}/waiting_rooms/{waiting_room_id}">client.waiting_rooms.<a href="./src/cloudflare/resources/waiting_rooms/waiting_rooms.py">edit</a>(waiting_room_id, \*, zone_id, \*\*<a href="src/cloudflare/types/waiting_rooms/waiting_room_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/waiting_room.py">WaitingRoom</a></code>
- <code title="get /zones/{zone_id}/waiting_rooms/{waiting_room_id}">client.waiting_rooms.<a href="./src/cloudflare/resources/waiting_rooms/waiting_rooms.py">get</a>(waiting_room_id, \*, zone_id) -> <a href="./src/cloudflare/types/waiting_rooms/waiting_room.py">WaitingRoom</a></code>

## Page

Types:

```python
from cloudflare.types.waiting_rooms import PagePreviewResponse
```

Methods:

- <code title="post /zones/{zone_id}/waiting_rooms/preview">client.waiting_rooms.page.<a href="./src/cloudflare/resources/waiting_rooms/page.py">preview</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/waiting_rooms/page_preview_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/page_preview_response.py">PagePreviewResponse</a></code>

## Events

Types:

```python
from cloudflare.types.waiting_rooms import Event, EventDeleteResponse
```

Methods:

- <code title="post /zones/{zone_id}/waiting_rooms/{waiting_room_id}/events">client.waiting_rooms.events.<a href="./src/cloudflare/resources/waiting_rooms/events/events.py">create</a>(waiting_room_id, \*, zone_id, \*\*<a href="src/cloudflare/types/waiting_rooms/event_create_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/event.py">Event</a></code>
- <code title="put /zones/{zone_id}/waiting_rooms/{waiting_room_id}/events/{event_id}">client.waiting_rooms.events.<a href="./src/cloudflare/resources/waiting_rooms/events/events.py">update</a>(event_id, \*, zone_id, waiting_room_id, \*\*<a href="src/cloudflare/types/waiting_rooms/event_update_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/event.py">Event</a></code>
- <code title="get /zones/{zone_id}/waiting_rooms/{waiting_room_id}/events">client.waiting_rooms.events.<a href="./src/cloudflare/resources/waiting_rooms/events/events.py">list</a>(waiting_room_id, \*, zone_id, \*\*<a href="src/cloudflare/types/waiting_rooms/event_list_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/event.py">SyncV4PagePaginationArray[Event]</a></code>
- <code title="delete /zones/{zone_id}/waiting_rooms/{waiting_room_id}/events/{event_id}">client.waiting_rooms.events.<a href="./src/cloudflare/resources/waiting_rooms/events/events.py">delete</a>(event_id, \*, zone_id, waiting_room_id) -> <a href="./src/cloudflare/types/waiting_rooms/event_delete_response.py">EventDeleteResponse</a></code>
- <code title="patch /zones/{zone_id}/waiting_rooms/{waiting_room_id}/events/{event_id}">client.waiting_rooms.events.<a href="./src/cloudflare/resources/waiting_rooms/events/events.py">edit</a>(event_id, \*, zone_id, waiting_room_id, \*\*<a href="src/cloudflare/types/waiting_rooms/event_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/event.py">Event</a></code>
- <code title="get /zones/{zone_id}/waiting_rooms/{waiting_room_id}/events/{event_id}">client.waiting_rooms.events.<a href="./src/cloudflare/resources/waiting_rooms/events/events.py">get</a>(event_id, \*, zone_id, waiting_room_id) -> <a href="./src/cloudflare/types/waiting_rooms/event.py">Event</a></code>

### Details

Types:

```python
from cloudflare.types.waiting_rooms.events import EventQuery, DetailGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/waiting_rooms/{waiting_room_id}/events/{event_id}/details">client.waiting_rooms.events.details.<a href="./src/cloudflare/resources/waiting_rooms/events/details.py">get</a>(event_id, \*, zone_id, waiting_room_id) -> <a href="./src/cloudflare/types/waiting_rooms/events/detail_get_response.py">DetailGetResponse</a></code>

## Rules

Types:

```python
from cloudflare.types.waiting_rooms import (
    WaitingRoomRule,
    RuleCreateResponse,
    RuleUpdateResponse,
    RuleDeleteResponse,
    RuleEditResponse,
    RuleGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules">client.waiting_rooms.rules.<a href="./src/cloudflare/resources/waiting_rooms/rules.py">create</a>(waiting_room_id, \*, zone_id, \*\*<a href="src/cloudflare/types/waiting_rooms/rule_create_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/rule_create_response.py">Optional</a></code>
- <code title="put /zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules">client.waiting_rooms.rules.<a href="./src/cloudflare/resources/waiting_rooms/rules.py">update</a>(waiting_room_id, \*, zone_id, \*\*<a href="src/cloudflare/types/waiting_rooms/rule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/rule_update_response.py">Optional</a></code>
- <code title="delete /zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules/{rule_id}">client.waiting_rooms.rules.<a href="./src/cloudflare/resources/waiting_rooms/rules.py">delete</a>(rule_id, \*, zone_id, waiting_room_id) -> <a href="./src/cloudflare/types/waiting_rooms/rule_delete_response.py">Optional</a></code>
- <code title="patch /zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules/{rule_id}">client.waiting_rooms.rules.<a href="./src/cloudflare/resources/waiting_rooms/rules.py">edit</a>(rule_id, \*, zone_id, waiting_room_id, \*\*<a href="src/cloudflare/types/waiting_rooms/rule_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/rule_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules">client.waiting_rooms.rules.<a href="./src/cloudflare/resources/waiting_rooms/rules.py">get</a>(waiting_room_id, \*, zone_id) -> <a href="./src/cloudflare/types/waiting_rooms/rule_get_response.py">Optional</a></code>

## Statuses

Types:

```python
from cloudflare.types.waiting_rooms import StatusGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/waiting_rooms/{waiting_room_id}/status">client.waiting_rooms.statuses.<a href="./src/cloudflare/resources/waiting_rooms/statuses.py">get</a>(waiting_room_id, \*, zone_id) -> <a href="./src/cloudflare/types/waiting_rooms/status_get_response.py">StatusGetResponse</a></code>

## Settings

Types:

```python
from cloudflare.types.waiting_rooms import (
    Setting,
    SettingUpdateResponse,
    SettingEditResponse,
    SettingGetResponse,
)
```

Methods:

- <code title="put /zones/{zone_id}/waiting_rooms/settings">client.waiting_rooms.settings.<a href="./src/cloudflare/resources/waiting_rooms/settings.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/waiting_rooms/setting_update_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/setting_update_response.py">SettingUpdateResponse</a></code>
- <code title="patch /zones/{zone_id}/waiting_rooms/settings">client.waiting_rooms.settings.<a href="./src/cloudflare/resources/waiting_rooms/settings.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/waiting_rooms/setting_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/setting_edit_response.py">SettingEditResponse</a></code>
- <code title="get /zones/{zone_id}/waiting_rooms/settings">client.waiting_rooms.settings.<a href="./src/cloudflare/resources/waiting_rooms/settings.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/waiting_rooms/setting_get_response.py">SettingGetResponse</a></code>

# Web3

## Hostnames

Types:

```python
from cloudflare.types.web3 import Hostname, HostnameDeleteResponse
```

Methods:

- <code title="post /zones/{zone_id}/web3/hostnames">client.web3.hostnames.<a href="./src/cloudflare/resources/web3/hostnames/hostnames.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/web3/hostname_create_params.py">params</a>) -> <a href="./src/cloudflare/types/web3/hostname.py">Hostname</a></code>
- <code title="get /zones/{zone_id}/web3/hostnames">client.web3.hostnames.<a href="./src/cloudflare/resources/web3/hostnames/hostnames.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/web3/hostname.py">SyncSinglePage[Hostname]</a></code>
- <code title="delete /zones/{zone_id}/web3/hostnames/{identifier}">client.web3.hostnames.<a href="./src/cloudflare/resources/web3/hostnames/hostnames.py">delete</a>(identifier, \*, zone_id) -> <a href="./src/cloudflare/types/web3/hostname_delete_response.py">Optional</a></code>
- <code title="patch /zones/{zone_id}/web3/hostnames/{identifier}">client.web3.hostnames.<a href="./src/cloudflare/resources/web3/hostnames/hostnames.py">edit</a>(identifier, \*, zone_id, \*\*<a href="src/cloudflare/types/web3/hostname_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/web3/hostname.py">Hostname</a></code>
- <code title="get /zones/{zone_id}/web3/hostnames/{identifier}">client.web3.hostnames.<a href="./src/cloudflare/resources/web3/hostnames/hostnames.py">get</a>(identifier, \*, zone_id) -> <a href="./src/cloudflare/types/web3/hostname.py">Hostname</a></code>

### IPFSUniversalPaths

#### ContentLists

Types:

```python
from cloudflare.types.web3.hostnames.ipfs_universal_paths import ContentList
```

Methods:

- <code title="put /zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list">client.web3.hostnames.ipfs_universal_paths.content_lists.<a href="./src/cloudflare/resources/web3/hostnames/ipfs_universal_paths/content_lists/content_lists.py">update</a>(identifier, \*, zone_id, \*\*<a href="src/cloudflare/types/web3/hostnames/ipfs_universal_paths/content_list_update_params.py">params</a>) -> <a href="./src/cloudflare/types/web3/hostnames/ipfs_universal_paths/content_list.py">ContentList</a></code>
- <code title="get /zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list">client.web3.hostnames.ipfs_universal_paths.content_lists.<a href="./src/cloudflare/resources/web3/hostnames/ipfs_universal_paths/content_lists/content_lists.py">get</a>(identifier, \*, zone_id) -> <a href="./src/cloudflare/types/web3/hostnames/ipfs_universal_paths/content_list.py">ContentList</a></code>

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

- <code title="post /zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries">client.web3.hostnames.ipfs_universal_paths.content_lists.entries.<a href="./src/cloudflare/resources/web3/hostnames/ipfs_universal_paths/content_lists/entries.py">create</a>(identifier, \*, zone_id, \*\*<a href="src/cloudflare/types/web3/hostnames/ipfs_universal_paths/content_lists/entry_create_params.py">params</a>) -> <a href="./src/cloudflare/types/web3/hostnames/ipfs_universal_paths/content_lists/entry_create_response.py">EntryCreateResponse</a></code>
- <code title="put /zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries/{content_list_entry_identifier}">client.web3.hostnames.ipfs_universal_paths.content_lists.entries.<a href="./src/cloudflare/resources/web3/hostnames/ipfs_universal_paths/content_lists/entries.py">update</a>(content_list_entry_identifier, \*, zone_id, identifier, \*\*<a href="src/cloudflare/types/web3/hostnames/ipfs_universal_paths/content_lists/entry_update_params.py">params</a>) -> <a href="./src/cloudflare/types/web3/hostnames/ipfs_universal_paths/content_lists/entry_update_response.py">EntryUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries">client.web3.hostnames.ipfs_universal_paths.content_lists.entries.<a href="./src/cloudflare/resources/web3/hostnames/ipfs_universal_paths/content_lists/entries.py">list</a>(identifier, \*, zone_id) -> <a href="./src/cloudflare/types/web3/hostnames/ipfs_universal_paths/content_lists/entry_list_response.py">Optional</a></code>
- <code title="delete /zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries/{content_list_entry_identifier}">client.web3.hostnames.ipfs_universal_paths.content_lists.entries.<a href="./src/cloudflare/resources/web3/hostnames/ipfs_universal_paths/content_lists/entries.py">delete</a>(content_list_entry_identifier, \*, zone_id, identifier) -> <a href="./src/cloudflare/types/web3/hostnames/ipfs_universal_paths/content_lists/entry_delete_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries/{content_list_entry_identifier}">client.web3.hostnames.ipfs_universal_paths.content_lists.entries.<a href="./src/cloudflare/resources/web3/hostnames/ipfs_universal_paths/content_lists/entries.py">get</a>(content_list_entry_identifier, \*, zone_id, identifier) -> <a href="./src/cloudflare/types/web3/hostnames/ipfs_universal_paths/content_lists/entry_get_response.py">EntryGetResponse</a></code>

# Workers

Types:

```python
from cloudflare.types.workers import (
    Binding,
    D1Binding,
    DispatchNamespaceBinding,
    DurableObjectBinding,
    KVNamespaceBinding,
    MigrationStep,
    MTLSCERTBinding,
    PlacementConfiguration,
    R2Binding,
    ServiceBinding,
    SingleStepMigration,
    SteppedMigration,
    WorkerMetadata,
)
```

## AI

Types:

```python
from cloudflare.types.workers import AIRunResponse
```

Methods:

- <code title="post /accounts/{account_id}/ai/run/{model_name}">client.workers.ai.<a href="./src/cloudflare/resources/workers/ai/ai.py">run</a>(model_name, \*, account_id, \*\*<a href="src/cloudflare/types/workers/ai_run_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/ai_run_response.py">Optional</a></code>

### Models

#### Schema

Types:

```python
from cloudflare.types.workers.ai.models import SchemaGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/ai/models/schema">client.workers.ai.models.schema.<a href="./src/cloudflare/resources/workers/ai/models/schema.py">get</a>(\*, account_id, \*\*<a href="src/cloudflare/types/workers/ai/models/schema_get_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/ai/models/schema_get_response.py">object</a></code>

## Scripts

Types:

```python
from cloudflare.types.workers import Script, ScriptSetting, ScriptUpdateResponse
```

Methods:

- <code title="put /accounts/{account_id}/workers/scripts/{script_name}">client.workers.scripts.<a href="./src/cloudflare/resources/workers/scripts/scripts.py">update</a>(script_name, \*, account_id, \*\*<a href="src/cloudflare/types/workers/script_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/script_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/workers/scripts">client.workers.scripts.<a href="./src/cloudflare/resources/workers/scripts/scripts.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/workers/script.py">SyncSinglePage[Script]</a></code>
- <code title="delete /accounts/{account_id}/workers/scripts/{script_name}">client.workers.scripts.<a href="./src/cloudflare/resources/workers/scripts/scripts.py">delete</a>(script_name, \*, account_id, \*\*<a href="src/cloudflare/types/workers/script_delete_params.py">params</a>) -> None</code>
- <code title="get /accounts/{account_id}/workers/scripts/{script_name}">client.workers.scripts.<a href="./src/cloudflare/resources/workers/scripts/scripts.py">get</a>(script_name, \*, account_id) -> BinaryAPIResponse</code>

### Schedules

Types:

```python
from cloudflare.types.workers.scripts import Schedule, ScheduleUpdateResponse, ScheduleGetResponse
```

Methods:

- <code title="put /accounts/{account_id}/workers/scripts/{script_name}/schedules">client.workers.scripts.schedules.<a href="./src/cloudflare/resources/workers/scripts/schedules.py">update</a>(script_name, \*, account_id, \*\*<a href="src/cloudflare/types/workers/scripts/schedule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/scripts/schedule_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/workers/scripts/{script_name}/schedules">client.workers.scripts.schedules.<a href="./src/cloudflare/resources/workers/scripts/schedules.py">get</a>(script_name, \*, account_id) -> <a href="./src/cloudflare/types/workers/scripts/schedule_get_response.py">Optional</a></code>

### Tail

Types:

```python
from cloudflare.types.workers.scripts import (
    ConsumerScript,
    TailCreateResponse,
    TailDeleteResponse,
    TailGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/workers/scripts/{script_name}/tails">client.workers.scripts.tail.<a href="./src/cloudflare/resources/workers/scripts/tail.py">create</a>(script_name, \*, account_id, \*\*<a href="src/cloudflare/types/workers/scripts/tail_create_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/scripts/tail_create_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/workers/scripts/{script_name}/tails/{id}">client.workers.scripts.tail.<a href="./src/cloudflare/resources/workers/scripts/tail.py">delete</a>(id, \*, account_id, script_name) -> <a href="./src/cloudflare/types/workers/scripts/tail_delete_response.py">TailDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/workers/scripts/{script_name}/tails">client.workers.scripts.tail.<a href="./src/cloudflare/resources/workers/scripts/tail.py">get</a>(script_name, \*, account_id) -> <a href="./src/cloudflare/types/workers/scripts/tail_get_response.py">Optional</a></code>

### Content

Methods:

- <code title="put /accounts/{account_id}/workers/scripts/{script_name}/content">client.workers.scripts.content.<a href="./src/cloudflare/resources/workers/scripts/content.py">update</a>(script_name, \*, account_id, \*\*<a href="src/cloudflare/types/workers/scripts/content_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/script.py">Optional</a></code>
- <code title="get /accounts/{account_id}/workers/scripts/{script_name}/content/v2">client.workers.scripts.content.<a href="./src/cloudflare/resources/workers/scripts/content.py">get</a>(script_name, \*, account_id) -> BinaryAPIResponse</code>

### Settings

Methods:

- <code title="patch /accounts/{account_id}/workers/scripts/{script_name}/script-settings">client.workers.scripts.settings.<a href="./src/cloudflare/resources/workers/scripts/settings.py">edit</a>(script_name, \*, account_id, \*\*<a href="src/cloudflare/types/workers/scripts/setting_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/script_setting.py">Optional</a></code>
- <code title="get /accounts/{account_id}/workers/scripts/{script_name}/script-settings">client.workers.scripts.settings.<a href="./src/cloudflare/resources/workers/scripts/settings.py">get</a>(script_name, \*, account_id) -> <a href="./src/cloudflare/types/workers/script_setting.py">Optional</a></code>

### Deployments

Types:

```python
from cloudflare.types.workers.scripts import (
    Deployment,
    DeploymentCreateResponse,
    DeploymentGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/workers/scripts/{script_name}/deployments">client.workers.scripts.deployments.<a href="./src/cloudflare/resources/workers/scripts/deployments.py">create</a>(script_name, \*, account_id, \*\*<a href="src/cloudflare/types/workers/scripts/deployment_create_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/scripts/deployment_create_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/workers/scripts/{script_name}/deployments">client.workers.scripts.deployments.<a href="./src/cloudflare/resources/workers/scripts/deployments.py">get</a>(script_name, \*, account_id) -> <a href="./src/cloudflare/types/workers/scripts/deployment_get_response.py">Optional</a></code>

### Versions

Types:

```python
from cloudflare.types.workers.scripts import (
    VersionCreateResponse,
    VersionListResponse,
    VersionGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/workers/scripts/{script_name}/versions">client.workers.scripts.versions.<a href="./src/cloudflare/resources/workers/scripts/versions.py">create</a>(script_name, \*, account_id, \*\*<a href="src/cloudflare/types/workers/scripts/version_create_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/scripts/version_create_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/workers/scripts/{script_name}/versions">client.workers.scripts.versions.<a href="./src/cloudflare/resources/workers/scripts/versions.py">list</a>(script_name, \*, account_id, \*\*<a href="src/cloudflare/types/workers/scripts/version_list_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/scripts/version_list_response.py">SyncV4PagePagination[VersionListResponse]</a></code>
- <code title="get /accounts/{account_id}/workers/scripts/{script_name}/versions/{version_id}">client.workers.scripts.versions.<a href="./src/cloudflare/resources/workers/scripts/versions.py">get</a>(version_id, \*, account_id, script_name) -> <a href="./src/cloudflare/types/workers/scripts/version_get_response.py">Optional</a></code>

## AccountSettings

Types:

```python
from cloudflare.types.workers import AccountSettingUpdateResponse, AccountSettingGetResponse
```

Methods:

- <code title="put /accounts/{account_id}/workers/account-settings">client.workers.account_settings.<a href="./src/cloudflare/resources/workers/account_settings.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/workers/account_setting_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/account_setting_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/workers/account-settings">client.workers.account_settings.<a href="./src/cloudflare/resources/workers/account_settings.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/workers/account_setting_get_response.py">Optional</a></code>

## Domains

Types:

```python
from cloudflare.types.workers import Domain
```

Methods:

- <code title="put /accounts/{account_id}/workers/domains">client.workers.domains.<a href="./src/cloudflare/resources/workers/domains.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/workers/domain_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/domain.py">Optional</a></code>
- <code title="get /accounts/{account_id}/workers/domains">client.workers.domains.<a href="./src/cloudflare/resources/workers/domains.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/workers/domain_list_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/domain.py">SyncSinglePage[Domain]</a></code>
- <code title="delete /accounts/{account_id}/workers/domains/{domain_id}">client.workers.domains.<a href="./src/cloudflare/resources/workers/domains.py">delete</a>(domain_id, \*, account_id) -> None</code>
- <code title="get /accounts/{account_id}/workers/domains/{domain_id}">client.workers.domains.<a href="./src/cloudflare/resources/workers/domains.py">get</a>(domain_id, \*, account_id) -> <a href="./src/cloudflare/types/workers/domain.py">Optional</a></code>

## Subdomains

Types:

```python
from cloudflare.types.workers import SubdomainUpdateResponse, SubdomainGetResponse
```

Methods:

- <code title="put /accounts/{account_id}/workers/subdomain">client.workers.subdomains.<a href="./src/cloudflare/resources/workers/subdomains.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/workers/subdomain_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/subdomain_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/workers/subdomain">client.workers.subdomains.<a href="./src/cloudflare/resources/workers/subdomains.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/workers/subdomain_get_response.py">Optional</a></code>

# KV

## Namespaces

Types:

```python
from cloudflare.types.kv import Namespace, NamespaceUpdateResponse, NamespaceDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/storage/kv/namespaces">client.kv.namespaces.<a href="./src/cloudflare/resources/kv/namespaces/namespaces.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/kv/namespace_create_params.py">params</a>) -> <a href="./src/cloudflare/types/kv/namespace.py">Optional</a></code>
- <code title="put /accounts/{account_id}/storage/kv/namespaces/{namespace_id}">client.kv.namespaces.<a href="./src/cloudflare/resources/kv/namespaces/namespaces.py">update</a>(namespace_id, \*, account_id, \*\*<a href="src/cloudflare/types/kv/namespace_update_params.py">params</a>) -> <a href="./src/cloudflare/types/kv/namespace_update_response.py">object</a></code>
- <code title="get /accounts/{account_id}/storage/kv/namespaces">client.kv.namespaces.<a href="./src/cloudflare/resources/kv/namespaces/namespaces.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/kv/namespace_list_params.py">params</a>) -> <a href="./src/cloudflare/types/kv/namespace.py">SyncV4PagePaginationArray[Namespace]</a></code>
- <code title="delete /accounts/{account_id}/storage/kv/namespaces/{namespace_id}">client.kv.namespaces.<a href="./src/cloudflare/resources/kv/namespaces/namespaces.py">delete</a>(namespace_id, \*, account_id) -> <a href="./src/cloudflare/types/kv/namespace_delete_response.py">object</a></code>
- <code title="get /accounts/{account_id}/storage/kv/namespaces/{namespace_id}">client.kv.namespaces.<a href="./src/cloudflare/resources/kv/namespaces/namespaces.py">get</a>(namespace_id, \*, account_id) -> <a href="./src/cloudflare/types/kv/namespace.py">Optional</a></code>

### Bulk

Types:

```python
from cloudflare.types.kv.namespaces import BulkUpdateResponse, BulkDeleteResponse
```

Methods:

- <code title="put /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk">client.kv.namespaces.bulk.<a href="./src/cloudflare/resources/kv/namespaces/bulk.py">update</a>(namespace_id, \*, account_id, \*\*<a href="src/cloudflare/types/kv/namespaces/bulk_update_params.py">params</a>) -> <a href="./src/cloudflare/types/kv/namespaces/bulk_update_response.py">object</a></code>
- <code title="delete /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk">client.kv.namespaces.bulk.<a href="./src/cloudflare/resources/kv/namespaces/bulk.py">delete</a>(namespace_id, \*, account_id) -> <a href="./src/cloudflare/types/kv/namespaces/bulk_delete_response.py">object</a></code>

### Keys

Types:

```python
from cloudflare.types.kv.namespaces import Key
```

Methods:

- <code title="get /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/keys">client.kv.namespaces.keys.<a href="./src/cloudflare/resources/kv/namespaces/keys.py">list</a>(namespace_id, \*, account_id, \*\*<a href="src/cloudflare/types/kv/namespaces/key_list_params.py">params</a>) -> <a href="./src/cloudflare/types/kv/namespaces/key.py">SyncCursorLimitPagination[Key]</a></code>

### Metadata

Types:

```python
from cloudflare.types.kv.namespaces import MetadataGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/metadata/{key_name}">client.kv.namespaces.metadata.<a href="./src/cloudflare/resources/kv/namespaces/metadata.py">get</a>(key_name, \*, account_id, namespace_id) -> <a href="./src/cloudflare/types/kv/namespaces/metadata_get_response.py">Optional</a></code>

### Values

Types:

```python
from cloudflare.types.kv.namespaces import ValueUpdateResponse, ValueDeleteResponse
```

Methods:

- <code title="put /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}">client.kv.namespaces.values.<a href="./src/cloudflare/resources/kv/namespaces/values.py">update</a>(key_name, \*, account_id, namespace_id, \*\*<a href="src/cloudflare/types/kv/namespaces/value_update_params.py">params</a>) -> <a href="./src/cloudflare/types/kv/namespaces/value_update_response.py">object</a></code>
- <code title="delete /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}">client.kv.namespaces.values.<a href="./src/cloudflare/resources/kv/namespaces/values.py">delete</a>(key_name, \*, account_id, namespace_id) -> <a href="./src/cloudflare/types/kv/namespaces/value_delete_response.py">object</a></code>
- <code title="get /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}">client.kv.namespaces.values.<a href="./src/cloudflare/resources/kv/namespaces/values.py">get</a>(key_name, \*, account_id, namespace_id) -> BinaryAPIResponse</code>

# DurableObjects

## Namespaces

Types:

```python
from cloudflare.types.durable_objects import Namespace
```

Methods:

- <code title="get /accounts/{account_id}/workers/durable_objects/namespaces">client.durable_objects.namespaces.<a href="./src/cloudflare/resources/durable_objects/namespaces/namespaces.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/durable_objects/namespace.py">SyncSinglePage[Namespace]</a></code>

### Objects

Types:

```python
from cloudflare.types.durable_objects.namespaces import DurableObject
```

Methods:

- <code title="get /accounts/{account_id}/workers/durable_objects/namespaces/{id}/objects">client.durable_objects.namespaces.objects.<a href="./src/cloudflare/resources/durable_objects/namespaces/objects.py">list</a>(id, \*, account_id, \*\*<a href="src/cloudflare/types/durable_objects/namespaces/object_list_params.py">params</a>) -> <a href="./src/cloudflare/types/durable_objects/namespaces/durable_object.py">SyncCursorLimitPagination[DurableObject]</a></code>

# Queues

Types:

```python
from cloudflare.types.queues import Queue, QueueCreated, QueueUpdated, QueueDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/queues">client.queues.<a href="./src/cloudflare/resources/queues/queues.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/queues/queue_create_params.py">params</a>) -> <a href="./src/cloudflare/types/queues/queue_created.py">Optional</a></code>
- <code title="put /accounts/{account_id}/queues/{queue_id}">client.queues.<a href="./src/cloudflare/resources/queues/queues.py">update</a>(queue_id, \*, account_id, \*\*<a href="src/cloudflare/types/queues/queue_update_params.py">params</a>) -> <a href="./src/cloudflare/types/queues/queue_updated.py">Optional</a></code>
- <code title="get /accounts/{account_id}/queues">client.queues.<a href="./src/cloudflare/resources/queues/queues.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/queues/queue.py">SyncSinglePage[Queue]</a></code>
- <code title="delete /accounts/{account_id}/queues/{queue_id}">client.queues.<a href="./src/cloudflare/resources/queues/queues.py">delete</a>(queue_id, \*, account_id) -> <a href="./src/cloudflare/types/queues/queue_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/queues/{queue_id}">client.queues.<a href="./src/cloudflare/resources/queues/queues.py">get</a>(queue_id, \*, account_id) -> <a href="./src/cloudflare/types/queues/queue.py">Optional</a></code>

## Consumers

Types:

```python
from cloudflare.types.queues import (
    Consumer,
    ConsumerCreateResponse,
    ConsumerUpdateResponse,
    ConsumerDeleteResponse,
    ConsumerGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/queues/{queue_id}/consumers">client.queues.consumers.<a href="./src/cloudflare/resources/queues/consumers.py">create</a>(queue_id, \*, account_id, \*\*<a href="src/cloudflare/types/queues/consumer_create_params.py">params</a>) -> <a href="./src/cloudflare/types/queues/consumer_create_response.py">Optional</a></code>
- <code title="put /accounts/{account_id}/queues/{queue_id}/consumers/{consumer_id}">client.queues.consumers.<a href="./src/cloudflare/resources/queues/consumers.py">update</a>(consumer_id, \*, account_id, queue_id, \*\*<a href="src/cloudflare/types/queues/consumer_update_params.py">params</a>) -> <a href="./src/cloudflare/types/queues/consumer_update_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/queues/{queue_id}/consumers/{consumer_id}">client.queues.consumers.<a href="./src/cloudflare/resources/queues/consumers.py">delete</a>(consumer_id, \*, account_id, queue_id) -> <a href="./src/cloudflare/types/queues/consumer_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/queues/{queue_id}/consumers">client.queues.consumers.<a href="./src/cloudflare/resources/queues/consumers.py">get</a>(queue_id, \*, account_id) -> <a href="./src/cloudflare/types/queues/consumer_get_response.py">Optional</a></code>

## Messages

Types:

```python
from cloudflare.types.queues import MessageAckResponse, MessagePullResponse
```

Methods:

- <code title="post /accounts/{account_id}/queues/{queue_id}/messages/ack">client.queues.messages.<a href="./src/cloudflare/resources/queues/messages.py">ack</a>(queue_id, \*, account_id, \*\*<a href="src/cloudflare/types/queues/message_ack_params.py">params</a>) -> <a href="./src/cloudflare/types/queues/message_ack_response.py">Optional</a></code>
- <code title="post /accounts/{account_id}/queues/{queue_id}/messages/pull">client.queues.messages.<a href="./src/cloudflare/resources/queues/messages.py">pull</a>(queue_id, \*, account_id, \*\*<a href="src/cloudflare/types/queues/message_pull_params.py">params</a>) -> <a href="./src/cloudflare/types/queues/message_pull_response.py">Optional</a></code>

# APIGateway

## Configurations

Types:

```python
from cloudflare.types.api_gateway import Configuration, ConfigurationUpdateResponse
```

Methods:

- <code title="put /zones/{zone_id}/api_gateway/configuration">client.api_gateway.configurations.<a href="./src/cloudflare/resources/api_gateway/configurations.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/configuration_update_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/configuration_update_response.py">ConfigurationUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/api_gateway/configuration">client.api_gateway.configurations.<a href="./src/cloudflare/resources/api_gateway/configurations.py">get</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/configuration_get_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/configuration.py">Configuration</a></code>

## Discovery

Types:

```python
from cloudflare.types.api_gateway import DiscoveryOperation, DiscoveryGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/api_gateway/discovery">client.api_gateway.discovery.<a href="./src/cloudflare/resources/api_gateway/discovery/discovery.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/api_gateway/discovery_get_response.py">DiscoveryGetResponse</a></code>

### Operations

Types:

```python
from cloudflare.types.api_gateway.discovery import OperationEditResponse
```

Methods:

- <code title="get /zones/{zone_id}/api_gateway/discovery/operations">client.api_gateway.discovery.operations.<a href="./src/cloudflare/resources/api_gateway/discovery/operations.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/discovery/operation_list_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/discovery_operation.py">SyncV4PagePaginationArray[DiscoveryOperation]</a></code>
- <code title="patch /zones/{zone_id}/api_gateway/discovery/operations/{operation_id}">client.api_gateway.discovery.operations.<a href="./src/cloudflare/resources/api_gateway/discovery/operations.py">edit</a>(operation_id, \*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/discovery/operation_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/discovery/operation_edit_response.py">OperationEditResponse</a></code>

## Operations

Types:

```python
from cloudflare.types.api_gateway import (
    APIShield,
    OperationCreateResponse,
    OperationListResponse,
    OperationDeleteResponse,
    OperationGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/api_gateway/operations">client.api_gateway.operations.<a href="./src/cloudflare/resources/api_gateway/operations/operations.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/operation_create_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/operation_create_response.py">OperationCreateResponse</a></code>
- <code title="get /zones/{zone_id}/api_gateway/operations">client.api_gateway.operations.<a href="./src/cloudflare/resources/api_gateway/operations/operations.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/operation_list_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/operation_list_response.py">SyncV4PagePaginationArray[OperationListResponse]</a></code>
- <code title="delete /zones/{zone_id}/api_gateway/operations/{operation_id}">client.api_gateway.operations.<a href="./src/cloudflare/resources/api_gateway/operations/operations.py">delete</a>(operation_id, \*, zone_id) -> <a href="./src/cloudflare/types/api_gateway/operation_delete_response.py">OperationDeleteResponse</a></code>
- <code title="get /zones/{zone_id}/api_gateway/operations/{operation_id}">client.api_gateway.operations.<a href="./src/cloudflare/resources/api_gateway/operations/operations.py">get</a>(operation_id, \*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/operation_get_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/operation_get_response.py">OperationGetResponse</a></code>

### SchemaValidation

Types:

```python
from cloudflare.types.api_gateway.operations import (
    SettingsMultipleRequest,
    SchemaValidationUpdateResponse,
    SchemaValidationGetResponse,
)
```

Methods:

- <code title="put /zones/{zone_id}/api_gateway/operations/{operation_id}/schema_validation">client.api_gateway.operations.schema_validation.<a href="./src/cloudflare/resources/api_gateway/operations/schema_validation.py">update</a>(operation_id, \*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/operations/schema_validation_update_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/operations/schema_validation_update_response.py">SchemaValidationUpdateResponse</a></code>
- <code title="patch /zones/{zone_id}/api_gateway/operations/schema_validation">client.api_gateway.operations.schema_validation.<a href="./src/cloudflare/resources/api_gateway/operations/schema_validation.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/operations/schema_validation_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/operations/settings_multiple_request.py">SettingsMultipleRequest</a></code>
- <code title="get /zones/{zone_id}/api_gateway/operations/{operation_id}/schema_validation">client.api_gateway.operations.schema_validation.<a href="./src/cloudflare/resources/api_gateway/operations/schema_validation.py">get</a>(operation_id, \*, zone_id) -> <a href="./src/cloudflare/types/api_gateway/operations/schema_validation_get_response.py">SchemaValidationGetResponse</a></code>

## Schemas

Types:

```python
from cloudflare.types.api_gateway import SchemaListResponse
```

Methods:

- <code title="get /zones/{zone_id}/api_gateway/schemas">client.api_gateway.schemas.<a href="./src/cloudflare/resources/api_gateway/schemas.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/schema_list_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/schema_list_response.py">SchemaListResponse</a></code>

## Settings

Types:

```python
from cloudflare.types.api_gateway import Settings
```

### SchemaValidation

Methods:

- <code title="put /zones/{zone_id}/api_gateway/settings/schema_validation">client.api_gateway.settings.schema_validation.<a href="./src/cloudflare/resources/api_gateway/settings/schema_validation.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/settings/schema_validation_update_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/settings/settings.py">Settings</a></code>
- <code title="patch /zones/{zone_id}/api_gateway/settings/schema_validation">client.api_gateway.settings.schema_validation.<a href="./src/cloudflare/resources/api_gateway/settings/schema_validation.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/settings/schema_validation_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/settings/settings.py">Settings</a></code>
- <code title="get /zones/{zone_id}/api_gateway/settings/schema_validation">client.api_gateway.settings.schema_validation.<a href="./src/cloudflare/resources/api_gateway/settings/schema_validation.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/api_gateway/settings/settings.py">Settings</a></code>

## UserSchemas

Types:

```python
from cloudflare.types.api_gateway import (
    Message,
    PublicSchema,
    SchemaUpload,
    UserSchemaDeleteResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/api_gateway/user_schemas">client.api_gateway.user_schemas.<a href="./src/cloudflare/resources/api_gateway/user_schemas/user_schemas.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/user_schema_create_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/schema_upload.py">SchemaUpload</a></code>
- <code title="get /zones/{zone_id}/api_gateway/user_schemas">client.api_gateway.user_schemas.<a href="./src/cloudflare/resources/api_gateway/user_schemas/user_schemas.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/user_schema_list_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/public_schema.py">SyncV4PagePaginationArray[PublicSchema]</a></code>
- <code title="delete /zones/{zone_id}/api_gateway/user_schemas/{schema_id}">client.api_gateway.user_schemas.<a href="./src/cloudflare/resources/api_gateway/user_schemas/user_schemas.py">delete</a>(schema_id, \*, zone_id) -> <a href="./src/cloudflare/types/api_gateway/user_schema_delete_response.py">UserSchemaDeleteResponse</a></code>
- <code title="patch /zones/{zone_id}/api_gateway/user_schemas/{schema_id}">client.api_gateway.user_schemas.<a href="./src/cloudflare/resources/api_gateway/user_schemas/user_schemas.py">edit</a>(schema_id, \*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/user_schema_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/public_schema.py">PublicSchema</a></code>
- <code title="get /zones/{zone_id}/api_gateway/user_schemas/{schema_id}">client.api_gateway.user_schemas.<a href="./src/cloudflare/resources/api_gateway/user_schemas/user_schemas.py">get</a>(schema_id, \*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/user_schema_get_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/public_schema.py">PublicSchema</a></code>

### Operations

Types:

```python
from cloudflare.types.api_gateway.user_schemas import OperationListResponse
```

Methods:

- <code title="get /zones/{zone_id}/api_gateway/user_schemas/{schema_id}/operations">client.api_gateway.user_schemas.operations.<a href="./src/cloudflare/resources/api_gateway/user_schemas/operations.py">list</a>(schema_id, \*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/user_schemas/operation_list_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/user_schemas/operation_list_response.py">SyncV4PagePaginationArray[OperationListResponse]</a></code>

# ManagedHeaders

Types:

```python
from cloudflare.types.managed_headers import (
    RequestModel,
    ManagedHeaderListResponse,
    ManagedHeaderEditResponse,
)
```

Methods:

- <code title="get /zones/{zone_id}/managed_headers">client.managed_headers.<a href="./src/cloudflare/resources/managed_headers.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/managed_headers/managed_header_list_response.py">ManagedHeaderListResponse</a></code>
- <code title="patch /zones/{zone_id}/managed_headers">client.managed_headers.<a href="./src/cloudflare/resources/managed_headers.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/managed_headers/managed_header_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/managed_headers/managed_header_edit_response.py">ManagedHeaderEditResponse</a></code>

# PageShield

Types:

```python
from cloudflare.types.page_shield import Setting, PageShieldUpdateResponse
```

Methods:

- <code title="put /zones/{zone_id}/page_shield">client.page_shield.<a href="./src/cloudflare/resources/page_shield/page_shield.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/page_shield/page_shield_update_params.py">params</a>) -> <a href="./src/cloudflare/types/page_shield/page_shield_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/page_shield">client.page_shield.<a href="./src/cloudflare/resources/page_shield/page_shield.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/page_shield/setting.py">Optional</a></code>

## Policies

Types:

```python
from cloudflare.types.page_shield import (
    Policy,
    PolicyCreateResponse,
    PolicyUpdateResponse,
    PolicyListResponse,
    PolicyGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/page_shield/policies">client.page_shield.policies.<a href="./src/cloudflare/resources/page_shield/policies.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/page_shield/policy_create_params.py">params</a>) -> <a href="./src/cloudflare/types/page_shield/policy_create_response.py">Optional</a></code>
- <code title="put /zones/{zone_id}/page_shield/policies/{policy_id}">client.page_shield.policies.<a href="./src/cloudflare/resources/page_shield/policies.py">update</a>(policy_id, \*, zone_id, \*\*<a href="src/cloudflare/types/page_shield/policy_update_params.py">params</a>) -> <a href="./src/cloudflare/types/page_shield/policy_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/page_shield/policies">client.page_shield.policies.<a href="./src/cloudflare/resources/page_shield/policies.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/page_shield/policy_list_response.py">SyncSinglePage[PolicyListResponse]</a></code>
- <code title="delete /zones/{zone_id}/page_shield/policies/{policy_id}">client.page_shield.policies.<a href="./src/cloudflare/resources/page_shield/policies.py">delete</a>(policy_id, \*, zone_id) -> None</code>
- <code title="get /zones/{zone_id}/page_shield/policies/{policy_id}">client.page_shield.policies.<a href="./src/cloudflare/resources/page_shield/policies.py">get</a>(policy_id, \*, zone_id) -> <a href="./src/cloudflare/types/page_shield/policy_get_response.py">Optional</a></code>

## Connections

Types:

```python
from cloudflare.types.page_shield import Connection
```

Methods:

- <code title="get /zones/{zone_id}/page_shield/connections">client.page_shield.connections.<a href="./src/cloudflare/resources/page_shield/connections.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/page_shield/connection_list_params.py">params</a>) -> <a href="./src/cloudflare/types/page_shield/connection.py">SyncSinglePage[Connection]</a></code>
- <code title="get /zones/{zone_id}/page_shield/connections/{connection_id}">client.page_shield.connections.<a href="./src/cloudflare/resources/page_shield/connections.py">get</a>(connection_id, \*, zone_id) -> <a href="./src/cloudflare/types/page_shield/connection.py">Optional</a></code>

## Scripts

Types:

```python
from cloudflare.types.page_shield import Script, ScriptGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/page_shield/scripts">client.page_shield.scripts.<a href="./src/cloudflare/resources/page_shield/scripts.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/page_shield/script_list_params.py">params</a>) -> <a href="./src/cloudflare/types/page_shield/script.py">SyncSinglePage[Script]</a></code>
- <code title="get /zones/{zone_id}/page_shield/scripts/{script_id}">client.page_shield.scripts.<a href="./src/cloudflare/resources/page_shield/scripts.py">get</a>(script_id, \*, zone_id) -> <a href="./src/cloudflare/types/page_shield/script_get_response.py">Optional</a></code>

## Cookies

Types:

```python
from cloudflare.types.page_shield import CookieListResponse, CookieGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/page_shield/cookies">client.page_shield.cookies.<a href="./src/cloudflare/resources/page_shield/cookies.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/page_shield/cookie_list_params.py">params</a>) -> <a href="./src/cloudflare/types/page_shield/cookie_list_response.py">SyncSinglePage[CookieListResponse]</a></code>
- <code title="get /zones/{zone_id}/page_shield/cookies/{cookie_id}">client.page_shield.cookies.<a href="./src/cloudflare/resources/page_shield/cookies.py">get</a>(cookie_id, \*, zone_id) -> <a href="./src/cloudflare/types/page_shield/cookie_get_response.py">Optional</a></code>

# Rulesets

Types:

```python
from cloudflare.types.rulesets import (
    Kind,
    Phase,
    Ruleset,
    RulesetCreateResponse,
    RulesetUpdateResponse,
    RulesetListResponse,
    RulesetGetResponse,
)
```

Methods:

- <code title="post /{account_or_zone}/{account_or_zone_id}/rulesets">client.rulesets.<a href="./src/cloudflare/resources/rulesets/rulesets.py">create</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/rulesets/ruleset_create_params.py">params</a>) -> <a href="./src/cloudflare/types/rulesets/ruleset_create_response.py">RulesetCreateResponse</a></code>
- <code title="put /{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}">client.rulesets.<a href="./src/cloudflare/resources/rulesets/rulesets.py">update</a>(ruleset_id, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/rulesets/ruleset_update_params.py">params</a>) -> <a href="./src/cloudflare/types/rulesets/ruleset_update_response.py">RulesetUpdateResponse</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/rulesets">client.rulesets.<a href="./src/cloudflare/resources/rulesets/rulesets.py">list</a>(\*, account_id, zone_id) -> <a href="./src/cloudflare/types/rulesets/ruleset_list_response.py">SyncSinglePage[RulesetListResponse]</a></code>
- <code title="delete /{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}">client.rulesets.<a href="./src/cloudflare/resources/rulesets/rulesets.py">delete</a>(ruleset_id, \*, account_id, zone_id) -> None</code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}">client.rulesets.<a href="./src/cloudflare/resources/rulesets/rulesets.py">get</a>(ruleset_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/rulesets/ruleset_get_response.py">RulesetGetResponse</a></code>

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

- <code title="get /{account_or_zone}/{account_or_zone_id}/rulesets/phases/{ruleset_phase}/entrypoint/versions">client.rulesets.phases.versions.<a href="./src/cloudflare/resources/rulesets/phases/versions.py">list</a>(ruleset_phase, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/rulesets/phases/version_list_response.py">SyncSinglePage[VersionListResponse]</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/rulesets/phases/{ruleset_phase}/entrypoint/versions/{ruleset_version}">client.rulesets.phases.versions.<a href="./src/cloudflare/resources/rulesets/phases/versions.py">get</a>(ruleset_version, \*, ruleset_phase, account_id, zone_id) -> <a href="./src/cloudflare/types/rulesets/phases/version_get_response.py">VersionGetResponse</a></code>

## Rules

Types:

```python
from cloudflare.types.rulesets import (
    BlockRule,
    CompressResponseRule,
    DDoSDynamicRule,
    ExecuteRule,
    ForceConnectionCloseRule,
    LogCustomFieldRule,
    LogRule,
    Logging,
    ManagedChallengeRule,
    RedirectRule,
    RewriteRule,
    RewriteURIPart,
    RouteRule,
    RulesetRule,
    ScoreRule,
    ServeErrorRule,
    SetCacheSettingsRule,
    SetConfigRule,
    SkipRule,
    RuleCreateResponse,
    RuleDeleteResponse,
    RuleEditResponse,
)
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

- <code title="get /{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/versions">client.rulesets.versions.<a href="./src/cloudflare/resources/rulesets/versions/versions.py">list</a>(ruleset_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/rulesets/version_list_response.py">SyncSinglePage[VersionListResponse]</a></code>
- <code title="delete /{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/versions/{ruleset_version}">client.rulesets.versions.<a href="./src/cloudflare/resources/rulesets/versions/versions.py">delete</a>(ruleset_version, \*, ruleset_id, account_id, zone_id) -> None</code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/versions/{ruleset_version}">client.rulesets.versions.<a href="./src/cloudflare/resources/rulesets/versions/versions.py">get</a>(ruleset_version, \*, ruleset_id, account_id, zone_id) -> <a href="./src/cloudflare/types/rulesets/version_get_response.py">VersionGetResponse</a></code>

### ByTag

Types:

```python
from cloudflare.types.rulesets.versions import ByTagGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/rulesets/{ruleset_id}/versions/{ruleset_version}/by_tag/{rule_tag}">client.rulesets.versions.by_tag.<a href="./src/cloudflare/resources/rulesets/versions/by_tag.py">get</a>(rule_tag, \*, account_id, ruleset_id, ruleset_version) -> <a href="./src/cloudflare/types/rulesets/versions/by_tag_get_response.py">ByTagGetResponse</a></code>

# URLNormalization

Types:

```python
from cloudflare.types.url_normalization import (
    URLNormalizationUpdateResponse,
    URLNormalizationGetResponse,
)
```

Methods:

- <code title="put /zones/{zone_id}/url_normalization">client.url_normalization.<a href="./src/cloudflare/resources/url_normalization.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/url_normalization/url_normalization_update_params.py">params</a>) -> <a href="./src/cloudflare/types/url_normalization/url_normalization_update_response.py">URLNormalizationUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/url_normalization">client.url_normalization.<a href="./src/cloudflare/resources/url_normalization.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/url_normalization/url_normalization_get_response.py">URLNormalizationGetResponse</a></code>

# Spectrum

Types:

```python
from cloudflare.types.spectrum import DNS, EdgeIPs, OriginDNS, OriginPort
```

## Analytics

### Aggregates

#### Currents

Types:

```python
from cloudflare.types.spectrum.analytics.aggregates import CurrentGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/spectrum/analytics/aggregate/current">client.spectrum.analytics.aggregates.currents.<a href="./src/cloudflare/resources/spectrum/analytics/aggregates/currents.py">get</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/spectrum/analytics/aggregates/current_get_params.py">params</a>) -> <a href="./src/cloudflare/types/spectrum/analytics/aggregates/current_get_response.py">Optional</a></code>

### Events

Types:

```python
from cloudflare.types.spectrum.analytics import Dimension
```

#### Bytimes

Types:

```python
from cloudflare.types.spectrum.analytics.events import BytimeGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/spectrum/analytics/events/bytime">client.spectrum.analytics.events.bytimes.<a href="./src/cloudflare/resources/spectrum/analytics/events/bytimes.py">get</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/spectrum/analytics/events/bytime_get_params.py">params</a>) -> <a href="./src/cloudflare/types/spectrum/analytics/events/bytime_get_response.py">Optional</a></code>

#### Summaries

Types:

```python
from cloudflare.types.spectrum.analytics.events import SummaryGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/spectrum/analytics/events/summary">client.spectrum.analytics.events.summaries.<a href="./src/cloudflare/resources/spectrum/analytics/events/summaries.py">get</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/spectrum/analytics/events/summary_get_params.py">params</a>) -> <a href="./src/cloudflare/types/spectrum/analytics/events/summary_get_response.py">Optional</a></code>

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

- <code title="post /zones/{zone_id}/spectrum/apps">client.spectrum.apps.<a href="./src/cloudflare/resources/spectrum/apps.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/spectrum/app_create_params.py">params</a>) -> <a href="./src/cloudflare/types/spectrum/app_create_response.py">Optional</a></code>
- <code title="put /zones/{zone_id}/spectrum/apps/{app_id}">client.spectrum.apps.<a href="./src/cloudflare/resources/spectrum/apps.py">update</a>(app_id, \*, zone_id, \*\*<a href="src/cloudflare/types/spectrum/app_update_params.py">params</a>) -> <a href="./src/cloudflare/types/spectrum/app_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/spectrum/apps">client.spectrum.apps.<a href="./src/cloudflare/resources/spectrum/apps.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/spectrum/app_list_params.py">params</a>) -> <a href="./src/cloudflare/types/spectrum/app_list_response.py">Optional</a></code>
- <code title="delete /zones/{zone_id}/spectrum/apps/{app_id}">client.spectrum.apps.<a href="./src/cloudflare/resources/spectrum/apps.py">delete</a>(app_id, \*, zone_id) -> <a href="./src/cloudflare/types/spectrum/app_delete_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/spectrum/apps/{app_id}">client.spectrum.apps.<a href="./src/cloudflare/resources/spectrum/apps.py">get</a>(app_id, \*, zone_id) -> <a href="./src/cloudflare/types/spectrum/app_get_response.py">Optional</a></code>

# Addressing

## RegionalHostnames

Types:

```python
from cloudflare.types.addressing import (
    RegionalHostnameCreateResponse,
    RegionalHostnameListResponse,
    RegionalHostnameDeleteResponse,
    RegionalHostnameEditResponse,
    RegionalHostnameGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/addressing/regional_hostnames">client.addressing.regional_hostnames.<a href="./src/cloudflare/resources/addressing/regional_hostnames/regional_hostnames.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/addressing/regional_hostname_create_params.py">params</a>) -> <a href="./src/cloudflare/types/addressing/regional_hostname_create_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/addressing/regional_hostnames">client.addressing.regional_hostnames.<a href="./src/cloudflare/resources/addressing/regional_hostnames/regional_hostnames.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/addressing/regional_hostname_list_response.py">SyncSinglePage[RegionalHostnameListResponse]</a></code>
- <code title="delete /zones/{zone_id}/addressing/regional_hostnames/{hostname}">client.addressing.regional_hostnames.<a href="./src/cloudflare/resources/addressing/regional_hostnames/regional_hostnames.py">delete</a>(hostname, \*, zone_id) -> <a href="./src/cloudflare/types/addressing/regional_hostname_delete_response.py">RegionalHostnameDeleteResponse</a></code>
- <code title="patch /zones/{zone_id}/addressing/regional_hostnames/{hostname}">client.addressing.regional_hostnames.<a href="./src/cloudflare/resources/addressing/regional_hostnames/regional_hostnames.py">edit</a>(hostname, \*, zone_id, \*\*<a href="src/cloudflare/types/addressing/regional_hostname_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/addressing/regional_hostname_edit_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/addressing/regional_hostnames/{hostname}">client.addressing.regional_hostnames.<a href="./src/cloudflare/resources/addressing/regional_hostnames/regional_hostnames.py">get</a>(hostname, \*, zone_id) -> <a href="./src/cloudflare/types/addressing/regional_hostname_get_response.py">Optional</a></code>

### Regions

Types:

```python
from cloudflare.types.addressing.regional_hostnames import RegionListResponse
```

Methods:

- <code title="get /accounts/{account_id}/addressing/regional_hostnames/regions">client.addressing.regional_hostnames.regions.<a href="./src/cloudflare/resources/addressing/regional_hostnames/regions.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/addressing/regional_hostnames/region_list_response.py">SyncSinglePage[RegionListResponse]</a></code>

## Services

Types:

```python
from cloudflare.types.addressing import ServiceListResponse
```

Methods:

- <code title="get /accounts/{account_id}/addressing/services">client.addressing.services.<a href="./src/cloudflare/resources/addressing/services.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/addressing/service_list_response.py">SyncSinglePage[ServiceListResponse]</a></code>

## AddressMaps

Types:

```python
from cloudflare.types.addressing import (
    AddressMap,
    Kind,
    AddressMapCreateResponse,
    AddressMapDeleteResponse,
    AddressMapGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/addressing/address_maps">client.addressing.address_maps.<a href="./src/cloudflare/resources/addressing/address_maps/address_maps.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/addressing/address_map_create_params.py">params</a>) -> <a href="./src/cloudflare/types/addressing/address_map_create_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/addressing/address_maps">client.addressing.address_maps.<a href="./src/cloudflare/resources/addressing/address_maps/address_maps.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/addressing/address_map.py">SyncSinglePage[AddressMap]</a></code>
- <code title="delete /accounts/{account_id}/addressing/address_maps/{address_map_id}">client.addressing.address_maps.<a href="./src/cloudflare/resources/addressing/address_maps/address_maps.py">delete</a>(address_map_id, \*, account_id) -> <a href="./src/cloudflare/types/addressing/address_map_delete_response.py">AddressMapDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/addressing/address_maps/{address_map_id}">client.addressing.address_maps.<a href="./src/cloudflare/resources/addressing/address_maps/address_maps.py">edit</a>(address_map_id, \*, account_id, \*\*<a href="src/cloudflare/types/addressing/address_map_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/addressing/address_map.py">Optional</a></code>
- <code title="get /accounts/{account_id}/addressing/address_maps/{address_map_id}">client.addressing.address_maps.<a href="./src/cloudflare/resources/addressing/address_maps/address_maps.py">get</a>(address_map_id, \*, account_id) -> <a href="./src/cloudflare/types/addressing/address_map_get_response.py">Optional</a></code>

### Accounts

Types:

```python
from cloudflare.types.addressing.address_maps import AccountUpdateResponse, AccountDeleteResponse
```

Methods:

- <code title="put /accounts/{account_id}/addressing/address_maps/{address_map_id}/accounts/{account_id}">client.addressing.address_maps.accounts.<a href="./src/cloudflare/resources/addressing/address_maps/accounts.py">update</a>(address_map_id, \*, account_id, \*\*<a href="src/cloudflare/types/addressing/address_maps/account_update_params.py">params</a>) -> <a href="./src/cloudflare/types/addressing/address_maps/account_update_response.py">AccountUpdateResponse</a></code>
- <code title="delete /accounts/{account_id}/addressing/address_maps/{address_map_id}/accounts/{account_id}">client.addressing.address_maps.accounts.<a href="./src/cloudflare/resources/addressing/address_maps/accounts.py">delete</a>(address_map_id, \*, account_id) -> <a href="./src/cloudflare/types/addressing/address_maps/account_delete_response.py">AccountDeleteResponse</a></code>

### IPs

Types:

```python
from cloudflare.types.addressing.address_maps import IPUpdateResponse, IPDeleteResponse
```

Methods:

- <code title="put /accounts/{account_id}/addressing/address_maps/{address_map_id}/ips/{ip_address}">client.addressing.address_maps.ips.<a href="./src/cloudflare/resources/addressing/address_maps/ips.py">update</a>(ip_address, \*, account_id, address_map_id, \*\*<a href="src/cloudflare/types/addressing/address_maps/ip_update_params.py">params</a>) -> <a href="./src/cloudflare/types/addressing/address_maps/ip_update_response.py">IPUpdateResponse</a></code>
- <code title="delete /accounts/{account_id}/addressing/address_maps/{address_map_id}/ips/{ip_address}">client.addressing.address_maps.ips.<a href="./src/cloudflare/resources/addressing/address_maps/ips.py">delete</a>(ip_address, \*, account_id, address_map_id) -> <a href="./src/cloudflare/types/addressing/address_maps/ip_delete_response.py">IPDeleteResponse</a></code>

### Zones

Types:

```python
from cloudflare.types.addressing.address_maps import ZoneUpdateResponse, ZoneDeleteResponse
```

Methods:

- <code title="put /accounts/{account_id}/addressing/address_maps/{address_map_id}/zones/{zone_id}">client.addressing.address_maps.zones.<a href="./src/cloudflare/resources/addressing/address_maps/zones.py">update</a>(address_map_id, \*, zone_id, account_id, \*\*<a href="src/cloudflare/types/addressing/address_maps/zone_update_params.py">params</a>) -> <a href="./src/cloudflare/types/addressing/address_maps/zone_update_response.py">ZoneUpdateResponse</a></code>
- <code title="delete /accounts/{account_id}/addressing/address_maps/{address_map_id}/zones/{zone_id}">client.addressing.address_maps.zones.<a href="./src/cloudflare/resources/addressing/address_maps/zones.py">delete</a>(address_map_id, \*, zone_id, account_id) -> <a href="./src/cloudflare/types/addressing/address_maps/zone_delete_response.py">ZoneDeleteResponse</a></code>

## LOADocuments

Types:

```python
from cloudflare.types.addressing import LOADocumentCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/addressing/loa_documents">client.addressing.loa_documents.<a href="./src/cloudflare/resources/addressing/loa_documents/loa_documents.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/addressing/loa_document_create_params.py">params</a>) -> <a href="./src/cloudflare/types/addressing/loa_document_create_response.py">Optional</a></code>

### Downloads

Methods:

- <code title="get /accounts/{account_id}/addressing/loa_documents/{loa_document_id}/download">client.addressing.loa_documents.downloads.<a href="./src/cloudflare/resources/addressing/loa_documents/downloads.py">get</a>(loa_document_id, \*, account_id) -> BinaryAPIResponse</code>

## Prefixes

Types:

```python
from cloudflare.types.addressing import Prefix, PrefixDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/addressing/prefixes">client.addressing.prefixes.<a href="./src/cloudflare/resources/addressing/prefixes/prefixes.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/addressing/prefix_create_params.py">params</a>) -> <a href="./src/cloudflare/types/addressing/prefix.py">Optional</a></code>
- <code title="get /accounts/{account_id}/addressing/prefixes">client.addressing.prefixes.<a href="./src/cloudflare/resources/addressing/prefixes/prefixes.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/addressing/prefix.py">SyncSinglePage[Prefix]</a></code>
- <code title="delete /accounts/{account_id}/addressing/prefixes/{prefix_id}">client.addressing.prefixes.<a href="./src/cloudflare/resources/addressing/prefixes/prefixes.py">delete</a>(prefix_id, \*, account_id) -> <a href="./src/cloudflare/types/addressing/prefix_delete_response.py">PrefixDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/addressing/prefixes/{prefix_id}">client.addressing.prefixes.<a href="./src/cloudflare/resources/addressing/prefixes/prefixes.py">edit</a>(prefix_id, \*, account_id, \*\*<a href="src/cloudflare/types/addressing/prefix_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/addressing/prefix.py">Optional</a></code>
- <code title="get /accounts/{account_id}/addressing/prefixes/{prefix_id}">client.addressing.prefixes.<a href="./src/cloudflare/resources/addressing/prefixes/prefixes.py">get</a>(prefix_id, \*, account_id) -> <a href="./src/cloudflare/types/addressing/prefix.py">Optional</a></code>

### BGP

#### Bindings

Types:

```python
from cloudflare.types.addressing.prefixes.bgp import ServiceBinding, BindingDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings">client.addressing.prefixes.bgp.bindings.<a href="./src/cloudflare/resources/addressing/prefixes/bgp/bindings.py">create</a>(prefix_id, \*, account_id, \*\*<a href="src/cloudflare/types/addressing/prefixes/bgp/binding_create_params.py">params</a>) -> <a href="./src/cloudflare/types/addressing/prefixes/bgp/service_binding.py">Optional</a></code>
- <code title="get /accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings">client.addressing.prefixes.bgp.bindings.<a href="./src/cloudflare/resources/addressing/prefixes/bgp/bindings.py">list</a>(prefix_id, \*, account_id) -> <a href="./src/cloudflare/types/addressing/prefixes/bgp/service_binding.py">SyncSinglePage[ServiceBinding]</a></code>
- <code title="delete /accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings/{binding_id}">client.addressing.prefixes.bgp.bindings.<a href="./src/cloudflare/resources/addressing/prefixes/bgp/bindings.py">delete</a>(binding_id, \*, account_id, prefix_id) -> <a href="./src/cloudflare/types/addressing/prefixes/bgp/binding_delete_response.py">BindingDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings/{binding_id}">client.addressing.prefixes.bgp.bindings.<a href="./src/cloudflare/resources/addressing/prefixes/bgp/bindings.py">get</a>(binding_id, \*, account_id, prefix_id) -> <a href="./src/cloudflare/types/addressing/prefixes/bgp/service_binding.py">Optional</a></code>

#### Prefixes

Types:

```python
from cloudflare.types.addressing.prefixes.bgp import BGPPrefix
```

Methods:

- <code title="get /accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/prefixes">client.addressing.prefixes.bgp.prefixes.<a href="./src/cloudflare/resources/addressing/prefixes/bgp/prefixes.py">list</a>(prefix_id, \*, account_id) -> <a href="./src/cloudflare/types/addressing/prefixes/bgp/bgp_prefix.py">SyncSinglePage[BGPPrefix]</a></code>
- <code title="patch /accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/prefixes/{bgp_prefix_id}">client.addressing.prefixes.bgp.prefixes.<a href="./src/cloudflare/resources/addressing/prefixes/bgp/prefixes.py">edit</a>(bgp_prefix_id, \*, account_id, prefix_id, \*\*<a href="src/cloudflare/types/addressing/prefixes/bgp/prefix_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/addressing/prefixes/bgp/bgp_prefix.py">Optional</a></code>
- <code title="get /accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/prefixes/{bgp_prefix_id}">client.addressing.prefixes.bgp.prefixes.<a href="./src/cloudflare/resources/addressing/prefixes/bgp/prefixes.py">get</a>(bgp_prefix_id, \*, account_id, prefix_id) -> <a href="./src/cloudflare/types/addressing/prefixes/bgp/bgp_prefix.py">Optional</a></code>

#### Statuses

Types:

```python
from cloudflare.types.addressing.prefixes.bgp import StatusEditResponse, StatusGetResponse
```

Methods:

- <code title="patch /accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/status">client.addressing.prefixes.bgp.statuses.<a href="./src/cloudflare/resources/addressing/prefixes/bgp/statuses.py">edit</a>(prefix_id, \*, account_id, \*\*<a href="src/cloudflare/types/addressing/prefixes/bgp/status_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/addressing/prefixes/bgp/status_edit_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/status">client.addressing.prefixes.bgp.statuses.<a href="./src/cloudflare/resources/addressing/prefixes/bgp/statuses.py">get</a>(prefix_id, \*, account_id) -> <a href="./src/cloudflare/types/addressing/prefixes/bgp/status_get_response.py">Optional</a></code>

### Delegations

Types:

```python
from cloudflare.types.addressing.prefixes import Delegations, DelegationDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/addressing/prefixes/{prefix_id}/delegations">client.addressing.prefixes.delegations.<a href="./src/cloudflare/resources/addressing/prefixes/delegations.py">create</a>(prefix_id, \*, account_id, \*\*<a href="src/cloudflare/types/addressing/prefixes/delegation_create_params.py">params</a>) -> <a href="./src/cloudflare/types/addressing/prefixes/delegations.py">Optional</a></code>
- <code title="get /accounts/{account_id}/addressing/prefixes/{prefix_id}/delegations">client.addressing.prefixes.delegations.<a href="./src/cloudflare/resources/addressing/prefixes/delegations.py">list</a>(prefix_id, \*, account_id) -> <a href="./src/cloudflare/types/addressing/prefixes/delegations.py">SyncSinglePage[Delegations]</a></code>
- <code title="delete /accounts/{account_id}/addressing/prefixes/{prefix_id}/delegations/{delegation_id}">client.addressing.prefixes.delegations.<a href="./src/cloudflare/resources/addressing/prefixes/delegations.py">delete</a>(delegation_id, \*, account_id, prefix_id) -> <a href="./src/cloudflare/types/addressing/prefixes/delegation_delete_response.py">Optional</a></code>

# AuditLogs

Methods:

- <code title="get /accounts/{account_id}/audit_logs">client.audit_logs.<a href="./src/cloudflare/resources/audit_logs.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/audit_logs/audit_log_list_params.py">params</a>) -> <a href="./src/cloudflare/types/shared/audit_log.py">SyncV4PagePaginationArray[AuditLog]</a></code>

# Billing

## Profiles

Types:

```python
from cloudflare.types.billing import ProfileGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/billing/profile">client.billing.profiles.<a href="./src/cloudflare/resources/billing/profiles.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/billing/profile_get_response.py">ProfileGetResponse</a></code>

# BrandProtection

Types:

```python
from cloudflare.types.brand_protection import (
    Info,
    RuleMatch,
    ScanStatus,
    Submit,
    URLInfoModelResults,
)
```

Methods:

- <code title="post /accounts/{account_id}/brand-protection/submit">client.brand_protection.<a href="./src/cloudflare/resources/brand_protection.py">submit</a>(\*, account_id, \*\*<a href="src/cloudflare/types/brand_protection/brand_protection_submit_params.py">params</a>) -> <a href="./src/cloudflare/types/brand_protection/submit.py">Optional</a></code>
- <code title="get /accounts/{account_id}/brand-protection/url-info">client.brand_protection.<a href="./src/cloudflare/resources/brand_protection.py">url_info</a>(\*, account_id, \*\*<a href="src/cloudflare/types/brand_protection/brand_protection_url_info_params.py">params</a>) -> <a href="./src/cloudflare/types/brand_protection/info.py">Optional</a></code>

# Diagnostics

## Traceroutes

Types:

```python
from cloudflare.types.diagnostics import Traceroute, TracerouteCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/diagnostics/traceroute">client.diagnostics.traceroutes.<a href="./src/cloudflare/resources/diagnostics/traceroutes.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/diagnostics/traceroute_create_params.py">params</a>) -> <a href="./src/cloudflare/types/diagnostics/traceroute_create_response.py">Optional</a></code>

# Images

## V1

Types:

```python
from cloudflare.types.images import Image, V1ListResponse, V1DeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/images/v1">client.images.v1.<a href="./src/cloudflare/resources/images/v1/v1.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/images/v1_create_params.py">params</a>) -> <a href="./src/cloudflare/types/images/image.py">Image</a></code>
- <code title="get /accounts/{account_id}/images/v1">client.images.v1.<a href="./src/cloudflare/resources/images/v1/v1.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/images/v1_list_params.py">params</a>) -> <a href="./src/cloudflare/types/images/v1_list_response.py">SyncV4PagePagination[V1ListResponse]</a></code>
- <code title="delete /accounts/{account_id}/images/v1/{image_id}">client.images.v1.<a href="./src/cloudflare/resources/images/v1/v1.py">delete</a>(image_id, \*, account_id) -> <a href="./src/cloudflare/types/images/v1_delete_response.py">V1DeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/images/v1/{image_id}">client.images.v1.<a href="./src/cloudflare/resources/images/v1/v1.py">edit</a>(image_id, \*, account_id, \*\*<a href="src/cloudflare/types/images/v1_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/images/image.py">Image</a></code>
- <code title="get /accounts/{account_id}/images/v1/{image_id}">client.images.v1.<a href="./src/cloudflare/resources/images/v1/v1.py">get</a>(image_id, \*, account_id) -> <a href="./src/cloudflare/types/images/image.py">Image</a></code>

### Keys

Types:

```python
from cloudflare.types.images.v1 import Key, KeyUpdateResponse, KeyListResponse, KeyDeleteResponse
```

Methods:

- <code title="put /accounts/{account_id}/images/v1/keys/{signing_key_name}">client.images.v1.keys.<a href="./src/cloudflare/resources/images/v1/keys.py">update</a>(signing_key_name, \*, account_id) -> <a href="./src/cloudflare/types/images/v1/key_update_response.py">KeyUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/images/v1/keys">client.images.v1.keys.<a href="./src/cloudflare/resources/images/v1/keys.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/images/v1/key_list_response.py">KeyListResponse</a></code>
- <code title="delete /accounts/{account_id}/images/v1/keys/{signing_key_name}">client.images.v1.keys.<a href="./src/cloudflare/resources/images/v1/keys.py">delete</a>(signing_key_name, \*, account_id) -> <a href="./src/cloudflare/types/images/v1/key_delete_response.py">KeyDeleteResponse</a></code>

### Stats

Types:

```python
from cloudflare.types.images.v1 import Stat
```

Methods:

- <code title="get /accounts/{account_id}/images/v1/stats">client.images.v1.stats.<a href="./src/cloudflare/resources/images/v1/stats.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/images/v1/stat.py">Stat</a></code>

### Variants

Types:

```python
from cloudflare.types.images.v1 import (
    Variant,
    VariantCreateResponse,
    VariantDeleteResponse,
    VariantEditResponse,
    VariantGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/images/v1/variants">client.images.v1.variants.<a href="./src/cloudflare/resources/images/v1/variants.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/images/v1/variant_create_params.py">params</a>) -> <a href="./src/cloudflare/types/images/v1/variant_create_response.py">VariantCreateResponse</a></code>
- <code title="get /accounts/{account_id}/images/v1/variants">client.images.v1.variants.<a href="./src/cloudflare/resources/images/v1/variants.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/images/v1/variant.py">Variant</a></code>
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

Methods:

- <code title="get /accounts/{account_id}/intel/asn/{asn}">client.intel.asn.<a href="./src/cloudflare/resources/intel/asn/asn.py">get</a>(asn, \*, account_id) -> <a href="./src/cloudflare/types/shared/asn.py">Optional</a></code>

### Subnets

Types:

```python
from cloudflare.types.intel.asn import SubnetGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/intel/asn/{asn}/subnets">client.intel.asn.subnets.<a href="./src/cloudflare/resources/intel/asn/subnets.py">get</a>(asn, \*, account_id) -> <a href="./src/cloudflare/types/intel/asn/subnet_get_response.py">SubnetGetResponse</a></code>

## DNS

Types:

```python
from cloudflare.types.intel import DNS, DNSListResponse
```

Methods:

- <code title="get /accounts/{account_id}/intel/dns">client.intel.dns.<a href="./src/cloudflare/resources/intel/dns.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/intel/dns_list_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/dns_list_response.py">SyncV4PagePagination[DNSListResponse]</a></code>

## Domains

Types:

```python
from cloudflare.types.intel import Domain
```

Methods:

- <code title="get /accounts/{account_id}/intel/domain">client.intel.domains.<a href="./src/cloudflare/resources/intel/domains/domains.py">get</a>(\*, account_id, \*\*<a href="src/cloudflare/types/intel/domain_get_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/domain.py">Optional</a></code>

### Bulks

Types:

```python
from cloudflare.types.intel.domains import BulkGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/intel/domain/bulk">client.intel.domains.bulks.<a href="./src/cloudflare/resources/intel/domains/bulks.py">get</a>(\*, account_id, \*\*<a href="src/cloudflare/types/intel/domains/bulk_get_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/domains/bulk_get_response.py">Optional</a></code>

## DomainHistory

Types:

```python
from cloudflare.types.intel import DomainHistory, DomainHistoryGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/intel/domain-history">client.intel.domain_history.<a href="./src/cloudflare/resources/intel/domain_history.py">get</a>(\*, account_id, \*\*<a href="src/cloudflare/types/intel/domain_history_get_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/domain_history_get_response.py">Optional</a></code>

## IPs

Types:

```python
from cloudflare.types.intel import IP, IPGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/intel/ip">client.intel.ips.<a href="./src/cloudflare/resources/intel/ips.py">get</a>(\*, account_id, \*\*<a href="src/cloudflare/types/intel/ip_get_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/ip_get_response.py">Optional</a></code>

## IPLists

Types:

```python
from cloudflare.types.intel import IPList, IPListGetResponse
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
from cloudflare.types.intel import Whois, WhoisGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/intel/whois">client.intel.whois.<a href="./src/cloudflare/resources/intel/whois.py">get</a>(\*, account_id, \*\*<a href="src/cloudflare/types/intel/whois_get_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/whois_get_response.py">Optional</a></code>

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

- <code title="post /accounts/{account_id}/intel/indicator-feeds">client.intel.indicator_feeds.<a href="./src/cloudflare/resources/intel/indicator_feeds/indicator_feeds.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/intel/indicator_feed_create_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/indicator_feed_create_response.py">Optional</a></code>
- <code title="put /accounts/{account_id}/intel/indicator-feeds/{feed_id}">client.intel.indicator_feeds.<a href="./src/cloudflare/resources/intel/indicator_feeds/indicator_feeds.py">update</a>(feed_id, \*, account_id, \*\*<a href="src/cloudflare/types/intel/indicator_feed_update_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/indicator_feed_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/intel/indicator-feeds">client.intel.indicator_feeds.<a href="./src/cloudflare/resources/intel/indicator_feeds/indicator_feeds.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/intel/indicator_feed_list_response.py">SyncSinglePage[IndicatorFeedListResponse]</a></code>
- <code title="get /accounts/{account_id}/intel/indicator-feeds/{feed_id}/data">client.intel.indicator_feeds.<a href="./src/cloudflare/resources/intel/indicator_feeds/indicator_feeds.py">data</a>(feed_id, \*, account_id) -> str</code>
- <code title="get /accounts/{account_id}/intel/indicator-feeds/{feed_id}">client.intel.indicator_feeds.<a href="./src/cloudflare/resources/intel/indicator_feeds/indicator_feeds.py">get</a>(feed_id, \*, account_id) -> <a href="./src/cloudflare/types/intel/indicator_feed_get_response.py">Optional</a></code>

### Snapshots

Types:

```python
from cloudflare.types.intel.indicator_feeds import SnapshotUpdateResponse
```

Methods:

- <code title="put /accounts/{account_id}/intel/indicator-feeds/{feed_id}/snapshot">client.intel.indicator_feeds.snapshots.<a href="./src/cloudflare/resources/intel/indicator_feeds/snapshots.py">update</a>(feed_id, \*, account_id, \*\*<a href="src/cloudflare/types/intel/indicator_feeds/snapshot_update_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/indicator_feeds/snapshot_update_response.py">Optional</a></code>

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

- <code title="put /accounts/{account_id}/intel/indicator-feeds/permissions/add">client.intel.indicator_feeds.permissions.<a href="./src/cloudflare/resources/intel/indicator_feeds/permissions.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/intel/indicator_feeds/permission_create_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/indicator_feeds/permission_create_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/intel/indicator-feeds/permissions/view">client.intel.indicator_feeds.permissions.<a href="./src/cloudflare/resources/intel/indicator_feeds/permissions.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/intel/indicator_feeds/permission_list_response.py">Optional</a></code>
- <code title="put /accounts/{account_id}/intel/indicator-feeds/permissions/remove">client.intel.indicator_feeds.permissions.<a href="./src/cloudflare/resources/intel/indicator_feeds/permissions.py">delete</a>(\*, account_id, \*\*<a href="src/cloudflare/types/intel/indicator_feeds/permission_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/indicator_feeds/permission_delete_response.py">Optional</a></code>

### Downloads

Types:

```python
from cloudflare.types.intel.indicator_feeds import DownloadGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/intel/indicator_feeds/{feed_id}/download">client.intel.indicator_feeds.downloads.<a href="./src/cloudflare/resources/intel/indicator_feeds/downloads.py">get</a>(feed_id, \*, account_id) -> <a href="./src/cloudflare/types/intel/indicator_feeds/download_get_response.py">Optional</a></code>

## Sinkholes

Types:

```python
from cloudflare.types.intel import Sinkhole
```

Methods:

- <code title="get /accounts/{account_id}/intel/sinkholes">client.intel.sinkholes.<a href="./src/cloudflare/resources/intel/sinkholes.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/intel/sinkhole.py">SyncSinglePage[Sinkhole]</a></code>

## AttackSurfaceReport

### IssueTypes

Types:

```python
from cloudflare.types.intel.attack_surface_report import IssueTypeGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/intel/attack-surface-report/issue-types">client.intel.attack_surface_report.issue_types.<a href="./src/cloudflare/resources/intel/attack_surface_report/issue_types.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/intel/attack_surface_report/issue_type_get_response.py">Optional</a></code>

### Issues

Types:

```python
from cloudflare.types.intel.attack_surface_report import (
    IssueType,
    SeverityQueryParam,
    IssueListResponse,
    IssueClassResponse,
    IssueDismissResponse,
    IssueSeverityResponse,
    IssueTypeResponse,
)
```

Methods:

- <code title="get /accounts/{account_id}/intel/attack-surface-report/issues">client.intel.attack_surface_report.issues.<a href="./src/cloudflare/resources/intel/attack_surface_report/issues.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/intel/attack_surface_report/issue_list_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/attack_surface_report/issue_list_response.py">SyncV4PagePagination[IssueListResponse]</a></code>
- <code title="get /accounts/{account_id}/intel/attack-surface-report/issues/class">client.intel.attack*surface_report.issues.<a href="./src/cloudflare/resources/intel/attack_surface_report/issues.py">class*</a>(\*, account_id, \*\*<a href="src/cloudflare/types/intel/attack_surface_report/issue_class_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/attack_surface_report/issue_class_response.py">Optional</a></code>
- <code title="put /accounts/{account_id}/intel/attack-surface-report/{issue_id}/dismiss">client.intel.attack_surface_report.issues.<a href="./src/cloudflare/resources/intel/attack_surface_report/issues.py">dismiss</a>(issue_id, \*, account_id, \*\*<a href="src/cloudflare/types/intel/attack_surface_report/issue_dismiss_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/attack_surface_report/issue_dismiss_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/intel/attack-surface-report/issues/severity">client.intel.attack_surface_report.issues.<a href="./src/cloudflare/resources/intel/attack_surface_report/issues.py">severity</a>(\*, account_id, \*\*<a href="src/cloudflare/types/intel/attack_surface_report/issue_severity_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/attack_surface_report/issue_severity_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/intel/attack-surface-report/issues/type">client.intel.attack_surface_report.issues.<a href="./src/cloudflare/resources/intel/attack_surface_report/issues.py">type</a>(\*, account_id, \*\*<a href="src/cloudflare/types/intel/attack_surface_report/issue_type_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/attack_surface_report/issue_type_response.py">Optional</a></code>

# MagicTransit

Types:

```python
from cloudflare.types.magic_transit import HealthCheck, HealthCheckRate, HealthCheckType
```

## Apps

Types:

```python
from cloudflare.types.magic_transit import (
    AppCreateResponse,
    AppUpdateResponse,
    AppListResponse,
    AppDeleteResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/magic/apps">client.magic_transit.apps.<a href="./src/cloudflare/resources/magic_transit/apps.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/app_create_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/app_create_response.py">Optional</a></code>
- <code title="put /accounts/{account_id}/magic/apps/{account_app_id}">client.magic_transit.apps.<a href="./src/cloudflare/resources/magic_transit/apps.py">update</a>(account_app_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/app_update_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/app_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/magic/apps">client.magic_transit.apps.<a href="./src/cloudflare/resources/magic_transit/apps.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/magic_transit/app_list_response.py">SyncSinglePage[AppListResponse]</a></code>
- <code title="delete /accounts/{account_id}/magic/apps/{account_app_id}">client.magic_transit.apps.<a href="./src/cloudflare/resources/magic_transit/apps.py">delete</a>(account_app_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_transit/app_delete_response.py">Optional</a></code>

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

- <code title="put /accounts/{account_id}/magic/cf_interconnects/{cf_interconnect_id}">client.magic_transit.cf_interconnects.<a href="./src/cloudflare/resources/magic_transit/cf_interconnects.py">update</a>(cf_interconnect_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/cf_interconnect_update_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/cf_interconnect_update_response.py">CfInterconnectUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/magic/cf_interconnects">client.magic_transit.cf_interconnects.<a href="./src/cloudflare/resources/magic_transit/cf_interconnects.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/magic_transit/cf_interconnect_list_response.py">CfInterconnectListResponse</a></code>
- <code title="get /accounts/{account_id}/magic/cf_interconnects/{cf_interconnect_id}">client.magic_transit.cf_interconnects.<a href="./src/cloudflare/resources/magic_transit/cf_interconnects.py">get</a>(cf_interconnect_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_transit/cf_interconnect_get_response.py">CfInterconnectGetResponse</a></code>

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

- <code title="post /accounts/{account_id}/magic/gre_tunnels">client.magic_transit.gre_tunnels.<a href="./src/cloudflare/resources/magic_transit/gre_tunnels.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/gre_tunnel_create_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/gre_tunnel_create_response.py">GRETunnelCreateResponse</a></code>
- <code title="put /accounts/{account_id}/magic/gre_tunnels/{gre_tunnel_id}">client.magic_transit.gre_tunnels.<a href="./src/cloudflare/resources/magic_transit/gre_tunnels.py">update</a>(gre_tunnel_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/gre_tunnel_update_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/gre_tunnel_update_response.py">GRETunnelUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/magic/gre_tunnels">client.magic_transit.gre_tunnels.<a href="./src/cloudflare/resources/magic_transit/gre_tunnels.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/magic_transit/gre_tunnel_list_response.py">GRETunnelListResponse</a></code>
- <code title="delete /accounts/{account_id}/magic/gre_tunnels/{gre_tunnel_id}">client.magic_transit.gre_tunnels.<a href="./src/cloudflare/resources/magic_transit/gre_tunnels.py">delete</a>(gre_tunnel_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_transit/gre_tunnel_delete_response.py">GRETunnelDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/magic/gre_tunnels/{gre_tunnel_id}">client.magic_transit.gre_tunnels.<a href="./src/cloudflare/resources/magic_transit/gre_tunnels.py">get</a>(gre_tunnel_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_transit/gre_tunnel_get_response.py">GRETunnelGetResponse</a></code>

## IPSECTunnels

Types:

```python
from cloudflare.types.magic_transit import (
    PSKMetadata,
    IPSECTunnelCreateResponse,
    IPSECTunnelUpdateResponse,
    IPSECTunnelListResponse,
    IPSECTunnelDeleteResponse,
    IPSECTunnelGetResponse,
    IPSECTunnelPSKGenerateResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/magic/ipsec_tunnels">client.magic_transit.ipsec_tunnels.<a href="./src/cloudflare/resources/magic_transit/ipsec_tunnels.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/ipsec_tunnel_create_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/ipsec_tunnel_create_response.py">IPSECTunnelCreateResponse</a></code>
- <code title="put /accounts/{account_id}/magic/ipsec_tunnels/{ipsec_tunnel_id}">client.magic_transit.ipsec_tunnels.<a href="./src/cloudflare/resources/magic_transit/ipsec_tunnels.py">update</a>(ipsec_tunnel_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/ipsec_tunnel_update_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/ipsec_tunnel_update_response.py">IPSECTunnelUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/magic/ipsec_tunnels">client.magic_transit.ipsec_tunnels.<a href="./src/cloudflare/resources/magic_transit/ipsec_tunnels.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/magic_transit/ipsec_tunnel_list_response.py">IPSECTunnelListResponse</a></code>
- <code title="delete /accounts/{account_id}/magic/ipsec_tunnels/{ipsec_tunnel_id}">client.magic_transit.ipsec_tunnels.<a href="./src/cloudflare/resources/magic_transit/ipsec_tunnels.py">delete</a>(ipsec_tunnel_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_transit/ipsec_tunnel_delete_response.py">IPSECTunnelDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/magic/ipsec_tunnels/{ipsec_tunnel_id}">client.magic_transit.ipsec_tunnels.<a href="./src/cloudflare/resources/magic_transit/ipsec_tunnels.py">get</a>(ipsec_tunnel_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_transit/ipsec_tunnel_get_response.py">IPSECTunnelGetResponse</a></code>
- <code title="post /accounts/{account_id}/magic/ipsec_tunnels/{ipsec_tunnel_id}/psk_generate">client.magic_transit.ipsec_tunnels.<a href="./src/cloudflare/resources/magic_transit/ipsec_tunnels.py">psk_generate</a>(ipsec_tunnel_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/ipsec_tunnel_psk_generate_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/ipsec_tunnel_psk_generate_response.py">IPSECTunnelPSKGenerateResponse</a></code>

## Routes

Types:

```python
from cloudflare.types.magic_transit import (
    Scope,
    RouteCreateResponse,
    RouteUpdateResponse,
    RouteListResponse,
    RouteDeleteResponse,
    RouteEmptyResponse,
    RouteGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/magic/routes">client.magic_transit.routes.<a href="./src/cloudflare/resources/magic_transit/routes.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/route_create_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/route_create_response.py">RouteCreateResponse</a></code>
- <code title="put /accounts/{account_id}/magic/routes/{route_id}">client.magic_transit.routes.<a href="./src/cloudflare/resources/magic_transit/routes.py">update</a>(route_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/route_update_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/route_update_response.py">RouteUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/magic/routes">client.magic_transit.routes.<a href="./src/cloudflare/resources/magic_transit/routes.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/magic_transit/route_list_response.py">RouteListResponse</a></code>
- <code title="delete /accounts/{account_id}/magic/routes/{route_id}">client.magic_transit.routes.<a href="./src/cloudflare/resources/magic_transit/routes.py">delete</a>(route_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_transit/route_delete_response.py">RouteDeleteResponse</a></code>
- <code title="delete /accounts/{account_id}/magic/routes">client.magic_transit.routes.<a href="./src/cloudflare/resources/magic_transit/routes.py">empty</a>(\*, account_id) -> <a href="./src/cloudflare/types/magic_transit/route_empty_response.py">RouteEmptyResponse</a></code>
- <code title="get /accounts/{account_id}/magic/routes/{route_id}">client.magic_transit.routes.<a href="./src/cloudflare/resources/magic_transit/routes.py">get</a>(route_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_transit/route_get_response.py">RouteGetResponse</a></code>

## Sites

Types:

```python
from cloudflare.types.magic_transit import Site, SiteLocation
```

Methods:

- <code title="post /accounts/{account_id}/magic/sites">client.magic_transit.sites.<a href="./src/cloudflare/resources/magic_transit/sites/sites.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/site_create_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/site.py">Site</a></code>
- <code title="put /accounts/{account_id}/magic/sites/{site_id}">client.magic_transit.sites.<a href="./src/cloudflare/resources/magic_transit/sites/sites.py">update</a>(site_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/site_update_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/site.py">Site</a></code>
- <code title="get /accounts/{account_id}/magic/sites">client.magic_transit.sites.<a href="./src/cloudflare/resources/magic_transit/sites/sites.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/site_list_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/site.py">SyncSinglePage[Site]</a></code>
- <code title="delete /accounts/{account_id}/magic/sites/{site_id}">client.magic_transit.sites.<a href="./src/cloudflare/resources/magic_transit/sites/sites.py">delete</a>(site_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_transit/site.py">Site</a></code>
- <code title="patch /accounts/{account_id}/magic/sites/{site_id}">client.magic_transit.sites.<a href="./src/cloudflare/resources/magic_transit/sites/sites.py">edit</a>(site_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/site_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/site.py">Site</a></code>
- <code title="get /accounts/{account_id}/magic/sites/{site_id}">client.magic_transit.sites.<a href="./src/cloudflare/resources/magic_transit/sites/sites.py">get</a>(site_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_transit/site.py">Site</a></code>

### ACLs

Types:

```python
from cloudflare.types.magic_transit.sites import ACL, ACLConfiguration, AllowedProtocol, Subnet
```

Methods:

- <code title="post /accounts/{account_id}/magic/sites/{site_id}/acls">client.magic_transit.sites.acls.<a href="./src/cloudflare/resources/magic_transit/sites/acls.py">create</a>(site_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/sites/acl_create_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/sites/acl.py">ACL</a></code>
- <code title="put /accounts/{account_id}/magic/sites/{site_id}/acls/{acl_id}">client.magic_transit.sites.acls.<a href="./src/cloudflare/resources/magic_transit/sites/acls.py">update</a>(acl_id, \*, account_id, site_id, \*\*<a href="src/cloudflare/types/magic_transit/sites/acl_update_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/sites/acl.py">ACL</a></code>
- <code title="get /accounts/{account_id}/magic/sites/{site_id}/acls">client.magic_transit.sites.acls.<a href="./src/cloudflare/resources/magic_transit/sites/acls.py">list</a>(site_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_transit/sites/acl.py">SyncSinglePage[ACL]</a></code>
- <code title="delete /accounts/{account_id}/magic/sites/{site_id}/acls/{acl_id}">client.magic_transit.sites.acls.<a href="./src/cloudflare/resources/magic_transit/sites/acls.py">delete</a>(acl_id, \*, account_id, site_id) -> <a href="./src/cloudflare/types/magic_transit/sites/acl.py">ACL</a></code>
- <code title="patch /accounts/{account_id}/magic/sites/{site_id}/acls/{acl_id}">client.magic_transit.sites.acls.<a href="./src/cloudflare/resources/magic_transit/sites/acls.py">edit</a>(acl_id, \*, account_id, site_id, \*\*<a href="src/cloudflare/types/magic_transit/sites/acl_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/sites/acl.py">ACL</a></code>
- <code title="get /accounts/{account_id}/magic/sites/{site_id}/acls/{acl_id}">client.magic_transit.sites.acls.<a href="./src/cloudflare/resources/magic_transit/sites/acls.py">get</a>(acl_id, \*, account_id, site_id) -> <a href="./src/cloudflare/types/magic_transit/sites/acl.py">ACL</a></code>

### LANs

Types:

```python
from cloudflare.types.magic_transit.sites import (
    DHCPRelay,
    DHCPServer,
    LAN,
    LANStaticAddressing,
    Nat,
    RoutedSubnet,
    LANCreateResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/magic/sites/{site_id}/lans">client.magic_transit.sites.lans.<a href="./src/cloudflare/resources/magic_transit/sites/lans.py">create</a>(site_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/sites/lan_create_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/sites/lan_create_response.py">LANCreateResponse</a></code>
- <code title="put /accounts/{account_id}/magic/sites/{site_id}/lans/{lan_id}">client.magic_transit.sites.lans.<a href="./src/cloudflare/resources/magic_transit/sites/lans.py">update</a>(lan_id, \*, account_id, site_id, \*\*<a href="src/cloudflare/types/magic_transit/sites/lan_update_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/sites/lan.py">LAN</a></code>
- <code title="get /accounts/{account_id}/magic/sites/{site_id}/lans">client.magic_transit.sites.lans.<a href="./src/cloudflare/resources/magic_transit/sites/lans.py">list</a>(site_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_transit/sites/lan.py">SyncSinglePage[LAN]</a></code>
- <code title="delete /accounts/{account_id}/magic/sites/{site_id}/lans/{lan_id}">client.magic_transit.sites.lans.<a href="./src/cloudflare/resources/magic_transit/sites/lans.py">delete</a>(lan_id, \*, account_id, site_id) -> <a href="./src/cloudflare/types/magic_transit/sites/lan.py">LAN</a></code>
- <code title="patch /accounts/{account_id}/magic/sites/{site_id}/lans/{lan_id}">client.magic_transit.sites.lans.<a href="./src/cloudflare/resources/magic_transit/sites/lans.py">edit</a>(lan_id, \*, account_id, site_id, \*\*<a href="src/cloudflare/types/magic_transit/sites/lan_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/sites/lan.py">LAN</a></code>
- <code title="get /accounts/{account_id}/magic/sites/{site_id}/lans/{lan_id}">client.magic_transit.sites.lans.<a href="./src/cloudflare/resources/magic_transit/sites/lans.py">get</a>(lan_id, \*, account_id, site_id) -> <a href="./src/cloudflare/types/magic_transit/sites/lan.py">LAN</a></code>

### WANs

Types:

```python
from cloudflare.types.magic_transit.sites import WAN, WANStaticAddressing, WANCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/magic/sites/{site_id}/wans">client.magic_transit.sites.wans.<a href="./src/cloudflare/resources/magic_transit/sites/wans.py">create</a>(site_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/sites/wan_create_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/sites/wan_create_response.py">WANCreateResponse</a></code>
- <code title="put /accounts/{account_id}/magic/sites/{site_id}/wans/{wan_id}">client.magic_transit.sites.wans.<a href="./src/cloudflare/resources/magic_transit/sites/wans.py">update</a>(wan_id, \*, account_id, site_id, \*\*<a href="src/cloudflare/types/magic_transit/sites/wan_update_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/sites/wan.py">WAN</a></code>
- <code title="get /accounts/{account_id}/magic/sites/{site_id}/wans">client.magic_transit.sites.wans.<a href="./src/cloudflare/resources/magic_transit/sites/wans.py">list</a>(site_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_transit/sites/wan.py">SyncSinglePage[WAN]</a></code>
- <code title="delete /accounts/{account_id}/magic/sites/{site_id}/wans/{wan_id}">client.magic_transit.sites.wans.<a href="./src/cloudflare/resources/magic_transit/sites/wans.py">delete</a>(wan_id, \*, account_id, site_id) -> <a href="./src/cloudflare/types/magic_transit/sites/wan.py">WAN</a></code>
- <code title="patch /accounts/{account_id}/magic/sites/{site_id}/wans/{wan_id}">client.magic_transit.sites.wans.<a href="./src/cloudflare/resources/magic_transit/sites/wans.py">edit</a>(wan_id, \*, account_id, site_id, \*\*<a href="src/cloudflare/types/magic_transit/sites/wan_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/sites/wan.py">WAN</a></code>
- <code title="get /accounts/{account_id}/magic/sites/{site_id}/wans/{wan_id}">client.magic_transit.sites.wans.<a href="./src/cloudflare/resources/magic_transit/sites/wans.py">get</a>(wan_id, \*, account_id, site_id) -> <a href="./src/cloudflare/types/magic_transit/sites/wan.py">WAN</a></code>

## Connectors

Types:

```python
from cloudflare.types.magic_transit import (
    ConnectorUpdateResponse,
    ConnectorListResponse,
    ConnectorEditResponse,
    ConnectorGetResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/magic/connectors/{connector_id}">client.magic_transit.connectors.<a href="./src/cloudflare/resources/magic_transit/connectors.py">update</a>(connector_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/connector_update_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/connector_update_response.py">ConnectorUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/magic/connectors">client.magic_transit.connectors.<a href="./src/cloudflare/resources/magic_transit/connectors.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/magic_transit/connector_list_response.py">SyncSinglePage[ConnectorListResponse]</a></code>
- <code title="patch /accounts/{account_id}/magic/connectors/{connector_id}">client.magic_transit.connectors.<a href="./src/cloudflare/resources/magic_transit/connectors.py">edit</a>(connector_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/connector_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/connector_edit_response.py">ConnectorEditResponse</a></code>
- <code title="get /accounts/{account_id}/magic/connectors/{connector_id}">client.magic_transit.connectors.<a href="./src/cloudflare/resources/magic_transit/connectors.py">get</a>(connector_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_transit/connector_get_response.py">ConnectorGetResponse</a></code>

# MagicNetworkMonitoring

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

- <code title="post /accounts/{account_id}/mnm/rules">client.magic_network_monitoring.rules.<a href="./src/cloudflare/resources/magic_network_monitoring/rules/rules.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/magic_network_monitoring/rule_create_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_network_monitoring/magic_network_monitoring_rule.py">Optional</a></code>
- <code title="put /accounts/{account_id}/mnm/rules">client.magic_network_monitoring.rules.<a href="./src/cloudflare/resources/magic_network_monitoring/rules/rules.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/magic_network_monitoring/rule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_network_monitoring/magic_network_monitoring_rule.py">Optional</a></code>
- <code title="get /accounts/{account_id}/mnm/rules">client.magic_network_monitoring.rules.<a href="./src/cloudflare/resources/magic_network_monitoring/rules/rules.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/magic_network_monitoring/magic_network_monitoring_rule.py">SyncSinglePage[Optional]</a></code>
- <code title="delete /accounts/{account_id}/mnm/rules/{rule_id}">client.magic_network_monitoring.rules.<a href="./src/cloudflare/resources/magic_network_monitoring/rules/rules.py">delete</a>(rule_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_network_monitoring/magic_network_monitoring_rule.py">Optional</a></code>
- <code title="patch /accounts/{account_id}/mnm/rules/{rule_id}">client.magic_network_monitoring.rules.<a href="./src/cloudflare/resources/magic_network_monitoring/rules/rules.py">edit</a>(rule_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_network_monitoring/rule_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_network_monitoring/magic_network_monitoring_rule.py">Optional</a></code>
- <code title="get /accounts/{account_id}/mnm/rules/{rule_id}">client.magic_network_monitoring.rules.<a href="./src/cloudflare/resources/magic_network_monitoring/rules/rules.py">get</a>(rule_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_network_monitoring/magic_network_monitoring_rule.py">Optional</a></code>

### Advertisements

Types:

```python
from cloudflare.types.magic_network_monitoring.rules import Advertisement
```

Methods:

- <code title="patch /accounts/{account_id}/mnm/rules/{rule_id}/advertisement">client.magic_network_monitoring.rules.advertisements.<a href="./src/cloudflare/resources/magic_network_monitoring/rules/advertisements.py">edit</a>(rule_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_network_monitoring/rules/advertisement_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_network_monitoring/rules/advertisement.py">Optional</a></code>

# MTLSCertificates

Types:

```python
from cloudflare.types.mtls_certificates import MTLSCertificate, MTLSCertificateCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/mtls_certificates">client.mtls_certificates.<a href="./src/cloudflare/resources/mtls_certificates/mtls_certificates.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/mtls_certificates/mtls_certificate_create_params.py">params</a>) -> <a href="./src/cloudflare/types/mtls_certificates/mtls_certificate_create_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/mtls_certificates">client.mtls_certificates.<a href="./src/cloudflare/resources/mtls_certificates/mtls_certificates.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/mtls_certificates/mtls_certificate.py">SyncSinglePage[MTLSCertificate]</a></code>
- <code title="delete /accounts/{account_id}/mtls_certificates/{mtls_certificate_id}">client.mtls_certificates.<a href="./src/cloudflare/resources/mtls_certificates/mtls_certificates.py">delete</a>(mtls_certificate_id, \*, account_id) -> <a href="./src/cloudflare/types/mtls_certificates/mtls_certificate.py">Optional</a></code>
- <code title="get /accounts/{account_id}/mtls_certificates/{mtls_certificate_id}">client.mtls_certificates.<a href="./src/cloudflare/resources/mtls_certificates/mtls_certificates.py">get</a>(mtls_certificate_id, \*, account_id) -> <a href="./src/cloudflare/types/mtls_certificates/mtls_certificate.py">Optional</a></code>

## Associations

Types:

```python
from cloudflare.types.mtls_certificates import CertificateAsssociation, AssociationGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/mtls_certificates/{mtls_certificate_id}/associations">client.mtls_certificates.associations.<a href="./src/cloudflare/resources/mtls_certificates/associations.py">get</a>(mtls_certificate_id, \*, account_id) -> <a href="./src/cloudflare/types/mtls_certificates/association_get_response.py">Optional</a></code>

# Pages

## Projects

Types:

```python
from cloudflare.types.pages import (
    Deployment,
    Project,
    Stage,
    ProjectDeleteResponse,
    ProjectPurgeBuildCacheResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/pages/projects">client.pages.projects.<a href="./src/cloudflare/resources/pages/projects/projects.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/pages/project_create_params.py">params</a>) -> <a href="./src/cloudflare/types/pages/project.py">Project</a></code>
- <code title="get /accounts/{account_id}/pages/projects">client.pages.projects.<a href="./src/cloudflare/resources/pages/projects/projects.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/pages/deployment.py">SyncSinglePage[Deployment]</a></code>
- <code title="delete /accounts/{account_id}/pages/projects/{project_name}">client.pages.projects.<a href="./src/cloudflare/resources/pages/projects/projects.py">delete</a>(project_name, \*, account_id) -> <a href="./src/cloudflare/types/pages/project_delete_response.py">object</a></code>
- <code title="patch /accounts/{account_id}/pages/projects/{project_name}">client.pages.projects.<a href="./src/cloudflare/resources/pages/projects/projects.py">edit</a>(project_name, \*, account_id, \*\*<a href="src/cloudflare/types/pages/project_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/pages/project.py">Project</a></code>
- <code title="get /accounts/{account_id}/pages/projects/{project_name}">client.pages.projects.<a href="./src/cloudflare/resources/pages/projects/projects.py">get</a>(project_name, \*, account_id) -> <a href="./src/cloudflare/types/pages/project.py">Project</a></code>
- <code title="post /accounts/{account_id}/pages/projects/{project_name}/purge_build_cache">client.pages.projects.<a href="./src/cloudflare/resources/pages/projects/projects.py">purge_build_cache</a>(project_name, \*, account_id) -> <a href="./src/cloudflare/types/pages/project_purge_build_cache_response.py">object</a></code>

### Deployments

Types:

```python
from cloudflare.types.pages.projects import DeploymentDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/pages/projects/{project_name}/deployments">client.pages.projects.deployments.<a href="./src/cloudflare/resources/pages/projects/deployments/deployments.py">create</a>(project_name, \*, account_id, \*\*<a href="src/cloudflare/types/pages/projects/deployment_create_params.py">params</a>) -> <a href="./src/cloudflare/types/pages/deployment.py">Deployment</a></code>
- <code title="get /accounts/{account_id}/pages/projects/{project_name}/deployments">client.pages.projects.deployments.<a href="./src/cloudflare/resources/pages/projects/deployments/deployments.py">list</a>(project_name, \*, account_id, \*\*<a href="src/cloudflare/types/pages/projects/deployment_list_params.py">params</a>) -> <a href="./src/cloudflare/types/pages/deployment.py">SyncSinglePage[Deployment]</a></code>
- <code title="delete /accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}">client.pages.projects.deployments.<a href="./src/cloudflare/resources/pages/projects/deployments/deployments.py">delete</a>(deployment_id, \*, account_id, project_name) -> <a href="./src/cloudflare/types/pages/projects/deployment_delete_response.py">object</a></code>
- <code title="get /accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}">client.pages.projects.deployments.<a href="./src/cloudflare/resources/pages/projects/deployments/deployments.py">get</a>(deployment_id, \*, account_id, project_name) -> <a href="./src/cloudflare/types/pages/deployment.py">Deployment</a></code>
- <code title="post /accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}/retry">client.pages.projects.deployments.<a href="./src/cloudflare/resources/pages/projects/deployments/deployments.py">retry</a>(deployment_id, \*, account_id, project_name, \*\*<a href="src/cloudflare/types/pages/projects/deployment_retry_params.py">params</a>) -> <a href="./src/cloudflare/types/pages/deployment.py">Deployment</a></code>
- <code title="post /accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}/rollback">client.pages.projects.deployments.<a href="./src/cloudflare/resources/pages/projects/deployments/deployments.py">rollback</a>(deployment_id, \*, account_id, project_name, \*\*<a href="src/cloudflare/types/pages/projects/deployment_rollback_params.py">params</a>) -> <a href="./src/cloudflare/types/pages/deployment.py">Deployment</a></code>

#### History

##### Logs

Types:

```python
from cloudflare.types.pages.projects.deployments.history import LogGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}/history/logs">client.pages.projects.deployments.history.logs.<a href="./src/cloudflare/resources/pages/projects/deployments/history/logs.py">get</a>(deployment_id, \*, account_id, project_name) -> <a href="./src/cloudflare/types/pages/projects/deployments/history/log_get_response.py">LogGetResponse</a></code>

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
- <code title="get /accounts/{account_id}/pages/projects/{project_name}/domains">client.pages.projects.domains.<a href="./src/cloudflare/resources/pages/projects/domains.py">list</a>(project_name, \*, account_id) -> <a href="./src/cloudflare/types/pages/projects/domain_list_response.py">SyncSinglePage[DomainListResponse]</a></code>
- <code title="delete /accounts/{account_id}/pages/projects/{project_name}/domains/{domain_name}">client.pages.projects.domains.<a href="./src/cloudflare/resources/pages/projects/domains.py">delete</a>(domain_name, \*, account_id, project_name) -> <a href="./src/cloudflare/types/pages/projects/domain_delete_response.py">object</a></code>
- <code title="patch /accounts/{account_id}/pages/projects/{project_name}/domains/{domain_name}">client.pages.projects.domains.<a href="./src/cloudflare/resources/pages/projects/domains.py">edit</a>(domain_name, \*, account_id, project_name, \*\*<a href="src/cloudflare/types/pages/projects/domain_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/pages/projects/domain_edit_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/pages/projects/{project_name}/domains/{domain_name}">client.pages.projects.domains.<a href="./src/cloudflare/resources/pages/projects/domains.py">get</a>(domain_name, \*, account_id, project_name) -> <a href="./src/cloudflare/types/pages/projects/domain_get_response.py">Optional</a></code>

# PCAPs

Types:

```python
from cloudflare.types.pcaps import (
    PCAP,
    PCAPFilter,
    PCAPCreateResponse,
    PCAPListResponse,
    PCAPGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/pcaps">client.pcaps.<a href="./src/cloudflare/resources/pcaps/pcaps.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/pcaps/pcap_create_params.py">params</a>) -> <a href="./src/cloudflare/types/pcaps/pcap_create_response.py">PCAPCreateResponse</a></code>
- <code title="get /accounts/{account_id}/pcaps">client.pcaps.<a href="./src/cloudflare/resources/pcaps/pcaps.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/pcaps/pcap_list_response.py">SyncSinglePage[PCAPListResponse]</a></code>
- <code title="get /accounts/{account_id}/pcaps/{pcap_id}">client.pcaps.<a href="./src/cloudflare/resources/pcaps/pcaps.py">get</a>(pcap_id, \*, account_id) -> <a href="./src/cloudflare/types/pcaps/pcap_get_response.py">PCAPGetResponse</a></code>

## Ownership

Types:

```python
from cloudflare.types.pcaps import Ownership, OwnershipGetResponse
```

Methods:

- <code title="post /accounts/{account_id}/pcaps/ownership">client.pcaps.ownership.<a href="./src/cloudflare/resources/pcaps/ownership.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/pcaps/ownership_create_params.py">params</a>) -> <a href="./src/cloudflare/types/pcaps/ownership.py">Ownership</a></code>
- <code title="delete /accounts/{account_id}/pcaps/ownership/{ownership_id}">client.pcaps.ownership.<a href="./src/cloudflare/resources/pcaps/ownership.py">delete</a>(ownership_id, \*, account_id) -> None</code>
- <code title="get /accounts/{account_id}/pcaps/ownership">client.pcaps.ownership.<a href="./src/cloudflare/resources/pcaps/ownership.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/pcaps/ownership_get_response.py">Optional</a></code>
- <code title="post /accounts/{account_id}/pcaps/ownership/validate">client.pcaps.ownership.<a href="./src/cloudflare/resources/pcaps/ownership.py">validate</a>(\*, account_id, \*\*<a href="src/cloudflare/types/pcaps/ownership_validate_params.py">params</a>) -> <a href="./src/cloudflare/types/pcaps/ownership.py">Ownership</a></code>

## Download

Methods:

- <code title="get /accounts/{account_id}/pcaps/{pcap_id}/download">client.pcaps.download.<a href="./src/cloudflare/resources/pcaps/download.py">get</a>(pcap_id, \*, account_id) -> BinaryAPIResponse</code>

# Registrar

## Domains

Types:

```python
from cloudflare.types.registrar import (
    Domain,
    DomainUpdateResponse,
    DomainListResponse,
    DomainGetResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/registrar/domains/{domain_name}">client.registrar.domains.<a href="./src/cloudflare/resources/registrar/domains.py">update</a>(domain_name, \*, account_id, \*\*<a href="src/cloudflare/types/registrar/domain_update_params.py">params</a>) -> <a href="./src/cloudflare/types/registrar/domain_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/registrar/domains">client.registrar.domains.<a href="./src/cloudflare/resources/registrar/domains.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/registrar/domain_list_response.py">SyncSinglePage[DomainListResponse]</a></code>
- <code title="get /accounts/{account_id}/registrar/domains/{domain_name}">client.registrar.domains.<a href="./src/cloudflare/resources/registrar/domains.py">get</a>(domain_name, \*, account_id) -> <a href="./src/cloudflare/types/registrar/domain_get_response.py">Optional</a></code>

# RequestTracers

## Traces

Types:

```python
from cloudflare.types.request_tracers import Trace, TraceItem, TraceCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/request-tracer/trace">client.request_tracers.traces.<a href="./src/cloudflare/resources/request_tracers/traces.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/request_tracers/trace_create_params.py">params</a>) -> <a href="./src/cloudflare/types/request_tracers/trace_create_response.py">Optional</a></code>

# Rules

## Lists

Types:

```python
from cloudflare.types.rules import Hostname, ListsList, Redirect, ListDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/rules/lists">client.rules.lists.<a href="./src/cloudflare/resources/rules/lists/lists.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/rules/list_create_params.py">params</a>) -> <a href="./src/cloudflare/types/rules/lists_list.py">Optional</a></code>
- <code title="put /accounts/{account_id}/rules/lists/{list_id}">client.rules.lists.<a href="./src/cloudflare/resources/rules/lists/lists.py">update</a>(list_id, \*, account_id, \*\*<a href="src/cloudflare/types/rules/list_update_params.py">params</a>) -> <a href="./src/cloudflare/types/rules/lists_list.py">Optional</a></code>
- <code title="get /accounts/{account_id}/rules/lists">client.rules.lists.<a href="./src/cloudflare/resources/rules/lists/lists.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/rules/lists_list.py">SyncSinglePage[ListsList]</a></code>
- <code title="delete /accounts/{account_id}/rules/lists/{list_id}">client.rules.lists.<a href="./src/cloudflare/resources/rules/lists/lists.py">delete</a>(list_id, \*, account_id) -> <a href="./src/cloudflare/types/rules/list_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/rules/lists/{list_id}">client.rules.lists.<a href="./src/cloudflare/resources/rules/lists/lists.py">get</a>(list_id, \*, account_id) -> <a href="./src/cloudflare/types/rules/lists_list.py">Optional</a></code>

### BulkOperations

Types:

```python
from cloudflare.types.rules.lists import OperationStatus, BulkOperationGetResponse
```

Methods:

- <code title="get /accounts/{account_identifier}/rules/lists/bulk_operations/{operation_id}">client.rules.lists.bulk_operations.<a href="./src/cloudflare/resources/rules/lists/bulk_operations.py">get</a>(operation_id, \*, account_identifier) -> <a href="./src/cloudflare/types/rules/lists/bulk_operation_get_response.py">Optional</a></code>

### Items

Types:

```python
from cloudflare.types.rules.lists import (
    ListCursor,
    ListItem,
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
- <code title="get /accounts/{account_id}/rules/lists/{list_id}/items">client.rules.lists.items.<a href="./src/cloudflare/resources/rules/lists/items.py">list</a>(list_id, \*, account_id, \*\*<a href="src/cloudflare/types/rules/lists/item_list_params.py">params</a>) -> <a href="./src/cloudflare/types/rules/lists/item_list_response.py">SyncCursorPagination[object]</a></code>
- <code title="delete /accounts/{account_id}/rules/lists/{list_id}/items">client.rules.lists.items.<a href="./src/cloudflare/resources/rules/lists/items.py">delete</a>(list_id, \*, account_id) -> <a href="./src/cloudflare/types/rules/lists/item_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_identifier}/rules/lists/{list_id}/items/{item_id}">client.rules.lists.items.<a href="./src/cloudflare/resources/rules/lists/items.py">get</a>(item_id, \*, account_identifier, list_id) -> <a href="./src/cloudflare/types/rules/lists/item_get_response.py">Optional</a></code>

# Storage

## Analytics

Types:

```python
from cloudflare.types.storage import Components, Schema
```

Methods:

- <code title="get /accounts/{account_id}/storage/analytics">client.storage.analytics.<a href="./src/cloudflare/resources/storage/analytics.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/storage/analytics_list_params.py">params</a>) -> <a href="./src/cloudflare/types/storage/schema.py">Optional</a></code>
- <code title="get /accounts/{account_id}/storage/analytics/stored">client.storage.analytics.<a href="./src/cloudflare/resources/storage/analytics.py">stored</a>(\*, account_id, \*\*<a href="src/cloudflare/types/storage/analytics_stored_params.py">params</a>) -> <a href="./src/cloudflare/types/storage/components.py">Optional</a></code>

# Stream

Types:

```python
from cloudflare.types.stream import AllowedOrigins, Video
```

Methods:

- <code title="post /accounts/{account_id}/stream">client.stream.<a href="./src/cloudflare/resources/stream/stream.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/stream/stream_create_params.py">params</a>) -> None</code>
- <code title="get /accounts/{account_id}/stream">client.stream.<a href="./src/cloudflare/resources/stream/stream.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/stream/stream_list_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/video.py">SyncSinglePage[Video]</a></code>
- <code title="delete /accounts/{account_id}/stream/{identifier}">client.stream.<a href="./src/cloudflare/resources/stream/stream.py">delete</a>(identifier, \*, account_id) -> None</code>
- <code title="get /accounts/{account_id}/stream/{identifier}">client.stream.<a href="./src/cloudflare/resources/stream/stream.py">get</a>(identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/video.py">Optional</a></code>

## AudioTracks

Types:

```python
from cloudflare.types.stream import Audio, AudioTrackDeleteResponse, AudioTrackGetResponse
```

Methods:

- <code title="delete /accounts/{account_id}/stream/{identifier}/audio/{audio_identifier}">client.stream.audio_tracks.<a href="./src/cloudflare/resources/stream/audio_tracks.py">delete</a>(audio_identifier, \*, account_id, identifier) -> <a href="./src/cloudflare/types/stream/audio_track_delete_response.py">str</a></code>
- <code title="post /accounts/{account_id}/stream/{identifier}/audio/copy">client.stream.audio_tracks.<a href="./src/cloudflare/resources/stream/audio_tracks.py">copy</a>(identifier, \*, account_id, \*\*<a href="src/cloudflare/types/stream/audio_track_copy_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/audio.py">Optional</a></code>
- <code title="patch /accounts/{account_id}/stream/{identifier}/audio/{audio_identifier}">client.stream.audio_tracks.<a href="./src/cloudflare/resources/stream/audio_tracks.py">edit</a>(audio_identifier, \*, account_id, identifier, \*\*<a href="src/cloudflare/types/stream/audio_track_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/audio.py">Optional</a></code>
- <code title="get /accounts/{account_id}/stream/{identifier}/audio">client.stream.audio_tracks.<a href="./src/cloudflare/resources/stream/audio_tracks.py">get</a>(identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/audio_track_get_response.py">Optional</a></code>

## Videos

Types:

```python
from cloudflare.types.stream import VideoStorageUsageResponse
```

Methods:

- <code title="get /accounts/{account_id}/stream/storage-usage">client.stream.videos.<a href="./src/cloudflare/resources/stream/videos.py">storage_usage</a>(\*, account_id, \*\*<a href="src/cloudflare/types/stream/video_storage_usage_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/video_storage_usage_response.py">Optional</a></code>

## Clip

Types:

```python
from cloudflare.types.stream import Clip
```

Methods:

- <code title="post /accounts/{account_id}/stream/clip">client.stream.clip.<a href="./src/cloudflare/resources/stream/clip.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/stream/clip_create_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/clip.py">Optional</a></code>

## Copy

Methods:

- <code title="post /accounts/{account_id}/stream/copy">client.stream.copy.<a href="./src/cloudflare/resources/stream/copy.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/stream/copy_create_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/video.py">Optional</a></code>

## DirectUpload

Types:

```python
from cloudflare.types.stream import DirectUploadCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/stream/direct_upload">client.stream.direct_upload.<a href="./src/cloudflare/resources/stream/direct_upload.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/stream/direct_upload_create_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/direct_upload_create_response.py">Optional</a></code>

## Keys

Types:

```python
from cloudflare.types.stream import Keys, KeyDeleteResponse, KeyGetResponse
```

Methods:

- <code title="post /accounts/{account_id}/stream/keys">client.stream.keys.<a href="./src/cloudflare/resources/stream/keys.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/stream/key_create_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/keys.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/stream/keys/{identifier}">client.stream.keys.<a href="./src/cloudflare/resources/stream/keys.py">delete</a>(identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/key_delete_response.py">str</a></code>
- <code title="get /accounts/{account_id}/stream/keys">client.stream.keys.<a href="./src/cloudflare/resources/stream/keys.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/stream/key_get_response.py">Optional</a></code>

## LiveInputs

Types:

```python
from cloudflare.types.stream import LiveInput, LiveInputListResponse
```

Methods:

- <code title="post /accounts/{account_id}/stream/live_inputs">client.stream.live_inputs.<a href="./src/cloudflare/resources/stream/live_inputs/live_inputs.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/stream/live_input_create_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/live_input.py">Optional</a></code>
- <code title="put /accounts/{account_id}/stream/live_inputs/{live_input_identifier}">client.stream.live_inputs.<a href="./src/cloudflare/resources/stream/live_inputs/live_inputs.py">update</a>(live_input_identifier, \*, account_id, \*\*<a href="src/cloudflare/types/stream/live_input_update_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/live_input.py">Optional</a></code>
- <code title="get /accounts/{account_id}/stream/live_inputs">client.stream.live_inputs.<a href="./src/cloudflare/resources/stream/live_inputs/live_inputs.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/stream/live_input_list_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/live_input_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/stream/live_inputs/{live_input_identifier}">client.stream.live_inputs.<a href="./src/cloudflare/resources/stream/live_inputs/live_inputs.py">delete</a>(live_input_identifier, \*, account_id) -> None</code>
- <code title="get /accounts/{account_id}/stream/live_inputs/{live_input_identifier}">client.stream.live_inputs.<a href="./src/cloudflare/resources/stream/live_inputs/live_inputs.py">get</a>(live_input_identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/live_input.py">Optional</a></code>

### Outputs

Types:

```python
from cloudflare.types.stream.live_inputs import Output
```

Methods:

- <code title="post /accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs">client.stream.live_inputs.outputs.<a href="./src/cloudflare/resources/stream/live_inputs/outputs.py">create</a>(live_input_identifier, \*, account_id, \*\*<a href="src/cloudflare/types/stream/live_inputs/output_create_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/live_inputs/output.py">Optional</a></code>
- <code title="put /accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs/{output_identifier}">client.stream.live_inputs.outputs.<a href="./src/cloudflare/resources/stream/live_inputs/outputs.py">update</a>(output_identifier, \*, account_id, live_input_identifier, \*\*<a href="src/cloudflare/types/stream/live_inputs/output_update_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/live_inputs/output.py">Optional</a></code>
- <code title="get /accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs">client.stream.live_inputs.outputs.<a href="./src/cloudflare/resources/stream/live_inputs/outputs.py">list</a>(live_input_identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/live_inputs/output.py">SyncSinglePage[Output]</a></code>
- <code title="delete /accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs/{output_identifier}">client.stream.live_inputs.outputs.<a href="./src/cloudflare/resources/stream/live_inputs/outputs.py">delete</a>(output_identifier, \*, account_id, live_input_identifier) -> None</code>

## Watermarks

Types:

```python
from cloudflare.types.stream import Watermark, WatermarkDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/stream/watermarks">client.stream.watermarks.<a href="./src/cloudflare/resources/stream/watermarks.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/stream/watermark_create_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/watermark.py">Optional</a></code>
- <code title="get /accounts/{account_id}/stream/watermarks">client.stream.watermarks.<a href="./src/cloudflare/resources/stream/watermarks.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/stream/watermark.py">SyncSinglePage[Watermark]</a></code>
- <code title="delete /accounts/{account_id}/stream/watermarks/{identifier}">client.stream.watermarks.<a href="./src/cloudflare/resources/stream/watermarks.py">delete</a>(identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/watermark_delete_response.py">str</a></code>
- <code title="get /accounts/{account_id}/stream/watermarks/{identifier}">client.stream.watermarks.<a href="./src/cloudflare/resources/stream/watermarks.py">get</a>(identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/watermark.py">Optional</a></code>

## Webhooks

Types:

```python
from cloudflare.types.stream import WebhookUpdateResponse, WebhookDeleteResponse, WebhookGetResponse
```

Methods:

- <code title="put /accounts/{account_id}/stream/webhook">client.stream.webhooks.<a href="./src/cloudflare/resources/stream/webhooks.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/stream/webhook_update_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/webhook_update_response.py">object</a></code>
- <code title="delete /accounts/{account_id}/stream/webhook">client.stream.webhooks.<a href="./src/cloudflare/resources/stream/webhooks.py">delete</a>(\*, account_id) -> <a href="./src/cloudflare/types/stream/webhook_delete_response.py">str</a></code>
- <code title="get /accounts/{account_id}/stream/webhook">client.stream.webhooks.<a href="./src/cloudflare/resources/stream/webhooks.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/stream/webhook_get_response.py">object</a></code>

## Captions

Types:

```python
from cloudflare.types.stream import Caption, CaptionGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/stream/{identifier}/captions">client.stream.captions.<a href="./src/cloudflare/resources/stream/captions/captions.py">get</a>(identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/caption_get_response.py">Optional</a></code>

### Language

Types:

```python
from cloudflare.types.stream.captions import LanguageDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/stream/{identifier}/captions/{language}/generate">client.stream.captions.language.<a href="./src/cloudflare/resources/stream/captions/language/language.py">create</a>(language, \*, account_id, identifier) -> <a href="./src/cloudflare/types/stream/caption.py">Optional</a></code>
- <code title="put /accounts/{account_id}/stream/{identifier}/captions/{language}">client.stream.captions.language.<a href="./src/cloudflare/resources/stream/captions/language/language.py">update</a>(language, \*, account_id, identifier, \*\*<a href="src/cloudflare/types/stream/captions/language_update_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/caption.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/stream/{identifier}/captions/{language}">client.stream.captions.language.<a href="./src/cloudflare/resources/stream/captions/language/language.py">delete</a>(language, \*, account_id, identifier) -> <a href="./src/cloudflare/types/stream/captions/language_delete_response.py">str</a></code>
- <code title="get /accounts/{account_id}/stream/{identifier}/captions/{language}">client.stream.captions.language.<a href="./src/cloudflare/resources/stream/captions/language/language.py">get</a>(language, \*, account_id, identifier) -> <a href="./src/cloudflare/types/stream/caption.py">Optional</a></code>

#### Vtt

Types:

```python
from cloudflare.types.stream.captions.language import VttGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/stream/{identifier}/captions/{language}/vtt">client.stream.captions.language.vtt.<a href="./src/cloudflare/resources/stream/captions/language/vtt.py">get</a>(language, \*, account_id, identifier) -> str</code>

## Downloads

Types:

```python
from cloudflare.types.stream import (
    DownloadCreateResponse,
    DownloadDeleteResponse,
    DownloadGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/stream/{identifier}/downloads">client.stream.downloads.<a href="./src/cloudflare/resources/stream/downloads.py">create</a>(identifier, \*, account_id, \*\*<a href="src/cloudflare/types/stream/download_create_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/download_create_response.py">object</a></code>
- <code title="delete /accounts/{account_id}/stream/{identifier}/downloads">client.stream.downloads.<a href="./src/cloudflare/resources/stream/downloads.py">delete</a>(identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/download_delete_response.py">str</a></code>
- <code title="get /accounts/{account_id}/stream/{identifier}/downloads">client.stream.downloads.<a href="./src/cloudflare/resources/stream/downloads.py">get</a>(identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/download_get_response.py">object</a></code>

## Embed

Types:

```python
from cloudflare.types.stream import EmbedGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/stream/{identifier}/embed">client.stream.embed.<a href="./src/cloudflare/resources/stream/embed.py">get</a>(identifier, \*, account_id) -> str</code>

## Token

Types:

```python
from cloudflare.types.stream import TokenCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/stream/{identifier}/token">client.stream.token.<a href="./src/cloudflare/resources/stream/token.py">create</a>(identifier, \*, account_id, \*\*<a href="src/cloudflare/types/stream/token_create_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/token_create_response.py">Optional</a></code>

# Alerting

## AvailableAlerts

Types:

```python
from cloudflare.types.alerting import AvailableAlertListResponse
```

Methods:

- <code title="get /accounts/{account_id}/alerting/v3/available_alerts">client.alerting.available_alerts.<a href="./src/cloudflare/resources/alerting/available_alerts.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/alerting/available_alert_list_response.py">Optional</a></code>

## Destinations

### Eligible

Types:

```python
from cloudflare.types.alerting.destinations import EligibleGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/alerting/v3/destinations/eligible">client.alerting.destinations.eligible.<a href="./src/cloudflare/resources/alerting/destinations/eligible.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/alerting/destinations/eligible_get_response.py">Optional</a></code>

### Pagerduty

Types:

```python
from cloudflare.types.alerting.destinations import (
    Pagerduty,
    PagerdutyCreateResponse,
    PagerdutyDeleteResponse,
    PagerdutyGetResponse,
    PagerdutyLinkResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/alerting/v3/destinations/pagerduty/connect">client.alerting.destinations.pagerduty.<a href="./src/cloudflare/resources/alerting/destinations/pagerduty.py">create</a>(\*, account_id) -> <a href="./src/cloudflare/types/alerting/destinations/pagerduty_create_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/alerting/v3/destinations/pagerduty">client.alerting.destinations.pagerduty.<a href="./src/cloudflare/resources/alerting/destinations/pagerduty.py">delete</a>(\*, account_id) -> <a href="./src/cloudflare/types/alerting/destinations/pagerduty_delete_response.py">PagerdutyDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/alerting/v3/destinations/pagerduty">client.alerting.destinations.pagerduty.<a href="./src/cloudflare/resources/alerting/destinations/pagerduty.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/alerting/destinations/pagerduty_get_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/alerting/v3/destinations/pagerduty/connect/{token_id}">client.alerting.destinations.pagerduty.<a href="./src/cloudflare/resources/alerting/destinations/pagerduty.py">link</a>(token_id, \*, account_id) -> <a href="./src/cloudflare/types/alerting/destinations/pagerduty_link_response.py">Optional</a></code>

### Webhooks

Types:

```python
from cloudflare.types.alerting.destinations import (
    Webhooks,
    WebhookCreateResponse,
    WebhookUpdateResponse,
    WebhookDeleteResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/alerting/v3/destinations/webhooks">client.alerting.destinations.webhooks.<a href="./src/cloudflare/resources/alerting/destinations/webhooks.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/alerting/destinations/webhook_create_params.py">params</a>) -> <a href="./src/cloudflare/types/alerting/destinations/webhook_create_response.py">Optional</a></code>
- <code title="put /accounts/{account_id}/alerting/v3/destinations/webhooks/{webhook_id}">client.alerting.destinations.webhooks.<a href="./src/cloudflare/resources/alerting/destinations/webhooks.py">update</a>(webhook_id, \*, account_id, \*\*<a href="src/cloudflare/types/alerting/destinations/webhook_update_params.py">params</a>) -> <a href="./src/cloudflare/types/alerting/destinations/webhook_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/alerting/v3/destinations/webhooks">client.alerting.destinations.webhooks.<a href="./src/cloudflare/resources/alerting/destinations/webhooks.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/alerting/destinations/webhooks.py">SyncSinglePage[Webhooks]</a></code>
- <code title="delete /accounts/{account_id}/alerting/v3/destinations/webhooks/{webhook_id}">client.alerting.destinations.webhooks.<a href="./src/cloudflare/resources/alerting/destinations/webhooks.py">delete</a>(webhook_id, \*, account_id) -> <a href="./src/cloudflare/types/alerting/destinations/webhook_delete_response.py">WebhookDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/alerting/v3/destinations/webhooks/{webhook_id}">client.alerting.destinations.webhooks.<a href="./src/cloudflare/resources/alerting/destinations/webhooks.py">get</a>(webhook_id, \*, account_id) -> <a href="./src/cloudflare/types/alerting/destinations/webhooks.py">Optional</a></code>

## History

Types:

```python
from cloudflare.types.alerting import History
```

Methods:

- <code title="get /accounts/{account_id}/alerting/v3/history">client.alerting.history.<a href="./src/cloudflare/resources/alerting/history.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/alerting/history_list_params.py">params</a>) -> <a href="./src/cloudflare/types/alerting/history.py">SyncV4PagePaginationArray[History]</a></code>

## Policies

Types:

```python
from cloudflare.types.alerting import (
    Mechanism,
    Policy,
    PolicyFilter,
    PolicyCreateResponse,
    PolicyUpdateResponse,
    PolicyDeleteResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/alerting/v3/policies">client.alerting.policies.<a href="./src/cloudflare/resources/alerting/policies.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/alerting/policy_create_params.py">params</a>) -> <a href="./src/cloudflare/types/alerting/policy_create_response.py">Optional</a></code>
- <code title="put /accounts/{account_id}/alerting/v3/policies/{policy_id}">client.alerting.policies.<a href="./src/cloudflare/resources/alerting/policies.py">update</a>(policy_id, \*, account_id, \*\*<a href="src/cloudflare/types/alerting/policy_update_params.py">params</a>) -> <a href="./src/cloudflare/types/alerting/policy_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/alerting/v3/policies">client.alerting.policies.<a href="./src/cloudflare/resources/alerting/policies.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/alerting/policy.py">SyncSinglePage[Policy]</a></code>
- <code title="delete /accounts/{account_id}/alerting/v3/policies/{policy_id}">client.alerting.policies.<a href="./src/cloudflare/resources/alerting/policies.py">delete</a>(policy_id, \*, account_id) -> <a href="./src/cloudflare/types/alerting/policy_delete_response.py">PolicyDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/alerting/v3/policies/{policy_id}">client.alerting.policies.<a href="./src/cloudflare/resources/alerting/policies.py">get</a>(policy_id, \*, account_id) -> <a href="./src/cloudflare/types/alerting/policy.py">Optional</a></code>

# D1

Types:

```python
from cloudflare.types.d1 import D1
```

## Database

Types:

```python
from cloudflare.types.d1 import (
    QueryResult,
    DatabaseListResponse,
    DatabaseDeleteResponse,
    DatabaseExportResponse,
    DatabaseImportResponse,
    DatabaseQueryResponse,
    DatabaseRawResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/d1/database">client.d1.database.<a href="./src/cloudflare/resources/d1/database.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/d1/database_create_params.py">params</a>) -> <a href="./src/cloudflare/types/d1/d1.py">D1</a></code>
- <code title="get /accounts/{account_id}/d1/database">client.d1.database.<a href="./src/cloudflare/resources/d1/database.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/d1/database_list_params.py">params</a>) -> <a href="./src/cloudflare/types/d1/database_list_response.py">SyncV4PagePaginationArray[DatabaseListResponse]</a></code>
- <code title="delete /accounts/{account_id}/d1/database/{database_id}">client.d1.database.<a href="./src/cloudflare/resources/d1/database.py">delete</a>(database_id, \*, account_id) -> <a href="./src/cloudflare/types/d1/database_delete_response.py">object</a></code>
- <code title="post /accounts/{account_id}/d1/database/{database_id}/export">client.d1.database.<a href="./src/cloudflare/resources/d1/database.py">export</a>(database_id, \*, account_id, \*\*<a href="src/cloudflare/types/d1/database_export_params.py">params</a>) -> <a href="./src/cloudflare/types/d1/database_export_response.py">DatabaseExportResponse</a></code>
- <code title="get /accounts/{account_id}/d1/database/{database_id}">client.d1.database.<a href="./src/cloudflare/resources/d1/database.py">get</a>(database_id, \*, account_id) -> <a href="./src/cloudflare/types/d1/d1.py">D1</a></code>
- <code title="post /accounts/{account_id}/d1/database/{database_id}/import">client.d1.database.<a href="./src/cloudflare/resources/d1/database.py">import\_</a>(database_id, \*, account_id, \*\*<a href="src/cloudflare/types/d1/database_import_params.py">params</a>) -> <a href="./src/cloudflare/types/d1/database_import_response.py">DatabaseImportResponse</a></code>
- <code title="post /accounts/{account_id}/d1/database/{database_id}/query">client.d1.database.<a href="./src/cloudflare/resources/d1/database.py">query</a>(database_id, \*, account_id, \*\*<a href="src/cloudflare/types/d1/database_query_params.py">params</a>) -> <a href="./src/cloudflare/types/d1/database_query_response.py">DatabaseQueryResponse</a></code>
- <code title="post /accounts/{account_id}/d1/database/{database_id}/raw">client.d1.database.<a href="./src/cloudflare/resources/d1/database.py">raw</a>(database_id, \*, account_id, \*\*<a href="src/cloudflare/types/d1/database_raw_params.py">params</a>) -> <a href="./src/cloudflare/types/d1/database_raw_response.py">DatabaseRawResponse</a></code>

# R2

## Buckets

Types:

```python
from cloudflare.types.r2 import Bucket, BucketListResponse, BucketDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/r2/buckets">client.r2.buckets.<a href="./src/cloudflare/resources/r2/buckets.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/r2/bucket_create_params.py">params</a>) -> <a href="./src/cloudflare/types/r2/bucket.py">Bucket</a></code>
- <code title="get /accounts/{account_id}/r2/buckets">client.r2.buckets.<a href="./src/cloudflare/resources/r2/buckets.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/r2/bucket_list_params.py">params</a>) -> <a href="./src/cloudflare/types/r2/bucket_list_response.py">BucketListResponse</a></code>
- <code title="delete /accounts/{account_id}/r2/buckets/{bucket_name}">client.r2.buckets.<a href="./src/cloudflare/resources/r2/buckets.py">delete</a>(bucket_name, \*, account_id) -> <a href="./src/cloudflare/types/r2/bucket_delete_response.py">object</a></code>
- <code title="get /accounts/{account_id}/r2/buckets/{bucket_name}">client.r2.buckets.<a href="./src/cloudflare/resources/r2/buckets.py">get</a>(bucket_name, \*, account_id) -> <a href="./src/cloudflare/types/r2/bucket.py">Bucket</a></code>

## Sippy

Types:

```python
from cloudflare.types.r2 import Provider, Sippy, SippyDeleteResponse
```

Methods:

- <code title="put /accounts/{account_id}/r2/buckets/{bucket_name}/sippy">client.r2.sippy.<a href="./src/cloudflare/resources/r2/sippy.py">update</a>(bucket_name, \*, account_id, \*\*<a href="src/cloudflare/types/r2/sippy_update_params.py">params</a>) -> <a href="./src/cloudflare/types/r2/sippy.py">Sippy</a></code>
- <code title="delete /accounts/{account_id}/r2/buckets/{bucket_name}/sippy">client.r2.sippy.<a href="./src/cloudflare/resources/r2/sippy.py">delete</a>(bucket_name, \*, account_id) -> <a href="./src/cloudflare/types/r2/sippy_delete_response.py">SippyDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/r2/buckets/{bucket_name}/sippy">client.r2.sippy.<a href="./src/cloudflare/resources/r2/sippy.py">get</a>(bucket_name, \*, account_id) -> <a href="./src/cloudflare/types/r2/sippy.py">Sippy</a></code>

## TemporaryCredentials

Types:

```python
from cloudflare.types.r2 import TemporaryCredential, TemporaryCredentialCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/r2/temp-access-credentials">client.r2.temporary_credentials.<a href="./src/cloudflare/resources/r2/temporary_credentials.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/r2/temporary_credential_create_params.py">params</a>) -> <a href="./src/cloudflare/types/r2/temporary_credential_create_response.py">TemporaryCredentialCreateResponse</a></code>

## Domains

### Custom

Types:

```python
from cloudflare.types.r2.domains import (
    CustomCreateResponse,
    CustomUpdateResponse,
    CustomListResponse,
    CustomDeleteResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/r2/buckets/{bucket_name}/domains/custom">client.r2.domains.custom.<a href="./src/cloudflare/resources/r2/domains/custom.py">create</a>(bucket_name, \*, account_id, \*\*<a href="src/cloudflare/types/r2/domains/custom_create_params.py">params</a>) -> <a href="./src/cloudflare/types/r2/domains/custom_create_response.py">CustomCreateResponse</a></code>
- <code title="put /accounts/{account_id}/r2/buckets/{bucket_name}/domains/custom/{domain_name}">client.r2.domains.custom.<a href="./src/cloudflare/resources/r2/domains/custom.py">update</a>(domain_name, \*, account_id, bucket_name, \*\*<a href="src/cloudflare/types/r2/domains/custom_update_params.py">params</a>) -> <a href="./src/cloudflare/types/r2/domains/custom_update_response.py">CustomUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/r2/buckets/{bucket_name}/domains/custom">client.r2.domains.custom.<a href="./src/cloudflare/resources/r2/domains/custom.py">list</a>(bucket_name, \*, account_id) -> <a href="./src/cloudflare/types/r2/domains/custom_list_response.py">CustomListResponse</a></code>
- <code title="delete /accounts/{account_id}/r2/buckets/{bucket_name}/domains/custom/{domain_name}">client.r2.domains.custom.<a href="./src/cloudflare/resources/r2/domains/custom.py">delete</a>(domain_name, \*, account_id, bucket_name) -> <a href="./src/cloudflare/types/r2/domains/custom_delete_response.py">CustomDeleteResponse</a></code>

### Managed

Types:

```python
from cloudflare.types.r2.domains import ManagedUpdateResponse, ManagedListResponse
```

Methods:

- <code title="put /accounts/{account_id}/r2/buckets/{bucket_name}/domains/managed">client.r2.domains.managed.<a href="./src/cloudflare/resources/r2/domains/managed.py">update</a>(bucket_name, \*, account_id, \*\*<a href="src/cloudflare/types/r2/domains/managed_update_params.py">params</a>) -> <a href="./src/cloudflare/types/r2/domains/managed_update_response.py">ManagedUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/r2/buckets/{bucket_name}/domains/managed">client.r2.domains.managed.<a href="./src/cloudflare/resources/r2/domains/managed.py">list</a>(bucket_name, \*, account_id) -> <a href="./src/cloudflare/types/r2/domains/managed_list_response.py">ManagedListResponse</a></code>

# WARPConnector

Types:

```python
from cloudflare.types.warp_connector import (
    WARPConnectorCreateResponse,
    WARPConnectorListResponse,
    WARPConnectorDeleteResponse,
    WARPConnectorEditResponse,
    WARPConnectorGetResponse,
    WARPConnectorTokenResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/warp_connector">client.warp_connector.<a href="./src/cloudflare/resources/warp_connector.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/warp_connector/warp_connector_create_params.py">params</a>) -> <a href="./src/cloudflare/types/warp_connector/warp_connector_create_response.py">WARPConnectorCreateResponse</a></code>
- <code title="get /accounts/{account_id}/warp_connector">client.warp_connector.<a href="./src/cloudflare/resources/warp_connector.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/warp_connector/warp_connector_list_params.py">params</a>) -> <a href="./src/cloudflare/types/warp_connector/warp_connector_list_response.py">SyncV4PagePaginationArray[WARPConnectorListResponse]</a></code>
- <code title="delete /accounts/{account_id}/warp_connector/{tunnel_id}">client.warp_connector.<a href="./src/cloudflare/resources/warp_connector.py">delete</a>(tunnel_id, \*, account_id) -> <a href="./src/cloudflare/types/warp_connector/warp_connector_delete_response.py">WARPConnectorDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/warp_connector/{tunnel_id}">client.warp_connector.<a href="./src/cloudflare/resources/warp_connector.py">edit</a>(tunnel_id, \*, account_id, \*\*<a href="src/cloudflare/types/warp_connector/warp_connector_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/warp_connector/warp_connector_edit_response.py">WARPConnectorEditResponse</a></code>
- <code title="get /accounts/{account_id}/warp_connector/{tunnel_id}">client.warp_connector.<a href="./src/cloudflare/resources/warp_connector.py">get</a>(tunnel_id, \*, account_id) -> <a href="./src/cloudflare/types/warp_connector/warp_connector_get_response.py">WARPConnectorGetResponse</a></code>
- <code title="get /accounts/{account_id}/warp_connector/{tunnel_id}/token">client.warp_connector.<a href="./src/cloudflare/resources/warp_connector.py">token</a>(tunnel_id, \*, account_id) -> <a href="./src/cloudflare/types/warp_connector/warp_connector_token_response.py">WARPConnectorTokenResponse</a></code>

# WorkersForPlatforms

## Dispatch

### Namespaces

Types:

```python
from cloudflare.types.workers_for_platforms.dispatch import (
    NamespaceCreateResponse,
    NamespaceListResponse,
    NamespaceDeleteResponse,
    NamespaceGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/workers/dispatch/namespaces">client.workers_for_platforms.dispatch.namespaces.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/namespaces.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/workers_for_platforms/dispatch/namespace_create_params.py">params</a>) -> <a href="./src/cloudflare/types/workers_for_platforms/dispatch/namespace_create_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/workers/dispatch/namespaces">client.workers_for_platforms.dispatch.namespaces.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/namespaces.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/workers_for_platforms/dispatch/namespace_list_response.py">SyncSinglePage[NamespaceListResponse]</a></code>
- <code title="delete /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}">client.workers_for_platforms.dispatch.namespaces.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/namespaces.py">delete</a>(dispatch_namespace, \*, account_id) -> <a href="./src/cloudflare/types/workers_for_platforms/dispatch/namespace_delete_response.py">object</a></code>
- <code title="get /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}">client.workers_for_platforms.dispatch.namespaces.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/namespaces.py">get</a>(dispatch_namespace, \*, account_id) -> <a href="./src/cloudflare/types/workers_for_platforms/dispatch/namespace_get_response.py">Optional</a></code>

#### Scripts

Types:

```python
from cloudflare.types.workers_for_platforms.dispatch.namespaces import Script, ScriptUpdateResponse
```

Methods:

- <code title="put /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}">client.workers_for_platforms.dispatch.namespaces.scripts.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/scripts.py">update</a>(script_name, \*, account_id, dispatch_namespace, \*\*<a href="src/cloudflare/types/workers_for_platforms/dispatch/namespaces/script_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers_for_platforms/dispatch/namespaces/script_update_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}">client.workers_for_platforms.dispatch.namespaces.scripts.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/scripts.py">delete</a>(script_name, \*, account_id, dispatch_namespace, \*\*<a href="src/cloudflare/types/workers_for_platforms/dispatch/namespaces/script_delete_params.py">params</a>) -> None</code>
- <code title="get /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}">client.workers_for_platforms.dispatch.namespaces.scripts.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/scripts.py">get</a>(script_name, \*, account_id, dispatch_namespace) -> <a href="./src/cloudflare/types/workers_for_platforms/dispatch/namespaces/script.py">Optional</a></code>

##### Content

Methods:

- <code title="put /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/content">client.workers_for_platforms.dispatch.namespaces.scripts.content.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/content.py">update</a>(script_name, \*, account_id, dispatch_namespace, \*\*<a href="src/cloudflare/types/workers_for_platforms/dispatch/namespaces/scripts/content_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/script.py">Optional</a></code>
- <code title="get /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/content">client.workers_for_platforms.dispatch.namespaces.scripts.content.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/content.py">get</a>(script_name, \*, account_id, dispatch_namespace) -> BinaryAPIResponse</code>

##### Settings

Types:

```python
from cloudflare.types.workers_for_platforms.dispatch.namespaces.scripts import (
    SettingEditResponse,
    SettingGetResponse,
)
```

Methods:

- <code title="patch /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/settings">client.workers_for_platforms.dispatch.namespaces.scripts.settings.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/settings.py">edit</a>(script_name, \*, account_id, dispatch_namespace, \*\*<a href="src/cloudflare/types/workers_for_platforms/dispatch/namespaces/scripts/setting_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/workers_for_platforms/dispatch/namespaces/scripts/setting_edit_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/settings">client.workers_for_platforms.dispatch.namespaces.scripts.settings.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/settings.py">get</a>(script_name, \*, account_id, dispatch_namespace) -> <a href="./src/cloudflare/types/workers_for_platforms/dispatch/namespaces/scripts/setting_get_response.py">Optional</a></code>

##### Bindings

Types:

```python
from cloudflare.types.workers_for_platforms.dispatch.namespaces.scripts import BindingGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/bindings">client.workers_for_platforms.dispatch.namespaces.scripts.bindings.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/bindings.py">get</a>(script_name, \*, account_id, dispatch_namespace) -> <a href="./src/cloudflare/types/workers_for_platforms/dispatch/namespaces/scripts/binding_get_response.py">Optional</a></code>

##### Secrets

Types:

```python
from cloudflare.types.workers_for_platforms.dispatch.namespaces.scripts import (
    SecretUpdateResponse,
    SecretListResponse,
    SecretGetResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/secrets">client.workers_for_platforms.dispatch.namespaces.scripts.secrets.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/secrets.py">update</a>(script_name, \*, account_id, dispatch_namespace, \*\*<a href="src/cloudflare/types/workers_for_platforms/dispatch/namespaces/scripts/secret_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers_for_platforms/dispatch/namespaces/scripts/secret_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/secrets">client.workers_for_platforms.dispatch.namespaces.scripts.secrets.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/secrets.py">list</a>(script_name, \*, account_id, dispatch_namespace) -> <a href="./src/cloudflare/types/workers_for_platforms/dispatch/namespaces/scripts/secret_list_response.py">SyncSinglePage[SecretListResponse]</a></code>
- <code title="get /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/secrets/{secret_name}">client.workers_for_platforms.dispatch.namespaces.scripts.secrets.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/secrets.py">get</a>(secret_name, \*, account_id, dispatch_namespace, script_name) -> <a href="./src/cloudflare/types/workers_for_platforms/dispatch/namespaces/scripts/secret_get_response.py">Optional</a></code>

##### Tags

Types:

```python
from cloudflare.types.workers_for_platforms.dispatch.namespaces.scripts import (
    TagUpdateResponse,
    TagListResponse,
    TagDeleteResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/tags">client.workers_for_platforms.dispatch.namespaces.scripts.tags.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/tags.py">update</a>(script_name, \*, account_id, dispatch_namespace, \*\*<a href="src/cloudflare/types/workers_for_platforms/dispatch/namespaces/scripts/tag_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers_for_platforms/dispatch/namespaces/scripts/tag_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/tags">client.workers_for_platforms.dispatch.namespaces.scripts.tags.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/tags.py">list</a>(script_name, \*, account_id, dispatch_namespace) -> <a href="./src/cloudflare/types/workers_for_platforms/dispatch/namespaces/scripts/tag_list_response.py">SyncSinglePage[TagListResponse]</a></code>
- <code title="delete /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/tags/{tag}">client.workers_for_platforms.dispatch.namespaces.scripts.tags.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/tags.py">delete</a>(tag, \*, account_id, dispatch_namespace, script_name) -> <a href="./src/cloudflare/types/workers_for_platforms/dispatch/namespaces/scripts/tag_delete_response.py">object</a></code>

# ZeroTrust

## Devices

Types:

```python
from cloudflare.types.zero_trust import Device, DeviceGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/devices">client.zero_trust.devices.<a href="./src/cloudflare/resources/zero_trust/devices/devices.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/device.py">SyncSinglePage[Device]</a></code>
- <code title="get /accounts/{account_id}/devices/{device_id}">client.zero_trust.devices.<a href="./src/cloudflare/resources/zero_trust/devices/devices.py">get</a>(device_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/device_get_response.py">Optional</a></code>

### DEXTests

Types:

```python
from cloudflare.types.zero_trust.devices import (
    DEXTest,
    SchemaData,
    SchemaHTTP,
    DEXTestDeleteResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/devices/dex_tests">client.zero_trust.devices.dex_tests.<a href="./src/cloudflare/resources/zero_trust/devices/dex_tests.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/dex_test_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/schema_http.py">Optional</a></code>
- <code title="put /accounts/{account_id}/devices/dex_tests/{dex_test_id}">client.zero_trust.devices.dex_tests.<a href="./src/cloudflare/resources/zero_trust/devices/dex_tests.py">update</a>(dex_test_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/dex_test_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/schema_http.py">Optional</a></code>
- <code title="get /accounts/{account_id}/devices/dex_tests">client.zero_trust.devices.dex_tests.<a href="./src/cloudflare/resources/zero_trust/devices/dex_tests.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/schema_http.py">SyncSinglePage[SchemaHTTP]</a></code>
- <code title="delete /accounts/{account_id}/devices/dex_tests/{dex_test_id}">client.zero_trust.devices.dex_tests.<a href="./src/cloudflare/resources/zero_trust/devices/dex_tests.py">delete</a>(dex_test_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/dex_test_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/devices/dex_tests/{dex_test_id}">client.zero_trust.devices.dex_tests.<a href="./src/cloudflare/resources/zero_trust/devices/dex_tests.py">get</a>(dex_test_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/schema_http.py">Optional</a></code>

### Networks

Types:

```python
from cloudflare.types.zero_trust.devices import DeviceNetwork, NetworkDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/devices/networks">client.zero_trust.devices.networks.<a href="./src/cloudflare/resources/zero_trust/devices/networks.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/network_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/device_network.py">Optional</a></code>
- <code title="put /accounts/{account_id}/devices/networks/{network_id}">client.zero_trust.devices.networks.<a href="./src/cloudflare/resources/zero_trust/devices/networks.py">update</a>(network_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/network_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/device_network.py">Optional</a></code>
- <code title="get /accounts/{account_id}/devices/networks">client.zero_trust.devices.networks.<a href="./src/cloudflare/resources/zero_trust/devices/networks.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/device_network.py">SyncSinglePage[DeviceNetwork]</a></code>
- <code title="delete /accounts/{account_id}/devices/networks/{network_id}">client.zero_trust.devices.networks.<a href="./src/cloudflare/resources/zero_trust/devices/networks.py">delete</a>(network_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/network_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/devices/networks/{network_id}">client.zero_trust.devices.networks.<a href="./src/cloudflare/resources/zero_trust/devices/networks.py">get</a>(network_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/device_network.py">Optional</a></code>

### Policies

Types:

```python
from cloudflare.types.zero_trust.devices import SettingsPolicy, PolicyDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/devices/policy">client.zero_trust.devices.policies.<a href="./src/cloudflare/resources/zero_trust/devices/policies/policies.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/policy_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/settings_policy.py">Optional</a></code>
- <code title="get /accounts/{account_id}/devices/policies">client.zero_trust.devices.policies.<a href="./src/cloudflare/resources/zero_trust/devices/policies/policies.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/settings_policy.py">SyncSinglePage[SettingsPolicy]</a></code>
- <code title="delete /accounts/{account_id}/devices/policy/{policy_id}">client.zero_trust.devices.policies.<a href="./src/cloudflare/resources/zero_trust/devices/policies/policies.py">delete</a>(policy_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/policy_delete_response.py">Optional</a></code>
- <code title="patch /accounts/{account_id}/devices/policy/{policy_id}">client.zero_trust.devices.policies.<a href="./src/cloudflare/resources/zero_trust/devices/policies/policies.py">edit</a>(policy_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/policy_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/settings_policy.py">Optional</a></code>
- <code title="get /accounts/{account_id}/devices/policy/{policy_id}">client.zero_trust.devices.policies.<a href="./src/cloudflare/resources/zero_trust/devices/policies/policies.py">get</a>(policy_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/settings_policy.py">Optional</a></code>

#### Certificates

Types:

```python
from cloudflare.types.zero_trust.devices.policies import (
    DevicePolicyCertificates,
    CertificateUpdateResponse,
    CertificateGetResponse,
)
```

Methods:

- <code title="patch /zones/{zone_tag}/devices/policy/certificates">client.zero_trust.devices.policies.certificates.<a href="./src/cloudflare/resources/zero_trust/devices/policies/certificates.py">update</a>(zone_tag, \*\*<a href="src/cloudflare/types/zero_trust/devices/policies/certificate_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/policies/certificate_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_tag}/devices/policy/certificates">client.zero_trust.devices.policies.certificates.<a href="./src/cloudflare/resources/zero_trust/devices/policies/certificates.py">get</a>(zone_tag) -> <a href="./src/cloudflare/types/zero_trust/devices/policies/certificate_get_response.py">Optional</a></code>

#### DefaultPolicy

Types:

```python
from cloudflare.types.zero_trust.devices.policies import DefaultPolicyGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/devices/policy">client.zero_trust.devices.policies.default_policy.<a href="./src/cloudflare/resources/zero_trust/devices/policies/default_policy.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/policies/default_policy_get_response.py">Optional</a></code>

#### Excludes

Types:

```python
from cloudflare.types.zero_trust.devices.policies import (
    SplitTunnelExclude,
    ExcludeUpdateResponse,
    ExcludeGetResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/devices/policy/exclude">client.zero_trust.devices.policies.excludes.<a href="./src/cloudflare/resources/zero_trust/devices/policies/excludes.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/policies/exclude_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/policies/exclude_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/devices/policy/exclude">client.zero_trust.devices.policies.excludes.<a href="./src/cloudflare/resources/zero_trust/devices/policies/excludes.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/policies/split_tunnel_exclude.py">SyncSinglePage[SplitTunnelExclude]</a></code>
- <code title="get /accounts/{account_id}/devices/policy/{policy_id}/exclude">client.zero_trust.devices.policies.excludes.<a href="./src/cloudflare/resources/zero_trust/devices/policies/excludes.py">get</a>(policy_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/policies/exclude_get_response.py">Optional</a></code>

#### FallbackDomains

Types:

```python
from cloudflare.types.zero_trust.devices.policies import (
    FallbackDomain,
    FallbackDomainPolicy,
    FallbackDomainUpdateResponse,
    FallbackDomainGetResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/devices/policy/{policy_id}/fallback_domains">client.zero_trust.devices.policies.fallback_domains.<a href="./src/cloudflare/resources/zero_trust/devices/policies/fallback_domains.py">update</a>(policy_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/policies/fallback_domain_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/policies/fallback_domain_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/devices/policy/fallback_domains">client.zero_trust.devices.policies.fallback_domains.<a href="./src/cloudflare/resources/zero_trust/devices/policies/fallback_domains.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/policies/fallback_domain.py">SyncSinglePage[FallbackDomain]</a></code>
- <code title="get /accounts/{account_id}/devices/policy/{policy_id}/fallback_domains">client.zero_trust.devices.policies.fallback_domains.<a href="./src/cloudflare/resources/zero_trust/devices/policies/fallback_domains.py">get</a>(policy_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/policies/fallback_domain_get_response.py">Optional</a></code>

#### Includes

Types:

```python
from cloudflare.types.zero_trust.devices.policies import (
    SplitTunnelInclude,
    IncludeUpdateResponse,
    IncludeGetResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/devices/policy/include">client.zero_trust.devices.policies.includes.<a href="./src/cloudflare/resources/zero_trust/devices/policies/includes.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/policies/include_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/policies/include_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/devices/policy/include">client.zero_trust.devices.policies.includes.<a href="./src/cloudflare/resources/zero_trust/devices/policies/includes.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/policies/split_tunnel_include.py">SyncSinglePage[SplitTunnelInclude]</a></code>
- <code title="get /accounts/{account_id}/devices/policy/{policy_id}/include">client.zero_trust.devices.policies.includes.<a href="./src/cloudflare/resources/zero_trust/devices/policies/includes.py">get</a>(policy_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/policies/include_get_response.py">Optional</a></code>

### Posture

Types:

```python
from cloudflare.types.zero_trust.devices import (
    CarbonblackInput,
    ClientCertificateInput,
    CrowdstrikeInput,
    DeviceInput,
    DeviceMatch,
    DevicePostureRule,
    DiskEncryptionInput,
    DomainJoinedInput,
    FileInput,
    FirewallInput,
    IntuneInput,
    KolideInput,
    OSVersionInput,
    SentineloneInput,
    SentineloneS2sInput,
    TaniumInput,
    UniqueClientIDInput,
    WorkspaceOneInput,
    PostureDeleteResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/devices/posture">client.zero_trust.devices.posture.<a href="./src/cloudflare/resources/zero_trust/devices/posture/posture.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/posture_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/device_posture_rule.py">Optional</a></code>
- <code title="put /accounts/{account_id}/devices/posture/{rule_id}">client.zero_trust.devices.posture.<a href="./src/cloudflare/resources/zero_trust/devices/posture/posture.py">update</a>(rule_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/posture_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/device_posture_rule.py">Optional</a></code>
- <code title="get /accounts/{account_id}/devices/posture">client.zero_trust.devices.posture.<a href="./src/cloudflare/resources/zero_trust/devices/posture/posture.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/device_posture_rule.py">SyncSinglePage[DevicePostureRule]</a></code>
- <code title="delete /accounts/{account_id}/devices/posture/{rule_id}">client.zero_trust.devices.posture.<a href="./src/cloudflare/resources/zero_trust/devices/posture/posture.py">delete</a>(rule_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/posture_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/devices/posture/{rule_id}">client.zero_trust.devices.posture.<a href="./src/cloudflare/resources/zero_trust/devices/posture/posture.py">get</a>(rule_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/device_posture_rule.py">Optional</a></code>

#### Integrations

Types:

```python
from cloudflare.types.zero_trust.devices.posture import Integration, IntegrationDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/devices/posture/integration">client.zero_trust.devices.posture.integrations.<a href="./src/cloudflare/resources/zero_trust/devices/posture/integrations.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/posture/integration_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/posture/integration.py">Optional</a></code>
- <code title="get /accounts/{account_id}/devices/posture/integration">client.zero_trust.devices.posture.integrations.<a href="./src/cloudflare/resources/zero_trust/devices/posture/integrations.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/posture/integration.py">SyncSinglePage[Integration]</a></code>
- <code title="delete /accounts/{account_id}/devices/posture/integration/{integration_id}">client.zero_trust.devices.posture.integrations.<a href="./src/cloudflare/resources/zero_trust/devices/posture/integrations.py">delete</a>(integration_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/posture/integration_delete_response.py">Optional</a></code>
- <code title="patch /accounts/{account_id}/devices/posture/integration/{integration_id}">client.zero_trust.devices.posture.integrations.<a href="./src/cloudflare/resources/zero_trust/devices/posture/integrations.py">edit</a>(integration_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/posture/integration_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/posture/integration.py">Optional</a></code>
- <code title="get /accounts/{account_id}/devices/posture/integration/{integration_id}">client.zero_trust.devices.posture.integrations.<a href="./src/cloudflare/resources/zero_trust/devices/posture/integrations.py">get</a>(integration_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/posture/integration.py">Optional</a></code>

### Revoke

Types:

```python
from cloudflare.types.zero_trust.devices import RevokeCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/devices/revoke">client.zero_trust.devices.revoke.<a href="./src/cloudflare/resources/zero_trust/devices/revoke.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/revoke_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/revoke_create_response.py">Optional</a></code>

### Settings

Types:

```python
from cloudflare.types.zero_trust.devices import DeviceSettings
```

Methods:

- <code title="put /accounts/{account_id}/devices/settings">client.zero_trust.devices.settings.<a href="./src/cloudflare/resources/zero_trust/devices/settings.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/setting_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/device_settings.py">Optional</a></code>
- <code title="get /accounts/{account_id}/devices/settings">client.zero_trust.devices.settings.<a href="./src/cloudflare/resources/zero_trust/devices/settings.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/device_settings.py">Optional</a></code>
- <code title="patch /accounts/{account_id}/devices/settings">client.zero_trust.devices.settings.<a href="./src/cloudflare/resources/zero_trust/devices/settings.py">edit</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/setting_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/device_settings.py">Optional</a></code>

### Unrevoke

Types:

```python
from cloudflare.types.zero_trust.devices import UnrevokeCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/devices/unrevoke">client.zero_trust.devices.unrevoke.<a href="./src/cloudflare/resources/zero_trust/devices/unrevoke.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/unrevoke_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/unrevoke_create_response.py">Optional</a></code>

### OverrideCodes

Types:

```python
from cloudflare.types.zero_trust.devices import OverrideCodeListResponse
```

Methods:

- <code title="get /accounts/{account_id}/devices/{device_id}/override_codes">client.zero_trust.devices.override_codes.<a href="./src/cloudflare/resources/zero_trust/devices/override_codes.py">list</a>(device_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/override_code_list_response.py">Optional</a></code>

## IdentityProviders

Types:

```python
from cloudflare.types.zero_trust import (
    AzureAD,
    GenericOAuthConfig,
    IdentityProvider,
    IdentityProviderSCIMConfig,
    IdentityProviderType,
    IdentityProviderListResponse,
    IdentityProviderDeleteResponse,
)
```

Methods:

- <code title="post /{account_or_zone}/{account_or_zone_id}/access/identity_providers">client.zero_trust.identity_providers.<a href="./src/cloudflare/resources/zero_trust/identity_providers.py">create</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/identity_provider_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/identity_provider.py">Optional</a></code>
- <code title="put /{account_or_zone}/{account_or_zone_id}/access/identity_providers/{identity_provider_id}">client.zero_trust.identity_providers.<a href="./src/cloudflare/resources/zero_trust/identity_providers.py">update</a>(identity_provider_id, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/identity_provider_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/identity_provider.py">Optional</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/identity_providers">client.zero_trust.identity_providers.<a href="./src/cloudflare/resources/zero_trust/identity_providers.py">list</a>(\*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/identity_provider_list_response.py">SyncSinglePage[IdentityProviderListResponse]</a></code>
- <code title="delete /{account_or_zone}/{account_or_zone_id}/access/identity_providers/{identity_provider_id}">client.zero_trust.identity_providers.<a href="./src/cloudflare/resources/zero_trust/identity_providers.py">delete</a>(identity_provider_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/identity_provider_delete_response.py">Optional</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/identity_providers/{identity_provider_id}">client.zero_trust.identity_providers.<a href="./src/cloudflare/resources/zero_trust/identity_providers.py">get</a>(identity_provider_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/identity_provider.py">Optional</a></code>

## Organizations

Types:

```python
from cloudflare.types.zero_trust import LoginDesign, Organization, OrganizationRevokeUsersResponse
```

Methods:

- <code title="post /{account_or_zone}/{account_or_zone_id}/access/organizations">client.zero_trust.organizations.<a href="./src/cloudflare/resources/zero_trust/organizations.py">create</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/organization_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/organization.py">Optional</a></code>
- <code title="put /{account_or_zone}/{account_or_zone_id}/access/organizations">client.zero_trust.organizations.<a href="./src/cloudflare/resources/zero_trust/organizations.py">update</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/organization_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/organization.py">Optional</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/organizations">client.zero_trust.organizations.<a href="./src/cloudflare/resources/zero_trust/organizations.py">list</a>(\*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/organization.py">Optional</a></code>
- <code title="post /{account_or_zone}/{account_or_zone_id}/access/organizations/revoke_user">client.zero_trust.organizations.<a href="./src/cloudflare/resources/zero_trust/organizations.py">revoke_users</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/organization_revoke_users_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/organization_revoke_users_response.py">Optional</a></code>

## Seats

Types:

```python
from cloudflare.types.zero_trust import Seat, SeatEditResponse
```

Methods:

- <code title="patch /accounts/{account_id}/access/seats">client.zero_trust.seats.<a href="./src/cloudflare/resources/zero_trust/seats.py">edit</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/seat_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/seat_edit_response.py">Optional</a></code>

## Access

Types:

```python
from cloudflare.types.zero_trust import (
    AccessDevicePostureRule,
    AccessRule,
    AnyValidServiceTokenRule,
    AuthenticationMethodRule,
    AzureGroupRule,
    CertificateRule,
    CountryRule,
    DomainRule,
    EmailListRule,
    EmailRule,
    EveryoneRule,
    ExternalEvaluationRule,
    GitHubOrganizationRule,
    GroupRule,
    GSuiteGroupRule,
    IPListRule,
    IPRule,
    OktaGroupRule,
    SAMLGroupRule,
    ServiceTokenRule,
)
```

### Applications

Types:

```python
from cloudflare.types.zero_trust.access import (
    AllowedHeaders,
    AllowedIdPs,
    AllowedMethods,
    AllowedOrigins,
    AppID,
    Application,
    ApplicationPolicy,
    ApplicationSCIMConfig,
    ApplicationType,
    CORSHeaders,
    Decision,
    OIDCSaaSApp,
    SaaSAppNameFormat,
    SaaSAppNameIDFormat,
    SaaSAppSource,
    SAMLSaaSApp,
    SCIMConfigAuthenticationHTTPBasic,
    SCIMConfigAuthenticationOAuthBearerToken,
    SCIMConfigAuthenticationOauth2,
    SCIMConfigMapping,
    SelfHostedDomains,
    ApplicationCreateResponse,
    ApplicationUpdateResponse,
    ApplicationListResponse,
    ApplicationDeleteResponse,
    ApplicationGetResponse,
    ApplicationRevokeTokensResponse,
)
```

Methods:

- <code title="post /{account_or_zone}/{account_or_zone_id}/access/apps">client.zero_trust.access.applications.<a href="./src/cloudflare/resources/zero_trust/access/applications/applications.py">create</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/application_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/application_create_response.py">Optional</a></code>
- <code title="put /{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}">client.zero_trust.access.applications.<a href="./src/cloudflare/resources/zero_trust/access/applications/applications.py">update</a>(app_id, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/application_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/application_update_response.py">Optional</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/apps">client.zero_trust.access.applications.<a href="./src/cloudflare/resources/zero_trust/access/applications/applications.py">list</a>(\*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/application_list_response.py">SyncSinglePage[ApplicationListResponse]</a></code>
- <code title="delete /{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}">client.zero_trust.access.applications.<a href="./src/cloudflare/resources/zero_trust/access/applications/applications.py">delete</a>(app_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/application_delete_response.py">Optional</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}">client.zero_trust.access.applications.<a href="./src/cloudflare/resources/zero_trust/access/applications/applications.py">get</a>(app_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/application_get_response.py">Optional</a></code>
- <code title="post /{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}/revoke_tokens">client.zero_trust.access.applications.<a href="./src/cloudflare/resources/zero_trust/access/applications/applications.py">revoke_tokens</a>(app_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/application_revoke_tokens_response.py">object</a></code>

#### CAs

Types:

```python
from cloudflare.types.zero_trust.access.applications import (
    CA,
    CACreateResponse,
    CADeleteResponse,
    CAGetResponse,
)
```

Methods:

- <code title="post /{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}/ca">client.zero_trust.access.applications.cas.<a href="./src/cloudflare/resources/zero_trust/access/applications/cas.py">create</a>(app_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/applications/ca_create_response.py">object</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/apps/ca">client.zero_trust.access.applications.cas.<a href="./src/cloudflare/resources/zero_trust/access/applications/cas.py">list</a>(\*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/applications/ca.py">SyncSinglePage[CA]</a></code>
- <code title="delete /{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}/ca">client.zero_trust.access.applications.cas.<a href="./src/cloudflare/resources/zero_trust/access/applications/cas.py">delete</a>(app_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/applications/ca_delete_response.py">Optional</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}/ca">client.zero_trust.access.applications.cas.<a href="./src/cloudflare/resources/zero_trust/access/applications/cas.py">get</a>(app_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/applications/ca_get_response.py">object</a></code>

#### UserPolicyChecks

Types:

```python
from cloudflare.types.zero_trust.access.applications import (
    UserPolicyCheckGeo,
    UserPolicyCheckListResponse,
)
```

Methods:

- <code title="get /{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}/user_policy_checks">client.zero_trust.access.applications.user_policy_checks.<a href="./src/cloudflare/resources/zero_trust/access/applications/user_policy_checks.py">list</a>(app_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/applications/user_policy_check_list_response.py">Optional</a></code>

#### Policies

Types:

```python
from cloudflare.types.zero_trust.access.applications import (
    ApprovalGroup,
    Policy,
    PolicyDeleteResponse,
)
```

Methods:

- <code title="post /{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}/policies">client.zero_trust.access.applications.policies.<a href="./src/cloudflare/resources/zero_trust/access/applications/policies.py">create</a>(app_id, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/applications/policy_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/application_policy.py">Optional</a></code>
- <code title="put /{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}/policies/{policy_id}">client.zero_trust.access.applications.policies.<a href="./src/cloudflare/resources/zero_trust/access/applications/policies.py">update</a>(policy_id, \*, app_id, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/applications/policy_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/application_policy.py">Optional</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}/policies">client.zero_trust.access.applications.policies.<a href="./src/cloudflare/resources/zero_trust/access/applications/policies.py">list</a>(app_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/application_policy.py">SyncSinglePage[ApplicationPolicy]</a></code>
- <code title="delete /{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}/policies/{policy_id}">client.zero_trust.access.applications.policies.<a href="./src/cloudflare/resources/zero_trust/access/applications/policies.py">delete</a>(policy_id, \*, app_id, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/applications/policy_delete_response.py">Optional</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}/policies/{policy_id}">client.zero_trust.access.applications.policies.<a href="./src/cloudflare/resources/zero_trust/access/applications/policies.py">get</a>(policy_id, \*, app_id, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/application_policy.py">Optional</a></code>

#### PolicyTests

Types:

```python
from cloudflare.types.zero_trust.access.applications import (
    PolicyTestCreateResponse,
    PolicyTestGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/access/policy-tests">client.zero_trust.access.applications.policy_tests.<a href="./src/cloudflare/resources/zero_trust/access/applications/policy_tests/policy_tests.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/applications/policy_test_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/applications/policy_test_create_response.py">PolicyTestCreateResponse</a></code>
- <code title="get /accounts/{account_id}/access/policy-tests/{policy_test_id}">client.zero_trust.access.applications.policy_tests.<a href="./src/cloudflare/resources/zero_trust/access/applications/policy_tests/policy_tests.py">get</a>(policy_test_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/applications/policy_test_get_response.py">PolicyTestGetResponse</a></code>

##### Users

Types:

```python
from cloudflare.types.zero_trust.access.applications.policy_tests import UserListResponse
```

Methods:

- <code title="get /accounts/{account_id}/access/policy-tests/{policy_test_id}/users">client.zero_trust.access.applications.policy_tests.users.<a href="./src/cloudflare/resources/zero_trust/access/applications/policy_tests/users.py">list</a>(policy_test_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/applications/policy_tests/user_list_response.py">UserListResponse</a></code>

### Certificates

Types:

```python
from cloudflare.types.zero_trust.access import (
    AssociatedHostnames,
    Certificate,
    CertificateDeleteResponse,
)
```

Methods:

- <code title="post /{account_or_zone}/{account_or_zone_id}/access/certificates">client.zero_trust.access.certificates.<a href="./src/cloudflare/resources/zero_trust/access/certificates/certificates.py">create</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/certificate_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/certificate.py">Optional</a></code>
- <code title="put /{account_or_zone}/{account_or_zone_id}/access/certificates/{certificate_id}">client.zero_trust.access.certificates.<a href="./src/cloudflare/resources/zero_trust/access/certificates/certificates.py">update</a>(certificate_id, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/certificate_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/certificate.py">Optional</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/certificates">client.zero_trust.access.certificates.<a href="./src/cloudflare/resources/zero_trust/access/certificates/certificates.py">list</a>(\*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/certificate.py">SyncSinglePage[Certificate]</a></code>
- <code title="delete /{account_or_zone}/{account_or_zone_id}/access/certificates/{certificate_id}">client.zero_trust.access.certificates.<a href="./src/cloudflare/resources/zero_trust/access/certificates/certificates.py">delete</a>(certificate_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/certificate_delete_response.py">Optional</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/certificates/{certificate_id}">client.zero_trust.access.certificates.<a href="./src/cloudflare/resources/zero_trust/access/certificates/certificates.py">get</a>(certificate_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/certificate.py">Optional</a></code>

#### Settings

Types:

```python
from cloudflare.types.zero_trust.access.certificates import (
    CertificateSettings,
    SettingUpdateResponse,
    SettingGetResponse,
)
```

Methods:

- <code title="put /{account_or_zone}/{account_or_zone_id}/access/certificates/settings">client.zero_trust.access.certificates.settings.<a href="./src/cloudflare/resources/zero_trust/access/certificates/settings.py">update</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/certificates/setting_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/certificates/setting_update_response.py">Optional</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/certificates/settings">client.zero_trust.access.certificates.settings.<a href="./src/cloudflare/resources/zero_trust/access/certificates/settings.py">get</a>(\*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/certificates/setting_get_response.py">Optional</a></code>

### Groups

Types:

```python
from cloudflare.types.zero_trust.access import ZeroTrustGroup, GroupDeleteResponse
```

Methods:

- <code title="post /{account_or_zone}/{account_or_zone_id}/access/groups">client.zero_trust.access.groups.<a href="./src/cloudflare/resources/zero_trust/access/groups.py">create</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/group_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/zero_trust_group.py">Optional</a></code>
- <code title="put /{account_or_zone}/{account_or_zone_id}/access/groups/{group_id}">client.zero_trust.access.groups.<a href="./src/cloudflare/resources/zero_trust/access/groups.py">update</a>(group_id, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/group_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/zero_trust_group.py">Optional</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/groups">client.zero_trust.access.groups.<a href="./src/cloudflare/resources/zero_trust/access/groups.py">list</a>(\*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/zero_trust_group.py">SyncSinglePage[ZeroTrustGroup]</a></code>
- <code title="delete /{account_or_zone}/{account_or_zone_id}/access/groups/{group_id}">client.zero_trust.access.groups.<a href="./src/cloudflare/resources/zero_trust/access/groups.py">delete</a>(group_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/group_delete_response.py">Optional</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/groups/{group_id}">client.zero_trust.access.groups.<a href="./src/cloudflare/resources/zero_trust/access/groups.py">get</a>(group_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/zero_trust_group.py">Optional</a></code>

### ServiceTokens

Types:

```python
from cloudflare.types.zero_trust.access import (
    ServiceToken,
    ServiceTokenCreateResponse,
    ServiceTokenRotateResponse,
)
```

Methods:

- <code title="post /{account_or_zone}/{account_or_zone_id}/access/service_tokens">client.zero_trust.access.service_tokens.<a href="./src/cloudflare/resources/zero_trust/access/service_tokens.py">create</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/service_token_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/service_token_create_response.py">Optional</a></code>
- <code title="put /{account_or_zone}/{account_or_zone_id}/access/service_tokens/{service_token_id}">client.zero_trust.access.service_tokens.<a href="./src/cloudflare/resources/zero_trust/access/service_tokens.py">update</a>(service_token_id, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/service_token_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/service_token.py">Optional</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/service_tokens">client.zero_trust.access.service_tokens.<a href="./src/cloudflare/resources/zero_trust/access/service_tokens.py">list</a>(\*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/service_token.py">SyncSinglePage[ServiceToken]</a></code>
- <code title="delete /{account_or_zone}/{account_or_zone_id}/access/service_tokens/{service_token_id}">client.zero_trust.access.service_tokens.<a href="./src/cloudflare/resources/zero_trust/access/service_tokens.py">delete</a>(service_token_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/service_token.py">Optional</a></code>
- <code title="get /{account_or_zone}/{account_or_zone_id}/access/service_tokens/{service_token_id}">client.zero_trust.access.service_tokens.<a href="./src/cloudflare/resources/zero_trust/access/service_tokens.py">get</a>(service_token_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/service_token.py">Optional</a></code>
- <code title="post /accounts/{account_id}/access/service_tokens/{service_token_id}/refresh">client.zero_trust.access.service_tokens.<a href="./src/cloudflare/resources/zero_trust/access/service_tokens.py">refresh</a>(service_token_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/service_token.py">Optional</a></code>
- <code title="post /accounts/{account_id}/access/service_tokens/{service_token_id}/rotate">client.zero_trust.access.service_tokens.<a href="./src/cloudflare/resources/zero_trust/access/service_tokens.py">rotate</a>(service_token_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/service_token_rotate_response.py">Optional</a></code>

### Bookmarks

Types:

```python
from cloudflare.types.zero_trust.access import Bookmark, BookmarkDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/access/bookmarks/{bookmark_id}">client.zero_trust.access.bookmarks.<a href="./src/cloudflare/resources/zero_trust/access/bookmarks.py">create</a>(bookmark_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/bookmark_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/bookmark.py">Optional</a></code>
- <code title="put /accounts/{account_id}/access/bookmarks/{bookmark_id}">client.zero_trust.access.bookmarks.<a href="./src/cloudflare/resources/zero_trust/access/bookmarks.py">update</a>(bookmark_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/bookmark_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/bookmark.py">Optional</a></code>
- <code title="get /accounts/{account_id}/access/bookmarks">client.zero_trust.access.bookmarks.<a href="./src/cloudflare/resources/zero_trust/access/bookmarks.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/bookmark.py">SyncSinglePage[Bookmark]</a></code>
- <code title="delete /accounts/{account_id}/access/bookmarks/{bookmark_id}">client.zero_trust.access.bookmarks.<a href="./src/cloudflare/resources/zero_trust/access/bookmarks.py">delete</a>(bookmark_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/bookmark_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/access/bookmarks/{bookmark_id}">client.zero_trust.access.bookmarks.<a href="./src/cloudflare/resources/zero_trust/access/bookmarks.py">get</a>(bookmark_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/bookmark.py">Optional</a></code>

### Keys

Types:

```python
from cloudflare.types.zero_trust.access import KeyUpdateResponse, KeyGetResponse, KeyRotateResponse
```

Methods:

- <code title="put /accounts/{account_id}/access/keys">client.zero_trust.access.keys.<a href="./src/cloudflare/resources/zero_trust/access/keys.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/key_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/key_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/access/keys">client.zero_trust.access.keys.<a href="./src/cloudflare/resources/zero_trust/access/keys.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/key_get_response.py">Optional</a></code>
- <code title="post /accounts/{account_id}/access/keys/rotate">client.zero_trust.access.keys.<a href="./src/cloudflare/resources/zero_trust/access/keys.py">rotate</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/key_rotate_response.py">Optional</a></code>

### Logs

#### AccessRequests

Types:

```python
from cloudflare.types.zero_trust.access.logs import AccessRequests, AccessRequestListResponse
```

Methods:

- <code title="get /accounts/{account_id}/access/logs/access_requests">client.zero_trust.access.logs.access_requests.<a href="./src/cloudflare/resources/zero_trust/access/logs/access_requests.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/logs/access_request_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/logs/access_request_list_response.py">Optional</a></code>

### Users

Types:

```python
from cloudflare.types.zero_trust.access import AccessUser
```

Methods:

- <code title="get /accounts/{account_id}/access/users">client.zero_trust.access.users.<a href="./src/cloudflare/resources/zero_trust/access/users/users.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/access_user.py">SyncSinglePage[AccessUser]</a></code>

#### ActiveSessions

Types:

```python
from cloudflare.types.zero_trust.access.users import (
    ActiveSessionListResponse,
    ActiveSessionGetResponse,
)
```

Methods:

- <code title="get /accounts/{account_id}/access/users/{user_id}/active_sessions">client.zero_trust.access.users.active_sessions.<a href="./src/cloudflare/resources/zero_trust/access/users/active_sessions.py">list</a>(user_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/users/active_session_list_response.py">SyncSinglePage[ActiveSessionListResponse]</a></code>
- <code title="get /accounts/{account_id}/access/users/{user_id}/active_sessions/{nonce}">client.zero_trust.access.users.active_sessions.<a href="./src/cloudflare/resources/zero_trust/access/users/active_sessions.py">get</a>(nonce, \*, account_id, user_id) -> <a href="./src/cloudflare/types/zero_trust/access/users/active_session_get_response.py">Optional</a></code>

#### LastSeenIdentity

Types:

```python
from cloudflare.types.zero_trust.access.users import Identity
```

Methods:

- <code title="get /accounts/{account_id}/access/users/{user_id}/last_seen_identity">client.zero_trust.access.users.last_seen_identity.<a href="./src/cloudflare/resources/zero_trust/access/users/last_seen_identity.py">get</a>(user_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/users/identity.py">Optional</a></code>

#### FailedLogins

Types:

```python
from cloudflare.types.zero_trust.access.users import FailedLoginListResponse
```

Methods:

- <code title="get /accounts/{account_id}/access/users/{user_id}/failed_logins">client.zero_trust.access.users.failed_logins.<a href="./src/cloudflare/resources/zero_trust/access/users/failed_logins.py">list</a>(user_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/users/failed_login_list_response.py">SyncSinglePage[FailedLoginListResponse]</a></code>

### CustomPages

Types:

```python
from cloudflare.types.zero_trust.access import (
    CustomPage,
    CustomPageWithoutHTML,
    CustomPageDeleteResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/access/custom_pages">client.zero_trust.access.custom_pages.<a href="./src/cloudflare/resources/zero_trust/access/custom_pages.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/custom_page_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/custom_page_without_html.py">Optional</a></code>
- <code title="put /accounts/{account_id}/access/custom_pages/{custom_page_id}">client.zero_trust.access.custom_pages.<a href="./src/cloudflare/resources/zero_trust/access/custom_pages.py">update</a>(custom_page_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/custom_page_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/custom_page_without_html.py">Optional</a></code>
- <code title="get /accounts/{account_id}/access/custom_pages">client.zero_trust.access.custom_pages.<a href="./src/cloudflare/resources/zero_trust/access/custom_pages.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/custom_page_without_html.py">SyncSinglePage[CustomPageWithoutHTML]</a></code>
- <code title="delete /accounts/{account_id}/access/custom_pages/{custom_page_id}">client.zero_trust.access.custom_pages.<a href="./src/cloudflare/resources/zero_trust/access/custom_pages.py">delete</a>(custom_page_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/custom_page_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/access/custom_pages/{custom_page_id}">client.zero_trust.access.custom_pages.<a href="./src/cloudflare/resources/zero_trust/access/custom_pages.py">get</a>(custom_page_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/custom_page.py">Optional</a></code>

### Tags

Types:

```python
from cloudflare.types.zero_trust.access import Tag, TagDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/access/tags">client.zero_trust.access.tags.<a href="./src/cloudflare/resources/zero_trust/access/tags.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/tag_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/tag.py">Optional</a></code>
- <code title="put /accounts/{account_id}/access/tags/{tag_name}">client.zero_trust.access.tags.<a href="./src/cloudflare/resources/zero_trust/access/tags.py">update</a>(tag_name, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/tag_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/tag.py">Optional</a></code>
- <code title="get /accounts/{account_id}/access/tags">client.zero_trust.access.tags.<a href="./src/cloudflare/resources/zero_trust/access/tags.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/tag.py">SyncSinglePage[Tag]</a></code>
- <code title="delete /accounts/{account_id}/access/tags/{tag_name}">client.zero_trust.access.tags.<a href="./src/cloudflare/resources/zero_trust/access/tags.py">delete</a>(tag_name, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/tag_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/access/tags/{tag_name}">client.zero_trust.access.tags.<a href="./src/cloudflare/resources/zero_trust/access/tags.py">get</a>(tag_name, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/tag.py">Optional</a></code>

### Policies

Types:

```python
from cloudflare.types.zero_trust.access import (
    PolicyCreateResponse,
    PolicyUpdateResponse,
    PolicyListResponse,
    PolicyDeleteResponse,
    PolicyGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/access/policies">client.zero_trust.access.policies.<a href="./src/cloudflare/resources/zero_trust/access/policies.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/policy_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/policy_create_response.py">Optional</a></code>
- <code title="put /accounts/{account_id}/access/policies/{policy_id}">client.zero_trust.access.policies.<a href="./src/cloudflare/resources/zero_trust/access/policies.py">update</a>(policy_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/policy_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/policy_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/access/policies">client.zero_trust.access.policies.<a href="./src/cloudflare/resources/zero_trust/access/policies.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/policy_list_response.py">SyncSinglePage[PolicyListResponse]</a></code>
- <code title="delete /accounts/{account_id}/access/policies/{policy_id}">client.zero_trust.access.policies.<a href="./src/cloudflare/resources/zero_trust/access/policies.py">delete</a>(policy_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/policy_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/access/policies/{policy_id}">client.zero_trust.access.policies.<a href="./src/cloudflare/resources/zero_trust/access/policies.py">get</a>(policy_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/policy_get_response.py">Optional</a></code>

## DEX

Types:

```python
from cloudflare.types.zero_trust import (
    DeviceExperienceMonitor,
    NetworkPath,
    NetworkPathResponse,
    Percentiles,
)
```

### Colos

Types:

```python
from cloudflare.types.zero_trust.dex import ColoListResponse
```

Methods:

- <code title="get /accounts/{account_id}/dex/colos">client.zero_trust.dex.colos.<a href="./src/cloudflare/resources/zero_trust/dex/colos.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dex/colo_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dex/colo_list_response.py">SyncSinglePage[object]</a></code>

### FleetStatus

Types:

```python
from cloudflare.types.zero_trust.dex import LiveStat, FleetStatusLiveResponse
```

Methods:

- <code title="get /accounts/{account_id}/dex/fleet-status/live">client.zero_trust.dex.fleet_status.<a href="./src/cloudflare/resources/zero_trust/dex/fleet_status/fleet_status.py">live</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dex/fleet_status_live_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dex/fleet_status_live_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/dex/fleet-status/over-time">client.zero_trust.dex.fleet_status.<a href="./src/cloudflare/resources/zero_trust/dex/fleet_status/fleet_status.py">over_time</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dex/fleet_status_over_time_params.py">params</a>) -> None</code>

#### Devices

Types:

```python
from cloudflare.types.zero_trust.dex.fleet_status import DeviceListResponse
```

Methods:

- <code title="get /accounts/{account_id}/dex/fleet-status/devices">client.zero_trust.dex.fleet_status.devices.<a href="./src/cloudflare/resources/zero_trust/dex/fleet_status/devices.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dex/fleet_status/device_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dex/fleet_status/device_list_response.py">SyncV4PagePaginationArray[DeviceListResponse]</a></code>

### HTTPTests

Types:

```python
from cloudflare.types.zero_trust.dex import HTTPDetails
```

Methods:

- <code title="get /accounts/{account_id}/dex/http-tests/{test_id}">client.zero_trust.dex.http_tests.<a href="./src/cloudflare/resources/zero_trust/dex/http_tests/http_tests.py">get</a>(test_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dex/http_test_get_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dex/http_details.py">Optional</a></code>

#### Percentiles

Types:

```python
from cloudflare.types.zero_trust.dex.http_tests import HTTPDetailsPercentiles, TestStatOverTime
```

Methods:

- <code title="get /accounts/{account_id}/dex/http-tests/{test_id}/percentiles">client.zero_trust.dex.http_tests.percentiles.<a href="./src/cloudflare/resources/zero_trust/dex/http_tests/percentiles.py">get</a>(test_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dex/http_tests/percentile_get_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dex/http_tests/http_details_percentiles.py">Optional</a></code>

### Tests

Types:

```python
from cloudflare.types.zero_trust.dex import AggregateTimePeriod, Tests, TestListResponse
```

Methods:

- <code title="get /accounts/{account_id}/dex/tests">client.zero_trust.dex.tests.<a href="./src/cloudflare/resources/zero_trust/dex/tests/tests.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dex/test_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dex/test_list_response.py">SyncV4PagePagination[TestListResponse]</a></code>

#### UniqueDevices

Types:

```python
from cloudflare.types.zero_trust.dex.tests import UniqueDevices
```

Methods:

- <code title="get /accounts/{account_id}/dex/tests/unique-devices">client.zero_trust.dex.tests.unique_devices.<a href="./src/cloudflare/resources/zero_trust/dex/tests/unique_devices.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dex/tests/unique_device_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dex/tests/unique_devices.py">Optional</a></code>

### TracerouteTestResults

#### NetworkPath

Types:

```python
from cloudflare.types.zero_trust.dex.traceroute_test_results import NetworkPathGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/dex/traceroute-test-results/{test_result_id}/network-path">client.zero_trust.dex.traceroute_test_results.network_path.<a href="./src/cloudflare/resources/zero_trust/dex/traceroute_test_results/network_path.py">get</a>(test_result_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dex/traceroute_test_results/network_path_get_response.py">Optional</a></code>

### TracerouteTests

Types:

```python
from cloudflare.types.zero_trust.dex import Traceroute, TracerouteTestPercentilesResponse
```

Methods:

- <code title="get /accounts/{account_id}/dex/traceroute-tests/{test_id}">client.zero_trust.dex.traceroute_tests.<a href="./src/cloudflare/resources/zero_trust/dex/traceroute_tests.py">get</a>(test_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dex/traceroute_test_get_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dex/traceroute.py">Optional</a></code>
- <code title="get /accounts/{account_id}/dex/traceroute-tests/{test_id}/network-path">client.zero_trust.dex.traceroute_tests.<a href="./src/cloudflare/resources/zero_trust/dex/traceroute_tests.py">network_path</a>(test_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dex/traceroute_test_network_path_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/network_path_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/dex/traceroute-tests/{test_id}/percentiles">client.zero_trust.dex.traceroute_tests.<a href="./src/cloudflare/resources/zero_trust/dex/traceroute_tests.py">percentiles</a>(test_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dex/traceroute_test_percentiles_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dex/traceroute_test_percentiles_response.py">Optional</a></code>

## Tunnels

Types:

```python
from cloudflare.types.zero_trust import (
    Connection,
    TunnelCreateResponse,
    TunnelListResponse,
    TunnelDeleteResponse,
    TunnelEditResponse,
    TunnelGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/cfd_tunnel">client.zero_trust.tunnels.<a href="./src/cloudflare/resources/zero_trust/tunnels/tunnels.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/tunnel_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/tunnel_create_response.py">TunnelCreateResponse</a></code>
- <code title="get /accounts/{account_id}/cfd_tunnel">client.zero_trust.tunnels.<a href="./src/cloudflare/resources/zero_trust/tunnels/tunnels.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/tunnel_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/tunnel_list_response.py">SyncV4PagePaginationArray[TunnelListResponse]</a></code>
- <code title="delete /accounts/{account_id}/cfd_tunnel/{tunnel_id}">client.zero_trust.tunnels.<a href="./src/cloudflare/resources/zero_trust/tunnels/tunnels.py">delete</a>(tunnel_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/tunnel_delete_response.py">TunnelDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/cfd_tunnel/{tunnel_id}">client.zero_trust.tunnels.<a href="./src/cloudflare/resources/zero_trust/tunnels/tunnels.py">edit</a>(tunnel_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/tunnel_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/tunnel_edit_response.py">TunnelEditResponse</a></code>
- <code title="get /accounts/{account_id}/cfd_tunnel/{tunnel_id}">client.zero_trust.tunnels.<a href="./src/cloudflare/resources/zero_trust/tunnels/tunnels.py">get</a>(tunnel_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/tunnel_get_response.py">TunnelGetResponse</a></code>

### Configurations

Types:

```python
from cloudflare.types.zero_trust.tunnels import (
    ConfigurationUpdateResponse,
    ConfigurationGetResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/cfd_tunnel/{tunnel_id}/configurations">client.zero_trust.tunnels.configurations.<a href="./src/cloudflare/resources/zero_trust/tunnels/configurations.py">update</a>(tunnel_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/tunnels/configuration_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/tunnels/configuration_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/cfd_tunnel/{tunnel_id}/configurations">client.zero_trust.tunnels.configurations.<a href="./src/cloudflare/resources/zero_trust/tunnels/configurations.py">get</a>(tunnel_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/tunnels/configuration_get_response.py">Optional</a></code>

### Connections

Types:

```python
from cloudflare.types.zero_trust.tunnels import (
    Client,
    ConnectionDeleteResponse,
    ConnectionGetResponse,
)
```

Methods:

- <code title="delete /accounts/{account_id}/cfd_tunnel/{tunnel_id}/connections">client.zero_trust.tunnels.connections.<a href="./src/cloudflare/resources/zero_trust/tunnels/connections.py">delete</a>(tunnel_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/tunnels/connection_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/tunnels/connection_delete_response.py">object</a></code>
- <code title="get /accounts/{account_id}/cfd_tunnel/{tunnel_id}/connections">client.zero_trust.tunnels.connections.<a href="./src/cloudflare/resources/zero_trust/tunnels/connections.py">get</a>(tunnel_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/tunnels/connection_get_response.py">Optional</a></code>

### Token

Types:

```python
from cloudflare.types.zero_trust.tunnels import TokenGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/cfd_tunnel/{tunnel_id}/token">client.zero_trust.tunnels.token.<a href="./src/cloudflare/resources/zero_trust/tunnels/token.py">get</a>(tunnel_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/tunnels/token_get_response.py">TokenGetResponse</a></code>

### Connectors

Methods:

- <code title="get /accounts/{account_id}/cfd_tunnel/{tunnel_id}/connectors/{connector_id}">client.zero_trust.tunnels.connectors.<a href="./src/cloudflare/resources/zero_trust/tunnels/connectors.py">get</a>(connector_id, \*, account_id, tunnel_id) -> <a href="./src/cloudflare/types/zero_trust/tunnels/client.py">Client</a></code>

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
from cloudflare.types.zero_trust.dlp import Dataset, DatasetArray, DatasetCreation
```

Methods:

- <code title="post /accounts/{account_id}/dlp/datasets">client.zero_trust.dlp.datasets.<a href="./src/cloudflare/resources/zero_trust/dlp/datasets/datasets.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/dataset_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/dataset_creation.py">Optional</a></code>
- <code title="put /accounts/{account_id}/dlp/datasets/{dataset_id}">client.zero_trust.dlp.datasets.<a href="./src/cloudflare/resources/zero_trust/dlp/datasets/datasets.py">update</a>(dataset_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/dataset_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/dataset.py">Optional</a></code>
- <code title="get /accounts/{account_id}/dlp/datasets">client.zero_trust.dlp.datasets.<a href="./src/cloudflare/resources/zero_trust/dlp/datasets/datasets.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/dataset.py">SyncSinglePage[Dataset]</a></code>
- <code title="delete /accounts/{account_id}/dlp/datasets/{dataset_id}">client.zero_trust.dlp.datasets.<a href="./src/cloudflare/resources/zero_trust/dlp/datasets/datasets.py">delete</a>(dataset_id, \*, account_id) -> None</code>
- <code title="get /accounts/{account_id}/dlp/datasets/{dataset_id}">client.zero_trust.dlp.datasets.<a href="./src/cloudflare/resources/zero_trust/dlp/datasets/datasets.py">get</a>(dataset_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/dataset.py">Optional</a></code>

#### Upload

Types:

```python
from cloudflare.types.zero_trust.dlp.datasets import NewVersion
```

Methods:

- <code title="post /accounts/{account_id}/dlp/datasets/{dataset_id}/upload">client.zero_trust.dlp.datasets.upload.<a href="./src/cloudflare/resources/zero_trust/dlp/datasets/upload.py">create</a>(dataset_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/datasets/new_version.py">Optional</a></code>
- <code title="post /accounts/{account_id}/dlp/datasets/{dataset_id}/upload/{version}">client.zero_trust.dlp.datasets.upload.<a href="./src/cloudflare/resources/zero_trust/dlp/datasets/upload.py">edit</a>(version, \*, account_id, dataset_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/datasets/upload_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/dataset.py">Optional</a></code>

#### Versions

Types:

```python
from cloudflare.types.zero_trust.dlp.datasets import VersionCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/dlp/datasets/{dataset_id}/versions/{version}">client.zero_trust.dlp.datasets.versions.<a href="./src/cloudflare/resources/zero_trust/dlp/datasets/versions/versions.py">create</a>(version, \*, account_id, dataset_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/datasets/version_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/datasets/version_create_response.py">Optional</a></code>

##### Entries

Types:

```python
from cloudflare.types.zero_trust.dlp.datasets.versions import EntryCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/dlp/datasets/{dataset_id}/versions/{version}/entries/{entry_id}">client.zero_trust.dlp.datasets.versions.entries.<a href="./src/cloudflare/resources/zero_trust/dlp/datasets/versions/entries.py">create</a>(entry_id, \*, account_id, dataset_id, version, \*\*<a href="src/cloudflare/types/zero_trust/dlp/datasets/versions/entry_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/datasets/versions/entry_create_response.py">Optional</a></code>

### Patterns

Types:

```python
from cloudflare.types.zero_trust.dlp import PatternValidateResponse
```

Methods:

- <code title="post /accounts/{account_id}/dlp/patterns/validate">client.zero_trust.dlp.patterns.<a href="./src/cloudflare/resources/zero_trust/dlp/patterns.py">validate</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/pattern_validate_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/pattern_validate_response.py">Optional</a></code>

### PayloadLogs

Types:

```python
from cloudflare.types.zero_trust.dlp import PayloadLogUpdateResponse, PayloadLogGetResponse
```

Methods:

- <code title="put /accounts/{account_id}/dlp/payload_log">client.zero_trust.dlp.payload_logs.<a href="./src/cloudflare/resources/zero_trust/dlp/payload_logs.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/payload_log_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/payload_log_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/dlp/payload_log">client.zero_trust.dlp.payload_logs.<a href="./src/cloudflare/resources/zero_trust/dlp/payload_logs.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/payload_log_get_response.py">Optional</a></code>

### Profiles

Types:

```python
from cloudflare.types.zero_trust.dlp import ContextAwareness, Profile, SkipConfiguration
```

Methods:

- <code title="get /accounts/{account_id}/dlp/profiles">client.zero_trust.dlp.profiles.<a href="./src/cloudflare/resources/zero_trust/dlp/profiles/profiles.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/profile_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/profile.py">SyncSinglePage[Profile]</a></code>
- <code title="get /accounts/{account_id}/dlp/profiles/{profile_id}">client.zero_trust.dlp.profiles.<a href="./src/cloudflare/resources/zero_trust/dlp/profiles/profiles.py">get</a>(profile_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/profile.py">Optional</a></code>

#### Custom

Types:

```python
from cloudflare.types.zero_trust.dlp.profiles import (
    CustomProfile,
    Pattern,
    CustomCreateResponse,
    CustomDeleteResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/dlp/profiles/custom">client.zero_trust.dlp.profiles.custom.<a href="./src/cloudflare/resources/zero_trust/dlp/profiles/custom.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/profiles/custom_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/profiles/custom_create_response.py">Optional</a></code>
- <code title="put /accounts/{account_id}/dlp/profiles/custom/{profile_id}">client.zero_trust.dlp.profiles.custom.<a href="./src/cloudflare/resources/zero_trust/dlp/profiles/custom.py">update</a>(profile_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/profiles/custom_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/profile.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/dlp/profiles/custom/{profile_id}">client.zero_trust.dlp.profiles.custom.<a href="./src/cloudflare/resources/zero_trust/dlp/profiles/custom.py">delete</a>(profile_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/profiles/custom_delete_response.py">object</a></code>
- <code title="get /accounts/{account_id}/dlp/profiles/custom/{profile_id}">client.zero_trust.dlp.profiles.custom.<a href="./src/cloudflare/resources/zero_trust/dlp/profiles/custom.py">get</a>(profile_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/profile.py">Optional</a></code>

#### Predefined

Types:

```python
from cloudflare.types.zero_trust.dlp.profiles import PredefinedProfile
```

Methods:

- <code title="put /accounts/{account_id}/dlp/profiles/predefined/{profile_id}">client.zero_trust.dlp.profiles.predefined.<a href="./src/cloudflare/resources/zero_trust/dlp/profiles/predefined.py">update</a>(profile_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/profiles/predefined_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/profile.py">Optional</a></code>
- <code title="get /accounts/{account_id}/dlp/profiles/predefined/{profile_id}">client.zero_trust.dlp.profiles.predefined.<a href="./src/cloudflare/resources/zero_trust/dlp/profiles/predefined.py">get</a>(profile_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/profile.py">Optional</a></code>

### Limits

Types:

```python
from cloudflare.types.zero_trust.dlp import LimitListResponse
```

Methods:

- <code title="get /accounts/{account_id}/dlp/limits">client.zero_trust.dlp.limits.<a href="./src/cloudflare/resources/zero_trust/dlp/limits.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/limit_list_response.py">Optional</a></code>

## Gateway

Types:

```python
from cloudflare.types.zero_trust import GatewayCreateResponse, GatewayListResponse
```

Methods:

- <code title="post /accounts/{account_id}/gateway">client.zero_trust.gateway.<a href="./src/cloudflare/resources/zero_trust/gateway/gateway.py">create</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway_create_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/gateway">client.zero_trust.gateway.<a href="./src/cloudflare/resources/zero_trust/gateway/gateway.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway_list_response.py">Optional</a></code>

### AuditSSHSettings

Types:

```python
from cloudflare.types.zero_trust.gateway import GatewaySettings
```

Methods:

- <code title="put /accounts/{account_id}/gateway/audit_ssh_settings">client.zero_trust.gateway.audit_ssh_settings.<a href="./src/cloudflare/resources/zero_trust/gateway/audit_ssh_settings.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/audit_ssh_setting_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/gateway_settings.py">Optional</a></code>
- <code title="get /accounts/{account_id}/gateway/audit_ssh_settings">client.zero_trust.gateway.audit_ssh_settings.<a href="./src/cloudflare/resources/zero_trust/gateway/audit_ssh_settings.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/gateway_settings.py">Optional</a></code>

### Categories

Types:

```python
from cloudflare.types.zero_trust.gateway import Category
```

Methods:

- <code title="get /accounts/{account_id}/gateway/categories">client.zero_trust.gateway.categories.<a href="./src/cloudflare/resources/zero_trust/gateway/categories.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/category.py">SyncSinglePage[Category]</a></code>

### AppTypes

Types:

```python
from cloudflare.types.zero_trust.gateway import AppType
```

Methods:

- <code title="get /accounts/{account_id}/gateway/app_types">client.zero_trust.gateway.app_types.<a href="./src/cloudflare/resources/zero_trust/gateway/app_types.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/app_type.py">SyncSinglePage[AppType]</a></code>

### Configurations

Types:

```python
from cloudflare.types.zero_trust.gateway import (
    ActivityLogSettings,
    AntiVirusSettings,
    BlockPageSettings,
    BodyScanningSettings,
    BrowserIsolationSettings,
    CustomCertificateSettings,
    ExtendedEmailMatching,
    FipsSettings,
    GatewayConfigurationSettings,
    NotificationSettings,
    ProtocolDetection,
    TLSSettings,
    ConfigurationUpdateResponse,
    ConfigurationEditResponse,
    ConfigurationGetResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/gateway/configuration">client.zero_trust.gateway.configurations.<a href="./src/cloudflare/resources/zero_trust/gateway/configurations/configurations.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/configuration_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/configuration_update_response.py">Optional</a></code>
- <code title="patch /accounts/{account_id}/gateway/configuration">client.zero_trust.gateway.configurations.<a href="./src/cloudflare/resources/zero_trust/gateway/configurations/configurations.py">edit</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/configuration_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/configuration_edit_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/gateway/configuration">client.zero_trust.gateway.configurations.<a href="./src/cloudflare/resources/zero_trust/gateway/configurations/configurations.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/configuration_get_response.py">Optional</a></code>

#### CustomCertificate

Methods:

- <code title="get /accounts/{account_id}/gateway/configuration/custom_certificate">client.zero_trust.gateway.configurations.custom_certificate.<a href="./src/cloudflare/resources/zero_trust/gateway/configurations/custom_certificate.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/custom_certificate_settings.py">CustomCertificateSettings</a></code>

### Lists

Types:

```python
from cloudflare.types.zero_trust.gateway import (
    GatewayItem,
    GatewayList,
    ListCreateResponse,
    ListDeleteResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/gateway/lists">client.zero_trust.gateway.lists.<a href="./src/cloudflare/resources/zero_trust/gateway/lists/lists.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/list_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/list_create_response.py">Optional</a></code>
- <code title="put /accounts/{account_id}/gateway/lists/{list_id}">client.zero_trust.gateway.lists.<a href="./src/cloudflare/resources/zero_trust/gateway/lists/lists.py">update</a>(list_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/list_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/gateway_list.py">Optional</a></code>
- <code title="get /accounts/{account_id}/gateway/lists">client.zero_trust.gateway.lists.<a href="./src/cloudflare/resources/zero_trust/gateway/lists/lists.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/list_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/gateway_list.py">SyncSinglePage[GatewayList]</a></code>
- <code title="delete /accounts/{account_id}/gateway/lists/{list_id}">client.zero_trust.gateway.lists.<a href="./src/cloudflare/resources/zero_trust/gateway/lists/lists.py">delete</a>(list_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/list_delete_response.py">object</a></code>
- <code title="patch /accounts/{account_id}/gateway/lists/{list_id}">client.zero_trust.gateway.lists.<a href="./src/cloudflare/resources/zero_trust/gateway/lists/lists.py">edit</a>(list_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/list_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/gateway_list.py">Optional</a></code>
- <code title="get /accounts/{account_id}/gateway/lists/{list_id}">client.zero_trust.gateway.lists.<a href="./src/cloudflare/resources/zero_trust/gateway/lists/lists.py">get</a>(list_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/gateway_list.py">Optional</a></code>

#### Items

Types:

```python
from cloudflare.types.zero_trust.gateway.lists import ItemListResponse
```

Methods:

- <code title="get /accounts/{account_id}/gateway/lists/{list_id}/items">client.zero_trust.gateway.lists.items.<a href="./src/cloudflare/resources/zero_trust/gateway/lists/items.py">list</a>(list_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/lists/item_list_response.py">SyncSinglePage[ItemListResponse]</a></code>

### Locations

Types:

```python
from cloudflare.types.zero_trust.gateway import (
    DOHEndpoint,
    DOTEndpoint,
    Endpoint,
    IPNetwork,
    IPV4Endpoint,
    IPV6Endpoint,
    IPV6Network,
    Location,
    LocationDeleteResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/gateway/locations">client.zero_trust.gateway.locations.<a href="./src/cloudflare/resources/zero_trust/gateway/locations.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/location_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/location.py">Optional</a></code>
- <code title="put /accounts/{account_id}/gateway/locations/{location_id}">client.zero_trust.gateway.locations.<a href="./src/cloudflare/resources/zero_trust/gateway/locations.py">update</a>(location_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/location_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/location.py">Optional</a></code>
- <code title="get /accounts/{account_id}/gateway/locations">client.zero_trust.gateway.locations.<a href="./src/cloudflare/resources/zero_trust/gateway/locations.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/location.py">SyncSinglePage[Location]</a></code>
- <code title="delete /accounts/{account_id}/gateway/locations/{location_id}">client.zero_trust.gateway.locations.<a href="./src/cloudflare/resources/zero_trust/gateway/locations.py">delete</a>(location_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/location_delete_response.py">object</a></code>
- <code title="get /accounts/{account_id}/gateway/locations/{location_id}">client.zero_trust.gateway.locations.<a href="./src/cloudflare/resources/zero_trust/gateway/locations.py">get</a>(location_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/location.py">Optional</a></code>

### Logging

Types:

```python
from cloudflare.types.zero_trust.gateway import LoggingSetting
```

Methods:

- <code title="put /accounts/{account_id}/gateway/logging">client.zero_trust.gateway.logging.<a href="./src/cloudflare/resources/zero_trust/gateway/logging.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/logging_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/logging_setting.py">Optional</a></code>
- <code title="get /accounts/{account_id}/gateway/logging">client.zero_trust.gateway.logging.<a href="./src/cloudflare/resources/zero_trust/gateway/logging.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/logging_setting.py">Optional</a></code>

### ProxyEndpoints

Types:

```python
from cloudflare.types.zero_trust.gateway import (
    GatewayIPs,
    ProxyEndpoint,
    ProxyEndpointDeleteResponse,
    ProxyEndpointGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/gateway/proxy_endpoints">client.zero_trust.gateway.proxy_endpoints.<a href="./src/cloudflare/resources/zero_trust/gateway/proxy_endpoints.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/proxy_endpoint_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/proxy_endpoint.py">Optional</a></code>
- <code title="get /accounts/{account_id}/gateway/proxy_endpoints">client.zero_trust.gateway.proxy_endpoints.<a href="./src/cloudflare/resources/zero_trust/gateway/proxy_endpoints.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/proxy_endpoint.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/gateway/proxy_endpoints/{proxy_endpoint_id}">client.zero_trust.gateway.proxy_endpoints.<a href="./src/cloudflare/resources/zero_trust/gateway/proxy_endpoints.py">delete</a>(proxy_endpoint_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/proxy_endpoint_delete_response.py">object</a></code>
- <code title="patch /accounts/{account_id}/gateway/proxy_endpoints/{proxy_endpoint_id}">client.zero_trust.gateway.proxy_endpoints.<a href="./src/cloudflare/resources/zero_trust/gateway/proxy_endpoints.py">edit</a>(proxy_endpoint_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/proxy_endpoint_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/proxy_endpoint.py">Optional</a></code>
- <code title="get /accounts/{account_id}/gateway/proxy_endpoints/{proxy_endpoint_id}">client.zero_trust.gateway.proxy_endpoints.<a href="./src/cloudflare/resources/zero_trust/gateway/proxy_endpoints.py">get</a>(proxy_endpoint_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/proxy_endpoint_get_response.py">Optional</a></code>

### Rules

Types:

```python
from cloudflare.types.zero_trust.gateway import (
    DNSResolverSettingsV4,
    DNSResolverSettingsV6,
    GatewayFilter,
    GatewayRule,
    RuleSetting,
    Schedule,
    RuleDeleteResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/gateway/rules">client.zero_trust.gateway.rules.<a href="./src/cloudflare/resources/zero_trust/gateway/rules.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/rule_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/gateway_rule.py">Optional</a></code>
- <code title="put /accounts/{account_id}/gateway/rules/{rule_id}">client.zero_trust.gateway.rules.<a href="./src/cloudflare/resources/zero_trust/gateway/rules.py">update</a>(rule_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/rule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/gateway_rule.py">Optional</a></code>
- <code title="get /accounts/{account_id}/gateway/rules">client.zero_trust.gateway.rules.<a href="./src/cloudflare/resources/zero_trust/gateway/rules.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/gateway_rule.py">SyncSinglePage[GatewayRule]</a></code>
- <code title="delete /accounts/{account_id}/gateway/rules/{rule_id}">client.zero_trust.gateway.rules.<a href="./src/cloudflare/resources/zero_trust/gateway/rules.py">delete</a>(rule_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/rule_delete_response.py">object</a></code>
- <code title="get /accounts/{account_id}/gateway/rules/{rule_id}">client.zero_trust.gateway.rules.<a href="./src/cloudflare/resources/zero_trust/gateway/rules.py">get</a>(rule_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/gateway_rule.py">Optional</a></code>

### Certificates

Types:

```python
from cloudflare.types.zero_trust.gateway import (
    CertificateCreateResponse,
    CertificateListResponse,
    CertificateDeleteResponse,
    CertificateActivateResponse,
    CertificateDeactivateResponse,
    CertificateGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/gateway/certificates">client.zero_trust.gateway.certificates.<a href="./src/cloudflare/resources/zero_trust/gateway/certificates.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/certificate_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/certificate_create_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/gateway/certificates">client.zero_trust.gateway.certificates.<a href="./src/cloudflare/resources/zero_trust/gateway/certificates.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/certificate_list_response.py">SyncSinglePage[CertificateListResponse]</a></code>
- <code title="delete /accounts/{account_id}/gateway/certificates/{certificate_id}">client.zero_trust.gateway.certificates.<a href="./src/cloudflare/resources/zero_trust/gateway/certificates.py">delete</a>(certificate_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/certificate_delete_response.py">Optional</a></code>
- <code title="post /accounts/{account_id}/gateway/certificates/{certificate_id}/activate">client.zero_trust.gateway.certificates.<a href="./src/cloudflare/resources/zero_trust/gateway/certificates.py">activate</a>(certificate_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/certificate_activate_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/certificate_activate_response.py">Optional</a></code>
- <code title="post /accounts/{account_id}/gateway/certificates/{certificate_id}/deactivate">client.zero_trust.gateway.certificates.<a href="./src/cloudflare/resources/zero_trust/gateway/certificates.py">deactivate</a>(certificate_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/certificate_deactivate_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/certificate_deactivate_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/gateway/certificates/{certificate_id}">client.zero_trust.gateway.certificates.<a href="./src/cloudflare/resources/zero_trust/gateway/certificates.py">get</a>(certificate_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/certificate_get_response.py">Optional</a></code>

## Networks

### Routes

Types:

```python
from cloudflare.types.zero_trust.networks import NetworkRoute, Route, Teamnet
```

Methods:

- <code title="post /accounts/{account_id}/teamnet/routes">client.zero_trust.networks.routes.<a href="./src/cloudflare/resources/zero_trust/networks/routes/routes.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/networks/route_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/networks/route.py">Route</a></code>
- <code title="get /accounts/{account_id}/teamnet/routes">client.zero_trust.networks.routes.<a href="./src/cloudflare/resources/zero_trust/networks/routes/routes.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/networks/route_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/networks/teamnet.py">SyncV4PagePaginationArray[Teamnet]</a></code>
- <code title="delete /accounts/{account_id}/teamnet/routes/{route_id}">client.zero_trust.networks.routes.<a href="./src/cloudflare/resources/zero_trust/networks/routes/routes.py">delete</a>(route_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/networks/route.py">Route</a></code>
- <code title="patch /accounts/{account_id}/teamnet/routes/{route_id}">client.zero_trust.networks.routes.<a href="./src/cloudflare/resources/zero_trust/networks/routes/routes.py">edit</a>(route_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/networks/route_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/networks/route.py">Route</a></code>
- <code title="get /accounts/{account_id}/teamnet/routes/{route_id}">client.zero_trust.networks.routes.<a href="./src/cloudflare/resources/zero_trust/networks/routes/routes.py">get</a>(route_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/networks/route.py">Route</a></code>

#### IPs

Methods:

- <code title="get /accounts/{account_id}/teamnet/routes/ip/{ip}">client.zero_trust.networks.routes.ips.<a href="./src/cloudflare/resources/zero_trust/networks/routes/ips.py">get</a>(ip, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/networks/routes/ip_get_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/networks/teamnet.py">Teamnet</a></code>

#### Networks

Methods:

- <code title="post /accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}">client.zero_trust.networks.routes.networks.<a href="./src/cloudflare/resources/zero_trust/networks/routes/networks.py">create</a>(ip_network_encoded, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/networks/routes/network_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/networks/route.py">Route</a></code>
- <code title="delete /accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}">client.zero_trust.networks.routes.networks.<a href="./src/cloudflare/resources/zero_trust/networks/routes/networks.py">delete</a>(ip_network_encoded, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/networks/routes/network_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/networks/route.py">Route</a></code>
- <code title="patch /accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}">client.zero_trust.networks.routes.networks.<a href="./src/cloudflare/resources/zero_trust/networks/routes/networks.py">edit</a>(ip_network_encoded, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/networks/route.py">Route</a></code>

### VirtualNetworks

Types:

```python
from cloudflare.types.zero_trust.networks import VirtualNetwork
```

Methods:

- <code title="post /accounts/{account_id}/teamnet/virtual_networks">client.zero_trust.networks.virtual_networks.<a href="./src/cloudflare/resources/zero_trust/networks/virtual_networks.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/networks/virtual_network_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/networks/virtual_network.py">VirtualNetwork</a></code>
- <code title="get /accounts/{account_id}/teamnet/virtual_networks">client.zero_trust.networks.virtual_networks.<a href="./src/cloudflare/resources/zero_trust/networks/virtual_networks.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/networks/virtual_network_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/networks/virtual_network.py">SyncSinglePage[VirtualNetwork]</a></code>
- <code title="delete /accounts/{account_id}/teamnet/virtual_networks/{virtual_network_id}">client.zero_trust.networks.virtual_networks.<a href="./src/cloudflare/resources/zero_trust/networks/virtual_networks.py">delete</a>(virtual_network_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/networks/virtual_network.py">VirtualNetwork</a></code>
- <code title="patch /accounts/{account_id}/teamnet/virtual_networks/{virtual_network_id}">client.zero_trust.networks.virtual_networks.<a href="./src/cloudflare/resources/zero_trust/networks/virtual_networks.py">edit</a>(virtual_network_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/networks/virtual_network_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/networks/virtual_network.py">VirtualNetwork</a></code>
- <code title="get /accounts/{account_id}/teamnet/virtual_networks/{virtual_network_id}">client.zero_trust.networks.virtual_networks.<a href="./src/cloudflare/resources/zero_trust/networks/virtual_networks.py">get</a>(virtual_network_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/networks/virtual_network.py">VirtualNetwork</a></code>

## RiskScoring

Types:

```python
from cloudflare.types.zero_trust import RiskScoringGetResponse, RiskScoringResetResponse
```

Methods:

- <code title="get /accounts/{account_id}/zt_risk_scoring/{user_id}">client.zero_trust.risk_scoring.<a href="./src/cloudflare/resources/zero_trust/risk_scoring/risk_scoring.py">get</a>(user_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/risk_scoring_get_response.py">Optional</a></code>
- <code title="post /accounts/{account_id}/zt_risk_scoring/{user_id}/reset">client.zero_trust.risk_scoring.<a href="./src/cloudflare/resources/zero_trust/risk_scoring/risk_scoring.py">reset</a>(user_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/risk_scoring_reset_response.py">object</a></code>

### Behaviours

Types:

```python
from cloudflare.types.zero_trust.risk_scoring import BehaviourUpdateResponse, BehaviourGetResponse
```

Methods:

- <code title="put /accounts/{account_id}/zt_risk_scoring/behaviors">client.zero_trust.risk_scoring.behaviours.<a href="./src/cloudflare/resources/zero_trust/risk_scoring/behaviours.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/risk_scoring/behaviour_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/risk_scoring/behaviour_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/zt_risk_scoring/behaviors">client.zero_trust.risk_scoring.behaviours.<a href="./src/cloudflare/resources/zero_trust/risk_scoring/behaviours.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/risk_scoring/behaviour_get_response.py">Optional</a></code>

### Summary

Types:

```python
from cloudflare.types.zero_trust.risk_scoring import SummaryGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/zt_risk_scoring/summary">client.zero_trust.risk_scoring.summary.<a href="./src/cloudflare/resources/zero_trust/risk_scoring/summary.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/risk_scoring/summary_get_response.py">Optional</a></code>

### Integrations

Types:

```python
from cloudflare.types.zero_trust.risk_scoring import (
    IntegrationCreateResponse,
    IntegrationUpdateResponse,
    IntegrationListResponse,
    IntegrationDeleteResponse,
    IntegrationGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/zt_risk_scoring/integrations">client.zero_trust.risk_scoring.integrations.<a href="./src/cloudflare/resources/zero_trust/risk_scoring/integrations/integrations.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/risk_scoring/integration_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/risk_scoring/integration_create_response.py">Optional</a></code>
- <code title="put /accounts/{account_id}/zt_risk_scoring/integrations/{integration_id}">client.zero_trust.risk_scoring.integrations.<a href="./src/cloudflare/resources/zero_trust/risk_scoring/integrations/integrations.py">update</a>(integration_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/risk_scoring/integration_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/risk_scoring/integration_update_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/zt_risk_scoring/integrations">client.zero_trust.risk_scoring.integrations.<a href="./src/cloudflare/resources/zero_trust/risk_scoring/integrations/integrations.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/risk_scoring/integration_list_response.py">SyncSinglePage[IntegrationListResponse]</a></code>
- <code title="delete /accounts/{account_id}/zt_risk_scoring/integrations/{integration_id}">client.zero_trust.risk_scoring.integrations.<a href="./src/cloudflare/resources/zero_trust/risk_scoring/integrations/integrations.py">delete</a>(integration_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/risk_scoring/integration_delete_response.py">object</a></code>
- <code title="get /accounts/{account_id}/zt_risk_scoring/integrations/{integration_id}">client.zero_trust.risk_scoring.integrations.<a href="./src/cloudflare/resources/zero_trust/risk_scoring/integrations/integrations.py">get</a>(integration_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/risk_scoring/integration_get_response.py">Optional</a></code>

#### References

Types:

```python
from cloudflare.types.zero_trust.risk_scoring.integrations import ReferenceGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/zt_risk_scoring/integrations/reference_id/{reference_id}">client.zero_trust.risk_scoring.integrations.references.<a href="./src/cloudflare/resources/zero_trust/risk_scoring/integrations/references.py">get</a>(reference_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/risk_scoring/integrations/reference_get_response.py">Optional</a></code>

# Challenges

## Widgets

Types:

```python
from cloudflare.types.challenges import Widget, WidgetDomain, WidgetListResponse
```

Methods:

- <code title="post /accounts/{account_id}/challenges/widgets">client.challenges.widgets.<a href="./src/cloudflare/resources/challenges/widgets.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/challenges/widget_create_params.py">params</a>) -> <a href="./src/cloudflare/types/challenges/widget.py">Optional</a></code>
- <code title="put /accounts/{account_id}/challenges/widgets/{sitekey}">client.challenges.widgets.<a href="./src/cloudflare/resources/challenges/widgets.py">update</a>(sitekey, \*, account_id, \*\*<a href="src/cloudflare/types/challenges/widget_update_params.py">params</a>) -> <a href="./src/cloudflare/types/challenges/widget.py">Optional</a></code>
- <code title="get /accounts/{account_id}/challenges/widgets">client.challenges.widgets.<a href="./src/cloudflare/resources/challenges/widgets.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/challenges/widget_list_params.py">params</a>) -> <a href="./src/cloudflare/types/challenges/widget_list_response.py">SyncV4PagePaginationArray[WidgetListResponse]</a></code>
- <code title="delete /accounts/{account_id}/challenges/widgets/{sitekey}">client.challenges.widgets.<a href="./src/cloudflare/resources/challenges/widgets.py">delete</a>(sitekey, \*, account_id) -> <a href="./src/cloudflare/types/challenges/widget.py">Optional</a></code>
- <code title="get /accounts/{account_id}/challenges/widgets/{sitekey}">client.challenges.widgets.<a href="./src/cloudflare/resources/challenges/widgets.py">get</a>(sitekey, \*, account_id) -> <a href="./src/cloudflare/types/challenges/widget.py">Optional</a></code>
- <code title="post /accounts/{account_id}/challenges/widgets/{sitekey}/rotate_secret">client.challenges.widgets.<a href="./src/cloudflare/resources/challenges/widgets.py">rotate_secret</a>(sitekey, \*, account_id, \*\*<a href="src/cloudflare/types/challenges/widget_rotate_secret_params.py">params</a>) -> <a href="./src/cloudflare/types/challenges/widget.py">Optional</a></code>

# Hyperdrive

Types:

```python
from cloudflare.types.hyperdrive import Configuration, Hyperdrive
```

## Configs

Types:

```python
from cloudflare.types.hyperdrive import ConfigDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/hyperdrive/configs">client.hyperdrive.configs.<a href="./src/cloudflare/resources/hyperdrive/configs.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/hyperdrive/config_create_params.py">params</a>) -> <a href="./src/cloudflare/types/hyperdrive/hyperdrive.py">Optional</a></code>
- <code title="put /accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}">client.hyperdrive.configs.<a href="./src/cloudflare/resources/hyperdrive/configs.py">update</a>(hyperdrive_id, \*, account_id, \*\*<a href="src/cloudflare/types/hyperdrive/config_update_params.py">params</a>) -> <a href="./src/cloudflare/types/hyperdrive/hyperdrive.py">Optional</a></code>
- <code title="get /accounts/{account_id}/hyperdrive/configs">client.hyperdrive.configs.<a href="./src/cloudflare/resources/hyperdrive/configs.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/hyperdrive/hyperdrive.py">SyncSinglePage[Hyperdrive]</a></code>
- <code title="delete /accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}">client.hyperdrive.configs.<a href="./src/cloudflare/resources/hyperdrive/configs.py">delete</a>(hyperdrive_id, \*, account_id) -> <a href="./src/cloudflare/types/hyperdrive/config_delete_response.py">Optional</a></code>
- <code title="patch /accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}">client.hyperdrive.configs.<a href="./src/cloudflare/resources/hyperdrive/configs.py">edit</a>(hyperdrive_id, \*, account_id, \*\*<a href="src/cloudflare/types/hyperdrive/config_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/hyperdrive/hyperdrive.py">Optional</a></code>
- <code title="get /accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}">client.hyperdrive.configs.<a href="./src/cloudflare/resources/hyperdrive/configs.py">get</a>(hyperdrive_id, \*, account_id) -> <a href="./src/cloudflare/types/hyperdrive/hyperdrive.py">Optional</a></code>

# RUM

## SiteInfo

Types:

```python
from cloudflare.types.rum import Site, SiteInfoDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/rum/site_info">client.rum.site_info.<a href="./src/cloudflare/resources/rum/site_info.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/rum/site_info_create_params.py">params</a>) -> <a href="./src/cloudflare/types/rum/site.py">Optional</a></code>
- <code title="put /accounts/{account_id}/rum/site_info/{site_id}">client.rum.site_info.<a href="./src/cloudflare/resources/rum/site_info.py">update</a>(site_id, \*, account_id, \*\*<a href="src/cloudflare/types/rum/site_info_update_params.py">params</a>) -> <a href="./src/cloudflare/types/rum/site.py">Optional</a></code>
- <code title="get /accounts/{account_id}/rum/site_info/list">client.rum.site_info.<a href="./src/cloudflare/resources/rum/site_info.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/rum/site_info_list_params.py">params</a>) -> <a href="./src/cloudflare/types/rum/site.py">SyncV4PagePaginationArray[Site]</a></code>
- <code title="delete /accounts/{account_id}/rum/site_info/{site_id}">client.rum.site_info.<a href="./src/cloudflare/resources/rum/site_info.py">delete</a>(site_id, \*, account_id) -> <a href="./src/cloudflare/types/rum/site_info_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/rum/site_info/{site_id}">client.rum.site_info.<a href="./src/cloudflare/resources/rum/site_info.py">get</a>(site_id, \*, account_id) -> <a href="./src/cloudflare/types/rum/site.py">Optional</a></code>

## Rules

Types:

```python
from cloudflare.types.rum import RUMRule, RuleListResponse, RuleDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/rum/v2/{ruleset_id}/rule">client.rum.rules.<a href="./src/cloudflare/resources/rum/rules.py">create</a>(ruleset_id, \*, account_id, \*\*<a href="src/cloudflare/types/rum/rule_create_params.py">params</a>) -> <a href="./src/cloudflare/types/rum/rum_rule.py">Optional</a></code>
- <code title="put /accounts/{account_id}/rum/v2/{ruleset_id}/rule/{rule_id}">client.rum.rules.<a href="./src/cloudflare/resources/rum/rules.py">update</a>(rule_id, \*, account_id, ruleset_id, \*\*<a href="src/cloudflare/types/rum/rule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/rum/rum_rule.py">Optional</a></code>
- <code title="get /accounts/{account_id}/rum/v2/{ruleset_id}/rules">client.rum.rules.<a href="./src/cloudflare/resources/rum/rules.py">list</a>(ruleset_id, \*, account_id) -> <a href="./src/cloudflare/types/rum/rule_list_response.py">Optional</a></code>
- <code title="delete /accounts/{account_id}/rum/v2/{ruleset_id}/rule/{rule_id}">client.rum.rules.<a href="./src/cloudflare/resources/rum/rules.py">delete</a>(rule_id, \*, account_id, ruleset_id) -> <a href="./src/cloudflare/types/rum/rule_delete_response.py">Optional</a></code>

# Vectorize

## Indexes

Types:

```python
from cloudflare.types.vectorize import (
    CreateIndex,
    IndexDeleteVectorsByID,
    IndexDimensionConfiguration,
    IndexInsert,
    IndexQuery,
    IndexUpsert,
    IndexDeleteResponse,
    IndexDeleteByIDsResponse,
    IndexGetByIDsResponse,
    IndexInfoResponse,
    IndexInsertResponse,
    IndexQueryResponse,
    IndexUpsertResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/vectorize/v2/indexes">client.vectorize.indexes.<a href="./src/cloudflare/resources/vectorize/indexes/indexes.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/vectorize/index_create_params.py">params</a>) -> <a href="./src/cloudflare/types/vectorize/create_index.py">Optional</a></code>
- <code title="get /accounts/{account_id}/vectorize/v2/indexes">client.vectorize.indexes.<a href="./src/cloudflare/resources/vectorize/indexes/indexes.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/vectorize/create_index.py">SyncSinglePage[CreateIndex]</a></code>
- <code title="delete /accounts/{account_id}/vectorize/v2/indexes/{index_name}">client.vectorize.indexes.<a href="./src/cloudflare/resources/vectorize/indexes/indexes.py">delete</a>(index_name, \*, account_id) -> <a href="./src/cloudflare/types/vectorize/index_delete_response.py">Optional</a></code>
- <code title="post /accounts/{account_id}/vectorize/v2/indexes/{index_name}/delete_by_ids">client.vectorize.indexes.<a href="./src/cloudflare/resources/vectorize/indexes/indexes.py">delete_by_ids</a>(index_name, \*, account_id, \*\*<a href="src/cloudflare/types/vectorize/index_delete_by_ids_params.py">params</a>) -> <a href="./src/cloudflare/types/vectorize/index_delete_by_ids_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/vectorize/v2/indexes/{index_name}">client.vectorize.indexes.<a href="./src/cloudflare/resources/vectorize/indexes/indexes.py">get</a>(index_name, \*, account_id) -> <a href="./src/cloudflare/types/vectorize/create_index.py">Optional</a></code>
- <code title="post /accounts/{account_id}/vectorize/v2/indexes/{index_name}/get_by_ids">client.vectorize.indexes.<a href="./src/cloudflare/resources/vectorize/indexes/indexes.py">get_by_ids</a>(index_name, \*, account_id, \*\*<a href="src/cloudflare/types/vectorize/index_get_by_ids_params.py">params</a>) -> <a href="./src/cloudflare/types/vectorize/index_get_by_ids_response.py">object</a></code>
- <code title="get /accounts/{account_id}/vectorize/v2/indexes/{index_name}/info">client.vectorize.indexes.<a href="./src/cloudflare/resources/vectorize/indexes/indexes.py">info</a>(index_name, \*, account_id) -> <a href="./src/cloudflare/types/vectorize/index_info_response.py">Optional</a></code>
- <code title="post /accounts/{account_id}/vectorize/v2/indexes/{index_name}/insert">client.vectorize.indexes.<a href="./src/cloudflare/resources/vectorize/indexes/indexes.py">insert</a>(index_name, \*, account_id, \*\*<a href="src/cloudflare/types/vectorize/index_insert_params.py">params</a>) -> <a href="./src/cloudflare/types/vectorize/index_insert_response.py">Optional</a></code>
- <code title="post /accounts/{account_id}/vectorize/v2/indexes/{index_name}/query">client.vectorize.indexes.<a href="./src/cloudflare/resources/vectorize/indexes/indexes.py">query</a>(index_name, \*, account_id, \*\*<a href="src/cloudflare/types/vectorize/index_query_params.py">params</a>) -> <a href="./src/cloudflare/types/vectorize/index_query_response.py">Optional</a></code>
- <code title="post /accounts/{account_id}/vectorize/v2/indexes/{index_name}/upsert">client.vectorize.indexes.<a href="./src/cloudflare/resources/vectorize/indexes/indexes.py">upsert</a>(index_name, \*, account_id, \*\*<a href="src/cloudflare/types/vectorize/index_upsert_params.py">params</a>) -> <a href="./src/cloudflare/types/vectorize/index_upsert_response.py">Optional</a></code>

### MetadataIndex

Types:

```python
from cloudflare.types.vectorize.indexes import (
    MetadataIndexCreateResponse,
    MetadataIndexListResponse,
    MetadataIndexDeleteResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/vectorize/v2/indexes/{index_name}/metadata_index/create">client.vectorize.indexes.metadata_index.<a href="./src/cloudflare/resources/vectorize/indexes/metadata_index.py">create</a>(index_name, \*, account_id, \*\*<a href="src/cloudflare/types/vectorize/indexes/metadata_index_create_params.py">params</a>) -> <a href="./src/cloudflare/types/vectorize/indexes/metadata_index_create_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/vectorize/v2/indexes/{index_name}/metadata_index/list">client.vectorize.indexes.metadata_index.<a href="./src/cloudflare/resources/vectorize/indexes/metadata_index.py">list</a>(index_name, \*, account_id) -> <a href="./src/cloudflare/types/vectorize/indexes/metadata_index_list_response.py">Optional</a></code>
- <code title="post /accounts/{account_id}/vectorize/v2/indexes/{index_name}/metadata_index/delete">client.vectorize.indexes.metadata_index.<a href="./src/cloudflare/resources/vectorize/indexes/metadata_index.py">delete</a>(index_name, \*, account_id, \*\*<a href="src/cloudflare/types/vectorize/indexes/metadata_index_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/vectorize/indexes/metadata_index_delete_response.py">Optional</a></code>

# URLScanner

Types:

```python
from cloudflare.types.url_scanner import URLScannerScanResponse
```

Methods:

- <code title="get /accounts/{accountId}/urlscanner/scan">client.url_scanner.<a href="./src/cloudflare/resources/url_scanner/url_scanner.py">scan</a>(account_id, \*\*<a href="src/cloudflare/types/url_scanner/url_scanner_scan_params.py">params</a>) -> <a href="./src/cloudflare/types/url_scanner/url_scanner_scan_response.py">URLScannerScanResponse</a></code>

## Scans

Types:

```python
from cloudflare.types.url_scanner import (
    URLScannerDomain,
    URLScannerTask,
    ScanCreateResponse,
    ScanGetResponse,
    ScanHarResponse,
)
```

Methods:

- <code title="post /accounts/{accountId}/urlscanner/scan">client.url_scanner.scans.<a href="./src/cloudflare/resources/url_scanner/scans.py">create</a>(account_id, \*\*<a href="src/cloudflare/types/url_scanner/scan_create_params.py">params</a>) -> <a href="./src/cloudflare/types/url_scanner/scan_create_response.py">ScanCreateResponse</a></code>
- <code title="get /accounts/{accountId}/urlscanner/scan/{scanId}">client.url_scanner.scans.<a href="./src/cloudflare/resources/url_scanner/scans.py">get</a>(scan_id, \*, account_id, \*\*<a href="src/cloudflare/types/url_scanner/scan_get_params.py">params</a>) -> <a href="./src/cloudflare/types/url_scanner/scan_get_response.py">ScanGetResponse</a></code>
- <code title="get /accounts/{accountId}/urlscanner/scan/{scanId}/har">client.url_scanner.scans.<a href="./src/cloudflare/resources/url_scanner/scans.py">har</a>(scan_id, \*, account_id) -> <a href="./src/cloudflare/types/url_scanner/scan_har_response.py">ScanHarResponse</a></code>
- <code title="get /accounts/{accountId}/urlscanner/scan/{scanId}/screenshot">client.url_scanner.scans.<a href="./src/cloudflare/resources/url_scanner/scans.py">screenshot</a>(scan_id, \*, account_id, \*\*<a href="src/cloudflare/types/url_scanner/scan_screenshot_params.py">params</a>) -> BinaryAPIResponse</code>

# Radar

## AI

### Gateway

#### Summary

Types:

```python
from cloudflare.types.radar.ai.gateway import (
    SummaryModelResponse,
    SummaryProviderResponse,
    SummaryTaskResponse,
)
```

Methods:

- <code title="get /radar/ai/inference/summary/model">client.radar.ai.gateway.summary.<a href="./src/cloudflare/resources/radar/ai/gateway/summary.py">model</a>(\*\*<a href="src/cloudflare/types/radar/ai/gateway/summary_model_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/ai/gateway/summary_model_response.py">SummaryModelResponse</a></code>
- <code title="get /radar/ai/gateway/summary/provider">client.radar.ai.gateway.summary.<a href="./src/cloudflare/resources/radar/ai/gateway/summary.py">provider</a>(\*\*<a href="src/cloudflare/types/radar/ai/gateway/summary_provider_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/ai/gateway/summary_provider_response.py">SummaryProviderResponse</a></code>
- <code title="get /radar/ai/inference/summary/task">client.radar.ai.gateway.summary.<a href="./src/cloudflare/resources/radar/ai/gateway/summary.py">task</a>(\*\*<a href="src/cloudflare/types/radar/ai/gateway/summary_task_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/ai/gateway/summary_task_response.py">SummaryTaskResponse</a></code>

#### TimeseriesGroups

Types:

```python
from cloudflare.types.radar.ai.gateway import (
    TimeseriesGroupModelResponse,
    TimeseriesGroupProviderResponse,
    TimeseriesGroupTaskResponse,
)
```

Methods:

- <code title="get /radar/ai/inference/timeseries_groups/model">client.radar.ai.gateway.timeseries_groups.<a href="./src/cloudflare/resources/radar/ai/gateway/timeseries_groups.py">model</a>(\*\*<a href="src/cloudflare/types/radar/ai/gateway/timeseries_group_model_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/ai/gateway/timeseries_group_model_response.py">TimeseriesGroupModelResponse</a></code>
- <code title="get /radar/ai/gateway/timeseries_groups/provider">client.radar.ai.gateway.timeseries_groups.<a href="./src/cloudflare/resources/radar/ai/gateway/timeseries_groups.py">provider</a>(\*\*<a href="src/cloudflare/types/radar/ai/gateway/timeseries_group_provider_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/ai/gateway/timeseries_group_provider_response.py">TimeseriesGroupProviderResponse</a></code>
- <code title="get /radar/ai/inference/timeseries_groups/task">client.radar.ai.gateway.timeseries_groups.<a href="./src/cloudflare/resources/radar/ai/gateway/timeseries_groups.py">task</a>(\*\*<a href="src/cloudflare/types/radar/ai/gateway/timeseries_group_task_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/ai/gateway/timeseries_group_task_response.py">TimeseriesGroupTaskResponse</a></code>

## Annotations

Types:

```python
from cloudflare.types.radar import AnnotationListResponse
```

Methods:

- <code title="get /radar/annotations">client.radar.annotations.<a href="./src/cloudflare/resources/radar/annotations/annotations.py">list</a>(\*\*<a href="src/cloudflare/types/radar/annotation_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/annotation_list_response.py">AnnotationListResponse</a></code>

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

#### Events

Types:

```python
from cloudflare.types.radar.bgp.leaks import EventListResponse
```

Methods:

- <code title="get /radar/bgp/leaks/events">client.radar.bgp.leaks.events.<a href="./src/cloudflare/resources/radar/bgp/leaks/events.py">list</a>(\*\*<a href="src/cloudflare/types/radar/bgp/leaks/event_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bgp/leaks/event_list_response.py">SyncV4PagePagination[EventListResponse]</a></code>

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

#### Events

Types:

```python
from cloudflare.types.radar.bgp.hijacks import EventListResponse
```

Methods:

- <code title="get /radar/bgp/hijacks/events">client.radar.bgp.hijacks.events.<a href="./src/cloudflare/resources/radar/bgp/hijacks/events.py">list</a>(\*\*<a href="src/cloudflare/types/radar/bgp/hijacks/event_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bgp/hijacks/event_list_response.py">SyncV4PagePagination[EventListResponse]</a></code>

### Routes

Types:

```python
from cloudflare.types.radar.bgp import (
    RouteAsesResponse,
    RouteMoasResponse,
    RoutePfx2asResponse,
    RouteStatsResponse,
)
```

Methods:

- <code title="get /radar/bgp/routes/ases">client.radar.bgp.routes.<a href="./src/cloudflare/resources/radar/bgp/routes.py">ases</a>(\*\*<a href="src/cloudflare/types/radar/bgp/route_ases_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bgp/route_ases_response.py">RouteAsesResponse</a></code>
- <code title="get /radar/bgp/routes/moas">client.radar.bgp.routes.<a href="./src/cloudflare/resources/radar/bgp/routes.py">moas</a>(\*\*<a href="src/cloudflare/types/radar/bgp/route_moas_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bgp/route_moas_response.py">RouteMoasResponse</a></code>
- <code title="get /radar/bgp/routes/pfx2as">client.radar.bgp.routes.<a href="./src/cloudflare/resources/radar/bgp/routes.py">pfx2as</a>(\*\*<a href="src/cloudflare/types/radar/bgp/route_pfx2as_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bgp/route_pfx2as_response.py">RoutePfx2asResponse</a></code>
- <code title="get /radar/bgp/routes/stats">client.radar.bgp.routes.<a href="./src/cloudflare/resources/radar/bgp/routes.py">stats</a>(\*\*<a href="src/cloudflare/types/radar/bgp/route_stats_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bgp/route_stats_response.py">RouteStatsResponse</a></code>

### IPs

Types:

```python
from cloudflare.types.radar.bgp import IPTimeseriesResponse
```

Methods:

- <code title="get /radar/bgp/ips/timeseries">client.radar.bgp.ips.<a href="./src/cloudflare/resources/radar/bgp/ips.py">timeseries</a>(\*\*<a href="src/cloudflare/types/radar/bgp/ip_timeseries_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bgp/ip_timeseries_response.py">IPTimeseriesResponse</a></code>

## Datasets

Types:

```python
from cloudflare.types.radar import DatasetListResponse, DatasetDownloadResponse, DatasetGetResponse
```

Methods:

- <code title="get /radar/datasets">client.radar.datasets.<a href="./src/cloudflare/resources/radar/datasets.py">list</a>(\*\*<a href="src/cloudflare/types/radar/dataset_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/dataset_list_response.py">DatasetListResponse</a></code>
- <code title="post /radar/datasets/download">client.radar.datasets.<a href="./src/cloudflare/resources/radar/datasets.py">download</a>(\*\*<a href="src/cloudflare/types/radar/dataset_download_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/dataset_download_response.py">DatasetDownloadResponse</a></code>
- <code title="get /radar/datasets/{alias}">client.radar.datasets.<a href="./src/cloudflare/resources/radar/datasets.py">get</a>(alias) -> str</code>

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
from cloudflare.types.radar import NetflowSummaryResponse, NetflowTimeseriesResponse
```

Methods:

- <code title="get /radar/netflows/summary">client.radar.netflows.<a href="./src/cloudflare/resources/radar/netflows/netflows.py">summary</a>(\*\*<a href="src/cloudflare/types/radar/netflow_summary_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/netflow_summary_response.py">NetflowSummaryResponse</a></code>
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

## Email

Types:

```python
from cloudflare.types.radar import RadarEmailSeries, RadarEmailSummary
```

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

Types:

```python
from cloudflare.types.radar import HTTPTimeseriesResponse
```

Methods:

- <code title="get /radar/http/timeseries">client.radar.http.<a href="./src/cloudflare/resources/radar/http/http.py">timeseries</a>(\*\*<a href="src/cloudflare/types/radar/http_timeseries_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http_timeseries_response.py">HTTPTimeseriesResponse</a></code>

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

#### BrowserFamily

Types:

```python
from cloudflare.types.radar.http.locations import BrowserFamilyGetResponse
```

Methods:

- <code title="get /radar/http/top/locations/browser_family/{browser_family}">client.radar.http.locations.browser_family.<a href="./src/cloudflare/resources/radar/http/locations/browser_family.py">get</a>(browser_family, \*\*<a href="src/cloudflare/types/radar/http/locations/browser_family_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/locations/browser_family_get_response.py">BrowserFamilyGetResponse</a></code>

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

#### BrowserFamily

Types:

```python
from cloudflare.types.radar.http.ases import BrowserFamilyGetResponse
```

Methods:

- <code title="get /radar/http/top/ases/browser_family/{browser_family}">client.radar.http.ases.browser_family.<a href="./src/cloudflare/resources/radar/http/ases/browser_family.py">get</a>(browser_family, \*\*<a href="src/cloudflare/types/radar/http/ases/browser_family_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/ases/browser_family_get_response.py">BrowserFamilyGetResponse</a></code>

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
    SummaryPostQuantumResponse,
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
- <code title="get /radar/http/summary/post_quantum">client.radar.http.summary.<a href="./src/cloudflare/resources/radar/http/summary.py">post_quantum</a>(\*\*<a href="src/cloudflare/types/radar/http/summary_post_quantum_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/summary_post_quantum_response.py">SummaryPostQuantumResponse</a></code>
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
    TimeseriesGroupPostQuantumResponse,
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
- <code title="get /radar/http/timeseries_groups/post_quantum">client.radar.http.timeseries_groups.<a href="./src/cloudflare/resources/radar/http/timeseries_groups.py">post_quantum</a>(\*\*<a href="src/cloudflare/types/radar/http/timeseries_group_post_quantum_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/timeseries_group_post_quantum_response.py">TimeseriesGroupPostQuantumResponse</a></code>
- <code title="get /radar/http/timeseries_groups/tls_version">client.radar.http.timeseries_groups.<a href="./src/cloudflare/resources/radar/http/timeseries_groups.py">tls_version</a>(\*\*<a href="src/cloudflare/types/radar/http/timeseries_group_tls_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/timeseries_group_tls_version_response.py">TimeseriesGroupTLSVersionResponse</a></code>

### Top

Types:

```python
from cloudflare.types.radar.http import TopBrowserResponse, TopBrowserFamilyResponse
```

Methods:

- <code title="get /radar/http/top/browser">client.radar.http.top.<a href="./src/cloudflare/resources/radar/http/top.py">browser</a>(\*\*<a href="src/cloudflare/types/radar/http/top_browser_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/top_browser_response.py">TopBrowserResponse</a></code>
- <code title="get /radar/http/top/browser_family">client.radar.http.top.<a href="./src/cloudflare/resources/radar/http/top.py">browser_family</a>(\*\*<a href="src/cloudflare/types/radar/http/top_browser_family_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/top_browser_family_response.py">TopBrowserFamilyResponse</a></code>

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

## TCPResetsTimeouts

Types:

```python
from cloudflare.types.radar import (
    TCPResetsTimeoutSummaryResponse,
    TCPResetsTimeoutTimeseriesGroupsResponse,
)
```

Methods:

- <code title="get /radar/tcp_resets_timeouts/summary">client.radar.tcp_resets_timeouts.<a href="./src/cloudflare/resources/radar/tcp_resets_timeouts.py">summary</a>(\*\*<a href="src/cloudflare/types/radar/tcp_resets_timeout_summary_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/tcp_resets_timeout_summary_response.py">TCPResetsTimeoutSummaryResponse</a></code>
- <code title="get /radar/tcp_resets_timeouts/timeseries_groups">client.radar.tcp_resets_timeouts.<a href="./src/cloudflare/resources/radar/tcp_resets_timeouts.py">timeseries_groups</a>(\*\*<a href="src/cloudflare/types/radar/tcp_resets_timeout_timeseries_groups_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/tcp_resets_timeout_timeseries_groups_response.py">TCPResetsTimeoutTimeseriesGroupsResponse</a></code>

# BotManagement

Types:

```python
from cloudflare.types.bot_management import (
    BotFightModeConfiguration,
    SubscriptionConfiguration,
    SuperBotFightModeDefinitelyConfiguration,
    SuperBotFightModeLikelyConfiguration,
    BotManagementUpdateResponse,
    BotManagementGetResponse,
)
```

Methods:

- <code title="put /zones/{zone_id}/bot_management">client.bot_management.<a href="./src/cloudflare/resources/bot_management.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/bot_management/bot_management_update_params.py">params</a>) -> <a href="./src/cloudflare/types/bot_management/bot_management_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/bot_management">client.bot_management.<a href="./src/cloudflare/resources/bot_management.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/bot_management/bot_management_get_response.py">Optional</a></code>

# OriginPostQuantumEncryption

Types:

```python
from cloudflare.types.origin_post_quantum_encryption import (
    OriginPostQuantumEncryptionUpdateResponse,
    OriginPostQuantumEncryptionGetResponse,
)
```

Methods:

- <code title="put /zones/{zone_id}/cache/origin_post_quantum_encryption">client.origin_post_quantum_encryption.<a href="./src/cloudflare/resources/origin_post_quantum_encryption.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/origin_post_quantum_encryption/origin_post_quantum_encryption_update_params.py">params</a>) -> <a href="./src/cloudflare/types/origin_post_quantum_encryption/origin_post_quantum_encryption_update_response.py">object</a></code>
- <code title="get /zones/{zone_id}/cache/origin_post_quantum_encryption">client.origin_post_quantum_encryption.<a href="./src/cloudflare/resources/origin_post_quantum_encryption.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/origin_post_quantum_encryption/origin_post_quantum_encryption_get_response.py">object</a></code>

# Speed

Types:

```python
from cloudflare.types.speed import LabeledRegion, LighthouseReport, Trend
```

## Schedule

Types:

```python
from cloudflare.types.speed import Schedule, ScheduleCreateResponse, ScheduleDeleteResponse
```

Methods:

- <code title="post /zones/{zone_id}/speed_api/schedule/{url}">client.speed.schedule.<a href="./src/cloudflare/resources/speed/schedule.py">create</a>(url, \*, zone_id, \*\*<a href="src/cloudflare/types/speed/schedule_create_params.py">params</a>) -> <a href="./src/cloudflare/types/speed/schedule_create_response.py">Optional</a></code>
- <code title="delete /zones/{zone_id}/speed_api/schedule/{url}">client.speed.schedule.<a href="./src/cloudflare/resources/speed/schedule.py">delete</a>(url, \*, zone_id, \*\*<a href="src/cloudflare/types/speed/schedule_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/speed/schedule_delete_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/speed_api/schedule/{url}">client.speed.schedule.<a href="./src/cloudflare/resources/speed/schedule.py">get</a>(url, \*, zone_id, \*\*<a href="src/cloudflare/types/speed/schedule_get_params.py">params</a>) -> <a href="./src/cloudflare/types/speed/schedule.py">Optional</a></code>

## Availabilities

Types:

```python
from cloudflare.types.speed import Availability
```

Methods:

- <code title="get /zones/{zone_id}/speed_api/availabilities">client.speed.availabilities.<a href="./src/cloudflare/resources/speed/availabilities.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/speed/availability.py">Optional</a></code>

## Pages

Types:

```python
from cloudflare.types.speed import PageListResponse
```

Methods:

- <code title="get /zones/{zone_id}/speed_api/pages">client.speed.pages.<a href="./src/cloudflare/resources/speed/pages/pages.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/speed/page_list_response.py">SyncSinglePage[PageListResponse]</a></code>
- <code title="get /zones/{zone_id}/speed_api/pages/{url}/trend">client.speed.pages.<a href="./src/cloudflare/resources/speed/pages/pages.py">trend</a>(url, \*, zone_id, \*\*<a href="src/cloudflare/types/speed/page_trend_params.py">params</a>) -> <a href="./src/cloudflare/types/speed/trend.py">Optional</a></code>

### Tests

Types:

```python
from cloudflare.types.speed.pages import Test, TestDeleteResponse
```

Methods:

- <code title="post /zones/{zone_id}/speed_api/pages/{url}/tests">client.speed.pages.tests.<a href="./src/cloudflare/resources/speed/pages/tests.py">create</a>(url, \*, zone_id, \*\*<a href="src/cloudflare/types/speed/pages/test_create_params.py">params</a>) -> <a href="./src/cloudflare/types/speed/pages/test.py">Optional</a></code>
- <code title="get /zones/{zone_id}/speed_api/pages/{url}/tests">client.speed.pages.tests.<a href="./src/cloudflare/resources/speed/pages/tests.py">list</a>(url, \*, zone_id, \*\*<a href="src/cloudflare/types/speed/pages/test_list_params.py">params</a>) -> <a href="./src/cloudflare/types/speed/pages/test.py">SyncV4PagePaginationArray[Test]</a></code>
- <code title="delete /zones/{zone_id}/speed_api/pages/{url}/tests">client.speed.pages.tests.<a href="./src/cloudflare/resources/speed/pages/tests.py">delete</a>(url, \*, zone_id, \*\*<a href="src/cloudflare/types/speed/pages/test_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/speed/pages/test_delete_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/speed_api/pages/{url}/tests/{test_id}">client.speed.pages.tests.<a href="./src/cloudflare/resources/speed/pages/tests.py">get</a>(test_id, \*, zone_id, url) -> <a href="./src/cloudflare/types/speed/pages/test.py">Optional</a></code>

# DCVDelegation

Types:

```python
from cloudflare.types.dcv_delegation import DCVDelegationUUID
```

Methods:

- <code title="get /zones/{zone_id}/dcv_delegation/uuid">client.dcv_delegation.<a href="./src/cloudflare/resources/dcv_delegation.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/dcv_delegation/dcv_delegation_uuid.py">Optional</a></code>

# Hostnames

## Settings

### TLS

Types:

```python
from cloudflare.types.hostnames.settings import (
    Setting,
    SettingValue,
    TLSDeleteResponse,
    TLSGetResponse,
)
```

Methods:

- <code title="put /zones/{zone_id}/hostnames/settings/{setting_id}/{hostname}">client.hostnames.settings.tls.<a href="./src/cloudflare/resources/hostnames/settings/tls.py">update</a>(hostname, \*, zone_id, setting_id, \*\*<a href="src/cloudflare/types/hostnames/settings/tls_update_params.py">params</a>) -> <a href="./src/cloudflare/types/hostnames/settings/setting.py">Optional</a></code>
- <code title="delete /zones/{zone_id}/hostnames/settings/{setting_id}/{hostname}">client.hostnames.settings.tls.<a href="./src/cloudflare/resources/hostnames/settings/tls.py">delete</a>(hostname, \*, zone_id, setting_id) -> <a href="./src/cloudflare/types/hostnames/settings/tls_delete_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/hostnames/settings/{setting_id}">client.hostnames.settings.tls.<a href="./src/cloudflare/resources/hostnames/settings/tls.py">get</a>(setting_id, \*, zone_id) -> <a href="./src/cloudflare/types/hostnames/settings/tls_get_response.py">Optional</a></code>

# Snippets

Types:

```python
from cloudflare.types.snippets import Snippet, SnippetDeleteResponse
```

Methods:

- <code title="put /zones/{zone_id}/snippets/{snippet_name}">client.snippets.<a href="./src/cloudflare/resources/snippets/snippets.py">update</a>(snippet_name, \*, zone_id, \*\*<a href="src/cloudflare/types/snippets/snippet_update_params.py">params</a>) -> <a href="./src/cloudflare/types/snippets/snippet.py">Optional</a></code>
- <code title="get /zones/{zone_id}/snippets">client.snippets.<a href="./src/cloudflare/resources/snippets/snippets.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/snippets/snippet.py">SyncSinglePage[Snippet]</a></code>
- <code title="delete /zones/{zone_id}/snippets/{snippet_name}">client.snippets.<a href="./src/cloudflare/resources/snippets/snippets.py">delete</a>(snippet_name, \*, zone_id) -> <a href="./src/cloudflare/types/snippets/snippet_delete_response.py">SnippetDeleteResponse</a></code>
- <code title="get /zones/{zone_id}/snippets/{snippet_name}">client.snippets.<a href="./src/cloudflare/resources/snippets/snippets.py">get</a>(snippet_name, \*, zone_id) -> <a href="./src/cloudflare/types/snippets/snippet.py">Optional</a></code>

## Content

Methods:

- <code title="get /zones/{zone_id}/snippets/{snippet_name}/content">client.snippets.content.<a href="./src/cloudflare/resources/snippets/content.py">get</a>(snippet_name, \*, zone_id) -> BinaryAPIResponse</code>

## Rules

Types:

```python
from cloudflare.types.snippets import RuleUpdateResponse, RuleListResponse
```

Methods:

- <code title="put /zones/{zone_id}/snippets/snippet_rules">client.snippets.rules.<a href="./src/cloudflare/resources/snippets/rules.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/snippets/rule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/snippets/rule_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/snippets/snippet_rules">client.snippets.rules.<a href="./src/cloudflare/resources/snippets/rules.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/snippets/rule_list_response.py">SyncSinglePage[RuleListResponse]</a></code>

# Calls

Types:

```python
from cloudflare.types.calls import CallsApp, CallsAppWithSecret, CallListResponse
```

Methods:

- <code title="post /accounts/{account_id}/calls/apps">client.calls.<a href="./src/cloudflare/resources/calls/calls.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/calls/call_create_params.py">params</a>) -> <a href="./src/cloudflare/types/calls/calls_app_with_secret.py">Optional</a></code>
- <code title="put /accounts/{account_id}/calls/apps/{app_id}">client.calls.<a href="./src/cloudflare/resources/calls/calls.py">update</a>(app_id, \*, account_id, \*\*<a href="src/cloudflare/types/calls/call_update_params.py">params</a>) -> <a href="./src/cloudflare/types/calls/calls_app.py">Optional</a></code>
- <code title="get /accounts/{account_id}/calls/apps">client.calls.<a href="./src/cloudflare/resources/calls/calls.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/calls/call_list_response.py">SyncSinglePage[CallListResponse]</a></code>
- <code title="delete /accounts/{account_id}/calls/apps/{app_id}">client.calls.<a href="./src/cloudflare/resources/calls/calls.py">delete</a>(app_id, \*, account_id) -> <a href="./src/cloudflare/types/calls/calls_app.py">Optional</a></code>
- <code title="get /accounts/{account_id}/calls/apps/{app_id}">client.calls.<a href="./src/cloudflare/resources/calls/calls.py">get</a>(app_id, \*, account_id) -> <a href="./src/cloudflare/types/calls/calls_app.py">Optional</a></code>

## TURN

### Keys

Types:

```python
from cloudflare.types.calls.turn import (
    KeyCreateResponse,
    KeyUpdateResponse,
    KeyListResponse,
    KeyDeleteResponse,
    KeyGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/calls/turn_keys">client.calls.turn.keys.<a href="./src/cloudflare/resources/calls/turn/keys.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/calls/turn/key_create_params.py">params</a>) -> <a href="./src/cloudflare/types/calls/turn/key_create_response.py">KeyCreateResponse</a></code>
- <code title="put /accounts/{account_id}/calls/turn_keys/{key_id}">client.calls.turn.keys.<a href="./src/cloudflare/resources/calls/turn/keys.py">update</a>(key_id, \*, account_id, \*\*<a href="src/cloudflare/types/calls/turn/key_update_params.py">params</a>) -> <a href="./src/cloudflare/types/calls/turn/key_update_response.py">str</a></code>
- <code title="get /accounts/{account_id}/calls/turn_keys">client.calls.turn.keys.<a href="./src/cloudflare/resources/calls/turn/keys.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/calls/turn/key_list_response.py">SyncSinglePage[KeyListResponse]</a></code>
- <code title="delete /accounts/{account_id}/calls/turn_keys/{key_id}">client.calls.turn.keys.<a href="./src/cloudflare/resources/calls/turn/keys.py">delete</a>(key_id, \*, account_id) -> <a href="./src/cloudflare/types/calls/turn/key_delete_response.py">str</a></code>
- <code title="get /accounts/{account_id}/calls/turn_keys/{key_id}">client.calls.turn.keys.<a href="./src/cloudflare/resources/calls/turn/keys.py">get</a>(key_id, \*, account_id) -> <a href="./src/cloudflare/types/calls/turn/key_get_response.py">str</a></code>

# CloudforceOne

## Requests

Types:

```python
from cloudflare.types.cloudforce_one import (
    Item,
    ListItem,
    Quota,
    RequestConstants,
    RequestTypes,
    RequestDeleteResponse,
)
```

Methods:

- <code title="post /accounts/{account_identifier}/cloudforce-one/requests/new">client.cloudforce_one.requests.<a href="./src/cloudflare/resources/cloudforce_one/requests/requests.py">create</a>(account_identifier, \*\*<a href="src/cloudflare/types/cloudforce_one/request_create_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/item.py">Optional</a></code>
- <code title="put /accounts/{account_identifier}/cloudforce-one/requests/{request_identifier}">client.cloudforce_one.requests.<a href="./src/cloudflare/resources/cloudforce_one/requests/requests.py">update</a>(request_identifier, \*, account_identifier, \*\*<a href="src/cloudflare/types/cloudforce_one/request_update_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/item.py">Optional</a></code>
- <code title="post /accounts/{account_identifier}/cloudforce-one/requests">client.cloudforce_one.requests.<a href="./src/cloudflare/resources/cloudforce_one/requests/requests.py">list</a>(account_identifier, \*\*<a href="src/cloudflare/types/cloudforce_one/request_list_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/list_item.py">SyncV4PagePaginationArray[ListItem]</a></code>
- <code title="delete /accounts/{account_identifier}/cloudforce-one/requests/{request_identifier}">client.cloudforce_one.requests.<a href="./src/cloudflare/resources/cloudforce_one/requests/requests.py">delete</a>(request_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/cloudforce_one/request_delete_response.py">RequestDeleteResponse</a></code>
- <code title="get /accounts/{account_identifier}/cloudforce-one/requests/constants">client.cloudforce_one.requests.<a href="./src/cloudflare/resources/cloudforce_one/requests/requests.py">constants</a>(account_identifier) -> <a href="./src/cloudflare/types/cloudforce_one/request_constants.py">Optional</a></code>
- <code title="get /accounts/{account_identifier}/cloudforce-one/requests/{request_identifier}">client.cloudforce_one.requests.<a href="./src/cloudflare/resources/cloudforce_one/requests/requests.py">get</a>(request_identifier, \*, account_identifier) -> <a href="./src/cloudflare/types/cloudforce_one/item.py">Optional</a></code>
- <code title="get /accounts/{account_identifier}/cloudforce-one/requests/quota">client.cloudforce_one.requests.<a href="./src/cloudflare/resources/cloudforce_one/requests/requests.py">quota</a>(account_identifier) -> <a href="./src/cloudflare/types/cloudforce_one/quota.py">Optional</a></code>
- <code title="get /accounts/{account_identifier}/cloudforce-one/requests/types">client.cloudforce_one.requests.<a href="./src/cloudflare/resources/cloudforce_one/requests/requests.py">types</a>(account_identifier) -> <a href="./src/cloudflare/types/cloudforce_one/request_types.py">Optional</a></code>

### Message

Types:

```python
from cloudflare.types.cloudforce_one.requests import (
    Message,
    MessageDeleteResponse,
    MessageGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_identifier}/cloudforce-one/requests/{request_identifier}/message/new">client.cloudforce_one.requests.message.<a href="./src/cloudflare/resources/cloudforce_one/requests/message.py">create</a>(request_identifier, \*, account_identifier, \*\*<a href="src/cloudflare/types/cloudforce_one/requests/message_create_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/requests/message.py">Optional</a></code>
- <code title="put /accounts/{account_identifier}/cloudforce-one/requests/{request_identifier}/message/{message_identifer}">client.cloudforce_one.requests.message.<a href="./src/cloudflare/resources/cloudforce_one/requests/message.py">update</a>(message_identifer, \*, account_identifier, request_identifier, \*\*<a href="src/cloudflare/types/cloudforce_one/requests/message_update_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/requests/message.py">Optional</a></code>
- <code title="delete /accounts/{account_identifier}/cloudforce-one/requests/{request_identifier}/message/{message_identifer}">client.cloudforce_one.requests.message.<a href="./src/cloudflare/resources/cloudforce_one/requests/message.py">delete</a>(message_identifer, \*, account_identifier, request_identifier) -> <a href="./src/cloudflare/types/cloudforce_one/requests/message_delete_response.py">MessageDeleteResponse</a></code>
- <code title="post /accounts/{account_identifier}/cloudforce-one/requests/{request_identifier}/message">client.cloudforce_one.requests.message.<a href="./src/cloudflare/resources/cloudforce_one/requests/message.py">get</a>(request_identifier, \*, account_identifier, \*\*<a href="src/cloudflare/types/cloudforce_one/requests/message_get_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/requests/message_get_response.py">Optional</a></code>

### Priority

Types:

```python
from cloudflare.types.cloudforce_one.requests import (
    Label,
    Priority,
    PriorityEdit,
    PriorityDeleteResponse,
)
```

Methods:

- <code title="post /accounts/{account_identifier}/cloudforce-one/requests/priority/new">client.cloudforce_one.requests.priority.<a href="./src/cloudflare/resources/cloudforce_one/requests/priority.py">create</a>(account_identifier, \*\*<a href="src/cloudflare/types/cloudforce_one/requests/priority_create_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/requests/priority.py">Optional</a></code>
- <code title="put /accounts/{account_identifier}/cloudforce-one/requests/priority/{priority_identifer}">client.cloudforce_one.requests.priority.<a href="./src/cloudflare/resources/cloudforce_one/requests/priority.py">update</a>(priority_identifer, \*, account_identifier, \*\*<a href="src/cloudflare/types/cloudforce_one/requests/priority_update_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/item.py">Optional</a></code>
- <code title="delete /accounts/{account_identifier}/cloudforce-one/requests/priority/{priority_identifer}">client.cloudforce_one.requests.priority.<a href="./src/cloudflare/resources/cloudforce_one/requests/priority.py">delete</a>(priority_identifer, \*, account_identifier) -> <a href="./src/cloudflare/types/cloudforce_one/requests/priority_delete_response.py">PriorityDeleteResponse</a></code>
- <code title="get /accounts/{account_identifier}/cloudforce-one/requests/priority/{priority_identifer}">client.cloudforce_one.requests.priority.<a href="./src/cloudflare/resources/cloudforce_one/requests/priority.py">get</a>(priority_identifer, \*, account_identifier) -> <a href="./src/cloudflare/types/cloudforce_one/item.py">Optional</a></code>
- <code title="get /accounts/{account_identifier}/cloudforce-one/requests/priority/quota">client.cloudforce_one.requests.priority.<a href="./src/cloudflare/resources/cloudforce_one/requests/priority.py">quota</a>(account_identifier) -> <a href="./src/cloudflare/types/cloudforce_one/quota.py">Optional</a></code>

# EventNotifications

## R2

### Configuration

Types:

```python
from cloudflare.types.event_notifications.r2 import ConfigurationGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/event_notifications/r2/{bucket_name}/configuration">client.event_notifications.r2.configuration.<a href="./src/cloudflare/resources/event_notifications/r2/configuration/configuration.py">get</a>(bucket_name, \*, account_id) -> <a href="./src/cloudflare/types/event_notifications/r2/configuration_get_response.py">ConfigurationGetResponse</a></code>

#### Queues

Types:

```python
from cloudflare.types.event_notifications.r2.configuration import (
    QueueUpdateResponse,
    QueueDeleteResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/event_notifications/r2/{bucket_name}/configuration/queues/{queue_id}">client.event_notifications.r2.configuration.queues.<a href="./src/cloudflare/resources/event_notifications/r2/configuration/queues.py">update</a>(queue_id, \*, account_id, bucket_name, \*\*<a href="src/cloudflare/types/event_notifications/r2/configuration/queue_update_params.py">params</a>) -> <a href="./src/cloudflare/types/event_notifications/r2/configuration/queue_update_response.py">QueueUpdateResponse</a></code>
- <code title="delete /accounts/{account_id}/event_notifications/r2/{bucket_name}/configuration/queues/{queue_id}">client.event_notifications.r2.configuration.queues.<a href="./src/cloudflare/resources/event_notifications/r2/configuration/queues.py">delete</a>(queue_id, \*, account_id, bucket_name) -> <a href="./src/cloudflare/types/event_notifications/r2/configuration/queue_delete_response.py">QueueDeleteResponse</a></code>

# AIGateway

Types:

```python
from cloudflare.types.ai_gateway import (
    AIGatewayCreateResponse,
    AIGatewayUpdateResponse,
    AIGatewayListResponse,
    AIGatewayDeleteResponse,
    AIGatewayGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/ai-gateway/gateways">client.ai_gateway.<a href="./src/cloudflare/resources/ai_gateway/ai_gateway.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/ai_gateway/ai_gateway_create_params.py">params</a>) -> <a href="./src/cloudflare/types/ai_gateway/ai_gateway_create_response.py">AIGatewayCreateResponse</a></code>
- <code title="put /accounts/{account_id}/ai-gateway/gateways/{id}">client.ai_gateway.<a href="./src/cloudflare/resources/ai_gateway/ai_gateway.py">update</a>(id, \*, account_id, \*\*<a href="src/cloudflare/types/ai_gateway/ai_gateway_update_params.py">params</a>) -> <a href="./src/cloudflare/types/ai_gateway/ai_gateway_update_response.py">AIGatewayUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/ai-gateway/gateways">client.ai_gateway.<a href="./src/cloudflare/resources/ai_gateway/ai_gateway.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/ai_gateway/ai_gateway_list_params.py">params</a>) -> <a href="./src/cloudflare/types/ai_gateway/ai_gateway_list_response.py">SyncV4PagePaginationArray[AIGatewayListResponse]</a></code>
- <code title="delete /accounts/{account_id}/ai-gateway/gateways/{id}">client.ai_gateway.<a href="./src/cloudflare/resources/ai_gateway/ai_gateway.py">delete</a>(id, \*, account_id) -> <a href="./src/cloudflare/types/ai_gateway/ai_gateway_delete_response.py">AIGatewayDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/ai-gateway/gateways/{id}">client.ai_gateway.<a href="./src/cloudflare/resources/ai_gateway/ai_gateway.py">get</a>(id, \*, account_id) -> <a href="./src/cloudflare/types/ai_gateway/ai_gateway_get_response.py">AIGatewayGetResponse</a></code>

## Logs

Types:

```python
from cloudflare.types.ai_gateway import LogListResponse
```

Methods:

- <code title="get /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs">client.ai_gateway.logs.<a href="./src/cloudflare/resources/ai_gateway/logs.py">list</a>(gateway_id, \*, account_id, \*\*<a href="src/cloudflare/types/ai_gateway/log_list_params.py">params</a>) -> <a href="./src/cloudflare/types/ai_gateway/log_list_response.py">SyncV4PagePaginationArray[LogListResponse]</a></code>

# IAM

## PermissionGroups

Types:

```python
from cloudflare.types.iam import PermissionGroupListResponse, PermissionGroupGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/iam/permission_groups">client.iam.permission_groups.<a href="./src/cloudflare/resources/iam/permission_groups.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/iam/permission_group_list_params.py">params</a>) -> <a href="./src/cloudflare/types/iam/permission_group_list_response.py">SyncV4PagePaginationArray[object]</a></code>
- <code title="get /accounts/{account_id}/iam/permission_groups/{permission_group_id}">client.iam.permission_groups.<a href="./src/cloudflare/resources/iam/permission_groups.py">get</a>(permission_group_id, \*, account_id) -> <a href="./src/cloudflare/types/iam/permission_group_get_response.py">PermissionGroupGetResponse</a></code>

## ResourceGroups

Types:

```python
from cloudflare.types.iam import (
    ResourceGroupCreateResponse,
    ResourceGroupUpdateResponse,
    ResourceGroupListResponse,
    ResourceGroupDeleteResponse,
    ResourceGroupGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/iam/resource_groups">client.iam.resource_groups.<a href="./src/cloudflare/resources/iam/resource_groups.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/iam/resource_group_create_params.py">params</a>) -> <a href="./src/cloudflare/types/iam/resource_group_create_response.py">ResourceGroupCreateResponse</a></code>
- <code title="put /accounts/{account_id}/iam/resource_groups/{resource_group_id}">client.iam.resource_groups.<a href="./src/cloudflare/resources/iam/resource_groups.py">update</a>(resource_group_id, \*, account_id, \*\*<a href="src/cloudflare/types/iam/resource_group_update_params.py">params</a>) -> <a href="./src/cloudflare/types/iam/resource_group_update_response.py">ResourceGroupUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/iam/resource_groups">client.iam.resource_groups.<a href="./src/cloudflare/resources/iam/resource_groups.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/iam/resource_group_list_params.py">params</a>) -> <a href="./src/cloudflare/types/iam/resource_group_list_response.py">SyncV4PagePaginationArray[object]</a></code>
- <code title="delete /accounts/{account_id}/iam/resource_groups/{resource_group_id}">client.iam.resource_groups.<a href="./src/cloudflare/resources/iam/resource_groups.py">delete</a>(resource_group_id, \*, account_id) -> <a href="./src/cloudflare/types/iam/resource_group_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/iam/resource_groups/{resource_group_id}">client.iam.resource_groups.<a href="./src/cloudflare/resources/iam/resource_groups.py">get</a>(resource_group_id, \*, account_id) -> <a href="./src/cloudflare/types/iam/resource_group_get_response.py">ResourceGroupGetResponse</a></code>

# CloudConnector

## Rules

Types:

```python
from cloudflare.types.cloud_connector import RuleUpdateResponse, RuleListResponse
```

Methods:

- <code title="put /zones/{zone_id}/cloud_connector/rules">client.cloud_connector.rules.<a href="./src/cloudflare/resources/cloud_connector/rules.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/cloud_connector/rule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/cloud_connector/rule_update_response.py">Optional</a></code>
- <code title="get /zones/{zone_id}/cloud_connector/rules">client.cloud_connector.rules.<a href="./src/cloudflare/resources/cloud_connector/rules.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/cloud_connector/rule_list_response.py">SyncSinglePage[RuleListResponse]</a></code>

# BotnetFeed

## ASN

Types:

```python
from cloudflare.types.botnet_feed import ASNDayReportResponse, ASNFullReportResponse
```

Methods:

- <code title="get /accounts/{account_id}/botnet_feed/asn/{asn_id}/day_report">client.botnet_feed.asn.<a href="./src/cloudflare/resources/botnet_feed/asn.py">day_report</a>(asn_id, \*, account_id, \*\*<a href="src/cloudflare/types/botnet_feed/asn_day_report_params.py">params</a>) -> <a href="./src/cloudflare/types/botnet_feed/asn_day_report_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/botnet_feed/asn/{asn_id}/full_report">client.botnet_feed.asn.<a href="./src/cloudflare/resources/botnet_feed/asn.py">full_report</a>(asn_id, \*, account_id) -> <a href="./src/cloudflare/types/botnet_feed/asn_full_report_response.py">Optional</a></code>

## Configs

### ASN

Types:

```python
from cloudflare.types.botnet_feed.configs import ASNDeleteResponse, ASNGetResponse
```

Methods:

- <code title="delete /accounts/{account_id}/botnet_feed/configs/asn/{asn_id}">client.botnet_feed.configs.asn.<a href="./src/cloudflare/resources/botnet_feed/configs/asn.py">delete</a>(asn_id, \*, account_id) -> <a href="./src/cloudflare/types/botnet_feed/configs/asn_delete_response.py">Optional</a></code>
- <code title="get /accounts/{account_id}/botnet_feed/configs/asn">client.botnet_feed.configs.asn.<a href="./src/cloudflare/resources/botnet_feed/configs/asn.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/botnet_feed/configs/asn_get_response.py">Optional</a></code>
