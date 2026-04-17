# KeylessCertificates

Types:

```python
from cloudflare.types.keyless_certificates import (
    KeylessCertificate,
    Tunnel,
    KeylessCertificateDeleteResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/keyless_certificates">client.keyless_certificates.<a href="./src/cloudflare/resources/keyless_certificates/keyless_certificates.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/keyless_certificates/keyless_certificate_create_params.py">params</a>) -> <a href="./src/cloudflare/types/keyless_certificates/keyless_certificate.py">Optional[KeylessCertificate]</a></code>
- <code title="get /zones/{zone_id}/keyless_certificates">client.keyless_certificates.<a href="./src/cloudflare/resources/keyless_certificates/keyless_certificates.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/keyless_certificates/keyless_certificate.py">SyncSinglePage[KeylessCertificate]</a></code>
- <code title="delete /zones/{zone_id}/keyless_certificates/{keyless_certificate_id}">client.keyless_certificates.<a href="./src/cloudflare/resources/keyless_certificates/keyless_certificates.py">delete</a>(keyless_certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/keyless_certificates/keyless_certificate_delete_response.py">Optional[KeylessCertificateDeleteResponse]</a></code>
- <code title="patch /zones/{zone_id}/keyless_certificates/{keyless_certificate_id}">client.keyless_certificates.<a href="./src/cloudflare/resources/keyless_certificates/keyless_certificates.py">edit</a>(keyless_certificate_id, \*, zone_id, \*\*<a href="src/cloudflare/types/keyless_certificates/keyless_certificate_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/keyless_certificates/keyless_certificate.py">Optional[KeylessCertificate]</a></code>
- <code title="get /zones/{zone_id}/keyless_certificates/{keyless_certificate_id}">client.keyless_certificates.<a href="./src/cloudflare/resources/keyless_certificates/keyless_certificates.py">get</a>(keyless_certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/keyless_certificates/keyless_certificate.py">Optional[KeylessCertificate]</a></code>
