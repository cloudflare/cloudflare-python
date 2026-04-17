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

- <code title="patch /zones/{zone_id}/argo/tiered_caching">client.argo.tiered_caching.<a href="./src/cloudflare/resources/argo/tiered_caching.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/argo/tiered_caching_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/argo/tiered_caching_edit_response.py">Optional[TieredCachingEditResponse]</a></code>
- <code title="get /zones/{zone_id}/argo/tiered_caching">client.argo.tiered_caching.<a href="./src/cloudflare/resources/argo/tiered_caching.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/argo/tiered_caching_get_response.py">Optional[TieredCachingGetResponse]</a></code>
