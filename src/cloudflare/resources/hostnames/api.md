# Hostnames

## Settings

### TLS

Types:

```python
from cloudflare.types.hostnames.settings import (
    Setting,
    SettingValue,
    TLSDeleteResponse,
    TLSGetResponse,
)
```

Methods:

- <code title="put /zones/{zone_id}/hostnames/settings/{setting_id}/{hostname}">client.hostnames.settings.tls.<a href="./src/cloudflare/resources/hostnames/settings/tls.py">update</a>(hostname, \*, zone_id, setting_id, \*\*<a href="src/cloudflare/types/hostnames/settings/tls_update_params.py">params</a>) -> <a href="./src/cloudflare/types/hostnames/settings/setting.py">Optional[Setting]</a></code>
- <code title="delete /zones/{zone_id}/hostnames/settings/{setting_id}/{hostname}">client.hostnames.settings.tls.<a href="./src/cloudflare/resources/hostnames/settings/tls.py">delete</a>(hostname, \*, zone_id, setting_id) -> <a href="./src/cloudflare/types/hostnames/settings/tls_delete_response.py">Optional[TLSDeleteResponse]</a></code>
- <code title="get /zones/{zone_id}/hostnames/settings/{setting_id}">client.hostnames.settings.tls.<a href="./src/cloudflare/resources/hostnames/settings/tls.py">get</a>(setting_id, \*, zone_id) -> <a href="./src/cloudflare/types/hostnames/settings/tls_get_response.py">SyncSinglePage[TLSGetResponse]</a></code>
