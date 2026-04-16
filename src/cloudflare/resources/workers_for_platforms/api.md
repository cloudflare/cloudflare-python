# WorkersForPlatforms

## Dispatch

### Namespaces

Types:

```python
from cloudflare.types.workers_for_platforms.dispatch import (
    NamespaceCreateResponse,
    NamespaceListResponse,
    NamespaceGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/workers/dispatch/namespaces">client.workers_for_platforms.dispatch.namespaces.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/namespaces.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/workers_for_platforms/dispatch/namespace_create_params.py">params</a>) -> <a href="./src/cloudflare/types/workers_for_platforms/dispatch/namespace_create_response.py">Optional[NamespaceCreateResponse]</a></code>
- <code title="get /accounts/{account_id}/workers/dispatch/namespaces">client.workers_for_platforms.dispatch.namespaces.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/namespaces.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/workers_for_platforms/dispatch/namespace_list_response.py">SyncSinglePage[NamespaceListResponse]</a></code>
- <code title="delete /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}">client.workers_for_platforms.dispatch.namespaces.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/namespaces.py">delete</a>(dispatch_namespace, \*, account_id) -> object</code>
- <code title="get /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}">client.workers_for_platforms.dispatch.namespaces.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/namespaces.py">get</a>(dispatch_namespace, \*, account_id) -> <a href="./src/cloudflare/types/workers_for_platforms/dispatch/namespace_get_response.py">Optional[NamespaceGetResponse]</a></code>

#### Scripts

Types:

```python
from cloudflare.types.workers_for_platforms.dispatch.namespaces import Script, ScriptUpdateResponse
```

Methods:

- <code title="put /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}">client.workers_for_platforms.dispatch.namespaces.scripts.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/scripts.py">update</a>(script_name, \*, account_id, dispatch_namespace, \*\*<a href="src/cloudflare/types/workers_for_platforms/dispatch/namespaces/script_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers_for_platforms/dispatch/namespaces/script_update_response.py">ScriptUpdateResponse</a></code>
- <code title="delete /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}">client.workers_for_platforms.dispatch.namespaces.scripts.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/scripts.py">delete</a>(script_name, \*, account_id, dispatch_namespace, \*\*<a href="src/cloudflare/types/workers_for_platforms/dispatch/namespaces/script_delete_params.py">params</a>) -> object</code>
- <code title="get /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}">client.workers_for_platforms.dispatch.namespaces.scripts.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/scripts.py">get</a>(script_name, \*, account_id, dispatch_namespace) -> <a href="./src/cloudflare/types/workers_for_platforms/dispatch/namespaces/script.py">Script</a></code>

##### AssetUpload

Types:

```python
from cloudflare.types.workers_for_platforms.dispatch.namespaces.scripts import (
    AssetUploadCreateResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/assets-upload-session">client.workers_for_platforms.dispatch.namespaces.scripts.asset_upload.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/asset_upload.py">create</a>(script_name, \*, account_id, dispatch_namespace, \*\*<a href="src/cloudflare/types/workers_for_platforms/dispatch/namespaces/scripts/asset_upload_create_params.py">params</a>) -> <a href="./src/cloudflare/types/workers_for_platforms/dispatch/namespaces/scripts/asset_upload_create_response.py">Optional[AssetUploadCreateResponse]</a></code>

##### Content

Methods:

- <code title="put /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/content">client.workers_for_platforms.dispatch.namespaces.scripts.content.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/content.py">update</a>(script_name, \*, account_id, dispatch_namespace, \*\*<a href="src/cloudflare/types/workers_for_platforms/dispatch/namespaces/scripts/content_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/script.py">Script</a></code>
- <code title="get /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/content">client.workers_for_platforms.dispatch.namespaces.scripts.content.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/content.py">get</a>(script_name, \*, account_id, dispatch_namespace) -> BinaryAPIResponse</code>

##### Settings

Types:

```python
from cloudflare.types.workers_for_platforms.dispatch.namespaces.scripts import (
    SettingEditResponse,
    SettingGetResponse,
)
```

Methods:

- <code title="patch /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/settings">client.workers_for_platforms.dispatch.namespaces.scripts.settings.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/settings.py">edit</a>(script_name, \*, account_id, dispatch_namespace, \*\*<a href="src/cloudflare/types/workers_for_platforms/dispatch/namespaces/scripts/setting_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/workers_for_platforms/dispatch/namespaces/scripts/setting_edit_response.py">Optional[SettingEditResponse]</a></code>
- <code title="get /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/settings">client.workers_for_platforms.dispatch.namespaces.scripts.settings.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/settings.py">get</a>(script_name, \*, account_id, dispatch_namespace) -> <a href="./src/cloudflare/types/workers_for_platforms/dispatch/namespaces/scripts/setting_get_response.py">Optional[SettingGetResponse]</a></code>

##### Bindings

Types:

```python
from cloudflare.types.workers_for_platforms.dispatch.namespaces.scripts import BindingGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/bindings">client.workers_for_platforms.dispatch.namespaces.scripts.bindings.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/bindings.py">get</a>(script_name, \*, account_id, dispatch_namespace) -> <a href="./src/cloudflare/types/workers_for_platforms/dispatch/namespaces/scripts/binding_get_response.py">SyncSinglePage[BindingGetResponse]</a></code>

##### Secrets

Types:

```python
from cloudflare.types.workers_for_platforms.dispatch.namespaces.scripts import (
    SecretUpdateResponse,
    SecretListResponse,
    SecretGetResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/secrets">client.workers_for_platforms.dispatch.namespaces.scripts.secrets.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/secrets.py">update</a>(script_name, \*, account_id, dispatch_namespace, \*\*<a href="src/cloudflare/types/workers_for_platforms/dispatch/namespaces/scripts/secret_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers_for_platforms/dispatch/namespaces/scripts/secret_update_response.py">SecretUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/secrets">client.workers_for_platforms.dispatch.namespaces.scripts.secrets.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/secrets.py">list</a>(script_name, \*, account_id, dispatch_namespace) -> <a href="./src/cloudflare/types/workers_for_platforms/dispatch/namespaces/scripts/secret_list_response.py">SyncSinglePage[SecretListResponse]</a></code>
- <code title="delete /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/secrets/{secret_name}">client.workers_for_platforms.dispatch.namespaces.scripts.secrets.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/secrets.py">delete</a>(secret_name, \*, account_id, dispatch_namespace, script_name, \*\*<a href="src/cloudflare/types/workers_for_platforms/dispatch/namespaces/scripts/secret_delete_params.py">params</a>) -> object</code>
- <code title="get /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/secrets/{secret_name}">client.workers_for_platforms.dispatch.namespaces.scripts.secrets.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/secrets.py">get</a>(secret_name, \*, account_id, dispatch_namespace, script_name, \*\*<a href="src/cloudflare/types/workers_for_platforms/dispatch/namespaces/scripts/secret_get_params.py">params</a>) -> <a href="./src/cloudflare/types/workers_for_platforms/dispatch/namespaces/scripts/secret_get_response.py">SecretGetResponse</a></code>

##### Tags

Types:

```python
from cloudflare.types.workers_for_platforms.dispatch.namespaces.scripts import (
    TagUpdateResponse,
    TagListResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/tags">client.workers_for_platforms.dispatch.namespaces.scripts.tags.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/tags.py">update</a>(script_name, \*, account_id, dispatch_namespace, \*\*<a href="src/cloudflare/types/workers_for_platforms/dispatch/namespaces/scripts/tag_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers_for_platforms/dispatch/namespaces/scripts/tag_update_response.py">SyncSinglePage[TagUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/tags">client.workers_for_platforms.dispatch.namespaces.scripts.tags.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/tags.py">list</a>(script_name, \*, account_id, dispatch_namespace) -> <a href="./src/cloudflare/types/workers_for_platforms/dispatch/namespaces/scripts/tag_list_response.py">SyncSinglePage[TagListResponse]</a></code>
- <code title="delete /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/tags/{tag}">client.workers_for_platforms.dispatch.namespaces.scripts.tags.<a href="./src/cloudflare/resources/workers_for_platforms/dispatch/namespaces/scripts/tags.py">delete</a>(tag, \*, account_id, dispatch_namespace, script_name) -> object</code>
