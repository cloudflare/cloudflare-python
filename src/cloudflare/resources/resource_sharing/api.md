# ResourceSharing

Types:

```python
from cloudflare.types.resource_sharing import (
    ResourceSharingCreateResponse,
    ResourceSharingUpdateResponse,
    ResourceSharingListResponse,
    ResourceSharingDeleteResponse,
    ResourceSharingGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/shares">client.resource_sharing.<a href="./src/cloudflare/resources/resource_sharing/resource_sharing.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/resource_sharing/resource_sharing_create_params.py">params</a>) -> <a href="./src/cloudflare/types/resource_sharing/resource_sharing_create_response.py">Optional[ResourceSharingCreateResponse]</a></code>
- <code title="put /accounts/{account_id}/shares/{share_id}">client.resource_sharing.<a href="./src/cloudflare/resources/resource_sharing/resource_sharing.py">update</a>(share_id, \*, account_id, \*\*<a href="src/cloudflare/types/resource_sharing/resource_sharing_update_params.py">params</a>) -> <a href="./src/cloudflare/types/resource_sharing/resource_sharing_update_response.py">Optional[ResourceSharingUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/shares">client.resource_sharing.<a href="./src/cloudflare/resources/resource_sharing/resource_sharing.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/resource_sharing/resource_sharing_list_params.py">params</a>) -> <a href="./src/cloudflare/types/resource_sharing/resource_sharing_list_response.py">SyncV4PagePaginationArray[ResourceSharingListResponse]</a></code>
- <code title="delete /accounts/{account_id}/shares/{share_id}">client.resource_sharing.<a href="./src/cloudflare/resources/resource_sharing/resource_sharing.py">delete</a>(share_id, \*, account_id) -> <a href="./src/cloudflare/types/resource_sharing/resource_sharing_delete_response.py">Optional[ResourceSharingDeleteResponse]</a></code>
- <code title="get /accounts/{account_id}/shares/{share_id}">client.resource_sharing.<a href="./src/cloudflare/resources/resource_sharing/resource_sharing.py">get</a>(share_id, \*, account_id, \*\*<a href="src/cloudflare/types/resource_sharing/resource_sharing_get_params.py">params</a>) -> <a href="./src/cloudflare/types/resource_sharing/resource_sharing_get_response.py">Optional[ResourceSharingGetResponse]</a></code>

## Recipients

Types:

```python
from cloudflare.types.resource_sharing import (
    RecipientCreateResponse,
    RecipientListResponse,
    RecipientDeleteResponse,
    RecipientGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/shares/{share_id}/recipients">client.resource_sharing.recipients.<a href="./src/cloudflare/resources/resource_sharing/recipients.py">create</a>(share_id, \*, path_account_id, \*\*<a href="src/cloudflare/types/resource_sharing/recipient_create_params.py">params</a>) -> <a href="./src/cloudflare/types/resource_sharing/recipient_create_response.py">Optional[RecipientCreateResponse]</a></code>
- <code title="get /accounts/{account_id}/shares/{share_id}/recipients">client.resource_sharing.recipients.<a href="./src/cloudflare/resources/resource_sharing/recipients.py">list</a>(share_id, \*, account_id, \*\*<a href="src/cloudflare/types/resource_sharing/recipient_list_params.py">params</a>) -> <a href="./src/cloudflare/types/resource_sharing/recipient_list_response.py">SyncV4PagePaginationArray[RecipientListResponse]</a></code>
- <code title="delete /accounts/{account_id}/shares/{share_id}/recipients/{recipient_id}">client.resource_sharing.recipients.<a href="./src/cloudflare/resources/resource_sharing/recipients.py">delete</a>(recipient_id, \*, account_id, share_id) -> <a href="./src/cloudflare/types/resource_sharing/recipient_delete_response.py">Optional[RecipientDeleteResponse]</a></code>
- <code title="get /accounts/{account_id}/shares/{share_id}/recipients/{recipient_id}">client.resource_sharing.recipients.<a href="./src/cloudflare/resources/resource_sharing/recipients.py">get</a>(recipient_id, \*, account_id, share_id, \*\*<a href="src/cloudflare/types/resource_sharing/recipient_get_params.py">params</a>) -> <a href="./src/cloudflare/types/resource_sharing/recipient_get_response.py">Optional[RecipientGetResponse]</a></code>

## Resources

Types:

```python
from cloudflare.types.resource_sharing import (
    ResourceCreateResponse,
    ResourceUpdateResponse,
    ResourceListResponse,
    ResourceDeleteResponse,
    ResourceGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/shares/{share_id}/resources">client.resource_sharing.resources.<a href="./src/cloudflare/resources/resource_sharing/resources.py">create</a>(share_id, \*, account_id, \*\*<a href="src/cloudflare/types/resource_sharing/resource_create_params.py">params</a>) -> <a href="./src/cloudflare/types/resource_sharing/resource_create_response.py">Optional[ResourceCreateResponse]</a></code>
- <code title="put /accounts/{account_id}/shares/{share_id}/resources/{resource_id}">client.resource_sharing.resources.<a href="./src/cloudflare/resources/resource_sharing/resources.py">update</a>(resource_id, \*, account_id, share_id, \*\*<a href="src/cloudflare/types/resource_sharing/resource_update_params.py">params</a>) -> <a href="./src/cloudflare/types/resource_sharing/resource_update_response.py">Optional[ResourceUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/shares/{share_id}/resources">client.resource_sharing.resources.<a href="./src/cloudflare/resources/resource_sharing/resources.py">list</a>(share_id, \*, account_id, \*\*<a href="src/cloudflare/types/resource_sharing/resource_list_params.py">params</a>) -> <a href="./src/cloudflare/types/resource_sharing/resource_list_response.py">SyncV4PagePaginationArray[ResourceListResponse]</a></code>
- <code title="delete /accounts/{account_id}/shares/{share_id}/resources/{resource_id}">client.resource_sharing.resources.<a href="./src/cloudflare/resources/resource_sharing/resources.py">delete</a>(resource_id, \*, account_id, share_id) -> <a href="./src/cloudflare/types/resource_sharing/resource_delete_response.py">Optional[ResourceDeleteResponse]</a></code>
- <code title="get /accounts/{account_id}/shares/{share_id}/resources/{resource_id}">client.resource_sharing.resources.<a href="./src/cloudflare/resources/resource_sharing/resources.py">get</a>(resource_id, \*, account_id, share_id) -> <a href="./src/cloudflare/types/resource_sharing/resource_get_response.py">Optional[ResourceGetResponse]</a></code>
