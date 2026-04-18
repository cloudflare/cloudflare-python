# Pipelines

Types:

```python
from cloudflare.types.pipelines import (
    PipelineCreateResponse,
    PipelineUpdateResponse,
    PipelineListResponse,
    PipelineGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/pipelines">client.pipelines.<a href="./src/cloudflare/resources/pipelines/pipelines.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/pipelines/pipeline_create_params.py">params</a>) -> <a href="./src/cloudflare/types/pipelines/pipeline_create_response.py">PipelineCreateResponse</a></code>
- <code title="put /accounts/{account_id}/pipelines/{pipeline_name}">client.pipelines.<a href="./src/cloudflare/resources/pipelines/pipelines.py">update</a>(pipeline_name, \*, account_id, \*\*<a href="src/cloudflare/types/pipelines/pipeline_update_params.py">params</a>) -> <a href="./src/cloudflare/types/pipelines/pipeline_update_response.py">PipelineUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/pipelines">client.pipelines.<a href="./src/cloudflare/resources/pipelines/pipelines.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/pipelines/pipeline_list_params.py">params</a>) -> <a href="./src/cloudflare/types/pipelines/pipeline_list_response.py">PipelineListResponse</a></code>
- <code title="delete /accounts/{account_id}/pipelines/{pipeline_name}">client.pipelines.<a href="./src/cloudflare/resources/pipelines/pipelines.py">delete</a>(pipeline_name, \*, account_id) -> None</code>
- <code title="get /accounts/{account_id}/pipelines/{pipeline_name}">client.pipelines.<a href="./src/cloudflare/resources/pipelines/pipelines.py">get</a>(pipeline_name, \*, account_id) -> <a href="./src/cloudflare/types/pipelines/pipeline_get_response.py">PipelineGetResponse</a></code>
