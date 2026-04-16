# Zaraz

Types:

```python
from cloudflare.types.zaraz import ButtonTextTranslation, NeoEvent
```

Methods:

- <code title="put /zones/{zone_id}/settings/zaraz/workflow">client.zaraz.<a href="./src/cloudflare/resources/zaraz/zaraz.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zaraz/zaraz_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zaraz/workflow.py">Workflow</a></code>

## Config

Types:

```python
from cloudflare.types.zaraz import Configuration
```

Methods:

- <code title="put /zones/{zone_id}/settings/zaraz/config">client.zaraz.config.<a href="./src/cloudflare/resources/zaraz/config.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zaraz/config_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zaraz/configuration.py">Configuration</a></code>
- <code title="get /zones/{zone_id}/settings/zaraz/config">client.zaraz.config.<a href="./src/cloudflare/resources/zaraz/config.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zaraz/configuration.py">Configuration</a></code>

## Default

Methods:

- <code title="get /zones/{zone_id}/settings/zaraz/default">client.zaraz.default.<a href="./src/cloudflare/resources/zaraz/default.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zaraz/configuration.py">Configuration</a></code>

## Export

Methods:

- <code title="get /zones/{zone_id}/settings/zaraz/export">client.zaraz.export.<a href="./src/cloudflare/resources/zaraz/export.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zaraz/configuration.py">Configuration</a></code>

## History

Types:

```python
from cloudflare.types.zaraz import HistoryListResponse
```

Methods:

- <code title="put /zones/{zone_id}/settings/zaraz/history">client.zaraz.history.<a href="./src/cloudflare/resources/zaraz/history/history.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zaraz/history_update_params.py">params</a>) -> <a href="./src/cloudflare/types/zaraz/configuration.py">Configuration</a></code>
- <code title="get /zones/{zone_id}/settings/zaraz/history">client.zaraz.history.<a href="./src/cloudflare/resources/zaraz/history/history.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zaraz/history_list_params.py">params</a>) -> <a href="./src/cloudflare/types/zaraz/history_list_response.py">SyncSinglePage[HistoryListResponse]</a></code>

### Configs

Types:

```python
from cloudflare.types.zaraz.history import ConfigGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/settings/zaraz/history/configs">client.zaraz.history.configs.<a href="./src/cloudflare/resources/zaraz/history/configs.py">get</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zaraz/history/config_get_params.py">params</a>) -> <a href="./src/cloudflare/types/zaraz/history/config_get_response.py">ConfigGetResponse</a></code>

## Publish

Types:

```python
from cloudflare.types.zaraz import PublishCreateResponse
```

Methods:

- <code title="post /zones/{zone_id}/settings/zaraz/publish">client.zaraz.publish.<a href="./src/cloudflare/resources/zaraz/publish.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/zaraz/publish_create_params.py">params</a>) -> <a href="./src/cloudflare/types/zaraz/publish_create_response.py">str</a></code>

## Workflow

Types:

```python
from cloudflare.types.zaraz import Workflow
```

Methods:

- <code title="get /zones/{zone_id}/settings/zaraz/workflow">client.zaraz.workflow.<a href="./src/cloudflare/resources/zaraz/workflow.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/zaraz/workflow.py">Workflow</a></code>
