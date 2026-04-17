# Queues

Types:

```python
from cloudflare.types.queues import Queue, QueueDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/queues">client.queues.<a href="./src/cloudflare/resources/queues/queues.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/queues/queue_create_params.py">params</a>) -> <a href="./src/cloudflare/types/queues/queue.py">Optional[Queue]</a></code>
- <code title="put /accounts/{account_id}/queues/{queue_id}">client.queues.<a href="./src/cloudflare/resources/queues/queues.py">update</a>(queue_id, \*, account_id, \*\*<a href="src/cloudflare/types/queues/queue_update_params.py">params</a>) -> <a href="./src/cloudflare/types/queues/queue.py">Optional[Queue]</a></code>
- <code title="get /accounts/{account_id}/queues">client.queues.<a href="./src/cloudflare/resources/queues/queues.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/queues/queue.py">SyncSinglePage[Queue]</a></code>
- <code title="delete /accounts/{account_id}/queues/{queue_id}">client.queues.<a href="./src/cloudflare/resources/queues/queues.py">delete</a>(queue_id, \*, account_id) -> <a href="./src/cloudflare/types/queues/queue_delete_response.py">QueueDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/queues/{queue_id}">client.queues.<a href="./src/cloudflare/resources/queues/queues.py">edit</a>(queue_id, \*, account_id, \*\*<a href="src/cloudflare/types/queues/queue_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/queues/queue.py">Optional[Queue]</a></code>
- <code title="get /accounts/{account_id}/queues/{queue_id}">client.queues.<a href="./src/cloudflare/resources/queues/queues.py">get</a>(queue_id, \*, account_id) -> <a href="./src/cloudflare/types/queues/queue.py">Optional[Queue]</a></code>

## Messages

Types:

```python
from cloudflare.types.queues import (
    MessageAckResponse,
    MessageBulkPushResponse,
    MessagePullResponse,
    MessagePushResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/queues/{queue_id}/messages/ack">client.queues.messages.<a href="./src/cloudflare/resources/queues/messages.py">ack</a>(queue_id, \*, account_id, \*\*<a href="src/cloudflare/types/queues/message_ack_params.py">params</a>) -> <a href="./src/cloudflare/types/queues/message_ack_response.py">Optional[MessageAckResponse]</a></code>
- <code title="post /accounts/{account_id}/queues/{queue_id}/messages/batch">client.queues.messages.<a href="./src/cloudflare/resources/queues/messages.py">bulk_push</a>(queue_id, \*, account_id, \*\*<a href="src/cloudflare/types/queues/message_bulk_push_params.py">params</a>) -> <a href="./src/cloudflare/types/queues/message_bulk_push_response.py">Optional[MessageBulkPushResponse]</a></code>
- <code title="post /accounts/{account_id}/queues/{queue_id}/messages/pull">client.queues.messages.<a href="./src/cloudflare/resources/queues/messages.py">pull</a>(queue_id, \*, account_id, \*\*<a href="src/cloudflare/types/queues/message_pull_params.py">params</a>) -> <a href="./src/cloudflare/types/queues/message_pull_response.py">Optional[MessagePullResponse]</a></code>
- <code title="post /accounts/{account_id}/queues/{queue_id}/messages">client.queues.messages.<a href="./src/cloudflare/resources/queues/messages.py">push</a>(queue_id, \*, account_id, \*\*<a href="src/cloudflare/types/queues/message_push_params.py">params</a>) -> <a href="./src/cloudflare/types/queues/message_push_response.py">Optional[MessagePushResponse]</a></code>

## Purge

Types:

```python
from cloudflare.types.queues import PurgeStatusResponse
```

Methods:

- <code title="post /accounts/{account_id}/queues/{queue_id}/purge">client.queues.purge.<a href="./src/cloudflare/resources/queues/purge.py">start</a>(queue_id, \*, account_id, \*\*<a href="src/cloudflare/types/queues/purge_start_params.py">params</a>) -> <a href="./src/cloudflare/types/queues/queue.py">Optional[Queue]</a></code>
- <code title="get /accounts/{account_id}/queues/{queue_id}/purge">client.queues.purge.<a href="./src/cloudflare/resources/queues/purge.py">status</a>(queue_id, \*, account_id) -> <a href="./src/cloudflare/types/queues/purge_status_response.py">Optional[PurgeStatusResponse]</a></code>

## Consumers

Types:

```python
from cloudflare.types.queues import Consumer, ConsumerDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/queues/{queue_id}/consumers">client.queues.consumers.<a href="./src/cloudflare/resources/queues/consumers.py">create</a>(queue_id, \*, account_id, \*\*<a href="src/cloudflare/types/queues/consumer_create_params.py">params</a>) -> <a href="./src/cloudflare/types/queues/consumer.py">Optional[Consumer]</a></code>
- <code title="put /accounts/{account_id}/queues/{queue_id}/consumers/{consumer_id}">client.queues.consumers.<a href="./src/cloudflare/resources/queues/consumers.py">update</a>(consumer_id, \*, account_id, queue_id, \*\*<a href="src/cloudflare/types/queues/consumer_update_params.py">params</a>) -> <a href="./src/cloudflare/types/queues/consumer.py">Optional[Consumer]</a></code>
- <code title="get /accounts/{account_id}/queues/{queue_id}/consumers">client.queues.consumers.<a href="./src/cloudflare/resources/queues/consumers.py">list</a>(queue_id, \*, account_id) -> <a href="./src/cloudflare/types/queues/consumer.py">SyncSinglePage[Consumer]</a></code>
- <code title="delete /accounts/{account_id}/queues/{queue_id}/consumers/{consumer_id}">client.queues.consumers.<a href="./src/cloudflare/resources/queues/consumers.py">delete</a>(consumer_id, \*, account_id, queue_id) -> <a href="./src/cloudflare/types/queues/consumer_delete_response.py">ConsumerDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/queues/{queue_id}/consumers/{consumer_id}">client.queues.consumers.<a href="./src/cloudflare/resources/queues/consumers.py">get</a>(consumer_id, \*, account_id, queue_id) -> <a href="./src/cloudflare/types/queues/consumer.py">Optional[Consumer]</a></code>

## Subscriptions

Types:

```python
from cloudflare.types.queues import (
    SubscriptionCreateResponse,
    SubscriptionUpdateResponse,
    SubscriptionListResponse,
    SubscriptionDeleteResponse,
    SubscriptionGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/event_subscriptions/subscriptions">client.queues.subscriptions.<a href="./src/cloudflare/resources/queues/subscriptions.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/queues/subscription_create_params.py">params</a>) -> <a href="./src/cloudflare/types/queues/subscription_create_response.py">Optional[SubscriptionCreateResponse]</a></code>
- <code title="patch /accounts/{account_id}/event_subscriptions/subscriptions/{subscription_id}">client.queues.subscriptions.<a href="./src/cloudflare/resources/queues/subscriptions.py">update</a>(subscription_id, \*, account_id, \*\*<a href="src/cloudflare/types/queues/subscription_update_params.py">params</a>) -> <a href="./src/cloudflare/types/queues/subscription_update_response.py">Optional[SubscriptionUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/event_subscriptions/subscriptions">client.queues.subscriptions.<a href="./src/cloudflare/resources/queues/subscriptions.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/queues/subscription_list_params.py">params</a>) -> <a href="./src/cloudflare/types/queues/subscription_list_response.py">SyncV4PagePaginationArray[SubscriptionListResponse]</a></code>
- <code title="delete /accounts/{account_id}/event_subscriptions/subscriptions/{subscription_id}">client.queues.subscriptions.<a href="./src/cloudflare/resources/queues/subscriptions.py">delete</a>(subscription_id, \*, account_id) -> <a href="./src/cloudflare/types/queues/subscription_delete_response.py">Optional[SubscriptionDeleteResponse]</a></code>
- <code title="get /accounts/{account_id}/event_subscriptions/subscriptions/{subscription_id}">client.queues.subscriptions.<a href="./src/cloudflare/resources/queues/subscriptions.py">get</a>(subscription_id, \*, account_id) -> <a href="./src/cloudflare/types/queues/subscription_get_response.py">Optional[SubscriptionGetResponse]</a></code>
