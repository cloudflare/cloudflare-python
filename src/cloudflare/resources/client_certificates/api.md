# ClientCertificates

Types:

```python
from cloudflare.types.client_certificates import ClientCertificate
```

Methods:

- <code title="post /zones/{zone_id}/client_certificates">client.client_certificates.<a href="./src/cloudflare/resources/client_certificates/client_certificates.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/client_certificates/client_certificate_create_params.py">params</a>) -> <a href="./src/cloudflare/types/client_certificates/client_certificate.py">Optional[ClientCertificate]</a></code>
- <code title="get /zones/{zone_id}/client_certificates">client.client_certificates.<a href="./src/cloudflare/resources/client_certificates/client_certificates.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/client_certificates/client_certificate_list_params.py">params</a>) -> <a href="./src/cloudflare/types/client_certificates/client_certificate.py">SyncV4PagePaginationArray[ClientCertificate]</a></code>
- <code title="delete /zones/{zone_id}/client_certificates/{client_certificate_id}">client.client_certificates.<a href="./src/cloudflare/resources/client_certificates/client_certificates.py">delete</a>(client_certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/client_certificates/client_certificate.py">Optional[ClientCertificate]</a></code>
- <code title="patch /zones/{zone_id}/client_certificates/{client_certificate_id}">client.client_certificates.<a href="./src/cloudflare/resources/client_certificates/client_certificates.py">edit</a>(client_certificate_id, \*, zone_id, \*\*<a href="src/cloudflare/types/client_certificates/client_certificate_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/client_certificates/client_certificate.py">Optional[ClientCertificate]</a></code>
- <code title="get /zones/{zone_id}/client_certificates/{client_certificate_id}">client.client_certificates.<a href="./src/cloudflare/resources/client_certificates/client_certificates.py">get</a>(client_certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/client_certificates/client_certificate.py">Optional[ClientCertificate]</a></code>
