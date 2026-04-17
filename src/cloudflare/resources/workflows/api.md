# Workflows

Types:

```python
from cloudflare.types.workflows import (
    WorkflowUpdateResponse,
    WorkflowListResponse,
    WorkflowDeleteResponse,
    WorkflowGetResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/workflows/{workflow_name}">client.workflows.<a href="./src/cloudflare/resources/workflows/workflows.py">update</a>(workflow_name, \*, account_id, \*\*<a href="src/cloudflare/types/workflows/workflow_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workflows/workflow_update_response.py">WorkflowUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/workflows">client.workflows.<a href="./src/cloudflare/resources/workflows/workflows.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/workflows/workflow_list_params.py">params</a>) -> <a href="./src/cloudflare/types/workflows/workflow_list_response.py">SyncV4PagePaginationArray[WorkflowListResponse]</a></code>
- <code title="delete /accounts/{account_id}/workflows/{workflow_name}">client.workflows.<a href="./src/cloudflare/resources/workflows/workflows.py">delete</a>(workflow_name, \*, account_id) -> <a href="./src/cloudflare/types/workflows/workflow_delete_response.py">WorkflowDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/workflows/{workflow_name}">client.workflows.<a href="./src/cloudflare/resources/workflows/workflows.py">get</a>(workflow_name, \*, account_id) -> <a href="./src/cloudflare/types/workflows/workflow_get_response.py">WorkflowGetResponse</a></code>

## Instances

Types:

```python
from cloudflare.types.workflows import (
    InstanceCreateResponse,
    InstanceListResponse,
    InstanceBulkResponse,
    InstanceGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/workflows/{workflow_name}/instances">client.workflows.instances.<a href="./src/cloudflare/resources/workflows/instances/instances.py">create</a>(workflow_name, \*, account_id, \*\*<a href="src/cloudflare/types/workflows/instance_create_params.py">params</a>) -> <a href="./src/cloudflare/types/workflows/instance_create_response.py">InstanceCreateResponse</a></code>
- <code title="get /accounts/{account_id}/workflows/{workflow_name}/instances">client.workflows.instances.<a href="./src/cloudflare/resources/workflows/instances/instances.py">list</a>(workflow_name, \*, account_id, \*\*<a href="src/cloudflare/types/workflows/instance_list_params.py">params</a>) -> <a href="./src/cloudflare/types/workflows/instance_list_response.py">SyncV4PagePaginationArray[InstanceListResponse]</a></code>
- <code title="post /accounts/{account_id}/workflows/{workflow_name}/instances/batch">client.workflows.instances.<a href="./src/cloudflare/resources/workflows/instances/instances.py">bulk</a>(workflow_name, \*, account_id, \*\*<a href="src/cloudflare/types/workflows/instance_bulk_params.py">params</a>) -> <a href="./src/cloudflare/types/workflows/instance_bulk_response.py">SyncSinglePage[InstanceBulkResponse]</a></code>
- <code title="get /accounts/{account_id}/workflows/{workflow_name}/instances/{instance_id}">client.workflows.instances.<a href="./src/cloudflare/resources/workflows/instances/instances.py">get</a>(instance_id, \*, account_id, workflow_name, \*\*<a href="src/cloudflare/types/workflows/instance_get_params.py">params</a>) -> <a href="./src/cloudflare/types/workflows/instance_get_response.py">InstanceGetResponse</a></code>

### Status

Types:

```python
from cloudflare.types.workflows.instances import StatusEditResponse
```

Methods:

- <code title="patch /accounts/{account_id}/workflows/{workflow_name}/instances/{instance_id}/status">client.workflows.instances.status.<a href="./src/cloudflare/resources/workflows/instances/status.py">edit</a>(instance_id, \*, account_id, workflow_name, \*\*<a href="src/cloudflare/types/workflows/instances/status_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/workflows/instances/status_edit_response.py">StatusEditResponse</a></code>

### Events

Methods:

- <code title="post /accounts/{account_id}/workflows/{workflow_name}/instances/{instance_id}/events/{event_type}">client.workflows.instances.events.<a href="./src/cloudflare/resources/workflows/instances/events.py">create</a>(event_type, \*, account_id, workflow_name, instance_id, \*\*<a href="src/cloudflare/types/workflows/instances/event_create_params.py">params</a>) -> object</code>

## Versions

Types:

```python
from cloudflare.types.workflows import VersionListResponse, VersionGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/workflows/{workflow_name}/versions">client.workflows.versions.<a href="./src/cloudflare/resources/workflows/versions.py">list</a>(workflow_name, \*, account_id, \*\*<a href="src/cloudflare/types/workflows/version_list_params.py">params</a>) -> <a href="./src/cloudflare/types/workflows/version_list_response.py">SyncV4PagePaginationArray[VersionListResponse]</a></code>
- <code title="get /accounts/{account_id}/workflows/{workflow_name}/versions/{version_id}">client.workflows.versions.<a href="./src/cloudflare/resources/workflows/versions.py">get</a>(version_id, \*, account_id, workflow_name) -> <a href="./src/cloudflare/types/workflows/version_get_response.py">VersionGetResponse</a></code>
