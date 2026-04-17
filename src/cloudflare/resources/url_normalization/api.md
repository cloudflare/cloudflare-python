# URLNormalization

Types:

```python
from cloudflare.types.url_normalization import (
    URLNormalizationUpdateResponse,
    URLNormalizationGetResponse,
)
```

Methods:

- <code title="put /zones/{zone_id}/url_normalization">client.url_normalization.<a href="./src/cloudflare/resources/url_normalization/url_normalization.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/url_normalization/url_normalization_update_params.py">params</a>) -> <a href="./src/cloudflare/types/url_normalization/url_normalization_update_response.py">URLNormalizationUpdateResponse</a></code>
- <code title="delete /zones/{zone_id}/url_normalization">client.url_normalization.<a href="./src/cloudflare/resources/url_normalization/url_normalization.py">delete</a>(\*, zone_id) -> None</code>
- <code title="get /zones/{zone_id}/url_normalization">client.url_normalization.<a href="./src/cloudflare/resources/url_normalization/url_normalization.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/url_normalization/url_normalization_get_response.py">URLNormalizationGetResponse</a></code>
