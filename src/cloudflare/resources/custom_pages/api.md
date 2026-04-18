# CustomPages

Types:

```python
from cloudflare.types.custom_pages import (
    CustomPageUpdateResponse,
    CustomPageListResponse,
    CustomPageGetResponse,
)
```

Methods:

- <code title="put /{accounts_or_zones}/{account_or_zone_id}/custom_pages/{identifier}">client.custom_pages.<a href="./src/cloudflare/resources/custom_pages/custom_pages.py">update</a>(identifier, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/custom_pages/custom_page_update_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_pages/custom_page_update_response.py">Optional[CustomPageUpdateResponse]</a></code>
- <code title="get /{accounts_or_zones}/{account_or_zone_id}/custom_pages">client.custom_pages.<a href="./src/cloudflare/resources/custom_pages/custom_pages.py">list</a>(\*, account_id, zone_id) -> <a href="./src/cloudflare/types/custom_pages/custom_page_list_response.py">SyncSinglePage[CustomPageListResponse]</a></code>
- <code title="get /{accounts_or_zones}/{account_or_zone_id}/custom_pages/{identifier}">client.custom_pages.<a href="./src/cloudflare/resources/custom_pages/custom_pages.py">get</a>(identifier, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/custom_pages/custom_page_get_response.py">Optional[CustomPageGetResponse]</a></code>
