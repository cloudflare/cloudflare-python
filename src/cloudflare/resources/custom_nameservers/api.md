# CustomNameservers

Types:

```python
from cloudflare.types.custom_nameservers import CustomNameserver, CustomNameserverDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/custom_ns">client.custom_nameservers.<a href="./src/cloudflare/resources/custom_nameservers/custom_nameservers.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/custom_nameservers/custom_nameserver_create_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_nameservers/custom_nameserver.py">Optional[CustomNameserver]</a></code>
- <code title="delete /accounts/{account_id}/custom_ns/{custom_ns_id}">client.custom_nameservers.<a href="./src/cloudflare/resources/custom_nameservers/custom_nameservers.py">delete</a>(custom_ns_id, \*, account_id) -> <a href="./src/cloudflare/types/custom_nameservers/custom_nameserver_delete_response.py">SyncSinglePage[CustomNameserverDeleteResponse]</a></code>
- <code title="get /accounts/{account_id}/custom_ns">client.custom_nameservers.<a href="./src/cloudflare/resources/custom_nameservers/custom_nameservers.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/custom_nameservers/custom_nameserver.py">SyncSinglePage[CustomNameserver]</a></code>
