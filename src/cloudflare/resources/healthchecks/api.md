# Healthchecks

Types:

```python
from cloudflare.types.healthchecks import (
    CheckRegion,
    Healthcheck,
    HTTPConfiguration,
    QueryHealthcheck,
    TCPConfiguration,
    HealthcheckDeleteResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/healthchecks">client.healthchecks.<a href="./src/cloudflare/resources/healthchecks/healthchecks.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/healthchecks/healthcheck_create_params.py">params</a>) -> <a href="./src/cloudflare/types/healthchecks/healthcheck.py">Healthcheck</a></code>
- <code title="put /zones/{zone_id}/healthchecks/{healthcheck_id}">client.healthchecks.<a href="./src/cloudflare/resources/healthchecks/healthchecks.py">update</a>(healthcheck_id, \*, zone_id, \*\*<a href="src/cloudflare/types/healthchecks/healthcheck_update_params.py">params</a>) -> <a href="./src/cloudflare/types/healthchecks/healthcheck.py">Healthcheck</a></code>
- <code title="get /zones/{zone_id}/healthchecks">client.healthchecks.<a href="./src/cloudflare/resources/healthchecks/healthchecks.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/healthchecks/healthcheck_list_params.py">params</a>) -> <a href="./src/cloudflare/types/healthchecks/healthcheck.py">SyncV4PagePaginationArray[Healthcheck]</a></code>
- <code title="delete /zones/{zone_id}/healthchecks/{healthcheck_id}">client.healthchecks.<a href="./src/cloudflare/resources/healthchecks/healthchecks.py">delete</a>(healthcheck_id, \*, zone_id) -> <a href="./src/cloudflare/types/healthchecks/healthcheck_delete_response.py">HealthcheckDeleteResponse</a></code>
- <code title="patch /zones/{zone_id}/healthchecks/{healthcheck_id}">client.healthchecks.<a href="./src/cloudflare/resources/healthchecks/healthchecks.py">edit</a>(healthcheck_id, \*, zone_id, \*\*<a href="src/cloudflare/types/healthchecks/healthcheck_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/healthchecks/healthcheck.py">Healthcheck</a></code>
- <code title="get /zones/{zone_id}/healthchecks/{healthcheck_id}">client.healthchecks.<a href="./src/cloudflare/resources/healthchecks/healthchecks.py">get</a>(healthcheck_id, \*, zone_id) -> <a href="./src/cloudflare/types/healthchecks/healthcheck.py">Healthcheck</a></code>

## Previews

Types:

```python
from cloudflare.types.healthchecks import PreviewDeleteResponse
```

Methods:

- <code title="post /zones/{zone_id}/healthchecks/preview">client.healthchecks.previews.<a href="./src/cloudflare/resources/healthchecks/previews.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/healthchecks/preview_create_params.py">params</a>) -> <a href="./src/cloudflare/types/healthchecks/healthcheck.py">Healthcheck</a></code>
- <code title="delete /zones/{zone_id}/healthchecks/preview/{healthcheck_id}">client.healthchecks.previews.<a href="./src/cloudflare/resources/healthchecks/previews.py">delete</a>(healthcheck_id, \*, zone_id) -> <a href="./src/cloudflare/types/healthchecks/preview_delete_response.py">PreviewDeleteResponse</a></code>
- <code title="get /zones/{zone_id}/healthchecks/preview/{healthcheck_id}">client.healthchecks.previews.<a href="./src/cloudflare/resources/healthchecks/previews.py">get</a>(healthcheck_id, \*, zone_id) -> <a href="./src/cloudflare/types/healthchecks/healthcheck.py">Healthcheck</a></code>
