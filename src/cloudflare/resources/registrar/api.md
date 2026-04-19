# Registrar

Types:

```python
from cloudflare.types.registrar import (
    Registration,
    WorkflowStatus,
    RegistrarCheckResponse,
    RegistrarSearchResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/registrar/domain-check">client.registrar.<a href="./src/cloudflare/resources/registrar/registrar.py">check</a>(\*, account_id, \*\*<a href="src/cloudflare/types/registrar/registrar_check_params.py">params</a>) -> <a href="./src/cloudflare/types/registrar/registrar_check_response.py">RegistrarCheckResponse</a></code>
- <code title="get /accounts/{account_id}/registrar/domain-search">client.registrar.<a href="./src/cloudflare/resources/registrar/registrar.py">search</a>(\*, account_id, \*\*<a href="src/cloudflare/types/registrar/registrar_search_params.py">params</a>) -> <a href="./src/cloudflare/types/registrar/registrar_search_response.py">RegistrarSearchResponse</a></code>

## Domains

Types:

```python
from cloudflare.types.registrar import Domain
```

Methods:

- <code title="put /accounts/{account_id}/registrar/domains/{domain_name}">client.registrar.domains.<a href="./src/cloudflare/resources/registrar/domains.py">update</a>(domain_name, \*, account_id, \*\*<a href="src/cloudflare/types/registrar/domain_update_params.py">params</a>) -> object</code>
- <code title="get /accounts/{account_id}/registrar/domains">client.registrar.domains.<a href="./src/cloudflare/resources/registrar/domains.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/registrar/domain.py">SyncSinglePage[Domain]</a></code>
- <code title="get /accounts/{account_id}/registrar/domains/{domain_name}">client.registrar.domains.<a href="./src/cloudflare/resources/registrar/domains.py">get</a>(domain_name, \*, account_id) -> object</code>

## Registrations

Methods:

- <code title="post /accounts/{account_id}/registrar/registrations">client.registrar.registrations.<a href="./src/cloudflare/resources/registrar/registrations.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/registrar/registration_create_params.py">params</a>) -> <a href="./src/cloudflare/types/registrar/workflow_status.py">WorkflowStatus</a></code>
- <code title="get /accounts/{account_id}/registrar/registrations">client.registrar.registrations.<a href="./src/cloudflare/resources/registrar/registrations.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/registrar/registration_list_params.py">params</a>) -> <a href="./src/cloudflare/types/registrar/registration.py">SyncCursorPagination[Registration]</a></code>
- <code title="patch /accounts/{account_id}/registrar/registrations/{domain_name}">client.registrar.registrations.<a href="./src/cloudflare/resources/registrar/registrations.py">edit</a>(domain_name, \*, account_id, \*\*<a href="src/cloudflare/types/registrar/registration_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/registrar/workflow_status.py">WorkflowStatus</a></code>
- <code title="get /accounts/{account_id}/registrar/registrations/{domain_name}">client.registrar.registrations.<a href="./src/cloudflare/resources/registrar/registrations.py">get</a>(domain_name, \*, account_id) -> <a href="./src/cloudflare/types/registrar/registration.py">Registration</a></code>

## RegistrationStatus

Methods:

- <code title="get /accounts/{account_id}/registrar/registrations/{domain_name}/registration-status">client.registrar.registration_status.<a href="./src/cloudflare/resources/registrar/registration_status.py">get</a>(domain_name, \*, account_id) -> <a href="./src/cloudflare/types/registrar/workflow_status.py">WorkflowStatus</a></code>

## UpdateStatus

Methods:

- <code title="get /accounts/{account_id}/registrar/registrations/{domain_name}/update-status">client.registrar.update_status.<a href="./src/cloudflare/resources/registrar/update_status.py">get</a>(domain_name, \*, account_id) -> <a href="./src/cloudflare/types/registrar/workflow_status.py">WorkflowStatus</a></code>
