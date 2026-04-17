# Vectorize

## Indexes

Types:

```python
from cloudflare.types.vectorize import (
    CreateIndex,
    IndexDeleteVectorsByID,
    IndexDimensionConfiguration,
    IndexInsert,
    IndexQuery,
    IndexUpsert,
    IndexDeleteResponse,
    IndexDeleteByIDsResponse,
    IndexInfoResponse,
    IndexInsertResponse,
    IndexListVectorsResponse,
    IndexQueryResponse,
    IndexUpsertResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/vectorize/v2/indexes">client.vectorize.indexes.<a href="./src/cloudflare/resources/vectorize/indexes/indexes.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/vectorize/index_create_params.py">params</a>) -> <a href="./src/cloudflare/types/vectorize/create_index.py">Optional[CreateIndex]</a></code>
- <code title="get /accounts/{account_id}/vectorize/v2/indexes">client.vectorize.indexes.<a href="./src/cloudflare/resources/vectorize/indexes/indexes.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/vectorize/create_index.py">SyncSinglePage[CreateIndex]</a></code>
- <code title="delete /accounts/{account_id}/vectorize/v2/indexes/{index_name}">client.vectorize.indexes.<a href="./src/cloudflare/resources/vectorize/indexes/indexes.py">delete</a>(index_name, \*, account_id) -> <a href="./src/cloudflare/types/vectorize/index_delete_response.py">Optional[IndexDeleteResponse]</a></code>
- <code title="post /accounts/{account_id}/vectorize/v2/indexes/{index_name}/delete_by_ids">client.vectorize.indexes.<a href="./src/cloudflare/resources/vectorize/indexes/indexes.py">delete_by_ids</a>(index_name, \*, account_id, \*\*<a href="src/cloudflare/types/vectorize/index_delete_by_ids_params.py">params</a>) -> <a href="./src/cloudflare/types/vectorize/index_delete_by_ids_response.py">Optional[IndexDeleteByIDsResponse]</a></code>
- <code title="get /accounts/{account_id}/vectorize/v2/indexes/{index_name}">client.vectorize.indexes.<a href="./src/cloudflare/resources/vectorize/indexes/indexes.py">get</a>(index_name, \*, account_id) -> <a href="./src/cloudflare/types/vectorize/create_index.py">Optional[CreateIndex]</a></code>
- <code title="post /accounts/{account_id}/vectorize/v2/indexes/{index_name}/get_by_ids">client.vectorize.indexes.<a href="./src/cloudflare/resources/vectorize/indexes/indexes.py">get_by_ids</a>(index_name, \*, account_id, \*\*<a href="src/cloudflare/types/vectorize/index_get_by_ids_params.py">params</a>) -> object</code>
- <code title="get /accounts/{account_id}/vectorize/v2/indexes/{index_name}/info">client.vectorize.indexes.<a href="./src/cloudflare/resources/vectorize/indexes/indexes.py">info</a>(index_name, \*, account_id) -> <a href="./src/cloudflare/types/vectorize/index_info_response.py">Optional[IndexInfoResponse]</a></code>
- <code title="post /accounts/{account_id}/vectorize/v2/indexes/{index_name}/insert">client.vectorize.indexes.<a href="./src/cloudflare/resources/vectorize/indexes/indexes.py">insert</a>(index_name, \*, account_id, \*\*<a href="src/cloudflare/types/vectorize/index_insert_params.py">params</a>) -> <a href="./src/cloudflare/types/vectorize/index_insert_response.py">Optional[IndexInsertResponse]</a></code>
- <code title="get /accounts/{account_id}/vectorize/v2/indexes/{index_name}/list">client.vectorize.indexes.<a href="./src/cloudflare/resources/vectorize/indexes/indexes.py">list_vectors</a>(index_name, \*, account_id, \*\*<a href="src/cloudflare/types/vectorize/index_list_vectors_params.py">params</a>) -> <a href="./src/cloudflare/types/vectorize/index_list_vectors_response.py">Optional[IndexListVectorsResponse]</a></code>
- <code title="post /accounts/{account_id}/vectorize/v2/indexes/{index_name}/query">client.vectorize.indexes.<a href="./src/cloudflare/resources/vectorize/indexes/indexes.py">query</a>(index_name, \*, account_id, \*\*<a href="src/cloudflare/types/vectorize/index_query_params.py">params</a>) -> <a href="./src/cloudflare/types/vectorize/index_query_response.py">Optional[IndexQueryResponse]</a></code>
- <code title="post /accounts/{account_id}/vectorize/v2/indexes/{index_name}/upsert">client.vectorize.indexes.<a href="./src/cloudflare/resources/vectorize/indexes/indexes.py">upsert</a>(index_name, \*, account_id, \*\*<a href="src/cloudflare/types/vectorize/index_upsert_params.py">params</a>) -> <a href="./src/cloudflare/types/vectorize/index_upsert_response.py">Optional[IndexUpsertResponse]</a></code>

### MetadataIndex

Types:

```python
from cloudflare.types.vectorize.indexes import (
    MetadataIndexCreateResponse,
    MetadataIndexListResponse,
    MetadataIndexDeleteResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/vectorize/v2/indexes/{index_name}/metadata_index/create">client.vectorize.indexes.metadata_index.<a href="./src/cloudflare/resources/vectorize/indexes/metadata_index.py">create</a>(index_name, \*, account_id, \*\*<a href="src/cloudflare/types/vectorize/indexes/metadata_index_create_params.py">params</a>) -> <a href="./src/cloudflare/types/vectorize/indexes/metadata_index_create_response.py">Optional[MetadataIndexCreateResponse]</a></code>
- <code title="get /accounts/{account_id}/vectorize/v2/indexes/{index_name}/metadata_index/list">client.vectorize.indexes.metadata_index.<a href="./src/cloudflare/resources/vectorize/indexes/metadata_index.py">list</a>(index_name, \*, account_id) -> <a href="./src/cloudflare/types/vectorize/indexes/metadata_index_list_response.py">Optional[MetadataIndexListResponse]</a></code>
- <code title="post /accounts/{account_id}/vectorize/v2/indexes/{index_name}/metadata_index/delete">client.vectorize.indexes.metadata_index.<a href="./src/cloudflare/resources/vectorize/indexes/metadata_index.py">delete</a>(index_name, \*, account_id, \*\*<a href="src/cloudflare/types/vectorize/indexes/metadata_index_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/vectorize/indexes/metadata_index_delete_response.py">Optional[MetadataIndexDeleteResponse]</a></code>
