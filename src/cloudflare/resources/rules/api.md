# Rules

## Lists

Types:

```python
from cloudflare.types.rules import (
    Hostname,
    ListsList,
    Redirect,
    ListCreateResponse,
    ListUpdateResponse,
    ListDeleteResponse,
    ListGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/rules/lists">client.rules.lists.<a href="./src/cloudflare/resources/rules/lists/lists.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/rules/list_create_params.py">params</a>) -> <a href="./src/cloudflare/types/rules/list_create_response.py">ListCreateResponse</a></code>
- <code title="put /accounts/{account_id}/rules/lists/{list_id}">client.rules.lists.<a href="./src/cloudflare/resources/rules/lists/lists.py">update</a>(list_id, \*, account_id, \*\*<a href="src/cloudflare/types/rules/list_update_params.py">params</a>) -> <a href="./src/cloudflare/types/rules/list_update_response.py">ListUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/rules/lists">client.rules.lists.<a href="./src/cloudflare/resources/rules/lists/lists.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/rules/lists_list.py">SyncSinglePage[ListsList]</a></code>
- <code title="delete /accounts/{account_id}/rules/lists/{list_id}">client.rules.lists.<a href="./src/cloudflare/resources/rules/lists/lists.py">delete</a>(list_id, \*, account_id) -> <a href="./src/cloudflare/types/rules/list_delete_response.py">ListDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/rules/lists/{list_id}">client.rules.lists.<a href="./src/cloudflare/resources/rules/lists/lists.py">get</a>(list_id, \*, account_id) -> <a href="./src/cloudflare/types/rules/list_get_response.py">ListGetResponse</a></code>

### BulkOperations

Types:

```python
from cloudflare.types.rules.lists import BulkOperationGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/rules/lists/bulk_operations/{operation_id}">client.rules.lists.bulk_operations.<a href="./src/cloudflare/resources/rules/lists/bulk_operations.py">get</a>(operation_id, \*, account_id) -> <a href="./src/cloudflare/types/rules/lists/bulk_operation_get_response.py">BulkOperationGetResponse</a></code>

### Items

Types:

```python
from cloudflare.types.rules.lists import (
    ListCursor,
    ListItem,
    ItemCreateResponse,
    ItemUpdateResponse,
    ItemListResponse,
    ItemDeleteResponse,
    ItemGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/rules/lists/{list_id}/items">client.rules.lists.items.<a href="./src/cloudflare/resources/rules/lists/items.py">create</a>(list_id, \*, account_id, \*\*<a href="src/cloudflare/types/rules/lists/item_create_params.py">params</a>) -> <a href="./src/cloudflare/types/rules/lists/item_create_response.py">ItemCreateResponse</a></code>
- <code title="put /accounts/{account_id}/rules/lists/{list_id}/items">client.rules.lists.items.<a href="./src/cloudflare/resources/rules/lists/items.py">update</a>(list_id, \*, account_id, \*\*<a href="src/cloudflare/types/rules/lists/item_update_params.py">params</a>) -> <a href="./src/cloudflare/types/rules/lists/item_update_response.py">ItemUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/rules/lists/{list_id}/items">client.rules.lists.items.<a href="./src/cloudflare/resources/rules/lists/items.py">list</a>(list_id, \*, account_id, \*\*<a href="src/cloudflare/types/rules/lists/item_list_params.py">params</a>) -> <a href="./src/cloudflare/types/rules/lists/item_list_response.py">SyncCursorPaginationAfter[ItemListResponse]</a></code>
- <code title="delete /accounts/{account_id}/rules/lists/{list_id}/items">client.rules.lists.items.<a href="./src/cloudflare/resources/rules/lists/items.py">delete</a>(list_id, \*, account_id, \*\*<a href="src/cloudflare/types/rules/lists/item_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/rules/lists/item_delete_response.py">ItemDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/rules/lists/{list_id}/items/{item_id}">client.rules.lists.items.<a href="./src/cloudflare/resources/rules/lists/items.py">get</a>(item_id, \*, account_id, list_id) -> <a href="./src/cloudflare/types/rules/lists/item_get_response.py">ItemGetResponse</a></code>
