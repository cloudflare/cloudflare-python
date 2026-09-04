# Hostnames

## Settings

### TLS

Types:

```python
from cloudflare.types.hostnames.settings import (
    Setting,
    SettingValue,
    TLSListResponse,
    TLSDeleteResponse,
)
```

Methods:

- <code title="put /zones/{zone_id}/hostnames/settings/{setting_id}/{hostname}">client.hostnames.settings.tls.<a href="./src/cloudflare/resources/hostnames/settings/tls.py">update</a>(hostname, \*, zone_id, setting_id, \*\*<a href="src/cloudflare/types/hostnames/settings/tls_update_params.py">params</a>) -> <a href="./src/cloudflare/types/hostnames/settings/setting.py">Optional[Setting]</a></code>
- <code title="get /zones/{zone_id}/hostnames/settings/{setting_id}">client.hostnames.settings.tls.<a href="./src/cloudflare/resources/hostnames/settings/tls.py">list</a>(setting_id, \*, zone_id) -> <a href="./src/cloudflare/types/hostnames/settings/tls_list_response.py">SyncSinglePage[TLSListResponse]</a></code>
- <code title="delete /zones/{zone_id}/hostnames/settings/{setting_id}/{hostname}">client.hostnames.settings.tls.<a href="./src/cloudflare/resources/hostnames/settings/tls.py">delete</a>(hostname, \*, zone_id, setting_id) -> <a href="./src/cloudflare/types/hostnames/settings/tls_delete_response.py">Optional[TLSDeleteResponse]</a></code>
- <code title="get /zones/{zone_id}/hostnames/settings/{setting_id}/{hostname}">client.hostnames.settings.tls.<a href="./src/cloudflare/resources/hostnames/settings/tls.py">get</a>(hostname, \*, zone_id, setting_id) -> <a href="./src/cloudflare/types/hostnames/settings/setting.py">Optional[Setting]</a></code>
