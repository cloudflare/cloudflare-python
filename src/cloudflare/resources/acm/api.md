# ACM

## TotalTLS

Types:

```python
from cloudflare.types.acm import CertificateAuthority, TotalTLSCreateResponse, TotalTLSGetResponse
```

Methods:

- <code title="post /zones/{zone_id}/acm/total_tls">client.acm.total_tls.<a href="./src/cloudflare/resources/acm/total_tls.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/acm/total_tls_create_params.py">params</a>) -> <a href="./src/cloudflare/types/acm/total_tls_create_response.py">Optional[TotalTLSCreateResponse]</a></code>
- <code title="get /zones/{zone_id}/acm/total_tls">client.acm.total_tls.<a href="./src/cloudflare/resources/acm/total_tls.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/acm/total_tls_get_response.py">Optional[TotalTLSGetResponse]</a></code>
