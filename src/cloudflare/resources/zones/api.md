# Zones

Types:

```python
from cloudflare.types.zones import Type, Zone, ZoneDeleteResponse
```

Methods:

- <code title="post /zones">client.zones.<a href="./src/cloudflare/resources/zones/zones.py">create</a>(\*\*<a href="src/cloudflare/types/zones/zone_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/zone.py">Optional[Zone]</a></code>
- <code title="get /zones">client.zones.<a href="./src/cloudflare/resources/zones/zones.py">list</a>(\*\*<a href="src/cloudflare/types/zones/zone_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/zone.py">SyncV4PagePaginationArray[Zone]</a></code>
- <code title="delete /zones/{zone_id}">client.zones.<a href="./src/cloudflare/resources/zones/zones.py">delete</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/zone_delete_response.py">Optional[ZoneDeleteResponse]</a></code>
- <code title="patch /zones/{zone_id}">client.zones.<a href="./src/cloudflare/resources/zones/zones.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/zone_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/zone.py">Optional[Zone]</a></code>
- <code title="get /zones/{zone_id}">client.zones.<a href="./src/cloudflare/resources/zones/zones.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/zone.py">Optional[Zone]</a></code>

## ActivationCheck

Types:

```python
from cloudflare.types.zones import ActivationCheckTriggerResponse
```

Methods:

- <code title="put /zones/{zone_id}/activation_check">client.zones.activation_check.<a href="./src/cloudflare/resources/zones/activation_check.py">trigger</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/activation_check_trigger_response.py">Optional[ActivationCheckTriggerResponse]</a></code>

## Settings

Types:

```python
from cloudflare.types.zones import (
    AdvancedDDoS,
    Aegis,
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

- <code title="patch /zones/{zone_id}/settings/{setting_id}">client.zones.settings.<a href="./src/cloudflare/resources/zones/settings.py">edit</a>(setting_id, \*, zone_id, \*\*<a href="src/cloudflare/types/zones/setting_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/setting_edit_response.py">Optional[SettingEditResponse]</a></code>
- <code title="get /zones/{zone_id}/settings/{setting_id}">client.zones.settings.<a href="./src/cloudflare/resources/zones/settings.py">get</a>(setting_id, \*, zone_id) -> <a href="./src/cloudflare/types/zones/setting_get_response.py">Optional[SettingGetResponse]</a></code>

## Environments

Types:

```python
from cloudflare.types.zones import (
    EnvironmentCreateResponse,
    EnvironmentUpdateResponse,
    EnvironmentListResponse,
    EnvironmentDeleteResponse,
    EnvironmentEditResponse,
    EnvironmentRollbackResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/environments">client.zones.environments.<a href="./src/cloudflare/resources/zones/environments.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/environment_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/environment_create_response.py">EnvironmentCreateResponse</a></code>
- <code title="put /zones/{zone_id}/environments">client.zones.environments.<a href="./src/cloudflare/resources/zones/environments.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/environment_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/environment_update_response.py">EnvironmentUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/environments">client.zones.environments.<a href="./src/cloudflare/resources/zones/environments.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/environment_list_response.py">EnvironmentListResponse</a></code>
- <code title="delete /zones/{zone_id}/environments/{environment_id}">client.zones.environments.<a href="./src/cloudflare/resources/zones/environments.py">delete</a>(environment_id, \*, zone_id) -> <a href="./src/cloudflare/types/zones/environment_delete_response.py">EnvironmentDeleteResponse</a></code>
- <code title="patch /zones/{zone_id}/environments">client.zones.environments.<a href="./src/cloudflare/resources/zones/environments.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/environment_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/environment_edit_response.py">EnvironmentEditResponse</a></code>
- <code title="post /zones/{zone_id}/environments/{environment_id}/rollback">client.zones.environments.<a href="./src/cloudflare/resources/zones/environments.py">rollback</a>(environment_id, \*, zone_id) -> <a href="./src/cloudflare/types/zones/environment_rollback_response.py">EnvironmentRollbackResponse</a></code>

## CustomNameservers

Types:

```python
from cloudflare.types.zones import CustomNameserverUpdateResponse, CustomNameserverGetResponse
```

Methods:

- <code title="put /zones/{zone_id}/custom_ns">client.zones.custom_nameservers.<a href="./src/cloudflare/resources/zones/custom_nameservers.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/custom_nameserver_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/custom_nameserver_update_response.py">SyncSinglePage[CustomNameserverUpdateResponse]</a></code>
- <code title="get /zones/{zone_id}/custom_ns">client.zones.custom_nameservers.<a href="./src/cloudflare/resources/zones/custom_nameservers.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/custom_nameserver_get_response.py">CustomNameserverGetResponse</a></code>

## Holds

Types:

```python
from cloudflare.types.zones import ZoneHold
```

Methods:

- <code title="post /zones/{zone_id}/hold">client.zones.holds.<a href="./src/cloudflare/resources/zones/holds.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/hold_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/zone_hold.py">ZoneHold</a></code>
- <code title="delete /zones/{zone_id}/hold">client.zones.holds.<a href="./src/cloudflare/resources/zones/holds.py">delete</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/hold_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/zone_hold.py">ZoneHold</a></code>
- <code title="patch /zones/{zone_id}/hold">client.zones.holds.<a href="./src/cloudflare/resources/zones/holds.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/hold_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/zone_hold.py">ZoneHold</a></code>
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

- <code title="post /zones/{zone_id}/subscription">client.zones.subscriptions.<a href="./src/cloudflare/resources/zones/subscriptions.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/subscription_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/subscription_create_response.py">SubscriptionCreateResponse</a></code>
- <code title="put /zones/{zone_id}/subscription">client.zones.subscriptions.<a href="./src/cloudflare/resources/zones/subscriptions.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zones/subscription_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zones/subscription_update_response.py">SubscriptionUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/subscription">client.zones.subscriptions.<a href="./src/cloudflare/resources/zones/subscriptions.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/subscription_get_response.py">SubscriptionGetResponse</a></code>

## Plans

Types:

```python
from cloudflare.types.zones import AvailableRatePlan
```

Methods:

- <code title="get /zones/{zone_id}/available_plans">client.zones.plans.<a href="./src/cloudflare/resources/zones/plans.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/available_rate_plan.py">SyncSinglePage[AvailableRatePlan]</a></code>
- <code title="get /zones/{zone_id}/available_plans/{plan_identifier}">client.zones.plans.<a href="./src/cloudflare/resources/zones/plans.py">get</a>(plan_identifier, \*, zone_id) -> <a href="./src/cloudflare/types/zones/available_rate_plan.py">AvailableRatePlan</a></code>

## RatePlans

Types:

```python
from cloudflare.types.zones import RatePlanGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/available_rate_plans">client.zones.rate_plans.<a href="./src/cloudflare/resources/zones/rate_plans.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zones/rate_plan_get_response.py">SyncSinglePage[RatePlanGetResponse]</a></code>
