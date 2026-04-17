# Speed

Types:

```python
from cloudflare.types.speed import LabeledRegion, LighthouseReport, Trend
```

## Schedule

Types:

```python
from cloudflare.types.speed import Schedule, ScheduleCreateResponse, ScheduleDeleteResponse
```

Methods:

- <code title="post /zones/{zone_id}/speed_api/schedule/{url}">client.speed.schedule.<a href="./src/cloudflare/resources/speed/schedule.py">create</a>(url, \*, zone_id, \*\*<a href="src/cloudflare/types/speed/schedule_create_params.py">params</a>) -> <a href="./src/cloudflare/types/speed/schedule_create_response.py">Optional[ScheduleCreateResponse]</a></code>
- <code title="delete /zones/{zone_id}/speed_api/schedule/{url}">client.speed.schedule.<a href="./src/cloudflare/resources/speed/schedule.py">delete</a>(url, \*, zone_id, \*\*<a href="src/cloudflare/types/speed/schedule_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/speed/schedule_delete_response.py">Optional[ScheduleDeleteResponse]</a></code>
- <code title="get /zones/{zone_id}/speed_api/schedule/{url}">client.speed.schedule.<a href="./src/cloudflare/resources/speed/schedule.py">get</a>(url, \*, zone_id, \*\*<a href="src/cloudflare/types/speed/schedule_get_params.py">params</a>) -> <a href="./src/cloudflare/types/speed/schedule.py">Optional[Schedule]</a></code>

## Availabilities

Types:

```python
from cloudflare.types.speed import Availability
```

Methods:

- <code title="get /zones/{zone_id}/speed_api/availabilities">client.speed.availabilities.<a href="./src/cloudflare/resources/speed/availabilities.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/speed/availability.py">Optional[Availability]</a></code>

## Pages

Types:

```python
from cloudflare.types.speed import PageListResponse
```

Methods:

- <code title="get /zones/{zone_id}/speed_api/pages">client.speed.pages.<a href="./src/cloudflare/resources/speed/pages/pages.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/speed/page_list_response.py">SyncSinglePage[PageListResponse]</a></code>
- <code title="get /zones/{zone_id}/speed_api/pages/{url}/trend">client.speed.pages.<a href="./src/cloudflare/resources/speed/pages/pages.py">trend</a>(url, \*, zone_id, \*\*<a href="src/cloudflare/types/speed/page_trend_params.py">params</a>) -> <a href="./src/cloudflare/types/speed/trend.py">Optional[Trend]</a></code>

### Tests

Types:

```python
from cloudflare.types.speed.pages import Test, TestDeleteResponse
```

Methods:

- <code title="post /zones/{zone_id}/speed_api/pages/{url}/tests">client.speed.pages.tests.<a href="./src/cloudflare/resources/speed/pages/tests.py">create</a>(url, \*, zone_id, \*\*<a href="src/cloudflare/types/speed/pages/test_create_params.py">params</a>) -> <a href="./src/cloudflare/types/speed/pages/test.py">Optional[Test]</a></code>
- <code title="get /zones/{zone_id}/speed_api/pages/{url}/tests">client.speed.pages.tests.<a href="./src/cloudflare/resources/speed/pages/tests.py">list</a>(url, \*, zone_id, \*\*<a href="src/cloudflare/types/speed/pages/test_list_params.py">params</a>) -> <a href="./src/cloudflare/types/speed/pages/test.py">SyncV4PagePaginationArray[Test]</a></code>
- <code title="delete /zones/{zone_id}/speed_api/pages/{url}/tests">client.speed.pages.tests.<a href="./src/cloudflare/resources/speed/pages/tests.py">delete</a>(url, \*, zone_id, \*\*<a href="src/cloudflare/types/speed/pages/test_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/speed/pages/test_delete_response.py">Optional[TestDeleteResponse]</a></code>
- <code title="get /zones/{zone_id}/speed_api/pages/{url}/tests/{test_id}">client.speed.pages.tests.<a href="./src/cloudflare/resources/speed/pages/tests.py">get</a>(test_id, \*, zone_id, url) -> <a href="./src/cloudflare/types/speed/pages/test.py">Optional[Test]</a></code>
