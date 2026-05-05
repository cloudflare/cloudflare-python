# Cache

Types:

```python
from cloudflare.types.cache import CachePurgeResponse
```

Methods:

- <code title="post /zones/{zone_id}/purge_cache">client.cache.<a href="./src/cloudflare/resources/cache/cache.py">purge</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/cache/cache_purge_params.py">params</a>) -> <a href="./src/cloudflare/types/cache/cache_purge_response.py">Optional[CachePurgeResponse]</a></code>

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

- <code title="post /zones/{zone_id}/cache/cache_reserve_clear">client.cache.cache_reserve.<a href="./src/cloudflare/resources/cache/cache_reserve.py">clear</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/cache/cache_reserve_clear_params.py">params</a>) -> <a href="./src/cloudflare/types/cache/cache_reserve_clear_response.py">Optional[CacheReserveClearResponse]</a></code>
- <code title="patch /zones/{zone_id}/cache/cache_reserve">client.cache.cache_reserve.<a href="./src/cloudflare/resources/cache/cache_reserve.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/cache/cache_reserve_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/cache/cache_reserve_edit_response.py">Optional[CacheReserveEditResponse]</a></code>
- <code title="get /zones/{zone_id}/cache/cache_reserve">client.cache.cache_reserve.<a href="./src/cloudflare/resources/cache/cache_reserve.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/cache/cache_reserve_get_response.py">Optional[CacheReserveGetResponse]</a></code>
- <code title="get /zones/{zone_id}/cache/cache_reserve_clear">client.cache.cache_reserve.<a href="./src/cloudflare/resources/cache/cache_reserve.py">status</a>(\*, zone_id) -> <a href="./src/cloudflare/types/cache/cache_reserve_status_response.py">Optional[CacheReserveStatusResponse]</a></code>

## SmartTieredCache

Types:

```python
from cloudflare.types.cache import (
    SmartTieredCacheCreateResponse,
    SmartTieredCacheDeleteResponse,
    SmartTieredCacheEditResponse,
    SmartTieredCacheGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/cache/tiered_cache_smart_topology_enable">client.cache.smart_tiered_cache.<a href="./src/cloudflare/resources/cache/smart_tiered_cache.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/cache/smart_tiered_cache_create_params.py">params</a>) -> <a href="./src/cloudflare/types/cache/smart_tiered_cache_create_response.py">Optional[SmartTieredCacheCreateResponse]</a></code>
- <code title="delete /zones/{zone_id}/cache/tiered_cache_smart_topology_enable">client.cache.smart_tiered_cache.<a href="./src/cloudflare/resources/cache/smart_tiered_cache.py">delete</a>(\*, zone_id) -> <a href="./src/cloudflare/types/cache/smart_tiered_cache_delete_response.py">Optional[SmartTieredCacheDeleteResponse]</a></code>
- <code title="patch /zones/{zone_id}/cache/tiered_cache_smart_topology_enable">client.cache.smart_tiered_cache.<a href="./src/cloudflare/resources/cache/smart_tiered_cache.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/cache/smart_tiered_cache_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/cache/smart_tiered_cache_edit_response.py">Optional[SmartTieredCacheEditResponse]</a></code>
- <code title="get /zones/{zone_id}/cache/tiered_cache_smart_topology_enable">client.cache.smart_tiered_cache.<a href="./src/cloudflare/resources/cache/smart_tiered_cache.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/cache/smart_tiered_cache_get_response.py">Optional[SmartTieredCacheGetResponse]</a></code>

## Variants

Types:

```python
from cloudflare.types.cache import (
    CacheVariant,
    VariantDeleteResponse,
    VariantEditResponse,
    VariantGetResponse,
)
```

Methods:

- <code title="delete /zones/{zone_id}/cache/variants">client.cache.variants.<a href="./src/cloudflare/resources/cache/variants.py">delete</a>(\*, zone_id) -> <a href="./src/cloudflare/types/cache/variant_delete_response.py">Optional[VariantDeleteResponse]</a></code>
- <code title="patch /zones/{zone_id}/cache/variants">client.cache.variants.<a href="./src/cloudflare/resources/cache/variants.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/cache/variant_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/cache/variant_edit_response.py">Optional[VariantEditResponse]</a></code>
- <code title="get /zones/{zone_id}/cache/variants">client.cache.variants.<a href="./src/cloudflare/resources/cache/variants.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/cache/variant_get_response.py">Optional[VariantGetResponse]</a></code>

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

- <code title="patch /zones/{zone_id}/cache/regional_tiered_cache">client.cache.regional_tiered_cache.<a href="./src/cloudflare/resources/cache/regional_tiered_cache.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/cache/regional_tiered_cache_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/cache/regional_tiered_cache_edit_response.py">Optional[RegionalTieredCacheEditResponse]</a></code>
- <code title="get /zones/{zone_id}/cache/regional_tiered_cache">client.cache.regional_tiered_cache.<a href="./src/cloudflare/resources/cache/regional_tiered_cache.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/cache/regional_tiered_cache_get_response.py">Optional[RegionalTieredCacheGetResponse]</a></code>

## OriginCloudRegions

Types:

```python
from cloudflare.types.cache import (
    OriginCloudRegion,
    OriginCloudRegionDeleteResponse,
    OriginCloudRegionBulkDeleteResponse,
    OriginCloudRegionBulkUpdateResponse,
    OriginCloudRegionSupportedRegionsResponse,
)
```

Methods:

- <code title="put /zones/{zone_id}/origin/cloud_regions/{origin_ip}">client.cache.origin_cloud_regions.<a href="./src/cloudflare/resources/cache/origin_cloud_regions.py">update</a>(path_origin_ip, \*, zone_id, \*\*<a href="src/cloudflare/types/cache/origin_cloud_region_update_params.py">params</a>) -> <a href="./src/cloudflare/types/cache/origin_cloud_region.py">Optional[OriginCloudRegion]</a></code>
- <code title="get /zones/{zone_id}/origin/cloud_regions">client.cache.origin_cloud_regions.<a href="./src/cloudflare/resources/cache/origin_cloud_regions.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/cache/origin_cloud_region_list_params.py">params</a>) -> <a href="./src/cloudflare/types/cache/origin_cloud_region.py">SyncV4PagePaginationArray[OriginCloudRegion]</a></code>
- <code title="delete /zones/{zone_id}/origin/cloud_regions/{origin_ip}">client.cache.origin_cloud_regions.<a href="./src/cloudflare/resources/cache/origin_cloud_regions.py">delete</a>(origin_ip, \*, zone_id) -> <a href="./src/cloudflare/types/cache/origin_cloud_region_delete_response.py">Optional[OriginCloudRegionDeleteResponse]</a></code>
- <code title="delete /zones/{zone_id}/origin/cloud_regions/batch">client.cache.origin_cloud_regions.<a href="./src/cloudflare/resources/cache/origin_cloud_regions.py">bulk_delete</a>(\*, zone_id) -> <a href="./src/cloudflare/types/cache/origin_cloud_region_bulk_delete_response.py">Optional[OriginCloudRegionBulkDeleteResponse]</a></code>
- <code title="put /zones/{zone_id}/origin/cloud_regions/batch">client.cache.origin_cloud_regions.<a href="./src/cloudflare/resources/cache/origin_cloud_regions.py">bulk_update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/cache/origin_cloud_region_bulk_update_params.py">params</a>) -> <a href="./src/cloudflare/types/cache/origin_cloud_region_bulk_update_response.py">Optional[OriginCloudRegionBulkUpdateResponse]</a></code>
- <code title="get /zones/{zone_id}/origin/cloud_regions/{origin_ip}">client.cache.origin_cloud_regions.<a href="./src/cloudflare/resources/cache/origin_cloud_regions.py">get</a>(origin_ip, \*, zone_id) -> <a href="./src/cloudflare/types/cache/origin_cloud_region.py">Optional[OriginCloudRegion]</a></code>
- <code title="get /zones/{zone_id}/origin/cloud_regions/supported_regions">client.cache.origin_cloud_regions.<a href="./src/cloudflare/resources/cache/origin_cloud_regions.py">supported_regions</a>(\*, zone_id) -> <a href="./src/cloudflare/types/cache/origin_cloud_region_supported_regions_response.py">Optional[OriginCloudRegionSupportedRegionsResponse]</a></code>
