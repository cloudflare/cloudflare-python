# TenantCustomNameservers

Types:

```python
from cloudflare.types.tenant_custom_nameservers import (
    TenantCustomNameserverCreateResponse,
    TenantCustomNameserverDeleteResponse,
    TenantCustomNameserverGetResponse,
)
```

Methods:

- <code title="post /tenants/{tenant_tag}/custom_ns">client.tenant_custom_nameservers.<a href="./src/cloudflare/resources/tenant_custom_nameservers/tenant_custom_nameservers.py">create</a>(tenant_tag, \*\*<a href="src/cloudflare/types/tenant_custom_nameservers/tenant_custom_nameserver_create_params.py">params</a>) -> <a href="./src/cloudflare/types/tenant_custom_nameservers/tenant_custom_nameserver_create_response.py">Optional[TenantCustomNameserverCreateResponse]</a></code>
- <code title="delete /tenants/{tenant_tag}/custom_ns/{custom_ns_id}">client.tenant_custom_nameservers.<a href="./src/cloudflare/resources/tenant_custom_nameservers/tenant_custom_nameservers.py">delete</a>(custom_ns_id, \*, tenant_tag) -> <a href="./src/cloudflare/types/tenant_custom_nameservers/tenant_custom_nameserver_delete_response.py">SyncSinglePage[TenantCustomNameserverDeleteResponse]</a></code>
- <code title="get /tenants/{tenant_tag}/custom_ns">client.tenant_custom_nameservers.<a href="./src/cloudflare/resources/tenant_custom_nameservers/tenant_custom_nameservers.py">get</a>(tenant_tag) -> <a href="./src/cloudflare/types/tenant_custom_nameservers/tenant_custom_nameserver_get_response.py">SyncSinglePage[TenantCustomNameserverGetResponse]</a></code>
