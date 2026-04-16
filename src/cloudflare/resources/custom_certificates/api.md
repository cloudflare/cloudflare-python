# CustomCertificates

Types:

```python
from cloudflare.types.custom_certificates import (
    CustomCertificate,
    GeoRestrictions,
    Status,
    CustomCertificateDeleteResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/custom_certificates">client.custom_certificates.<a href="./src/cloudflare/resources/custom_certificates/custom_certificates.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/custom_certificates/custom_certificate_create_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_certificates/custom_certificate.py">Optional[CustomCertificate]</a></code>
- <code title="get /zones/{zone_id}/custom_certificates">client.custom_certificates.<a href="./src/cloudflare/resources/custom_certificates/custom_certificates.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/custom_certificates/custom_certificate_list_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_certificates/custom_certificate.py">SyncV4PagePaginationArray[CustomCertificate]</a></code>
- <code title="delete /zones/{zone_id}/custom_certificates/{custom_certificate_id}">client.custom_certificates.<a href="./src/cloudflare/resources/custom_certificates/custom_certificates.py">delete</a>(custom_certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/custom_certificates/custom_certificate_delete_response.py">Optional[CustomCertificateDeleteResponse]</a></code>
- <code title="patch /zones/{zone_id}/custom_certificates/{custom_certificate_id}">client.custom_certificates.<a href="./src/cloudflare/resources/custom_certificates/custom_certificates.py">edit</a>(custom_certificate_id, \*, zone_id, \*\*<a href="src/cloudflare/types/custom_certificates/custom_certificate_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_certificates/custom_certificate.py">Optional[CustomCertificate]</a></code>
- <code title="get /zones/{zone_id}/custom_certificates/{custom_certificate_id}">client.custom_certificates.<a href="./src/cloudflare/resources/custom_certificates/custom_certificates.py">get</a>(custom_certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/custom_certificates/custom_certificate.py">Optional[CustomCertificate]</a></code>

## Prioritize

Methods:

- <code title="put /zones/{zone_id}/custom_certificates/prioritize">client.custom_certificates.prioritize.<a href="./src/cloudflare/resources/custom_certificates/prioritize.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/custom_certificates/prioritize_update_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_certificates/custom_certificate.py">SyncSinglePage[CustomCertificate]</a></code>
