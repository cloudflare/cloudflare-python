# K2

## Streams

Types:

```python
from cloudflare.types.k2 import (
    StreamCreateResponse,
    StreamUpdateResponse,
    StreamListResponse,
    StreamGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/k2/streams">client.k2.streams.<a href="./src/cloudflare/resources/k2/streams/streams.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/k2/stream_create_params.py">params</a>) -> <a href="./src/cloudflare/types/k2/stream_create_response.py">StreamCreateResponse</a></code>
- <code title="patch /accounts/{account_id}/k2/streams/{stream_id}">client.k2.streams.<a href="./src/cloudflare/resources/k2/streams/streams.py">update</a>(stream_id, \*, account_id, \*\*<a href="src/cloudflare/types/k2/stream_update_params.py">params</a>) -> <a href="./src/cloudflare/types/k2/stream_update_response.py">StreamUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/k2/streams">client.k2.streams.<a href="./src/cloudflare/resources/k2/streams/streams.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/k2/stream_list_params.py">params</a>) -> <a href="./src/cloudflare/types/k2/stream_list_response.py">SyncV4PagePaginationArray[StreamListResponse]</a></code>
- <code title="delete /accounts/{account_id}/k2/streams/{stream_id}">client.k2.streams.<a href="./src/cloudflare/resources/k2/streams/streams.py">delete</a>(stream_id, \*, account_id) -> object</code>
- <code title="get /accounts/{account_id}/k2/streams/{stream_id}">client.k2.streams.<a href="./src/cloudflare/resources/k2/streams/streams.py">get</a>(stream_id, \*, account_id) -> <a href="./src/cloudflare/types/k2/stream_get_response.py">StreamGetResponse</a></code>

### Subscriptions

Types:

```python
from cloudflare.types.k2.streams import SubscriptionListResponse
```

Methods:

- <code title="get /accounts/{account_id}/k2/streams/{stream_id}/subscriptions">client.k2.streams.subscriptions.<a href="./src/cloudflare/resources/k2/streams/subscriptions.py">list</a>(stream_id, \*, account_id) -> <a href="./src/cloudflare/types/k2/streams/subscription_list_response.py">SyncSinglePage[SubscriptionListResponse]</a></code>
