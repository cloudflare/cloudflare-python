# SecretsStore

## Stores

Types:

```python
from cloudflare.types.secrets_store import StoreCreateResponse, StoreListResponse
```

Methods:

- <code title="post /accounts/{account_id}/secrets_store/stores">client.secrets_store.stores.<a href="./src/cloudflare/resources/secrets_store/stores/stores.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/secrets_store/store_create_params.py">params</a>) -> <a href="./src/cloudflare/types/secrets_store/store_create_response.py">Optional[StoreCreateResponse]</a></code>
- <code title="get /accounts/{account_id}/secrets_store/stores">client.secrets_store.stores.<a href="./src/cloudflare/resources/secrets_store/stores/stores.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/secrets_store/store_list_params.py">params</a>) -> <a href="./src/cloudflare/types/secrets_store/store_list_response.py">SyncV4PagePaginationArray[StoreListResponse]</a></code>
- <code title="delete /accounts/{account_id}/secrets_store/stores/{store_id}">client.secrets_store.stores.<a href="./src/cloudflare/resources/secrets_store/stores/stores.py">delete</a>(store_id, \*, account_id) -> object</code>

### Secrets

Types:

```python
from cloudflare.types.secrets_store.stores import (
    SecretCreateResponse,
    SecretListResponse,
    SecretDuplicateResponse,
    SecretEditResponse,
    SecretGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/secrets_store/stores/{store_id}/secrets">client.secrets_store.stores.secrets.<a href="./src/cloudflare/resources/secrets_store/stores/secrets.py">create</a>(store_id, \*, account_id, \*\*<a href="src/cloudflare/types/secrets_store/stores/secret_create_params.py">params</a>) -> <a href="./src/cloudflare/types/secrets_store/stores/secret_create_response.py">SyncSinglePage[SecretCreateResponse]</a></code>
- <code title="get /accounts/{account_id}/secrets_store/stores/{store_id}/secrets">client.secrets_store.stores.secrets.<a href="./src/cloudflare/resources/secrets_store/stores/secrets.py">list</a>(store_id, \*, account_id, \*\*<a href="src/cloudflare/types/secrets_store/stores/secret_list_params.py">params</a>) -> <a href="./src/cloudflare/types/secrets_store/stores/secret_list_response.py">SyncV4PagePaginationArray[SecretListResponse]</a></code>
- <code title="delete /accounts/{account_id}/secrets_store/stores/{store_id}/secrets/{secret_id}">client.secrets_store.stores.secrets.<a href="./src/cloudflare/resources/secrets_store/stores/secrets.py">delete</a>(secret_id, \*, account_id, store_id) -> object</code>
- <code title="delete /accounts/{account_id}/secrets_store/stores/{store_id}/secrets">client.secrets_store.stores.secrets.<a href="./src/cloudflare/resources/secrets_store/stores/secrets.py">bulk_delete</a>(store_id, \*, account_id) -> object</code>
- <code title="post /accounts/{account_id}/secrets_store/stores/{store_id}/secrets/{secret_id}/duplicate">client.secrets_store.stores.secrets.<a href="./src/cloudflare/resources/secrets_store/stores/secrets.py">duplicate</a>(secret_id, \*, account_id, store_id, \*\*<a href="src/cloudflare/types/secrets_store/stores/secret_duplicate_params.py">params</a>) -> <a href="./src/cloudflare/types/secrets_store/stores/secret_duplicate_response.py">Optional[SecretDuplicateResponse]</a></code>
- <code title="patch /accounts/{account_id}/secrets_store/stores/{store_id}/secrets/{secret_id}">client.secrets_store.stores.secrets.<a href="./src/cloudflare/resources/secrets_store/stores/secrets.py">edit</a>(secret_id, \*, account_id, store_id, \*\*<a href="src/cloudflare/types/secrets_store/stores/secret_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/secrets_store/stores/secret_edit_response.py">Optional[SecretEditResponse]</a></code>
- <code title="get /accounts/{account_id}/secrets_store/stores/{store_id}/secrets/{secret_id}">client.secrets_store.stores.secrets.<a href="./src/cloudflare/resources/secrets_store/stores/secrets.py">get</a>(secret_id, \*, account_id, store_id) -> <a href="./src/cloudflare/types/secrets_store/stores/secret_get_response.py">Optional[SecretGetResponse]</a></code>

## Quota

Types:

```python
from cloudflare.types.secrets_store import QuotaGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/secrets_store/quota">client.secrets_store.quota.<a href="./src/cloudflare/resources/secrets_store/quota.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/secrets_store/quota_get_response.py">Optional[QuotaGetResponse]</a></code>
