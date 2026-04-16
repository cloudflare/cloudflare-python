# Pipelines

Types:

```python
from cloudflare.types.pipelines import (
    PipelineCreateResponse,
    PipelineUpdateResponse,
    PipelineListResponse,
    PipelineCreateV1Response,
    PipelineGetResponse,
    PipelineGetV1Response,
    PipelineListV1Response,
    PipelineValidateSqlResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/pipelines">client.pipelines.<a href="./src/cloudflare/resources/pipelines/pipelines.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/pipelines/pipeline_create_params.py">params</a>) -> <a href="./src/cloudflare/types/pipelines/pipeline_create_response.py">PipelineCreateResponse</a></code>
- <code title="put /accounts/{account_id}/pipelines/{pipeline_name}">client.pipelines.<a href="./src/cloudflare/resources/pipelines/pipelines.py">update</a>(pipeline_name, \*, account_id, \*\*<a href="src/cloudflare/types/pipelines/pipeline_update_params.py">params</a>) -> <a href="./src/cloudflare/types/pipelines/pipeline_update_response.py">PipelineUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/pipelines">client.pipelines.<a href="./src/cloudflare/resources/pipelines/pipelines.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/pipelines/pipeline_list_params.py">params</a>) -> <a href="./src/cloudflare/types/pipelines/pipeline_list_response.py">PipelineListResponse</a></code>
- <code title="delete /accounts/{account_id}/pipelines/{pipeline_name}">client.pipelines.<a href="./src/cloudflare/resources/pipelines/pipelines.py">delete</a>(pipeline_name, \*, account_id) -> None</code>
- <code title="post /accounts/{account_id}/pipelines/v1/pipelines">client.pipelines.<a href="./src/cloudflare/resources/pipelines/pipelines.py">create_v1</a>(\*, account_id, \*\*<a href="src/cloudflare/types/pipelines/pipeline_create_v1_params.py">params</a>) -> <a href="./src/cloudflare/types/pipelines/pipeline_create_v1_response.py">PipelineCreateV1Response</a></code>
- <code title="delete /accounts/{account_id}/pipelines/v1/pipelines/{pipeline_id}">client.pipelines.<a href="./src/cloudflare/resources/pipelines/pipelines.py">delete_v1</a>(pipeline_id, \*, account_id) -> object</code>
- <code title="get /accounts/{account_id}/pipelines/{pipeline_name}">client.pipelines.<a href="./src/cloudflare/resources/pipelines/pipelines.py">get</a>(pipeline_name, \*, account_id) -> <a href="./src/cloudflare/types/pipelines/pipeline_get_response.py">PipelineGetResponse</a></code>
- <code title="get /accounts/{account_id}/pipelines/v1/pipelines/{pipeline_id}">client.pipelines.<a href="./src/cloudflare/resources/pipelines/pipelines.py">get_v1</a>(pipeline_id, \*, account_id) -> <a href="./src/cloudflare/types/pipelines/pipeline_get_v1_response.py">PipelineGetV1Response</a></code>
- <code title="get /accounts/{account_id}/pipelines/v1/pipelines">client.pipelines.<a href="./src/cloudflare/resources/pipelines/pipelines.py">list_v1</a>(\*, account_id, \*\*<a href="src/cloudflare/types/pipelines/pipeline_list_v1_params.py">params</a>) -> <a href="./src/cloudflare/types/pipelines/pipeline_list_v1_response.py">SyncV4PagePaginationArray[PipelineListV1Response]</a></code>
- <code title="post /accounts/{account_id}/pipelines/v1/validate_sql">client.pipelines.<a href="./src/cloudflare/resources/pipelines/pipelines.py">validate_sql</a>(\*, account_id, \*\*<a href="src/cloudflare/types/pipelines/pipeline_validate_sql_params.py">params</a>) -> <a href="./src/cloudflare/types/pipelines/pipeline_validate_sql_response.py">PipelineValidateSqlResponse</a></code>

## Sinks

Types:

```python
from cloudflare.types.pipelines import SinkCreateResponse, SinkListResponse, SinkGetResponse
```

Methods:

- <code title="post /accounts/{account_id}/pipelines/v1/sinks">client.pipelines.sinks.<a href="./src/cloudflare/resources/pipelines/sinks.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/pipelines/sink_create_params.py">params</a>) -> <a href="./src/cloudflare/types/pipelines/sink_create_response.py">SinkCreateResponse</a></code>
- <code title="get /accounts/{account_id}/pipelines/v1/sinks">client.pipelines.sinks.<a href="./src/cloudflare/resources/pipelines/sinks.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/pipelines/sink_list_params.py">params</a>) -> <a href="./src/cloudflare/types/pipelines/sink_list_response.py">SyncV4PagePaginationArray[SinkListResponse]</a></code>
- <code title="delete /accounts/{account_id}/pipelines/v1/sinks/{sink_id}">client.pipelines.sinks.<a href="./src/cloudflare/resources/pipelines/sinks.py">delete</a>(sink_id, \*, account_id, \*\*<a href="src/cloudflare/types/pipelines/sink_delete_params.py">params</a>) -> object</code>
- <code title="get /accounts/{account_id}/pipelines/v1/sinks/{sink_id}">client.pipelines.sinks.<a href="./src/cloudflare/resources/pipelines/sinks.py">get</a>(sink_id, \*, account_id) -> <a href="./src/cloudflare/types/pipelines/sink_get_response.py">SinkGetResponse</a></code>

## Streams

Types:

```python
from cloudflare.types.pipelines import (
    StreamCreateResponse,
    StreamUpdateResponse,
    StreamListResponse,
    StreamGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/pipelines/v1/streams">client.pipelines.streams.<a href="./src/cloudflare/resources/pipelines/streams.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/pipelines/stream_create_params.py">params</a>) -> <a href="./src/cloudflare/types/pipelines/stream_create_response.py">StreamCreateResponse</a></code>
- <code title="patch /accounts/{account_id}/pipelines/v1/streams/{stream_id}">client.pipelines.streams.<a href="./src/cloudflare/resources/pipelines/streams.py">update</a>(stream_id, \*, account_id, \*\*<a href="src/cloudflare/types/pipelines/stream_update_params.py">params</a>) -> <a href="./src/cloudflare/types/pipelines/stream_update_response.py">StreamUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/pipelines/v1/streams">client.pipelines.streams.<a href="./src/cloudflare/resources/pipelines/streams.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/pipelines/stream_list_params.py">params</a>) -> <a href="./src/cloudflare/types/pipelines/stream_list_response.py">SyncV4PagePaginationArray[StreamListResponse]</a></code>
- <code title="delete /accounts/{account_id}/pipelines/v1/streams/{stream_id}">client.pipelines.streams.<a href="./src/cloudflare/resources/pipelines/streams.py">delete</a>(stream_id, \*, account_id, \*\*<a href="src/cloudflare/types/pipelines/stream_delete_params.py">params</a>) -> object</code>
- <code title="get /accounts/{account_id}/pipelines/v1/streams/{stream_id}">client.pipelines.streams.<a href="./src/cloudflare/resources/pipelines/streams.py">get</a>(stream_id, \*, account_id) -> <a href="./src/cloudflare/types/pipelines/stream_get_response.py">StreamGetResponse</a></code>
