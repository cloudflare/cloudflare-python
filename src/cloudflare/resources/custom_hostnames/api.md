# CustomHostnames

Types:

```python
from cloudflare.types.custom_hostnames import (
    BundleMethod,
    CustomHostname,
    DCVMethod,
    DomainValidationType,
    CustomHostnameCreateResponse,
    CustomHostnameListResponse,
    CustomHostnameDeleteResponse,
    CustomHostnameEditResponse,
    CustomHostnameGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/custom_hostnames">client.custom_hostnames.<a href="./src/cloudflare/resources/custom_hostnames/custom_hostnames.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/custom_hostnames/custom_hostname_create_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_hostnames/custom_hostname_create_response.py">Optional[CustomHostnameCreateResponse]</a></code>
- <code title="get /zones/{zone_id}/custom_hostnames">client.custom_hostnames.<a href="./src/cloudflare/resources/custom_hostnames/custom_hostnames.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/custom_hostnames/custom_hostname_list_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_hostnames/custom_hostname_list_response.py">SyncV4PagePaginationArray[CustomHostnameListResponse]</a></code>
- <code title="delete /zones/{zone_id}/custom_hostnames/{custom_hostname_id}">client.custom_hostnames.<a href="./src/cloudflare/resources/custom_hostnames/custom_hostnames.py">delete</a>(custom_hostname_id, \*, zone_id) -> <a href="./src/cloudflare/types/custom_hostnames/custom_hostname_delete_response.py">CustomHostnameDeleteResponse</a></code>
- <code title="patch /zones/{zone_id}/custom_hostnames/{custom_hostname_id}">client.custom_hostnames.<a href="./src/cloudflare/resources/custom_hostnames/custom_hostnames.py">edit</a>(custom_hostname_id, \*, zone_id, \*\*<a href="src/cloudflare/types/custom_hostnames/custom_hostname_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_hostnames/custom_hostname_edit_response.py">Optional[CustomHostnameEditResponse]</a></code>
- <code title="get /zones/{zone_id}/custom_hostnames/{custom_hostname_id}">client.custom_hostnames.<a href="./src/cloudflare/resources/custom_hostnames/custom_hostnames.py">get</a>(custom_hostname_id, \*, zone_id) -> <a href="./src/cloudflare/types/custom_hostnames/custom_hostname_get_response.py">Optional[CustomHostnameGetResponse]</a></code>

## FallbackOrigin

Types:

```python
from cloudflare.types.custom_hostnames import (
    FallbackOriginUpdateResponse,
    FallbackOriginDeleteResponse,
    FallbackOriginGetResponse,
)
```

Methods:

- <code title="put /zones/{zone_id}/custom_hostnames/fallback_origin">client.custom_hostnames.fallback_origin.<a href="./src/cloudflare/resources/custom_hostnames/fallback_origin.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/custom_hostnames/fallback_origin_update_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_hostnames/fallback_origin_update_response.py">Optional[FallbackOriginUpdateResponse]</a></code>
- <code title="delete /zones/{zone_id}/custom_hostnames/fallback_origin">client.custom_hostnames.fallback_origin.<a href="./src/cloudflare/resources/custom_hostnames/fallback_origin.py">delete</a>(\*, zone_id) -> <a href="./src/cloudflare/types/custom_hostnames/fallback_origin_delete_response.py">Optional[FallbackOriginDeleteResponse]</a></code>
- <code title="get /zones/{zone_id}/custom_hostnames/fallback_origin">client.custom_hostnames.fallback_origin.<a href="./src/cloudflare/resources/custom_hostnames/fallback_origin.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/custom_hostnames/fallback_origin_get_response.py">Optional[FallbackOriginGetResponse]</a></code>

## CertificatePack

### Certificates

Types:

```python
from cloudflare.types.custom_hostnames.certificate_pack import (
    CertificateUpdateResponse,
    CertificateDeleteResponse,
)
```

Methods:

- <code title="put /zones/{zone_id}/custom_hostnames/{custom_hostname_id}/certificate_pack/{certificate_pack_id}/certificates/{certificate_id}">client.custom_hostnames.certificate_pack.certificates.<a href="./src/cloudflare/resources/custom_hostnames/certificate_pack/certificates.py">update</a>(certificate_id, \*, zone_id, custom_hostname_id, certificate_pack_id, \*\*<a href="src/cloudflare/types/custom_hostnames/certificate_pack/certificate_update_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_hostnames/certificate_pack/certificate_update_response.py">Optional[CertificateUpdateResponse]</a></code>
- <code title="delete /zones/{zone_id}/custom_hostnames/{custom_hostname_id}/certificate_pack/{certificate_pack_id}/certificates/{certificate_id}">client.custom_hostnames.certificate_pack.certificates.<a href="./src/cloudflare/resources/custom_hostnames/certificate_pack/certificates.py">delete</a>(certificate_id, \*, zone_id, custom_hostname_id, certificate_pack_id) -> <a href="./src/cloudflare/types/custom_hostnames/certificate_pack/certificate_delete_response.py">CertificateDeleteResponse</a></code>
