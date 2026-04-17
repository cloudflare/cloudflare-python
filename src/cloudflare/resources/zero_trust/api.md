# ZeroTrust

## Devices

Types:

```python
from cloudflare.types.zero_trust import Device, DeviceGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/devices">client.zero_trust.devices.<a href="./src/cloudflare/resources/zero_trust/devices/devices.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/device.py">SyncSinglePage[Device]</a></code>
- <code title="get /accounts/{account_id}/devices/{device_id}">client.zero_trust.devices.<a href="./src/cloudflare/resources/zero_trust/devices/devices.py">get</a>(device_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/device_get_response.py">Optional[DeviceGetResponse]</a></code>

### Devices

Types:

```python
from cloudflare.types.zero_trust.devices import DeviceListResponse, DeviceGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/devices/physical-devices">client.zero*trust.devices.devices.<a href="./src/cloudflare/resources/zero_trust/devices/devices*.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/device_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/device_list_response.py">SyncCursorPagination[DeviceListResponse]</a></code>
- <code title="delete /accounts/{account_id}/devices/physical-devices/{device_id}">client.zero*trust.devices.devices.<a href="./src/cloudflare/resources/zero_trust/devices/devices*.py">delete</a>(device_id, \*, account_id) -> object</code>
- <code title="get /accounts/{account_id}/devices/physical-devices/{device_id}">client.zero*trust.devices.devices.<a href="./src/cloudflare/resources/zero_trust/devices/devices*.py">get</a>(device_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/device_get_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/device_get_response.py">DeviceGetResponse</a></code>
- <code title="post /accounts/{account_id}/devices/physical-devices/{device_id}/revoke">client.zero*trust.devices.devices.<a href="./src/cloudflare/resources/zero_trust/devices/devices*.py">revoke</a>(device_id, \*, account_id) -> object</code>

### Resilience

#### GlobalWARPOverride

Types:

```python
from cloudflare.types.zero_trust.devices.resilience import (
    GlobalWARPOverrideCreateResponse,
    GlobalWARPOverrideGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/devices/resilience/disconnect">client.zero_trust.devices.resilience.global_warp_override.<a href="./src/cloudflare/resources/zero_trust/devices/resilience/global_warp_override.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/resilience/global_warp_override_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/resilience/global_warp_override_create_response.py">Optional[GlobalWARPOverrideCreateResponse]</a></code>
- <code title="get /accounts/{account_id}/devices/resilience/disconnect">client.zero_trust.devices.resilience.global_warp_override.<a href="./src/cloudflare/resources/zero_trust/devices/resilience/global_warp_override.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/resilience/global_warp_override_get_response.py">Optional[GlobalWARPOverrideGetResponse]</a></code>

### Registrations

Types:

```python
from cloudflare.types.zero_trust.devices import RegistrationListResponse, RegistrationGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/devices/registrations">client.zero_trust.devices.registrations.<a href="./src/cloudflare/resources/zero_trust/devices/registrations.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/registration_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/registration_list_response.py">SyncCursorPagination[RegistrationListResponse]</a></code>
- <code title="delete /accounts/{account_id}/devices/registrations/{registration_id}">client.zero_trust.devices.registrations.<a href="./src/cloudflare/resources/zero_trust/devices/registrations.py">delete</a>(registration_id, \*, account_id) -> object</code>
- <code title="delete /accounts/{account_id}/devices/registrations">client.zero_trust.devices.registrations.<a href="./src/cloudflare/resources/zero_trust/devices/registrations.py">bulk_delete</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/registration_bulk_delete_params.py">params</a>) -> object</code>
- <code title="get /accounts/{account_id}/devices/registrations/{registration_id}">client.zero_trust.devices.registrations.<a href="./src/cloudflare/resources/zero_trust/devices/registrations.py">get</a>(registration_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/registration_get_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/registration_get_response.py">RegistrationGetResponse</a></code>
- <code title="post /accounts/{account_id}/devices/registrations/revoke">client.zero_trust.devices.registrations.<a href="./src/cloudflare/resources/zero_trust/devices/registrations.py">revoke</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/registration_revoke_params.py">params</a>) -> object</code>
- <code title="post /accounts/{account_id}/devices/registrations/unrevoke">client.zero_trust.devices.registrations.<a href="./src/cloudflare/resources/zero_trust/devices/registrations.py">unrevoke</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/registration_unrevoke_params.py">params</a>) -> object</code>

### DEXTests

Types:

```python
from cloudflare.types.zero_trust.devices import (
    SchemaData,
    SchemaHTTP,
    DEXTestCreateResponse,
    DEXTestUpdateResponse,
    DEXTestListResponse,
    DEXTestDeleteResponse,
    DEXTestGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/dex/devices/dex_tests">client.zero_trust.devices.dex_tests.<a href="./src/cloudflare/resources/zero_trust/devices/dex_tests.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/dex_test_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/dex_test_create_response.py">Optional[DEXTestCreateResponse]</a></code>
- <code title="put /accounts/{account_id}/dex/devices/dex_tests/{dex_test_id}">client.zero_trust.devices.dex_tests.<a href="./src/cloudflare/resources/zero_trust/devices/dex_tests.py">update</a>(dex_test_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/dex_test_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/dex_test_update_response.py">Optional[DEXTestUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/dex/devices/dex_tests">client.zero_trust.devices.dex_tests.<a href="./src/cloudflare/resources/zero_trust/devices/dex_tests.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/dex_test_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/dex_test_list_response.py">SyncV4PagePaginationArray[DEXTestListResponse]</a></code>
- <code title="delete /accounts/{account_id}/dex/devices/dex_tests/{dex_test_id}">client.zero_trust.devices.dex_tests.<a href="./src/cloudflare/resources/zero_trust/devices/dex_tests.py">delete</a>(dex_test_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/dex_test_delete_response.py">Optional[DEXTestDeleteResponse]</a></code>
- <code title="get /accounts/{account_id}/dex/devices/dex_tests/{dex_test_id}">client.zero_trust.devices.dex_tests.<a href="./src/cloudflare/resources/zero_trust/devices/dex_tests.py">get</a>(dex_test_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/dex_test_get_response.py">Optional[DEXTestGetResponse]</a></code>

### IPProfiles

Types:

```python
from cloudflare.types.zero_trust.devices import IPProfile, IPProfileDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/devices/ip-profiles">client.zero_trust.devices.ip_profiles.<a href="./src/cloudflare/resources/zero_trust/devices/ip_profiles.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/ip_profile_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/ip_profile.py">IPProfile</a></code>
- <code title="patch /accounts/{account_id}/devices/ip-profiles/{profile_id}">client.zero_trust.devices.ip_profiles.<a href="./src/cloudflare/resources/zero_trust/devices/ip_profiles.py">update</a>(profile_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/ip_profile_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/ip_profile.py">IPProfile</a></code>
- <code title="get /accounts/{account_id}/devices/ip-profiles">client.zero_trust.devices.ip_profiles.<a href="./src/cloudflare/resources/zero_trust/devices/ip_profiles.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/ip_profile_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/ip_profile.py">SyncSinglePage[IPProfile]</a></code>
- <code title="delete /accounts/{account_id}/devices/ip-profiles/{profile_id}">client.zero_trust.devices.ip_profiles.<a href="./src/cloudflare/resources/zero_trust/devices/ip_profiles.py">delete</a>(profile_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/ip_profile_delete_response.py">IPProfileDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/devices/ip-profiles/{profile_id}">client.zero_trust.devices.ip_profiles.<a href="./src/cloudflare/resources/zero_trust/devices/ip_profiles.py">get</a>(profile_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/ip_profile.py">IPProfile</a></code>

### Networks

Types:

```python
from cloudflare.types.zero_trust.devices import DeviceNetwork
```

Methods:

- <code title="post /accounts/{account_id}/devices/networks">client.zero_trust.devices.networks.<a href="./src/cloudflare/resources/zero_trust/devices/networks.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/network_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/device_network.py">Optional[DeviceNetwork]</a></code>
- <code title="put /accounts/{account_id}/devices/networks/{network_id}">client.zero_trust.devices.networks.<a href="./src/cloudflare/resources/zero_trust/devices/networks.py">update</a>(network_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/network_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/device_network.py">Optional[DeviceNetwork]</a></code>
- <code title="get /accounts/{account_id}/devices/networks">client.zero_trust.devices.networks.<a href="./src/cloudflare/resources/zero_trust/devices/networks.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/device_network.py">SyncSinglePage[DeviceNetwork]</a></code>
- <code title="delete /accounts/{account_id}/devices/networks/{network_id}">client.zero_trust.devices.networks.<a href="./src/cloudflare/resources/zero_trust/devices/networks.py">delete</a>(network_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/device_network.py">SyncSinglePage[DeviceNetwork]</a></code>
- <code title="get /accounts/{account_id}/devices/networks/{network_id}">client.zero_trust.devices.networks.<a href="./src/cloudflare/resources/zero_trust/devices/networks.py">get</a>(network_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/device_network.py">Optional[DeviceNetwork]</a></code>

### FleetStatus

Types:

```python
from cloudflare.types.zero_trust.devices import FleetStatusGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/dex/devices/{device_id}/fleet-status/live">client.zero_trust.devices.fleet_status.<a href="./src/cloudflare/resources/zero_trust/devices/fleet_status.py">get</a>(device_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/fleet_status_get_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/fleet_status_get_response.py">FleetStatusGetResponse</a></code>

### Policies

Types:

```python
from cloudflare.types.zero_trust.devices import (
    DevicePolicyCertificates,
    FallbackDomain,
    FallbackDomainPolicy,
    SettingsPolicy,
    SplitTunnelExclude,
    SplitTunnelInclude,
)
```

#### Default

Types:

```python
from cloudflare.types.zero_trust.devices.policies import DefaultEditResponse, DefaultGetResponse
```

Methods:

- <code title="patch /accounts/{account_id}/devices/policy">client.zero_trust.devices.policies.default.<a href="./src/cloudflare/resources/zero_trust/devices/policies/default/default.py">edit</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/policies/default_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/policies/default_edit_response.py">Optional[DefaultEditResponse]</a></code>
- <code title="get /accounts/{account_id}/devices/policy">client.zero_trust.devices.policies.default.<a href="./src/cloudflare/resources/zero_trust/devices/policies/default/default.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/policies/default_get_response.py">Optional[DefaultGetResponse]</a></code>

##### Excludes

Methods:

- <code title="put /accounts/{account_id}/devices/policy/exclude">client.zero_trust.devices.policies.default.excludes.<a href="./src/cloudflare/resources/zero_trust/devices/policies/default/excludes.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/policies/default/exclude_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/split_tunnel_exclude.py">SyncSinglePage[SplitTunnelExclude]</a></code>
- <code title="get /accounts/{account_id}/devices/policy/exclude">client.zero_trust.devices.policies.default.excludes.<a href="./src/cloudflare/resources/zero_trust/devices/policies/default/excludes.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/split_tunnel_exclude.py">SyncSinglePage[SplitTunnelExclude]</a></code>

##### Includes

Methods:

- <code title="put /accounts/{account_id}/devices/policy/include">client.zero_trust.devices.policies.default.includes.<a href="./src/cloudflare/resources/zero_trust/devices/policies/default/includes.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/policies/default/include_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/split_tunnel_include.py">SyncSinglePage[SplitTunnelInclude]</a></code>
- <code title="get /accounts/{account_id}/devices/policy/include">client.zero_trust.devices.policies.default.includes.<a href="./src/cloudflare/resources/zero_trust/devices/policies/default/includes.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/split_tunnel_include.py">SyncSinglePage[SplitTunnelInclude]</a></code>

##### FallbackDomains

Methods:

- <code title="put /accounts/{account_id}/devices/policy/fallback_domains">client.zero_trust.devices.policies.default.fallback_domains.<a href="./src/cloudflare/resources/zero_trust/devices/policies/default/fallback_domains.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/policies/default/fallback_domain_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/fallback_domain.py">SyncSinglePage[FallbackDomain]</a></code>
- <code title="get /accounts/{account_id}/devices/policy/fallback_domains">client.zero_trust.devices.policies.default.fallback_domains.<a href="./src/cloudflare/resources/zero_trust/devices/policies/default/fallback_domains.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/fallback_domain.py">SyncSinglePage[FallbackDomain]</a></code>

##### Certificates

Methods:

- <code title="patch /zones/{zone_id}/devices/policy/certificates">client.zero_trust.devices.policies.default.certificates.<a href="./src/cloudflare/resources/zero_trust/devices/policies/default/certificates.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/policies/default/certificate_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/device_policy_certificates.py">Optional[DevicePolicyCertificates]</a></code>
- <code title="get /zones/{zone_id}/devices/policy/certificates">client.zero_trust.devices.policies.default.certificates.<a href="./src/cloudflare/resources/zero_trust/devices/policies/default/certificates.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zero_trust/devices/device_policy_certificates.py">Optional[DevicePolicyCertificates]</a></code>

#### Custom

Methods:

- <code title="post /accounts/{account_id}/devices/policy">client.zero_trust.devices.policies.custom.<a href="./src/cloudflare/resources/zero_trust/devices/policies/custom/custom.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/policies/custom_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/settings_policy.py">Optional[SettingsPolicy]</a></code>
- <code title="get /accounts/{account_id}/devices/policies">client.zero_trust.devices.policies.custom.<a href="./src/cloudflare/resources/zero_trust/devices/policies/custom/custom.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/settings_policy.py">SyncSinglePage[SettingsPolicy]</a></code>
- <code title="delete /accounts/{account_id}/devices/policy/{policy_id}">client.zero_trust.devices.policies.custom.<a href="./src/cloudflare/resources/zero_trust/devices/policies/custom/custom.py">delete</a>(policy_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/settings_policy.py">SyncSinglePage[SettingsPolicy]</a></code>
- <code title="patch /accounts/{account_id}/devices/policy/{policy_id}">client.zero_trust.devices.policies.custom.<a href="./src/cloudflare/resources/zero_trust/devices/policies/custom/custom.py">edit</a>(policy_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/policies/custom_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/settings_policy.py">Optional[SettingsPolicy]</a></code>
- <code title="get /accounts/{account_id}/devices/policy/{policy_id}">client.zero_trust.devices.policies.custom.<a href="./src/cloudflare/resources/zero_trust/devices/policies/custom/custom.py">get</a>(policy_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/settings_policy.py">Optional[SettingsPolicy]</a></code>

##### Excludes

Methods:

- <code title="put /accounts/{account_id}/devices/policy/{policy_id}/exclude">client.zero_trust.devices.policies.custom.excludes.<a href="./src/cloudflare/resources/zero_trust/devices/policies/custom/excludes.py">update</a>(policy_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/policies/custom/exclude_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/split_tunnel_exclude.py">SyncSinglePage[SplitTunnelExclude]</a></code>
- <code title="get /accounts/{account_id}/devices/policy/{policy_id}/exclude">client.zero_trust.devices.policies.custom.excludes.<a href="./src/cloudflare/resources/zero_trust/devices/policies/custom/excludes.py">get</a>(policy_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/split_tunnel_exclude.py">SyncSinglePage[SplitTunnelExclude]</a></code>

##### Includes

Methods:

- <code title="put /accounts/{account_id}/devices/policy/{policy_id}/include">client.zero_trust.devices.policies.custom.includes.<a href="./src/cloudflare/resources/zero_trust/devices/policies/custom/includes.py">update</a>(policy_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/policies/custom/include_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/split_tunnel_include.py">SyncSinglePage[SplitTunnelInclude]</a></code>
- <code title="get /accounts/{account_id}/devices/policy/{policy_id}/include">client.zero_trust.devices.policies.custom.includes.<a href="./src/cloudflare/resources/zero_trust/devices/policies/custom/includes.py">get</a>(policy_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/split_tunnel_include.py">SyncSinglePage[SplitTunnelInclude]</a></code>

##### FallbackDomains

Methods:

- <code title="put /accounts/{account_id}/devices/policy/{policy_id}/fallback_domains">client.zero_trust.devices.policies.custom.fallback_domains.<a href="./src/cloudflare/resources/zero_trust/devices/policies/custom/fallback_domains.py">update</a>(policy_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/policies/custom/fallback_domain_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/fallback_domain.py">SyncSinglePage[FallbackDomain]</a></code>
- <code title="get /accounts/{account_id}/devices/policy/{policy_id}/fallback_domains">client.zero_trust.devices.policies.custom.fallback_domains.<a href="./src/cloudflare/resources/zero_trust/devices/policies/custom/fallback_domains.py">get</a>(policy_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/fallback_domain.py">SyncSinglePage[FallbackDomain]</a></code>

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

- <code title="post /accounts/{account_id}/devices/posture">client.zero_trust.devices.posture.<a href="./src/cloudflare/resources/zero_trust/devices/posture/posture.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/posture_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/device_posture_rule.py">Optional[DevicePostureRule]</a></code>
- <code title="put /accounts/{account_id}/devices/posture/{rule_id}">client.zero_trust.devices.posture.<a href="./src/cloudflare/resources/zero_trust/devices/posture/posture.py">update</a>(rule_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/posture_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/device_posture_rule.py">Optional[DevicePostureRule]</a></code>
- <code title="get /accounts/{account_id}/devices/posture">client.zero_trust.devices.posture.<a href="./src/cloudflare/resources/zero_trust/devices/posture/posture.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/device_posture_rule.py">SyncSinglePage[DevicePostureRule]</a></code>
- <code title="delete /accounts/{account_id}/devices/posture/{rule_id}">client.zero_trust.devices.posture.<a href="./src/cloudflare/resources/zero_trust/devices/posture/posture.py">delete</a>(rule_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/posture_delete_response.py">Optional[PostureDeleteResponse]</a></code>
- <code title="get /accounts/{account_id}/devices/posture/{rule_id}">client.zero_trust.devices.posture.<a href="./src/cloudflare/resources/zero_trust/devices/posture/posture.py">get</a>(rule_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/device_posture_rule.py">Optional[DevicePostureRule]</a></code>

#### Integrations

Types:

```python
from cloudflare.types.zero_trust.devices.posture import Integration, IntegrationDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/devices/posture/integration">client.zero_trust.devices.posture.integrations.<a href="./src/cloudflare/resources/zero_trust/devices/posture/integrations.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/posture/integration_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/posture/integration.py">Optional[Integration]</a></code>
- <code title="get /accounts/{account_id}/devices/posture/integration">client.zero_trust.devices.posture.integrations.<a href="./src/cloudflare/resources/zero_trust/devices/posture/integrations.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/posture/integration.py">SyncSinglePage[Integration]</a></code>
- <code title="delete /accounts/{account_id}/devices/posture/integration/{integration_id}">client.zero_trust.devices.posture.integrations.<a href="./src/cloudflare/resources/zero_trust/devices/posture/integrations.py">delete</a>(integration_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/posture/integration_delete_response.py">Optional[IntegrationDeleteResponse]</a></code>
- <code title="patch /accounts/{account_id}/devices/posture/integration/{integration_id}">client.zero_trust.devices.posture.integrations.<a href="./src/cloudflare/resources/zero_trust/devices/posture/integrations.py">edit</a>(integration_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/posture/integration_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/posture/integration.py">Optional[Integration]</a></code>
- <code title="get /accounts/{account_id}/devices/posture/integration/{integration_id}">client.zero_trust.devices.posture.integrations.<a href="./src/cloudflare/resources/zero_trust/devices/posture/integrations.py">get</a>(integration_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/posture/integration.py">Optional[Integration]</a></code>

### Revoke

Types:

```python
from cloudflare.types.zero_trust.devices import RevokeCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/devices/revoke">client.zero_trust.devices.revoke.<a href="./src/cloudflare/resources/zero_trust/devices/revoke.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/revoke_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/revoke_create_response.py">Optional[RevokeCreateResponse]</a></code>

### Settings

Types:

```python
from cloudflare.types.zero_trust.devices import DeviceSettings
```

Methods:

- <code title="put /accounts/{account_id}/devices/settings">client.zero_trust.devices.settings.<a href="./src/cloudflare/resources/zero_trust/devices/settings.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/setting_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/device_settings.py">Optional[DeviceSettings]</a></code>
- <code title="delete /accounts/{account_id}/devices/settings">client.zero_trust.devices.settings.<a href="./src/cloudflare/resources/zero_trust/devices/settings.py">delete</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/device_settings.py">Optional[DeviceSettings]</a></code>
- <code title="patch /accounts/{account_id}/devices/settings">client.zero_trust.devices.settings.<a href="./src/cloudflare/resources/zero_trust/devices/settings.py">edit</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/setting_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/device_settings.py">Optional[DeviceSettings]</a></code>
- <code title="get /accounts/{account_id}/devices/settings">client.zero_trust.devices.settings.<a href="./src/cloudflare/resources/zero_trust/devices/settings.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/device_settings.py">Optional[DeviceSettings]</a></code>

### Unrevoke

Types:

```python
from cloudflare.types.zero_trust.devices import UnrevokeCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/devices/unrevoke">client.zero_trust.devices.unrevoke.<a href="./src/cloudflare/resources/zero_trust/devices/unrevoke.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/devices/unrevoke_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/devices/unrevoke_create_response.py">Optional[UnrevokeCreateResponse]</a></code>

### OverrideCodes

Types:

```python
from cloudflare.types.zero_trust.devices import OverrideCodeGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/devices/{device_id}/override_codes">client.zero_trust.devices.override_codes.<a href="./src/cloudflare/resources/zero_trust/devices/override_codes.py">list</a>(device_id, \*, account_id) -> SyncSinglePage[object]</code>
- <code title="get /accounts/{account_id}/devices/registrations/{registration_id}/override_codes">client.zero_trust.devices.override_codes.<a href="./src/cloudflare/resources/zero_trust/devices/override_codes.py">get</a>(registration_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/devices/override_code_get_response.py">OverrideCodeGetResponse</a></code>

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

- <code title="post /{accounts_or_zones}/{account_or_zone_id}/access/identity_providers">client.zero_trust.identity_providers.<a href="./src/cloudflare/resources/zero_trust/identity_providers/identity_providers.py">create</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/identity_provider_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/identity_provider.py">Optional[IdentityProvider]</a></code>
- <code title="put /{accounts_or_zones}/{account_or_zone_id}/access/identity_providers/{identity_provider_id}">client.zero_trust.identity_providers.<a href="./src/cloudflare/resources/zero_trust/identity_providers/identity_providers.py">update</a>(identity_provider_id, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/identity_provider_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/identity_provider.py">Optional[IdentityProvider]</a></code>
- <code title="get /{accounts_or_zones}/{account_or_zone_id}/access/identity_providers">client.zero_trust.identity_providers.<a href="./src/cloudflare/resources/zero_trust/identity_providers/identity_providers.py">list</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/identity_provider_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/identity_provider_list_response.py">SyncV4PagePaginationArray[IdentityProviderListResponse]</a></code>
- <code title="delete /{accounts_or_zones}/{account_or_zone_id}/access/identity_providers/{identity_provider_id}">client.zero_trust.identity_providers.<a href="./src/cloudflare/resources/zero_trust/identity_providers/identity_providers.py">delete</a>(identity_provider_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/identity_provider_delete_response.py">Optional[IdentityProviderDeleteResponse]</a></code>
- <code title="get /{accounts_or_zones}/{account_or_zone_id}/access/identity_providers/{identity_provider_id}">client.zero_trust.identity_providers.<a href="./src/cloudflare/resources/zero_trust/identity_providers/identity_providers.py">get</a>(identity_provider_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/identity_provider.py">Optional[IdentityProvider]</a></code>

### SCIM

#### Groups

Methods:

- <code title="get /accounts/{account_id}/access/identity_providers/{identity_provider_id}/scim/groups">client.zero_trust.identity_providers.scim.groups.<a href="./src/cloudflare/resources/zero_trust/identity_providers/scim/groups.py">list</a>(identity_provider_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/identity_providers/scim/group_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/zero_trust_group.py">SyncV4PagePaginationArray[ZeroTrustGroup]</a></code>

#### Users

Methods:

- <code title="get /accounts/{account_id}/access/identity_providers/{identity_provider_id}/scim/users">client.zero_trust.identity_providers.scim.users.<a href="./src/cloudflare/resources/zero_trust/identity_providers/scim/users.py">list</a>(identity_provider_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/identity_providers/scim/user_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/access_user.py">SyncV4PagePaginationArray[AccessUser]</a></code>

## Organizations

Types:

```python
from cloudflare.types.zero_trust import LoginDesign, Organization, OrganizationRevokeUsersResponse
```

Methods:

- <code title="post /{accounts_or_zones}/{account_or_zone_id}/access/organizations">client.zero_trust.organizations.<a href="./src/cloudflare/resources/zero_trust/organizations/organizations.py">create</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/organization_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/organization.py">Optional[Organization]</a></code>
- <code title="put /{accounts_or_zones}/{account_or_zone_id}/access/organizations">client.zero_trust.organizations.<a href="./src/cloudflare/resources/zero_trust/organizations/organizations.py">update</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/organization_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/organization.py">Optional[Organization]</a></code>
- <code title="get /{accounts_or_zones}/{account_or_zone_id}/access/organizations">client.zero_trust.organizations.<a href="./src/cloudflare/resources/zero_trust/organizations/organizations.py">list</a>(\*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/organization.py">Optional[Organization]</a></code>
- <code title="post /{accounts_or_zones}/{account_or_zone_id}/access/organizations/revoke_user">client.zero_trust.organizations.<a href="./src/cloudflare/resources/zero_trust/organizations/organizations.py">revoke_users</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/organization_revoke_users_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/organization_revoke_users_response.py">Optional[OrganizationRevokeUsersResponse]</a></code>

### DOH

Types:

```python
from cloudflare.types.zero_trust.organizations import DOHUpdateResponse, DOHGetResponse
```

Methods:

- <code title="put /accounts/{account_id}/access/organizations/doh">client.zero_trust.organizations.doh.<a href="./src/cloudflare/resources/zero_trust/organizations/doh.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/organizations/doh_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/organizations/doh_update_response.py">Optional[DOHUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/access/organizations/doh">client.zero_trust.organizations.doh.<a href="./src/cloudflare/resources/zero_trust/organizations/doh.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/organizations/doh_get_response.py">Optional[DOHGetResponse]</a></code>

## Seats

Types:

```python
from cloudflare.types.zero_trust import Seat
```

Methods:

- <code title="patch /accounts/{account_id}/access/seats">client.zero_trust.seats.<a href="./src/cloudflare/resources/zero_trust/seats.py">edit</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/seat_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/seat.py">SyncSinglePage[Seat]</a></code>

## Access

### AIControls

#### Mcp

##### Portals

Types:

```python
from cloudflare.types.zero_trust.access.ai_controls.mcp import (
    PortalCreateResponse,
    PortalUpdateResponse,
    PortalListResponse,
    PortalDeleteResponse,
    PortalReadResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/access/ai-controls/mcp/portals">client.zero_trust.access.ai_controls.mcp.portals.<a href="./src/cloudflare/resources/zero_trust/access/ai_controls/mcp/portals.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/ai_controls/mcp/portal_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/ai_controls/mcp/portal_create_response.py">PortalCreateResponse</a></code>
- <code title="put /accounts/{account_id}/access/ai-controls/mcp/portals/{id}">client.zero_trust.access.ai_controls.mcp.portals.<a href="./src/cloudflare/resources/zero_trust/access/ai_controls/mcp/portals.py">update</a>(id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/ai_controls/mcp/portal_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/ai_controls/mcp/portal_update_response.py">PortalUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/access/ai-controls/mcp/portals">client.zero_trust.access.ai_controls.mcp.portals.<a href="./src/cloudflare/resources/zero_trust/access/ai_controls/mcp/portals.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/ai_controls/mcp/portal_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/ai_controls/mcp/portal_list_response.py">SyncV4PagePaginationArray[PortalListResponse]</a></code>
- <code title="delete /accounts/{account_id}/access/ai-controls/mcp/portals/{id}">client.zero_trust.access.ai_controls.mcp.portals.<a href="./src/cloudflare/resources/zero_trust/access/ai_controls/mcp/portals.py">delete</a>(id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/ai_controls/mcp/portal_delete_response.py">PortalDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/access/ai-controls/mcp/portals/{id}">client.zero_trust.access.ai_controls.mcp.portals.<a href="./src/cloudflare/resources/zero_trust/access/ai_controls/mcp/portals.py">read</a>(id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/ai_controls/mcp/portal_read_response.py">PortalReadResponse</a></code>

##### Servers

Types:

```python
from cloudflare.types.zero_trust.access.ai_controls.mcp import (
    ServerCreateResponse,
    ServerUpdateResponse,
    ServerListResponse,
    ServerDeleteResponse,
    ServerReadResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/access/ai-controls/mcp/servers">client.zero_trust.access.ai_controls.mcp.servers.<a href="./src/cloudflare/resources/zero_trust/access/ai_controls/mcp/servers.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/ai_controls/mcp/server_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/ai_controls/mcp/server_create_response.py">ServerCreateResponse</a></code>
- <code title="put /accounts/{account_id}/access/ai-controls/mcp/servers/{id}">client.zero_trust.access.ai_controls.mcp.servers.<a href="./src/cloudflare/resources/zero_trust/access/ai_controls/mcp/servers.py">update</a>(id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/ai_controls/mcp/server_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/ai_controls/mcp/server_update_response.py">ServerUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/access/ai-controls/mcp/servers">client.zero_trust.access.ai_controls.mcp.servers.<a href="./src/cloudflare/resources/zero_trust/access/ai_controls/mcp/servers.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/ai_controls/mcp/server_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/ai_controls/mcp/server_list_response.py">SyncV4PagePaginationArray[ServerListResponse]</a></code>
- <code title="delete /accounts/{account_id}/access/ai-controls/mcp/servers/{id}">client.zero_trust.access.ai_controls.mcp.servers.<a href="./src/cloudflare/resources/zero_trust/access/ai_controls/mcp/servers.py">delete</a>(id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/ai_controls/mcp/server_delete_response.py">ServerDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/access/ai-controls/mcp/servers/{id}">client.zero_trust.access.ai_controls.mcp.servers.<a href="./src/cloudflare/resources/zero_trust/access/ai_controls/mcp/servers.py">read</a>(id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/ai_controls/mcp/server_read_response.py">ServerReadResponse</a></code>
- <code title="post /accounts/{account_id}/access/ai-controls/mcp/servers/{id}/sync">client.zero_trust.access.ai_controls.mcp.servers.<a href="./src/cloudflare/resources/zero_trust/access/ai_controls/mcp/servers.py">sync</a>(id, \*, account_id) -> object</code>

### GatewayCA

Types:

```python
from cloudflare.types.zero_trust.access import (
    GatewayCACreateResponse,
    GatewayCAListResponse,
    GatewayCADeleteResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/access/gateway_ca">client.zero_trust.access.gateway_ca.<a href="./src/cloudflare/resources/zero_trust/access/gateway_ca.py">create</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/gateway_ca_create_response.py">Optional[GatewayCACreateResponse]</a></code>
- <code title="get /accounts/{account_id}/access/gateway_ca">client.zero_trust.access.gateway_ca.<a href="./src/cloudflare/resources/zero_trust/access/gateway_ca.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/gateway_ca_list_response.py">SyncSinglePage[GatewayCAListResponse]</a></code>
- <code title="delete /accounts/{account_id}/access/gateway_ca/{certificate_id}">client.zero_trust.access.gateway_ca.<a href="./src/cloudflare/resources/zero_trust/access/gateway_ca.py">delete</a>(certificate_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/gateway_ca_delete_response.py">Optional[GatewayCADeleteResponse]</a></code>

### Infrastructure

#### Targets

Types:

```python
from cloudflare.types.zero_trust.access.infrastructure import (
    TargetCreateResponse,
    TargetUpdateResponse,
    TargetListResponse,
    TargetBulkUpdateResponse,
    TargetGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/infrastructure/targets">client.zero_trust.access.infrastructure.targets.<a href="./src/cloudflare/resources/zero_trust/access/infrastructure/targets.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/infrastructure/target_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/infrastructure/target_create_response.py">Optional[TargetCreateResponse]</a></code>
- <code title="put /accounts/{account_id}/infrastructure/targets/{target_id}">client.zero_trust.access.infrastructure.targets.<a href="./src/cloudflare/resources/zero_trust/access/infrastructure/targets.py">update</a>(target_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/infrastructure/target_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/infrastructure/target_update_response.py">Optional[TargetUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/infrastructure/targets">client.zero_trust.access.infrastructure.targets.<a href="./src/cloudflare/resources/zero_trust/access/infrastructure/targets.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/infrastructure/target_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/infrastructure/target_list_response.py">SyncV4PagePaginationArray[TargetListResponse]</a></code>
- <code title="delete /accounts/{account_id}/infrastructure/targets/{target_id}">client.zero_trust.access.infrastructure.targets.<a href="./src/cloudflare/resources/zero_trust/access/infrastructure/targets.py">delete</a>(target_id, \*, account_id) -> None</code>
- <code title="delete /accounts/{account_id}/infrastructure/targets/batch">client.zero_trust.access.infrastructure.targets.<a href="./src/cloudflare/resources/zero_trust/access/infrastructure/targets.py">bulk_delete</a>(\*, account_id) -> None</code>
- <code title="post /accounts/{account_id}/infrastructure/targets/batch_delete">client.zero_trust.access.infrastructure.targets.<a href="./src/cloudflare/resources/zero_trust/access/infrastructure/targets.py">bulk_delete_v2</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/infrastructure/target_bulk_delete_v2_params.py">params</a>) -> None</code>
- <code title="put /accounts/{account_id}/infrastructure/targets/batch">client.zero_trust.access.infrastructure.targets.<a href="./src/cloudflare/resources/zero_trust/access/infrastructure/targets.py">bulk_update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/infrastructure/target_bulk_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/infrastructure/target_bulk_update_response.py">SyncSinglePage[TargetBulkUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/infrastructure/targets/{target_id}">client.zero_trust.access.infrastructure.targets.<a href="./src/cloudflare/resources/zero_trust/access/infrastructure/targets.py">get</a>(target_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/infrastructure/target_get_response.py">Optional[TargetGetResponse]</a></code>

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
    SaaSAppNameIDFormat,
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
)
```

Methods:

- <code title="post /{accounts_or_zones}/{account_or_zone_id}/access/apps">client.zero_trust.access.applications.<a href="./src/cloudflare/resources/zero_trust/access/applications/applications.py">create</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/application_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/application_create_response.py">Optional[ApplicationCreateResponse]</a></code>
- <code title="put /{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}">client.zero_trust.access.applications.<a href="./src/cloudflare/resources/zero_trust/access/applications/applications.py">update</a>(app_id, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/application_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/application_update_response.py">Optional[ApplicationUpdateResponse]</a></code>
- <code title="get /{accounts_or_zones}/{account_or_zone_id}/access/apps">client.zero_trust.access.applications.<a href="./src/cloudflare/resources/zero_trust/access/applications/applications.py">list</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/application_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/application_list_response.py">SyncV4PagePaginationArray[ApplicationListResponse]</a></code>
- <code title="delete /{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}">client.zero_trust.access.applications.<a href="./src/cloudflare/resources/zero_trust/access/applications/applications.py">delete</a>(app_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/application_delete_response.py">Optional[ApplicationDeleteResponse]</a></code>
- <code title="get /{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}">client.zero_trust.access.applications.<a href="./src/cloudflare/resources/zero_trust/access/applications/applications.py">get</a>(app_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/application_get_response.py">Optional[ApplicationGetResponse]</a></code>
- <code title="post /{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}/revoke_tokens">client.zero_trust.access.applications.<a href="./src/cloudflare/resources/zero_trust/access/applications/applications.py">revoke_tokens</a>(app_id, \*, account_id, zone_id) -> object</code>

#### CAs

Types:

```python
from cloudflare.types.zero_trust.access.applications import CA, CADeleteResponse
```

Methods:

- <code title="post /{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}/ca">client.zero_trust.access.applications.cas.<a href="./src/cloudflare/resources/zero_trust/access/applications/cas.py">create</a>(app_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/applications/ca.py">Optional[CA]</a></code>
- <code title="get /{accounts_or_zones}/{account_or_zone_id}/access/apps/ca">client.zero_trust.access.applications.cas.<a href="./src/cloudflare/resources/zero_trust/access/applications/cas.py">list</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/applications/ca_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/applications/ca.py">SyncV4PagePaginationArray[CA]</a></code>
- <code title="delete /{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}/ca">client.zero_trust.access.applications.cas.<a href="./src/cloudflare/resources/zero_trust/access/applications/cas.py">delete</a>(app_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/applications/ca_delete_response.py">Optional[CADeleteResponse]</a></code>
- <code title="get /{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}/ca">client.zero_trust.access.applications.cas.<a href="./src/cloudflare/resources/zero_trust/access/applications/cas.py">get</a>(app_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/applications/ca.py">Optional[CA]</a></code>

#### UserPolicyChecks

Types:

```python
from cloudflare.types.zero_trust.access.applications import (
    UserPolicyCheckGeo,
    UserPolicyCheckListResponse,
)
```

Methods:

- <code title="get /{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}/user_policy_checks">client.zero_trust.access.applications.user_policy_checks.<a href="./src/cloudflare/resources/zero_trust/access/applications/user_policy_checks.py">list</a>(app_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/applications/user_policy_check_list_response.py">Optional[UserPolicyCheckListResponse]</a></code>

#### Policies

Types:

```python
from cloudflare.types.zero_trust.access.applications import (
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
    PolicyCreateResponse,
    PolicyUpdateResponse,
    PolicyListResponse,
    PolicyDeleteResponse,
    PolicyGetResponse,
)
```

Methods:

- <code title="post /{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}/policies">client.zero_trust.access.applications.policies.<a href="./src/cloudflare/resources/zero_trust/access/applications/policies.py">create</a>(app_id, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/applications/policy_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/applications/policy_create_response.py">Optional[PolicyCreateResponse]</a></code>
- <code title="put /{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}/policies/{policy_id}">client.zero_trust.access.applications.policies.<a href="./src/cloudflare/resources/zero_trust/access/applications/policies.py">update</a>(policy_id, \*, app_id, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/applications/policy_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/applications/policy_update_response.py">Optional[PolicyUpdateResponse]</a></code>
- <code title="get /{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}/policies">client.zero_trust.access.applications.policies.<a href="./src/cloudflare/resources/zero_trust/access/applications/policies.py">list</a>(app_id, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/applications/policy_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/applications/policy_list_response.py">SyncV4PagePaginationArray[PolicyListResponse]</a></code>
- <code title="delete /{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}/policies/{policy_id}">client.zero_trust.access.applications.policies.<a href="./src/cloudflare/resources/zero_trust/access/applications/policies.py">delete</a>(policy_id, \*, app_id, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/applications/policy_delete_response.py">Optional[PolicyDeleteResponse]</a></code>
- <code title="get /{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}/policies/{policy_id}">client.zero_trust.access.applications.policies.<a href="./src/cloudflare/resources/zero_trust/access/applications/policies.py">get</a>(policy_id, \*, app_id, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/applications/policy_get_response.py">Optional[PolicyGetResponse]</a></code>

#### PolicyTests

Types:

```python
from cloudflare.types.zero_trust.access.applications import (
    PolicyTestCreateResponse,
    PolicyTestGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/access/policy-tests">client.zero_trust.access.applications.policy_tests.<a href="./src/cloudflare/resources/zero_trust/access/applications/policy_tests/policy_tests.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/applications/policy_test_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/applications/policy_test_create_response.py">Optional[PolicyTestCreateResponse]</a></code>
- <code title="get /accounts/{account_id}/access/policy-tests/{policy_test_id}">client.zero_trust.access.applications.policy_tests.<a href="./src/cloudflare/resources/zero_trust/access/applications/policy_tests/policy_tests.py">get</a>(policy_test_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/applications/policy_test_get_response.py">Optional[PolicyTestGetResponse]</a></code>

##### Users

Types:

```python
from cloudflare.types.zero_trust.access.applications.policy_tests import UserListResponse
```

Methods:

- <code title="get /accounts/{account_id}/access/policy-tests/{policy_test_id}/users">client.zero_trust.access.applications.policy_tests.users.<a href="./src/cloudflare/resources/zero_trust/access/applications/policy_tests/users.py">list</a>(policy_test_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/applications/policy_tests/user_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/applications/policy_tests/user_list_response.py">SyncV4PagePaginationArray[UserListResponse]</a></code>

#### Settings

Types:

```python
from cloudflare.types.zero_trust.access.applications import (
    SettingUpdateResponse,
    SettingEditResponse,
)
```

Methods:

- <code title="put /{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}/settings">client.zero_trust.access.applications.settings.<a href="./src/cloudflare/resources/zero_trust/access/applications/settings.py">update</a>(app_id, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/applications/setting_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/applications/setting_update_response.py">Optional[SettingUpdateResponse]</a></code>
- <code title="patch /{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}/settings">client.zero_trust.access.applications.settings.<a href="./src/cloudflare/resources/zero_trust/access/applications/settings.py">edit</a>(app_id, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/applications/setting_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/applications/setting_edit_response.py">Optional[SettingEditResponse]</a></code>

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

- <code title="post /{accounts_or_zones}/{account_or_zone_id}/access/certificates">client.zero_trust.access.certificates.<a href="./src/cloudflare/resources/zero_trust/access/certificates/certificates.py">create</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/certificate_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/certificate.py">Optional[Certificate]</a></code>
- <code title="put /{accounts_or_zones}/{account_or_zone_id}/access/certificates/{certificate_id}">client.zero_trust.access.certificates.<a href="./src/cloudflare/resources/zero_trust/access/certificates/certificates.py">update</a>(certificate_id, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/certificate_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/certificate.py">Optional[Certificate]</a></code>
- <code title="get /{accounts_or_zones}/{account_or_zone_id}/access/certificates">client.zero_trust.access.certificates.<a href="./src/cloudflare/resources/zero_trust/access/certificates/certificates.py">list</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/certificate_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/certificate.py">SyncV4PagePaginationArray[Certificate]</a></code>
- <code title="delete /{accounts_or_zones}/{account_or_zone_id}/access/certificates/{certificate_id}">client.zero_trust.access.certificates.<a href="./src/cloudflare/resources/zero_trust/access/certificates/certificates.py">delete</a>(certificate_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/certificate_delete_response.py">Optional[CertificateDeleteResponse]</a></code>
- <code title="get /{accounts_or_zones}/{account_or_zone_id}/access/certificates/{certificate_id}">client.zero_trust.access.certificates.<a href="./src/cloudflare/resources/zero_trust/access/certificates/certificates.py">get</a>(certificate_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/certificate.py">Optional[Certificate]</a></code>

#### Settings

Types:

```python
from cloudflare.types.zero_trust.access.certificates import CertificateSettings
```

Methods:

- <code title="put /{accounts_or_zones}/{account_or_zone_id}/access/certificates/settings">client.zero_trust.access.certificates.settings.<a href="./src/cloudflare/resources/zero_trust/access/certificates/settings.py">update</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/certificates/setting_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/certificates/certificate_settings.py">SyncSinglePage[CertificateSettings]</a></code>
- <code title="get /{accounts_or_zones}/{account_or_zone_id}/access/certificates/settings">client.zero_trust.access.certificates.settings.<a href="./src/cloudflare/resources/zero_trust/access/certificates/settings.py">get</a>(\*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/certificates/certificate_settings.py">SyncSinglePage[CertificateSettings]</a></code>

### Groups

Types:

```python
from cloudflare.types.zero_trust.access import (
    ZeroTrustGroup,
    GroupCreateResponse,
    GroupUpdateResponse,
    GroupListResponse,
    GroupDeleteResponse,
    GroupGetResponse,
)
```

Methods:

- <code title="post /{accounts_or_zones}/{account_or_zone_id}/access/groups">client.zero_trust.access.groups.<a href="./src/cloudflare/resources/zero_trust/access/groups.py">create</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/group_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/group_create_response.py">Optional[GroupCreateResponse]</a></code>
- <code title="put /{accounts_or_zones}/{account_or_zone_id}/access/groups/{group_id}">client.zero_trust.access.groups.<a href="./src/cloudflare/resources/zero_trust/access/groups.py">update</a>(group_id, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/group_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/group_update_response.py">Optional[GroupUpdateResponse]</a></code>
- <code title="get /{accounts_or_zones}/{account_or_zone_id}/access/groups">client.zero_trust.access.groups.<a href="./src/cloudflare/resources/zero_trust/access/groups.py">list</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/group_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/group_list_response.py">SyncV4PagePaginationArray[GroupListResponse]</a></code>
- <code title="delete /{accounts_or_zones}/{account_or_zone_id}/access/groups/{group_id}">client.zero_trust.access.groups.<a href="./src/cloudflare/resources/zero_trust/access/groups.py">delete</a>(group_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/group_delete_response.py">Optional[GroupDeleteResponse]</a></code>
- <code title="get /{accounts_or_zones}/{account_or_zone_id}/access/groups/{group_id}">client.zero_trust.access.groups.<a href="./src/cloudflare/resources/zero_trust/access/groups.py">get</a>(group_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/group_get_response.py">Optional[GroupGetResponse]</a></code>

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

- <code title="post /{accounts_or_zones}/{account_or_zone_id}/access/service_tokens">client.zero_trust.access.service_tokens.<a href="./src/cloudflare/resources/zero_trust/access/service_tokens.py">create</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/service_token_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/service_token_create_response.py">Optional[ServiceTokenCreateResponse]</a></code>
- <code title="put /{accounts_or_zones}/{account_or_zone_id}/access/service_tokens/{service_token_id}">client.zero_trust.access.service_tokens.<a href="./src/cloudflare/resources/zero_trust/access/service_tokens.py">update</a>(service_token_id, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/service_token_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/service_token.py">Optional[ServiceToken]</a></code>
- <code title="get /{accounts_or_zones}/{account_or_zone_id}/access/service_tokens">client.zero_trust.access.service_tokens.<a href="./src/cloudflare/resources/zero_trust/access/service_tokens.py">list</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/zero_trust/access/service_token_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/service_token.py">SyncV4PagePaginationArray[ServiceToken]</a></code>
- <code title="delete /{accounts_or_zones}/{account_or_zone_id}/access/service_tokens/{service_token_id}">client.zero_trust.access.service_tokens.<a href="./src/cloudflare/resources/zero_trust/access/service_tokens.py">delete</a>(service_token_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/service_token.py">Optional[ServiceToken]</a></code>
- <code title="get /{accounts_or_zones}/{account_or_zone_id}/access/service_tokens/{service_token_id}">client.zero_trust.access.service_tokens.<a href="./src/cloudflare/resources/zero_trust/access/service_tokens.py">get</a>(service_token_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/zero_trust/access/service_token.py">Optional[ServiceToken]</a></code>
- <code title="post /accounts/{account_id}/access/service_tokens/{service_token_id}/refresh">client.zero_trust.access.service_tokens.<a href="./src/cloudflare/resources/zero_trust/access/service_tokens.py">refresh</a>(service_token_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/service_token.py">Optional[ServiceToken]</a></code>
- <code title="post /accounts/{account_id}/access/service_tokens/{service_token_id}/rotate">client.zero_trust.access.service_tokens.<a href="./src/cloudflare/resources/zero_trust/access/service_tokens.py">rotate</a>(service_token_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/service_token_rotate_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/service_token_rotate_response.py">Optional[ServiceTokenRotateResponse]</a></code>

### Bookmarks

Types:

```python
from cloudflare.types.zero_trust.access import Bookmark, BookmarkDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/access/bookmarks/{bookmark_id}">client.zero_trust.access.bookmarks.<a href="./src/cloudflare/resources/zero_trust/access/bookmarks.py">create</a>(bookmark_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/bookmark_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/bookmark.py">Optional[Bookmark]</a></code>
- <code title="put /accounts/{account_id}/access/bookmarks/{bookmark_id}">client.zero_trust.access.bookmarks.<a href="./src/cloudflare/resources/zero_trust/access/bookmarks.py">update</a>(bookmark_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/bookmark_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/bookmark.py">Optional[Bookmark]</a></code>
- <code title="get /accounts/{account_id}/access/bookmarks">client.zero_trust.access.bookmarks.<a href="./src/cloudflare/resources/zero_trust/access/bookmarks.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/bookmark.py">SyncSinglePage[Bookmark]</a></code>
- <code title="delete /accounts/{account_id}/access/bookmarks/{bookmark_id}">client.zero_trust.access.bookmarks.<a href="./src/cloudflare/resources/zero_trust/access/bookmarks.py">delete</a>(bookmark_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/bookmark_delete_response.py">Optional[BookmarkDeleteResponse]</a></code>
- <code title="get /accounts/{account_id}/access/bookmarks/{bookmark_id}">client.zero_trust.access.bookmarks.<a href="./src/cloudflare/resources/zero_trust/access/bookmarks.py">get</a>(bookmark_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/bookmark.py">Optional[Bookmark]</a></code>

### Keys

Types:

```python
from cloudflare.types.zero_trust.access import KeyUpdateResponse, KeyGetResponse, KeyRotateResponse
```

Methods:

- <code title="put /accounts/{account_id}/access/keys">client.zero_trust.access.keys.<a href="./src/cloudflare/resources/zero_trust/access/keys.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/key_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/key_update_response.py">Optional[KeyUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/access/keys">client.zero_trust.access.keys.<a href="./src/cloudflare/resources/zero_trust/access/keys.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/key_get_response.py">Optional[KeyGetResponse]</a></code>
- <code title="post /accounts/{account_id}/access/keys/rotate">client.zero_trust.access.keys.<a href="./src/cloudflare/resources/zero_trust/access/keys.py">rotate</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/key_rotate_response.py">Optional[KeyRotateResponse]</a></code>

### Logs

#### AccessRequests

Types:

```python
from cloudflare.types.zero_trust.access.logs import AccessRequestListResponse
```

Methods:

- <code title="get /accounts/{account_id}/access/logs/access_requests">client.zero_trust.access.logs.access_requests.<a href="./src/cloudflare/resources/zero_trust/access/logs/access_requests.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/logs/access_request_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/logs/access_request_list_response.py">Optional[AccessRequestListResponse]</a></code>

#### SCIM

Types:

```python
from cloudflare.types.zero_trust.access.logs import AccessRequest
```

##### Updates

Types:

```python
from cloudflare.types.zero_trust.access.logs.scim import UpdateListResponse
```

Methods:

- <code title="get /accounts/{account_id}/access/logs/scim/updates">client.zero_trust.access.logs.scim.updates.<a href="./src/cloudflare/resources/zero_trust/access/logs/scim/updates.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/logs/scim/update_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/logs/scim/update_list_response.py">SyncV4PagePaginationArray[UpdateListResponse]</a></code>

### Users

Types:

```python
from cloudflare.types.zero_trust.access import (
    AccessUser,
    UserCreateResponse,
    UserUpdateResponse,
    UserListResponse,
    UserGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/access/users">client.zero_trust.access.users.<a href="./src/cloudflare/resources/zero_trust/access/users/users.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/user_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/user_create_response.py">Optional[UserCreateResponse]</a></code>
- <code title="put /accounts/{account_id}/access/users/{user_id}">client.zero_trust.access.users.<a href="./src/cloudflare/resources/zero_trust/access/users/users.py">update</a>(user_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/user_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/user_update_response.py">Optional[UserUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/access/users">client.zero_trust.access.users.<a href="./src/cloudflare/resources/zero_trust/access/users/users.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/user_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/user_list_response.py">SyncV4PagePaginationArray[UserListResponse]</a></code>
- <code title="delete /accounts/{account_id}/access/users/{user_id}">client.zero_trust.access.users.<a href="./src/cloudflare/resources/zero_trust/access/users/users.py">delete</a>(user_id, \*, account_id) -> object</code>
- <code title="get /accounts/{account_id}/access/users/{user_id}">client.zero_trust.access.users.<a href="./src/cloudflare/resources/zero_trust/access/users/users.py">get</a>(user_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/user_get_response.py">Optional[UserGetResponse]</a></code>

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
- <code title="get /accounts/{account_id}/access/users/{user_id}/active_sessions/{nonce}">client.zero_trust.access.users.active_sessions.<a href="./src/cloudflare/resources/zero_trust/access/users/active_sessions.py">get</a>(nonce, \*, account_id, user_id) -> <a href="./src/cloudflare/types/zero_trust/access/users/active_session_get_response.py">Optional[ActiveSessionGetResponse]</a></code>

#### LastSeenIdentity

Types:

```python
from cloudflare.types.zero_trust.access.users import Identity
```

Methods:

- <code title="get /accounts/{account_id}/access/users/{user_id}/last_seen_identity">client.zero_trust.access.users.last_seen_identity.<a href="./src/cloudflare/resources/zero_trust/access/users/last_seen_identity.py">get</a>(user_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/users/identity.py">Optional[Identity]</a></code>

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

- <code title="post /accounts/{account_id}/access/custom_pages">client.zero_trust.access.custom_pages.<a href="./src/cloudflare/resources/zero_trust/access/custom_pages.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/custom_page_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/custom_page_without_html.py">Optional[CustomPageWithoutHTML]</a></code>
- <code title="put /accounts/{account_id}/access/custom_pages/{custom_page_id}">client.zero_trust.access.custom_pages.<a href="./src/cloudflare/resources/zero_trust/access/custom_pages.py">update</a>(custom_page_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/custom_page_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/custom_page_without_html.py">Optional[CustomPageWithoutHTML]</a></code>
- <code title="get /accounts/{account_id}/access/custom_pages">client.zero_trust.access.custom_pages.<a href="./src/cloudflare/resources/zero_trust/access/custom_pages.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/custom_page_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/custom_page_without_html.py">SyncV4PagePaginationArray[CustomPageWithoutHTML]</a></code>
- <code title="delete /accounts/{account_id}/access/custom_pages/{custom_page_id}">client.zero_trust.access.custom_pages.<a href="./src/cloudflare/resources/zero_trust/access/custom_pages.py">delete</a>(custom_page_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/custom_page_delete_response.py">Optional[CustomPageDeleteResponse]</a></code>
- <code title="get /accounts/{account_id}/access/custom_pages/{custom_page_id}">client.zero_trust.access.custom_pages.<a href="./src/cloudflare/resources/zero_trust/access/custom_pages.py">get</a>(custom_page_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/custom_page.py">Optional[CustomPage]</a></code>

### Tags

Types:

```python
from cloudflare.types.zero_trust.access import Tag, TagDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/access/tags">client.zero_trust.access.tags.<a href="./src/cloudflare/resources/zero_trust/access/tags.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/tag_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/tag.py">Optional[Tag]</a></code>
- <code title="put /accounts/{account_id}/access/tags/{tag_name}">client.zero_trust.access.tags.<a href="./src/cloudflare/resources/zero_trust/access/tags.py">update</a>(tag_name, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/tag_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/tag.py">Optional[Tag]</a></code>
- <code title="get /accounts/{account_id}/access/tags">client.zero_trust.access.tags.<a href="./src/cloudflare/resources/zero_trust/access/tags.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/tag_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/tag.py">SyncV4PagePaginationArray[Tag]</a></code>
- <code title="delete /accounts/{account_id}/access/tags/{tag_name}">client.zero_trust.access.tags.<a href="./src/cloudflare/resources/zero_trust/access/tags.py">delete</a>(tag_name, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/tag_delete_response.py">Optional[TagDeleteResponse]</a></code>
- <code title="get /accounts/{account_id}/access/tags/{tag_name}">client.zero_trust.access.tags.<a href="./src/cloudflare/resources/zero_trust/access/tags.py">get</a>(tag_name, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/tag.py">Optional[Tag]</a></code>

### Policies

Types:

```python
from cloudflare.types.zero_trust.access import (
    ApprovalGroup,
    Policy,
    PolicyCreateResponse,
    PolicyUpdateResponse,
    PolicyListResponse,
    PolicyDeleteResponse,
    PolicyGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/access/policies">client.zero_trust.access.policies.<a href="./src/cloudflare/resources/zero_trust/access/policies.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/policy_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/policy_create_response.py">Optional[PolicyCreateResponse]</a></code>
- <code title="put /accounts/{account_id}/access/policies/{policy_id}">client.zero_trust.access.policies.<a href="./src/cloudflare/resources/zero_trust/access/policies.py">update</a>(policy_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/policy_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/policy_update_response.py">Optional[PolicyUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/access/policies">client.zero_trust.access.policies.<a href="./src/cloudflare/resources/zero_trust/access/policies.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/access/policy_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/access/policy_list_response.py">SyncV4PagePaginationArray[PolicyListResponse]</a></code>
- <code title="delete /accounts/{account_id}/access/policies/{policy_id}">client.zero_trust.access.policies.<a href="./src/cloudflare/resources/zero_trust/access/policies.py">delete</a>(policy_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/policy_delete_response.py">Optional[PolicyDeleteResponse]</a></code>
- <code title="get /accounts/{account_id}/access/policies/{policy_id}">client.zero_trust.access.policies.<a href="./src/cloudflare/resources/zero_trust/access/policies.py">get</a>(policy_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/access/policy_get_response.py">Optional[PolicyGetResponse]</a></code>

## DEX

Types:

```python
from cloudflare.types.zero_trust import (
    DigitalExperienceMonitor,
    NetworkPath,
    NetworkPathResponse,
    Percentiles,
)
```

### WARPChangeEvents

Types:

```python
from cloudflare.types.zero_trust.dex import WARPChangeEventGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/dex/warp-change-events">client.zero_trust.dex.warp_change_events.<a href="./src/cloudflare/resources/zero_trust/dex/warp_change_events.py">get</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dex/warp_change_event_get_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dex/warp_change_event_get_response.py">Optional[WARPChangeEventGetResponse]</a></code>

### Commands

Types:

```python
from cloudflare.types.zero_trust.dex import CommandCreateResponse, CommandListResponse
```

Methods:

- <code title="post /accounts/{account_id}/dex/commands">client.zero_trust.dex.commands.<a href="./src/cloudflare/resources/zero_trust/dex/commands/commands.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dex/command_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dex/command_create_response.py">Optional[CommandCreateResponse]</a></code>
- <code title="get /accounts/{account_id}/dex/commands">client.zero_trust.dex.commands.<a href="./src/cloudflare/resources/zero_trust/dex/commands/commands.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dex/command_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dex/command_list_response.py">SyncV4PagePagination[Optional[CommandListResponse]]</a></code>

#### Devices

Types:

```python
from cloudflare.types.zero_trust.dex.commands import DeviceListResponse
```

Methods:

- <code title="get /accounts/{account_id}/dex/commands/devices">client.zero_trust.dex.commands.devices.<a href="./src/cloudflare/resources/zero_trust/dex/commands/devices.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dex/commands/device_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dex/commands/device_list_response.py">SyncV4PagePagination[Optional[DeviceListResponse]]</a></code>

#### Downloads

Methods:

- <code title="get /accounts/{account_id}/dex/commands/{command_id}/downloads/{filename}">client.zero_trust.dex.commands.downloads.<a href="./src/cloudflare/resources/zero_trust/dex/commands/downloads.py">get</a>(filename, \*, account_id, command_id) -> BinaryAPIResponse</code>

#### Quota

Types:

```python
from cloudflare.types.zero_trust.dex.commands import QuotaGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/dex/commands/quota">client.zero_trust.dex.commands.quota.<a href="./src/cloudflare/resources/zero_trust/dex/commands/quota.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dex/commands/quota_get_response.py">Optional[QuotaGetResponse]</a></code>

### Colos

Types:

```python
from cloudflare.types.zero_trust.dex import ColoListResponse
```

Methods:

- <code title="get /accounts/{account_id}/dex/colos">client.zero_trust.dex.colos.<a href="./src/cloudflare/resources/zero_trust/dex/colos.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dex/colo_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dex/colo_list_response.py">SyncSinglePage[ColoListResponse]</a></code>

### FleetStatus

Types:

```python
from cloudflare.types.zero_trust.dex import (
    LiveStat,
    FleetStatusLiveResponse,
    FleetStatusOverTimeResponse,
)
```

Methods:

- <code title="get /accounts/{account_id}/dex/fleet-status/live">client.zero_trust.dex.fleet_status.<a href="./src/cloudflare/resources/zero_trust/dex/fleet_status/fleet_status.py">live</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dex/fleet_status_live_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dex/fleet_status_live_response.py">Optional[FleetStatusLiveResponse]</a></code>
- <code title="get /accounts/{account_id}/dex/fleet-status/over-time">client.zero_trust.dex.fleet_status.<a href="./src/cloudflare/resources/zero_trust/dex/fleet_status/fleet_status.py">over_time</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dex/fleet_status_over_time_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dex/fleet_status_over_time_response.py">Optional[FleetStatusOverTimeResponse]</a></code>

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

- <code title="get /accounts/{account_id}/dex/http-tests/{test_id}">client.zero_trust.dex.http_tests.<a href="./src/cloudflare/resources/zero_trust/dex/http_tests/http_tests.py">get</a>(test_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dex/http_test_get_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dex/http_details.py">Optional[HTTPDetails]</a></code>

#### Percentiles

Types:

```python
from cloudflare.types.zero_trust.dex.http_tests import HTTPDetailsPercentiles, TestStatOverTime
```

Methods:

- <code title="get /accounts/{account_id}/dex/http-tests/{test_id}/percentiles">client.zero_trust.dex.http_tests.percentiles.<a href="./src/cloudflare/resources/zero_trust/dex/http_tests/percentiles.py">get</a>(test_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dex/http_tests/percentile_get_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dex/http_tests/http_details_percentiles.py">Optional[HTTPDetailsPercentiles]</a></code>

### Tests

Types:

```python
from cloudflare.types.zero_trust.dex import AggregateTimePeriod, Tests
```

Methods:

- <code title="get /accounts/{account_id}/dex/tests/overview">client.zero_trust.dex.tests.<a href="./src/cloudflare/resources/zero_trust/dex/tests/tests.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dex/test_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dex/tests/tests.py">SyncV4PagePagination[Optional[Tests]]</a></code>

#### UniqueDevices

Types:

```python
from cloudflare.types.zero_trust.dex.tests import UniqueDevices
```

Methods:

- <code title="get /accounts/{account_id}/dex/tests/unique-devices">client.zero_trust.dex.tests.unique_devices.<a href="./src/cloudflare/resources/zero_trust/dex/tests/unique_devices.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dex/tests/unique_device_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dex/tests/unique_devices.py">Optional[UniqueDevices]</a></code>

### TracerouteTestResults

#### NetworkPath

Types:

```python
from cloudflare.types.zero_trust.dex.traceroute_test_results import NetworkPathGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/dex/traceroute-test-results/{test_result_id}/network-path">client.zero_trust.dex.traceroute_test_results.network_path.<a href="./src/cloudflare/resources/zero_trust/dex/traceroute_test_results/network_path.py">get</a>(test_result_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dex/traceroute_test_results/network_path_get_response.py">Optional[NetworkPathGetResponse]</a></code>

### TracerouteTests

Types:

```python
from cloudflare.types.zero_trust.dex import Traceroute, TracerouteTestPercentilesResponse
```

Methods:

- <code title="get /accounts/{account_id}/dex/traceroute-tests/{test_id}">client.zero_trust.dex.traceroute_tests.<a href="./src/cloudflare/resources/zero_trust/dex/traceroute_tests.py">get</a>(test_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dex/traceroute_test_get_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dex/traceroute.py">Optional[Traceroute]</a></code>
- <code title="get /accounts/{account_id}/dex/traceroute-tests/{test_id}/network-path">client.zero_trust.dex.traceroute_tests.<a href="./src/cloudflare/resources/zero_trust/dex/traceroute_tests.py">network_path</a>(test_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dex/traceroute_test_network_path_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/network_path_response.py">Optional[NetworkPathResponse]</a></code>
- <code title="get /accounts/{account_id}/dex/traceroute-tests/{test_id}/percentiles">client.zero_trust.dex.traceroute_tests.<a href="./src/cloudflare/resources/zero_trust/dex/traceroute_tests.py">percentiles</a>(test_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dex/traceroute_test_percentiles_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dex/traceroute_test_percentiles_response.py">Optional[TracerouteTestPercentilesResponse]</a></code>

### Rules

Types:

```python
from cloudflare.types.zero_trust.dex import (
    RuleCreateResponse,
    RuleUpdateResponse,
    RuleListResponse,
    RuleDeleteResponse,
    RuleGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/dex/rules">client.zero_trust.dex.rules.<a href="./src/cloudflare/resources/zero_trust/dex/rules.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dex/rule_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dex/rule_create_response.py">Optional[RuleCreateResponse]</a></code>
- <code title="patch /accounts/{account_id}/dex/rules/{rule_id}">client.zero_trust.dex.rules.<a href="./src/cloudflare/resources/zero_trust/dex/rules.py">update</a>(rule_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dex/rule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dex/rule_update_response.py">Optional[RuleUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/dex/rules">client.zero_trust.dex.rules.<a href="./src/cloudflare/resources/zero_trust/dex/rules.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dex/rule_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dex/rule_list_response.py">SyncV4PagePagination[Optional[RuleListResponse]]</a></code>
- <code title="delete /accounts/{account_id}/dex/rules/{rule_id}">client.zero_trust.dex.rules.<a href="./src/cloudflare/resources/zero_trust/dex/rules.py">delete</a>(rule_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dex/rule_delete_response.py">Optional[RuleDeleteResponse]</a></code>
- <code title="get /accounts/{account_id}/dex/rules/{rule_id}">client.zero_trust.dex.rules.<a href="./src/cloudflare/resources/zero_trust/dex/rules.py">get</a>(rule_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dex/rule_get_response.py">Optional[RuleGetResponse]</a></code>

## Tunnels

Types:

```python
from cloudflare.types.zero_trust import Connection, TunnelListResponse
```

Methods:

- <code title="get /accounts/{account_id}/tunnels">client.zero_trust.tunnels.<a href="./src/cloudflare/resources/zero_trust/tunnels/tunnels.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/tunnel_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/tunnel_list_response.py">SyncV4PagePaginationArray[TunnelListResponse]</a></code>

### Cloudflared

Methods:

- <code title="post /accounts/{account_id}/cfd_tunnel">client.zero_trust.tunnels.cloudflared.<a href="./src/cloudflare/resources/zero_trust/tunnels/cloudflared/cloudflared.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/tunnels/cloudflared_create_params.py">params</a>) -> <a href="./src/cloudflare/types/shared/cloudflare_tunnel.py">CloudflareTunnel</a></code>
- <code title="get /accounts/{account_id}/cfd_tunnel">client.zero_trust.tunnels.cloudflared.<a href="./src/cloudflare/resources/zero_trust/tunnels/cloudflared/cloudflared.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/tunnels/cloudflared_list_params.py">params</a>) -> <a href="./src/cloudflare/types/shared/cloudflare_tunnel.py">SyncV4PagePaginationArray[CloudflareTunnel]</a></code>
- <code title="delete /accounts/{account_id}/cfd_tunnel/{tunnel_id}">client.zero_trust.tunnels.cloudflared.<a href="./src/cloudflare/resources/zero_trust/tunnels/cloudflared/cloudflared.py">delete</a>(tunnel_id, \*, account_id) -> <a href="./src/cloudflare/types/shared/cloudflare_tunnel.py">CloudflareTunnel</a></code>
- <code title="patch /accounts/{account_id}/cfd_tunnel/{tunnel_id}">client.zero_trust.tunnels.cloudflared.<a href="./src/cloudflare/resources/zero_trust/tunnels/cloudflared/cloudflared.py">edit</a>(tunnel_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/tunnels/cloudflared_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/shared/cloudflare_tunnel.py">CloudflareTunnel</a></code>
- <code title="get /accounts/{account_id}/cfd_tunnel/{tunnel_id}">client.zero_trust.tunnels.cloudflared.<a href="./src/cloudflare/resources/zero_trust/tunnels/cloudflared/cloudflared.py">get</a>(tunnel_id, \*, account_id) -> <a href="./src/cloudflare/types/shared/cloudflare_tunnel.py">CloudflareTunnel</a></code>

#### Configurations

Types:

```python
from cloudflare.types.zero_trust.tunnels.cloudflared import (
    ConfigurationUpdateResponse,
    ConfigurationGetResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/cfd_tunnel/{tunnel_id}/configurations">client.zero_trust.tunnels.cloudflared.configurations.<a href="./src/cloudflare/resources/zero_trust/tunnels/cloudflared/configurations.py">update</a>(tunnel_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/tunnels/cloudflared/configuration_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/tunnels/cloudflared/configuration_update_response.py">Optional[ConfigurationUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/cfd_tunnel/{tunnel_id}/configurations">client.zero_trust.tunnels.cloudflared.configurations.<a href="./src/cloudflare/resources/zero_trust/tunnels/cloudflared/configurations.py">get</a>(tunnel_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/tunnels/cloudflared/configuration_get_response.py">Optional[ConfigurationGetResponse]</a></code>

#### Connections

Types:

```python
from cloudflare.types.zero_trust.tunnels.cloudflared import Client
```

Methods:

- <code title="delete /accounts/{account_id}/cfd_tunnel/{tunnel_id}/connections">client.zero_trust.tunnels.cloudflared.connections.<a href="./src/cloudflare/resources/zero_trust/tunnels/cloudflared/connections.py">delete</a>(tunnel_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/tunnels/cloudflared/connection_delete_params.py">params</a>) -> object</code>
- <code title="get /accounts/{account_id}/cfd_tunnel/{tunnel_id}/connections">client.zero_trust.tunnels.cloudflared.connections.<a href="./src/cloudflare/resources/zero_trust/tunnels/cloudflared/connections.py">get</a>(tunnel_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/tunnels/cloudflared/client.py">SyncSinglePage[Client]</a></code>

#### Token

Types:

```python
from cloudflare.types.zero_trust.tunnels.cloudflared import TokenGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/cfd_tunnel/{tunnel_id}/token">client.zero_trust.tunnels.cloudflared.token.<a href="./src/cloudflare/resources/zero_trust/tunnels/cloudflared/token.py">get</a>(tunnel_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/tunnels/cloudflared/token_get_response.py">str</a></code>

#### Connectors

Methods:

- <code title="get /accounts/{account_id}/cfd_tunnel/{tunnel_id}/connectors/{connector_id}">client.zero_trust.tunnels.cloudflared.connectors.<a href="./src/cloudflare/resources/zero_trust/tunnels/cloudflared/connectors.py">get</a>(connector_id, \*, account_id, tunnel_id) -> <a href="./src/cloudflare/types/zero_trust/tunnels/cloudflared/client.py">Client</a></code>

#### Management

Types:

```python
from cloudflare.types.zero_trust.tunnels.cloudflared import ManagementCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/cfd_tunnel/{tunnel_id}/management">client.zero_trust.tunnels.cloudflared.management.<a href="./src/cloudflare/resources/zero_trust/tunnels/cloudflared/management.py">create</a>(tunnel_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/tunnels/cloudflared/management_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/tunnels/cloudflared/management_create_response.py">str</a></code>

### WARPConnector

Types:

```python
from cloudflare.types.zero_trust.tunnels import (
    WARPConnectorCreateResponse,
    WARPConnectorListResponse,
    WARPConnectorDeleteResponse,
    WARPConnectorEditResponse,
    WARPConnectorGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/warp_connector">client.zero_trust.tunnels.warp_connector.<a href="./src/cloudflare/resources/zero_trust/tunnels/warp_connector/warp_connector.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/tunnels/warp_connector_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/tunnels/warp_connector_create_response.py">WARPConnectorCreateResponse</a></code>
- <code title="get /accounts/{account_id}/warp_connector">client.zero_trust.tunnels.warp_connector.<a href="./src/cloudflare/resources/zero_trust/tunnels/warp_connector/warp_connector.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/tunnels/warp_connector_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/tunnels/warp_connector_list_response.py">SyncV4PagePaginationArray[WARPConnectorListResponse]</a></code>
- <code title="delete /accounts/{account_id}/warp_connector/{tunnel_id}">client.zero_trust.tunnels.warp_connector.<a href="./src/cloudflare/resources/zero_trust/tunnels/warp_connector/warp_connector.py">delete</a>(tunnel_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/tunnels/warp_connector_delete_response.py">WARPConnectorDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/warp_connector/{tunnel_id}">client.zero_trust.tunnels.warp_connector.<a href="./src/cloudflare/resources/zero_trust/tunnels/warp_connector/warp_connector.py">edit</a>(tunnel_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/tunnels/warp_connector_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/tunnels/warp_connector_edit_response.py">WARPConnectorEditResponse</a></code>
- <code title="get /accounts/{account_id}/warp_connector/{tunnel_id}">client.zero_trust.tunnels.warp_connector.<a href="./src/cloudflare/resources/zero_trust/tunnels/warp_connector/warp_connector.py">get</a>(tunnel_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/tunnels/warp_connector_get_response.py">WARPConnectorGetResponse</a></code>

#### Token

Types:

```python
from cloudflare.types.zero_trust.tunnels.warp_connector import TokenGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/warp_connector/{tunnel_id}/token">client.zero_trust.tunnels.warp_connector.token.<a href="./src/cloudflare/resources/zero_trust/tunnels/warp_connector/token.py">get</a>(tunnel_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/tunnels/warp_connector/token_get_response.py">str</a></code>

#### Connections

Types:

```python
from cloudflare.types.zero_trust.tunnels.warp_connector import ConnectionGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/warp_connector/{tunnel_id}/connections">client.zero_trust.tunnels.warp_connector.connections.<a href="./src/cloudflare/resources/zero_trust/tunnels/warp_connector/connections.py">get</a>(tunnel_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/tunnels/warp_connector/connection_get_response.py">SyncSinglePage[ConnectionGetResponse]</a></code>

#### Connectors

Types:

```python
from cloudflare.types.zero_trust.tunnels.warp_connector import ConnectorGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/warp_connector/{tunnel_id}/connectors/{connector_id}">client.zero_trust.tunnels.warp_connector.connectors.<a href="./src/cloudflare/resources/zero_trust/tunnels/warp_connector/connectors.py">get</a>(connector_id, \*, account_id, tunnel_id) -> <a href="./src/cloudflare/types/zero_trust/tunnels/warp_connector/connector_get_response.py">ConnectorGetResponse</a></code>

#### Failover

Methods:

- <code title="put /accounts/{account_id}/warp_connector/{tunnel_id}/failover">client.zero_trust.tunnels.warp_connector.failover.<a href="./src/cloudflare/resources/zero_trust/tunnels/warp_connector/failover.py">update</a>(tunnel_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/tunnels/warp_connector/failover_update_params.py">params</a>) -> object</code>

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

- <code title="post /accounts/{account_id}/dlp/datasets">client.zero_trust.dlp.datasets.<a href="./src/cloudflare/resources/zero_trust/dlp/datasets/datasets.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/dataset_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/dataset_creation.py">Optional[DatasetCreation]</a></code>
- <code title="put /accounts/{account_id}/dlp/datasets/{dataset_id}">client.zero_trust.dlp.datasets.<a href="./src/cloudflare/resources/zero_trust/dlp/datasets/datasets.py">update</a>(dataset_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/dataset_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/dataset.py">Optional[Dataset]</a></code>
- <code title="get /accounts/{account_id}/dlp/datasets">client.zero_trust.dlp.datasets.<a href="./src/cloudflare/resources/zero_trust/dlp/datasets/datasets.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/dataset.py">SyncSinglePage[Dataset]</a></code>
- <code title="delete /accounts/{account_id}/dlp/datasets/{dataset_id}">client.zero_trust.dlp.datasets.<a href="./src/cloudflare/resources/zero_trust/dlp/datasets/datasets.py">delete</a>(dataset_id, \*, account_id) -> None</code>
- <code title="get /accounts/{account_id}/dlp/datasets/{dataset_id}">client.zero_trust.dlp.datasets.<a href="./src/cloudflare/resources/zero_trust/dlp/datasets/datasets.py">get</a>(dataset_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/dataset.py">Optional[Dataset]</a></code>

#### Upload

Types:

```python
from cloudflare.types.zero_trust.dlp.datasets import NewVersion
```

Methods:

- <code title="post /accounts/{account_id}/dlp/datasets/{dataset_id}/upload">client.zero_trust.dlp.datasets.upload.<a href="./src/cloudflare/resources/zero_trust/dlp/datasets/upload.py">create</a>(dataset_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/datasets/new_version.py">Optional[NewVersion]</a></code>
- <code title="post /accounts/{account_id}/dlp/datasets/{dataset_id}/upload/{version}">client.zero_trust.dlp.datasets.upload.<a href="./src/cloudflare/resources/zero_trust/dlp/datasets/upload.py">edit</a>(version, dataset, \*, account_id, dataset_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/datasets/upload_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/dataset.py">Optional[Dataset]</a></code>

#### Versions

Types:

```python
from cloudflare.types.zero_trust.dlp.datasets import VersionCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/dlp/datasets/{dataset_id}/versions/{version}">client.zero_trust.dlp.datasets.versions.<a href="./src/cloudflare/resources/zero_trust/dlp/datasets/versions/versions.py">create</a>(version, \*, account_id, dataset_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/datasets/version_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/datasets/version_create_response.py">SyncSinglePage[VersionCreateResponse]</a></code>

##### Entries

Types:

```python
from cloudflare.types.zero_trust.dlp.datasets.versions import EntryCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/dlp/datasets/{dataset_id}/versions/{version}/entries/{entry_id}">client.zero_trust.dlp.datasets.versions.entries.<a href="./src/cloudflare/resources/zero_trust/dlp/datasets/versions/entries.py">create</a>(entry_id, dataset_version_entry, \*, account_id, dataset_id, version, \*\*<a href="src/cloudflare/types/zero_trust/dlp/datasets/versions/entry_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/datasets/versions/entry_create_response.py">Optional[EntryCreateResponse]</a></code>

### Patterns

Types:

```python
from cloudflare.types.zero_trust.dlp import PatternValidateResponse
```

Methods:

- <code title="post /accounts/{account_id}/dlp/patterns/validate">client.zero_trust.dlp.patterns.<a href="./src/cloudflare/resources/zero_trust/dlp/patterns.py">validate</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/pattern_validate_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/pattern_validate_response.py">Optional[PatternValidateResponse]</a></code>

### PayloadLogs

Types:

```python
from cloudflare.types.zero_trust.dlp import PayloadLogUpdateResponse, PayloadLogGetResponse
```

Methods:

- <code title="put /accounts/{account_id}/dlp/payload_log">client.zero_trust.dlp.payload_logs.<a href="./src/cloudflare/resources/zero_trust/dlp/payload_logs.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/payload_log_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/payload_log_update_response.py">Optional[PayloadLogUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/dlp/payload_log">client.zero_trust.dlp.payload_logs.<a href="./src/cloudflare/resources/zero_trust/dlp/payload_logs.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/payload_log_get_response.py">Optional[PayloadLogGetResponse]</a></code>

### Settings

Types:

```python
from cloudflare.types.zero_trust.dlp import DLPSettings
```

Methods:

- <code title="put /accounts/{account_id}/dlp/settings">client.zero_trust.dlp.settings.<a href="./src/cloudflare/resources/zero_trust/dlp/settings.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/setting_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/dlp_settings.py">Optional[DLPSettings]</a></code>
- <code title="delete /accounts/{account_id}/dlp/settings">client.zero_trust.dlp.settings.<a href="./src/cloudflare/resources/zero_trust/dlp/settings.py">delete</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/dlp_settings.py">Optional[DLPSettings]</a></code>
- <code title="patch /accounts/{account_id}/dlp/settings">client.zero_trust.dlp.settings.<a href="./src/cloudflare/resources/zero_trust/dlp/settings.py">edit</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/setting_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/dlp_settings.py">Optional[DLPSettings]</a></code>
- <code title="get /accounts/{account_id}/dlp/settings">client.zero_trust.dlp.settings.<a href="./src/cloudflare/resources/zero_trust/dlp/settings.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/dlp_settings.py">Optional[DLPSettings]</a></code>

### Email

#### AccountMapping

Types:

```python
from cloudflare.types.zero_trust.dlp.email import (
    AccountMappingCreateResponse,
    AccountMappingGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/dlp/email/account_mapping">client.zero_trust.dlp.email.account_mapping.<a href="./src/cloudflare/resources/zero_trust/dlp/email/account_mapping.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/email/account_mapping_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/email/account_mapping_create_response.py">Optional[AccountMappingCreateResponse]</a></code>
- <code title="get /accounts/{account_id}/dlp/email/account_mapping">client.zero_trust.dlp.email.account_mapping.<a href="./src/cloudflare/resources/zero_trust/dlp/email/account_mapping.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/email/account_mapping_get_response.py">Optional[AccountMappingGetResponse]</a></code>

#### Rules

Types:

```python
from cloudflare.types.zero_trust.dlp.email import (
    RuleCreateResponse,
    RuleUpdateResponse,
    RuleListResponse,
    RuleDeleteResponse,
    RuleBulkEditResponse,
    RuleGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/dlp/email/rules">client.zero_trust.dlp.email.rules.<a href="./src/cloudflare/resources/zero_trust/dlp/email/rules.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/email/rule_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/email/rule_create_response.py">Optional[RuleCreateResponse]</a></code>
- <code title="put /accounts/{account_id}/dlp/email/rules/{rule_id}">client.zero_trust.dlp.email.rules.<a href="./src/cloudflare/resources/zero_trust/dlp/email/rules.py">update</a>(rule_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/email/rule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/email/rule_update_response.py">Optional[RuleUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/dlp/email/rules">client.zero_trust.dlp.email.rules.<a href="./src/cloudflare/resources/zero_trust/dlp/email/rules.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/email/rule_list_response.py">SyncSinglePage[RuleListResponse]</a></code>
- <code title="delete /accounts/{account_id}/dlp/email/rules/{rule_id}">client.zero_trust.dlp.email.rules.<a href="./src/cloudflare/resources/zero_trust/dlp/email/rules.py">delete</a>(rule_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/email/rule_delete_response.py">Optional[RuleDeleteResponse]</a></code>
- <code title="patch /accounts/{account_id}/dlp/email/rules">client.zero_trust.dlp.email.rules.<a href="./src/cloudflare/resources/zero_trust/dlp/email/rules.py">bulk_edit</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/email/rule_bulk_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/email/rule_bulk_edit_response.py">Optional[RuleBulkEditResponse]</a></code>
- <code title="get /accounts/{account_id}/dlp/email/rules/{rule_id}">client.zero_trust.dlp.email.rules.<a href="./src/cloudflare/resources/zero_trust/dlp/email/rules.py">get</a>(rule_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/email/rule_get_response.py">Optional[RuleGetResponse]</a></code>

### Profiles

Types:

```python
from cloudflare.types.zero_trust.dlp import ContextAwareness, Profile, SkipConfiguration
```

Methods:

- <code title="get /accounts/{account_id}/dlp/profiles">client.zero_trust.dlp.profiles.<a href="./src/cloudflare/resources/zero_trust/dlp/profiles/profiles.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/profile_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/profile.py">SyncSinglePage[Profile]</a></code>
- <code title="get /accounts/{account_id}/dlp/profiles/{profile_id}">client.zero_trust.dlp.profiles.<a href="./src/cloudflare/resources/zero_trust/dlp/profiles/profiles.py">get</a>(profile_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/profile.py">Optional[Profile]</a></code>

#### Custom

Types:

```python
from cloudflare.types.zero_trust.dlp.profiles import CustomProfile, Pattern
```

Methods:

- <code title="post /accounts/{account_id}/dlp/profiles/custom">client.zero_trust.dlp.profiles.custom.<a href="./src/cloudflare/resources/zero_trust/dlp/profiles/custom.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/profiles/custom_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/profile.py">Optional[Profile]</a></code>
- <code title="put /accounts/{account_id}/dlp/profiles/custom/{profile_id}">client.zero_trust.dlp.profiles.custom.<a href="./src/cloudflare/resources/zero_trust/dlp/profiles/custom.py">update</a>(profile_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/profiles/custom_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/profile.py">Optional[Profile]</a></code>
- <code title="delete /accounts/{account_id}/dlp/profiles/custom/{profile_id}">client.zero_trust.dlp.profiles.custom.<a href="./src/cloudflare/resources/zero_trust/dlp/profiles/custom.py">delete</a>(profile_id, \*, account_id) -> object</code>
- <code title="get /accounts/{account_id}/dlp/profiles/custom/{profile_id}">client.zero_trust.dlp.profiles.custom.<a href="./src/cloudflare/resources/zero_trust/dlp/profiles/custom.py">get</a>(profile_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/profile.py">Optional[Profile]</a></code>

#### Predefined

Types:

```python
from cloudflare.types.zero_trust.dlp.profiles import PredefinedProfile
```

Methods:

- <code title="put /accounts/{account_id}/dlp/profiles/predefined/{profile_id}/config">client.zero_trust.dlp.profiles.predefined.<a href="./src/cloudflare/resources/zero_trust/dlp/profiles/predefined.py">update</a>(profile_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/profiles/predefined_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/profiles/predefined_profile.py">Optional[PredefinedProfile]</a></code>
- <code title="delete /accounts/{account_id}/dlp/profiles/predefined/{profile_id}">client.zero_trust.dlp.profiles.predefined.<a href="./src/cloudflare/resources/zero_trust/dlp/profiles/predefined.py">delete</a>(profile_id, \*, account_id) -> object</code>
- <code title="get /accounts/{account_id}/dlp/profiles/predefined/{profile_id}/config">client.zero_trust.dlp.profiles.predefined.<a href="./src/cloudflare/resources/zero_trust/dlp/profiles/predefined.py">get</a>(profile_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/profiles/predefined_profile.py">Optional[PredefinedProfile]</a></code>

### Limits

Types:

```python
from cloudflare.types.zero_trust.dlp import LimitListResponse
```

Methods:

- <code title="get /accounts/{account_id}/dlp/limits">client.zero_trust.dlp.limits.<a href="./src/cloudflare/resources/zero_trust/dlp/limits.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/limit_list_response.py">Optional[LimitListResponse]</a></code>

### Entries

Types:

```python
from cloudflare.types.zero_trust.dlp import (
    EntryCreateResponse,
    EntryUpdateResponse,
    EntryListResponse,
    EntryGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/dlp/entries">client.zero_trust.dlp.entries.<a href="./src/cloudflare/resources/zero_trust/dlp/entries/entries.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/entry_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/entry_create_response.py">Optional[EntryCreateResponse]</a></code>
- <code title="put /accounts/{account_id}/dlp/entries/{entry_id}">client.zero_trust.dlp.entries.<a href="./src/cloudflare/resources/zero_trust/dlp/entries/entries.py">update</a>(entry_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/entry_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/entry_update_response.py">Optional[EntryUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/dlp/entries">client.zero_trust.dlp.entries.<a href="./src/cloudflare/resources/zero_trust/dlp/entries/entries.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/entry_list_response.py">SyncSinglePage[EntryListResponse]</a></code>
- <code title="delete /accounts/{account_id}/dlp/entries/{entry_id}">client.zero_trust.dlp.entries.<a href="./src/cloudflare/resources/zero_trust/dlp/entries/entries.py">delete</a>(entry_id, \*, account_id) -> object</code>
- <code title="get /accounts/{account_id}/dlp/entries/{entry_id}">client.zero_trust.dlp.entries.<a href="./src/cloudflare/resources/zero_trust/dlp/entries/entries.py">get</a>(entry_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/entry_get_response.py">Optional[EntryGetResponse]</a></code>

#### Custom

Types:

```python
from cloudflare.types.zero_trust.dlp.entries import (
    CustomCreateResponse,
    CustomUpdateResponse,
    CustomListResponse,
    CustomGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/dlp/entries">client.zero_trust.dlp.entries.custom.<a href="./src/cloudflare/resources/zero_trust/dlp/entries/custom.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/entries/custom_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/entries/custom_create_response.py">Optional[CustomCreateResponse]</a></code>
- <code title="put /accounts/{account_id}/dlp/entries/custom/{entry_id}">client.zero_trust.dlp.entries.custom.<a href="./src/cloudflare/resources/zero_trust/dlp/entries/custom.py">update</a>(entry_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/entries/custom_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/entries/custom_update_response.py">Optional[CustomUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/dlp/entries">client.zero_trust.dlp.entries.custom.<a href="./src/cloudflare/resources/zero_trust/dlp/entries/custom.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/entries/custom_list_response.py">SyncSinglePage[CustomListResponse]</a></code>
- <code title="delete /accounts/{account_id}/dlp/entries/{entry_id}">client.zero_trust.dlp.entries.custom.<a href="./src/cloudflare/resources/zero_trust/dlp/entries/custom.py">delete</a>(entry_id, \*, account_id) -> object</code>
- <code title="get /accounts/{account_id}/dlp/entries/{entry_id}">client.zero_trust.dlp.entries.custom.<a href="./src/cloudflare/resources/zero_trust/dlp/entries/custom.py">get</a>(entry_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/entries/custom_get_response.py">Optional[CustomGetResponse]</a></code>

#### Predefined

Types:

```python
from cloudflare.types.zero_trust.dlp.entries import (
    PredefinedCreateResponse,
    PredefinedUpdateResponse,
    PredefinedListResponse,
    PredefinedGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/dlp/entries/predefined">client.zero_trust.dlp.entries.predefined.<a href="./src/cloudflare/resources/zero_trust/dlp/entries/predefined.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/entries/predefined_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/entries/predefined_create_response.py">Optional[PredefinedCreateResponse]</a></code>
- <code title="put /accounts/{account_id}/dlp/entries/predefined/{entry_id}">client.zero_trust.dlp.entries.predefined.<a href="./src/cloudflare/resources/zero_trust/dlp/entries/predefined.py">update</a>(entry_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/entries/predefined_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/entries/predefined_update_response.py">Optional[PredefinedUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/dlp/entries">client.zero_trust.dlp.entries.predefined.<a href="./src/cloudflare/resources/zero_trust/dlp/entries/predefined.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/entries/predefined_list_response.py">SyncSinglePage[PredefinedListResponse]</a></code>
- <code title="delete /accounts/{account_id}/dlp/entries/predefined/{entry_id}">client.zero_trust.dlp.entries.predefined.<a href="./src/cloudflare/resources/zero_trust/dlp/entries/predefined.py">delete</a>(entry_id, \*, account_id) -> object</code>
- <code title="get /accounts/{account_id}/dlp/entries/{entry_id}">client.zero_trust.dlp.entries.predefined.<a href="./src/cloudflare/resources/zero_trust/dlp/entries/predefined.py">get</a>(entry_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/entries/predefined_get_response.py">Optional[PredefinedGetResponse]</a></code>

#### Integration

Types:

```python
from cloudflare.types.zero_trust.dlp.entries import (
    IntegrationCreateResponse,
    IntegrationUpdateResponse,
    IntegrationListResponse,
    IntegrationGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/dlp/entries/integration">client.zero_trust.dlp.entries.integration.<a href="./src/cloudflare/resources/zero_trust/dlp/entries/integration.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/entries/integration_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/entries/integration_create_response.py">Optional[IntegrationCreateResponse]</a></code>
- <code title="put /accounts/{account_id}/dlp/entries/integration/{entry_id}">client.zero_trust.dlp.entries.integration.<a href="./src/cloudflare/resources/zero_trust/dlp/entries/integration.py">update</a>(entry_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/dlp/entries/integration_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/dlp/entries/integration_update_response.py">Optional[IntegrationUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/dlp/entries">client.zero_trust.dlp.entries.integration.<a href="./src/cloudflare/resources/zero_trust/dlp/entries/integration.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/entries/integration_list_response.py">SyncSinglePage[IntegrationListResponse]</a></code>
- <code title="delete /accounts/{account_id}/dlp/entries/integration/{entry_id}">client.zero_trust.dlp.entries.integration.<a href="./src/cloudflare/resources/zero_trust/dlp/entries/integration.py">delete</a>(entry_id, \*, account_id) -> object</code>
- <code title="get /accounts/{account_id}/dlp/entries/{entry_id}">client.zero_trust.dlp.entries.integration.<a href="./src/cloudflare/resources/zero_trust/dlp/entries/integration.py">get</a>(entry_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/dlp/entries/integration_get_response.py">Optional[IntegrationGetResponse]</a></code>

## Gateway

Types:

```python
from cloudflare.types.zero_trust import GatewayCreateResponse, GatewayListResponse
```

Methods:

- <code title="post /accounts/{account_id}/gateway">client.zero_trust.gateway.<a href="./src/cloudflare/resources/zero_trust/gateway/gateway.py">create</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway_create_response.py">Optional[GatewayCreateResponse]</a></code>
- <code title="get /accounts/{account_id}/gateway">client.zero_trust.gateway.<a href="./src/cloudflare/resources/zero_trust/gateway/gateway.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway_list_response.py">Optional[GatewayListResponse]</a></code>

### AuditSSHSettings

Types:

```python
from cloudflare.types.zero_trust.gateway import GatewaySettings
```

Methods:

- <code title="put /accounts/{account_id}/gateway/audit_ssh_settings">client.zero_trust.gateway.audit_ssh_settings.<a href="./src/cloudflare/resources/zero_trust/gateway/audit_ssh_settings.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/audit_ssh_setting_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/gateway_settings.py">Optional[GatewaySettings]</a></code>
- <code title="get /accounts/{account_id}/gateway/audit_ssh_settings">client.zero_trust.gateway.audit_ssh_settings.<a href="./src/cloudflare/resources/zero_trust/gateway/audit_ssh_settings.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/gateway_settings.py">Optional[GatewaySettings]</a></code>
- <code title="post /accounts/{account_id}/gateway/audit_ssh_settings/rotate_seed">client.zero_trust.gateway.audit_ssh_settings.<a href="./src/cloudflare/resources/zero_trust/gateway/audit_ssh_settings.py">rotate_seed</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/gateway_settings.py">Optional[GatewaySettings]</a></code>

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

- <code title="put /accounts/{account_id}/gateway/configuration">client.zero_trust.gateway.configurations.<a href="./src/cloudflare/resources/zero_trust/gateway/configurations/configurations.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/configuration_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/configuration_update_response.py">Optional[ConfigurationUpdateResponse]</a></code>
- <code title="patch /accounts/{account_id}/gateway/configuration">client.zero_trust.gateway.configurations.<a href="./src/cloudflare/resources/zero_trust/gateway/configurations/configurations.py">edit</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/configuration_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/configuration_edit_response.py">Optional[ConfigurationEditResponse]</a></code>
- <code title="get /accounts/{account_id}/gateway/configuration">client.zero_trust.gateway.configurations.<a href="./src/cloudflare/resources/zero_trust/gateway/configurations/configurations.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/configuration_get_response.py">Optional[ConfigurationGetResponse]</a></code>

#### CustomCertificate

Methods:

- <code title="get /accounts/{account_id}/gateway/configuration/custom_certificate">client.zero_trust.gateway.configurations.custom_certificate.<a href="./src/cloudflare/resources/zero_trust/gateway/configurations/custom_certificate.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/custom_certificate_settings.py">Optional[CustomCertificateSettings]</a></code>

### Lists

Types:

```python
from cloudflare.types.zero_trust.gateway import GatewayItem, GatewayList, ListCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/gateway/lists">client.zero_trust.gateway.lists.<a href="./src/cloudflare/resources/zero_trust/gateway/lists/lists.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/list_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/list_create_response.py">Optional[ListCreateResponse]</a></code>
- <code title="put /accounts/{account_id}/gateway/lists/{list_id}">client.zero_trust.gateway.lists.<a href="./src/cloudflare/resources/zero_trust/gateway/lists/lists.py">update</a>(list_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/list_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/gateway_list.py">Optional[GatewayList]</a></code>
- <code title="get /accounts/{account_id}/gateway/lists">client.zero_trust.gateway.lists.<a href="./src/cloudflare/resources/zero_trust/gateway/lists/lists.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/list_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/gateway_list.py">SyncSinglePage[GatewayList]</a></code>
- <code title="delete /accounts/{account_id}/gateway/lists/{list_id}">client.zero_trust.gateway.lists.<a href="./src/cloudflare/resources/zero_trust/gateway/lists/lists.py">delete</a>(list_id, \*, account_id) -> object</code>
- <code title="patch /accounts/{account_id}/gateway/lists/{list_id}">client.zero_trust.gateway.lists.<a href="./src/cloudflare/resources/zero_trust/gateway/lists/lists.py">edit</a>(list_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/list_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/gateway_list.py">Optional[GatewayList]</a></code>
- <code title="get /accounts/{account_id}/gateway/lists/{list_id}">client.zero_trust.gateway.lists.<a href="./src/cloudflare/resources/zero_trust/gateway/lists/lists.py">get</a>(list_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/gateway_list.py">Optional[GatewayList]</a></code>

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
)
```

Methods:

- <code title="post /accounts/{account_id}/gateway/locations">client.zero_trust.gateway.locations.<a href="./src/cloudflare/resources/zero_trust/gateway/locations.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/location_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/location.py">Optional[Location]</a></code>
- <code title="put /accounts/{account_id}/gateway/locations/{location_id}">client.zero_trust.gateway.locations.<a href="./src/cloudflare/resources/zero_trust/gateway/locations.py">update</a>(location_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/location_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/location.py">Optional[Location]</a></code>
- <code title="get /accounts/{account_id}/gateway/locations">client.zero_trust.gateway.locations.<a href="./src/cloudflare/resources/zero_trust/gateway/locations.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/location.py">SyncSinglePage[Location]</a></code>
- <code title="delete /accounts/{account_id}/gateway/locations/{location_id}">client.zero_trust.gateway.locations.<a href="./src/cloudflare/resources/zero_trust/gateway/locations.py">delete</a>(location_id, \*, account_id) -> object</code>
- <code title="get /accounts/{account_id}/gateway/locations/{location_id}">client.zero_trust.gateway.locations.<a href="./src/cloudflare/resources/zero_trust/gateway/locations.py">get</a>(location_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/location.py">Optional[Location]</a></code>

### Logging

Types:

```python
from cloudflare.types.zero_trust.gateway import LoggingSetting
```

Methods:

- <code title="put /accounts/{account_id}/gateway/logging">client.zero_trust.gateway.logging.<a href="./src/cloudflare/resources/zero_trust/gateway/logging.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/logging_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/logging_setting.py">Optional[LoggingSetting]</a></code>
- <code title="get /accounts/{account_id}/gateway/logging">client.zero_trust.gateway.logging.<a href="./src/cloudflare/resources/zero_trust/gateway/logging.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/logging_setting.py">Optional[LoggingSetting]</a></code>

### ProxyEndpoints

Types:

```python
from cloudflare.types.zero_trust.gateway import GatewayIPs, ProxyEndpoint
```

Methods:

- <code title="post /accounts/{account_id}/gateway/proxy_endpoints">client.zero_trust.gateway.proxy_endpoints.<a href="./src/cloudflare/resources/zero_trust/gateway/proxy_endpoints.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/proxy_endpoint_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/proxy_endpoint.py">Optional[ProxyEndpoint]</a></code>
- <code title="get /accounts/{account_id}/gateway/proxy_endpoints">client.zero_trust.gateway.proxy_endpoints.<a href="./src/cloudflare/resources/zero_trust/gateway/proxy_endpoints.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/proxy_endpoint.py">SyncSinglePage[ProxyEndpoint]</a></code>
- <code title="delete /accounts/{account_id}/gateway/proxy_endpoints/{proxy_endpoint_id}">client.zero_trust.gateway.proxy_endpoints.<a href="./src/cloudflare/resources/zero_trust/gateway/proxy_endpoints.py">delete</a>(proxy_endpoint_id, \*, account_id) -> object</code>
- <code title="patch /accounts/{account_id}/gateway/proxy_endpoints/{proxy_endpoint_id}">client.zero_trust.gateway.proxy_endpoints.<a href="./src/cloudflare/resources/zero_trust/gateway/proxy_endpoints.py">edit</a>(proxy_endpoint_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/proxy_endpoint_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/proxy_endpoint.py">Optional[ProxyEndpoint]</a></code>
- <code title="get /accounts/{account_id}/gateway/proxy_endpoints/{proxy_endpoint_id}">client.zero_trust.gateway.proxy_endpoints.<a href="./src/cloudflare/resources/zero_trust/gateway/proxy_endpoints.py">get</a>(proxy_endpoint_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/proxy_endpoint.py">Optional[ProxyEndpoint]</a></code>

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
)
```

Methods:

- <code title="post /accounts/{account_id}/gateway/rules">client.zero_trust.gateway.rules.<a href="./src/cloudflare/resources/zero_trust/gateway/rules.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/rule_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/gateway_rule.py">Optional[GatewayRule]</a></code>
- <code title="put /accounts/{account_id}/gateway/rules/{rule_id}">client.zero_trust.gateway.rules.<a href="./src/cloudflare/resources/zero_trust/gateway/rules.py">update</a>(rule_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/rule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/gateway_rule.py">Optional[GatewayRule]</a></code>
- <code title="get /accounts/{account_id}/gateway/rules">client.zero_trust.gateway.rules.<a href="./src/cloudflare/resources/zero_trust/gateway/rules.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/gateway_rule.py">SyncSinglePage[GatewayRule]</a></code>
- <code title="delete /accounts/{account_id}/gateway/rules/{rule_id}">client.zero_trust.gateway.rules.<a href="./src/cloudflare/resources/zero_trust/gateway/rules.py">delete</a>(rule_id, \*, account_id) -> object</code>
- <code title="get /accounts/{account_id}/gateway/rules/{rule_id}">client.zero_trust.gateway.rules.<a href="./src/cloudflare/resources/zero_trust/gateway/rules.py">get</a>(rule_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/gateway_rule.py">Optional[GatewayRule]</a></code>
- <code title="get /accounts/{account_id}/gateway/rules/tenant">client.zero_trust.gateway.rules.<a href="./src/cloudflare/resources/zero_trust/gateway/rules.py">list_tenant</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/gateway_rule.py">SyncSinglePage[GatewayRule]</a></code>
- <code title="post /accounts/{account_id}/gateway/rules/{rule_id}/reset_expiration">client.zero_trust.gateway.rules.<a href="./src/cloudflare/resources/zero_trust/gateway/rules.py">reset_expiration</a>(rule_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/gateway_rule.py">Optional[GatewayRule]</a></code>

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

- <code title="post /accounts/{account_id}/gateway/certificates">client.zero_trust.gateway.certificates.<a href="./src/cloudflare/resources/zero_trust/gateway/certificates.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/certificate_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/certificate_create_response.py">Optional[CertificateCreateResponse]</a></code>
- <code title="get /accounts/{account_id}/gateway/certificates">client.zero_trust.gateway.certificates.<a href="./src/cloudflare/resources/zero_trust/gateway/certificates.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/certificate_list_response.py">SyncSinglePage[CertificateListResponse]</a></code>
- <code title="delete /accounts/{account_id}/gateway/certificates/{certificate_id}">client.zero_trust.gateway.certificates.<a href="./src/cloudflare/resources/zero_trust/gateway/certificates.py">delete</a>(certificate_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/certificate_delete_response.py">Optional[CertificateDeleteResponse]</a></code>
- <code title="post /accounts/{account_id}/gateway/certificates/{certificate_id}/activate">client.zero_trust.gateway.certificates.<a href="./src/cloudflare/resources/zero_trust/gateway/certificates.py">activate</a>(certificate_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/certificate_activate_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/certificate_activate_response.py">Optional[CertificateActivateResponse]</a></code>
- <code title="post /accounts/{account_id}/gateway/certificates/{certificate_id}/deactivate">client.zero_trust.gateway.certificates.<a href="./src/cloudflare/resources/zero_trust/gateway/certificates.py">deactivate</a>(certificate_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/certificate_deactivate_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/certificate_deactivate_response.py">Optional[CertificateDeactivateResponse]</a></code>
- <code title="get /accounts/{account_id}/gateway/certificates/{certificate_id}">client.zero_trust.gateway.certificates.<a href="./src/cloudflare/resources/zero_trust/gateway/certificates.py">get</a>(certificate_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/certificate_get_response.py">Optional[CertificateGetResponse]</a></code>

### Pacfiles

Types:

```python
from cloudflare.types.zero_trust.gateway import (
    PacfileCreateResponse,
    PacfileUpdateResponse,
    PacfileListResponse,
    PacfileGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/gateway/pacfiles">client.zero_trust.gateway.pacfiles.<a href="./src/cloudflare/resources/zero_trust/gateway/pacfiles.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/pacfile_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/pacfile_create_response.py">Optional[PacfileCreateResponse]</a></code>
- <code title="put /accounts/{account_id}/gateway/pacfiles/{pacfile_id}">client.zero_trust.gateway.pacfiles.<a href="./src/cloudflare/resources/zero_trust/gateway/pacfiles.py">update</a>(pacfile_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/gateway/pacfile_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/gateway/pacfile_update_response.py">Optional[PacfileUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/gateway/pacfiles">client.zero_trust.gateway.pacfiles.<a href="./src/cloudflare/resources/zero_trust/gateway/pacfiles.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/pacfile_list_response.py">SyncSinglePage[PacfileListResponse]</a></code>
- <code title="delete /accounts/{account_id}/gateway/pacfiles/{pacfile_id}">client.zero_trust.gateway.pacfiles.<a href="./src/cloudflare/resources/zero_trust/gateway/pacfiles.py">delete</a>(pacfile_id, \*, account_id) -> object</code>
- <code title="get /accounts/{account_id}/gateway/pacfiles/{pacfile_id}">client.zero_trust.gateway.pacfiles.<a href="./src/cloudflare/resources/zero_trust/gateway/pacfiles.py">get</a>(pacfile_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/gateway/pacfile_get_response.py">Optional[PacfileGetResponse]</a></code>

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

### Subnets

Methods:

- <code title="get /accounts/{account_id}/zerotrust/subnets">client.zero_trust.networks.subnets.<a href="./src/cloudflare/resources/zero_trust/networks/subnets/subnets.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/networks/subnet_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/networks/subnets/subnet.py">SyncV4PagePaginationArray[Subnet]</a></code>

#### WARP

Types:

```python
from cloudflare.types.zero_trust.networks.subnets import Subnet, WARPDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/zerotrust/subnets/warp">client.zero_trust.networks.subnets.warp.<a href="./src/cloudflare/resources/zero_trust/networks/subnets/warp.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/networks/subnets/warp_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/networks/subnets/subnet.py">Subnet</a></code>
- <code title="delete /accounts/{account_id}/zerotrust/subnets/warp/{subnet_id}">client.zero_trust.networks.subnets.warp.<a href="./src/cloudflare/resources/zero_trust/networks/subnets/warp.py">delete</a>(subnet_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/networks/subnets/warp_delete_response.py">Optional[WARPDeleteResponse]</a></code>
- <code title="patch /accounts/{account_id}/zerotrust/subnets/warp/{subnet_id}">client.zero_trust.networks.subnets.warp.<a href="./src/cloudflare/resources/zero_trust/networks/subnets/warp.py">edit</a>(subnet_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/networks/subnets/warp_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/networks/subnets/subnet.py">Subnet</a></code>
- <code title="get /accounts/{account_id}/zerotrust/subnets/warp/{subnet_id}">client.zero_trust.networks.subnets.warp.<a href="./src/cloudflare/resources/zero_trust/networks/subnets/warp.py">get</a>(subnet_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/networks/subnets/subnet.py">Subnet</a></code>

#### CloudflareSource

Methods:

- <code title="patch /accounts/{account_id}/zerotrust/subnets/cloudflare_source/{address_family}">client.zero_trust.networks.subnets.cloudflare_source.<a href="./src/cloudflare/resources/zero_trust/networks/subnets/cloudflare_source.py">update</a>(address_family, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/networks/subnets/cloudflare_source_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/networks/subnets/subnet.py">Subnet</a></code>

### HostnameRoutes

Types:

```python
from cloudflare.types.zero_trust.networks import HostnameRoute
```

Methods:

- <code title="post /accounts/{account_id}/zerotrust/routes/hostname">client.zero_trust.networks.hostname_routes.<a href="./src/cloudflare/resources/zero_trust/networks/hostname_routes.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/networks/hostname_route_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/networks/hostname_route.py">HostnameRoute</a></code>
- <code title="get /accounts/{account_id}/zerotrust/routes/hostname">client.zero_trust.networks.hostname_routes.<a href="./src/cloudflare/resources/zero_trust/networks/hostname_routes.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/networks/hostname_route_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/networks/hostname_route.py">SyncV4PagePaginationArray[HostnameRoute]</a></code>
- <code title="delete /accounts/{account_id}/zerotrust/routes/hostname/{hostname_route_id}">client.zero_trust.networks.hostname_routes.<a href="./src/cloudflare/resources/zero_trust/networks/hostname_routes.py">delete</a>(hostname_route_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/networks/hostname_route.py">HostnameRoute</a></code>
- <code title="patch /accounts/{account_id}/zerotrust/routes/hostname/{hostname_route_id}">client.zero_trust.networks.hostname_routes.<a href="./src/cloudflare/resources/zero_trust/networks/hostname_routes.py">edit</a>(hostname_route_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/networks/hostname_route_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/networks/hostname_route.py">HostnameRoute</a></code>
- <code title="get /accounts/{account_id}/zerotrust/routes/hostname/{hostname_route_id}">client.zero_trust.networks.hostname_routes.<a href="./src/cloudflare/resources/zero_trust/networks/hostname_routes.py">get</a>(hostname_route_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/networks/hostname_route.py">HostnameRoute</a></code>

## RiskScoring

Types:

```python
from cloudflare.types.zero_trust import RiskScoringGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/zt_risk_scoring/{user_id}">client.zero_trust.risk_scoring.<a href="./src/cloudflare/resources/zero_trust/risk_scoring/risk_scoring.py">get</a>(user_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/risk_scoring_get_response.py">Optional[RiskScoringGetResponse]</a></code>
- <code title="post /accounts/{account_id}/zt_risk_scoring/{user_id}/reset">client.zero_trust.risk_scoring.<a href="./src/cloudflare/resources/zero_trust/risk_scoring/risk_scoring.py">reset</a>(user_id, \*, account_id) -> object</code>

### Behaviours

Types:

```python
from cloudflare.types.zero_trust.risk_scoring import BehaviourUpdateResponse, BehaviourGetResponse
```

Methods:

- <code title="put /accounts/{account_id}/zt_risk_scoring/behaviors">client.zero_trust.risk_scoring.behaviours.<a href="./src/cloudflare/resources/zero_trust/risk_scoring/behaviours.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/risk_scoring/behaviour_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/risk_scoring/behaviour_update_response.py">Optional[BehaviourUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/zt_risk_scoring/behaviors">client.zero_trust.risk_scoring.behaviours.<a href="./src/cloudflare/resources/zero_trust/risk_scoring/behaviours.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/risk_scoring/behaviour_get_response.py">Optional[BehaviourGetResponse]</a></code>

### Summary

Types:

```python
from cloudflare.types.zero_trust.risk_scoring import SummaryGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/zt_risk_scoring/summary">client.zero_trust.risk_scoring.summary.<a href="./src/cloudflare/resources/zero_trust/risk_scoring/summary.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/risk_scoring/summary_get_response.py">Optional[SummaryGetResponse]</a></code>

### Integrations

Types:

```python
from cloudflare.types.zero_trust.risk_scoring import (
    IntegrationCreateResponse,
    IntegrationUpdateResponse,
    IntegrationListResponse,
    IntegrationGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/zt_risk_scoring/integrations">client.zero_trust.risk_scoring.integrations.<a href="./src/cloudflare/resources/zero_trust/risk_scoring/integrations/integrations.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/risk_scoring/integration_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/risk_scoring/integration_create_response.py">Optional[IntegrationCreateResponse]</a></code>
- <code title="put /accounts/{account_id}/zt_risk_scoring/integrations/{integration_id}">client.zero_trust.risk_scoring.integrations.<a href="./src/cloudflare/resources/zero_trust/risk_scoring/integrations/integrations.py">update</a>(integration_id, \*, account_id, \*\*<a href="src/cloudflare/types/zero_trust/risk_scoring/integration_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zero_trust/risk_scoring/integration_update_response.py">Optional[IntegrationUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/zt_risk_scoring/integrations">client.zero_trust.risk_scoring.integrations.<a href="./src/cloudflare/resources/zero_trust/risk_scoring/integrations/integrations.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/zero_trust/risk_scoring/integration_list_response.py">SyncSinglePage[IntegrationListResponse]</a></code>
- <code title="delete /accounts/{account_id}/zt_risk_scoring/integrations/{integration_id}">client.zero_trust.risk_scoring.integrations.<a href="./src/cloudflare/resources/zero_trust/risk_scoring/integrations/integrations.py">delete</a>(integration_id, \*, account_id) -> object</code>
- <code title="get /accounts/{account_id}/zt_risk_scoring/integrations/{integration_id}">client.zero_trust.risk_scoring.integrations.<a href="./src/cloudflare/resources/zero_trust/risk_scoring/integrations/integrations.py">get</a>(integration_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/risk_scoring/integration_get_response.py">Optional[IntegrationGetResponse]</a></code>

#### References

Types:

```python
from cloudflare.types.zero_trust.risk_scoring.integrations import ReferenceGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/zt_risk_scoring/integrations/reference_id/{reference_id}">client.zero_trust.risk_scoring.integrations.references.<a href="./src/cloudflare/resources/zero_trust/risk_scoring/integrations/references.py">get</a>(reference_id, \*, account_id) -> <a href="./src/cloudflare/types/zero_trust/risk_scoring/integrations/reference_get_response.py">Optional[ReferenceGetResponse]</a></code>
