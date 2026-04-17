# Logs

## Control

### Retention

Types:

```python
from cloudflare.types.logs.control import RetentionCreateResponse, RetentionGetResponse
```

Methods:

- <code title="post /zones/{zone_id}/logs/control/retention/flag">client.logs.control.retention.<a href="./src/cloudflare/resources/logs/control/retention.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/logs/control/retention_create_params.py">params</a>) -> <a href="./src/cloudflare/types/logs/control/retention_create_response.py">Optional[RetentionCreateResponse]</a></code>
- <code title="get /zones/{zone_id}/logs/control/retention/flag">client.logs.control.retention.<a href="./src/cloudflare/resources/logs/control/retention.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/logs/control/retention_get_response.py">Optional[RetentionGetResponse]</a></code>

### Cmb

#### Config

Types:

```python
from cloudflare.types.logs.control.cmb import CmbConfig
```

Methods:

- <code title="post /accounts/{account_id}/logs/control/cmb/config">client.logs.control.cmb.config.<a href="./src/cloudflare/resources/logs/control/cmb/config.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/logs/control/cmb/config_create_params.py">params</a>) -> <a href="./src/cloudflare/types/logs/control/cmb/cmb_config.py">Optional[CmbConfig]</a></code>
- <code title="delete /accounts/{account_id}/logs/control/cmb/config">client.logs.control.cmb.config.<a href="./src/cloudflare/resources/logs/control/cmb/config.py">delete</a>(\*, account_id) -> object</code>
- <code title="get /accounts/{account_id}/logs/control/cmb/config">client.logs.control.cmb.config.<a href="./src/cloudflare/resources/logs/control/cmb/config.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/logs/control/cmb/cmb_config.py">Optional[CmbConfig]</a></code>

## RayID

Types:

```python
from cloudflare.types.logs import RayIDGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/logs/rayids/{ray_id}">client.logs.rayid.<a href="./src/cloudflare/resources/logs/rayid.py">get</a>(rayid, \*, zone_id, \*\*<a href="src/cloudflare/types/logs/rayid_get_params.py">params</a>) -> <a href="./src/cloudflare/types/logs/rayid_get_response.py">RayIDGetResponse</a></code>

## Received

Types:

```python
from cloudflare.types.logs import ReceivedGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/logs/received">client.logs.received.<a href="./src/cloudflare/resources/logs/received/received.py">get</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/logs/received_get_params.py">params</a>) -> <a href="./src/cloudflare/types/logs/received_get_response.py">ReceivedGetResponse</a></code>

### Fields

Types:

```python
from cloudflare.types.logs.received import FieldGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/logs/received/fields">client.logs.received.fields.<a href="./src/cloudflare/resources/logs/received/fields.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/logs/received/field_get_response.py">FieldGetResponse</a></code>
