# AI

Types:

```python
from cloudflare.types.ai import AIRunResponse
```

Methods:

- <code title="post /accounts/{account_id}/ai/run/{model_name}">client.ai.<a href="./src/cloudflare/resources/ai/ai.py">run</a>(model_name, \*, account_id, \*\*<a href="src/cloudflare/types/ai/ai_run_params.py">params</a>) -> <a href="./src/cloudflare/types/ai/ai_run_response.py">Optional[AIRunResponse]</a></code>

## Finetunes

Types:

```python
from cloudflare.types.ai import FinetuneCreateResponse, FinetuneListResponse
```

Methods:

- <code title="post /accounts/{account_id}/ai/finetunes">client.ai.finetunes.<a href="./src/cloudflare/resources/ai/finetunes/finetunes.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/ai/finetune_create_params.py">params</a>) -> <a href="./src/cloudflare/types/ai/finetune_create_response.py">FinetuneCreateResponse</a></code>
- <code title="get /accounts/{account_id}/ai/finetunes">client.ai.finetunes.<a href="./src/cloudflare/resources/ai/finetunes/finetunes.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/ai/finetune_list_response.py">FinetuneListResponse</a></code>

### Assets

Types:

```python
from cloudflare.types.ai.finetunes import AssetCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/ai/finetunes/{finetune_id}/finetune-assets">client.ai.finetunes.assets.<a href="./src/cloudflare/resources/ai/finetunes/assets.py">create</a>(finetune_id, \*, account_id, \*\*<a href="src/cloudflare/types/ai/finetunes/asset_create_params.py">params</a>) -> <a href="./src/cloudflare/types/ai/finetunes/asset_create_response.py">AssetCreateResponse</a></code>

### Public

Types:

```python
from cloudflare.types.ai.finetunes import PublicListResponse
```

Methods:

- <code title="get /accounts/{account_id}/ai/finetunes/public">client.ai.finetunes.public.<a href="./src/cloudflare/resources/ai/finetunes/public.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/ai/finetunes/public_list_params.py">params</a>) -> <a href="./src/cloudflare/types/ai/finetunes/public_list_response.py">SyncSinglePage[PublicListResponse]</a></code>

## Authors

Methods:

- <code title="get /accounts/{account_id}/ai/authors/search">client.ai.authors.<a href="./src/cloudflare/resources/ai/authors.py">list</a>(\*, account_id) -> SyncSinglePage[object]</code>

## Tasks

Methods:

- <code title="get /accounts/{account_id}/ai/tasks/search">client.ai.tasks.<a href="./src/cloudflare/resources/ai/tasks.py">list</a>(\*, account_id) -> SyncSinglePage[object]</code>

## Models

Methods:

- <code title="get /accounts/{account_id}/ai/models/search">client.ai.models.<a href="./src/cloudflare/resources/ai/models/models.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/ai/model_list_params.py">params</a>) -> SyncV4PagePaginationArray[object]</code>

### Schema

Types:

```python
from cloudflare.types.ai.models import SchemaGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/ai/models/schema">client.ai.models.schema.<a href="./src/cloudflare/resources/ai/models/schema.py">get</a>(\*, account_id, \*\*<a href="src/cloudflare/types/ai/models/schema_get_params.py">params</a>) -> <a href="./src/cloudflare/types/ai/models/schema_get_response.py">SchemaGetResponse</a></code>

## ToMarkdown

Types:

```python
from cloudflare.types.ai import ToMarkdownSupportedResponse, ToMarkdownTransformResponse
```

Methods:

- <code title="get /accounts/{account_id}/ai/tomarkdown/supported">client.ai.to_markdown.<a href="./src/cloudflare/resources/ai/to_markdown.py">supported</a>(\*, account_id) -> <a href="./src/cloudflare/types/ai/to_markdown_supported_response.py">SyncSinglePage[ToMarkdownSupportedResponse]</a></code>
- <code title="post /accounts/{account_id}/ai/tomarkdown">client.ai.to_markdown.<a href="./src/cloudflare/resources/ai/to_markdown.py">transform</a>(\*, account_id, \*\*<a href="src/cloudflare/types/ai/to_markdown_transform_params.py">params</a>) -> <a href="./src/cloudflare/types/ai/to_markdown_transform_response.py">SyncSinglePage[ToMarkdownTransformResponse]</a></code>
