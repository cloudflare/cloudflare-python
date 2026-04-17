# DurableObjects

## Namespaces

Types:

```python
from cloudflare.types.durable_objects import Namespace
```

Methods:

- <code title="get /accounts/{account_id}/workers/durable_objects/namespaces">client.durable_objects.namespaces.<a href="./src/cloudflare/resources/durable_objects/namespaces/namespaces.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/durable_objects/namespace_list_params.py">params</a>) -> <a href="./src/cloudflare/types/durable_objects/namespace.py">SyncV4PagePaginationArray[Namespace]</a></code>

### Objects

Types:

```python
from cloudflare.types.durable_objects.namespaces import DurableObject
```

Methods:

- <code title="get /accounts/{account_id}/workers/durable_objects/namespaces/{id}/objects">client.durable_objects.namespaces.objects.<a href="./src/cloudflare/resources/durable_objects/namespaces/objects.py">list</a>(id, \*, account_id, \*\*<a href="src/cloudflare/types/durable_objects/namespaces/object_list_params.py">params</a>) -> <a href="./src/cloudflare/types/durable_objects/namespaces/durable_object.py">SyncCursorPaginationAfter[DurableObject]</a></code>
