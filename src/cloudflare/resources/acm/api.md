# ACM

## TotalTLS

Types:

```python
from cloudflare.types.acm import (
    CertificateAuthority,
    TotalTLSUpdateResponse,
    TotalTLSEditResponse,
    TotalTLSGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/acm/total_tls">client.acm.total_tls.<a href="./src/cloudflare/resources/acm/total_tls.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/acm/total_tls_update_params.py">params</a>) -> <a href="./src/cloudflare/types/acm/total_tls_update_response.py">Optional[TotalTLSUpdateResponse]</a></code>
- <code title="post /zones/{zone_id}/acm/total_tls">client.acm.total_tls.<a href="./src/cloudflare/resources/acm/total_tls.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/acm/total_tls_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/acm/total_tls_edit_response.py">Optional[TotalTLSEditResponse]</a></code>
- <code title="get /zones/{zone_id}/acm/total_tls">client.acm.total_tls.<a href="./src/cloudflare/resources/acm/total_tls.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/acm/total_tls_get_response.py">Optional[TotalTLSGetResponse]</a></code>

## CustomTrustStore

Types:

```python
from cloudflare.types.acm import CustomTrustStore, CustomTrustStoreDeleteResponse
```

Methods:

- <code title="post /zones/{zone_id}/acm/custom_trust_store">client.acm.custom_trust_store.<a href="./src/cloudflare/resources/acm/custom_trust_store.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/acm/custom_trust_store_create_params.py">params</a>) -> <a href="./src/cloudflare/types/acm/custom_trust_store.py">Optional[CustomTrustStore]</a></code>
- <code title="get /zones/{zone_id}/acm/custom_trust_store">client.acm.custom_trust_store.<a href="./src/cloudflare/resources/acm/custom_trust_store.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/acm/custom_trust_store_list_params.py">params</a>) -> <a href="./src/cloudflare/types/acm/custom_trust_store.py">SyncV4PagePaginationArray[CustomTrustStore]</a></code>
- <code title="delete /zones/{zone_id}/acm/custom_trust_store/{custom_origin_trust_store_id}">client.acm.custom_trust_store.<a href="./src/cloudflare/resources/acm/custom_trust_store.py">delete</a>(custom_origin_trust_store_id, \*, zone_id) -> <a href="./src/cloudflare/types/acm/custom_trust_store_delete_response.py">Optional[CustomTrustStoreDeleteResponse]</a></code>
- <code title="get /zones/{zone_id}/acm/custom_trust_store/{custom_origin_trust_store_id}">client.acm.custom_trust_store.<a href="./src/cloudflare/resources/acm/custom_trust_store.py">get</a>(custom_origin_trust_store_id, \*, zone_id) -> <a href="./src/cloudflare/types/acm/custom_trust_store.py">Optional[CustomTrustStore]</a></code>
