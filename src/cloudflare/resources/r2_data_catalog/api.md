# R2DataCatalog

Types:

```python
from cloudflare.types.r2_data_catalog import (
    R2DataCatalogListResponse,
    R2DataCatalogEnableResponse,
    R2DataCatalogGetResponse,
)
```

Methods:

- <code title="get /accounts/{account_id}/r2-catalog">client.r2_data_catalog.<a href="./src/cloudflare/resources/r2_data_catalog/r2_data_catalog.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/r2_data_catalog/r2_data_catalog_list_response.py">Optional[R2DataCatalogListResponse]</a></code>
- <code title="post /accounts/{account_id}/r2-catalog/{bucket_name}/disable">client.r2_data_catalog.<a href="./src/cloudflare/resources/r2_data_catalog/r2_data_catalog.py">disable</a>(bucket_name, \*, account_id) -> None</code>
- <code title="post /accounts/{account_id}/r2-catalog/{bucket_name}/enable">client.r2_data_catalog.<a href="./src/cloudflare/resources/r2_data_catalog/r2_data_catalog.py">enable</a>(bucket_name, \*, account_id) -> <a href="./src/cloudflare/types/r2_data_catalog/r2_data_catalog_enable_response.py">Optional[R2DataCatalogEnableResponse]</a></code>
- <code title="get /accounts/{account_id}/r2-catalog/{bucket_name}">client.r2_data_catalog.<a href="./src/cloudflare/resources/r2_data_catalog/r2_data_catalog.py">get</a>(bucket_name, \*, account_id) -> <a href="./src/cloudflare/types/r2_data_catalog/r2_data_catalog_get_response.py">Optional[R2DataCatalogGetResponse]</a></code>

## MaintenanceConfigs

Types:

```python
from cloudflare.types.r2_data_catalog import (
    MaintenanceConfigUpdateResponse,
    MaintenanceConfigGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/r2-catalog/{bucket_name}/maintenance-configs">client.r2_data_catalog.maintenance_configs.<a href="./src/cloudflare/resources/r2_data_catalog/maintenance_configs.py">update</a>(bucket_name, \*, account_id, \*\*<a href="src/cloudflare/types/r2_data_catalog/maintenance_config_update_params.py">params</a>) -> <a href="./src/cloudflare/types/r2_data_catalog/maintenance_config_update_response.py">Optional[MaintenanceConfigUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/r2-catalog/{bucket_name}/maintenance-configs">client.r2_data_catalog.maintenance_configs.<a href="./src/cloudflare/resources/r2_data_catalog/maintenance_configs.py">get</a>(bucket_name, \*, account_id) -> <a href="./src/cloudflare/types/r2_data_catalog/maintenance_config_get_response.py">Optional[MaintenanceConfigGetResponse]</a></code>

## Credentials

Methods:

- <code title="post /accounts/{account_id}/r2-catalog/{bucket_name}/credential">client.r2_data_catalog.credentials.<a href="./src/cloudflare/resources/r2_data_catalog/credentials.py">create</a>(bucket_name, \*, account_id, \*\*<a href="src/cloudflare/types/r2_data_catalog/credential_create_params.py">params</a>) -> object</code>

## Namespaces

Types:

```python
from cloudflare.types.r2_data_catalog import NamespaceListResponse
```

Methods:

- <code title="get /accounts/{account_id}/r2-catalog/{bucket_name}/namespaces">client.r2_data_catalog.namespaces.<a href="./src/cloudflare/resources/r2_data_catalog/namespaces/namespaces.py">list</a>(bucket_name, \*, account_id, \*\*<a href="src/cloudflare/types/r2_data_catalog/namespace_list_params.py">params</a>) -> <a href="./src/cloudflare/types/r2_data_catalog/namespace_list_response.py">Optional[NamespaceListResponse]</a></code>

### Tables

Types:

```python
from cloudflare.types.r2_data_catalog.namespaces import TableListResponse
```

Methods:

- <code title="get /accounts/{account_id}/r2-catalog/{bucket_name}/namespaces/{namespace}/tables">client.r2_data_catalog.namespaces.tables.<a href="./src/cloudflare/resources/r2_data_catalog/namespaces/tables/tables.py">list</a>(namespace, \*, account_id, bucket_name, \*\*<a href="src/cloudflare/types/r2_data_catalog/namespaces/table_list_params.py">params</a>) -> <a href="./src/cloudflare/types/r2_data_catalog/namespaces/table_list_response.py">Optional[TableListResponse]</a></code>

#### MaintenanceConfigs

Types:

```python
from cloudflare.types.r2_data_catalog.namespaces.tables import (
    MaintenanceConfigUpdateResponse,
    MaintenanceConfigGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/r2-catalog/{bucket_name}/namespaces/{namespace}/tables/{table_name}/maintenance-configs">client.r2_data_catalog.namespaces.tables.maintenance_configs.<a href="./src/cloudflare/resources/r2_data_catalog/namespaces/tables/maintenance_configs.py">update</a>(table_name, \*, account_id, bucket_name, namespace, \*\*<a href="src/cloudflare/types/r2_data_catalog/namespaces/tables/maintenance_config_update_params.py">params</a>) -> <a href="./src/cloudflare/types/r2_data_catalog/namespaces/tables/maintenance_config_update_response.py">Optional[MaintenanceConfigUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/r2-catalog/{bucket_name}/namespaces/{namespace}/tables/{table_name}/maintenance-configs">client.r2_data_catalog.namespaces.tables.maintenance_configs.<a href="./src/cloudflare/resources/r2_data_catalog/namespaces/tables/maintenance_configs.py">get</a>(table_name, \*, account_id, bucket_name, namespace) -> <a href="./src/cloudflare/types/r2_data_catalog/namespaces/tables/maintenance_config_get_response.py">Optional[MaintenanceConfigGetResponse]</a></code>
