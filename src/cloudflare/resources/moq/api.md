# MoQ

## Relays

Types:

```python
from cloudflare.types.moq import (
    RelayCreateResponse,
    RelayUpdateResponse,
    RelayListResponse,
    RelayGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/moq/relays">client.moq.relays.<a href="./src/cloudflare/resources/moq/relays/relays.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/moq/relay_create_params.py">params</a>) -> <a href="./src/cloudflare/types/moq/relay_create_response.py">Optional[RelayCreateResponse]</a></code>
- <code title="put /accounts/{account_id}/moq/relays/{relay_id}">client.moq.relays.<a href="./src/cloudflare/resources/moq/relays/relays.py">update</a>(relay_id, \*, account_id, \*\*<a href="src/cloudflare/types/moq/relay_update_params.py">params</a>) -> <a href="./src/cloudflare/types/moq/relay_update_response.py">Optional[RelayUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/moq/relays">client.moq.relays.<a href="./src/cloudflare/resources/moq/relays/relays.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/moq/relay_list_params.py">params</a>) -> <a href="./src/cloudflare/types/moq/relay_list_response.py">SyncSinglePage[RelayListResponse]</a></code>
- <code title="delete /accounts/{account_id}/moq/relays/{relay_id}">client.moq.relays.<a href="./src/cloudflare/resources/moq/relays/relays.py">delete</a>(relay_id, \*, account_id) -> object</code>
- <code title="get /accounts/{account_id}/moq/relays/{relay_id}">client.moq.relays.<a href="./src/cloudflare/resources/moq/relays/relays.py">get</a>(relay_id, \*, account_id) -> <a href="./src/cloudflare/types/moq/relay_get_response.py">Optional[RelayGetResponse]</a></code>

### Tokens

Types:

```python
from cloudflare.types.moq.relays import TokenCreateResponse, TokenListResponse, TokenDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/moq/relays/{relay_id}/tokens">client.moq.relays.tokens.<a href="./src/cloudflare/resources/moq/relays/tokens.py">create</a>(relay_id, \*, account_id, \*\*<a href="src/cloudflare/types/moq/relays/token_create_params.py">params</a>) -> <a href="./src/cloudflare/types/moq/relays/token_create_response.py">Optional[TokenCreateResponse]</a></code>
- <code title="get /accounts/{account_id}/moq/relays/{relay_id}/tokens">client.moq.relays.tokens.<a href="./src/cloudflare/resources/moq/relays/tokens.py">list</a>(relay_id, \*, account_id) -> <a href="./src/cloudflare/types/moq/relays/token_list_response.py">Optional[TokenListResponse]</a></code>
- <code title="delete /accounts/{account_id}/moq/relays/{relay_id}/tokens/{jti}">client.moq.relays.tokens.<a href="./src/cloudflare/resources/moq/relays/tokens.py">delete</a>(jti, \*, account_id, relay_id) -> <a href="./src/cloudflare/types/moq/relays/token_delete_response.py">TokenDeleteResponse</a></code>
