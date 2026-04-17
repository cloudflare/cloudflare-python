# MTLSCertificates

Types:

```python
from cloudflare.types.mtls_certificates import MTLSCertificate, MTLSCertificateCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/mtls_certificates">client.mtls_certificates.<a href="./src/cloudflare/resources/mtls_certificates/mtls_certificates.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/mtls_certificates/mtls_certificate_create_params.py">params</a>) -> <a href="./src/cloudflare/types/mtls_certificates/mtls_certificate_create_response.py">Optional[MTLSCertificateCreateResponse]</a></code>
- <code title="get /accounts/{account_id}/mtls_certificates">client.mtls_certificates.<a href="./src/cloudflare/resources/mtls_certificates/mtls_certificates.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/mtls_certificates/mtls_certificate_list_params.py">params</a>) -> <a href="./src/cloudflare/types/mtls_certificates/mtls_certificate.py">SyncSinglePage[MTLSCertificate]</a></code>
- <code title="delete /accounts/{account_id}/mtls_certificates/{mtls_certificate_id}">client.mtls_certificates.<a href="./src/cloudflare/resources/mtls_certificates/mtls_certificates.py">delete</a>(mtls_certificate_id, \*, account_id) -> <a href="./src/cloudflare/types/mtls_certificates/mtls_certificate.py">Optional[MTLSCertificate]</a></code>
- <code title="get /accounts/{account_id}/mtls_certificates/{mtls_certificate_id}">client.mtls_certificates.<a href="./src/cloudflare/resources/mtls_certificates/mtls_certificates.py">get</a>(mtls_certificate_id, \*, account_id) -> <a href="./src/cloudflare/types/mtls_certificates/mtls_certificate.py">Optional[MTLSCertificate]</a></code>

## Associations

Types:

```python
from cloudflare.types.mtls_certificates import CertificateAsssociation
```

Methods:

- <code title="get /accounts/{account_id}/mtls_certificates/{mtls_certificate_id}/associations">client.mtls_certificates.associations.<a href="./src/cloudflare/resources/mtls_certificates/associations.py">get</a>(mtls_certificate_id, \*, account_id) -> <a href="./src/cloudflare/types/mtls_certificates/certificate_asssociation.py">SyncSinglePage[CertificateAsssociation]</a></code>
