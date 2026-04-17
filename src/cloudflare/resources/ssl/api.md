# SSL

## Analyze

Methods:

- <code title="post /zones/{zone_id}/ssl/analyze">client.ssl.analyze.<a href="./src/cloudflare/resources/ssl/analyze.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/ssl/analyze_create_params.py">params</a>) -> object</code>

## CertificatePacks

Types:

```python
from cloudflare.types.ssl import (
    Host,
    RequestValidity,
    Status,
    ValidationMethod,
    CertificatePackCreateResponse,
    CertificatePackListResponse,
    CertificatePackDeleteResponse,
    CertificatePackEditResponse,
    CertificatePackGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/ssl/certificate_packs/order">client.ssl.certificate_packs.<a href="./src/cloudflare/resources/ssl/certificate_packs/certificate_packs.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/ssl/certificate_pack_create_params.py">params</a>) -> <a href="./src/cloudflare/types/ssl/certificate_pack_create_response.py">Optional[CertificatePackCreateResponse]</a></code>
- <code title="get /zones/{zone_id}/ssl/certificate_packs">client.ssl.certificate_packs.<a href="./src/cloudflare/resources/ssl/certificate_packs/certificate_packs.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/ssl/certificate_pack_list_params.py">params</a>) -> <a href="./src/cloudflare/types/ssl/certificate_pack_list_response.py">SyncV4PagePaginationArray[CertificatePackListResponse]</a></code>
- <code title="delete /zones/{zone_id}/ssl/certificate_packs/{certificate_pack_id}">client.ssl.certificate_packs.<a href="./src/cloudflare/resources/ssl/certificate_packs/certificate_packs.py">delete</a>(certificate_pack_id, \*, zone_id) -> <a href="./src/cloudflare/types/ssl/certificate_pack_delete_response.py">Optional[CertificatePackDeleteResponse]</a></code>
- <code title="patch /zones/{zone_id}/ssl/certificate_packs/{certificate_pack_id}">client.ssl.certificate_packs.<a href="./src/cloudflare/resources/ssl/certificate_packs/certificate_packs.py">edit</a>(certificate_pack_id, \*, zone_id, \*\*<a href="src/cloudflare/types/ssl/certificate_pack_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/ssl/certificate_pack_edit_response.py">Optional[CertificatePackEditResponse]</a></code>
- <code title="get /zones/{zone_id}/ssl/certificate_packs/{certificate_pack_id}">client.ssl.certificate_packs.<a href="./src/cloudflare/resources/ssl/certificate_packs/certificate_packs.py">get</a>(certificate_pack_id, \*, zone_id) -> <a href="./src/cloudflare/types/ssl/certificate_pack_get_response.py">Optional[CertificatePackGetResponse]</a></code>

### Quota

Types:

```python
from cloudflare.types.ssl.certificate_packs import QuotaGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/ssl/certificate_packs/quota">client.ssl.certificate_packs.quota.<a href="./src/cloudflare/resources/ssl/certificate_packs/quota.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/ssl/certificate_packs/quota_get_response.py">Optional[QuotaGetResponse]</a></code>

## Recommendations

Types:

```python
from cloudflare.types.ssl import RecommendationGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/ssl/recommendation">client.ssl.recommendations.<a href="./src/cloudflare/resources/ssl/recommendations.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/ssl/recommendation_get_response.py">RecommendationGetResponse</a></code>

## Universal

### Settings

Types:

```python
from cloudflare.types.ssl.universal import UniversalSSLSettings
```

Methods:

- <code title="patch /zones/{zone_id}/ssl/universal/settings">client.ssl.universal.settings.<a href="./src/cloudflare/resources/ssl/universal/settings.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/ssl/universal/setting_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/ssl/universal/universal_ssl_settings.py">Optional[UniversalSSLSettings]</a></code>
- <code title="get /zones/{zone_id}/ssl/universal/settings">client.ssl.universal.settings.<a href="./src/cloudflare/resources/ssl/universal/settings.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/ssl/universal/universal_ssl_settings.py">Optional[UniversalSSLSettings]</a></code>

## Verification

Types:

```python
from cloudflare.types.ssl import Verification, VerificationEditResponse, VerificationGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/ssl/verification/{certificate_pack_id}">client.ssl.verification.<a href="./src/cloudflare/resources/ssl/verification.py">edit</a>(certificate_pack_id, \*, zone_id, \*\*<a href="src/cloudflare/types/ssl/verification_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/ssl/verification_edit_response.py">Optional[VerificationEditResponse]</a></code>
- <code title="get /zones/{zone_id}/ssl/verification">client.ssl.verification.<a href="./src/cloudflare/resources/ssl/verification.py">get</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/ssl/verification_get_params.py">params</a>) -> <a href="./src/cloudflare/types/ssl/verification_get_response.py">Optional[VerificationGetResponse]</a></code>
