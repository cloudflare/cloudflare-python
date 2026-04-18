# ContentScanning

Methods:

- <code title="post /zones/{zone_id}/content-upload-scan/disable">client.content_scanning.<a href="./src/cloudflare/resources/content_scanning/content_scanning.py">disable</a>(\*, zone_id) -> object</code>
- <code title="post /zones/{zone_id}/content-upload-scan/enable">client.content_scanning.<a href="./src/cloudflare/resources/content_scanning/content_scanning.py">enable</a>(\*, zone_id) -> object</code>

## Payloads

Types:

```python
from cloudflare.types.content_scanning import (
    PayloadCreateResponse,
    PayloadListResponse,
    PayloadDeleteResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/content-upload-scan/payloads">client.content_scanning.payloads.<a href="./src/cloudflare/resources/content_scanning/payloads.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/content_scanning/payload_create_params.py">params</a>) -> <a href="./src/cloudflare/types/content_scanning/payload_create_response.py">SyncSinglePage[PayloadCreateResponse]</a></code>
- <code title="get /zones/{zone_id}/content-upload-scan/payloads">client.content_scanning.payloads.<a href="./src/cloudflare/resources/content_scanning/payloads.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/content_scanning/payload_list_response.py">SyncSinglePage[PayloadListResponse]</a></code>
- <code title="delete /zones/{zone_id}/content-upload-scan/payloads/{expression_id}">client.content_scanning.payloads.<a href="./src/cloudflare/resources/content_scanning/payloads.py">delete</a>(expression_id, \*, zone_id) -> <a href="./src/cloudflare/types/content_scanning/payload_delete_response.py">SyncSinglePage[PayloadDeleteResponse]</a></code>

## Settings

Types:

```python
from cloudflare.types.content_scanning import SettingGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/content-upload-scan/settings">client.content_scanning.settings.<a href="./src/cloudflare/resources/content_scanning/settings.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/content_scanning/setting_get_response.py">SettingGetResponse</a></code>
