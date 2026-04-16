# Diagnostics

## Traceroutes

Types:

```python
from cloudflare.types.diagnostics import Traceroute
```

Methods:

- <code title="post /accounts/{account_id}/diagnostics/traceroute">client.diagnostics.traceroutes.<a href="./src/cloudflare/resources/diagnostics/traceroutes.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/diagnostics/traceroute_create_params.py">params</a>) -> <a href="./src/cloudflare/types/diagnostics/traceroute.py">SyncSinglePage[Traceroute]</a></code>

## EndpointHealthchecks

Types:

```python
from cloudflare.types.diagnostics import (
    EndpointHealthcheck,
    EndpointHealthcheckCreateResponse,
    EndpointHealthcheckUpdateResponse,
    EndpointHealthcheckListResponse,
    EndpointHealthcheckDeleteResponse,
    EndpointHealthcheckGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/diagnostics/endpoint-healthchecks">client.diagnostics.endpoint_healthchecks.<a href="./src/cloudflare/resources/diagnostics/endpoint_healthchecks.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/diagnostics/endpoint_healthcheck_create_params.py">params</a>) -> <a href="./src/cloudflare/types/diagnostics/endpoint_healthcheck_create_response.py">Optional[EndpointHealthcheckCreateResponse]</a></code>
- <code title="put /accounts/{account_id}/diagnostics/endpoint-healthchecks/{id}">client.diagnostics.endpoint_healthchecks.<a href="./src/cloudflare/resources/diagnostics/endpoint_healthchecks.py">update</a>(id, \*, account_id, \*\*<a href="src/cloudflare/types/diagnostics/endpoint_healthcheck_update_params.py">params</a>) -> <a href="./src/cloudflare/types/diagnostics/endpoint_healthcheck_update_response.py">Optional[EndpointHealthcheckUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/diagnostics/endpoint-healthchecks">client.diagnostics.endpoint_healthchecks.<a href="./src/cloudflare/resources/diagnostics/endpoint_healthchecks.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/diagnostics/endpoint_healthcheck_list_response.py">Optional[EndpointHealthcheckListResponse]</a></code>
- <code title="delete /accounts/{account_id}/diagnostics/endpoint-healthchecks/{id}">client.diagnostics.endpoint_healthchecks.<a href="./src/cloudflare/resources/diagnostics/endpoint_healthchecks.py">delete</a>(id, \*, account_id) -> <a href="./src/cloudflare/types/diagnostics/endpoint_healthcheck_delete_response.py">EndpointHealthcheckDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/diagnostics/endpoint-healthchecks/{id}">client.diagnostics.endpoint_healthchecks.<a href="./src/cloudflare/resources/diagnostics/endpoint_healthchecks.py">get</a>(id, \*, account_id) -> <a href="./src/cloudflare/types/diagnostics/endpoint_healthcheck_get_response.py">Optional[EndpointHealthcheckGetResponse]</a></code>
