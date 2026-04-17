# RateLimits

Types:

```python
from cloudflare.types.rate_limits import Action, RateLimit, RateLimitDeleteResponse
```

Methods:

- <code title="post /zones/{zone_id}/rate_limits">client.rate_limits.<a href="./src/cloudflare/resources/rate_limits/rate_limits.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/rate_limits/rate_limit_create_params.py">params</a>) -> <a href="./src/cloudflare/types/rate_limits/rate_limit.py">RateLimit</a></code>
- <code title="get /zones/{zone_id}/rate_limits">client.rate_limits.<a href="./src/cloudflare/resources/rate_limits/rate_limits.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/rate_limits/rate_limit_list_params.py">params</a>) -> <a href="./src/cloudflare/types/rate_limits/rate_limit.py">SyncV4PagePaginationArray[RateLimit]</a></code>
- <code title="delete /zones/{zone_id}/rate_limits/{rate_limit_id}">client.rate_limits.<a href="./src/cloudflare/resources/rate_limits/rate_limits.py">delete</a>(rate_limit_id, \*, zone_id) -> <a href="./src/cloudflare/types/rate_limits/rate_limit_delete_response.py">RateLimitDeleteResponse</a></code>
- <code title="put /zones/{zone_id}/rate_limits/{rate_limit_id}">client.rate_limits.<a href="./src/cloudflare/resources/rate_limits/rate_limits.py">edit</a>(rate_limit_id, \*, zone_id, \*\*<a href="src/cloudflare/types/rate_limits/rate_limit_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/rate_limits/rate_limit.py">RateLimit</a></code>
- <code title="get /zones/{zone_id}/rate_limits/{rate_limit_id}">client.rate_limits.<a href="./src/cloudflare/resources/rate_limits/rate_limits.py">get</a>(rate_limit_id, \*, zone_id) -> <a href="./src/cloudflare/types/rate_limits/rate_limit.py">RateLimit</a></code>
