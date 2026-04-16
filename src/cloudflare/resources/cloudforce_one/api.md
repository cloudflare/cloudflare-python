# CloudforceOne

## Scans

### Results

Types:

```python
from cloudflare.types.cloudforce_one.scans import ScanResult, ResultGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/cloudforce-one/scans/results/{config_id}">client.cloudforce_one.scans.results.<a href="./src/cloudflare/resources/cloudforce_one/scans/results.py">get</a>(config_id, \*, account_id) -> <a href="./src/cloudflare/types/cloudforce_one/scans/result_get_response.py">ResultGetResponse</a></code>

### Config

Types:

```python
from cloudflare.types.cloudforce_one.scans import (
    ConfigCreateResponse,
    ConfigListResponse,
    ConfigEditResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/cloudforce-one/scans/config">client.cloudforce_one.scans.config.<a href="./src/cloudflare/resources/cloudforce_one/scans/config.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/cloudforce_one/scans/config_create_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/scans/config_create_response.py">Optional[ConfigCreateResponse]</a></code>
- <code title="get /accounts/{account_id}/cloudforce-one/scans/config">client.cloudforce_one.scans.config.<a href="./src/cloudflare/resources/cloudforce_one/scans/config.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/cloudforce_one/scans/config_list_response.py">SyncSinglePage[ConfigListResponse]</a></code>
- <code title="delete /accounts/{account_id}/cloudforce-one/scans/config/{config_id}">client.cloudforce_one.scans.config.<a href="./src/cloudflare/resources/cloudforce_one/scans/config.py">delete</a>(config_id, \*, account_id) -> object</code>
- <code title="patch /accounts/{account_id}/cloudforce-one/scans/config/{config_id}">client.cloudforce_one.scans.config.<a href="./src/cloudflare/resources/cloudforce_one/scans/config.py">edit</a>(config_id, \*, account_id, \*\*<a href="src/cloudflare/types/cloudforce_one/scans/config_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/scans/config_edit_response.py">Optional[ConfigEditResponse]</a></code>

## BinaryStorage

Types:

```python
from cloudflare.types.cloudforce_one import BinaryStorageCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/cloudforce-one/binary">client.cloudforce_one.binary_storage.<a href="./src/cloudflare/resources/cloudforce_one/binary_storage.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/cloudforce_one/binary_storage_create_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/binary_storage_create_response.py">BinaryStorageCreateResponse</a></code>
- <code title="get /accounts/{account_id}/cloudforce-one/binary/{hash}">client.cloudforce_one.binary_storage.<a href="./src/cloudflare/resources/cloudforce_one/binary_storage.py">get</a>(hash, \*, account_id) -> None</code>

## Requests

Types:

```python
from cloudflare.types.cloudforce_one import (
    Item,
    ListItem,
    Quota,
    RequestConstants,
    RequestTypes,
    RequestDeleteResponse,
    RequestTypesResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/cloudforce-one/requests/new">client.cloudforce_one.requests.<a href="./src/cloudflare/resources/cloudforce_one/requests/requests.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/cloudforce_one/request_create_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/item.py">Optional[Item]</a></code>
- <code title="put /accounts/{account_id}/cloudforce-one/requests/{request_id}">client.cloudforce_one.requests.<a href="./src/cloudflare/resources/cloudforce_one/requests/requests.py">update</a>(request_id, \*, account_id, \*\*<a href="src/cloudflare/types/cloudforce_one/request_update_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/item.py">Optional[Item]</a></code>
- <code title="post /accounts/{account_id}/cloudforce-one/requests">client.cloudforce_one.requests.<a href="./src/cloudflare/resources/cloudforce_one/requests/requests.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/cloudforce_one/request_list_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/list_item.py">SyncSinglePage[ListItem]</a></code>
- <code title="delete /accounts/{account_id}/cloudforce-one/requests/{request_id}">client.cloudforce_one.requests.<a href="./src/cloudflare/resources/cloudforce_one/requests/requests.py">delete</a>(request_id, \*, account_id) -> <a href="./src/cloudflare/types/cloudforce_one/request_delete_response.py">RequestDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/cloudforce-one/requests/constants">client.cloudforce_one.requests.<a href="./src/cloudflare/resources/cloudforce_one/requests/requests.py">constants</a>(\*, account_id) -> <a href="./src/cloudflare/types/cloudforce_one/request_constants.py">Optional[RequestConstants]</a></code>
- <code title="get /accounts/{account_id}/cloudforce-one/requests/{request_id}">client.cloudforce_one.requests.<a href="./src/cloudflare/resources/cloudforce_one/requests/requests.py">get</a>(request_id, \*, account_id) -> <a href="./src/cloudflare/types/cloudforce_one/item.py">Optional[Item]</a></code>
- <code title="get /accounts/{account_id}/cloudforce-one/requests/quota">client.cloudforce_one.requests.<a href="./src/cloudflare/resources/cloudforce_one/requests/requests.py">quota</a>(\*, account_id) -> <a href="./src/cloudflare/types/cloudforce_one/quota.py">Optional[Quota]</a></code>
- <code title="get /accounts/{account_id}/cloudforce-one/requests/types">client.cloudforce_one.requests.<a href="./src/cloudflare/resources/cloudforce_one/requests/requests.py">types</a>(\*, account_id) -> <a href="./src/cloudflare/types/cloudforce_one/request_types_response.py">SyncSinglePage[RequestTypesResponse]</a></code>

### Message

Types:

```python
from cloudflare.types.cloudforce_one.requests import Message, MessageDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/cloudforce-one/requests/{request_id}/message/new">client.cloudforce_one.requests.message.<a href="./src/cloudflare/resources/cloudforce_one/requests/message.py">create</a>(request_id, \*, account_id, \*\*<a href="src/cloudflare/types/cloudforce_one/requests/message_create_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/requests/message.py">Optional[Message]</a></code>
- <code title="put /accounts/{account_id}/cloudforce-one/requests/{request_id}/message/{message_id}">client.cloudforce_one.requests.message.<a href="./src/cloudflare/resources/cloudforce_one/requests/message.py">update</a>(message_id, \*, account_id, request_id, \*\*<a href="src/cloudflare/types/cloudforce_one/requests/message_update_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/requests/message.py">Optional[Message]</a></code>
- <code title="delete /accounts/{account_id}/cloudforce-one/requests/{request_id}/message/{message_id}">client.cloudforce_one.requests.message.<a href="./src/cloudflare/resources/cloudforce_one/requests/message.py">delete</a>(message_id, \*, account_id, request_id) -> <a href="./src/cloudflare/types/cloudforce_one/requests/message_delete_response.py">MessageDeleteResponse</a></code>
- <code title="post /accounts/{account_id}/cloudforce-one/requests/{request_id}/message">client.cloudforce_one.requests.message.<a href="./src/cloudflare/resources/cloudforce_one/requests/message.py">get</a>(request_id, \*, account_id, \*\*<a href="src/cloudflare/types/cloudforce_one/requests/message_get_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/requests/message.py">SyncSinglePage[Message]</a></code>

### Priority

Types:

```python
from cloudflare.types.cloudforce_one.requests import (
    Label,
    Priority,
    PriorityEdit,
    PriorityDeleteResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/cloudforce-one/requests/priority/new">client.cloudforce_one.requests.priority.<a href="./src/cloudflare/resources/cloudforce_one/requests/priority.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/cloudforce_one/requests/priority_create_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/requests/priority.py">Optional[Priority]</a></code>
- <code title="put /accounts/{account_id}/cloudforce-one/requests/priority/{priority_id}">client.cloudforce_one.requests.priority.<a href="./src/cloudflare/resources/cloudforce_one/requests/priority.py">update</a>(priority_id, \*, account_id, \*\*<a href="src/cloudflare/types/cloudforce_one/requests/priority_update_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/item.py">Optional[Item]</a></code>
- <code title="delete /accounts/{account_id}/cloudforce-one/requests/priority/{priority_id}">client.cloudforce_one.requests.priority.<a href="./src/cloudflare/resources/cloudforce_one/requests/priority.py">delete</a>(priority_id, \*, account_id) -> <a href="./src/cloudflare/types/cloudforce_one/requests/priority_delete_response.py">PriorityDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/cloudforce-one/requests/priority/{priority_id}">client.cloudforce_one.requests.priority.<a href="./src/cloudflare/resources/cloudforce_one/requests/priority.py">get</a>(priority_id, \*, account_id) -> <a href="./src/cloudflare/types/cloudforce_one/item.py">Optional[Item]</a></code>
- <code title="get /accounts/{account_id}/cloudforce-one/requests/priority/quota">client.cloudforce_one.requests.priority.<a href="./src/cloudflare/resources/cloudforce_one/requests/priority.py">quota</a>(\*, account_id) -> <a href="./src/cloudflare/types/cloudforce_one/quota.py">Optional[Quota]</a></code>

### Assets

Types:

```python
from cloudflare.types.cloudforce_one.requests import (
    AssetCreateResponse,
    AssetUpdateResponse,
    AssetDeleteResponse,
    AssetGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/cloudforce-one/requests/{request_id}/asset">client.cloudforce_one.requests.assets.<a href="./src/cloudflare/resources/cloudforce_one/requests/assets.py">create</a>(request_id, \*, account_id, \*\*<a href="src/cloudflare/types/cloudforce_one/requests/asset_create_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/requests/asset_create_response.py">SyncSinglePage[AssetCreateResponse]</a></code>
- <code title="put /accounts/{account_id}/cloudforce-one/requests/{request_id}/asset/{asset_id}">client.cloudforce_one.requests.assets.<a href="./src/cloudflare/resources/cloudforce_one/requests/assets.py">update</a>(asset_id, \*, account_id, request_id, \*\*<a href="src/cloudflare/types/cloudforce_one/requests/asset_update_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/requests/asset_update_response.py">Optional[AssetUpdateResponse]</a></code>
- <code title="delete /accounts/{account_id}/cloudforce-one/requests/{request_id}/asset/{asset_id}">client.cloudforce_one.requests.assets.<a href="./src/cloudflare/resources/cloudforce_one/requests/assets.py">delete</a>(asset_id, \*, account_id, request_id) -> <a href="./src/cloudflare/types/cloudforce_one/requests/asset_delete_response.py">AssetDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/cloudforce-one/requests/{request_id}/asset/{asset_id}">client.cloudforce_one.requests.assets.<a href="./src/cloudflare/resources/cloudforce_one/requests/assets.py">get</a>(asset_id, \*, account_id, request_id) -> <a href="./src/cloudflare/types/cloudforce_one/requests/asset_get_response.py">SyncSinglePage[AssetGetResponse]</a></code>

## ThreatEvents

Types:

```python
from cloudflare.types.cloudforce_one import (
    ThreatEventCreateResponse,
    ThreatEventListResponse,
    ThreatEventBulkCreateResponse,
    ThreatEventEditResponse,
    ThreatEventGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/cloudforce-one/events/create">client.cloudforce_one.threat_events.<a href="./src/cloudflare/resources/cloudforce_one/threat_events/threat_events.py">create</a>(\*, path_account_id, \*\*<a href="src/cloudflare/types/cloudforce_one/threat_event_create_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/threat_event_create_response.py">ThreatEventCreateResponse</a></code>
- <code title="get /accounts/{account_id}/cloudforce-one/events">client.cloudforce_one.threat_events.<a href="./src/cloudflare/resources/cloudforce_one/threat_events/threat_events.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/cloudforce_one/threat_event_list_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/threat_event_list_response.py">ThreatEventListResponse</a></code>
- <code title="post /accounts/{account_id}/cloudforce-one/events/create/bulk">client.cloudforce_one.threat_events.<a href="./src/cloudflare/resources/cloudforce_one/threat_events/threat_events.py">bulk_create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/cloudforce_one/threat_event_bulk_create_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/threat_event_bulk_create_response.py">ThreatEventBulkCreateResponse</a></code>
- <code title="patch /accounts/{account_id}/cloudforce-one/events/{event_id}">client.cloudforce_one.threat_events.<a href="./src/cloudflare/resources/cloudforce_one/threat_events/threat_events.py">edit</a>(event_id, \*, account_id, \*\*<a href="src/cloudflare/types/cloudforce_one/threat_event_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/threat_event_edit_response.py">ThreatEventEditResponse</a></code>
- <code title="get /accounts/{account_id}/cloudforce-one/events/{event_id}">client.cloudforce_one.threat_events.<a href="./src/cloudflare/resources/cloudforce_one/threat_events/threat_events.py">get</a>(event_id, \*, account_id) -> <a href="./src/cloudflare/types/cloudforce_one/threat_event_get_response.py">ThreatEventGetResponse</a></code>

### Attackers

Types:

```python
from cloudflare.types.cloudforce_one.threat_events import AttackerListResponse
```

Methods:

- <code title="get /accounts/{account_id}/cloudforce-one/events/attackers">client.cloudforce_one.threat_events.attackers.<a href="./src/cloudflare/resources/cloudforce_one/threat_events/attackers.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/cloudforce_one/threat_events/attacker_list_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/threat_events/attacker_list_response.py">AttackerListResponse</a></code>

### Categories

Types:

```python
from cloudflare.types.cloudforce_one.threat_events import (
    CategoryCreateResponse,
    CategoryListResponse,
    CategoryDeleteResponse,
    CategoryEditResponse,
    CategoryGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/cloudforce-one/events/categories/create">client.cloudforce_one.threat_events.categories.<a href="./src/cloudflare/resources/cloudforce_one/threat_events/categories.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/cloudforce_one/threat_events/category_create_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/threat_events/category_create_response.py">CategoryCreateResponse</a></code>
- <code title="get /accounts/{account_id}/cloudforce-one/events/categories">client.cloudforce_one.threat_events.categories.<a href="./src/cloudflare/resources/cloudforce_one/threat_events/categories.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/cloudforce_one/threat_events/category_list_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/threat_events/category_list_response.py">CategoryListResponse</a></code>
- <code title="delete /accounts/{account_id}/cloudforce-one/events/categories/{category_id}">client.cloudforce_one.threat_events.categories.<a href="./src/cloudflare/resources/cloudforce_one/threat_events/categories.py">delete</a>(category_id, \*, account_id) -> <a href="./src/cloudflare/types/cloudforce_one/threat_events/category_delete_response.py">CategoryDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/cloudforce-one/events/categories/{category_id}">client.cloudforce_one.threat_events.categories.<a href="./src/cloudflare/resources/cloudforce_one/threat_events/categories.py">edit</a>(category_id, \*, account_id, \*\*<a href="src/cloudflare/types/cloudforce_one/threat_events/category_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/threat_events/category_edit_response.py">CategoryEditResponse</a></code>
- <code title="get /accounts/{account_id}/cloudforce-one/events/categories/{category_id}">client.cloudforce_one.threat_events.categories.<a href="./src/cloudflare/resources/cloudforce_one/threat_events/categories.py">get</a>(category_id, \*, account_id) -> <a href="./src/cloudflare/types/cloudforce_one/threat_events/category_get_response.py">CategoryGetResponse</a></code>

### Countries

Types:

```python
from cloudflare.types.cloudforce_one.threat_events import CountryListResponse
```

Methods:

- <code title="get /accounts/{account_id}/cloudforce-one/events/countries">client.cloudforce_one.threat_events.countries.<a href="./src/cloudflare/resources/cloudforce_one/threat_events/countries.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/cloudforce_one/threat_events/country_list_response.py">CountryListResponse</a></code>

### Datasets

Types:

```python
from cloudflare.types.cloudforce_one.threat_events import (
    DatasetCreateResponse,
    DatasetListResponse,
    DatasetEditResponse,
    DatasetGetResponse,
    DatasetRawResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/cloudforce-one/events/dataset/create">client.cloudforce_one.threat_events.datasets.<a href="./src/cloudflare/resources/cloudforce_one/threat_events/datasets.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/cloudforce_one/threat_events/dataset_create_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/threat_events/dataset_create_response.py">DatasetCreateResponse</a></code>
- <code title="get /accounts/{account_id}/cloudforce-one/events/dataset">client.cloudforce_one.threat_events.datasets.<a href="./src/cloudflare/resources/cloudforce_one/threat_events/datasets.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/cloudforce_one/threat_events/dataset_list_response.py">DatasetListResponse</a></code>
- <code title="patch /accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}">client.cloudforce_one.threat_events.datasets.<a href="./src/cloudflare/resources/cloudforce_one/threat_events/datasets.py">edit</a>(dataset_id, \*, account_id, \*\*<a href="src/cloudflare/types/cloudforce_one/threat_events/dataset_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/threat_events/dataset_edit_response.py">DatasetEditResponse</a></code>
- <code title="get /accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}">client.cloudforce_one.threat_events.datasets.<a href="./src/cloudflare/resources/cloudforce_one/threat_events/datasets.py">get</a>(dataset_id, \*, account_id) -> <a href="./src/cloudflare/types/cloudforce_one/threat_events/dataset_get_response.py">DatasetGetResponse</a></code>
- <code title="get /accounts/{account_id}/cloudforce-one/events/raw/{dataset_id}/{event_id}">client.cloudforce_one.threat_events.datasets.<a href="./src/cloudflare/resources/cloudforce_one/threat_events/datasets.py">raw</a>(event_id, \*, account_id, dataset_id) -> <a href="./src/cloudflare/types/cloudforce_one/threat_events/dataset_raw_response.py">DatasetRawResponse</a></code>

### IndicatorTypes

Types:

```python
from cloudflare.types.cloudforce_one.threat_events import IndicatorTypeListResponse
```

Methods:

- <code title="get /accounts/{account_id}/cloudforce-one/events/indicatorTypes">client.cloudforce_one.threat_events.indicator_types.<a href="./src/cloudflare/resources/cloudforce_one/threat_events/indicator_types.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/cloudforce_one/threat_events/indicator_type_list_response.py">IndicatorTypeListResponse</a></code>

### Raw

Types:

```python
from cloudflare.types.cloudforce_one.threat_events import RawEditResponse, RawGetResponse
```

Methods:

- <code title="patch /accounts/{account_id}/cloudforce-one/events/{event_id}/raw/{raw_id}">client.cloudforce_one.threat_events.raw.<a href="./src/cloudflare/resources/cloudforce_one/threat_events/raw.py">edit</a>(raw_id, \*, account_id, event_id, \*\*<a href="src/cloudflare/types/cloudforce_one/threat_events/raw_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/threat_events/raw_edit_response.py">RawEditResponse</a></code>
- <code title="get /accounts/{account_id}/cloudforce-one/events/{event_id}/raw/{raw_id}">client.cloudforce_one.threat_events.raw.<a href="./src/cloudflare/resources/cloudforce_one/threat_events/raw.py">get</a>(raw_id, \*, account_id, event_id) -> <a href="./src/cloudflare/types/cloudforce_one/threat_events/raw_get_response.py">RawGetResponse</a></code>

### Relate

Types:

```python
from cloudflare.types.cloudforce_one.threat_events import RelateDeleteResponse
```

Methods:

- <code title="delete /accounts/{account_id}/cloudforce-one/events/relate/{event_id}">client.cloudforce_one.threat_events.relate.<a href="./src/cloudflare/resources/cloudforce_one/threat_events/relate.py">delete</a>(event_id, \*, account_id) -> <a href="./src/cloudflare/types/cloudforce_one/threat_events/relate_delete_response.py">RelateDeleteResponse</a></code>

### Tags

Types:

```python
from cloudflare.types.cloudforce_one.threat_events import TagCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/cloudforce-one/events/tags/create">client.cloudforce_one.threat_events.tags.<a href="./src/cloudflare/resources/cloudforce_one/threat_events/tags.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/cloudforce_one/threat_events/tag_create_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/threat_events/tag_create_response.py">TagCreateResponse</a></code>

### EventTags

Types:

```python
from cloudflare.types.cloudforce_one.threat_events import (
    EventTagCreateResponse,
    EventTagDeleteResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/cloudforce-one/events/event_tag/{event_id}/create">client.cloudforce_one.threat_events.event_tags.<a href="./src/cloudflare/resources/cloudforce_one/threat_events/event_tags.py">create</a>(event_id, \*, account_id, \*\*<a href="src/cloudflare/types/cloudforce_one/threat_events/event_tag_create_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/threat_events/event_tag_create_response.py">EventTagCreateResponse</a></code>
- <code title="delete /accounts/{account_id}/cloudforce-one/events/event_tag/{event_id}">client.cloudforce_one.threat_events.event_tags.<a href="./src/cloudflare/resources/cloudforce_one/threat_events/event_tags.py">delete</a>(event_id, \*, account_id) -> <a href="./src/cloudflare/types/cloudforce_one/threat_events/event_tag_delete_response.py">EventTagDeleteResponse</a></code>

### TargetIndustries

Types:

```python
from cloudflare.types.cloudforce_one.threat_events import TargetIndustryListResponse
```

Methods:

- <code title="get /accounts/{account_id}/cloudforce-one/events/targetIndustries">client.cloudforce_one.threat_events.target_industries.<a href="./src/cloudflare/resources/cloudforce_one/threat_events/target_industries.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/cloudforce_one/threat_events/target_industry_list_params.py">params</a>) -> <a href="./src/cloudflare/types/cloudforce_one/threat_events/target_industry_list_response.py">TargetIndustryListResponse</a></code>
