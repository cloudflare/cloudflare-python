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

## Assets

Types:

```python
from cloudflare.types.custom_pages import (
    AssetCreateResponse,
    AssetUpdateResponse,
    AssetListResponse,
    AssetGetResponse,
)
```

Methods:

- <code title="post /{accounts_or_zones}/{account_or_zone_id}/custom_pages/assets">client.custom_pages.assets.<a href="./src/cloudflare/resources/custom_pages/assets.py">create</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/custom_pages/asset_create_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_pages/asset_create_response.py">Optional[AssetCreateResponse]</a></code>
- <code title="put /{accounts_or_zones}/{account_or_zone_id}/custom_pages/assets/{asset_name}">client.custom_pages.assets.<a href="./src/cloudflare/resources/custom_pages/assets.py">update</a>(asset_name, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/custom_pages/asset_update_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_pages/asset_update_response.py">Optional[AssetUpdateResponse]</a></code>
- <code title="get /{accounts_or_zones}/{account_or_zone_id}/custom_pages/assets">client.custom_pages.assets.<a href="./src/cloudflare/resources/custom_pages/assets.py">list</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/custom_pages/asset_list_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_pages/asset_list_response.py">SyncV4PagePaginationArray[AssetListResponse]</a></code>
- <code title="delete /{accounts_or_zones}/{account_or_zone_id}/custom_pages/assets/{asset_name}">client.custom_pages.assets.<a href="./src/cloudflare/resources/custom_pages/assets.py">delete</a>(asset_name, \*, account_id, zone_id) -> None</code>
- <code title="get /{accounts_or_zones}/{account_or_zone_id}/custom_pages/assets/{asset_name}">client.custom_pages.assets.<a href="./src/cloudflare/resources/custom_pages/assets.py">get</a>(asset_name, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/custom_pages/asset_get_response.py">Optional[AssetGetResponse]</a></code>
