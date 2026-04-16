# Filters

Types:

```python
from cloudflare.types.filters import FirewallFilter, FilterDeleteResponse, FilterBulkDeleteResponse
```

Methods:

- <code title="post /zones/{zone_id}/filters">client.filters.<a href="./src/cloudflare/resources/filters/filters.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/filters/filter_create_params.py">params</a>) -> <a href="./src/cloudflare/types/filters/firewall_filter.py">SyncSinglePage[FirewallFilter]</a></code>
- <code title="put /zones/{zone_id}/filters/{filter_id}">client.filters.<a href="./src/cloudflare/resources/filters/filters.py">update</a>(filter_id, \*, zone_id, \*\*<a href="src/cloudflare/types/filters/filter_update_params.py">params</a>) -> <a href="./src/cloudflare/types/filters/firewall_filter.py">FirewallFilter</a></code>
- <code title="get /zones/{zone_id}/filters">client.filters.<a href="./src/cloudflare/resources/filters/filters.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/filters/filter_list_params.py">params</a>) -> <a href="./src/cloudflare/types/filters/firewall_filter.py">SyncV4PagePaginationArray[FirewallFilter]</a></code>
- <code title="delete /zones/{zone_id}/filters/{filter_id}">client.filters.<a href="./src/cloudflare/resources/filters/filters.py">delete</a>(filter_id, \*, zone_id) -> <a href="./src/cloudflare/types/filters/filter_delete_response.py">FilterDeleteResponse</a></code>
- <code title="delete /zones/{zone_id}/filters">client.filters.<a href="./src/cloudflare/resources/filters/filters.py">bulk_delete</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/filters/filter_bulk_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/filters/filter_bulk_delete_response.py">Optional[FilterBulkDeleteResponse]</a></code>
- <code title="put /zones/{zone_id}/filters">client.filters.<a href="./src/cloudflare/resources/filters/filters.py">bulk_update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/filters/filter_bulk_update_params.py">params</a>) -> <a href="./src/cloudflare/types/filters/firewall_filter.py">SyncSinglePage[FirewallFilter]</a></code>
- <code title="get /zones/{zone_id}/filters/{filter_id}">client.filters.<a href="./src/cloudflare/resources/filters/filters.py">get</a>(filter_id, \*, zone_id) -> <a href="./src/cloudflare/types/filters/firewall_filter.py">FirewallFilter</a></code>
