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

### SchemaValidation

Types:

```python
from cloudflare.types.api_gateway.operations import (
    SchemaValidationUpdateResponse,
    SchemaValidationEditResponse,
    SchemaValidationGetResponse,
)
```

Methods:

- <code title="put /zones/{zone_id}/api_gateway/operations/{operation_id}/schema_validation">client.api_gateway.operations.schema_validation.<a href="./src/cloudflare/resources/api_gateway/operations/schema_validation.py">update</a>(operation_id, \*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/operations/schema_validation_update_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/operations/schema_validation_update_response.py">SchemaValidationUpdateResponse</a></code>
- <code title="patch /zones/{zone_id}/api_gateway/operations/schema_validation">client.api_gateway.operations.schema_validation.<a href="./src/cloudflare/resources/api_gateway/operations/schema_validation.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/operations/schema_validation_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/operations/schema_validation_edit_response.py">SchemaValidationEditResponse</a></code>
- <code title="get /zones/{zone_id}/api_gateway/operations/{operation_id}/schema_validation">client.api_gateway.operations.schema_validation.<a href="./src/cloudflare/resources/api_gateway/operations/schema_validation.py">get</a>(operation_id, \*, zone_id) -> <a href="./src/cloudflare/types/api_gateway/operations/schema_validation_get_response.py">SchemaValidationGetResponse</a></code>

## Schemas

Types:

```python
from cloudflare.types.api_gateway import SchemaListResponse
```

Methods:

- <code title="get /zones/{zone_id}/api_gateway/schemas">client.api_gateway.schemas.<a href="./src/cloudflare/resources/api_gateway/schemas.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/schema_list_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/schema_list_response.py">SchemaListResponse</a></code>

## Settings

### SchemaValidation

Types:

```python
from cloudflare.types.api_gateway.settings import (
    SchemaValidationUpdateResponse,
    SchemaValidationEditResponse,
    SchemaValidationGetResponse,
)
```

Methods:

- <code title="put /zones/{zone_id}/api_gateway/settings/schema_validation">client.api_gateway.settings.schema_validation.<a href="./src/cloudflare/resources/api_gateway/settings/schema_validation.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/settings/schema_validation_update_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/settings/schema_validation_update_response.py">SchemaValidationUpdateResponse</a></code>
- <code title="patch /zones/{zone_id}/api_gateway/settings/schema_validation">client.api_gateway.settings.schema_validation.<a href="./src/cloudflare/resources/api_gateway/settings/schema_validation.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/settings/schema_validation_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/settings/schema_validation_edit_response.py">SchemaValidationEditResponse</a></code>
- <code title="get /zones/{zone_id}/api_gateway/settings/schema_validation">client.api_gateway.settings.schema_validation.<a href="./src/cloudflare/resources/api_gateway/settings/schema_validation.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/api_gateway/settings/schema_validation_get_response.py">SchemaValidationGetResponse</a></code>

## UserSchemas

Types:

```python
from cloudflare.types.api_gateway import (
    Message,
    PublicSchema,
    UserSchemaCreateResponse,
    UserSchemaListResponse,
    UserSchemaDeleteResponse,
    UserSchemaEditResponse,
    UserSchemaGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/api_gateway/user_schemas">client.api_gateway.user_schemas.<a href="./src/cloudflare/resources/api_gateway/user_schemas/user_schemas.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/user_schema_create_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/user_schema_create_response.py">UserSchemaCreateResponse</a></code>
- <code title="get /zones/{zone_id}/api_gateway/user_schemas">client.api_gateway.user_schemas.<a href="./src/cloudflare/resources/api_gateway/user_schemas/user_schemas.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/user_schema_list_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/user_schema_list_response.py">SyncV4PagePaginationArray[UserSchemaListResponse]</a></code>
- <code title="delete /zones/{zone_id}/api_gateway/user_schemas/{schema_id}">client.api_gateway.user_schemas.<a href="./src/cloudflare/resources/api_gateway/user_schemas/user_schemas.py">delete</a>(schema_id, \*, zone_id) -> <a href="./src/cloudflare/types/api_gateway/user_schema_delete_response.py">UserSchemaDeleteResponse</a></code>
- <code title="patch /zones/{zone_id}/api_gateway/user_schemas/{schema_id}">client.api_gateway.user_schemas.<a href="./src/cloudflare/resources/api_gateway/user_schemas/user_schemas.py">edit</a>(schema_id, \*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/user_schema_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/user_schema_edit_response.py">UserSchemaEditResponse</a></code>
- <code title="get /zones/{zone_id}/api_gateway/user_schemas/{schema_id}">client.api_gateway.user_schemas.<a href="./src/cloudflare/resources/api_gateway/user_schemas/user_schemas.py">get</a>(schema_id, \*, zone_id, \*\*<a href="src/cloudflare/types/api_gateway/user_schema_get_params.py">params</a>) -> <a href="./src/cloudflare/types/api_gateway/user_schema_get_response.py">UserSchemaGetResponse</a></code>

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
