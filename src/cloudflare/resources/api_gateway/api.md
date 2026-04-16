# APIGateway

## Configurations

Types:

```python
from cloudflare.types.api_gateway import Configuration
```

Methods:

- <code title="put /zones/{zone_id}/api_gateway/configuration">client.api_gateway.configurations.<a href="./src/cloudflare/resources/api_gateway/configurations.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/configuration_update_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/configuration.py">Configuration</a></code>
- <code title="get /zones/{zone_id}/api_gateway/configuration">client.api_gateway.configurations.<a href="./src/cloudflare/resources/api_gateway/configurations.py">get</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/configuration_get_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/configuration.py">Configuration</a></code>

## Discovery

Types:

```python
from cloudflare.types.api_gateway import DiscoveryOperation, DiscoveryGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/api_gateway/discovery">client.api_gateway.discovery.<a href="./src/cloudflare/resources/api_gateway/discovery/discovery.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/api_gateway/discovery_get_response.py">DiscoveryGetResponse</a></code>

### Operations

Types:

```python
from cloudflare.types.api_gateway.discovery import OperationBulkEditResponse, OperationEditResponse
```

Methods:

- <code title="get /zones/{zone_id}/api_gateway/discovery/operations">client.api_gateway.discovery.operations.<a href="./src/cloudflare/resources/api_gateway/discovery/operations.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/discovery/operation_list_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/discovery_operation.py">SyncV4PagePaginationArray[DiscoveryOperation]</a></code>
- <code title="patch /zones/{zone_id}/api_gateway/discovery/operations">client.api_gateway.discovery.operations.<a href="./src/cloudflare/resources/api_gateway/discovery/operations.py">bulk_edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/discovery/operation_bulk_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/discovery/operation_bulk_edit_response.py">OperationBulkEditResponse</a></code>
- <code title="patch /zones/{zone_id}/api_gateway/discovery/operations/{operation_id}">client.api_gateway.discovery.operations.<a href="./src/cloudflare/resources/api_gateway/discovery/operations.py">edit</a>(operation_id, \*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/discovery/operation_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/discovery/operation_edit_response.py">OperationEditResponse</a></code>

## Labels

Types:

```python
from cloudflare.types.api_gateway import LabelListResponse
```

Methods:

- <code title="get /zones/{zone_id}/api_gateway/labels">client.api_gateway.labels.<a href="./src/cloudflare/resources/api_gateway/labels/labels.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/label_list_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/label_list_response.py">SyncV4PagePaginationArray[LabelListResponse]</a></code>

### User

Types:

```python
from cloudflare.types.api_gateway.labels import (
    UserUpdateResponse,
    UserDeleteResponse,
    UserBulkCreateResponse,
    UserBulkDeleteResponse,
    UserEditResponse,
    UserGetResponse,
)
```

Methods:

- <code title="put /zones/{zone_id}/api_gateway/labels/user/{name}">client.api_gateway.labels.user.<a href="./src/cloudflare/resources/api_gateway/labels/user/user.py">update</a>(name, \*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/labels/user_update_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/labels/user_update_response.py">UserUpdateResponse</a></code>
- <code title="delete /zones/{zone_id}/api_gateway/labels/user/{name}">client.api_gateway.labels.user.<a href="./src/cloudflare/resources/api_gateway/labels/user/user.py">delete</a>(name, \*, zone_id) -> <a href="./src/cloudflare/types/api_gateway/labels/user_delete_response.py">UserDeleteResponse</a></code>
- <code title="post /zones/{zone_id}/api_gateway/labels/user">client.api_gateway.labels.user.<a href="./src/cloudflare/resources/api_gateway/labels/user/user.py">bulk_create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/labels/user_bulk_create_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/labels/user_bulk_create_response.py">SyncSinglePage[UserBulkCreateResponse]</a></code>
- <code title="delete /zones/{zone_id}/api_gateway/labels/user">client.api_gateway.labels.user.<a href="./src/cloudflare/resources/api_gateway/labels/user/user.py">bulk_delete</a>(\*, zone_id) -> <a href="./src/cloudflare/types/api_gateway/labels/user_bulk_delete_response.py">SyncSinglePage[UserBulkDeleteResponse]</a></code>
- <code title="patch /zones/{zone_id}/api_gateway/labels/user/{name}">client.api_gateway.labels.user.<a href="./src/cloudflare/resources/api_gateway/labels/user/user.py">edit</a>(name, \*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/labels/user_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/labels/user_edit_response.py">UserEditResponse</a></code>
- <code title="get /zones/{zone_id}/api_gateway/labels/user/{name}">client.api_gateway.labels.user.<a href="./src/cloudflare/resources/api_gateway/labels/user/user.py">get</a>(name, \*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/labels/user_get_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/labels/user_get_response.py">UserGetResponse</a></code>

#### Resources

##### Operation

Types:

```python
from cloudflare.types.api_gateway.labels.user.resources import OperationUpdateResponse
```

Methods:

- <code title="put /zones/{zone_id}/api_gateway/labels/user/{name}/resources/operation">client.api_gateway.labels.user.resources.operation.<a href="./src/cloudflare/resources/api_gateway/labels/user/resources/operation.py">update</a>(name, \*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/labels/user/resources/operation_update_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/labels/user/resources/operation_update_response.py">OperationUpdateResponse</a></code>

### Managed

Types:

```python
from cloudflare.types.api_gateway.labels import ManagedGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/api_gateway/labels/managed/{name}">client.api_gateway.labels.managed.<a href="./src/cloudflare/resources/api_gateway/labels/managed/managed.py">get</a>(name, \*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/labels/managed_get_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/labels/managed_get_response.py">ManagedGetResponse</a></code>

#### Resources

##### Operation

Types:

```python
from cloudflare.types.api_gateway.labels.managed.resources import OperationUpdateResponse
```

Methods:

- <code title="put /zones/{zone_id}/api_gateway/labels/managed/{name}/resources/operation">client.api_gateway.labels.managed.resources.operation.<a href="./src/cloudflare/resources/api_gateway/labels/managed/resources/operation.py">update</a>(name, \*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/labels/managed/resources/operation_update_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/labels/managed/resources/operation_update_response.py">OperationUpdateResponse</a></code>

## Operations

Types:

```python
from cloudflare.types.api_gateway import (
    APIShield,
    OperationCreateResponse,
    OperationListResponse,
    OperationDeleteResponse,
    OperationBulkCreateResponse,
    OperationBulkDeleteResponse,
    OperationGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/api_gateway/operations/item">client.api_gateway.operations.<a href="./src/cloudflare/resources/api_gateway/operations/operations.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/operation_create_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/operation_create_response.py">OperationCreateResponse</a></code>
- <code title="get /zones/{zone_id}/api_gateway/operations">client.api_gateway.operations.<a href="./src/cloudflare/resources/api_gateway/operations/operations.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/operation_list_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/operation_list_response.py">SyncV4PagePaginationArray[OperationListResponse]</a></code>
- <code title="delete /zones/{zone_id}/api_gateway/operations/{operation_id}">client.api_gateway.operations.<a href="./src/cloudflare/resources/api_gateway/operations/operations.py">delete</a>(operation_id, \*, zone_id) -> <a href="./src/cloudflare/types/api_gateway/operation_delete_response.py">OperationDeleteResponse</a></code>
- <code title="post /zones/{zone_id}/api_gateway/operations">client.api_gateway.operations.<a href="./src/cloudflare/resources/api_gateway/operations/operations.py">bulk_create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/operation_bulk_create_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/operation_bulk_create_response.py">SyncSinglePage[OperationBulkCreateResponse]</a></code>
- <code title="delete /zones/{zone_id}/api_gateway/operations">client.api_gateway.operations.<a href="./src/cloudflare/resources/api_gateway/operations/operations.py">bulk_delete</a>(\*, zone_id) -> <a href="./src/cloudflare/types/api_gateway/operation_bulk_delete_response.py">OperationBulkDeleteResponse</a></code>
- <code title="get /zones/{zone_id}/api_gateway/operations/{operation_id}">client.api_gateway.operations.<a href="./src/cloudflare/resources/api_gateway/operations/operations.py">get</a>(operation_id, \*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/operation_get_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/operation_get_response.py">OperationGetResponse</a></code>

### Labels

Types:

```python
from cloudflare.types.api_gateway.operations import (
    LabelCreateResponse,
    LabelUpdateResponse,
    LabelDeleteResponse,
    LabelBulkCreateResponse,
    LabelBulkDeleteResponse,
    LabelBulkUpdateResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/api_gateway/operations/{operation_id}/labels">client.api_gateway.operations.labels.<a href="./src/cloudflare/resources/api_gateway/operations/labels.py">create</a>(operation_id, \*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/operations/label_create_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/operations/label_create_response.py">LabelCreateResponse</a></code>
- <code title="put /zones/{zone_id}/api_gateway/operations/{operation_id}/labels">client.api_gateway.operations.labels.<a href="./src/cloudflare/resources/api_gateway/operations/labels.py">update</a>(operation_id, \*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/operations/label_update_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/operations/label_update_response.py">LabelUpdateResponse</a></code>
- <code title="delete /zones/{zone_id}/api_gateway/operations/{operation_id}/labels">client.api_gateway.operations.labels.<a href="./src/cloudflare/resources/api_gateway/operations/labels.py">delete</a>(operation_id, \*, zone_id) -> <a href="./src/cloudflare/types/api_gateway/operations/label_delete_response.py">LabelDeleteResponse</a></code>
- <code title="post /zones/{zone_id}/api_gateway/operations/labels">client.api_gateway.operations.labels.<a href="./src/cloudflare/resources/api_gateway/operations/labels.py">bulk_create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/operations/label_bulk_create_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/operations/label_bulk_create_response.py">SyncSinglePage[LabelBulkCreateResponse]</a></code>
- <code title="delete /zones/{zone_id}/api_gateway/operations/labels">client.api_gateway.operations.labels.<a href="./src/cloudflare/resources/api_gateway/operations/labels.py">bulk_delete</a>(\*, zone_id) -> <a href="./src/cloudflare/types/api_gateway/operations/label_bulk_delete_response.py">SyncSinglePage[LabelBulkDeleteResponse]</a></code>
- <code title="put /zones/{zone_id}/api_gateway/operations/labels">client.api_gateway.operations.labels.<a href="./src/cloudflare/resources/api_gateway/operations/labels.py">bulk_update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/operations/label_bulk_update_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/operations/label_bulk_update_response.py">SyncSinglePage[LabelBulkUpdateResponse]</a></code>

### SchemaValidation

Types:

```python
from cloudflare.types.api_gateway.operations import (
    SettingsMultipleRequest,
    SchemaValidationUpdateResponse,
    SchemaValidationGetResponse,
)
```

Methods:

- <code title="put /zones/{zone_id}/api_gateway/operations/{operation_id}/schema_validation">client.api_gateway.operations.schema_validation.<a href="./src/cloudflare/resources/api_gateway/operations/schema_validation.py">update</a>(operation_id, \*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/operations/schema_validation_update_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/operations/schema_validation_update_response.py">SchemaValidationUpdateResponse</a></code>
- <code title="patch /zones/{zone_id}/api_gateway/operations/schema_validation">client.api_gateway.operations.schema_validation.<a href="./src/cloudflare/resources/api_gateway/operations/schema_validation.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/operations/schema_validation_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/operations/settings_multiple_request.py">SettingsMultipleRequest</a></code>
- <code title="get /zones/{zone_id}/api_gateway/operations/{operation_id}/schema_validation">client.api_gateway.operations.schema_validation.<a href="./src/cloudflare/resources/api_gateway/operations/schema_validation.py">get</a>(operation_id, \*, zone_id) -> <a href="./src/cloudflare/types/api_gateway/operations/schema_validation_get_response.py">SchemaValidationGetResponse</a></code>

## Schemas

Types:

```python
from cloudflare.types.api_gateway import SchemaListResponse
```

Methods:

- <code title="get /zones/{zone_id}/api_gateway/schemas">client.api_gateway.schemas.<a href="./src/cloudflare/resources/api_gateway/schemas.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/schema_list_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/schema_list_response.py">SchemaListResponse</a></code>

## Settings

Types:

```python
from cloudflare.types.api_gateway import Settings
```

### SchemaValidation

Methods:

- <code title="put /zones/{zone_id}/api_gateway/settings/schema_validation">client.api_gateway.settings.schema_validation.<a href="./src/cloudflare/resources/api_gateway/settings/schema_validation.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/settings/schema_validation_update_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/settings/settings.py">Settings</a></code>
- <code title="patch /zones/{zone_id}/api_gateway/settings/schema_validation">client.api_gateway.settings.schema_validation.<a href="./src/cloudflare/resources/api_gateway/settings/schema_validation.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/settings/schema_validation_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/settings/settings.py">Settings</a></code>
- <code title="get /zones/{zone_id}/api_gateway/settings/schema_validation">client.api_gateway.settings.schema_validation.<a href="./src/cloudflare/resources/api_gateway/settings/schema_validation.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/api_gateway/settings/settings.py">Settings</a></code>

## UserSchemas

Types:

```python
from cloudflare.types.api_gateway import (
    Message,
    OldPublicSchema,
    UserSchemaCreateResponse,
    UserSchemaDeleteResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/api_gateway/user_schemas">client.api_gateway.user_schemas.<a href="./src/cloudflare/resources/api_gateway/user_schemas/user_schemas.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/user_schema_create_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/user_schema_create_response.py">UserSchemaCreateResponse</a></code>
- <code title="get /zones/{zone_id}/api_gateway/user_schemas">client.api_gateway.user_schemas.<a href="./src/cloudflare/resources/api_gateway/user_schemas/user_schemas.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/user_schema_list_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/old_public_schema.py">SyncV4PagePaginationArray[OldPublicSchema]</a></code>
- <code title="delete /zones/{zone_id}/api_gateway/user_schemas/{schema_id}">client.api_gateway.user_schemas.<a href="./src/cloudflare/resources/api_gateway/user_schemas/user_schemas.py">delete</a>(schema_id, \*, zone_id) -> <a href="./src/cloudflare/types/api_gateway/user_schema_delete_response.py">UserSchemaDeleteResponse</a></code>
- <code title="patch /zones/{zone_id}/api_gateway/user_schemas/{schema_id}">client.api_gateway.user_schemas.<a href="./src/cloudflare/resources/api_gateway/user_schemas/user_schemas.py">edit</a>(schema_id, \*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/user_schema_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/old_public_schema.py">OldPublicSchema</a></code>
- <code title="get /zones/{zone_id}/api_gateway/user_schemas/{schema_id}">client.api_gateway.user_schemas.<a href="./src/cloudflare/resources/api_gateway/user_schemas/user_schemas.py">get</a>(schema_id, \*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/user_schema_get_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/old_public_schema.py">OldPublicSchema</a></code>

### Operations

Types:

```python
from cloudflare.types.api_gateway.user_schemas import OperationListResponse
```

Methods:

- <code title="get /zones/{zone_id}/api_gateway/user_schemas/{schema_id}/operations">client.api_gateway.user_schemas.operations.<a href="./src/cloudflare/resources/api_gateway/user_schemas/operations.py">list</a>(schema_id, \*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/user_schemas/operation_list_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/user_schemas/operation_list_response.py">SyncV4PagePaginationArray[OperationListResponse]</a></code>

### Hosts

Types:

```python
from cloudflare.types.api_gateway.user_schemas import HostListResponse
```

Methods:

- <code title="get /zones/{zone_id}/api_gateway/user_schemas/hosts">client.api_gateway.user_schemas.hosts.<a href="./src/cloudflare/resources/api_gateway/user_schemas/hosts.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/user_schemas/host_list_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/user_schemas/host_list_response.py">SyncV4PagePaginationArray[HostListResponse]</a></code>

## ExpressionTemplate

### Fallthrough

Types:

```python
from cloudflare.types.api_gateway.expression_template import FallthroughCreateResponse
```

Methods:

- <code title="post /zones/{zone_id}/api_gateway/expression-template/fallthrough">client.api_gateway.expression_template.fallthrough.<a href="./src/cloudflare/resources/api_gateway/expression_template/fallthrough.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/expression_template/fallthrough_create_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/expression_template/fallthrough_create_response.py">FallthroughCreateResponse</a></code>
