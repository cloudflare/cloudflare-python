# ResourceTagging

Types:

```python
from cloudflare.types.resource_tagging import ResourceTaggingListResponse
```

Methods:

- <code title="get /accounts/{account_id}/tags/resources">client.resource_tagging.<a href="./src/cloudflare/resources/resource_tagging/resource_tagging.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/resource_tagging/resource_tagging_list_params.py">params</a>) -> <a href="./src/cloudflare/types/resource_tagging/resource_tagging_list_response.py">SyncCursorPaginationAfter[ResourceTaggingListResponse]</a></code>

## AccountTags

Types:

```python
from cloudflare.types.resource_tagging import AccountTagUpdateResponse, AccountTagGetResponse
```

Methods:

- <code title="put /accounts/{account_id}/tags">client.resource_tagging.account_tags.<a href="./src/cloudflare/resources/resource_tagging/account_tags.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/resource_tagging/account_tag_update_params.py">params</a>) -> <a href="./src/cloudflare/types/resource_tagging/account_tag_update_response.py">Optional[AccountTagUpdateResponse]</a></code>
- <code title="delete /accounts/{account_id}/tags">client.resource_tagging.account_tags.<a href="./src/cloudflare/resources/resource_tagging/account_tags.py">delete</a>(\*, account_id) -> None</code>
- <code title="get /accounts/{account_id}/tags">client.resource_tagging.account_tags.<a href="./src/cloudflare/resources/resource_tagging/account_tags.py">get</a>(\*, account_id, \*\*<a href="src/cloudflare/types/resource_tagging/account_tag_get_params.py">params</a>) -> <a href="./src/cloudflare/types/resource_tagging/account_tag_get_response.py">Optional[AccountTagGetResponse]</a></code>

## ZoneTags

Types:

```python
from cloudflare.types.resource_tagging import ZoneTagUpdateResponse, ZoneTagGetResponse
```

Methods:

- <code title="put /zones/{zone_id}/tags">client.resource_tagging.zone_tags.<a href="./src/cloudflare/resources/resource_tagging/zone_tags.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/resource_tagging/zone_tag_update_params.py">params</a>) -> <a href="./src/cloudflare/types/resource_tagging/zone_tag_update_response.py">Optional[ZoneTagUpdateResponse]</a></code>
- <code title="delete /zones/{zone_id}/tags">client.resource_tagging.zone_tags.<a href="./src/cloudflare/resources/resource_tagging/zone_tags.py">delete</a>(\*, zone_id) -> None</code>
- <code title="get /zones/{zone_id}/tags">client.resource_tagging.zone_tags.<a href="./src/cloudflare/resources/resource_tagging/zone_tags.py">get</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/resource_tagging/zone_tag_get_params.py">params</a>) -> <a href="./src/cloudflare/types/resource_tagging/zone_tag_get_response.py">Optional[ZoneTagGetResponse]</a></code>

## Keys

Types:

```python
from cloudflare.types.resource_tagging import KeyListResponse
```

Methods:

- <code title="get /accounts/{account_id}/tags/keys">client.resource_tagging.keys.<a href="./src/cloudflare/resources/resource_tagging/keys.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/resource_tagging/key_list_params.py">params</a>) -> <a href="./src/cloudflare/types/resource_tagging/key_list_response.py">SyncCursorPaginationAfter[KeyListResponse]</a></code>

## Values

Types:

```python
from cloudflare.types.resource_tagging import ValueListResponse
```

Methods:

- <code title="get /accounts/{account_id}/tags/values/{tag_key}">client.resource_tagging.values.<a href="./src/cloudflare/resources/resource_tagging/values.py">list</a>(tag_key, \*, account_id, \*\*<a href="src/cloudflare/types/resource_tagging/value_list_params.py">params</a>) -> <a href="./src/cloudflare/types/resource_tagging/value_list_response.py">SyncCursorPaginationAfter[ValueListResponse]</a></code>
