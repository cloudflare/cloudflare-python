# Logs

## LogExplorer

### Query

Types:

```python
from cloudflare.types.logs.log_explorer import QuerySqlResponse
```

Methods:

- <code title="post /{accounts_or_zones}/{account_or_zone_id}/logs/explorer/query/sql">client.logs.log_explorer.query.<a href="./src/cloudflare/resources/logs/log_explorer/query.py">sql</a>(body, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/logs/log_explorer/query_sql_params.py">params</a>) -> <a href="./src/cloudflare/types/logs/log_explorer/query_sql_response.py">SyncSinglePage[QuerySqlResponse]</a></code>

### Datasets

Types:

```python
from cloudflare.types.logs.log_explorer import CreateRequest, Dataset, DatasetSummary, UpdateRequest
```

Methods:

- <code title="post /{accounts_or_zones}/{account_or_zone_id}/logs/explorer/datasets">client.logs.log_explorer.datasets.<a href="./src/cloudflare/resources/logs/log_explorer/datasets/datasets.py">create</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/logs/log_explorer/dataset_create_params.py">params</a>) -> <a href="./src/cloudflare/types/logs/log_explorer/dataset.py">Optional[Dataset]</a></code>
- <code title="put /{accounts_or_zones}/{account_or_zone_id}/logs/explorer/datasets/{dataset_id}">client.logs.log_explorer.datasets.<a href="./src/cloudflare/resources/logs/log_explorer/datasets/datasets.py">update</a>(dataset_id, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/logs/log_explorer/dataset_update_params.py">params</a>) -> <a href="./src/cloudflare/types/logs/log_explorer/dataset.py">Optional[Dataset]</a></code>
- <code title="get /{accounts_or_zones}/{account_or_zone_id}/logs/explorer/datasets">client.logs.log_explorer.datasets.<a href="./src/cloudflare/resources/logs/log_explorer/datasets/datasets.py">list</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/logs/log_explorer/dataset_list_params.py">params</a>) -> <a href="./src/cloudflare/types/logs/log_explorer/dataset_summary.py">SyncSinglePage[DatasetSummary]</a></code>
- <code title="get /{accounts_or_zones}/{account_or_zone_id}/logs/explorer/datasets/{dataset_id}">client.logs.log_explorer.datasets.<a href="./src/cloudflare/resources/logs/log_explorer/datasets/datasets.py">get</a>(dataset_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/logs/log_explorer/dataset.py">Optional[Dataset]</a></code>

#### Available

Types:

```python
from cloudflare.types.logs.log_explorer.datasets import AvailableDataset, AvailableList
```

Methods:

- <code title="get /{accounts_or_zones}/{account_or_zone_id}/logs/explorer/datasets/available">client.logs.log_explorer.datasets.available.<a href="./src/cloudflare/resources/logs/log_explorer/datasets/available.py">list</a>(\*, account_id, zone_id) -> <a href="./src/cloudflare/types/logs/log_explorer/datasets/available_dataset.py">SyncSinglePage[AvailableDataset]</a></code>

## Control

### Retention

Types:

```python
from cloudflare.types.logs.control import RetentionCreateResponse, RetentionGetResponse
```

Methods:

- <code title="post /zones/{zone_id}/logs/control/retention/flag">client.logs.control.retention.<a href="./src/cloudflare/resources/logs/control/retention.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/logs/control/retention_create_params.py">params</a>) -> <a href="./src/cloudflare/types/logs/control/retention_create_response.py">Optional[RetentionCreateResponse]</a></code>
- <code title="get /zones/{zone_id}/logs/control/retention/flag">client.logs.control.retention.<a href="./src/cloudflare/resources/logs/control/retention.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/logs/control/retention_get_response.py">Optional[RetentionGetResponse]</a></code>

### Cmb

#### Config

Types:

```python
from cloudflare.types.logs.control.cmb import CmbConfig
```

Methods:

- <code title="post /accounts/{account_id}/logs/control/cmb/config">client.logs.control.cmb.config.<a href="./src/cloudflare/resources/logs/control/cmb/config.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/logs/control/cmb/config_create_params.py">params</a>) -> <a href="./src/cloudflare/types/logs/control/cmb/cmb_config.py">Optional[CmbConfig]</a></code>
- <code title="delete /accounts/{account_id}/logs/control/cmb/config">client.logs.control.cmb.config.<a href="./src/cloudflare/resources/logs/control/cmb/config.py">delete</a>(\*, account_id) -> object</code>
- <code title="get /accounts/{account_id}/logs/control/cmb/config">client.logs.control.cmb.config.<a href="./src/cloudflare/resources/logs/control/cmb/config.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/logs/control/cmb/cmb_config.py">Optional[CmbConfig]</a></code>

## RayID

Types:

```python
from cloudflare.types.logs import RayIDGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/logs/rayids/{ray_id}">client.logs.rayid.<a href="./src/cloudflare/resources/logs/rayid.py">get</a>(rayid, \*, zone_id, \*\*<a href="src/cloudflare/types/logs/rayid_get_params.py">params</a>) -> <a href="./src/cloudflare/types/logs/rayid_get_response.py">RayIDGetResponse</a></code>

## Received

Types:

```python
from cloudflare.types.logs import ReceivedGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/logs/received">client.logs.received.<a href="./src/cloudflare/resources/logs/received/received.py">get</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/logs/received_get_params.py">params</a>) -> <a href="./src/cloudflare/types/logs/received_get_response.py">ReceivedGetResponse</a></code>

### Fields

Types:

```python
from cloudflare.types.logs.received import FieldGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/logs/received/fields">client.logs.received.fields.<a href="./src/cloudflare/resources/logs/received/fields.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/logs/received/field_get_response.py">FieldGetResponse</a></code>
