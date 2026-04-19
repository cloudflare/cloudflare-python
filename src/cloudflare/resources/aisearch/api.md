# AISearch

## Namespaces

Types:

```python
from cloudflare.types.aisearch import (
    NamespaceCreateResponse,
    NamespaceUpdateResponse,
    NamespaceListResponse,
    NamespaceChatCompletionsResponse,
    NamespaceReadResponse,
    NamespaceSearchResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/ai-search/namespaces">client.aisearch.namespaces.<a href="./src/cloudflare/resources/aisearch/namespaces/namespaces.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/aisearch/namespace_create_params.py">params</a>) -> <a href="./src/cloudflare/types/aisearch/namespace_create_response.py">NamespaceCreateResponse</a></code>
- <code title="put /accounts/{account_id}/ai-search/namespaces/{name}">client.aisearch.namespaces.<a href="./src/cloudflare/resources/aisearch/namespaces/namespaces.py">update</a>(name, \*, account_id, \*\*<a href="src/cloudflare/types/aisearch/namespace_update_params.py">params</a>) -> <a href="./src/cloudflare/types/aisearch/namespace_update_response.py">NamespaceUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/ai-search/namespaces">client.aisearch.namespaces.<a href="./src/cloudflare/resources/aisearch/namespaces/namespaces.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/aisearch/namespace_list_params.py">params</a>) -> <a href="./src/cloudflare/types/aisearch/namespace_list_response.py">SyncV4PagePaginationArray[NamespaceListResponse]</a></code>
- <code title="delete /accounts/{account_id}/ai-search/namespaces/{name}">client.aisearch.namespaces.<a href="./src/cloudflare/resources/aisearch/namespaces/namespaces.py">delete</a>(name, \*, account_id) -> object</code>
- <code title="post /accounts/{account_id}/ai-search/namespaces/{name}/chat/completions">client.aisearch.namespaces.<a href="./src/cloudflare/resources/aisearch/namespaces/namespaces.py">chat_completions</a>(name, \*, account_id, \*\*<a href="src/cloudflare/types/aisearch/namespace_chat_completions_params.py">params</a>) -> <a href="./src/cloudflare/types/aisearch/namespace_chat_completions_response.py">NamespaceChatCompletionsResponse</a></code>
- <code title="get /accounts/{account_id}/ai-search/namespaces/{name}">client.aisearch.namespaces.<a href="./src/cloudflare/resources/aisearch/namespaces/namespaces.py">read</a>(name, \*, account_id) -> <a href="./src/cloudflare/types/aisearch/namespace_read_response.py">NamespaceReadResponse</a></code>
- <code title="post /accounts/{account_id}/ai-search/namespaces/{name}/search">client.aisearch.namespaces.<a href="./src/cloudflare/resources/aisearch/namespaces/namespaces.py">search</a>(name, \*, account_id, \*\*<a href="src/cloudflare/types/aisearch/namespace_search_params.py">params</a>) -> <a href="./src/cloudflare/types/aisearch/namespace_search_response.py">NamespaceSearchResponse</a></code>

### Instances

Types:

```python
from cloudflare.types.aisearch.namespaces import (
    InstanceCreateResponse,
    InstanceUpdateResponse,
    InstanceListResponse,
    InstanceDeleteResponse,
    InstanceChatCompletionsResponse,
    InstanceReadResponse,
    InstanceSearchResponse,
    InstanceStatsResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/ai-search/namespaces/{name}/instances">client.aisearch.namespaces.instances.<a href="./src/cloudflare/resources/aisearch/namespaces/instances/instances.py">create</a>(name, \*, account_id, \*\*<a href="src/cloudflare/types/aisearch/namespaces/instance_create_params.py">params</a>) -> <a href="./src/cloudflare/types/aisearch/namespaces/instance_create_response.py">InstanceCreateResponse</a></code>
- <code title="put /accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}">client.aisearch.namespaces.instances.<a href="./src/cloudflare/resources/aisearch/namespaces/instances/instances.py">update</a>(id, \*, account_id, name, \*\*<a href="src/cloudflare/types/aisearch/namespaces/instance_update_params.py">params</a>) -> <a href="./src/cloudflare/types/aisearch/namespaces/instance_update_response.py">InstanceUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/ai-search/namespaces/{name}/instances">client.aisearch.namespaces.instances.<a href="./src/cloudflare/resources/aisearch/namespaces/instances/instances.py">list</a>(name, \*, account_id, \*\*<a href="src/cloudflare/types/aisearch/namespaces/instance_list_params.py">params</a>) -> <a href="./src/cloudflare/types/aisearch/namespaces/instance_list_response.py">SyncV4PagePaginationArray[InstanceListResponse]</a></code>
- <code title="delete /accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}">client.aisearch.namespaces.instances.<a href="./src/cloudflare/resources/aisearch/namespaces/instances/instances.py">delete</a>(id, \*, account_id, name) -> <a href="./src/cloudflare/types/aisearch/namespaces/instance_delete_response.py">InstanceDeleteResponse</a></code>
- <code title="post /accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/chat/completions">client.aisearch.namespaces.instances.<a href="./src/cloudflare/resources/aisearch/namespaces/instances/instances.py">chat_completions</a>(id, \*, account_id, name, \*\*<a href="src/cloudflare/types/aisearch/namespaces/instance_chat_completions_params.py">params</a>) -> <a href="./src/cloudflare/types/aisearch/namespaces/instance_chat_completions_response.py">InstanceChatCompletionsResponse</a></code>
- <code title="get /accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}">client.aisearch.namespaces.instances.<a href="./src/cloudflare/resources/aisearch/namespaces/instances/instances.py">read</a>(id, \*, account_id, name) -> <a href="./src/cloudflare/types/aisearch/namespaces/instance_read_response.py">InstanceReadResponse</a></code>
- <code title="post /accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/search">client.aisearch.namespaces.instances.<a href="./src/cloudflare/resources/aisearch/namespaces/instances/instances.py">search</a>(id, \*, account_id, name, \*\*<a href="src/cloudflare/types/aisearch/namespaces/instance_search_params.py">params</a>) -> <a href="./src/cloudflare/types/aisearch/namespaces/instance_search_response.py">InstanceSearchResponse</a></code>
- <code title="get /accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/stats">client.aisearch.namespaces.instances.<a href="./src/cloudflare/resources/aisearch/namespaces/instances/instances.py">stats</a>(id, \*, account_id, name) -> <a href="./src/cloudflare/types/aisearch/namespaces/instance_stats_response.py">InstanceStatsResponse</a></code>

#### Jobs

Types:

```python
from cloudflare.types.aisearch.namespaces.instances import (
    JobCreateResponse,
    JobUpdateResponse,
    JobListResponse,
    JobGetResponse,
    JobLogsResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/jobs">client.aisearch.namespaces.instances.jobs.<a href="./src/cloudflare/resources/aisearch/namespaces/instances/jobs.py">create</a>(id, \*, account_id, name, \*\*<a href="src/cloudflare/types/aisearch/namespaces/instances/job_create_params.py">params</a>) -> <a href="./src/cloudflare/types/aisearch/namespaces/instances/job_create_response.py">JobCreateResponse</a></code>
- <code title="patch /accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/jobs/{job_id}">client.aisearch.namespaces.instances.jobs.<a href="./src/cloudflare/resources/aisearch/namespaces/instances/jobs.py">update</a>(job_id, \*, account_id, name, id, \*\*<a href="src/cloudflare/types/aisearch/namespaces/instances/job_update_params.py">params</a>) -> <a href="./src/cloudflare/types/aisearch/namespaces/instances/job_update_response.py">JobUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/jobs">client.aisearch.namespaces.instances.jobs.<a href="./src/cloudflare/resources/aisearch/namespaces/instances/jobs.py">list</a>(id, \*, account_id, name, \*\*<a href="src/cloudflare/types/aisearch/namespaces/instances/job_list_params.py">params</a>) -> <a href="./src/cloudflare/types/aisearch/namespaces/instances/job_list_response.py">SyncV4PagePaginationArray[JobListResponse]</a></code>
- <code title="get /accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/jobs/{job_id}">client.aisearch.namespaces.instances.jobs.<a href="./src/cloudflare/resources/aisearch/namespaces/instances/jobs.py">get</a>(job_id, \*, account_id, name, id) -> <a href="./src/cloudflare/types/aisearch/namespaces/instances/job_get_response.py">JobGetResponse</a></code>
- <code title="get /accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/jobs/{job_id}/logs">client.aisearch.namespaces.instances.jobs.<a href="./src/cloudflare/resources/aisearch/namespaces/instances/jobs.py">logs</a>(job_id, \*, account_id, name, id, \*\*<a href="src/cloudflare/types/aisearch/namespaces/instances/job_logs_params.py">params</a>) -> <a href="./src/cloudflare/types/aisearch/namespaces/instances/job_logs_response.py">JobLogsResponse</a></code>

#### Items

Types:

```python
from cloudflare.types.aisearch.namespaces.instances import (
    ItemListResponse,
    ItemDeleteResponse,
    ItemChunksResponse,
    ItemCreateOrUpdateResponse,
    ItemGetResponse,
    ItemLogsResponse,
    ItemSyncResponse,
    ItemUploadResponse,
)
```

Methods:

- <code title="get /accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items">client.aisearch.namespaces.instances.items.<a href="./src/cloudflare/resources/aisearch/namespaces/instances/items.py">list</a>(id, \*, account_id, name, \*\*<a href="src/cloudflare/types/aisearch/namespaces/instances/item_list_params.py">params</a>) -> <a href="./src/cloudflare/types/aisearch/namespaces/instances/item_list_response.py">SyncV4PagePaginationArray[ItemListResponse]</a></code>
- <code title="delete /accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items/{item_id}">client.aisearch.namespaces.instances.items.<a href="./src/cloudflare/resources/aisearch/namespaces/instances/items.py">delete</a>(item_id, \*, account_id, name, id) -> <a href="./src/cloudflare/types/aisearch/namespaces/instances/item_delete_response.py">ItemDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items/{item_id}/chunks">client.aisearch.namespaces.instances.items.<a href="./src/cloudflare/resources/aisearch/namespaces/instances/items.py">chunks</a>(item_id, \*, account_id, name, id, \*\*<a href="src/cloudflare/types/aisearch/namespaces/instances/item_chunks_params.py">params</a>) -> <a href="./src/cloudflare/types/aisearch/namespaces/instances/item_chunks_response.py">ItemChunksResponse</a></code>
- <code title="put /accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items">client.aisearch.namespaces.instances.items.<a href="./src/cloudflare/resources/aisearch/namespaces/instances/items.py">create_or_update</a>(id, \*, account_id, name, \*\*<a href="src/cloudflare/types/aisearch/namespaces/instances/item_create_or_update_params.py">params</a>) -> <a href="./src/cloudflare/types/aisearch/namespaces/instances/item_create_or_update_response.py">ItemCreateOrUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items/{item_id}/download">client.aisearch.namespaces.instances.items.<a href="./src/cloudflare/resources/aisearch/namespaces/instances/items.py">download</a>(item_id, \*, account_id, name, id) -> BinaryAPIResponse</code>
- <code title="get /accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items/{item_id}">client.aisearch.namespaces.instances.items.<a href="./src/cloudflare/resources/aisearch/namespaces/instances/items.py">get</a>(item_id, \*, account_id, name, id) -> <a href="./src/cloudflare/types/aisearch/namespaces/instances/item_get_response.py">ItemGetResponse</a></code>
- <code title="get /accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items/{item_id}/logs">client.aisearch.namespaces.instances.items.<a href="./src/cloudflare/resources/aisearch/namespaces/instances/items.py">logs</a>(item_id, \*, account_id, name, id, \*\*<a href="src/cloudflare/types/aisearch/namespaces/instances/item_logs_params.py">params</a>) -> <a href="./src/cloudflare/types/aisearch/namespaces/instances/item_logs_response.py">ItemLogsResponse</a></code>
- <code title="patch /accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items/{item_id}">client.aisearch.namespaces.instances.items.<a href="./src/cloudflare/resources/aisearch/namespaces/instances/items.py">sync</a>(item_id, \*, account_id, name, id, \*\*<a href="src/cloudflare/types/aisearch/namespaces/instances/item_sync_params.py">params</a>) -> <a href="./src/cloudflare/types/aisearch/namespaces/instances/item_sync_response.py">ItemSyncResponse</a></code>
- <code title="post /accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items">client.aisearch.namespaces.instances.items.<a href="./src/cloudflare/resources/aisearch/namespaces/instances/items.py">upload</a>(id, \*, account_id, name, \*\*<a href="src/cloudflare/types/aisearch/namespaces/instances/item_upload_params.py">params</a>) -> <a href="./src/cloudflare/types/aisearch/namespaces/instances/item_upload_response.py">ItemUploadResponse</a></code>

## Instances

Types:

```python
from cloudflare.types.aisearch import (
    InstanceCreateResponse,
    InstanceUpdateResponse,
    InstanceListResponse,
    InstanceDeleteResponse,
    InstanceChatCompletionsResponse,
    InstanceReadResponse,
    InstanceSearchResponse,
    InstanceStatsResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/ai-search/instances">client.aisearch.instances.<a href="./src/cloudflare/resources/aisearch/instances/instances.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/aisearch/instance_create_params.py">params</a>) -> <a href="./src/cloudflare/types/aisearch/instance_create_response.py">InstanceCreateResponse</a></code>
- <code title="put /accounts/{account_id}/ai-search/instances/{id}">client.aisearch.instances.<a href="./src/cloudflare/resources/aisearch/instances/instances.py">update</a>(id, \*, account_id, \*\*<a href="src/cloudflare/types/aisearch/instance_update_params.py">params</a>) -> <a href="./src/cloudflare/types/aisearch/instance_update_response.py">InstanceUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/ai-search/instances">client.aisearch.instances.<a href="./src/cloudflare/resources/aisearch/instances/instances.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/aisearch/instance_list_params.py">params</a>) -> <a href="./src/cloudflare/types/aisearch/instance_list_response.py">SyncV4PagePaginationArray[InstanceListResponse]</a></code>
- <code title="delete /accounts/{account_id}/ai-search/instances/{id}">client.aisearch.instances.<a href="./src/cloudflare/resources/aisearch/instances/instances.py">delete</a>(id, \*, account_id) -> <a href="./src/cloudflare/types/aisearch/instance_delete_response.py">InstanceDeleteResponse</a></code>
- <code title="post /accounts/{account_id}/ai-search/instances/{id}/chat/completions">client.aisearch.instances.<a href="./src/cloudflare/resources/aisearch/instances/instances.py">chat_completions</a>(id, \*, account_id, \*\*<a href="src/cloudflare/types/aisearch/instance_chat_completions_params.py">params</a>) -> <a href="./src/cloudflare/types/aisearch/instance_chat_completions_response.py">InstanceChatCompletionsResponse</a></code>
- <code title="get /accounts/{account_id}/ai-search/instances/{id}">client.aisearch.instances.<a href="./src/cloudflare/resources/aisearch/instances/instances.py">read</a>(id, \*, account_id) -> <a href="./src/cloudflare/types/aisearch/instance_read_response.py">InstanceReadResponse</a></code>
- <code title="post /accounts/{account_id}/ai-search/instances/{id}/search">client.aisearch.instances.<a href="./src/cloudflare/resources/aisearch/instances/instances.py">search</a>(id, \*, account_id, \*\*<a href="src/cloudflare/types/aisearch/instance_search_params.py">params</a>) -> <a href="./src/cloudflare/types/aisearch/instance_search_response.py">InstanceSearchResponse</a></code>
- <code title="get /accounts/{account_id}/ai-search/instances/{id}/stats">client.aisearch.instances.<a href="./src/cloudflare/resources/aisearch/instances/instances.py">stats</a>(id, \*, account_id) -> <a href="./src/cloudflare/types/aisearch/instance_stats_response.py">InstanceStatsResponse</a></code>

### Jobs

Types:

```python
from cloudflare.types.aisearch.instances import (
    JobCreateResponse,
    JobListResponse,
    JobGetResponse,
    JobLogsResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/ai-search/instances/{id}/jobs">client.aisearch.instances.jobs.<a href="./src/cloudflare/resources/aisearch/instances/jobs.py">create</a>(id, \*, account_id, \*\*<a href="src/cloudflare/types/aisearch/instances/job_create_params.py">params</a>) -> <a href="./src/cloudflare/types/aisearch/instances/job_create_response.py">JobCreateResponse</a></code>
- <code title="get /accounts/{account_id}/ai-search/instances/{id}/jobs">client.aisearch.instances.jobs.<a href="./src/cloudflare/resources/aisearch/instances/jobs.py">list</a>(id, \*, account_id, \*\*<a href="src/cloudflare/types/aisearch/instances/job_list_params.py">params</a>) -> <a href="./src/cloudflare/types/aisearch/instances/job_list_response.py">SyncV4PagePaginationArray[JobListResponse]</a></code>
- <code title="get /accounts/{account_id}/ai-search/instances/{id}/jobs/{job_id}">client.aisearch.instances.jobs.<a href="./src/cloudflare/resources/aisearch/instances/jobs.py">get</a>(job_id, \*, account_id, id) -> <a href="./src/cloudflare/types/aisearch/instances/job_get_response.py">JobGetResponse</a></code>
- <code title="get /accounts/{account_id}/ai-search/instances/{id}/jobs/{job_id}/logs">client.aisearch.instances.jobs.<a href="./src/cloudflare/resources/aisearch/instances/jobs.py">logs</a>(job_id, \*, account_id, id, \*\*<a href="src/cloudflare/types/aisearch/instances/job_logs_params.py">params</a>) -> <a href="./src/cloudflare/types/aisearch/instances/job_logs_response.py">JobLogsResponse</a></code>

## Tokens

Types:

```python
from cloudflare.types.aisearch import (
    TokenCreateResponse,
    TokenUpdateResponse,
    TokenListResponse,
    TokenReadResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/ai-search/tokens">client.aisearch.tokens.<a href="./src/cloudflare/resources/aisearch/tokens.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/aisearch/token_create_params.py">params</a>) -> <a href="./src/cloudflare/types/aisearch/token_create_response.py">TokenCreateResponse</a></code>
- <code title="put /accounts/{account_id}/ai-search/tokens/{id}">client.aisearch.tokens.<a href="./src/cloudflare/resources/aisearch/tokens.py">update</a>(id, \*, account_id, \*\*<a href="src/cloudflare/types/aisearch/token_update_params.py">params</a>) -> <a href="./src/cloudflare/types/aisearch/token_update_response.py">TokenUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/ai-search/tokens">client.aisearch.tokens.<a href="./src/cloudflare/resources/aisearch/tokens.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/aisearch/token_list_params.py">params</a>) -> <a href="./src/cloudflare/types/aisearch/token_list_response.py">SyncV4PagePaginationArray[TokenListResponse]</a></code>
- <code title="delete /accounts/{account_id}/ai-search/tokens/{id}">client.aisearch.tokens.<a href="./src/cloudflare/resources/aisearch/tokens.py">delete</a>(id, \*, account_id) -> object</code>
- <code title="get /accounts/{account_id}/ai-search/tokens/{id}">client.aisearch.tokens.<a href="./src/cloudflare/resources/aisearch/tokens.py">read</a>(id, \*, account_id) -> <a href="./src/cloudflare/types/aisearch/token_read_response.py">TokenReadResponse</a></code>
