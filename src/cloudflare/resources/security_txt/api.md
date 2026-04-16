# SecurityTXT

Types:

```python
from cloudflare.types.security_txt import (
    SecurityTXTUpdateResponse,
    SecurityTXTDeleteResponse,
    SecurityTXTGetResponse,
)
```

Methods:

- <code title="put /zones/{zone_id}/security-center/securitytxt">client.security_txt.<a href="./src/cloudflare/resources/security_txt/security_txt.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/security_txt/security_txt_update_params.py">params</a>) -> <a href="./src/cloudflare/types/security_txt/security_txt_update_response.py">SecurityTXTUpdateResponse</a></code>
- <code title="delete /zones/{zone_id}/security-center/securitytxt">client.security_txt.<a href="./src/cloudflare/resources/security_txt/security_txt.py">delete</a>(\*, zone_id) -> <a href="./src/cloudflare/types/security_txt/security_txt_delete_response.py">SecurityTXTDeleteResponse</a></code>
- <code title="get /zones/{zone_id}/security-center/securitytxt">client.security_txt.<a href="./src/cloudflare/resources/security_txt/security_txt.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/security_txt/security_txt_get_response.py">Optional[SecurityTXTGetResponse]</a></code>
