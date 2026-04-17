# KV

## Namespaces

Types:

```python
from cloudflare.types.kv import (
    Namespace,
    NamespaceDeleteResponse,
    NamespaceBulkDeleteResponse,
    NamespaceBulkGetResponse,
    NamespaceBulkUpdateResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/storage/kv/namespaces">client.kv.namespaces.<a href="./src/cloudflare/resources/kv/namespaces/namespaces.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/kv/namespace_create_params.py">params</a>) -> <a href="./src/cloudflare/types/kv/namespace.py">Optional[Namespace]</a></code>
- <code title="put /accounts/{account_id}/storage/kv/namespaces/{namespace_id}">client.kv.namespaces.<a href="./src/cloudflare/resources/kv/namespaces/namespaces.py">update</a>(namespace_id, \*, account_id, \*\*<a href="src/cloudflare/types/kv/namespace_update_params.py">params</a>) -> <a href="./src/cloudflare/types/kv/namespace.py">Namespace</a></code>
- <code title="get /accounts/{account_id}/storage/kv/namespaces">client.kv.namespaces.<a href="./src/cloudflare/resources/kv/namespaces/namespaces.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/kv/namespace_list_params.py">params</a>) -> <a href="./src/cloudflare/types/kv/namespace.py">SyncV4PagePaginationArray[Namespace]</a></code>
- <code title="delete /accounts/{account_id}/storage/kv/namespaces/{namespace_id}">client.kv.namespaces.<a href="./src/cloudflare/resources/kv/namespaces/namespaces.py">delete</a>(namespace_id, \*, account_id) -> <a href="./src/cloudflare/types/kv/namespace_delete_response.py">Optional[NamespaceDeleteResponse]</a></code>
- <code title="post /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk/delete">client.kv.namespaces.<a href="./src/cloudflare/resources/kv/namespaces/namespaces.py">bulk_delete</a>(namespace_id, \*, account_id, \*\*<a href="src/cloudflare/types/kv/namespace_bulk_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/kv/namespace_bulk_delete_response.py">Optional[NamespaceBulkDeleteResponse]</a></code>
- <code title="post /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk/get">client.kv.namespaces.<a href="./src/cloudflare/resources/kv/namespaces/namespaces.py">bulk_get</a>(namespace_id, \*, account_id, \*\*<a href="src/cloudflare/types/kv/namespace_bulk_get_params.py">params</a>) -> <a href="./src/cloudflare/types/kv/namespace_bulk_get_response.py">Optional[NamespaceBulkGetResponse]</a></code>
- <code title="put /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk">client.kv.namespaces.<a href="./src/cloudflare/resources/kv/namespaces/namespaces.py">bulk_update</a>(namespace_id, \*, account_id, \*\*<a href="src/cloudflare/types/kv/namespace_bulk_update_params.py">params</a>) -> <a href="./src/cloudflare/types/kv/namespace_bulk_update_response.py">Optional[NamespaceBulkUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/storage/kv/namespaces/{namespace_id}">client.kv.namespaces.<a href="./src/cloudflare/resources/kv/namespaces/namespaces.py">get</a>(namespace_id, \*, account_id) -> <a href="./src/cloudflare/types/kv/namespace.py">Optional[Namespace]</a></code>

### Keys

Types:

```python
from cloudflare.types.kv.namespaces import (
    Key,
    KeyBulkDeleteResponse,
    KeyBulkGetResponse,
    KeyBulkUpdateResponse,
)
```

Methods:

- <code title="get /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/keys">client.kv.namespaces.keys.<a href="./src/cloudflare/resources/kv/namespaces/keys.py">list</a>(namespace_id, \*, account_id, \*\*<a href="src/cloudflare/types/kv/namespaces/key_list_params.py">params</a>) -> <a href="./src/cloudflare/types/kv/namespaces/key.py">SyncCursorLimitPagination[Key]</a></code>
- <code title="post /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk/delete">client.kv.namespaces.keys.<a href="./src/cloudflare/resources/kv/namespaces/keys.py">bulk_delete</a>(namespace_id, \*, account_id, \*\*<a href="src/cloudflare/types/kv/namespaces/key_bulk_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/kv/namespaces/key_bulk_delete_response.py">Optional[KeyBulkDeleteResponse]</a></code>
- <code title="post /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk/get">client.kv.namespaces.keys.<a href="./src/cloudflare/resources/kv/namespaces/keys.py">bulk_get</a>(namespace_id, \*, account_id, \*\*<a href="src/cloudflare/types/kv/namespaces/key_bulk_get_params.py">params</a>) -> <a href="./src/cloudflare/types/kv/namespaces/key_bulk_get_response.py">Optional[KeyBulkGetResponse]</a></code>
- <code title="put /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk">client.kv.namespaces.keys.<a href="./src/cloudflare/resources/kv/namespaces/keys.py">bulk_update</a>(namespace_id, \*, account_id, \*\*<a href="src/cloudflare/types/kv/namespaces/key_bulk_update_params.py">params</a>) -> <a href="./src/cloudflare/types/kv/namespaces/key_bulk_update_response.py">Optional[KeyBulkUpdateResponse]</a></code>

### Metadata

Methods:

- <code title="get /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/metadata/{key_name}">client.kv.namespaces.metadata.<a href="./src/cloudflare/resources/kv/namespaces/metadata.py">get</a>(key_name, \*, account_id, namespace_id) -> object</code>

### Values

Types:

```python
from cloudflare.types.kv.namespaces import ValueUpdateResponse, ValueDeleteResponse
```

Methods:

- <code title="put /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}">client.kv.namespaces.values.<a href="./src/cloudflare/resources/kv/namespaces/values.py">update</a>(key_name, \*, account_id, namespace_id, \*\*<a href="src/cloudflare/types/kv/namespaces/value_update_params.py">params</a>) -> <a href="./src/cloudflare/types/kv/namespaces/value_update_response.py">Optional[ValueUpdateResponse]</a></code>
- <code title="delete /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}">client.kv.namespaces.values.<a href="./src/cloudflare/resources/kv/namespaces/values.py">delete</a>(key_name, \*, account_id, namespace_id) -> <a href="./src/cloudflare/types/kv/namespaces/value_delete_response.py">Optional[ValueDeleteResponse]</a></code>
- <code title="get /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}">client.kv.namespaces.values.<a href="./src/cloudflare/resources/kv/namespaces/values.py">get</a>(key_name, \*, account_id, namespace_id) -> BinaryAPIResponse</code>
