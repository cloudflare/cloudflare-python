# Calls

## SFU

Types:

```python
from cloudflare.types.calls import (
    SFUCreateResponse,
    SFUUpdateResponse,
    SFUListResponse,
    SFUDeleteResponse,
    SFUGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/calls/apps">client.calls.sfu.<a href="./src/cloudflare/resources/calls/sfu.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/calls/sfu_create_params.py">params</a>) -> <a href="./src/cloudflare/types/calls/sfu_create_response.py">Optional[SFUCreateResponse]</a></code>
- <code title="put /accounts/{account_id}/calls/apps/{app_id}">client.calls.sfu.<a href="./src/cloudflare/resources/calls/sfu.py">update</a>(app_id, \*, account_id, \*\*<a href="src/cloudflare/types/calls/sfu_update_params.py">params</a>) -> <a href="./src/cloudflare/types/calls/sfu_update_response.py">Optional[SFUUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/calls/apps">client.calls.sfu.<a href="./src/cloudflare/resources/calls/sfu.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/calls/sfu_list_response.py">SyncSinglePage[SFUListResponse]</a></code>
- <code title="delete /accounts/{account_id}/calls/apps/{app_id}">client.calls.sfu.<a href="./src/cloudflare/resources/calls/sfu.py">delete</a>(app_id, \*, account_id) -> <a href="./src/cloudflare/types/calls/sfu_delete_response.py">Optional[SFUDeleteResponse]</a></code>
- <code title="get /accounts/{account_id}/calls/apps/{app_id}">client.calls.sfu.<a href="./src/cloudflare/resources/calls/sfu.py">get</a>(app_id, \*, account_id) -> <a href="./src/cloudflare/types/calls/sfu_get_response.py">Optional[SFUGetResponse]</a></code>

## TURN

Types:

```python
from cloudflare.types.calls import (
    TURNCreateResponse,
    TURNUpdateResponse,
    TURNListResponse,
    TURNDeleteResponse,
    TURNGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/calls/turn_keys">client.calls.turn.<a href="./src/cloudflare/resources/calls/turn.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/calls/turn_create_params.py">params</a>) -> <a href="./src/cloudflare/types/calls/turn_create_response.py">Optional[TURNCreateResponse]</a></code>
- <code title="put /accounts/{account_id}/calls/turn_keys/{key_id}">client.calls.turn.<a href="./src/cloudflare/resources/calls/turn.py">update</a>(key_id, \*, account_id, \*\*<a href="src/cloudflare/types/calls/turn_update_params.py">params</a>) -> <a href="./src/cloudflare/types/calls/turn_update_response.py">Optional[TURNUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/calls/turn_keys">client.calls.turn.<a href="./src/cloudflare/resources/calls/turn.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/calls/turn_list_response.py">SyncSinglePage[TURNListResponse]</a></code>
- <code title="delete /accounts/{account_id}/calls/turn_keys/{key_id}">client.calls.turn.<a href="./src/cloudflare/resources/calls/turn.py">delete</a>(key_id, \*, account_id) -> <a href="./src/cloudflare/types/calls/turn_delete_response.py">Optional[TURNDeleteResponse]</a></code>
- <code title="get /accounts/{account_id}/calls/turn_keys/{key_id}">client.calls.turn.<a href="./src/cloudflare/resources/calls/turn.py">get</a>(key_id, \*, account_id) -> <a href="./src/cloudflare/types/calls/turn_get_response.py">Optional[TURNGetResponse]</a></code>
