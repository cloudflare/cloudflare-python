# OriginCACertificates

Types:

```python
from cloudflare.types.origin_ca_certificates import (
    OriginCACertificate,
    OriginCACertificateDeleteResponse,
)
```

Methods:

- <code title="post /certificates">client.origin_ca_certificates.<a href="./src/cloudflare/resources/origin_ca_certificates/origin_ca_certificates.py">create</a>(\*\*<a href="src/cloudflare/types/origin_ca_certificates/origin_ca_certificate_create_params.py">params</a>) -> <a href="./src/cloudflare/types/origin_ca_certificates/origin_ca_certificate.py">Optional[OriginCACertificate]</a></code>
- <code title="get /certificates">client.origin_ca_certificates.<a href="./src/cloudflare/resources/origin_ca_certificates/origin_ca_certificates.py">list</a>(\*\*<a href="src/cloudflare/types/origin_ca_certificates/origin_ca_certificate_list_params.py">params</a>) -> <a href="./src/cloudflare/types/origin_ca_certificates/origin_ca_certificate.py">SyncV4PagePaginationArray[OriginCACertificate]</a></code>
- <code title="delete /certificates/{certificate_id}">client.origin_ca_certificates.<a href="./src/cloudflare/resources/origin_ca_certificates/origin_ca_certificates.py">delete</a>(certificate_id) -> <a href="./src/cloudflare/types/origin_ca_certificates/origin_ca_certificate_delete_response.py">Optional[OriginCACertificateDeleteResponse]</a></code>
- <code title="get /certificates/{certificate_id}">client.origin_ca_certificates.<a href="./src/cloudflare/resources/origin_ca_certificates/origin_ca_certificates.py">get</a>(certificate_id) -> <a href="./src/cloudflare/types/origin_ca_certificates/origin_ca_certificate.py">Optional[OriginCACertificate]</a></code>
