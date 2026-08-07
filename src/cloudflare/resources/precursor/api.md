# Precursor

Types:

```python
from cloudflare.types.precursor import EnforcementRule, PrecursorConfig
```

Methods:

- <code title="put /zones/{zone_id}/precursor">client.precursor.<a href="./src/cloudflare/resources/precursor/precursor.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/precursor/precursor_update_params.py">params</a>) -> <a href="./src/cloudflare/types/precursor/precursor_config.py">Optional[PrecursorConfig]</a></code>
- <code title="get /zones/{zone_id}/precursor">client.precursor.<a href="./src/cloudflare/resources/precursor/precursor.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/precursor/precursor_config.py">Optional[PrecursorConfig]</a></code>
