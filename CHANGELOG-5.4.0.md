## 5.4.0 (2026-06-16)

Full Changelog: [v5.3.0...v5.4.0](https://github.com/cloudflare/cloudflare-python/compare/v5.3.0...v5.4.0)

### Features

* **ai_gateway:** add `custom_providers` sub-resource ([b982ff3](https://github.com/cloudflare/cloudflare-python/commit/b982ff391eab267ef16c719d0fc798d970292ed2))
* **ct_alerter:** add CT alerting subscription endpoints (`client.zones.ct.alerting`) ([5bb529c](https://github.com/cloudflare/cloudflare-python/commit/5bb529c2eabe4ce0c23cddbf8073c6a025dc3024))
* **d1:** add `fields` parameter to `client.d1.database.get` ([2b0e738](https://github.com/cloudflare/cloudflare-python/commit/2b0e7388107c4110489484c2b38d4d9295b15af2))
* **flagship:** add `flagship` resource with apps, flags, changelog, and evaluate endpoints ([2b0e738](https://github.com/cloudflare/cloudflare-python/commit/2b0e7388107c4110489484c2b38d4d9295b15af2))
* **magic_transit:** add `cf1_sites` sub-resource with ramps, and `ipsec_tunnels.psk_set` method ([5d8e422](https://github.com/cloudflare/cloudflare-python/commit/5d8e422736d8e044d2c73065cbb8595573b2656d))
* **origin_tls_compliance_modes:** add `origin_tls_compliance_modes` resource ([2b0e738](https://github.com/cloudflare/cloudflare-python/commit/2b0e7388107c4110489484c2b38d4d9295b15af2))
* **ssl:** add `auto_origin_tls_kex` sub-resource ([2b0e738](https://github.com/cloudflare/cloudflare-python/commit/2b0e7388107c4110489484c2b38d4d9295b15af2))
* **tenants:** add `tenants` top-level resource and `user.tenants` sub-resource ([7677b4c](https://github.com/cloudflare/cloudflare-python/commit/7677b4c9566495b627b2cd90c9220268f9c6c46d))
* **zero_trust:** add DLP `sensitivity_groups`, `data_tag_categories`, and `data_classes` sub-resources ([2b0e738](https://github.com/cloudflare/cloudflare-python/commit/2b0e7388107c4110489484c2b38d4d9295b15af2))
* **zero_trust:** add `tunnels.warp_connector.configurations` sub-resource ([2b0e738](https://github.com/cloudflare/cloudflare-python/commit/2b0e7388107c4110489484c2b38d4d9295b15af2))


### Bug Fixes

* **iam:** `OAuthScopeListResponse` type import path moved from `cloudflare.types.iam.oauth_scopes` to `cloudflare.types.iam` ([2b0e738](https://github.com/cloudflare/cloudflare-python/commit/2b0e7388107c4110489484c2b38d4d9295b15af2))


### Chores

* **api:** update composite API spec ([2b0e738](https://github.com/cloudflare/cloudflare-python/commit/2b0e7388107c4110489484c2b38d4d9295b15af2))


### New Resources

#### Tenants (`client.tenants`)

- `get(tenant_id) -> Tenant`
- `tenants.account_types.list(tenant_id) -> SyncSinglePage[AccountTypeListResponse]`
- `tenants.accounts.list(tenant_id) -> SyncSinglePage[TenantAccount]`
- `tenants.entitlements.get(tenant_id) -> TenantEntitlements`
- `tenants.memberships.list(tenant_id) -> SyncSinglePage[TenantMembership]`

New types:
```python
from cloudflare.types.tenants import (
    Tenant,
    AccountTypeListResponse,
    TenantAccount,
    TenantEntitlements,
    TenantMembership,
)
```

#### Flagship (`client.flagship`)

- `flagship.apps.create(*, account_id, **params) -> AppCreateResponse`
- `flagship.apps.update(app_id, *, account_id, **params) -> AppUpdateResponse`
- `flagship.apps.list(*, account_id) -> SyncSinglePage[AppListResponse]`
- `flagship.apps.delete(app_id, *, account_id) -> AppDeleteResponse`
- `flagship.apps.get(app_id, *, account_id) -> AppGetResponse`
- `flagship.apps.flags.create(app_id, *, account_id, **params) -> FlagCreateResponse`
- `flagship.apps.flags.update(flag_key, *, account_id, app_id, **params) -> FlagUpdateResponse`
- `flagship.apps.flags.list(app_id, *, account_id, **params) -> SyncCursorPaginationAfter[FlagListResponse]`
- `flagship.apps.flags.delete(flag_key, *, account_id, app_id) -> FlagDeleteResponse`
- `flagship.apps.flags.get(flag_key, *, account_id, app_id) -> FlagGetResponse`
- `flagship.apps.flags.changelog.list(flag_key, *, account_id, app_id, **params) -> SyncCursorPaginationAfter[ChangelogListResponse]`
- `flagship.apps.evaluate.get(app_id, *, account_id, **params) -> EvaluateGetResponse`

New types:
```python
from cloudflare.types.flagship import (
    AppCreateResponse,
    AppUpdateResponse,
    AppListResponse,
    AppDeleteResponse,
    AppGetResponse,
)
from cloudflare.types.flagship.apps import (
    FlagCreateResponse,
    FlagUpdateResponse,
    FlagListResponse,
    FlagDeleteResponse,
    FlagGetResponse,
    EvaluateGetResponse,
)
from cloudflare.types.flagship.apps.flags import ChangelogListResponse
```

#### Origin TLS Compliance Modes (`client.origin_tls_compliance_modes`)

- `update(*, zone_id, **params) -> Optional[OriginTLSComplianceModeUpdateResponse]`
- `delete(*, zone_id) -> Optional[OriginTLSComplianceModeDeleteResponse]`
- `edit(*, zone_id, **params) -> Optional[OriginTLSComplianceModeEditResponse]`
- `get(*, zone_id) -> Optional[OriginTLSComplianceModeGetResponse]`

New types:
```python
from cloudflare.types.origin_tls_compliance_modes import (
    OriginTLSComplianceModeUpdateResponse,
    OriginTLSComplianceModeDeleteResponse,
    OriginTLSComplianceModeEditResponse,
    OriginTLSComplianceModeGetResponse,
)
```

### New Sub-Resources on Existing Resources

#### AI Gateway - Custom Providers (`client.ai_gateway.custom_providers`)

- `create(*, account_id, **params) -> CustomProviderCreateResponse`
- `list(*, account_id, **params) -> SyncV4PagePaginationArray[CustomProviderListResponse]`
- `delete(id, *, account_id) -> CustomProviderDeleteResponse`
- `get(id, *, account_id) -> CustomProviderGetResponse`

New types:
```python
from cloudflare.types.ai_gateway import (
    CustomProviderCreateResponse,
    CustomProviderListResponse,
    CustomProviderDeleteResponse,
    CustomProviderGetResponse,
)
```

#### Magic Transit - CF1 Sites (`client.magic_transit.cf1_sites`)

- `create(*, account_id, **params) -> SyncSinglePage[Cf1Site]`
- `update(cf1_site_id, *, account_id, **params) -> Cf1Site`
- `list(*, account_id) -> SyncSinglePage[Cf1Site]`
- `delete(cf1_site_id, *, account_id) -> Cf1Site`
- `get(cf1_site_id, *, account_id) -> Cf1Site`
- `cf1_sites.ramps.create(cf1_site_id, *, account_id, **params) -> SyncSinglePage[Ramp]`
- `cf1_sites.ramps.list(cf1_site_id, *, account_id) -> SyncSinglePage[Ramp]`
- `cf1_sites.ramps.delete(ramp_id, *, account_id, cf1_site_id) -> Ramp`
- `cf1_sites.ramps.get(ramp_id, *, account_id, cf1_site_id) -> Ramp`

New types:
```python
from cloudflare.types.magic_transit import Cf1Site
from cloudflare.types.magic_transit.cf1_sites import Ramp
```

#### Magic Transit - IPsec Tunnels PSK Set (`client.magic_transit.ipsec_tunnels`)

- `psk_set(*, account_id, **params) -> IPSECTunnelPSKSetResponse`

New types:
```python
from cloudflare.types.magic_transit import IPSECTunnelPSKSetResponse
```

#### SSL - Auto Origin TLS Kex (`client.ssl.auto_origin_tls_kex`)

- `edit(*, zone_id, **params) -> AutoOriginTLSKexEditResponse`
- `get(*, zone_id) -> AutoOriginTLSKexGetResponse`

New types:
```python
from cloudflare.types.ssl import AutoOriginTLSKexEditResponse, AutoOriginTLSKexGetResponse
```

#### Zones - CT Alerting (`client.zones.ct.alerting`)

- `edit(*, zone_id, **params) -> Optional[AlertingEditResponse]`
- `get(*, zone_id) -> Optional[AlertingGetResponse]`

New types:
```python
from cloudflare.types.zones.ct import AlertingEditResponse, AlertingGetResponse
```

#### User - Tenants (`client.user.tenants`)

- `list() -> SyncSinglePage[Organization]`

#### Zero Trust - DLP Sensitivity Groups (`client.zero_trust.dlp.sensitivity_groups`)

- `create(*, account_id, **params) -> Optional[SensitivityGroupCreateResponse]`
- `update(sensitivity_group_id, *, account_id, **params) -> Optional[SensitivityGroupUpdateResponse]`
- `list(*, account_id) -> SyncSinglePage[SensitivityGroupListResponse]`
- `delete(sensitivity_group_id, *, account_id) -> object`
- `get(sensitivity_group_id, *, account_id) -> Optional[SensitivityGroupGetResponse]`
- `sensitivity_groups.levels.create(...)` / `update(...)` / `list(...)` / `delete(...)` / `get(...)`
- `sensitivity_groups.levels.order.update(...)` / `get(...)`

#### Zero Trust - DLP Data Tag Categories (`client.zero_trust.dlp.data_tag_categories`)

- `create(*, account_id, **params) -> Optional[DataTagCategoryCreateResponse]`
- `update(category_id, *, account_id, **params) -> Optional[DataTagCategoryUpdateResponse]`
- `list(*, account_id) -> SyncSinglePage[DataTagCategoryListResponse]`
- `delete(category_id, *, account_id) -> object`
- `get(category_id, *, account_id) -> Optional[DataTagCategoryGetResponse]`
- `data_tag_categories.data_tags.create(...)` / `update(...)` / `list(...)` / `delete(...)` / `get(...)`

#### Zero Trust - DLP Data Classes (`client.zero_trust.dlp.data_classes`)

- `create(*, account_id, **params) -> Optional[DataClassCreateResponse]`
- `update(data_class_id, *, account_id, **params) -> Optional[DataClassUpdateResponse]`
- `list(*, account_id) -> SyncSinglePage[DataClassListResponse]`
- `delete(data_class_id, *, account_id) -> object`
- `get(data_class_id, *, account_id) -> Optional[DataClassGetResponse]`

#### Zero Trust - WARP Connector Configurations (`client.zero_trust.tunnels.warp_connector.configurations`)

- `update(tunnel_id, *, account_id, **params) -> Optional[ConfigurationUpdateResponse]`
- `get(tunnel_id, *, account_id) -> Optional[ConfigurationGetResponse]`

New types:
```python
from cloudflare.types.zero_trust.tunnels.warp_connector import (
    ConfigurationUpdateResponse,
    ConfigurationGetResponse,
)
```

### Updated Methods

#### D1 - Database Get

`client.d1.database.get` now accepts an optional `fields` parameter to select which fields to include in the response.

```python
# Before (still works)
db = client.d1.database.get(database_id, account_id="...")

# New: select specific fields
db = client.d1.database.get(database_id, account_id="...", fields=["name", "uuid", "file_size"])
```

#### IAM - OAuth Scopes

`client.iam.oauth_scopes` module was flattened from a sub-package to a single module. The `OAuthScopeListResponse` type import path changed:

```python
# Before
from cloudflare.types.iam.oauth_scopes import OAuthScopeListResponse

# After
from cloudflare.types.iam import OAuthScopeListResponse
```
