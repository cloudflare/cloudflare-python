# Spectrum

Types:

```python
from cloudflare.types.spectrum import DNS, EdgeIPs, OriginDNS, OriginPort
```

## Analytics

### Aggregates

#### Currents

Types:

```python
from cloudflare.types.spectrum.analytics.aggregates import CurrentGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/spectrum/analytics/aggregate/current">client.spectrum.analytics.aggregates.currents.<a href="./src/cloudflare/resources/spectrum/analytics/aggregates/currents.py">get</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/spectrum/analytics/aggregates/current_get_params.py">params</a>) -> <a href="./src/cloudflare/types/spectrum/analytics/aggregates/current_get_response.py">Optional[CurrentGetResponse]</a></code>

### Events

Types:

```python
from cloudflare.types.spectrum.analytics import Dimension
```

#### Bytimes

Types:

```python
from cloudflare.types.spectrum.analytics.events import BytimeGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/spectrum/analytics/events/bytime">client.spectrum.analytics.events.bytimes.<a href="./src/cloudflare/resources/spectrum/analytics/events/bytimes.py">get</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/spectrum/analytics/events/bytime_get_params.py">params</a>) -> <a href="./src/cloudflare/types/spectrum/analytics/events/bytime_get_response.py">Optional[BytimeGetResponse]</a></code>

#### Summaries

Types:

```python
from cloudflare.types.spectrum.analytics.events import SummaryGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/spectrum/analytics/events/summary">client.spectrum.analytics.events.summaries.<a href="./src/cloudflare/resources/spectrum/analytics/events/summaries.py">get</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/spectrum/analytics/events/summary_get_params.py">params</a>) -> <a href="./src/cloudflare/types/spectrum/analytics/events/summary_get_response.py">Optional[SummaryGetResponse]</a></code>

## Apps

Types:

```python
from cloudflare.types.spectrum import (
    AppCreateResponse,
    AppUpdateResponse,
    AppListResponse,
    AppDeleteResponse,
    AppGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/spectrum/apps">client.spectrum.apps.<a href="./src/cloudflare/resources/spectrum/apps.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/spectrum/app_create_params.py">params</a>) -> <a href="./src/cloudflare/types/spectrum/app_create_response.py">Optional[AppCreateResponse]</a></code>
- <code title="put /zones/{zone_id}/spectrum/apps/{app_id}">client.spectrum.apps.<a href="./src/cloudflare/resources/spectrum/apps.py">update</a>(app_id, \*, zone_id, \*\*<a href="src/cloudflare/types/spectrum/app_update_params.py">params</a>) -> <a href="./src/cloudflare/types/spectrum/app_update_response.py">Optional[AppUpdateResponse]</a></code>
- <code title="get /zones/{zone_id}/spectrum/apps">client.spectrum.apps.<a href="./src/cloudflare/resources/spectrum/apps.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/spectrum/app_list_params.py">params</a>) -> <a href="./src/cloudflare/types/spectrum/app_list_response.py">SyncV4PagePaginationArray[AppListResponse]</a></code>
- <code title="delete /zones/{zone_id}/spectrum/apps/{app_id}">client.spectrum.apps.<a href="./src/cloudflare/resources/spectrum/apps.py">delete</a>(app_id, \*, zone_id) -> <a href="./src/cloudflare/types/spectrum/app_delete_response.py">Optional[AppDeleteResponse]</a></code>
- <code title="get /zones/{zone_id}/spectrum/apps/{app_id}">client.spectrum.apps.<a href="./src/cloudflare/resources/spectrum/apps.py">get</a>(app_id, \*, zone_id) -> <a href="./src/cloudflare/types/spectrum/app_get_response.py">Optional[AppGetResponse]</a></code>
