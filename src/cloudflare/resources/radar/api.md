# Radar

## AgentReadiness

Types:

```python
from cloudflare.types.radar import AgentReadinessSummaryResponse
```

Methods:

- <code title="get /radar/agent_readiness/summary/{dimension}">client.radar.agent_readiness.<a href="./src/cloudflare/resources/radar/agent_readiness.py">summary</a>(dimension, \*\*<a href="src/cloudflare/types/radar/agent_readiness_summary_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/agent_readiness_summary_response.py">AgentReadinessSummaryResponse</a></code>

## AI

### ToMarkdown

Types:

```python
from cloudflare.types.radar.ai import ToMarkdownCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/ai/tomarkdown">client.radar.ai.to_markdown.<a href="./src/cloudflare/resources/radar/ai/to_markdown.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/radar/ai/to_markdown_create_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/ai/to_markdown_create_response.py">SyncSinglePage[ToMarkdownCreateResponse]</a></code>

### Inference

Types:

```python
from cloudflare.types.radar.ai import (
    InferenceSummaryV2Response,
    InferenceTimeseriesGroupsV2Response,
)
```

Methods:

- <code title="get /radar/ai/inference/summary/{dimension}">client.radar.ai.inference.<a href="./src/cloudflare/resources/radar/ai/inference/inference.py">summary_v2</a>(dimension, \*\*<a href="src/cloudflare/types/radar/ai/inference_summary_v2_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/ai/inference_summary_v2_response.py">InferenceSummaryV2Response</a></code>
- <code title="get /radar/ai/inference/timeseries_groups/{dimension}">client.radar.ai.inference.<a href="./src/cloudflare/resources/radar/ai/inference/inference.py">timeseries_groups_v2</a>(dimension, \*\*<a href="src/cloudflare/types/radar/ai/inference_timeseries_groups_v2_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/ai/inference_timeseries_groups_v2_response.py">InferenceTimeseriesGroupsV2Response</a></code>

#### Summary

Types:

```python
from cloudflare.types.radar.ai.inference import SummaryModelResponse, SummaryTaskResponse
```

Methods:

- <code title="get /radar/ai/inference/summary/model">client.radar.ai.inference.summary.<a href="./src/cloudflare/resources/radar/ai/inference/summary.py">model</a>(\*\*<a href="src/cloudflare/types/radar/ai/inference/summary_model_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/ai/inference/summary_model_response.py">SummaryModelResponse</a></code>
- <code title="get /radar/ai/inference/summary/task">client.radar.ai.inference.summary.<a href="./src/cloudflare/resources/radar/ai/inference/summary.py">task</a>(\*\*<a href="src/cloudflare/types/radar/ai/inference/summary_task_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/ai/inference/summary_task_response.py">SummaryTaskResponse</a></code>

#### TimeseriesGroups

##### Summary

Types:

```python
from cloudflare.types.radar.ai.inference.timeseries_groups import (
    SummaryModelResponse,
    SummaryTaskResponse,
)
```

Methods:

- <code title="get /radar/ai/inference/timeseries_groups/model">client.radar.ai.inference.timeseries_groups.summary.<a href="./src/cloudflare/resources/radar/ai/inference/timeseries_groups/summary.py">model</a>(\*\*<a href="src/cloudflare/types/radar/ai/inference/timeseries_groups/summary_model_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/ai/inference/timeseries_groups/summary_model_response.py">SummaryModelResponse</a></code>
- <code title="get /radar/ai/inference/timeseries_groups/task">client.radar.ai.inference.timeseries_groups.summary.<a href="./src/cloudflare/resources/radar/ai/inference/timeseries_groups/summary.py">task</a>(\*\*<a href="src/cloudflare/types/radar/ai/inference/timeseries_groups/summary_task_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/ai/inference/timeseries_groups/summary_task_response.py">SummaryTaskResponse</a></code>

### Bots

Types:

```python
from cloudflare.types.radar.ai import (
    BotSummaryV2Response,
    BotTimeseriesResponse,
    BotTimeseriesGroupsResponse,
)
```

Methods:

- <code title="get /radar/ai/bots/summary/{dimension}">client.radar.ai.bots.<a href="./src/cloudflare/resources/radar/ai/bots/bots.py">summary_v2</a>(dimension, \*\*<a href="src/cloudflare/types/radar/ai/bot_summary_v2_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/ai/bot_summary_v2_response.py">BotSummaryV2Response</a></code>
- <code title="get /radar/ai/bots/timeseries">client.radar.ai.bots.<a href="./src/cloudflare/resources/radar/ai/bots/bots.py">timeseries</a>(\*\*<a href="src/cloudflare/types/radar/ai/bot_timeseries_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/ai/bot_timeseries_response.py">BotTimeseriesResponse</a></code>
- <code title="get /radar/ai/bots/timeseries_groups/{dimension}">client.radar.ai.bots.<a href="./src/cloudflare/resources/radar/ai/bots/bots.py">timeseries_groups</a>(dimension, \*\*<a href="src/cloudflare/types/radar/ai/bot_timeseries_groups_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/ai/bot_timeseries_groups_response.py">BotTimeseriesGroupsResponse</a></code>

#### Summary

Types:

```python
from cloudflare.types.radar.ai.bots import SummaryUserAgentResponse
```

Methods:

- <code title="get /radar/ai/bots/summary/user_agent">client.radar.ai.bots.summary.<a href="./src/cloudflare/resources/radar/ai/bots/summary.py">user_agent</a>(\*\*<a href="src/cloudflare/types/radar/ai/bots/summary_user_agent_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/ai/bots/summary_user_agent_response.py">SummaryUserAgentResponse</a></code>

### TimeseriesGroups

Types:

```python
from cloudflare.types.radar.ai import (
    TimeseriesGroupSummaryResponse,
    TimeseriesGroupTimeseriesResponse,
    TimeseriesGroupTimeseriesGroupsResponse,
    TimeseriesGroupUserAgentResponse,
)
```

Methods:

- <code title="get /radar/ai/bots/summary/{dimension}">client.radar.ai.timeseries_groups.<a href="./src/cloudflare/resources/radar/ai/timeseries_groups.py">summary</a>(dimension, \*\*<a href="src/cloudflare/types/radar/ai/timeseries_group_summary_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/ai/timeseries_group_summary_response.py">TimeseriesGroupSummaryResponse</a></code>
- <code title="get /radar/ai/bots/timeseries">client.radar.ai.timeseries_groups.<a href="./src/cloudflare/resources/radar/ai/timeseries_groups.py">timeseries</a>(\*\*<a href="src/cloudflare/types/radar/ai/timeseries_group_timeseries_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/ai/timeseries_group_timeseries_response.py">TimeseriesGroupTimeseriesResponse</a></code>
- <code title="get /radar/ai/bots/timeseries_groups/{dimension}">client.radar.ai.timeseries_groups.<a href="./src/cloudflare/resources/radar/ai/timeseries_groups.py">timeseries_groups</a>(dimension, \*\*<a href="src/cloudflare/types/radar/ai/timeseries_group_timeseries_groups_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/ai/timeseries_group_timeseries_groups_response.py">TimeseriesGroupTimeseriesGroupsResponse</a></code>
- <code title="get /radar/ai/bots/timeseries_groups/user_agent">client.radar.ai.timeseries_groups.<a href="./src/cloudflare/resources/radar/ai/timeseries_groups.py">user_agent</a>(\*\*<a href="src/cloudflare/types/radar/ai/timeseries_group_user_agent_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/ai/timeseries_group_user_agent_response.py">TimeseriesGroupUserAgentResponse</a></code>

### MarkdownForAgents

Types:

```python
from cloudflare.types.radar.ai import (
    MarkdownForAgentSummaryResponse,
    MarkdownForAgentTimeseriesResponse,
)
```

Methods:

- <code title="get /radar/ai/markdown_for_agents/summary">client.radar.ai.markdown_for_agents.<a href="./src/cloudflare/resources/radar/ai/markdown_for_agents.py">summary</a>(\*\*<a href="src/cloudflare/types/radar/ai/markdown_for_agent_summary_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/ai/markdown_for_agent_summary_response.py">MarkdownForAgentSummaryResponse</a></code>
- <code title="get /radar/ai/markdown_for_agents/timeseries">client.radar.ai.markdown_for_agents.<a href="./src/cloudflare/resources/radar/ai/markdown_for_agents.py">timeseries</a>(\*\*<a href="src/cloudflare/types/radar/ai/markdown_for_agent_timeseries_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/ai/markdown_for_agent_timeseries_response.py">MarkdownForAgentTimeseriesResponse</a></code>

## CT

Types:

```python
from cloudflare.types.radar import (
    CTSummaryResponse,
    CTTimeseriesResponse,
    CTTimeseriesGroupsResponse,
)
```

Methods:

- <code title="get /radar/ct/summary/{dimension}">client.radar.ct.<a href="./src/cloudflare/resources/radar/ct/ct.py">summary</a>(dimension, \*\*<a href="src/cloudflare/types/radar/ct_summary_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/ct_summary_response.py">CTSummaryResponse</a></code>
- <code title="get /radar/ct/timeseries">client.radar.ct.<a href="./src/cloudflare/resources/radar/ct/ct.py">timeseries</a>(\*\*<a href="src/cloudflare/types/radar/ct_timeseries_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/ct_timeseries_response.py">CTTimeseriesResponse</a></code>
- <code title="get /radar/ct/timeseries_groups/{dimension}">client.radar.ct.<a href="./src/cloudflare/resources/radar/ct/ct.py">timeseries_groups</a>(dimension, \*\*<a href="src/cloudflare/types/radar/ct_timeseries_groups_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/ct_timeseries_groups_response.py">CTTimeseriesGroupsResponse</a></code>

### Authorities

Types:

```python
from cloudflare.types.radar.ct import AuthorityListResponse, AuthorityGetResponse
```

Methods:

- <code title="get /radar/ct/authorities">client.radar.ct.authorities.<a href="./src/cloudflare/resources/radar/ct/authorities.py">list</a>(\*\*<a href="src/cloudflare/types/radar/ct/authority_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/ct/authority_list_response.py">AuthorityListResponse</a></code>
- <code title="get /radar/ct/authorities/{ca_slug}">client.radar.ct.authorities.<a href="./src/cloudflare/resources/radar/ct/authorities.py">get</a>(ca_slug, \*\*<a href="src/cloudflare/types/radar/ct/authority_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/ct/authority_get_response.py">AuthorityGetResponse</a></code>

### Logs

Types:

```python
from cloudflare.types.radar.ct import LogListResponse, LogGetResponse
```

Methods:

- <code title="get /radar/ct/logs">client.radar.ct.logs.<a href="./src/cloudflare/resources/radar/ct/logs.py">list</a>(\*\*<a href="src/cloudflare/types/radar/ct/log_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/ct/log_list_response.py">LogListResponse</a></code>
- <code title="get /radar/ct/logs/{log_slug}">client.radar.ct.logs.<a href="./src/cloudflare/resources/radar/ct/logs.py">get</a>(log_slug, \*\*<a href="src/cloudflare/types/radar/ct/log_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/ct/log_get_response.py">LogGetResponse</a></code>

## Annotations

Types:

```python
from cloudflare.types.radar import AnnotationListResponse
```

Methods:

- <code title="get /radar/annotations">client.radar.annotations.<a href="./src/cloudflare/resources/radar/annotations/annotations.py">list</a>(\*\*<a href="src/cloudflare/types/radar/annotation_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/annotation_list_response.py">AnnotationListResponse</a></code>

### Outages

Types:

```python
from cloudflare.types.radar.annotations import OutageGetResponse, OutageLocationsResponse
```

Methods:

- <code title="get /radar/annotations/outages">client.radar.annotations.outages.<a href="./src/cloudflare/resources/radar/annotations/outages.py">get</a>(\*\*<a href="src/cloudflare/types/radar/annotations/outage_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/annotations/outage_get_response.py">OutageGetResponse</a></code>
- <code title="get /radar/annotations/outages/locations">client.radar.annotations.outages.<a href="./src/cloudflare/resources/radar/annotations/outages.py">locations</a>(\*\*<a href="src/cloudflare/types/radar/annotations/outage_locations_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/annotations/outage_locations_response.py">OutageLocationsResponse</a></code>

## BGP

Types:

```python
from cloudflare.types.radar import BGPTimeseriesResponse
```

Methods:

- <code title="get /radar/bgp/timeseries">client.radar.bgp.<a href="./src/cloudflare/resources/radar/bgp/bgp.py">timeseries</a>(\*\*<a href="src/cloudflare/types/radar/bgp_timeseries_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bgp_timeseries_response.py">BGPTimeseriesResponse</a></code>

### Leaks

#### Events

Types:

```python
from cloudflare.types.radar.bgp.leaks import EventListResponse
```

Methods:

- <code title="get /radar/bgp/leaks/events">client.radar.bgp.leaks.events.<a href="./src/cloudflare/resources/radar/bgp/leaks/events.py">list</a>(\*\*<a href="src/cloudflare/types/radar/bgp/leaks/event_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bgp/leaks/event_list_response.py">SyncV4PagePagination[EventListResponse]</a></code>

### Top

Types:

```python
from cloudflare.types.radar.bgp import TopPrefixesResponse
```

Methods:

- <code title="get /radar/bgp/top/prefixes">client.radar.bgp.top.<a href="./src/cloudflare/resources/radar/bgp/top/top.py">prefixes</a>(\*\*<a href="src/cloudflare/types/radar/bgp/top_prefixes_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bgp/top_prefixes_response.py">TopPrefixesResponse</a></code>

#### Ases

Types:

```python
from cloudflare.types.radar.bgp.top import AseGetResponse, AsePrefixesResponse
```

Methods:

- <code title="get /radar/bgp/top/ases">client.radar.bgp.top.ases.<a href="./src/cloudflare/resources/radar/bgp/top/ases.py">get</a>(\*\*<a href="src/cloudflare/types/radar/bgp/top/ase_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bgp/top/ase_get_response.py">AseGetResponse</a></code>
- <code title="get /radar/bgp/top/ases/prefixes">client.radar.bgp.top.ases.<a href="./src/cloudflare/resources/radar/bgp/top/ases.py">prefixes</a>(\*\*<a href="src/cloudflare/types/radar/bgp/top/ase_prefixes_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bgp/top/ase_prefixes_response.py">AsePrefixesResponse</a></code>

### Hijacks

#### Events

Types:

```python
from cloudflare.types.radar.bgp.hijacks import EventListResponse
```

Methods:

- <code title="get /radar/bgp/hijacks/events">client.radar.bgp.hijacks.events.<a href="./src/cloudflare/resources/radar/bgp/hijacks/events.py">list</a>(\*\*<a href="src/cloudflare/types/radar/bgp/hijacks/event_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bgp/hijacks/event_list_response.py">SyncV4PagePagination[EventListResponse]</a></code>

### Routes

Types:

```python
from cloudflare.types.radar.bgp import (
    RouteAsesResponse,
    RouteMoasResponse,
    RoutePfx2asResponse,
    RouteRealtimeResponse,
    RouteStatsResponse,
)
```

Methods:

- <code title="get /radar/bgp/routes/ases">client.radar.bgp.routes.<a href="./src/cloudflare/resources/radar/bgp/routes.py">ases</a>(\*\*<a href="src/cloudflare/types/radar/bgp/route_ases_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bgp/route_ases_response.py">RouteAsesResponse</a></code>
- <code title="get /radar/bgp/routes/moas">client.radar.bgp.routes.<a href="./src/cloudflare/resources/radar/bgp/routes.py">moas</a>(\*\*<a href="src/cloudflare/types/radar/bgp/route_moas_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bgp/route_moas_response.py">RouteMoasResponse</a></code>
- <code title="get /radar/bgp/routes/pfx2as">client.radar.bgp.routes.<a href="./src/cloudflare/resources/radar/bgp/routes.py">pfx2as</a>(\*\*<a href="src/cloudflare/types/radar/bgp/route_pfx2as_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bgp/route_pfx2as_response.py">RoutePfx2asResponse</a></code>
- <code title="get /radar/bgp/routes/realtime">client.radar.bgp.routes.<a href="./src/cloudflare/resources/radar/bgp/routes.py">realtime</a>(\*\*<a href="src/cloudflare/types/radar/bgp/route_realtime_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bgp/route_realtime_response.py">RouteRealtimeResponse</a></code>
- <code title="get /radar/bgp/routes/stats">client.radar.bgp.routes.<a href="./src/cloudflare/resources/radar/bgp/routes.py">stats</a>(\*\*<a href="src/cloudflare/types/radar/bgp/route_stats_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bgp/route_stats_response.py">RouteStatsResponse</a></code>

### IPs

Types:

```python
from cloudflare.types.radar.bgp import IPTimeseriesResponse
```

Methods:

- <code title="get /radar/bgp/ips/timeseries">client.radar.bgp.ips.<a href="./src/cloudflare/resources/radar/bgp/ips.py">timeseries</a>(\*\*<a href="src/cloudflare/types/radar/bgp/ip_timeseries_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bgp/ip_timeseries_response.py">IPTimeseriesResponse</a></code>

### RPKI

#### ASPA

Types:

```python
from cloudflare.types.radar.bgp.rpki import (
    ASPAChangesResponse,
    ASPASnapshotResponse,
    ASPATimeseriesResponse,
)
```

Methods:

- <code title="get /radar/bgp/rpki/aspa/changes">client.radar.bgp.rpki.aspa.<a href="./src/cloudflare/resources/radar/bgp/rpki/aspa.py">changes</a>(\*\*<a href="src/cloudflare/types/radar/bgp/rpki/aspa_changes_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bgp/rpki/aspa_changes_response.py">ASPAChangesResponse</a></code>
- <code title="get /radar/bgp/rpki/aspa/snapshot">client.radar.bgp.rpki.aspa.<a href="./src/cloudflare/resources/radar/bgp/rpki/aspa.py">snapshot</a>(\*\*<a href="src/cloudflare/types/radar/bgp/rpki/aspa_snapshot_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bgp/rpki/aspa_snapshot_response.py">ASPASnapshotResponse</a></code>
- <code title="get /radar/bgp/rpki/aspa/timeseries">client.radar.bgp.rpki.aspa.<a href="./src/cloudflare/resources/radar/bgp/rpki/aspa.py">timeseries</a>(\*\*<a href="src/cloudflare/types/radar/bgp/rpki/aspa_timeseries_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bgp/rpki/aspa_timeseries_response.py">ASPATimeseriesResponse</a></code>

## Bots

Types:

```python
from cloudflare.types.radar import (
    BotListResponse,
    BotGetResponse,
    BotSummaryResponse,
    BotTimeseriesResponse,
    BotTimeseriesGroupsResponse,
)
```

Methods:

- <code title="get /radar/bots">client.radar.bots.<a href="./src/cloudflare/resources/radar/bots/bots.py">list</a>(\*\*<a href="src/cloudflare/types/radar/bot_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bot_list_response.py">BotListResponse</a></code>
- <code title="get /radar/bots/{bot_slug}">client.radar.bots.<a href="./src/cloudflare/resources/radar/bots/bots.py">get</a>(bot_slug, \*\*<a href="src/cloudflare/types/radar/bot_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bot_get_response.py">BotGetResponse</a></code>
- <code title="get /radar/bots/summary/{dimension}">client.radar.bots.<a href="./src/cloudflare/resources/radar/bots/bots.py">summary</a>(dimension, \*\*<a href="src/cloudflare/types/radar/bot_summary_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bot_summary_response.py">BotSummaryResponse</a></code>
- <code title="get /radar/bots/timeseries">client.radar.bots.<a href="./src/cloudflare/resources/radar/bots/bots.py">timeseries</a>(\*\*<a href="src/cloudflare/types/radar/bot_timeseries_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bot_timeseries_response.py">BotTimeseriesResponse</a></code>
- <code title="get /radar/bots/timeseries_groups/{dimension}">client.radar.bots.<a href="./src/cloudflare/resources/radar/bots/bots.py">timeseries_groups</a>(dimension, \*\*<a href="src/cloudflare/types/radar/bot_timeseries_groups_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bot_timeseries_groups_response.py">BotTimeseriesGroupsResponse</a></code>

### WebCrawlers

Types:

```python
from cloudflare.types.radar.bots import (
    WebCrawlerSummaryResponse,
    WebCrawlerTimeseriesGroupsResponse,
)
```

Methods:

- <code title="get /radar/bots/crawlers/summary/{dimension}">client.radar.bots.web_crawlers.<a href="./src/cloudflare/resources/radar/bots/web_crawlers.py">summary</a>(dimension, \*\*<a href="src/cloudflare/types/radar/bots/web_crawler_summary_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bots/web_crawler_summary_response.py">WebCrawlerSummaryResponse</a></code>
- <code title="get /radar/bots/crawlers/timeseries_groups/{dimension}">client.radar.bots.web_crawlers.<a href="./src/cloudflare/resources/radar/bots/web_crawlers.py">timeseries_groups</a>(dimension, \*\*<a href="src/cloudflare/types/radar/bots/web_crawler_timeseries_groups_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/bots/web_crawler_timeseries_groups_response.py">WebCrawlerTimeseriesGroupsResponse</a></code>

## Datasets

Types:

```python
from cloudflare.types.radar import DatasetListResponse, DatasetDownloadResponse, DatasetGetResponse
```

Methods:

- <code title="get /radar/datasets">client.radar.datasets.<a href="./src/cloudflare/resources/radar/datasets.py">list</a>(\*\*<a href="src/cloudflare/types/radar/dataset_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/dataset_list_response.py">DatasetListResponse</a></code>
- <code title="post /radar/datasets/download">client.radar.datasets.<a href="./src/cloudflare/resources/radar/datasets.py">download</a>(\*\*<a href="src/cloudflare/types/radar/dataset_download_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/dataset_download_response.py">DatasetDownloadResponse</a></code>
- <code title="get /radar/datasets/{alias}">client.radar.datasets.<a href="./src/cloudflare/resources/radar/datasets.py">get</a>(alias) -> str</code>

## DNS

Types:

```python
from cloudflare.types.radar import (
    DNSSummaryV2Response,
    DNSTimeseriesResponse,
    DNSTimeseriesGroupsV2Response,
)
```

Methods:

- <code title="get /radar/dns/summary/{dimension}">client.radar.dns.<a href="./src/cloudflare/resources/radar/dns/dns.py">summary_v2</a>(dimension, \*\*<a href="src/cloudflare/types/radar/dns_summary_v2_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/dns_summary_v2_response.py">DNSSummaryV2Response</a></code>
- <code title="get /radar/dns/timeseries">client.radar.dns.<a href="./src/cloudflare/resources/radar/dns/dns.py">timeseries</a>(\*\*<a href="src/cloudflare/types/radar/dns_timeseries_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/dns_timeseries_response.py">DNSTimeseriesResponse</a></code>
- <code title="get /radar/dns/timeseries_groups/{dimension}">client.radar.dns.<a href="./src/cloudflare/resources/radar/dns/dns.py">timeseries_groups_v2</a>(dimension, \*\*<a href="src/cloudflare/types/radar/dns_timeseries_groups_v2_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/dns_timeseries_groups_v2_response.py">DNSTimeseriesGroupsV2Response</a></code>

### Top

Types:

```python
from cloudflare.types.radar.dns import TopAsesResponse, TopLocationsResponse
```

Methods:

- <code title="get /radar/dns/top/ases">client.radar.dns.top.<a href="./src/cloudflare/resources/radar/dns/top.py">ases</a>(\*\*<a href="src/cloudflare/types/radar/dns/top_ases_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/dns/top_ases_response.py">TopAsesResponse</a></code>
- <code title="get /radar/dns/top/locations">client.radar.dns.top.<a href="./src/cloudflare/resources/radar/dns/top.py">locations</a>(\*\*<a href="src/cloudflare/types/radar/dns/top_locations_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/dns/top_locations_response.py">TopLocationsResponse</a></code>

### Summary

Types:

```python
from cloudflare.types.radar.dns import (
    SummaryCacheHitResponse,
    SummaryDNSSECResponse,
    SummaryDNSSECAwareResponse,
    SummaryDNSSECE2EResponse,
    SummaryIPVersionResponse,
    SummaryMatchingAnswerResponse,
    SummaryProtocolResponse,
    SummaryQueryTypeResponse,
    SummaryResponseCodeResponse,
    SummaryResponseTTLResponse,
)
```

Methods:

- <code title="get /radar/dns/summary/cache_hit">client.radar.dns.summary.<a href="./src/cloudflare/resources/radar/dns/summary.py">cache_hit</a>(\*\*<a href="src/cloudflare/types/radar/dns/summary_cache_hit_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/dns/summary_cache_hit_response.py">SummaryCacheHitResponse</a></code>
- <code title="get /radar/dns/summary/dnssec">client.radar.dns.summary.<a href="./src/cloudflare/resources/radar/dns/summary.py">dnssec</a>(\*\*<a href="src/cloudflare/types/radar/dns/summary_dnssec_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/dns/summary_dnssec_response.py">SummaryDNSSECResponse</a></code>
- <code title="get /radar/dns/summary/dnssec_aware">client.radar.dns.summary.<a href="./src/cloudflare/resources/radar/dns/summary.py">dnssec_aware</a>(\*\*<a href="src/cloudflare/types/radar/dns/summary_dnssec_aware_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/dns/summary_dnssec_aware_response.py">SummaryDNSSECAwareResponse</a></code>
- <code title="get /radar/dns/summary/dnssec_e2e">client.radar.dns.summary.<a href="./src/cloudflare/resources/radar/dns/summary.py">dnssec_e2e</a>(\*\*<a href="src/cloudflare/types/radar/dns/summary_dnssec_e2e_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/dns/summary_dnssec_e2e_response.py">SummaryDNSSECE2EResponse</a></code>
- <code title="get /radar/dns/summary/ip_version">client.radar.dns.summary.<a href="./src/cloudflare/resources/radar/dns/summary.py">ip_version</a>(\*\*<a href="src/cloudflare/types/radar/dns/summary_ip_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/dns/summary_ip_version_response.py">SummaryIPVersionResponse</a></code>
- <code title="get /radar/dns/summary/matching_answer">client.radar.dns.summary.<a href="./src/cloudflare/resources/radar/dns/summary.py">matching_answer</a>(\*\*<a href="src/cloudflare/types/radar/dns/summary_matching_answer_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/dns/summary_matching_answer_response.py">SummaryMatchingAnswerResponse</a></code>
- <code title="get /radar/dns/summary/protocol">client.radar.dns.summary.<a href="./src/cloudflare/resources/radar/dns/summary.py">protocol</a>(\*\*<a href="src/cloudflare/types/radar/dns/summary_protocol_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/dns/summary_protocol_response.py">SummaryProtocolResponse</a></code>
- <code title="get /radar/dns/summary/query_type">client.radar.dns.summary.<a href="./src/cloudflare/resources/radar/dns/summary.py">query_type</a>(\*\*<a href="src/cloudflare/types/radar/dns/summary_query_type_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/dns/summary_query_type_response.py">SummaryQueryTypeResponse</a></code>
- <code title="get /radar/dns/summary/response_code">client.radar.dns.summary.<a href="./src/cloudflare/resources/radar/dns/summary.py">response_code</a>(\*\*<a href="src/cloudflare/types/radar/dns/summary_response_code_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/dns/summary_response_code_response.py">SummaryResponseCodeResponse</a></code>
- <code title="get /radar/dns/summary/response_ttl">client.radar.dns.summary.<a href="./src/cloudflare/resources/radar/dns/summary.py">response_ttl</a>(\*\*<a href="src/cloudflare/types/radar/dns/summary_response_ttl_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/dns/summary_response_ttl_response.py">SummaryResponseTTLResponse</a></code>

### TimeseriesGroups

Types:

```python
from cloudflare.types.radar.dns import (
    TimeseriesGroupCacheHitResponse,
    TimeseriesGroupDNSSECResponse,
    TimeseriesGroupDNSSECAwareResponse,
    TimeseriesGroupDNSSECE2EResponse,
    TimeseriesGroupIPVersionResponse,
    TimeseriesGroupMatchingAnswerResponse,
    TimeseriesGroupProtocolResponse,
    TimeseriesGroupQueryTypeResponse,
    TimeseriesGroupResponseCodeResponse,
    TimeseriesGroupResponseTTLResponse,
)
```

Methods:

- <code title="get /radar/dns/timeseries_groups/cache_hit">client.radar.dns.timeseries_groups.<a href="./src/cloudflare/resources/radar/dns/timeseries_groups.py">cache_hit</a>(\*\*<a href="src/cloudflare/types/radar/dns/timeseries_group_cache_hit_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/dns/timeseries_group_cache_hit_response.py">TimeseriesGroupCacheHitResponse</a></code>
- <code title="get /radar/dns/timeseries_groups/dnssec">client.radar.dns.timeseries_groups.<a href="./src/cloudflare/resources/radar/dns/timeseries_groups.py">dnssec</a>(\*\*<a href="src/cloudflare/types/radar/dns/timeseries_group_dnssec_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/dns/timeseries_group_dnssec_response.py">TimeseriesGroupDNSSECResponse</a></code>
- <code title="get /radar/dns/timeseries_groups/dnssec_aware">client.radar.dns.timeseries_groups.<a href="./src/cloudflare/resources/radar/dns/timeseries_groups.py">dnssec_aware</a>(\*\*<a href="src/cloudflare/types/radar/dns/timeseries_group_dnssec_aware_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/dns/timeseries_group_dnssec_aware_response.py">TimeseriesGroupDNSSECAwareResponse</a></code>
- <code title="get /radar/dns/timeseries_groups/dnssec_e2e">client.radar.dns.timeseries_groups.<a href="./src/cloudflare/resources/radar/dns/timeseries_groups.py">dnssec_e2e</a>(\*\*<a href="src/cloudflare/types/radar/dns/timeseries_group_dnssec_e2e_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/dns/timeseries_group_dnssec_e2e_response.py">TimeseriesGroupDNSSECE2EResponse</a></code>
- <code title="get /radar/dns/timeseries_groups/ip_version">client.radar.dns.timeseries_groups.<a href="./src/cloudflare/resources/radar/dns/timeseries_groups.py">ip_version</a>(\*\*<a href="src/cloudflare/types/radar/dns/timeseries_group_ip_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/dns/timeseries_group_ip_version_response.py">TimeseriesGroupIPVersionResponse</a></code>
- <code title="get /radar/dns/timeseries_groups/matching_answer">client.radar.dns.timeseries_groups.<a href="./src/cloudflare/resources/radar/dns/timeseries_groups.py">matching_answer</a>(\*\*<a href="src/cloudflare/types/radar/dns/timeseries_group_matching_answer_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/dns/timeseries_group_matching_answer_response.py">TimeseriesGroupMatchingAnswerResponse</a></code>
- <code title="get /radar/dns/timeseries_groups/protocol">client.radar.dns.timeseries_groups.<a href="./src/cloudflare/resources/radar/dns/timeseries_groups.py">protocol</a>(\*\*<a href="src/cloudflare/types/radar/dns/timeseries_group_protocol_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/dns/timeseries_group_protocol_response.py">TimeseriesGroupProtocolResponse</a></code>
- <code title="get /radar/dns/timeseries_groups/query_type">client.radar.dns.timeseries_groups.<a href="./src/cloudflare/resources/radar/dns/timeseries_groups.py">query_type</a>(\*\*<a href="src/cloudflare/types/radar/dns/timeseries_group_query_type_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/dns/timeseries_group_query_type_response.py">TimeseriesGroupQueryTypeResponse</a></code>
- <code title="get /radar/dns/timeseries_groups/response_code">client.radar.dns.timeseries_groups.<a href="./src/cloudflare/resources/radar/dns/timeseries_groups.py">response_code</a>(\*\*<a href="src/cloudflare/types/radar/dns/timeseries_group_response_code_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/dns/timeseries_group_response_code_response.py">TimeseriesGroupResponseCodeResponse</a></code>
- <code title="get /radar/dns/timeseries_groups/response_ttl">client.radar.dns.timeseries_groups.<a href="./src/cloudflare/resources/radar/dns/timeseries_groups.py">response_ttl</a>(\*\*<a href="src/cloudflare/types/radar/dns/timeseries_group_response_ttl_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/dns/timeseries_group_response_ttl_response.py">TimeseriesGroupResponseTTLResponse</a></code>

## NetFlows

Types:

```python
from cloudflare.types.radar import (
    NetFlowsSummaryResponse,
    NetFlowsSummaryV2Response,
    NetFlowsTimeseriesResponse,
    NetFlowsTimeseriesGroupsResponse,
)
```

Methods:

- <code title="get /radar/netflows/summary">client.radar.netflows.<a href="./src/cloudflare/resources/radar/netflows/netflows.py">summary</a>(\*\*<a href="src/cloudflare/types/radar/netflows_summary_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/netflows_summary_response.py">NetFlowsSummaryResponse</a></code>
- <code title="get /radar/netflows/summary/{dimension}">client.radar.netflows.<a href="./src/cloudflare/resources/radar/netflows/netflows.py">summary_v2</a>(dimension, \*\*<a href="src/cloudflare/types/radar/netflows_summary_v2_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/netflows_summary_v2_response.py">NetFlowsSummaryV2Response</a></code>
- <code title="get /radar/netflows/timeseries">client.radar.netflows.<a href="./src/cloudflare/resources/radar/netflows/netflows.py">timeseries</a>(\*\*<a href="src/cloudflare/types/radar/netflows_timeseries_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/netflows_timeseries_response.py">NetFlowsTimeseriesResponse</a></code>
- <code title="get /radar/netflows/timeseries_groups/{dimension}">client.radar.netflows.<a href="./src/cloudflare/resources/radar/netflows/netflows.py">timeseries_groups</a>(dimension, \*\*<a href="src/cloudflare/types/radar/netflows_timeseries_groups_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/netflows_timeseries_groups_response.py">NetFlowsTimeseriesGroupsResponse</a></code>

### Top

Types:

```python
from cloudflare.types.radar.netflows import TopAsesResponse, TopLocationsResponse
```

Methods:

- <code title="get /radar/netflows/top/ases">client.radar.netflows.top.<a href="./src/cloudflare/resources/radar/netflows/top.py">ases</a>(\*\*<a href="src/cloudflare/types/radar/netflows/top_ases_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/netflows/top_ases_response.py">TopAsesResponse</a></code>
- <code title="get /radar/netflows/top/locations">client.radar.netflows.top.<a href="./src/cloudflare/resources/radar/netflows/top.py">locations</a>(\*\*<a href="src/cloudflare/types/radar/netflows/top_locations_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/netflows/top_locations_response.py">TopLocationsResponse</a></code>

## PostQuantum

### Origin

Types:

```python
from cloudflare.types.radar.post_quantum import (
    OriginSummaryResponse,
    OriginTimeseriesGroupsResponse,
)
```

Methods:

- <code title="get /radar/post_quantum/origin/summary/{dimension}">client.radar.post_quantum.origin.<a href="./src/cloudflare/resources/radar/post_quantum/origin.py">summary</a>(dimension, \*\*<a href="src/cloudflare/types/radar/post_quantum/origin_summary_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/post_quantum/origin_summary_response.py">OriginSummaryResponse</a></code>
- <code title="get /radar/post_quantum/origin/timeseries_groups/{dimension}">client.radar.post_quantum.origin.<a href="./src/cloudflare/resources/radar/post_quantum/origin.py">timeseries_groups</a>(dimension, \*\*<a href="src/cloudflare/types/radar/post_quantum/origin_timeseries_groups_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/post_quantum/origin_timeseries_groups_response.py">OriginTimeseriesGroupsResponse</a></code>

### TLS

Types:

```python
from cloudflare.types.radar.post_quantum import TLSSupportResponse
```

Methods:

- <code title="get /radar/post_quantum/tls/support">client.radar.post_quantum.tls.<a href="./src/cloudflare/resources/radar/post_quantum/tls.py">support</a>(\*\*<a href="src/cloudflare/types/radar/post_quantum/tls_support_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/post_quantum/tls_support_response.py">TLSSupportResponse</a></code>

## Search

Types:

```python
from cloudflare.types.radar import SearchGlobalResponse
```

Methods:

- <code title="get /radar/search/global">client.radar.search.<a href="./src/cloudflare/resources/radar/search.py">global\_</a>(\*\*<a href="src/cloudflare/types/radar/search_global_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/search_global_response.py">SearchGlobalResponse</a></code>

## VerifiedBots

### Top

Types:

```python
from cloudflare.types.radar.verified_bots import TopBotsResponse, TopCategoriesResponse
```

Methods:

- <code title="get /radar/verified_bots/top/bots">client.radar.verified_bots.top.<a href="./src/cloudflare/resources/radar/verified_bots/top.py">bots</a>(\*\*<a href="src/cloudflare/types/radar/verified_bots/top_bots_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/verified_bots/top_bots_response.py">TopBotsResponse</a></code>
- <code title="get /radar/verified_bots/top/categories">client.radar.verified_bots.top.<a href="./src/cloudflare/resources/radar/verified_bots/top.py">categories</a>(\*\*<a href="src/cloudflare/types/radar/verified_bots/top_categories_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/verified_bots/top_categories_response.py">TopCategoriesResponse</a></code>

## AS112

Types:

```python
from cloudflare.types.radar import (
    AS112SummaryV2Response,
    AS112TimeseriesResponse,
    AS112TimeseriesGroupsV2Response,
)
```

Methods:

- <code title="get /radar/as112/summary/{dimension}">client.radar.as112.<a href="./src/cloudflare/resources/radar/as112/as112.py">summary_v2</a>(dimension, \*\*<a href="src/cloudflare/types/radar/as112_summary_v2_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/as112_summary_v2_response.py">AS112SummaryV2Response</a></code>
- <code title="get /radar/as112/timeseries">client.radar.as112.<a href="./src/cloudflare/resources/radar/as112/as112.py">timeseries</a>(\*\*<a href="src/cloudflare/types/radar/as112_timeseries_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/as112_timeseries_response.py">AS112TimeseriesResponse</a></code>
- <code title="get /radar/as112/timeseries_groups/{dimension}">client.radar.as112.<a href="./src/cloudflare/resources/radar/as112/as112.py">timeseries_groups_v2</a>(dimension, \*\*<a href="src/cloudflare/types/radar/as112_timeseries_groups_v2_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/as112_timeseries_groups_v2_response.py">AS112TimeseriesGroupsV2Response</a></code>

### Summary

Types:

```python
from cloudflare.types.radar.as112 import (
    SummaryDNSSECResponse,
    SummaryEdnsResponse,
    SummaryIPVersionResponse,
    SummaryProtocolResponse,
    SummaryQueryTypeResponse,
    SummaryResponseCodesResponse,
)
```

Methods:

- <code title="get /radar/as112/summary/dnssec">client.radar.as112.summary.<a href="./src/cloudflare/resources/radar/as112/summary.py">dnssec</a>(\*\*<a href="src/cloudflare/types/radar/as112/summary_dnssec_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/as112/summary_dnssec_response.py">SummaryDNSSECResponse</a></code>
- <code title="get /radar/as112/summary/edns">client.radar.as112.summary.<a href="./src/cloudflare/resources/radar/as112/summary.py">edns</a>(\*\*<a href="src/cloudflare/types/radar/as112/summary_edns_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/as112/summary_edns_response.py">SummaryEdnsResponse</a></code>
- <code title="get /radar/as112/summary/ip_version">client.radar.as112.summary.<a href="./src/cloudflare/resources/radar/as112/summary.py">ip_version</a>(\*\*<a href="src/cloudflare/types/radar/as112/summary_ip_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/as112/summary_ip_version_response.py">SummaryIPVersionResponse</a></code>
- <code title="get /radar/as112/summary/protocol">client.radar.as112.summary.<a href="./src/cloudflare/resources/radar/as112/summary.py">protocol</a>(\*\*<a href="src/cloudflare/types/radar/as112/summary_protocol_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/as112/summary_protocol_response.py">SummaryProtocolResponse</a></code>
- <code title="get /radar/as112/summary/query_type">client.radar.as112.summary.<a href="./src/cloudflare/resources/radar/as112/summary.py">query_type</a>(\*\*<a href="src/cloudflare/types/radar/as112/summary_query_type_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/as112/summary_query_type_response.py">SummaryQueryTypeResponse</a></code>
- <code title="get /radar/as112/summary/response_codes">client.radar.as112.summary.<a href="./src/cloudflare/resources/radar/as112/summary.py">response_codes</a>(\*\*<a href="src/cloudflare/types/radar/as112/summary_response_codes_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/as112/summary_response_codes_response.py">SummaryResponseCodesResponse</a></code>

### TimeseriesGroups

Types:

```python
from cloudflare.types.radar.as112 import (
    TimeseriesGroupDNSSECResponse,
    TimeseriesGroupEdnsResponse,
    TimeseriesGroupIPVersionResponse,
    TimeseriesGroupProtocolResponse,
    TimeseriesGroupQueryTypeResponse,
    TimeseriesGroupResponseCodesResponse,
)
```

Methods:

- <code title="get /radar/as112/timeseries_groups/dnssec">client.radar.as112.timeseries_groups.<a href="./src/cloudflare/resources/radar/as112/timeseries_groups.py">dnssec</a>(\*\*<a href="src/cloudflare/types/radar/as112/timeseries_group_dnssec_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/as112/timeseries_group_dnssec_response.py">TimeseriesGroupDNSSECResponse</a></code>
- <code title="get /radar/as112/timeseries_groups/edns">client.radar.as112.timeseries_groups.<a href="./src/cloudflare/resources/radar/as112/timeseries_groups.py">edns</a>(\*\*<a href="src/cloudflare/types/radar/as112/timeseries_group_edns_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/as112/timeseries_group_edns_response.py">TimeseriesGroupEdnsResponse</a></code>
- <code title="get /radar/as112/timeseries_groups/ip_version">client.radar.as112.timeseries_groups.<a href="./src/cloudflare/resources/radar/as112/timeseries_groups.py">ip_version</a>(\*\*<a href="src/cloudflare/types/radar/as112/timeseries_group_ip_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/as112/timeseries_group_ip_version_response.py">TimeseriesGroupIPVersionResponse</a></code>
- <code title="get /radar/as112/timeseries_groups/protocol">client.radar.as112.timeseries_groups.<a href="./src/cloudflare/resources/radar/as112/timeseries_groups.py">protocol</a>(\*\*<a href="src/cloudflare/types/radar/as112/timeseries_group_protocol_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/as112/timeseries_group_protocol_response.py">TimeseriesGroupProtocolResponse</a></code>
- <code title="get /radar/as112/timeseries_groups/query_type">client.radar.as112.timeseries_groups.<a href="./src/cloudflare/resources/radar/as112/timeseries_groups.py">query_type</a>(\*\*<a href="src/cloudflare/types/radar/as112/timeseries_group_query_type_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/as112/timeseries_group_query_type_response.py">TimeseriesGroupQueryTypeResponse</a></code>
- <code title="get /radar/as112/timeseries_groups/response_codes">client.radar.as112.timeseries_groups.<a href="./src/cloudflare/resources/radar/as112/timeseries_groups.py">response_codes</a>(\*\*<a href="src/cloudflare/types/radar/as112/timeseries_group_response_codes_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/as112/timeseries_group_response_codes_response.py">TimeseriesGroupResponseCodesResponse</a></code>

### Top

Types:

```python
from cloudflare.types.radar.as112 import (
    TopDNSSECResponse,
    TopEdnsResponse,
    TopIPVersionResponse,
    TopLocationsResponse,
)
```

Methods:

- <code title="get /radar/as112/top/locations/dnssec/{dnssec}">client.radar.as112.top.<a href="./src/cloudflare/resources/radar/as112/top.py">dnssec</a>(dnssec, \*\*<a href="src/cloudflare/types/radar/as112/top_dnssec_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/as112/top_dnssec_response.py">TopDNSSECResponse</a></code>
- <code title="get /radar/as112/top/locations/edns/{edns}">client.radar.as112.top.<a href="./src/cloudflare/resources/radar/as112/top.py">edns</a>(edns, \*\*<a href="src/cloudflare/types/radar/as112/top_edns_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/as112/top_edns_response.py">TopEdnsResponse</a></code>
- <code title="get /radar/as112/top/locations/ip_version/{ip_version}">client.radar.as112.top.<a href="./src/cloudflare/resources/radar/as112/top.py">ip_version</a>(ip_version, \*\*<a href="src/cloudflare/types/radar/as112/top_ip_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/as112/top_ip_version_response.py">TopIPVersionResponse</a></code>
- <code title="get /radar/as112/top/locations">client.radar.as112.top.<a href="./src/cloudflare/resources/radar/as112/top.py">locations</a>(\*\*<a href="src/cloudflare/types/radar/as112/top_locations_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/as112/top_locations_response.py">TopLocationsResponse</a></code>

## Email

Types:

```python
from cloudflare.types.radar import RadarEmailSeries, RadarEmailSummary
```

### Routing

Types:

```python
from cloudflare.types.radar.email import RoutingSummaryV2Response, RoutingTimeseriesGroupsV2Response
```

Methods:

- <code title="get /radar/email/routing/summary/{dimension}">client.radar.email.routing.<a href="./src/cloudflare/resources/radar/email/routing/routing.py">summary_v2</a>(dimension, \*\*<a href="src/cloudflare/types/radar/email/routing_summary_v2_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/routing_summary_v2_response.py">RoutingSummaryV2Response</a></code>
- <code title="get /radar/email/routing/timeseries_groups/{dimension}">client.radar.email.routing.<a href="./src/cloudflare/resources/radar/email/routing/routing.py">timeseries_groups_v2</a>(dimension, \*\*<a href="src/cloudflare/types/radar/email/routing_timeseries_groups_v2_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/routing_timeseries_groups_v2_response.py">RoutingTimeseriesGroupsV2Response</a></code>

#### Summary

Types:

```python
from cloudflare.types.radar.email.routing import (
    SummaryARCResponse,
    SummaryDKIMResponse,
    SummaryDMARCResponse,
    SummaryEncryptedResponse,
    SummaryIPVersionResponse,
    SummarySPFResponse,
)
```

Methods:

- <code title="get /radar/email/routing/summary/arc">client.radar.email.routing.summary.<a href="./src/cloudflare/resources/radar/email/routing/summary.py">arc</a>(\*\*<a href="src/cloudflare/types/radar/email/routing/summary_arc_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/routing/summary_arc_response.py">SummaryARCResponse</a></code>
- <code title="get /radar/email/routing/summary/dkim">client.radar.email.routing.summary.<a href="./src/cloudflare/resources/radar/email/routing/summary.py">dkim</a>(\*\*<a href="src/cloudflare/types/radar/email/routing/summary_dkim_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/routing/summary_dkim_response.py">SummaryDKIMResponse</a></code>
- <code title="get /radar/email/routing/summary/dmarc">client.radar.email.routing.summary.<a href="./src/cloudflare/resources/radar/email/routing/summary.py">dmarc</a>(\*\*<a href="src/cloudflare/types/radar/email/routing/summary_dmarc_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/routing/summary_dmarc_response.py">SummaryDMARCResponse</a></code>
- <code title="get /radar/email/routing/summary/encrypted">client.radar.email.routing.summary.<a href="./src/cloudflare/resources/radar/email/routing/summary.py">encrypted</a>(\*\*<a href="src/cloudflare/types/radar/email/routing/summary_encrypted_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/routing/summary_encrypted_response.py">SummaryEncryptedResponse</a></code>
- <code title="get /radar/email/routing/summary/ip_version">client.radar.email.routing.summary.<a href="./src/cloudflare/resources/radar/email/routing/summary.py">ip_version</a>(\*\*<a href="src/cloudflare/types/radar/email/routing/summary_ip_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/routing/summary_ip_version_response.py">SummaryIPVersionResponse</a></code>
- <code title="get /radar/email/routing/summary/spf">client.radar.email.routing.summary.<a href="./src/cloudflare/resources/radar/email/routing/summary.py">spf</a>(\*\*<a href="src/cloudflare/types/radar/email/routing/summary_spf_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/routing/summary_spf_response.py">SummarySPFResponse</a></code>

#### TimeseriesGroups

Types:

```python
from cloudflare.types.radar.email.routing import (
    TimeseriesGroupARCResponse,
    TimeseriesGroupDKIMResponse,
    TimeseriesGroupDMARCResponse,
    TimeseriesGroupEncryptedResponse,
    TimeseriesGroupIPVersionResponse,
    TimeseriesGroupSPFResponse,
)
```

Methods:

- <code title="get /radar/email/routing/timeseries_groups/arc">client.radar.email.routing.timeseries_groups.<a href="./src/cloudflare/resources/radar/email/routing/timeseries_groups.py">arc</a>(\*\*<a href="src/cloudflare/types/radar/email/routing/timeseries_group_arc_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/routing/timeseries_group_arc_response.py">TimeseriesGroupARCResponse</a></code>
- <code title="get /radar/email/routing/timeseries_groups/dkim">client.radar.email.routing.timeseries_groups.<a href="./src/cloudflare/resources/radar/email/routing/timeseries_groups.py">dkim</a>(\*\*<a href="src/cloudflare/types/radar/email/routing/timeseries_group_dkim_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/routing/timeseries_group_dkim_response.py">TimeseriesGroupDKIMResponse</a></code>
- <code title="get /radar/email/routing/timeseries_groups/dmarc">client.radar.email.routing.timeseries_groups.<a href="./src/cloudflare/resources/radar/email/routing/timeseries_groups.py">dmarc</a>(\*\*<a href="src/cloudflare/types/radar/email/routing/timeseries_group_dmarc_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/routing/timeseries_group_dmarc_response.py">TimeseriesGroupDMARCResponse</a></code>
- <code title="get /radar/email/routing/timeseries_groups/encrypted">client.radar.email.routing.timeseries_groups.<a href="./src/cloudflare/resources/radar/email/routing/timeseries_groups.py">encrypted</a>(\*\*<a href="src/cloudflare/types/radar/email/routing/timeseries_group_encrypted_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/routing/timeseries_group_encrypted_response.py">TimeseriesGroupEncryptedResponse</a></code>
- <code title="get /radar/email/routing/timeseries_groups/ip_version">client.radar.email.routing.timeseries_groups.<a href="./src/cloudflare/resources/radar/email/routing/timeseries_groups.py">ip_version</a>(\*\*<a href="src/cloudflare/types/radar/email/routing/timeseries_group_ip_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/routing/timeseries_group_ip_version_response.py">TimeseriesGroupIPVersionResponse</a></code>
- <code title="get /radar/email/routing/timeseries_groups/spf">client.radar.email.routing.timeseries_groups.<a href="./src/cloudflare/resources/radar/email/routing/timeseries_groups.py">spf</a>(\*\*<a href="src/cloudflare/types/radar/email/routing/timeseries_group_spf_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/routing/timeseries_group_spf_response.py">TimeseriesGroupSPFResponse</a></code>

### Security

Types:

```python
from cloudflare.types.radar.email import (
    SecuritySummaryV2Response,
    SecurityTimeseriesGroupsV2Response,
)
```

Methods:

- <code title="get /radar/email/security/summary/{dimension}">client.radar.email.security.<a href="./src/cloudflare/resources/radar/email/security/security.py">summary_v2</a>(dimension, \*\*<a href="src/cloudflare/types/radar/email/security_summary_v2_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security_summary_v2_response.py">SecuritySummaryV2Response</a></code>
- <code title="get /radar/email/security/timeseries_groups/{dimension}">client.radar.email.security.<a href="./src/cloudflare/resources/radar/email/security/security.py">timeseries_groups_v2</a>(dimension, \*\*<a href="src/cloudflare/types/radar/email/security_timeseries_groups_v2_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security_timeseries_groups_v2_response.py">SecurityTimeseriesGroupsV2Response</a></code>

#### Top

##### TLDs

Types:

```python
from cloudflare.types.radar.email.security.top import TLDGetResponse
```

Methods:

- <code title="get /radar/email/security/top/tlds">client.radar.email.security.top.tlds.<a href="./src/cloudflare/resources/radar/email/security/top/tlds/tlds.py">get</a>(\*\*<a href="src/cloudflare/types/radar/email/security/top/tld_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/top/tld_get_response.py">TLDGetResponse</a></code>

###### Malicious

Types:

```python
from cloudflare.types.radar.email.security.top.tlds import MaliciousGetResponse
```

Methods:

- <code title="get /radar/email/security/top/tlds/malicious/{malicious}">client.radar.email.security.top.tlds.malicious.<a href="./src/cloudflare/resources/radar/email/security/top/tlds/malicious.py">get</a>(malicious, \*\*<a href="src/cloudflare/types/radar/email/security/top/tlds/malicious_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/top/tlds/malicious_get_response.py">MaliciousGetResponse</a></code>

###### Spam

Types:

```python
from cloudflare.types.radar.email.security.top.tlds import SpamGetResponse
```

Methods:

- <code title="get /radar/email/security/top/tlds/spam/{spam}">client.radar.email.security.top.tlds.spam.<a href="./src/cloudflare/resources/radar/email/security/top/tlds/spam.py">get</a>(spam, \*\*<a href="src/cloudflare/types/radar/email/security/top/tlds/spam_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/top/tlds/spam_get_response.py">SpamGetResponse</a></code>

###### Spoof

Types:

```python
from cloudflare.types.radar.email.security.top.tlds import SpoofGetResponse
```

Methods:

- <code title="get /radar/email/security/top/tlds/spoof/{spoof}">client.radar.email.security.top.tlds.spoof.<a href="./src/cloudflare/resources/radar/email/security/top/tlds/spoof.py">get</a>(spoof, \*\*<a href="src/cloudflare/types/radar/email/security/top/tlds/spoof_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/top/tlds/spoof_get_response.py">SpoofGetResponse</a></code>

#### Summary

Types:

```python
from cloudflare.types.radar.email.security import (
    SummaryARCResponse,
    SummaryDKIMResponse,
    SummaryDMARCResponse,
    SummaryMaliciousResponse,
    SummarySpamResponse,
    SummarySPFResponse,
    SummarySpoofResponse,
    SummaryThreatCategoryResponse,
    SummaryTLSVersionResponse,
)
```

Methods:

- <code title="get /radar/email/security/summary/arc">client.radar.email.security.summary.<a href="./src/cloudflare/resources/radar/email/security/summary.py">arc</a>(\*\*<a href="src/cloudflare/types/radar/email/security/summary_arc_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/summary_arc_response.py">SummaryARCResponse</a></code>
- <code title="get /radar/email/security/summary/dkim">client.radar.email.security.summary.<a href="./src/cloudflare/resources/radar/email/security/summary.py">dkim</a>(\*\*<a href="src/cloudflare/types/radar/email/security/summary_dkim_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/summary_dkim_response.py">SummaryDKIMResponse</a></code>
- <code title="get /radar/email/security/summary/dmarc">client.radar.email.security.summary.<a href="./src/cloudflare/resources/radar/email/security/summary.py">dmarc</a>(\*\*<a href="src/cloudflare/types/radar/email/security/summary_dmarc_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/summary_dmarc_response.py">SummaryDMARCResponse</a></code>
- <code title="get /radar/email/security/summary/malicious">client.radar.email.security.summary.<a href="./src/cloudflare/resources/radar/email/security/summary.py">malicious</a>(\*\*<a href="src/cloudflare/types/radar/email/security/summary_malicious_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/summary_malicious_response.py">SummaryMaliciousResponse</a></code>
- <code title="get /radar/email/security/summary/spam">client.radar.email.security.summary.<a href="./src/cloudflare/resources/radar/email/security/summary.py">spam</a>(\*\*<a href="src/cloudflare/types/radar/email/security/summary_spam_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/summary_spam_response.py">SummarySpamResponse</a></code>
- <code title="get /radar/email/security/summary/spf">client.radar.email.security.summary.<a href="./src/cloudflare/resources/radar/email/security/summary.py">spf</a>(\*\*<a href="src/cloudflare/types/radar/email/security/summary_spf_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/summary_spf_response.py">SummarySPFResponse</a></code>
- <code title="get /radar/email/security/summary/spoof">client.radar.email.security.summary.<a href="./src/cloudflare/resources/radar/email/security/summary.py">spoof</a>(\*\*<a href="src/cloudflare/types/radar/email/security/summary_spoof_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/summary_spoof_response.py">SummarySpoofResponse</a></code>
- <code title="get /radar/email/security/summary/threat_category">client.radar.email.security.summary.<a href="./src/cloudflare/resources/radar/email/security/summary.py">threat_category</a>(\*\*<a href="src/cloudflare/types/radar/email/security/summary_threat_category_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/summary_threat_category_response.py">SummaryThreatCategoryResponse</a></code>
- <code title="get /radar/email/security/summary/tls_version">client.radar.email.security.summary.<a href="./src/cloudflare/resources/radar/email/security/summary.py">tls_version</a>(\*\*<a href="src/cloudflare/types/radar/email/security/summary_tls_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/summary_tls_version_response.py">SummaryTLSVersionResponse</a></code>

#### TimeseriesGroups

Types:

```python
from cloudflare.types.radar.email.security import (
    TimeseriesGroupARCResponse,
    TimeseriesGroupDKIMResponse,
    TimeseriesGroupDMARCResponse,
    TimeseriesGroupMaliciousResponse,
    TimeseriesGroupSpamResponse,
    TimeseriesGroupSPFResponse,
    TimeseriesGroupSpoofResponse,
    TimeseriesGroupThreatCategoryResponse,
    TimeseriesGroupTLSVersionResponse,
)
```

Methods:

- <code title="get /radar/email/security/timeseries_groups/arc">client.radar.email.security.timeseries_groups.<a href="./src/cloudflare/resources/radar/email/security/timeseries_groups.py">arc</a>(\*\*<a href="src/cloudflare/types/radar/email/security/timeseries_group_arc_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/timeseries_group_arc_response.py">TimeseriesGroupARCResponse</a></code>
- <code title="get /radar/email/security/timeseries_groups/dkim">client.radar.email.security.timeseries_groups.<a href="./src/cloudflare/resources/radar/email/security/timeseries_groups.py">dkim</a>(\*\*<a href="src/cloudflare/types/radar/email/security/timeseries_group_dkim_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/timeseries_group_dkim_response.py">TimeseriesGroupDKIMResponse</a></code>
- <code title="get /radar/email/security/timeseries_groups/dmarc">client.radar.email.security.timeseries_groups.<a href="./src/cloudflare/resources/radar/email/security/timeseries_groups.py">dmarc</a>(\*\*<a href="src/cloudflare/types/radar/email/security/timeseries_group_dmarc_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/timeseries_group_dmarc_response.py">TimeseriesGroupDMARCResponse</a></code>
- <code title="get /radar/email/security/timeseries_groups/malicious">client.radar.email.security.timeseries_groups.<a href="./src/cloudflare/resources/radar/email/security/timeseries_groups.py">malicious</a>(\*\*<a href="src/cloudflare/types/radar/email/security/timeseries_group_malicious_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/timeseries_group_malicious_response.py">TimeseriesGroupMaliciousResponse</a></code>
- <code title="get /radar/email/security/timeseries_groups/spam">client.radar.email.security.timeseries_groups.<a href="./src/cloudflare/resources/radar/email/security/timeseries_groups.py">spam</a>(\*\*<a href="src/cloudflare/types/radar/email/security/timeseries_group_spam_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/timeseries_group_spam_response.py">TimeseriesGroupSpamResponse</a></code>
- <code title="get /radar/email/security/timeseries_groups/spf">client.radar.email.security.timeseries_groups.<a href="./src/cloudflare/resources/radar/email/security/timeseries_groups.py">spf</a>(\*\*<a href="src/cloudflare/types/radar/email/security/timeseries_group_spf_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/timeseries_group_spf_response.py">TimeseriesGroupSPFResponse</a></code>
- <code title="get /radar/email/security/timeseries_groups/spoof">client.radar.email.security.timeseries_groups.<a href="./src/cloudflare/resources/radar/email/security/timeseries_groups.py">spoof</a>(\*\*<a href="src/cloudflare/types/radar/email/security/timeseries_group_spoof_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/timeseries_group_spoof_response.py">TimeseriesGroupSpoofResponse</a></code>
- <code title="get /radar/email/security/timeseries_groups/threat_category">client.radar.email.security.timeseries_groups.<a href="./src/cloudflare/resources/radar/email/security/timeseries_groups.py">threat_category</a>(\*\*<a href="src/cloudflare/types/radar/email/security/timeseries_group_threat_category_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/timeseries_group_threat_category_response.py">TimeseriesGroupThreatCategoryResponse</a></code>
- <code title="get /radar/email/security/timeseries_groups/tls_version">client.radar.email.security.timeseries_groups.<a href="./src/cloudflare/resources/radar/email/security/timeseries_groups.py">tls_version</a>(\*\*<a href="src/cloudflare/types/radar/email/security/timeseries_group_tls_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/email/security/timeseries_group_tls_version_response.py">TimeseriesGroupTLSVersionResponse</a></code>

## Attacks

### Layer3

Types:

```python
from cloudflare.types.radar.attacks import (
    Layer3SummaryV2Response,
    Layer3TimeseriesResponse,
    Layer3TimeseriesGroupsV2Response,
)
```

Methods:

- <code title="get /radar/attacks/layer3/summary/{dimension}">client.radar.attacks.layer3.<a href="./src/cloudflare/resources/radar/attacks/layer3/layer3.py">summary_v2</a>(dimension, \*\*<a href="src/cloudflare/types/radar/attacks/layer3_summary_v2_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3_summary_v2_response.py">Layer3SummaryV2Response</a></code>
- <code title="get /radar/attacks/layer3/timeseries">client.radar.attacks.layer3.<a href="./src/cloudflare/resources/radar/attacks/layer3/layer3.py">timeseries</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3_timeseries_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3_timeseries_response.py">Layer3TimeseriesResponse</a></code>
- <code title="get /radar/attacks/layer3/timeseries_groups/{dimension}">client.radar.attacks.layer3.<a href="./src/cloudflare/resources/radar/attacks/layer3/layer3.py">timeseries_groups_v2</a>(dimension, \*\*<a href="src/cloudflare/types/radar/attacks/layer3_timeseries_groups_v2_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3_timeseries_groups_v2_response.py">Layer3TimeseriesGroupsV2Response</a></code>

#### Summary

Types:

```python
from cloudflare.types.radar.attacks.layer3 import (
    SummaryBitrateResponse,
    SummaryDurationResponse,
    SummaryIndustryResponse,
    SummaryIPVersionResponse,
    SummaryProtocolResponse,
    SummaryVectorResponse,
    SummaryVerticalResponse,
)
```

Methods:

- <code title="get /radar/attacks/layer3/summary/bitrate">client.radar.attacks.layer3.summary.<a href="./src/cloudflare/resources/radar/attacks/layer3/summary.py">bitrate</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/summary_bitrate_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/summary_bitrate_response.py">SummaryBitrateResponse</a></code>
- <code title="get /radar/attacks/layer3/summary/duration">client.radar.attacks.layer3.summary.<a href="./src/cloudflare/resources/radar/attacks/layer3/summary.py">duration</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/summary_duration_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/summary_duration_response.py">SummaryDurationResponse</a></code>
- <code title="get /radar/attacks/layer3/summary/industry">client.radar.attacks.layer3.summary.<a href="./src/cloudflare/resources/radar/attacks/layer3/summary.py">industry</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/summary_industry_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/summary_industry_response.py">SummaryIndustryResponse</a></code>
- <code title="get /radar/attacks/layer3/summary/ip_version">client.radar.attacks.layer3.summary.<a href="./src/cloudflare/resources/radar/attacks/layer3/summary.py">ip_version</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/summary_ip_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/summary_ip_version_response.py">SummaryIPVersionResponse</a></code>
- <code title="get /radar/attacks/layer3/summary/protocol">client.radar.attacks.layer3.summary.<a href="./src/cloudflare/resources/radar/attacks/layer3/summary.py">protocol</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/summary_protocol_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/summary_protocol_response.py">SummaryProtocolResponse</a></code>
- <code title="get /radar/attacks/layer3/summary/vector">client.radar.attacks.layer3.summary.<a href="./src/cloudflare/resources/radar/attacks/layer3/summary.py">vector</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/summary_vector_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/summary_vector_response.py">SummaryVectorResponse</a></code>
- <code title="get /radar/attacks/layer3/summary/vertical">client.radar.attacks.layer3.summary.<a href="./src/cloudflare/resources/radar/attacks/layer3/summary.py">vertical</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/summary_vertical_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/summary_vertical_response.py">SummaryVerticalResponse</a></code>

#### TimeseriesGroups

Types:

```python
from cloudflare.types.radar.attacks.layer3 import (
    TimeseriesGroupBitrateResponse,
    TimeseriesGroupDurationResponse,
    TimeseriesGroupIndustryResponse,
    TimeseriesGroupIPVersionResponse,
    TimeseriesGroupProtocolResponse,
    TimeseriesGroupVectorResponse,
    TimeseriesGroupVerticalResponse,
)
```

Methods:

- <code title="get /radar/attacks/layer3/timeseries_groups/bitrate">client.radar.attacks.layer3.timeseries_groups.<a href="./src/cloudflare/resources/radar/attacks/layer3/timeseries_groups.py">bitrate</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/timeseries_group_bitrate_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/timeseries_group_bitrate_response.py">TimeseriesGroupBitrateResponse</a></code>
- <code title="get /radar/attacks/layer3/timeseries_groups/duration">client.radar.attacks.layer3.timeseries_groups.<a href="./src/cloudflare/resources/radar/attacks/layer3/timeseries_groups.py">duration</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/timeseries_group_duration_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/timeseries_group_duration_response.py">TimeseriesGroupDurationResponse</a></code>
- <code title="get /radar/attacks/layer3/timeseries_groups/industry">client.radar.attacks.layer3.timeseries_groups.<a href="./src/cloudflare/resources/radar/attacks/layer3/timeseries_groups.py">industry</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/timeseries_group_industry_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/timeseries_group_industry_response.py">TimeseriesGroupIndustryResponse</a></code>
- <code title="get /radar/attacks/layer3/timeseries_groups/ip_version">client.radar.attacks.layer3.timeseries_groups.<a href="./src/cloudflare/resources/radar/attacks/layer3/timeseries_groups.py">ip_version</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/timeseries_group_ip_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/timeseries_group_ip_version_response.py">TimeseriesGroupIPVersionResponse</a></code>
- <code title="get /radar/attacks/layer3/timeseries_groups/protocol">client.radar.attacks.layer3.timeseries_groups.<a href="./src/cloudflare/resources/radar/attacks/layer3/timeseries_groups.py">protocol</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/timeseries_group_protocol_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/timeseries_group_protocol_response.py">TimeseriesGroupProtocolResponse</a></code>
- <code title="get /radar/attacks/layer3/timeseries_groups/vector">client.radar.attacks.layer3.timeseries_groups.<a href="./src/cloudflare/resources/radar/attacks/layer3/timeseries_groups.py">vector</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/timeseries_group_vector_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/timeseries_group_vector_response.py">TimeseriesGroupVectorResponse</a></code>
- <code title="get /radar/attacks/layer3/timeseries_groups/vertical">client.radar.attacks.layer3.timeseries_groups.<a href="./src/cloudflare/resources/radar/attacks/layer3/timeseries_groups.py">vertical</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/timeseries_group_vertical_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/timeseries_group_vertical_response.py">TimeseriesGroupVerticalResponse</a></code>

#### Top

Types:

```python
from cloudflare.types.radar.attacks.layer3 import (
    TopAttacksResponse,
    TopIndustryResponse,
    TopVerticalResponse,
)
```

Methods:

- <code title="get /radar/attacks/layer3/top/attacks">client.radar.attacks.layer3.top.<a href="./src/cloudflare/resources/radar/attacks/layer3/top/top.py">attacks</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/top_attacks_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/top_attacks_response.py">TopAttacksResponse</a></code>
- <code title="get /radar/attacks/layer3/top/industry">client.radar.attacks.layer3.top.<a href="./src/cloudflare/resources/radar/attacks/layer3/top/top.py">industry</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/top_industry_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/top_industry_response.py">TopIndustryResponse</a></code>
- <code title="get /radar/attacks/layer3/top/vertical">client.radar.attacks.layer3.top.<a href="./src/cloudflare/resources/radar/attacks/layer3/top/top.py">vertical</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/top_vertical_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/top_vertical_response.py">TopVerticalResponse</a></code>

##### Locations

Types:

```python
from cloudflare.types.radar.attacks.layer3.top import LocationOriginResponse, LocationTargetResponse
```

Methods:

- <code title="get /radar/attacks/layer3/top/locations/origin">client.radar.attacks.layer3.top.locations.<a href="./src/cloudflare/resources/radar/attacks/layer3/top/locations.py">origin</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/top/location_origin_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/top/location_origin_response.py">LocationOriginResponse</a></code>
- <code title="get /radar/attacks/layer3/top/locations/target">client.radar.attacks.layer3.top.locations.<a href="./src/cloudflare/resources/radar/attacks/layer3/top/locations.py">target</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer3/top/location_target_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer3/top/location_target_response.py">LocationTargetResponse</a></code>

### Layer7

Types:

```python
from cloudflare.types.radar.attacks import (
    Layer7SummaryV2Response,
    Layer7TimeseriesResponse,
    Layer7TimeseriesGroupsV2Response,
)
```

Methods:

- <code title="get /radar/attacks/layer7/summary/{dimension}">client.radar.attacks.layer7.<a href="./src/cloudflare/resources/radar/attacks/layer7/layer7.py">summary_v2</a>(dimension, \*\*<a href="src/cloudflare/types/radar/attacks/layer7_summary_v2_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7_summary_v2_response.py">Layer7SummaryV2Response</a></code>
- <code title="get /radar/attacks/layer7/timeseries">client.radar.attacks.layer7.<a href="./src/cloudflare/resources/radar/attacks/layer7/layer7.py">timeseries</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7_timeseries_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7_timeseries_response.py">Layer7TimeseriesResponse</a></code>
- <code title="get /radar/attacks/layer7/timeseries_groups/{dimension}">client.radar.attacks.layer7.<a href="./src/cloudflare/resources/radar/attacks/layer7/layer7.py">timeseries_groups_v2</a>(dimension, \*\*<a href="src/cloudflare/types/radar/attacks/layer7_timeseries_groups_v2_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7_timeseries_groups_v2_response.py">Layer7TimeseriesGroupsV2Response</a></code>

#### Summary

Types:

```python
from cloudflare.types.radar.attacks.layer7 import (
    SummaryHTTPMethodResponse,
    SummaryHTTPVersionResponse,
    SummaryIndustryResponse,
    SummaryIPVersionResponse,
    SummaryManagedRulesResponse,
    SummaryMitigationProductResponse,
    SummaryVerticalResponse,
)
```

Methods:

- <code title="get /radar/attacks/layer7/summary/http_method">client.radar.attacks.layer7.summary.<a href="./src/cloudflare/resources/radar/attacks/layer7/summary.py">http_method</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7/summary_http_method_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7/summary_http_method_response.py">SummaryHTTPMethodResponse</a></code>
- <code title="get /radar/attacks/layer7/summary/http_version">client.radar.attacks.layer7.summary.<a href="./src/cloudflare/resources/radar/attacks/layer7/summary.py">http_version</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7/summary_http_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7/summary_http_version_response.py">SummaryHTTPVersionResponse</a></code>
- <code title="get /radar/attacks/layer7/summary/industry">client.radar.attacks.layer7.summary.<a href="./src/cloudflare/resources/radar/attacks/layer7/summary.py">industry</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7/summary_industry_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7/summary_industry_response.py">SummaryIndustryResponse</a></code>
- <code title="get /radar/attacks/layer7/summary/ip_version">client.radar.attacks.layer7.summary.<a href="./src/cloudflare/resources/radar/attacks/layer7/summary.py">ip_version</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7/summary_ip_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7/summary_ip_version_response.py">SummaryIPVersionResponse</a></code>
- <code title="get /radar/attacks/layer7/summary/managed_rules">client.radar.attacks.layer7.summary.<a href="./src/cloudflare/resources/radar/attacks/layer7/summary.py">managed_rules</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7/summary_managed_rules_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7/summary_managed_rules_response.py">SummaryManagedRulesResponse</a></code>
- <code title="get /radar/attacks/layer7/summary/mitigation_product">client.radar.attacks.layer7.summary.<a href="./src/cloudflare/resources/radar/attacks/layer7/summary.py">mitigation_product</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7/summary_mitigation_product_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7/summary_mitigation_product_response.py">SummaryMitigationProductResponse</a></code>
- <code title="get /radar/attacks/layer7/summary/vertical">client.radar.attacks.layer7.summary.<a href="./src/cloudflare/resources/radar/attacks/layer7/summary.py">vertical</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7/summary_vertical_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7/summary_vertical_response.py">SummaryVerticalResponse</a></code>

#### TimeseriesGroups

Types:

```python
from cloudflare.types.radar.attacks.layer7 import (
    TimeseriesGroupHTTPMethodResponse,
    TimeseriesGroupHTTPVersionResponse,
    TimeseriesGroupIndustryResponse,
    TimeseriesGroupIPVersionResponse,
    TimeseriesGroupManagedRulesResponse,
    TimeseriesGroupMitigationProductResponse,
    TimeseriesGroupVerticalResponse,
)
```

Methods:

- <code title="get /radar/attacks/layer7/timeseries_groups/http_method">client.radar.attacks.layer7.timeseries_groups.<a href="./src/cloudflare/resources/radar/attacks/layer7/timeseries_groups.py">http_method</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7/timeseries_group_http_method_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7/timeseries_group_http_method_response.py">TimeseriesGroupHTTPMethodResponse</a></code>
- <code title="get /radar/attacks/layer7/timeseries_groups/http_version">client.radar.attacks.layer7.timeseries_groups.<a href="./src/cloudflare/resources/radar/attacks/layer7/timeseries_groups.py">http_version</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7/timeseries_group_http_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7/timeseries_group_http_version_response.py">TimeseriesGroupHTTPVersionResponse</a></code>
- <code title="get /radar/attacks/layer7/timeseries_groups/industry">client.radar.attacks.layer7.timeseries_groups.<a href="./src/cloudflare/resources/radar/attacks/layer7/timeseries_groups.py">industry</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7/timeseries_group_industry_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7/timeseries_group_industry_response.py">TimeseriesGroupIndustryResponse</a></code>
- <code title="get /radar/attacks/layer7/timeseries_groups/ip_version">client.radar.attacks.layer7.timeseries_groups.<a href="./src/cloudflare/resources/radar/attacks/layer7/timeseries_groups.py">ip_version</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7/timeseries_group_ip_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7/timeseries_group_ip_version_response.py">TimeseriesGroupIPVersionResponse</a></code>
- <code title="get /radar/attacks/layer7/timeseries_groups/managed_rules">client.radar.attacks.layer7.timeseries_groups.<a href="./src/cloudflare/resources/radar/attacks/layer7/timeseries_groups.py">managed_rules</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7/timeseries_group_managed_rules_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7/timeseries_group_managed_rules_response.py">TimeseriesGroupManagedRulesResponse</a></code>
- <code title="get /radar/attacks/layer7/timeseries_groups/mitigation_product">client.radar.attacks.layer7.timeseries_groups.<a href="./src/cloudflare/resources/radar/attacks/layer7/timeseries_groups.py">mitigation_product</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7/timeseries_group_mitigation_product_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7/timeseries_group_mitigation_product_response.py">TimeseriesGroupMitigationProductResponse</a></code>
- <code title="get /radar/attacks/layer7/timeseries_groups/vertical">client.radar.attacks.layer7.timeseries_groups.<a href="./src/cloudflare/resources/radar/attacks/layer7/timeseries_groups.py">vertical</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7/timeseries_group_vertical_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7/timeseries_group_vertical_response.py">TimeseriesGroupVerticalResponse</a></code>

#### Top

Types:

```python
from cloudflare.types.radar.attacks.layer7 import (
    TopAttacksResponse,
    TopIndustryResponse,
    TopVerticalResponse,
)
```

Methods:

- <code title="get /radar/attacks/layer7/top/attacks">client.radar.attacks.layer7.top.<a href="./src/cloudflare/resources/radar/attacks/layer7/top/top.py">attacks</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7/top_attacks_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7/top_attacks_response.py">TopAttacksResponse</a></code>
- <code title="get /radar/attacks/layer7/top/industry">client.radar.attacks.layer7.top.<a href="./src/cloudflare/resources/radar/attacks/layer7/top/top.py">industry</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7/top_industry_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7/top_industry_response.py">TopIndustryResponse</a></code>
- <code title="get /radar/attacks/layer7/top/vertical">client.radar.attacks.layer7.top.<a href="./src/cloudflare/resources/radar/attacks/layer7/top/top.py">vertical</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7/top_vertical_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7/top_vertical_response.py">TopVerticalResponse</a></code>

##### Locations

Types:

```python
from cloudflare.types.radar.attacks.layer7.top import LocationOriginResponse, LocationTargetResponse
```

Methods:

- <code title="get /radar/attacks/layer7/top/locations/origin">client.radar.attacks.layer7.top.locations.<a href="./src/cloudflare/resources/radar/attacks/layer7/top/locations.py">origin</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7/top/location_origin_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7/top/location_origin_response.py">LocationOriginResponse</a></code>
- <code title="get /radar/attacks/layer7/top/locations/target">client.radar.attacks.layer7.top.locations.<a href="./src/cloudflare/resources/radar/attacks/layer7/top/locations.py">target</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7/top/location_target_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7/top/location_target_response.py">LocationTargetResponse</a></code>

##### Ases

Types:

```python
from cloudflare.types.radar.attacks.layer7.top import AseOriginResponse
```

Methods:

- <code title="get /radar/attacks/layer7/top/ases/origin">client.radar.attacks.layer7.top.ases.<a href="./src/cloudflare/resources/radar/attacks/layer7/top/ases.py">origin</a>(\*\*<a href="src/cloudflare/types/radar/attacks/layer7/top/ase_origin_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/attacks/layer7/top/ase_origin_response.py">AseOriginResponse</a></code>

## Entities

Types:

```python
from cloudflare.types.radar import EntityGetResponse
```

Methods:

- <code title="get /radar/entities/ip">client.radar.entities.<a href="./src/cloudflare/resources/radar/entities/entities.py">get</a>(\*\*<a href="src/cloudflare/types/radar/entity_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/entity_get_response.py">EntityGetResponse</a></code>

### ASNs

Types:

```python
from cloudflare.types.radar.entities import (
    ASNListResponse,
    ASNAsSetResponse,
    ASNBotnetThreatFeedResponse,
    ASNGetResponse,
    ASNIPResponse,
    ASNRelResponse,
)
```

Methods:

- <code title="get /radar/entities/asns">client.radar.entities.asns.<a href="./src/cloudflare/resources/radar/entities/asns.py">list</a>(\*\*<a href="src/cloudflare/types/radar/entities/asn_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/entities/asn_list_response.py">ASNListResponse</a></code>
- <code title="get /radar/entities/asns/{asn}/as_set">client.radar.entities.asns.<a href="./src/cloudflare/resources/radar/entities/asns.py">as_set</a>(asn, \*\*<a href="src/cloudflare/types/radar/entities/asn_as_set_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/entities/asn_as_set_response.py">ASNAsSetResponse</a></code>
- <code title="get /radar/entities/asns/botnet_threat_feed">client.radar.entities.asns.<a href="./src/cloudflare/resources/radar/entities/asns.py">botnet_threat_feed</a>(\*\*<a href="src/cloudflare/types/radar/entities/asn_botnet_threat_feed_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/entities/asn_botnet_threat_feed_response.py">ASNBotnetThreatFeedResponse</a></code>
- <code title="get /radar/entities/asns/{asn}">client.radar.entities.asns.<a href="./src/cloudflare/resources/radar/entities/asns.py">get</a>(asn, \*\*<a href="src/cloudflare/types/radar/entities/asn_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/entities/asn_get_response.py">ASNGetResponse</a></code>
- <code title="get /radar/entities/asns/ip">client.radar.entities.asns.<a href="./src/cloudflare/resources/radar/entities/asns.py">ip</a>(\*\*<a href="src/cloudflare/types/radar/entities/asn_ip_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/entities/asn_ip_response.py">ASNIPResponse</a></code>
- <code title="get /radar/entities/asns/{asn}/rel">client.radar.entities.asns.<a href="./src/cloudflare/resources/radar/entities/asns.py">rel</a>(asn, \*\*<a href="src/cloudflare/types/radar/entities/asn_rel_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/entities/asn_rel_response.py">ASNRelResponse</a></code>

### Locations

Types:

```python
from cloudflare.types.radar.entities import LocationListResponse, LocationGetResponse
```

Methods:

- <code title="get /radar/entities/locations">client.radar.entities.locations.<a href="./src/cloudflare/resources/radar/entities/locations.py">list</a>(\*\*<a href="src/cloudflare/types/radar/entities/location_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/entities/location_list_response.py">LocationListResponse</a></code>
- <code title="get /radar/entities/locations/{location}">client.radar.entities.locations.<a href="./src/cloudflare/resources/radar/entities/locations.py">get</a>(location, \*\*<a href="src/cloudflare/types/radar/entities/location_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/entities/location_get_response.py">LocationGetResponse</a></code>

## Geolocations

Types:

```python
from cloudflare.types.radar import GeolocationListResponse, GeolocationGetResponse
```

Methods:

- <code title="get /radar/geolocations">client.radar.geolocations.<a href="./src/cloudflare/resources/radar/geolocations.py">list</a>(\*\*<a href="src/cloudflare/types/radar/geolocation_list_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/geolocation_list_response.py">GeolocationListResponse</a></code>
- <code title="get /radar/geolocations/{geo_id}">client.radar.geolocations.<a href="./src/cloudflare/resources/radar/geolocations.py">get</a>(geo_id, \*\*<a href="src/cloudflare/types/radar/geolocation_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/geolocation_get_response.py">GeolocationGetResponse</a></code>

## HTTP

Types:

```python
from cloudflare.types.radar import (
    HTTPSummaryV2Response,
    HTTPTimeseriesResponse,
    HTTPTimeseriesGroupsV2Response,
)
```

Methods:

- <code title="get /radar/http/summary/{dimension}">client.radar.http.<a href="./src/cloudflare/resources/radar/http/http.py">summary_v2</a>(dimension, \*\*<a href="src/cloudflare/types/radar/http_summary_v2_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http_summary_v2_response.py">HTTPSummaryV2Response</a></code>
- <code title="get /radar/http/timeseries">client.radar.http.<a href="./src/cloudflare/resources/radar/http/http.py">timeseries</a>(\*\*<a href="src/cloudflare/types/radar/http_timeseries_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http_timeseries_response.py">HTTPTimeseriesResponse</a></code>
- <code title="get /radar/http/timeseries_groups/{dimension}">client.radar.http.<a href="./src/cloudflare/resources/radar/http/http.py">timeseries_groups_v2</a>(dimension, \*\*<a href="src/cloudflare/types/radar/http_timeseries_groups_v2_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http_timeseries_groups_v2_response.py">HTTPTimeseriesGroupsV2Response</a></code>

### Locations

Types:

```python
from cloudflare.types.radar.http import LocationGetResponse
```

Methods:

- <code title="get /radar/http/top/locations">client.radar.http.locations.<a href="./src/cloudflare/resources/radar/http/locations/locations.py">get</a>(\*\*<a href="src/cloudflare/types/radar/http/location_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/location_get_response.py">LocationGetResponse</a></code>

#### BotClass

Types:

```python
from cloudflare.types.radar.http.locations import BotClassGetResponse
```

Methods:

- <code title="get /radar/http/top/locations/bot_class/{bot_class}">client.radar.http.locations.bot_class.<a href="./src/cloudflare/resources/radar/http/locations/bot_class.py">get</a>(bot_class, \*\*<a href="src/cloudflare/types/radar/http/locations/bot_class_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/locations/bot_class_get_response.py">BotClassGetResponse</a></code>

#### DeviceType

Types:

```python
from cloudflare.types.radar.http.locations import DeviceTypeGetResponse
```

Methods:

- <code title="get /radar/http/top/locations/device_type/{device_type}">client.radar.http.locations.device_type.<a href="./src/cloudflare/resources/radar/http/locations/device_type.py">get</a>(device_type, \*\*<a href="src/cloudflare/types/radar/http/locations/device_type_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/locations/device_type_get_response.py">DeviceTypeGetResponse</a></code>

#### HTTPProtocol

Types:

```python
from cloudflare.types.radar.http.locations import HTTPProtocolGetResponse
```

Methods:

- <code title="get /radar/http/top/locations/http_protocol/{http_protocol}">client.radar.http.locations.http_protocol.<a href="./src/cloudflare/resources/radar/http/locations/http_protocol.py">get</a>(http_protocol, \*\*<a href="src/cloudflare/types/radar/http/locations/http_protocol_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/locations/http_protocol_get_response.py">HTTPProtocolGetResponse</a></code>

#### HTTPMethod

Types:

```python
from cloudflare.types.radar.http.locations import HTTPMethodGetResponse
```

Methods:

- <code title="get /radar/http/top/locations/http_version/{http_version}">client.radar.http.locations.http_method.<a href="./src/cloudflare/resources/radar/http/locations/http_method.py">get</a>(http_version, \*\*<a href="src/cloudflare/types/radar/http/locations/http_method_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/locations/http_method_get_response.py">HTTPMethodGetResponse</a></code>

#### IPVersion

Types:

```python
from cloudflare.types.radar.http.locations import IPVersionGetResponse
```

Methods:

- <code title="get /radar/http/top/locations/ip_version/{ip_version}">client.radar.http.locations.ip_version.<a href="./src/cloudflare/resources/radar/http/locations/ip_version.py">get</a>(ip_version, \*\*<a href="src/cloudflare/types/radar/http/locations/ip_version_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/locations/ip_version_get_response.py">IPVersionGetResponse</a></code>

#### OS

Types:

```python
from cloudflare.types.radar.http.locations import OSGetResponse
```

Methods:

- <code title="get /radar/http/top/locations/os/{os}">client.radar.http.locations.os.<a href="./src/cloudflare/resources/radar/http/locations/os.py">get</a>(os, \*\*<a href="src/cloudflare/types/radar/http/locations/os_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/locations/os_get_response.py">OSGetResponse</a></code>

#### TLSVersion

Types:

```python
from cloudflare.types.radar.http.locations import TLSVersionGetResponse
```

Methods:

- <code title="get /radar/http/top/locations/tls_version/{tls_version}">client.radar.http.locations.tls_version.<a href="./src/cloudflare/resources/radar/http/locations/tls_version.py">get</a>(tls_version, \*\*<a href="src/cloudflare/types/radar/http/locations/tls_version_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/locations/tls_version_get_response.py">TLSVersionGetResponse</a></code>

#### BrowserFamily

Types:

```python
from cloudflare.types.radar.http.locations import BrowserFamilyGetResponse
```

Methods:

- <code title="get /radar/http/top/locations/browser_family/{browser_family}">client.radar.http.locations.browser_family.<a href="./src/cloudflare/resources/radar/http/locations/browser_family.py">get</a>(browser_family, \*\*<a href="src/cloudflare/types/radar/http/locations/browser_family_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/locations/browser_family_get_response.py">BrowserFamilyGetResponse</a></code>

### Ases

Types:

```python
from cloudflare.types.radar.http import AseGetResponse
```

Methods:

- <code title="get /radar/http/top/ases">client.radar.http.ases.<a href="./src/cloudflare/resources/radar/http/ases/ases.py">get</a>(\*\*<a href="src/cloudflare/types/radar/http/ase_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/ase_get_response.py">AseGetResponse</a></code>

#### BotClass

Types:

```python
from cloudflare.types.radar.http.ases import BotClassGetResponse
```

Methods:

- <code title="get /radar/http/top/ases/bot_class/{bot_class}">client.radar.http.ases.bot_class.<a href="./src/cloudflare/resources/radar/http/ases/bot_class.py">get</a>(bot_class, \*\*<a href="src/cloudflare/types/radar/http/ases/bot_class_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/ases/bot_class_get_response.py">BotClassGetResponse</a></code>

#### DeviceType

Types:

```python
from cloudflare.types.radar.http.ases import DeviceTypeGetResponse
```

Methods:

- <code title="get /radar/http/top/ases/device_type/{device_type}">client.radar.http.ases.device_type.<a href="./src/cloudflare/resources/radar/http/ases/device_type.py">get</a>(device_type, \*\*<a href="src/cloudflare/types/radar/http/ases/device_type_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/ases/device_type_get_response.py">DeviceTypeGetResponse</a></code>

#### HTTPProtocol

Types:

```python
from cloudflare.types.radar.http.ases import HTTPProtocolGetResponse
```

Methods:

- <code title="get /radar/http/top/ases/http_protocol/{http_protocol}">client.radar.http.ases.http_protocol.<a href="./src/cloudflare/resources/radar/http/ases/http_protocol.py">get</a>(http_protocol, \*\*<a href="src/cloudflare/types/radar/http/ases/http_protocol_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/ases/http_protocol_get_response.py">HTTPProtocolGetResponse</a></code>

#### HTTPMethod

Types:

```python
from cloudflare.types.radar.http.ases import HTTPMethodGetResponse
```

Methods:

- <code title="get /radar/http/top/ases/http_version/{http_version}">client.radar.http.ases.http_method.<a href="./src/cloudflare/resources/radar/http/ases/http_method.py">get</a>(http_version, \*\*<a href="src/cloudflare/types/radar/http/ases/http_method_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/ases/http_method_get_response.py">HTTPMethodGetResponse</a></code>

#### IPVersion

Types:

```python
from cloudflare.types.radar.http.ases import IPVersionGetResponse
```

Methods:

- <code title="get /radar/http/top/ases/ip_version/{ip_version}">client.radar.http.ases.ip_version.<a href="./src/cloudflare/resources/radar/http/ases/ip_version.py">get</a>(ip_version, \*\*<a href="src/cloudflare/types/radar/http/ases/ip_version_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/ases/ip_version_get_response.py">IPVersionGetResponse</a></code>

#### OS

Types:

```python
from cloudflare.types.radar.http.ases import OSGetResponse
```

Methods:

- <code title="get /radar/http/top/ases/os/{os}">client.radar.http.ases.os.<a href="./src/cloudflare/resources/radar/http/ases/os.py">get</a>(os, \*\*<a href="src/cloudflare/types/radar/http/ases/os_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/ases/os_get_response.py">OSGetResponse</a></code>

#### TLSVersion

Types:

```python
from cloudflare.types.radar.http.ases import TLSVersionGetResponse
```

Methods:

- <code title="get /radar/http/top/ases/tls_version/{tls_version}">client.radar.http.ases.tls_version.<a href="./src/cloudflare/resources/radar/http/ases/tls_version.py">get</a>(tls_version, \*\*<a href="src/cloudflare/types/radar/http/ases/tls_version_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/ases/tls_version_get_response.py">TLSVersionGetResponse</a></code>

#### BrowserFamily

Types:

```python
from cloudflare.types.radar.http.ases import BrowserFamilyGetResponse
```

Methods:

- <code title="get /radar/http/top/ases/browser_family/{browser_family}">client.radar.http.ases.browser_family.<a href="./src/cloudflare/resources/radar/http/ases/browser_family.py">get</a>(browser_family, \*\*<a href="src/cloudflare/types/radar/http/ases/browser_family_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/ases/browser_family_get_response.py">BrowserFamilyGetResponse</a></code>

### Summary

Types:

```python
from cloudflare.types.radar.http import (
    SummaryBotClassResponse,
    SummaryDeviceTypeResponse,
    SummaryHTTPProtocolResponse,
    SummaryHTTPVersionResponse,
    SummaryIPVersionResponse,
    SummaryOSResponse,
    SummaryPostQuantumResponse,
    SummaryTLSVersionResponse,
)
```

Methods:

- <code title="get /radar/http/summary/bot_class">client.radar.http.summary.<a href="./src/cloudflare/resources/radar/http/summary.py">bot_class</a>(\*\*<a href="src/cloudflare/types/radar/http/summary_bot_class_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/summary_bot_class_response.py">SummaryBotClassResponse</a></code>
- <code title="get /radar/http/summary/device_type">client.radar.http.summary.<a href="./src/cloudflare/resources/radar/http/summary.py">device_type</a>(\*\*<a href="src/cloudflare/types/radar/http/summary_device_type_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/summary_device_type_response.py">SummaryDeviceTypeResponse</a></code>
- <code title="get /radar/http/summary/http_protocol">client.radar.http.summary.<a href="./src/cloudflare/resources/radar/http/summary.py">http_protocol</a>(\*\*<a href="src/cloudflare/types/radar/http/summary_http_protocol_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/summary_http_protocol_response.py">SummaryHTTPProtocolResponse</a></code>
- <code title="get /radar/http/summary/http_version">client.radar.http.summary.<a href="./src/cloudflare/resources/radar/http/summary.py">http_version</a>(\*\*<a href="src/cloudflare/types/radar/http/summary_http_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/summary_http_version_response.py">SummaryHTTPVersionResponse</a></code>
- <code title="get /radar/http/summary/ip_version">client.radar.http.summary.<a href="./src/cloudflare/resources/radar/http/summary.py">ip_version</a>(\*\*<a href="src/cloudflare/types/radar/http/summary_ip_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/summary_ip_version_response.py">SummaryIPVersionResponse</a></code>
- <code title="get /radar/http/summary/os">client.radar.http.summary.<a href="./src/cloudflare/resources/radar/http/summary.py">os</a>(\*\*<a href="src/cloudflare/types/radar/http/summary_os_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/summary_os_response.py">SummaryOSResponse</a></code>
- <code title="get /radar/http/summary/post_quantum">client.radar.http.summary.<a href="./src/cloudflare/resources/radar/http/summary.py">post_quantum</a>(\*\*<a href="src/cloudflare/types/radar/http/summary_post_quantum_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/summary_post_quantum_response.py">SummaryPostQuantumResponse</a></code>
- <code title="get /radar/http/summary/tls_version">client.radar.http.summary.<a href="./src/cloudflare/resources/radar/http/summary.py">tls_version</a>(\*\*<a href="src/cloudflare/types/radar/http/summary_tls_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/summary_tls_version_response.py">SummaryTLSVersionResponse</a></code>

### TimeseriesGroups

Types:

```python
from cloudflare.types.radar.http import (
    TimeseriesGroupBotClassResponse,
    TimeseriesGroupBrowserResponse,
    TimeseriesGroupBrowserFamilyResponse,
    TimeseriesGroupDeviceTypeResponse,
    TimeseriesGroupHTTPProtocolResponse,
    TimeseriesGroupHTTPVersionResponse,
    TimeseriesGroupIPVersionResponse,
    TimeseriesGroupOSResponse,
    TimeseriesGroupPostQuantumResponse,
    TimeseriesGroupTLSVersionResponse,
)
```

Methods:

- <code title="get /radar/http/timeseries_groups/bot_class">client.radar.http.timeseries_groups.<a href="./src/cloudflare/resources/radar/http/timeseries_groups.py">bot_class</a>(\*\*<a href="src/cloudflare/types/radar/http/timeseries_group_bot_class_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/timeseries_group_bot_class_response.py">TimeseriesGroupBotClassResponse</a></code>
- <code title="get /radar/http/timeseries_groups/browser">client.radar.http.timeseries_groups.<a href="./src/cloudflare/resources/radar/http/timeseries_groups.py">browser</a>(\*\*<a href="src/cloudflare/types/radar/http/timeseries_group_browser_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/timeseries_group_browser_response.py">TimeseriesGroupBrowserResponse</a></code>
- <code title="get /radar/http/timeseries_groups/browser_family">client.radar.http.timeseries_groups.<a href="./src/cloudflare/resources/radar/http/timeseries_groups.py">browser_family</a>(\*\*<a href="src/cloudflare/types/radar/http/timeseries_group_browser_family_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/timeseries_group_browser_family_response.py">TimeseriesGroupBrowserFamilyResponse</a></code>
- <code title="get /radar/http/timeseries_groups/device_type">client.radar.http.timeseries_groups.<a href="./src/cloudflare/resources/radar/http/timeseries_groups.py">device_type</a>(\*\*<a href="src/cloudflare/types/radar/http/timeseries_group_device_type_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/timeseries_group_device_type_response.py">TimeseriesGroupDeviceTypeResponse</a></code>
- <code title="get /radar/http/timeseries_groups/http_protocol">client.radar.http.timeseries_groups.<a href="./src/cloudflare/resources/radar/http/timeseries_groups.py">http_protocol</a>(\*\*<a href="src/cloudflare/types/radar/http/timeseries_group_http_protocol_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/timeseries_group_http_protocol_response.py">TimeseriesGroupHTTPProtocolResponse</a></code>
- <code title="get /radar/http/timeseries_groups/http_version">client.radar.http.timeseries_groups.<a href="./src/cloudflare/resources/radar/http/timeseries_groups.py">http_version</a>(\*\*<a href="src/cloudflare/types/radar/http/timeseries_group_http_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/timeseries_group_http_version_response.py">TimeseriesGroupHTTPVersionResponse</a></code>
- <code title="get /radar/http/timeseries_groups/ip_version">client.radar.http.timeseries_groups.<a href="./src/cloudflare/resources/radar/http/timeseries_groups.py">ip_version</a>(\*\*<a href="src/cloudflare/types/radar/http/timeseries_group_ip_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/timeseries_group_ip_version_response.py">TimeseriesGroupIPVersionResponse</a></code>
- <code title="get /radar/http/timeseries_groups/os">client.radar.http.timeseries_groups.<a href="./src/cloudflare/resources/radar/http/timeseries_groups.py">os</a>(\*\*<a href="src/cloudflare/types/radar/http/timeseries_group_os_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/timeseries_group_os_response.py">TimeseriesGroupOSResponse</a></code>
- <code title="get /radar/http/timeseries_groups/post_quantum">client.radar.http.timeseries_groups.<a href="./src/cloudflare/resources/radar/http/timeseries_groups.py">post_quantum</a>(\*\*<a href="src/cloudflare/types/radar/http/timeseries_group_post_quantum_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/timeseries_group_post_quantum_response.py">TimeseriesGroupPostQuantumResponse</a></code>
- <code title="get /radar/http/timeseries_groups/tls_version">client.radar.http.timeseries_groups.<a href="./src/cloudflare/resources/radar/http/timeseries_groups.py">tls_version</a>(\*\*<a href="src/cloudflare/types/radar/http/timeseries_group_tls_version_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/timeseries_group_tls_version_response.py">TimeseriesGroupTLSVersionResponse</a></code>

### Top

Types:

```python
from cloudflare.types.radar.http import TopBrowserResponse, TopBrowserFamilyResponse
```

Methods:

- <code title="get /radar/http/top/browser">client.radar.http.top.<a href="./src/cloudflare/resources/radar/http/top.py">browser</a>(\*\*<a href="src/cloudflare/types/radar/http/top_browser_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/top_browser_response.py">TopBrowserResponse</a></code>
- <code title="get /radar/http/top/browser_family">client.radar.http.top.<a href="./src/cloudflare/resources/radar/http/top.py">browser_family</a>(\*\*<a href="src/cloudflare/types/radar/http/top_browser_family_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/http/top_browser_family_response.py">TopBrowserFamilyResponse</a></code>

## Quality

### IQI

Types:

```python
from cloudflare.types.radar.quality import IQISummaryResponse, IQITimeseriesGroupsResponse
```

Methods:

- <code title="get /radar/quality/iqi/summary">client.radar.quality.iqi.<a href="./src/cloudflare/resources/radar/quality/iqi.py">summary</a>(\*\*<a href="src/cloudflare/types/radar/quality/iqi_summary_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/quality/iqi_summary_response.py">IQISummaryResponse</a></code>
- <code title="get /radar/quality/iqi/timeseries_groups">client.radar.quality.iqi.<a href="./src/cloudflare/resources/radar/quality/iqi.py">timeseries_groups</a>(\*\*<a href="src/cloudflare/types/radar/quality/iqi_timeseries_groups_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/quality/iqi_timeseries_groups_response.py">IQITimeseriesGroupsResponse</a></code>

### Speed

Types:

```python
from cloudflare.types.radar.quality import SpeedHistogramResponse, SpeedSummaryResponse
```

Methods:

- <code title="get /radar/quality/speed/histogram">client.radar.quality.speed.<a href="./src/cloudflare/resources/radar/quality/speed/speed.py">histogram</a>(\*\*<a href="src/cloudflare/types/radar/quality/speed_histogram_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/quality/speed_histogram_response.py">SpeedHistogramResponse</a></code>
- <code title="get /radar/quality/speed/summary">client.radar.quality.speed.<a href="./src/cloudflare/resources/radar/quality/speed/speed.py">summary</a>(\*\*<a href="src/cloudflare/types/radar/quality/speed_summary_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/quality/speed_summary_response.py">SpeedSummaryResponse</a></code>

#### Top

Types:

```python
from cloudflare.types.radar.quality.speed import TopAsesResponse, TopLocationsResponse
```

Methods:

- <code title="get /radar/quality/speed/top/ases">client.radar.quality.speed.top.<a href="./src/cloudflare/resources/radar/quality/speed/top.py">ases</a>(\*\*<a href="src/cloudflare/types/radar/quality/speed/top_ases_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/quality/speed/top_ases_response.py">TopAsesResponse</a></code>
- <code title="get /radar/quality/speed/top/locations">client.radar.quality.speed.top.<a href="./src/cloudflare/resources/radar/quality/speed/top.py">locations</a>(\*\*<a href="src/cloudflare/types/radar/quality/speed/top_locations_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/quality/speed/top_locations_response.py">TopLocationsResponse</a></code>

## Ranking

Types:

```python
from cloudflare.types.radar import RankingTimeseriesGroupsResponse, RankingTopResponse
```

Methods:

- <code title="get /radar/ranking/timeseries_groups">client.radar.ranking.<a href="./src/cloudflare/resources/radar/ranking/ranking.py">timeseries_groups</a>(\*\*<a href="src/cloudflare/types/radar/ranking_timeseries_groups_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/ranking_timeseries_groups_response.py">RankingTimeseriesGroupsResponse</a></code>
- <code title="get /radar/ranking/top">client.radar.ranking.<a href="./src/cloudflare/resources/radar/ranking/ranking.py">top</a>(\*\*<a href="src/cloudflare/types/radar/ranking_top_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/ranking_top_response.py">RankingTopResponse</a></code>

### Domain

Types:

```python
from cloudflare.types.radar.ranking import DomainGetResponse
```

Methods:

- <code title="get /radar/ranking/domain/{domain}">client.radar.ranking.domain.<a href="./src/cloudflare/resources/radar/ranking/domain.py">get</a>(domain, \*\*<a href="src/cloudflare/types/radar/ranking/domain_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/ranking/domain_get_response.py">DomainGetResponse</a></code>

### InternetServices

Types:

```python
from cloudflare.types.radar.ranking import (
    InternetServiceCategoriesResponse,
    InternetServiceTimeseriesGroupsResponse,
    InternetServiceTopResponse,
)
```

Methods:

- <code title="get /radar/ranking/internet_services/categories">client.radar.ranking.internet_services.<a href="./src/cloudflare/resources/radar/ranking/internet_services.py">categories</a>(\*\*<a href="src/cloudflare/types/radar/ranking/internet_service_categories_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/ranking/internet_service_categories_response.py">InternetServiceCategoriesResponse</a></code>
- <code title="get /radar/ranking/internet_services/timeseries_groups">client.radar.ranking.internet_services.<a href="./src/cloudflare/resources/radar/ranking/internet_services.py">timeseries_groups</a>(\*\*<a href="src/cloudflare/types/radar/ranking/internet_service_timeseries_groups_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/ranking/internet_service_timeseries_groups_response.py">InternetServiceTimeseriesGroupsResponse</a></code>
- <code title="get /radar/ranking/internet_services/top">client.radar.ranking.internet_services.<a href="./src/cloudflare/resources/radar/ranking/internet_services.py">top</a>(\*\*<a href="src/cloudflare/types/radar/ranking/internet_service_top_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/ranking/internet_service_top_response.py">InternetServiceTopResponse</a></code>

## TrafficAnomalies

Types:

```python
from cloudflare.types.radar import TrafficAnomalyGetResponse
```

Methods:

- <code title="get /radar/traffic_anomalies">client.radar.traffic_anomalies.<a href="./src/cloudflare/resources/radar/traffic_anomalies/traffic_anomalies.py">get</a>(\*\*<a href="src/cloudflare/types/radar/traffic_anomaly_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/traffic_anomaly_get_response.py">TrafficAnomalyGetResponse</a></code>

### Locations

Types:

```python
from cloudflare.types.radar.traffic_anomalies import LocationGetResponse
```

Methods:

- <code title="get /radar/traffic_anomalies/locations">client.radar.traffic_anomalies.locations.<a href="./src/cloudflare/resources/radar/traffic_anomalies/locations.py">get</a>(\*\*<a href="src/cloudflare/types/radar/traffic_anomalies/location_get_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/traffic_anomalies/location_get_response.py">LocationGetResponse</a></code>

## TCPResetsTimeouts

Types:

```python
from cloudflare.types.radar import (
    TCPResetsTimeoutSummaryResponse,
    TCPResetsTimeoutTimeseriesGroupsResponse,
)
```

Methods:

- <code title="get /radar/tcp_resets_timeouts/summary">client.radar.tcp_resets_timeouts.<a href="./src/cloudflare/resources/radar/tcp_resets_timeouts.py">summary</a>(\*\*<a href="src/cloudflare/types/radar/tcp_resets_timeout_summary_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/tcp_resets_timeout_summary_response.py">TCPResetsTimeoutSummaryResponse</a></code>
- <code title="get /radar/tcp_resets_timeouts/timeseries_groups">client.radar.tcp_resets_timeouts.<a href="./src/cloudflare/resources/radar/tcp_resets_timeouts.py">timeseries_groups</a>(\*\*<a href="src/cloudflare/types/radar/tcp_resets_timeout_timeseries_groups_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/tcp_resets_timeout_timeseries_groups_response.py">TCPResetsTimeoutTimeseriesGroupsResponse</a></code>

## RobotsTXT

### Top

Types:

```python
from cloudflare.types.radar.robots_txt import TopDomainCategoriesResponse
```

Methods:

- <code title="get /radar/robots_txt/top/domain_categories">client.radar.robots_txt.top.<a href="./src/cloudflare/resources/radar/robots_txt/top/top.py">domain_categories</a>(\*\*<a href="src/cloudflare/types/radar/robots_txt/top_domain_categories_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/robots_txt/top_domain_categories_response.py">TopDomainCategoriesResponse</a></code>

#### UserAgents

Types:

```python
from cloudflare.types.radar.robots_txt.top import UserAgentDirectiveResponse
```

Methods:

- <code title="get /radar/robots_txt/top/user_agents/directive">client.radar.robots_txt.top.user_agents.<a href="./src/cloudflare/resources/radar/robots_txt/top/user_agents.py">directive</a>(\*\*<a href="src/cloudflare/types/radar/robots_txt/top/user_agent_directive_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/robots_txt/top/user_agent_directive_response.py">UserAgentDirectiveResponse</a></code>

## LeakedCredentials

Types:

```python
from cloudflare.types.radar import (
    LeakedCredentialSummaryV2Response,
    LeakedCredentialTimeseriesGroupsV2Response,
)
```

Methods:

- <code title="get /radar/leaked_credential_checks/summary/{dimension}">client.radar.leaked_credentials.<a href="./src/cloudflare/resources/radar/leaked_credentials/leaked_credentials.py">summary_v2</a>(dimension, \*\*<a href="src/cloudflare/types/radar/leaked_credential_summary_v2_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/leaked_credential_summary_v2_response.py">LeakedCredentialSummaryV2Response</a></code>
- <code title="get /radar/leaked_credential_checks/timeseries_groups/{dimension}">client.radar.leaked_credentials.<a href="./src/cloudflare/resources/radar/leaked_credentials/leaked_credentials.py">timeseries_groups_v2</a>(dimension, \*\*<a href="src/cloudflare/types/radar/leaked_credential_timeseries_groups_v2_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/leaked_credential_timeseries_groups_v2_response.py">LeakedCredentialTimeseriesGroupsV2Response</a></code>

### Summary

Types:

```python
from cloudflare.types.radar.leaked_credentials import (
    SummaryBotClassResponse,
    SummaryCompromisedResponse,
)
```

Methods:

- <code title="get /radar/leaked_credential_checks/summary/bot_class">client.radar.leaked_credentials.summary.<a href="./src/cloudflare/resources/radar/leaked_credentials/summary.py">bot_class</a>(\*\*<a href="src/cloudflare/types/radar/leaked_credentials/summary_bot_class_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/leaked_credentials/summary_bot_class_response.py">SummaryBotClassResponse</a></code>
- <code title="get /radar/leaked_credential_checks/summary/compromised">client.radar.leaked_credentials.summary.<a href="./src/cloudflare/resources/radar/leaked_credentials/summary.py">compromised</a>(\*\*<a href="src/cloudflare/types/radar/leaked_credentials/summary_compromised_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/leaked_credentials/summary_compromised_response.py">SummaryCompromisedResponse</a></code>

### TimeseriesGroups

Types:

```python
from cloudflare.types.radar.leaked_credentials import (
    TimeseriesGroupBotClassResponse,
    TimeseriesGroupCompromisedResponse,
)
```

Methods:

- <code title="get /radar/leaked_credential_checks/timeseries_groups/bot_class">client.radar.leaked_credentials.timeseries_groups.<a href="./src/cloudflare/resources/radar/leaked_credentials/timeseries_groups.py">bot_class</a>(\*\*<a href="src/cloudflare/types/radar/leaked_credentials/timeseries_group_bot_class_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/leaked_credentials/timeseries_group_bot_class_response.py">TimeseriesGroupBotClassResponse</a></code>
- <code title="get /radar/leaked_credential_checks/timeseries_groups/compromised">client.radar.leaked_credentials.timeseries_groups.<a href="./src/cloudflare/resources/radar/leaked_credentials/timeseries_groups.py">compromised</a>(\*\*<a href="src/cloudflare/types/radar/leaked_credentials/timeseries_group_compromised_params.py">params</a>) -> <a href="./src/cloudflare/types/radar/leaked_credentials/timeseries_group_compromised_response.py">TimeseriesGroupCompromisedResponse</a></code>
