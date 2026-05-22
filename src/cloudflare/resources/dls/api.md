# DLS

## Regions

Types:

```python
from cloudflare.types.dls import RegionListResponse, RegionGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/dls/regions">client.dls.regions.<a href="./src/cloudflare/resources/dls/regions.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/dls/region_list_params.py">params</a>) -> <a href="./src/cloudflare/types/dls/region_list_response.py">SyncCursorPagination[RegionListResponse]</a></code>
- <code title="get /accounts/{account_id}/dls/regions/{region_id}">client.dls.regions.<a href="./src/cloudflare/resources/dls/regions.py">get</a>(region_id, \*, account_id) -> <a href="./src/cloudflare/types/dls/region_get_response.py">RegionGetResponse</a></code>

## RegionalServices

### PrefixBindings

Types:

```python
from cloudflare.types.dls.regional_services import (
    PrefixBindingCreateResponse,
    PrefixBindingListResponse,
    PrefixBindingDeleteResponse,
    PrefixBindingEditResponse,
    PrefixBindingGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/dls/regional_services/prefix_bindings">client.dls.regional_services.prefix_bindings.<a href="./src/cloudflare/resources/dls/regional_services/prefix_bindings.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/dls/regional_services/prefix_binding_create_params.py">params</a>) -> <a href="./src/cloudflare/types/dls/regional_services/prefix_binding_create_response.py">PrefixBindingCreateResponse</a></code>
- <code title="get /accounts/{account_id}/dls/regional_services/prefix_bindings">client.dls.regional_services.prefix_bindings.<a href="./src/cloudflare/resources/dls/regional_services/prefix_bindings.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/dls/regional_services/prefix_binding_list_params.py">params</a>) -> <a href="./src/cloudflare/types/dls/regional_services/prefix_binding_list_response.py">SyncCursorPagination[PrefixBindingListResponse]</a></code>
- <code title="delete /accounts/{account_id}/dls/regional_services/prefix_bindings/{binding_id}">client.dls.regional_services.prefix_bindings.<a href="./src/cloudflare/resources/dls/regional_services/prefix_bindings.py">delete</a>(binding_id, \*, account_id) -> <a href="./src/cloudflare/types/dls/regional_services/prefix_binding_delete_response.py">PrefixBindingDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/dls/regional_services/prefix_bindings/{binding_id}">client.dls.regional_services.prefix_bindings.<a href="./src/cloudflare/resources/dls/regional_services/prefix_bindings.py">edit</a>(binding_id, \*, account_id, \*\*<a href="src/cloudflare/types/dls/regional_services/prefix_binding_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/dls/regional_services/prefix_binding_edit_response.py">PrefixBindingEditResponse</a></code>
- <code title="get /accounts/{account_id}/dls/regional_services/prefix_bindings/{binding_id}">client.dls.regional_services.prefix_bindings.<a href="./src/cloudflare/resources/dls/regional_services/prefix_bindings.py">get</a>(binding_id, \*, account_id) -> <a href="./src/cloudflare/types/dls/regional_services/prefix_binding_get_response.py">PrefixBindingGetResponse</a></code>
