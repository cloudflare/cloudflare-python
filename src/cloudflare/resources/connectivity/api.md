# Connectivity

## Directory

### Services

Types:

```python
from cloudflare.types.connectivity.directory import (
    ServiceCreateResponse,
    ServiceUpdateResponse,
    ServiceListResponse,
    ServiceGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/connectivity/directory/services">client.connectivity.directory.services.<a href="./src/cloudflare/resources/connectivity/directory/services.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/connectivity/directory/service_create_params.py">params</a>) -> <a href="./src/cloudflare/types/connectivity/directory/service_create_response.py">Optional[ServiceCreateResponse]</a></code>
- <code title="put /accounts/{account_id}/connectivity/directory/services/{service_id}">client.connectivity.directory.services.<a href="./src/cloudflare/resources/connectivity/directory/services.py">update</a>(service_id, \*, account_id, \*\*<a href="src/cloudflare/types/connectivity/directory/service_update_params.py">params</a>) -> <a href="./src/cloudflare/types/connectivity/directory/service_update_response.py">Optional[ServiceUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/connectivity/directory/services">client.connectivity.directory.services.<a href="./src/cloudflare/resources/connectivity/directory/services.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/connectivity/directory/service_list_params.py">params</a>) -> <a href="./src/cloudflare/types/connectivity/directory/service_list_response.py">SyncV4PagePaginationArray[ServiceListResponse]</a></code>
- <code title="delete /accounts/{account_id}/connectivity/directory/services/{service_id}">client.connectivity.directory.services.<a href="./src/cloudflare/resources/connectivity/directory/services.py">delete</a>(service_id, \*, account_id) -> None</code>
- <code title="get /accounts/{account_id}/connectivity/directory/services/{service_id}">client.connectivity.directory.services.<a href="./src/cloudflare/resources/connectivity/directory/services.py">get</a>(service_id, \*, account_id) -> <a href="./src/cloudflare/types/connectivity/directory/service_get_response.py">Optional[ServiceGetResponse]</a></code>
