# CertificateAuthorities

## HostnameAssociations

Types:

```python
from cloudflare.types.certificate_authorities import (
    HostnameAssociation,
    TLSHostnameAssociation,
    HostnameAssociationUpdateResponse,
    HostnameAssociationGetResponse,
)
```

Methods:

- <code title="put /zones/{zone_id}/certificate_authorities/hostname_associations">client.certificate_authorities.hostname_associations.<a href="./src/cloudflare/resources/certificate_authorities/hostname_associations.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/certificate_authorities/hostname_association_update_params.py">params</a>) -> <a href="./src/cloudflare/types/certificate_authorities/hostname_association_update_response.py">Optional[HostnameAssociationUpdateResponse]</a></code>
- <code title="get /zones/{zone_id}/certificate_authorities/hostname_associations">client.certificate_authorities.hostname_associations.<a href="./src/cloudflare/resources/certificate_authorities/hostname_associations.py">get</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/certificate_authorities/hostname_association_get_params.py">params</a>) -> <a href="./src/cloudflare/types/certificate_authorities/hostname_association_get_response.py">Optional[HostnameAssociationGetResponse]</a></code>
