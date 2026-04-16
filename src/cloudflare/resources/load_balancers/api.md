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

- <code title="get /accounts/{account_id}/load_balancers/monitors/{monitor_id}/references">client.load_balancers.monitors.references.<a href="./src/cloudflare/resources/load_balancers/monitors/references.py">get</a>(monitor_id, \*, account_id) -> <a href="./src/cloudflare/types/load_balancers/monitors/reference_get_response.py">SyncSinglePage[ReferenceGetResponse]</a></code>

## MonitorGroups

Types:

```python
from cloudflare.types.load_balancers import MonitorGroup
```

Methods:

- <code title="post /accounts/{account_id}/load_balancers/monitor_groups">client.load_balancers.monitor_groups.<a href="./src/cloudflare/resources/load_balancers/monitor_groups.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/load_balancers/monitor_group_create_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancers/monitor_group.py">MonitorGroup</a></code>
- <code title="put /accounts/{account_id}/load_balancers/monitor_groups/{monitor_group_id}">client.load_balancers.monitor_groups.<a href="./src/cloudflare/resources/load_balancers/monitor_groups.py">update</a>(monitor_group_id, \*, account_id, \*\*<a href="src/cloudflare/types/load_balancers/monitor_group_update_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancers/monitor_group.py">MonitorGroup</a></code>
- <code title="get /accounts/{account_id}/load_balancers/monitor_groups">client.load_balancers.monitor_groups.<a href="./src/cloudflare/resources/load_balancers/monitor_groups.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/load_balancers/monitor_group.py">SyncSinglePage[MonitorGroup]</a></code>
- <code title="delete /accounts/{account_id}/load_balancers/monitor_groups/{monitor_group_id}">client.load_balancers.monitor_groups.<a href="./src/cloudflare/resources/load_balancers/monitor_groups.py">delete</a>(monitor_group_id, \*, account_id) -> <a href="./src/cloudflare/types/load_balancers/monitor_group.py">MonitorGroup</a></code>
- <code title="patch /accounts/{account_id}/load_balancers/monitor_groups/{monitor_group_id}">client.load_balancers.monitor_groups.<a href="./src/cloudflare/resources/load_balancers/monitor_groups.py">edit</a>(monitor_group_id, \*, account_id, \*\*<a href="src/cloudflare/types/load_balancers/monitor_group_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancers/monitor_group.py">MonitorGroup</a></code>
- <code title="get /accounts/{account_id}/load_balancers/monitor_groups/{monitor_group_id}">client.load_balancers.monitor_groups.<a href="./src/cloudflare/resources/load_balancers/monitor_groups.py">get</a>(monitor_group_id, \*, account_id) -> <a href="./src/cloudflare/types/load_balancers/monitor_group.py">MonitorGroup</a></code>

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
- <code title="patch /accounts/{account_id}/load_balancers/pools">client.load_balancers.pools.<a href="./src/cloudflare/resources/load_balancers/pools/pools.py">bulk_edit</a>(\*, account_id, \*\*<a href="src/cloudflare/types/load_balancers/pool_bulk_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancers/pool.py">SyncSinglePage[Pool]</a></code>
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

- <code title="get /accounts/{account_id}/load_balancers/pools/{pool_id}/references">client.load_balancers.pools.references.<a href="./src/cloudflare/resources/load_balancers/pools/references.py">get</a>(pool_id, \*, account_id) -> <a href="./src/cloudflare/types/load_balancers/pools/reference_get_response.py">SyncSinglePage[ReferenceGetResponse]</a></code>

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

- <code title="get /accounts/{account_id}/load_balancers/search">client.load_balancers.searches.<a href="./src/cloudflare/resources/load_balancers/searches.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/load_balancers/search_list_params.py">params</a>) -> <a href="./src/cloudflare/types/load_balancers/search_list_response.py">SyncV4PagePagination[SearchListResponse]</a></code>
