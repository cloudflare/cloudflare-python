# BasinCatalog

Types:

```python
from cloudflare.types.basin_catalog import (
    BasinCatalogListResponse,
    BasinCatalogEnableResponse,
    BasinCatalogGetResponse,
)
```

Methods:

- <code title="get /accounts/{account_id}/basin-catalog">client.basin_catalog.<a href="./src/cloudflare/resources/basin_catalog/basin_catalog.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/basin_catalog/basin_catalog_list_response.py">Optional[BasinCatalogListResponse]</a></code>
- <code title="post /accounts/{account_id}/basin-catalog/{bucket_name}/delete">client.basin_catalog.<a href="./src/cloudflare/resources/basin_catalog/basin_catalog.py">delete</a>(bucket_name, \*, account_id, \*\*<a href="src/cloudflare/types/basin_catalog/basin_catalog_delete_params.py">params</a>) -> None</code>
- <code title="post /accounts/{account_id}/basin-catalog/{bucket_name}/disable">client.basin_catalog.<a href="./src/cloudflare/resources/basin_catalog/basin_catalog.py">disable</a>(bucket_name, \*, account_id) -> None</code>
- <code title="post /accounts/{account_id}/basin-catalog/{bucket_name}/enable">client.basin_catalog.<a href="./src/cloudflare/resources/basin_catalog/basin_catalog.py">enable</a>(bucket_name, \*, account_id) -> <a href="./src/cloudflare/types/basin_catalog/basin_catalog_enable_response.py">Optional[BasinCatalogEnableResponse]</a></code>
- <code title="get /accounts/{account_id}/basin-catalog/{bucket_name}">client.basin_catalog.<a href="./src/cloudflare/resources/basin_catalog/basin_catalog.py">get</a>(bucket_name, \*, account_id) -> <a href="./src/cloudflare/types/basin_catalog/basin_catalog_get_response.py">Optional[BasinCatalogGetResponse]</a></code>

## MaintenanceConfigs

Types:

```python
from cloudflare.types.basin_catalog import (
    MaintenanceConfigUpdateResponse,
    MaintenanceConfigGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/basin-catalog/{bucket_name}/maintenance-configs">client.basin_catalog.maintenance_configs.<a href="./src/cloudflare/resources/basin_catalog/maintenance_configs.py">update</a>(bucket_name, \*, account_id, \*\*<a href="src/cloudflare/types/basin_catalog/maintenance_config_update_params.py">params</a>) -> <a href="./src/cloudflare/types/basin_catalog/maintenance_config_update_response.py">Optional[MaintenanceConfigUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/basin-catalog/{bucket_name}/maintenance-configs">client.basin_catalog.maintenance_configs.<a href="./src/cloudflare/resources/basin_catalog/maintenance_configs.py">get</a>(bucket_name, \*, account_id) -> <a href="./src/cloudflare/types/basin_catalog/maintenance_config_get_response.py">Optional[MaintenanceConfigGetResponse]</a></code>

## Credentials

Methods:

- <code title="post /accounts/{account_id}/basin-catalog/{bucket_name}/credential">client.basin_catalog.credentials.<a href="./src/cloudflare/resources/basin_catalog/credentials.py">create</a>(bucket_name, \*, account_id, \*\*<a href="src/cloudflare/types/basin_catalog/credential_create_params.py">params</a>) -> object</code>

## Namespaces

Types:

```python
from cloudflare.types.basin_catalog import NamespaceListResponse
```

Methods:

- <code title="get /accounts/{account_id}/basin-catalog/{bucket_name}/namespaces">client.basin_catalog.namespaces.<a href="./src/cloudflare/resources/basin_catalog/namespaces/namespaces.py">list</a>(bucket_name, \*, account_id, \*\*<a href="src/cloudflare/types/basin_catalog/namespace_list_params.py">params</a>) -> <a href="./src/cloudflare/types/basin_catalog/namespace_list_response.py">Optional[NamespaceListResponse]</a></code>

### Tables

Types:

```python
from cloudflare.types.basin_catalog.namespaces import TableListResponse
```

Methods:

- <code title="get /accounts/{account_id}/basin-catalog/{bucket_name}/namespaces/{namespace}/tables">client.basin_catalog.namespaces.tables.<a href="./src/cloudflare/resources/basin_catalog/namespaces/tables/tables.py">list</a>(namespace, \*, account_id, bucket_name, \*\*<a href="src/cloudflare/types/basin_catalog/namespaces/table_list_params.py">params</a>) -> <a href="./src/cloudflare/types/basin_catalog/namespaces/table_list_response.py">Optional[TableListResponse]</a></code>

#### MaintenanceConfigs

Types:

```python
from cloudflare.types.basin_catalog.namespaces.tables import (
    MaintenanceConfigUpdateResponse,
    MaintenanceConfigGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/basin-catalog/{bucket_name}/namespaces/{namespace}/tables/{table_name}/maintenance-configs">client.basin_catalog.namespaces.tables.maintenance_configs.<a href="./src/cloudflare/resources/basin_catalog/namespaces/tables/maintenance_configs.py">update</a>(table_name, \*, account_id, bucket_name, namespace, \*\*<a href="src/cloudflare/types/basin_catalog/namespaces/tables/maintenance_config_update_params.py">params</a>) -> <a href="./src/cloudflare/types/basin_catalog/namespaces/tables/maintenance_config_update_response.py">Optional[MaintenanceConfigUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/basin-catalog/{bucket_name}/namespaces/{namespace}/tables/{table_name}/maintenance-configs">client.basin_catalog.namespaces.tables.maintenance_configs.<a href="./src/cloudflare/resources/basin_catalog/namespaces/tables/maintenance_configs.py">get</a>(table_name, \*, account_id, bucket_name, namespace) -> <a href="./src/cloudflare/types/basin_catalog/namespaces/tables/maintenance_config_get_response.py">Optional[MaintenanceConfigGetResponse]</a></code>
