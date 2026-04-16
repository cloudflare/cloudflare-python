# OriginTLSClientAuth

Types:

```python
from cloudflare.types.origin_tls_client_auth import (
    OriginTLSClientAuthCreateResponse,
    OriginTLSClientAuthListResponse,
    OriginTLSClientAuthDeleteResponse,
    OriginTLSClientAuthGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/origin_tls_client_auth">client.origin_tls_client_auth.<a href="./src/cloudflare/resources/origin_tls_client_auth/origin_tls_client_auth.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/origin_tls_client_auth/origin_tls_client_auth_create_params.py">params</a>) -> <a href="./src/cloudflare/types/origin_tls_client_auth/origin_tls_client_auth_create_response.py">Optional[OriginTLSClientAuthCreateResponse]</a></code>
- <code title="get /zones/{zone_id}/origin_tls_client_auth">client.origin_tls_client_auth.<a href="./src/cloudflare/resources/origin_tls_client_auth/origin_tls_client_auth.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/origin_tls_client_auth/origin_tls_client_auth_list_response.py">SyncSinglePage[OriginTLSClientAuthListResponse]</a></code>
- <code title="delete /zones/{zone_id}/origin_tls_client_auth/{certificate_id}">client.origin_tls_client_auth.<a href="./src/cloudflare/resources/origin_tls_client_auth/origin_tls_client_auth.py">delete</a>(certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/origin_tls_client_auth/origin_tls_client_auth_delete_response.py">Optional[OriginTLSClientAuthDeleteResponse]</a></code>
- <code title="get /zones/{zone_id}/origin_tls_client_auth/{certificate_id}">client.origin_tls_client_auth.<a href="./src/cloudflare/resources/origin_tls_client_auth/origin_tls_client_auth.py">get</a>(certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/origin_tls_client_auth/origin_tls_client_auth_get_response.py">Optional[OriginTLSClientAuthGetResponse]</a></code>

## ZoneCertificates

Types:

```python
from cloudflare.types.origin_tls_client_auth import (
    ZoneAuthenticatedOriginPull,
    ZoneCertificateCreateResponse,
    ZoneCertificateListResponse,
    ZoneCertificateDeleteResponse,
    ZoneCertificateGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/origin_tls_client_auth">client.origin_tls_client_auth.zone_certificates.<a href="./src/cloudflare/resources/origin_tls_client_auth/zone_certificates.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/origin_tls_client_auth/zone_certificate_create_params.py">params</a>) -> <a href="./src/cloudflare/types/origin_tls_client_auth/zone_certificate_create_response.py">Optional[ZoneCertificateCreateResponse]</a></code>
- <code title="get /zones/{zone_id}/origin_tls_client_auth">client.origin_tls_client_auth.zone_certificates.<a href="./src/cloudflare/resources/origin_tls_client_auth/zone_certificates.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/origin_tls_client_auth/zone_certificate_list_response.py">SyncSinglePage[ZoneCertificateListResponse]</a></code>
- <code title="delete /zones/{zone_id}/origin_tls_client_auth/{certificate_id}">client.origin_tls_client_auth.zone_certificates.<a href="./src/cloudflare/resources/origin_tls_client_auth/zone_certificates.py">delete</a>(certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/origin_tls_client_auth/zone_certificate_delete_response.py">Optional[ZoneCertificateDeleteResponse]</a></code>
- <code title="get /zones/{zone_id}/origin_tls_client_auth/{certificate_id}">client.origin_tls_client_auth.zone_certificates.<a href="./src/cloudflare/resources/origin_tls_client_auth/zone_certificates.py">get</a>(certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/origin_tls_client_auth/zone_certificate_get_response.py">Optional[ZoneCertificateGetResponse]</a></code>

## Hostnames

Types:

```python
from cloudflare.types.origin_tls_client_auth import AuthenticatedOriginPull, HostnameUpdateResponse
```

Methods:

- <code title="put /zones/{zone_id}/origin_tls_client_auth/hostnames">client.origin_tls_client_auth.hostnames.<a href="./src/cloudflare/resources/origin_tls_client_auth/hostnames.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/origin_tls_client_auth/hostname_update_params.py">params</a>) -> <a href="./src/cloudflare/types/origin_tls_client_auth/hostname_update_response.py">SyncSinglePage[HostnameUpdateResponse]</a></code>
- <code title="get /zones/{zone_id}/origin_tls_client_auth/hostnames/{hostname}">client.origin_tls_client_auth.hostnames.<a href="./src/cloudflare/resources/origin_tls_client_auth/hostnames.py">get</a>(hostname, \*, zone_id) -> <a href="./src/cloudflare/types/origin_tls_client_auth/authenticated_origin_pull.py">Optional[AuthenticatedOriginPull]</a></code>

## HostnameCertificates

Types:

```python
from cloudflare.types.origin_tls_client_auth import (
    Certificate,
    HostnameCertificateCreateResponse,
    HostnameCertificateListResponse,
    HostnameCertificateDeleteResponse,
    HostnameCertificateGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/origin_tls_client_auth/hostnames/certificates">client.origin_tls_client_auth.hostname_certificates.<a href="./src/cloudflare/resources/origin_tls_client_auth/hostname_certificates.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/origin_tls_client_auth/hostname_certificate_create_params.py">params</a>) -> <a href="./src/cloudflare/types/origin_tls_client_auth/hostname_certificate_create_response.py">Optional[HostnameCertificateCreateResponse]</a></code>
- <code title="get /zones/{zone_id}/origin_tls_client_auth/hostnames/certificates">client.origin_tls_client_auth.hostname_certificates.<a href="./src/cloudflare/resources/origin_tls_client_auth/hostname_certificates.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/origin_tls_client_auth/hostname_certificate_list_response.py">SyncSinglePage[HostnameCertificateListResponse]</a></code>
- <code title="delete /zones/{zone_id}/origin_tls_client_auth/hostnames/certificates/{certificate_id}">client.origin_tls_client_auth.hostname_certificates.<a href="./src/cloudflare/resources/origin_tls_client_auth/hostname_certificates.py">delete</a>(certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/origin_tls_client_auth/hostname_certificate_delete_response.py">Optional[HostnameCertificateDeleteResponse]</a></code>
- <code title="get /zones/{zone_id}/origin_tls_client_auth/hostnames/certificates/{certificate_id}">client.origin_tls_client_auth.hostname_certificates.<a href="./src/cloudflare/resources/origin_tls_client_auth/hostname_certificates.py">get</a>(certificate_id, \*, zone_id) -> <a href="./src/cloudflare/types/origin_tls_client_auth/hostname_certificate_get_response.py">Optional[HostnameCertificateGetResponse]</a></code>

## Settings

Types:

```python
from cloudflare.types.origin_tls_client_auth import SettingUpdateResponse, SettingGetResponse
```

Methods:

- <code title="put /zones/{zone_id}/origin_tls_client_auth/settings">client.origin_tls_client_auth.settings.<a href="./src/cloudflare/resources/origin_tls_client_auth/settings.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/origin_tls_client_auth/setting_update_params.py">params</a>) -> <a href="./src/cloudflare/types/origin_tls_client_auth/setting_update_response.py">Optional[SettingUpdateResponse]</a></code>
- <code title="get /zones/{zone_id}/origin_tls_client_auth/settings">client.origin_tls_client_auth.settings.<a href="./src/cloudflare/resources/origin_tls_client_auth/settings.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/origin_tls_client_auth/setting_get_response.py">Optional[SettingGetResponse]</a></code>
