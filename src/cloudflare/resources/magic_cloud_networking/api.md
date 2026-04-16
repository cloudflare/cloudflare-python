# MagicCloudNetworking

## CatalogSyncs

Types:

```python
from cloudflare.types.magic_cloud_networking import (
    CatalogSyncCreateResponse,
    CatalogSyncUpdateResponse,
    CatalogSyncListResponse,
    CatalogSyncDeleteResponse,
    CatalogSyncEditResponse,
    CatalogSyncGetResponse,
    CatalogSyncRefreshResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/magic/cloud/catalog-syncs">client.magic_cloud_networking.catalog_syncs.<a href="./src/cloudflare/resources/magic_cloud_networking/catalog_syncs/catalog_syncs.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/magic_cloud_networking/catalog_sync_create_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_cloud_networking/catalog_sync_create_response.py">CatalogSyncCreateResponse</a></code>
- <code title="put /accounts/{account_id}/magic/cloud/catalog-syncs/{sync_id}">client.magic_cloud_networking.catalog_syncs.<a href="./src/cloudflare/resources/magic_cloud_networking/catalog_syncs/catalog_syncs.py">update</a>(sync_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_cloud_networking/catalog_sync_update_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_cloud_networking/catalog_sync_update_response.py">CatalogSyncUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/magic/cloud/catalog-syncs">client.magic_cloud_networking.catalog_syncs.<a href="./src/cloudflare/resources/magic_cloud_networking/catalog_syncs/catalog_syncs.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/magic_cloud_networking/catalog_sync_list_response.py">SyncSinglePage[CatalogSyncListResponse]</a></code>
- <code title="delete /accounts/{account_id}/magic/cloud/catalog-syncs/{sync_id}">client.magic_cloud_networking.catalog_syncs.<a href="./src/cloudflare/resources/magic_cloud_networking/catalog_syncs/catalog_syncs.py">delete</a>(sync_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_cloud_networking/catalog_sync_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_cloud_networking/catalog_sync_delete_response.py">CatalogSyncDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/magic/cloud/catalog-syncs/{sync_id}">client.magic_cloud_networking.catalog_syncs.<a href="./src/cloudflare/resources/magic_cloud_networking/catalog_syncs/catalog_syncs.py">edit</a>(sync_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_cloud_networking/catalog_sync_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_cloud_networking/catalog_sync_edit_response.py">CatalogSyncEditResponse</a></code>
- <code title="get /accounts/{account_id}/magic/cloud/catalog-syncs/{sync_id}">client.magic_cloud_networking.catalog_syncs.<a href="./src/cloudflare/resources/magic_cloud_networking/catalog_syncs/catalog_syncs.py">get</a>(sync_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_cloud_networking/catalog_sync_get_response.py">CatalogSyncGetResponse</a></code>
- <code title="post /accounts/{account_id}/magic/cloud/catalog-syncs/{sync_id}/refresh">client.magic_cloud_networking.catalog_syncs.<a href="./src/cloudflare/resources/magic_cloud_networking/catalog_syncs/catalog_syncs.py">refresh</a>(sync_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_cloud_networking/catalog_sync_refresh_response.py">str</a></code>

### PrebuiltPolicies

Types:

```python
from cloudflare.types.magic_cloud_networking.catalog_syncs import PrebuiltPolicyListResponse
```

Methods:

- <code title="get /accounts/{account_id}/magic/cloud/catalog-syncs/prebuilt-policies">client.magic_cloud_networking.catalog_syncs.prebuilt_policies.<a href="./src/cloudflare/resources/magic_cloud_networking/catalog_syncs/prebuilt_policies.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/magic_cloud_networking/catalog_syncs/prebuilt_policy_list_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_cloud_networking/catalog_syncs/prebuilt_policy_list_response.py">SyncSinglePage[PrebuiltPolicyListResponse]</a></code>

## OnRamps

Types:

```python
from cloudflare.types.magic_cloud_networking import (
    OnRampCreateResponse,
    OnRampUpdateResponse,
    OnRampListResponse,
    OnRampDeleteResponse,
    OnRampApplyResponse,
    OnRampEditResponse,
    OnRampGetResponse,
    OnRampPlanResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/magic/cloud/onramps">client.magic_cloud_networking.on_ramps.<a href="./src/cloudflare/resources/magic_cloud_networking/on_ramps/on_ramps.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/magic_cloud_networking/on_ramp_create_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_cloud_networking/on_ramp_create_response.py">OnRampCreateResponse</a></code>
- <code title="put /accounts/{account_id}/magic/cloud/onramps/{onramp_id}">client.magic_cloud_networking.on_ramps.<a href="./src/cloudflare/resources/magic_cloud_networking/on_ramps/on_ramps.py">update</a>(onramp_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_cloud_networking/on_ramp_update_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_cloud_networking/on_ramp_update_response.py">OnRampUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/magic/cloud/onramps">client.magic_cloud_networking.on_ramps.<a href="./src/cloudflare/resources/magic_cloud_networking/on_ramps/on_ramps.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/magic_cloud_networking/on_ramp_list_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_cloud_networking/on_ramp_list_response.py">SyncSinglePage[OnRampListResponse]</a></code>
- <code title="delete /accounts/{account_id}/magic/cloud/onramps/{onramp_id}">client.magic_cloud_networking.on_ramps.<a href="./src/cloudflare/resources/magic_cloud_networking/on_ramps/on_ramps.py">delete</a>(onramp_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_cloud_networking/on_ramp_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_cloud_networking/on_ramp_delete_response.py">OnRampDeleteResponse</a></code>
- <code title="post /accounts/{account_id}/magic/cloud/onramps/{onramp_id}/apply">client.magic_cloud_networking.on_ramps.<a href="./src/cloudflare/resources/magic_cloud_networking/on_ramps/on_ramps.py">apply</a>(onramp_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_cloud_networking/on_ramp_apply_response.py">OnRampApplyResponse</a></code>
- <code title="patch /accounts/{account_id}/magic/cloud/onramps/{onramp_id}">client.magic_cloud_networking.on_ramps.<a href="./src/cloudflare/resources/magic_cloud_networking/on_ramps/on_ramps.py">edit</a>(onramp_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_cloud_networking/on_ramp_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_cloud_networking/on_ramp_edit_response.py">OnRampEditResponse</a></code>
- <code title="post /accounts/{account_id}/magic/cloud/onramps/{onramp_id}/export">client.magic_cloud_networking.on_ramps.<a href="./src/cloudflare/resources/magic_cloud_networking/on_ramps/on_ramps.py">export</a>(onramp_id, \*, account_id) -> BinaryAPIResponse</code>
- <code title="get /accounts/{account_id}/magic/cloud/onramps/{onramp_id}">client.magic_cloud_networking.on_ramps.<a href="./src/cloudflare/resources/magic_cloud_networking/on_ramps/on_ramps.py">get</a>(onramp_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_cloud_networking/on_ramp_get_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_cloud_networking/on_ramp_get_response.py">OnRampGetResponse</a></code>
- <code title="post /accounts/{account_id}/magic/cloud/onramps/{onramp_id}/plan">client.magic_cloud_networking.on_ramps.<a href="./src/cloudflare/resources/magic_cloud_networking/on_ramps/on_ramps.py">plan</a>(onramp_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_cloud_networking/on_ramp_plan_response.py">OnRampPlanResponse</a></code>

### AddressSpaces

Types:

```python
from cloudflare.types.magic_cloud_networking.on_ramps import (
    AddressSpaceUpdateResponse,
    AddressSpaceListResponse,
    AddressSpaceEditResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/magic/cloud/onramps/magic_wan_address_space">client.magic_cloud_networking.on_ramps.address_spaces.<a href="./src/cloudflare/resources/magic_cloud_networking/on_ramps/address_spaces.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/magic_cloud_networking/on_ramps/address_space_update_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_cloud_networking/on_ramps/address_space_update_response.py">AddressSpaceUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/magic/cloud/onramps/magic_wan_address_space">client.magic_cloud_networking.on_ramps.address_spaces.<a href="./src/cloudflare/resources/magic_cloud_networking/on_ramps/address_spaces.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/magic_cloud_networking/on_ramps/address_space_list_response.py">AddressSpaceListResponse</a></code>
- <code title="patch /accounts/{account_id}/magic/cloud/onramps/magic_wan_address_space">client.magic_cloud_networking.on_ramps.address_spaces.<a href="./src/cloudflare/resources/magic_cloud_networking/on_ramps/address_spaces.py">edit</a>(\*, account_id, \*\*<a href="src/cloudflare/types/magic_cloud_networking/on_ramps/address_space_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_cloud_networking/on_ramps/address_space_edit_response.py">AddressSpaceEditResponse</a></code>

## CloudIntegrations

Types:

```python
from cloudflare.types.magic_cloud_networking import (
    CloudIntegrationCreateResponse,
    CloudIntegrationUpdateResponse,
    CloudIntegrationListResponse,
    CloudIntegrationDeleteResponse,
    CloudIntegrationDiscoverResponse,
    CloudIntegrationDiscoverAllResponse,
    CloudIntegrationEditResponse,
    CloudIntegrationGetResponse,
    CloudIntegrationInitialSetupResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/magic/cloud/providers">client.magic_cloud_networking.cloud_integrations.<a href="./src/cloudflare/resources/magic_cloud_networking/cloud_integrations.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/magic_cloud_networking/cloud_integration_create_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_cloud_networking/cloud_integration_create_response.py">CloudIntegrationCreateResponse</a></code>
- <code title="put /accounts/{account_id}/magic/cloud/providers/{provider_id}">client.magic_cloud_networking.cloud_integrations.<a href="./src/cloudflare/resources/magic_cloud_networking/cloud_integrations.py">update</a>(provider_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_cloud_networking/cloud_integration_update_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_cloud_networking/cloud_integration_update_response.py">CloudIntegrationUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/magic/cloud/providers">client.magic_cloud_networking.cloud_integrations.<a href="./src/cloudflare/resources/magic_cloud_networking/cloud_integrations.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/magic_cloud_networking/cloud_integration_list_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_cloud_networking/cloud_integration_list_response.py">SyncSinglePage[CloudIntegrationListResponse]</a></code>
- <code title="delete /accounts/{account_id}/magic/cloud/providers/{provider_id}">client.magic_cloud_networking.cloud_integrations.<a href="./src/cloudflare/resources/magic_cloud_networking/cloud_integrations.py">delete</a>(provider_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_cloud_networking/cloud_integration_delete_response.py">CloudIntegrationDeleteResponse</a></code>
- <code title="post /accounts/{account_id}/magic/cloud/providers/{provider_id}/discover">client.magic_cloud_networking.cloud_integrations.<a href="./src/cloudflare/resources/magic_cloud_networking/cloud_integrations.py">discover</a>(provider_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_cloud_networking/cloud_integration_discover_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_cloud_networking/cloud_integration_discover_response.py">CloudIntegrationDiscoverResponse</a></code>
- <code title="post /accounts/{account_id}/magic/cloud/providers/discover">client.magic_cloud_networking.cloud_integrations.<a href="./src/cloudflare/resources/magic_cloud_networking/cloud_integrations.py">discover_all</a>(\*, account_id) -> <a href="./src/cloudflare/types/magic_cloud_networking/cloud_integration_discover_all_response.py">CloudIntegrationDiscoverAllResponse</a></code>
- <code title="patch /accounts/{account_id}/magic/cloud/providers/{provider_id}">client.magic_cloud_networking.cloud_integrations.<a href="./src/cloudflare/resources/magic_cloud_networking/cloud_integrations.py">edit</a>(provider_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_cloud_networking/cloud_integration_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_cloud_networking/cloud_integration_edit_response.py">CloudIntegrationEditResponse</a></code>
- <code title="get /accounts/{account_id}/magic/cloud/providers/{provider_id}">client.magic_cloud_networking.cloud_integrations.<a href="./src/cloudflare/resources/magic_cloud_networking/cloud_integrations.py">get</a>(provider_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_cloud_networking/cloud_integration_get_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_cloud_networking/cloud_integration_get_response.py">CloudIntegrationGetResponse</a></code>
- <code title="get /accounts/{account_id}/magic/cloud/providers/{provider_id}/initial_setup">client.magic_cloud_networking.cloud_integrations.<a href="./src/cloudflare/resources/magic_cloud_networking/cloud_integrations.py">initial_setup</a>(provider_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_cloud_networking/cloud_integration_initial_setup_response.py">CloudIntegrationInitialSetupResponse</a></code>

## Resources

Types:

```python
from cloudflare.types.magic_cloud_networking import (
    ResourceListResponse,
    ResourceGetResponse,
    ResourcePolicyPreviewResponse,
)
```

Methods:

- <code title="get /accounts/{account_id}/magic/cloud/resources">client.magic_cloud_networking.resources.<a href="./src/cloudflare/resources/magic_cloud_networking/resources.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/magic_cloud_networking/resource_list_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_cloud_networking/resource_list_response.py">SyncV4PagePaginationArray[ResourceListResponse]</a></code>
- <code title="get /accounts/{account_id}/magic/cloud/resources/export">client.magic_cloud_networking.resources.<a href="./src/cloudflare/resources/magic_cloud_networking/resources.py">export</a>(\*, account_id, \*\*<a href="src/cloudflare/types/magic_cloud_networking/resource_export_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /accounts/{account_id}/magic/cloud/resources/{resource_id}">client.magic_cloud_networking.resources.<a href="./src/cloudflare/resources/magic_cloud_networking/resources.py">get</a>(resource_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_cloud_networking/resource_get_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_cloud_networking/resource_get_response.py">ResourceGetResponse</a></code>
- <code title="post /accounts/{account_id}/magic/cloud/resources/policy-preview">client.magic_cloud_networking.resources.<a href="./src/cloudflare/resources/magic_cloud_networking/resources.py">policy_preview</a>(\*, account_id, \*\*<a href="src/cloudflare/types/magic_cloud_networking/resource_policy_preview_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_cloud_networking/resource_policy_preview_response.py">str</a></code>
