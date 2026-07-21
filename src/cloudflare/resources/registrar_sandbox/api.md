# RegistrarSandbox

Types:

```python
from cloudflare.types.registrar_sandbox import (
    Registration,
    WorkflowStatus,
    RegistrarSandboxCheckResponse,
    RegistrarSandboxSearchResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/registrar-sandbox/domain-check">client.registrar_sandbox.<a href="./src/cloudflare/resources/registrar_sandbox/registrar_sandbox.py">check</a>(\*, account_id, \*\*<a href="src/cloudflare/types/registrar_sandbox/registrar_sandbox_check_params.py">params</a>) -> <a href="./src/cloudflare/types/registrar_sandbox/registrar_sandbox_check_response.py">RegistrarSandboxCheckResponse</a></code>
- <code title="get /accounts/{account_id}/registrar-sandbox/domain-search">client.registrar_sandbox.<a href="./src/cloudflare/resources/registrar_sandbox/registrar_sandbox.py">search</a>(\*, account_id, \*\*<a href="src/cloudflare/types/registrar_sandbox/registrar_sandbox_search_params.py">params</a>) -> <a href="./src/cloudflare/types/registrar_sandbox/registrar_sandbox_search_response.py">RegistrarSandboxSearchResponse</a></code>

## Registrations

Types:

```python
from cloudflare.types.registrar_sandbox import (
    RegistrationCreateResponse,
    RegistrationListResponse,
    RegistrationEditResponse,
    RegistrationGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/registrar-sandbox/registrations">client.registrar_sandbox.registrations.<a href="./src/cloudflare/resources/registrar_sandbox/registrations.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/registrar_sandbox/registration_create_params.py">params</a>) -> <a href="./src/cloudflare/types/registrar_sandbox/registration_create_response.py">RegistrationCreateResponse</a></code>
- <code title="get /accounts/{account_id}/registrar-sandbox/registrations">client.registrar_sandbox.registrations.<a href="./src/cloudflare/resources/registrar_sandbox/registrations.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/registrar_sandbox/registration_list_params.py">params</a>) -> <a href="./src/cloudflare/types/registrar_sandbox/registration_list_response.py">SyncCursorPagination[RegistrationListResponse]</a></code>
- <code title="patch /accounts/{account_id}/registrar-sandbox/registrations/{domain_name}">client.registrar_sandbox.registrations.<a href="./src/cloudflare/resources/registrar_sandbox/registrations.py">edit</a>(domain_name, \*, account_id, \*\*<a href="src/cloudflare/types/registrar_sandbox/registration_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/registrar_sandbox/registration_edit_response.py">RegistrationEditResponse</a></code>
- <code title="get /accounts/{account_id}/registrar-sandbox/registrations/{domain_name}">client.registrar_sandbox.registrations.<a href="./src/cloudflare/resources/registrar_sandbox/registrations.py">get</a>(domain_name, \*, account_id) -> <a href="./src/cloudflare/types/registrar_sandbox/registration_get_response.py">RegistrationGetResponse</a></code>

## RegistrationStatus

Types:

```python
from cloudflare.types.registrar_sandbox import RegistrationStatusGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/registrar-sandbox/registrations/{domain_name}/registration-status">client.registrar_sandbox.registration_status.<a href="./src/cloudflare/resources/registrar_sandbox/registration_status.py">get</a>(domain_name, \*, account_id) -> <a href="./src/cloudflare/types/registrar_sandbox/registration_status_get_response.py">RegistrationStatusGetResponse</a></code>

## UpdateStatus

Types:

```python
from cloudflare.types.registrar_sandbox import UpdateStatusGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/registrar-sandbox/registrations/{domain_name}/update-status">client.registrar_sandbox.update_status.<a href="./src/cloudflare/resources/registrar_sandbox/update_status.py">get</a>(domain_name, \*, account_id) -> <a href="./src/cloudflare/types/registrar_sandbox/update_status_get_response.py">UpdateStatusGetResponse</a></code>
