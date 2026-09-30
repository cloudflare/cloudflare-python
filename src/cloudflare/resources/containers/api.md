# Containers

## Applications

Types:

```python
from cloudflare.types.containers import (
    ApplicationCreateResponse,
    ApplicationListResponse,
    ApplicationDeleteResponse,
    ApplicationEditResponse,
    ApplicationGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/containers/applications">client.containers.applications.<a href="./src/cloudflare/resources/containers/applications/applications.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/containers/application_create_params.py">params</a>) -> <a href="./src/cloudflare/types/containers/application_create_response.py">ApplicationCreateResponse</a></code>
- <code title="get /accounts/{account_id}/containers/applications">client.containers.applications.<a href="./src/cloudflare/resources/containers/applications/applications.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/containers/application_list_params.py">params</a>) -> <a href="./src/cloudflare/types/containers/application_list_response.py">SyncPageTokenPagination[ApplicationListResponse]</a></code>
- <code title="delete /accounts/{account_id}/containers/applications/{application_id}">client.containers.applications.<a href="./src/cloudflare/resources/containers/applications/applications.py">delete</a>(application_id, \*, account_id) -> <a href="./src/cloudflare/types/containers/application_delete_response.py">ApplicationDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/containers/applications/{application_id}">client.containers.applications.<a href="./src/cloudflare/resources/containers/applications/applications.py">edit</a>(application_id, \*, account_id, \*\*<a href="src/cloudflare/types/containers/application_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/containers/application_edit_response.py">ApplicationEditResponse</a></code>
- <code title="get /accounts/{account_id}/containers/applications/{application_id}">client.containers.applications.<a href="./src/cloudflare/resources/containers/applications/applications.py">get</a>(application_id, \*, account_id) -> <a href="./src/cloudflare/types/containers/application_get_response.py">ApplicationGetResponse</a></code>

### Instances

Types:

```python
from cloudflare.types.containers.applications import (
    InstanceListResponse,
    InstanceGetResponse,
    InstanceListV1Response,
)
```

Methods:

- <code title="get /accounts/{account_id}/containers/applications/{application_id}/instances-v2">client.containers.applications.instances.<a href="./src/cloudflare/resources/containers/applications/instances.py">list</a>(application_id, \*, account_id, \*\*<a href="src/cloudflare/types/containers/applications/instance_list_params.py">params</a>) -> <a href="./src/cloudflare/types/containers/applications/instance_list_response.py">SyncPageTokenPagination[InstanceListResponse]</a></code>
- <code title="get /accounts/{account_id}/containers/applications/{application_id}/instances/{instance_id}">client.containers.applications.instances.<a href="./src/cloudflare/resources/containers/applications/instances.py">get</a>(instance_id, \*, account_id, application_id) -> <a href="./src/cloudflare/types/containers/applications/instance_get_response.py">InstanceGetResponse</a></code>
- <code title="get /accounts/{account_id}/containers/applications/{application_id}/instances">client.containers.applications.instances.<a href="./src/cloudflare/resources/containers/applications/instances.py">list_v1</a>(application_id, \*, account_id, \*\*<a href="src/cloudflare/types/containers/applications/instance_list_v1_params.py">params</a>) -> <a href="./src/cloudflare/types/containers/applications/instance_list_v1_response.py">SyncContainersInstancesV1Pagination[InstanceListV1Response]</a></code>

### Rollouts

Types:

```python
from cloudflare.types.containers.applications import RolloutCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/containers/applications/{application_id}/rollouts">client.containers.applications.rollouts.<a href="./src/cloudflare/resources/containers/applications/rollouts.py">create</a>(application_id, \*, account_id, \*\*<a href="src/cloudflare/types/containers/applications/rollout_create_params.py">params</a>) -> <a href="./src/cloudflare/types/containers/applications/rollout_create_response.py">RolloutCreateResponse</a></code>

### Versions

Types:

```python
from cloudflare.types.containers.applications import VersionListResponse
```

Methods:

- <code title="get /accounts/{account_id}/containers/applications/{application_id}/versions">client.containers.applications.versions.<a href="./src/cloudflare/resources/containers/applications/versions.py">list</a>(application_id, \*, account_id) -> <a href="./src/cloudflare/types/containers/applications/version_list_response.py">SyncSinglePage[VersionListResponse]</a></code>

## Images

Types:

```python
from cloudflare.types.containers import ImagePrepareResponse
```

Methods:

- <code title="post /accounts/{account_id}/containers/image-preparations">client.containers.images.<a href="./src/cloudflare/resources/containers/images.py">prepare</a>(\*, account_id, \*\*<a href="src/cloudflare/types/containers/image_prepare_params.py">params</a>) -> <a href="./src/cloudflare/types/containers/image_prepare_response.py">ImagePrepareResponse</a></code>

## Registries

Types:

```python
from cloudflare.types.containers import (
    RegistryCreateResponse,
    RegistryListResponse,
    RegistryDeleteResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/containers/registries">client.containers.registries.<a href="./src/cloudflare/resources/containers/registries/registries.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/containers/registry_create_params.py">params</a>) -> <a href="./src/cloudflare/types/containers/registry_create_response.py">RegistryCreateResponse</a></code>
- <code title="get /accounts/{account_id}/containers/registries">client.containers.registries.<a href="./src/cloudflare/resources/containers/registries/registries.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/containers/registry_list_response.py">SyncSinglePage[RegistryListResponse]</a></code>
- <code title="delete /accounts/{account_id}/containers/registries/{domain}">client.containers.registries.<a href="./src/cloudflare/resources/containers/registries/registries.py">delete</a>(domain, \*, account_id) -> <a href="./src/cloudflare/types/containers/registry_delete_response.py">RegistryDeleteResponse</a></code>

### Credentials

Types:

```python
from cloudflare.types.containers.registries import CredentialGenerateResponse
```

Methods:

- <code title="post /accounts/{account_id}/containers/registries/{domain}/credentials">client.containers.registries.credentials.<a href="./src/cloudflare/resources/containers/registries/credentials.py">generate</a>(domain, \*, account_id, \*\*<a href="src/cloudflare/types/containers/registries/credential_generate_params.py">params</a>) -> <a href="./src/cloudflare/types/containers/registries/credential_generate_response.py">CredentialGenerateResponse</a></code>
