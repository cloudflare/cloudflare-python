# SchemaValidation

## Schemas

Types:

```python
from cloudflare.types.schema_validation import PublicSchema, SchemaDeleteResponse
```

Methods:

- <code title="post /zones/{zone_id}/schema_validation/schemas">client.schema_validation.schemas.<a href="./src/cloudflare/resources/schema_validation/schemas.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/schema_validation/schema_create_params.py">params</a>) -> <a href="./src/cloudflare/types/schema_validation/public_schema.py">PublicSchema</a></code>
- <code title="get /zones/{zone_id}/schema_validation/schemas">client.schema_validation.schemas.<a href="./src/cloudflare/resources/schema_validation/schemas.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/schema_validation/schema_list_params.py">params</a>) -> <a href="./src/cloudflare/types/schema_validation/public_schema.py">SyncV4PagePaginationArray[PublicSchema]</a></code>
- <code title="delete /zones/{zone_id}/schema_validation/schemas/{schema_id}">client.schema_validation.schemas.<a href="./src/cloudflare/resources/schema_validation/schemas.py">delete</a>(schema_id, \*, zone_id) -> <a href="./src/cloudflare/types/schema_validation/schema_delete_response.py">SchemaDeleteResponse</a></code>
- <code title="patch /zones/{zone_id}/schema_validation/schemas/{schema_id}">client.schema_validation.schemas.<a href="./src/cloudflare/resources/schema_validation/schemas.py">edit</a>(schema_id, \*, zone_id, \*\*<a href="src/cloudflare/types/schema_validation/schema_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/schema_validation/public_schema.py">PublicSchema</a></code>
- <code title="get /zones/{zone_id}/schema_validation/schemas/{schema_id}">client.schema_validation.schemas.<a href="./src/cloudflare/resources/schema_validation/schemas.py">get</a>(schema_id, \*, zone_id, \*\*<a href="src/cloudflare/types/schema_validation/schema_get_params.py">params</a>) -> <a href="./src/cloudflare/types/schema_validation/public_schema.py">PublicSchema</a></code>

## Settings

Types:

```python
from cloudflare.types.schema_validation import (
    SettingUpdateResponse,
    SettingEditResponse,
    SettingGetResponse,
)
```

Methods:

- <code title="put /zones/{zone_id}/schema_validation/settings">client.schema_validation.settings.<a href="./src/cloudflare/resources/schema_validation/settings/settings.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/schema_validation/setting_update_params.py">params</a>) -> <a href="./src/cloudflare/types/schema_validation/setting_update_response.py">SettingUpdateResponse</a></code>
- <code title="patch /zones/{zone_id}/schema_validation/settings">client.schema_validation.settings.<a href="./src/cloudflare/resources/schema_validation/settings/settings.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/schema_validation/setting_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/schema_validation/setting_edit_response.py">SettingEditResponse</a></code>
- <code title="get /zones/{zone_id}/schema_validation/settings">client.schema_validation.settings.<a href="./src/cloudflare/resources/schema_validation/settings/settings.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/schema_validation/setting_get_response.py">SettingGetResponse</a></code>

### Operations

Types:

```python
from cloudflare.types.schema_validation.settings import (
    OperationUpdateResponse,
    OperationListResponse,
    OperationDeleteResponse,
    OperationBulkEditResponse,
    OperationGetResponse,
)
```

Methods:

- <code title="put /zones/{zone_id}/schema_validation/settings/operations/{operation_id}">client.schema_validation.settings.operations.<a href="./src/cloudflare/resources/schema_validation/settings/operations.py">update</a>(operation_id, \*, zone_id, \*\*<a href="src/cloudflare/types/schema_validation/settings/operation_update_params.py">params</a>) -> <a href="./src/cloudflare/types/schema_validation/settings/operation_update_response.py">OperationUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/schema_validation/settings/operations">client.schema_validation.settings.operations.<a href="./src/cloudflare/resources/schema_validation/settings/operations.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/schema_validation/settings/operation_list_params.py">params</a>) -> <a href="./src/cloudflare/types/schema_validation/settings/operation_list_response.py">SyncV4PagePaginationArray[OperationListResponse]</a></code>
- <code title="delete /zones/{zone_id}/schema_validation/settings/operations/{operation_id}">client.schema_validation.settings.operations.<a href="./src/cloudflare/resources/schema_validation/settings/operations.py">delete</a>(operation_id, \*, zone_id) -> <a href="./src/cloudflare/types/schema_validation/settings/operation_delete_response.py">OperationDeleteResponse</a></code>
- <code title="patch /zones/{zone_id}/schema_validation/settings/operations">client.schema_validation.settings.operations.<a href="./src/cloudflare/resources/schema_validation/settings/operations.py">bulk_edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/schema_validation/settings/operation_bulk_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/schema_validation/settings/operation_bulk_edit_response.py">OperationBulkEditResponse</a></code>
- <code title="get /zones/{zone_id}/schema_validation/settings/operations/{operation_id}">client.schema_validation.settings.operations.<a href="./src/cloudflare/resources/schema_validation/settings/operations.py">get</a>(operation_id, \*, zone_id) -> <a href="./src/cloudflare/types/schema_validation/settings/operation_get_response.py">OperationGetResponse</a></code>
