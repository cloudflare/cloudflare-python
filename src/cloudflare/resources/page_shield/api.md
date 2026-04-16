# PageShield

Types:

```python
from cloudflare.types.page_shield import Setting, PageShieldUpdateResponse
```

Methods:

- <code title="put /zones/{zone_id}/page_shield">client.page_shield.<a href="./src/cloudflare/resources/page_shield/page_shield.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/page_shield/page_shield_update_params.py">params</a>) -> <a href="./src/cloudflare/types/page_shield/page_shield_update_response.py">Optional[PageShieldUpdateResponse]</a></code>
- <code title="get /zones/{zone_id}/page_shield">client.page_shield.<a href="./src/cloudflare/resources/page_shield/page_shield.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/page_shield/setting.py">Optional[Setting]</a></code>

## Policies

Types:

```python
from cloudflare.types.page_shield import (
    Policy,
    PolicyCreateResponse,
    PolicyUpdateResponse,
    PolicyListResponse,
    PolicyGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/page_shield/policies">client.page_shield.policies.<a href="./src/cloudflare/resources/page_shield/policies.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/page_shield/policy_create_params.py">params</a>) -> <a href="./src/cloudflare/types/page_shield/policy_create_response.py">Optional[PolicyCreateResponse]</a></code>
- <code title="put /zones/{zone_id}/page_shield/policies/{policy_id}">client.page_shield.policies.<a href="./src/cloudflare/resources/page_shield/policies.py">update</a>(policy_id, \*, zone_id, \*\*<a href="src/cloudflare/types/page_shield/policy_update_params.py">params</a>) -> <a href="./src/cloudflare/types/page_shield/policy_update_response.py">Optional[PolicyUpdateResponse]</a></code>
- <code title="get /zones/{zone_id}/page_shield/policies">client.page_shield.policies.<a href="./src/cloudflare/resources/page_shield/policies.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/page_shield/policy_list_response.py">SyncSinglePage[PolicyListResponse]</a></code>
- <code title="delete /zones/{zone_id}/page_shield/policies/{policy_id}">client.page_shield.policies.<a href="./src/cloudflare/resources/page_shield/policies.py">delete</a>(policy_id, \*, zone_id) -> None</code>
- <code title="get /zones/{zone_id}/page_shield/policies/{policy_id}">client.page_shield.policies.<a href="./src/cloudflare/resources/page_shield/policies.py">get</a>(policy_id, \*, zone_id) -> <a href="./src/cloudflare/types/page_shield/policy_get_response.py">Optional[PolicyGetResponse]</a></code>

## Connections

Types:

```python
from cloudflare.types.page_shield import Connection
```

Methods:

- <code title="get /zones/{zone_id}/page_shield/connections">client.page_shield.connections.<a href="./src/cloudflare/resources/page_shield/connections.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/page_shield/connection_list_params.py">params</a>) -> <a href="./src/cloudflare/types/page_shield/connection.py">SyncSinglePage[Connection]</a></code>
- <code title="get /zones/{zone_id}/page_shield/connections/{connection_id}">client.page_shield.connections.<a href="./src/cloudflare/resources/page_shield/connections.py">get</a>(connection_id, \*, zone_id) -> <a href="./src/cloudflare/types/page_shield/connection.py">Optional[Connection]</a></code>

## Scripts

Types:

```python
from cloudflare.types.page_shield import Script, ScriptGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/page_shield/scripts">client.page_shield.scripts.<a href="./src/cloudflare/resources/page_shield/scripts.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/page_shield/script_list_params.py">params</a>) -> <a href="./src/cloudflare/types/page_shield/script.py">SyncSinglePage[Script]</a></code>
- <code title="get /zones/{zone_id}/page_shield/scripts/{script_id}">client.page_shield.scripts.<a href="./src/cloudflare/resources/page_shield/scripts.py">get</a>(script_id, \*, zone_id) -> <a href="./src/cloudflare/types/page_shield/script_get_response.py">Optional[ScriptGetResponse]</a></code>

## Cookies

Types:

```python
from cloudflare.types.page_shield import CookieListResponse, CookieGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/page_shield/cookies">client.page_shield.cookies.<a href="./src/cloudflare/resources/page_shield/cookies.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/page_shield/cookie_list_params.py">params</a>) -> <a href="./src/cloudflare/types/page_shield/cookie_list_response.py">SyncSinglePage[CookieListResponse]</a></code>
- <code title="get /zones/{zone_id}/page_shield/cookies/{cookie_id}">client.page_shield.cookies.<a href="./src/cloudflare/resources/page_shield/cookies.py">get</a>(cookie_id, \*, zone_id) -> <a href="./src/cloudflare/types/page_shield/cookie_get_response.py">Optional[CookieGetResponse]</a></code>
