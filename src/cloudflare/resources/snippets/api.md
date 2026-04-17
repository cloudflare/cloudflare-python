# Snippets

Types:

```python
from cloudflare.types.snippets import SnippetUpdateResponse, SnippetListResponse, SnippetGetResponse
```

Methods:

- <code title="put /zones/{zone_id}/snippets/{snippet_name}">client.snippets.<a href="./src/cloudflare/resources/snippets/snippets.py">update</a>(snippet_name, \*, zone_id, \*\*<a href="src/cloudflare/types/snippets/snippet_update_params.py">params</a>) -> <a href="./src/cloudflare/types/snippets/snippet_update_response.py">SnippetUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/snippets">client.snippets.<a href="./src/cloudflare/resources/snippets/snippets.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/snippets/snippet_list_params.py">params</a>) -> <a href="./src/cloudflare/types/snippets/snippet_list_response.py">SyncV4PagePaginationArray[SnippetListResponse]</a></code>
- <code title="delete /zones/{zone_id}/snippets/{snippet_name}">client.snippets.<a href="./src/cloudflare/resources/snippets/snippets.py">delete</a>(snippet_name, \*, zone_id) -> object</code>
- <code title="get /zones/{zone_id}/snippets/{snippet_name}">client.snippets.<a href="./src/cloudflare/resources/snippets/snippets.py">get</a>(snippet_name, \*, zone_id) -> <a href="./src/cloudflare/types/snippets/snippet_get_response.py">SnippetGetResponse</a></code>

## Content

Methods:

- <code title="get /zones/{zone_id}/snippets/{snippet_name}/content">client.snippets.content.<a href="./src/cloudflare/resources/snippets/content.py">get</a>(snippet_name, \*, zone_id) -> BinaryAPIResponse</code>

## Rules

Methods:

- <code title="put /zones/{zone_id}/snippets/snippet_rules">client.snippets.rules.<a href="./src/cloudflare/resources/snippets/rules.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/snippets/rule_update_params.py">params</a>) -> object</code>
- <code title="get /zones/{zone_id}/snippets/snippet_rules">client.snippets.rules.<a href="./src/cloudflare/resources/snippets/rules.py">list</a>(\*, zone_id) -> object</code>
- <code title="delete /zones/{zone_id}/snippets/snippet_rules">client.snippets.rules.<a href="./src/cloudflare/resources/snippets/rules.py">delete</a>(\*, zone_id) -> object</code>
