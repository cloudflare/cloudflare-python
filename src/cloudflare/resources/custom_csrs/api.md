# CustomCsrs

Types:

```python
from cloudflare.types.custom_csrs import (
    CustomCsr,
    CustomCsrCreateResponse,
    CustomCsrListResponse,
    CustomCsrDeleteResponse,
    CustomCsrGetResponse,
)
```

Methods:

- <code title="post /{accounts_or_zones}/{account_or_zone_id}/custom_csrs">client.custom_csrs.<a href="./src/cloudflare/resources/custom_csrs/custom_csrs.py">create</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/custom_csrs/custom_csr_create_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_csrs/custom_csr_create_response.py">Optional[CustomCsrCreateResponse]</a></code>
- <code title="get /{accounts_or_zones}/{account_or_zone_id}/custom_csrs">client.custom_csrs.<a href="./src/cloudflare/resources/custom_csrs/custom_csrs.py">list</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/custom_csrs/custom_csr_list_params.py">params</a>) -> <a href="./src/cloudflare/types/custom_csrs/custom_csr_list_response.py">SyncV4PagePaginationArray[CustomCsrListResponse]</a></code>
- <code title="delete /{accounts_or_zones}/{account_or_zone_id}/custom_csrs/{custom_csr_id}">client.custom_csrs.<a href="./src/cloudflare/resources/custom_csrs/custom_csrs.py">delete</a>(custom_csr_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/custom_csrs/custom_csr_delete_response.py">Optional[CustomCsrDeleteResponse]</a></code>
- <code title="get /{accounts_or_zones}/{account_or_zone_id}/custom_csrs/{custom_csr_id}">client.custom_csrs.<a href="./src/cloudflare/resources/custom_csrs/custom_csrs.py">get</a>(custom_csr_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/custom_csrs/custom_csr_get_response.py">Optional[CustomCsrGetResponse]</a></code>
