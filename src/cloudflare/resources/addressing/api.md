# Addressing

## RegionalHostnames

Types:

```python
from cloudflare.types.addressing import (
    RegionalHostnameCreateResponse,
    RegionalHostnameListResponse,
    RegionalHostnameDeleteResponse,
    RegionalHostnameEditResponse,
    RegionalHostnameGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/addressing/regional_hostnames">client.addressing.regional_hostnames.<a href="./src/cloudflare/resources/addressing/regional_hostnames/regional_hostnames.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/addressing/regional_hostname_create_params.py">params</a>) -> <a href="./src/cloudflare/types/addressing/regional_hostname_create_response.py">Optional[RegionalHostnameCreateResponse]</a></code>
- <code title="get /zones/{zone_id}/addressing/regional_hostnames">client.addressing.regional_hostnames.<a href="./src/cloudflare/resources/addressing/regional_hostnames/regional_hostnames.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/addressing/regional_hostname_list_response.py">SyncSinglePage[RegionalHostnameListResponse]</a></code>
- <code title="delete /zones/{zone_id}/addressing/regional_hostnames/{hostname}">client.addressing.regional_hostnames.<a href="./src/cloudflare/resources/addressing/regional_hostnames/regional_hostnames.py">delete</a>(hostname, \*, zone_id) -> <a href="./src/cloudflare/types/addressing/regional_hostname_delete_response.py">RegionalHostnameDeleteResponse</a></code>
- <code title="patch /zones/{zone_id}/addressing/regional_hostnames/{hostname}">client.addressing.regional_hostnames.<a href="./src/cloudflare/resources/addressing/regional_hostnames/regional_hostnames.py">edit</a>(hostname, \*, zone_id, \*\*<a href="src/cloudflare/types/addressing/regional_hostname_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/addressing/regional_hostname_edit_response.py">Optional[RegionalHostnameEditResponse]</a></code>
- <code title="get /zones/{zone_id}/addressing/regional_hostnames/{hostname}">client.addressing.regional_hostnames.<a href="./src/cloudflare/resources/addressing/regional_hostnames/regional_hostnames.py">get</a>(hostname, \*, zone_id) -> <a href="./src/cloudflare/types/addressing/regional_hostname_get_response.py">Optional[RegionalHostnameGetResponse]</a></code>

### Regions

Types:

```python
from cloudflare.types.addressing.regional_hostnames import RegionListResponse
```

Methods:

- <code title="get /accounts/{account_id}/addressing/regional_hostnames/regions">client.addressing.regional_hostnames.regions.<a href="./src/cloudflare/resources/addressing/regional_hostnames/regions.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/addressing/regional_hostnames/region_list_response.py">SyncSinglePage[RegionListResponse]</a></code>

## Services

Types:

```python
from cloudflare.types.addressing import ServiceListResponse
```

Methods:

- <code title="get /accounts/{account_id}/addressing/services">client.addressing.services.<a href="./src/cloudflare/resources/addressing/services.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/addressing/service_list_response.py">SyncSinglePage[ServiceListResponse]</a></code>

## AddressMaps

Types:

```python
from cloudflare.types.addressing import (
    AddressMap,
    Kind,
    AddressMapCreateResponse,
    AddressMapDeleteResponse,
    AddressMapGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/addressing/address_maps">client.addressing.address_maps.<a href="./src/cloudflare/resources/addressing/address_maps/address_maps.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/addressing/address_map_create_params.py">params</a>) -> <a href="./src/cloudflare/types/addressing/address_map_create_response.py">Optional[AddressMapCreateResponse]</a></code>
- <code title="get /accounts/{account_id}/addressing/address_maps">client.addressing.address_maps.<a href="./src/cloudflare/resources/addressing/address_maps/address_maps.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/addressing/address_map.py">SyncSinglePage[AddressMap]</a></code>
- <code title="delete /accounts/{account_id}/addressing/address_maps/{address_map_id}">client.addressing.address_maps.<a href="./src/cloudflare/resources/addressing/address_maps/address_maps.py">delete</a>(address_map_id, \*, account_id) -> <a href="./src/cloudflare/types/addressing/address_map_delete_response.py">AddressMapDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/addressing/address_maps/{address_map_id}">client.addressing.address_maps.<a href="./src/cloudflare/resources/addressing/address_maps/address_maps.py">edit</a>(address_map_id, \*, account_id, \*\*<a href="src/cloudflare/types/addressing/address_map_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/addressing/address_map.py">Optional[AddressMap]</a></code>
- <code title="get /accounts/{account_id}/addressing/address_maps/{address_map_id}">client.addressing.address_maps.<a href="./src/cloudflare/resources/addressing/address_maps/address_maps.py">get</a>(address_map_id, \*, account_id) -> <a href="./src/cloudflare/types/addressing/address_map_get_response.py">Optional[AddressMapGetResponse]</a></code>

### Accounts

Types:

```python
from cloudflare.types.addressing.address_maps import AccountUpdateResponse, AccountDeleteResponse
```

Methods:

- <code title="put /accounts/{account_id}/addressing/address_maps/{address_map_id}/accounts/{account_id}">client.addressing.address_maps.accounts.<a href="./src/cloudflare/resources/addressing/address_maps/accounts.py">update</a>(address_map_id, \*, account_id, \*\*<a href="src/cloudflare/types/addressing/address_maps/account_update_params.py">params</a>) -> <a href="./src/cloudflare/types/addressing/address_maps/account_update_response.py">AccountUpdateResponse</a></code>
- <code title="delete /accounts/{account_id}/addressing/address_maps/{address_map_id}/accounts/{account_id}">client.addressing.address_maps.accounts.<a href="./src/cloudflare/resources/addressing/address_maps/accounts.py">delete</a>(address_map_id, \*, account_id) -> <a href="./src/cloudflare/types/addressing/address_maps/account_delete_response.py">AccountDeleteResponse</a></code>

### IPs

Types:

```python
from cloudflare.types.addressing.address_maps import IPUpdateResponse, IPDeleteResponse
```

Methods:

- <code title="put /accounts/{account_id}/addressing/address_maps/{address_map_id}/ips/{ip_address}">client.addressing.address_maps.ips.<a href="./src/cloudflare/resources/addressing/address_maps/ips.py">update</a>(ip_address, \*, account_id, address_map_id, \*\*<a href="src/cloudflare/types/addressing/address_maps/ip_update_params.py">params</a>) -> <a href="./src/cloudflare/types/addressing/address_maps/ip_update_response.py">IPUpdateResponse</a></code>
- <code title="delete /accounts/{account_id}/addressing/address_maps/{address_map_id}/ips/{ip_address}">client.addressing.address_maps.ips.<a href="./src/cloudflare/resources/addressing/address_maps/ips.py">delete</a>(ip_address, \*, account_id, address_map_id) -> <a href="./src/cloudflare/types/addressing/address_maps/ip_delete_response.py">IPDeleteResponse</a></code>

### Zones

Types:

```python
from cloudflare.types.addressing.address_maps import ZoneUpdateResponse, ZoneDeleteResponse
```

Methods:

- <code title="put /accounts/{account_id}/addressing/address_maps/{address_map_id}/zones/{zone_id}">client.addressing.address_maps.zones.<a href="./src/cloudflare/resources/addressing/address_maps/zones.py">update</a>(address_map_id, \*, zone_id, account_id, \*\*<a href="src/cloudflare/types/addressing/address_maps/zone_update_params.py">params</a>) -> <a href="./src/cloudflare/types/addressing/address_maps/zone_update_response.py">ZoneUpdateResponse</a></code>
- <code title="delete /accounts/{account_id}/addressing/address_maps/{address_map_id}/zones/{zone_id}">client.addressing.address_maps.zones.<a href="./src/cloudflare/resources/addressing/address_maps/zones.py">delete</a>(address_map_id, \*, zone_id, account_id) -> <a href="./src/cloudflare/types/addressing/address_maps/zone_delete_response.py">ZoneDeleteResponse</a></code>

## LOADocuments

Types:

```python
from cloudflare.types.addressing import LOADocumentCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/addressing/loa_documents">client.addressing.loa_documents.<a href="./src/cloudflare/resources/addressing/loa_documents.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/addressing/loa_document_create_params.py">params</a>) -> <a href="./src/cloudflare/types/addressing/loa_document_create_response.py">Optional[LOADocumentCreateResponse]</a></code>
- <code title="get /accounts/{account_id}/addressing/loa_documents/{loa_document_id}/download">client.addressing.loa_documents.<a href="./src/cloudflare/resources/addressing/loa_documents.py">get</a>(loa_document_id, \*, account_id) -> BinaryAPIResponse</code>

## Prefixes

Types:

```python
from cloudflare.types.addressing import Prefix, PrefixDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/addressing/prefixes">client.addressing.prefixes.<a href="./src/cloudflare/resources/addressing/prefixes/prefixes.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/addressing/prefix_create_params.py">params</a>) -> <a href="./src/cloudflare/types/addressing/prefix.py">Optional[Prefix]</a></code>
- <code title="get /accounts/{account_id}/addressing/prefixes">client.addressing.prefixes.<a href="./src/cloudflare/resources/addressing/prefixes/prefixes.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/addressing/prefix.py">SyncSinglePage[Prefix]</a></code>
- <code title="delete /accounts/{account_id}/addressing/prefixes/{prefix_id}">client.addressing.prefixes.<a href="./src/cloudflare/resources/addressing/prefixes/prefixes.py">delete</a>(prefix_id, \*, account_id) -> <a href="./src/cloudflare/types/addressing/prefix_delete_response.py">PrefixDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/addressing/prefixes/{prefix_id}">client.addressing.prefixes.<a href="./src/cloudflare/resources/addressing/prefixes/prefixes.py">edit</a>(prefix_id, \*, account_id, \*\*<a href="src/cloudflare/types/addressing/prefix_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/addressing/prefix.py">Optional[Prefix]</a></code>
- <code title="get /accounts/{account_id}/addressing/prefixes/{prefix_id}">client.addressing.prefixes.<a href="./src/cloudflare/resources/addressing/prefixes/prefixes.py">get</a>(prefix_id, \*, account_id) -> <a href="./src/cloudflare/types/addressing/prefix.py">Optional[Prefix]</a></code>

### ServiceBindings

Types:

```python
from cloudflare.types.addressing.prefixes import ServiceBinding, ServiceBindingDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings">client.addressing.prefixes.service_bindings.<a href="./src/cloudflare/resources/addressing/prefixes/service_bindings.py">create</a>(prefix_id, \*, account_id, \*\*<a href="src/cloudflare/types/addressing/prefixes/service_binding_create_params.py">params</a>) -> <a href="./src/cloudflare/types/addressing/prefixes/service_binding.py">Optional[ServiceBinding]</a></code>
- <code title="get /accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings">client.addressing.prefixes.service_bindings.<a href="./src/cloudflare/resources/addressing/prefixes/service_bindings.py">list</a>(prefix_id, \*, account_id) -> <a href="./src/cloudflare/types/addressing/prefixes/service_binding.py">SyncSinglePage[ServiceBinding]</a></code>
- <code title="delete /accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings/{binding_id}">client.addressing.prefixes.service_bindings.<a href="./src/cloudflare/resources/addressing/prefixes/service_bindings.py">delete</a>(binding_id, \*, account_id, prefix_id) -> <a href="./src/cloudflare/types/addressing/prefixes/service_binding_delete_response.py">ServiceBindingDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings/{binding_id}">client.addressing.prefixes.service_bindings.<a href="./src/cloudflare/resources/addressing/prefixes/service_bindings.py">get</a>(binding_id, \*, account_id, prefix_id) -> <a href="./src/cloudflare/types/addressing/prefixes/service_binding.py">Optional[ServiceBinding]</a></code>

### BGPPrefixes

Types:

```python
from cloudflare.types.addressing.prefixes import BGPPrefix
```

Methods:

- <code title="post /accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/prefixes">client.addressing.prefixes.bgp_prefixes.<a href="./src/cloudflare/resources/addressing/prefixes/bgp_prefixes.py">create</a>(prefix_id, \*, account_id, \*\*<a href="src/cloudflare/types/addressing/prefixes/bgp_prefix_create_params.py">params</a>) -> <a href="./src/cloudflare/types/addressing/prefixes/bgp_prefix.py">Optional[BGPPrefix]</a></code>
- <code title="get /accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/prefixes">client.addressing.prefixes.bgp_prefixes.<a href="./src/cloudflare/resources/addressing/prefixes/bgp_prefixes.py">list</a>(prefix_id, \*, account_id) -> <a href="./src/cloudflare/types/addressing/prefixes/bgp_prefix.py">SyncSinglePage[BGPPrefix]</a></code>
- <code title="patch /accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/prefixes/{bgp_prefix_id}">client.addressing.prefixes.bgp_prefixes.<a href="./src/cloudflare/resources/addressing/prefixes/bgp_prefixes.py">edit</a>(bgp_prefix_id, \*, account_id, prefix_id, \*\*<a href="src/cloudflare/types/addressing/prefixes/bgp_prefix_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/addressing/prefixes/bgp_prefix.py">Optional[BGPPrefix]</a></code>
- <code title="get /accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/prefixes/{bgp_prefix_id}">client.addressing.prefixes.bgp_prefixes.<a href="./src/cloudflare/resources/addressing/prefixes/bgp_prefixes.py">get</a>(bgp_prefix_id, \*, account_id, prefix_id) -> <a href="./src/cloudflare/types/addressing/prefixes/bgp_prefix.py">Optional[BGPPrefix]</a></code>

### AdvertisementStatus

Types:

```python
from cloudflare.types.addressing.prefixes import (
    AdvertisementStatusEditResponse,
    AdvertisementStatusGetResponse,
)
```

Methods:

- <code title="patch /accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/status">client.addressing.prefixes.advertisement_status.<a href="./src/cloudflare/resources/addressing/prefixes/advertisement_status.py">edit</a>(prefix_id, \*, account_id, \*\*<a href="src/cloudflare/types/addressing/prefixes/advertisement_status_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/addressing/prefixes/advertisement_status_edit_response.py">Optional[AdvertisementStatusEditResponse]</a></code>
- <code title="get /accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/status">client.addressing.prefixes.advertisement_status.<a href="./src/cloudflare/resources/addressing/prefixes/advertisement_status.py">get</a>(prefix_id, \*, account_id) -> <a href="./src/cloudflare/types/addressing/prefixes/advertisement_status_get_response.py">Optional[AdvertisementStatusGetResponse]</a></code>

### Delegations

Types:

```python
from cloudflare.types.addressing.prefixes import Delegations, DelegationDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/addressing/prefixes/{prefix_id}/delegations">client.addressing.prefixes.delegations.<a href="./src/cloudflare/resources/addressing/prefixes/delegations.py">create</a>(prefix_id, \*, account_id, \*\*<a href="src/cloudflare/types/addressing/prefixes/delegation_create_params.py">params</a>) -> <a href="./src/cloudflare/types/addressing/prefixes/delegations.py">Optional[Delegations]</a></code>
- <code title="get /accounts/{account_id}/addressing/prefixes/{prefix_id}/delegations">client.addressing.prefixes.delegations.<a href="./src/cloudflare/resources/addressing/prefixes/delegations.py">list</a>(prefix_id, \*, account_id) -> <a href="./src/cloudflare/types/addressing/prefixes/delegations.py">SyncSinglePage[Delegations]</a></code>
- <code title="delete /accounts/{account_id}/addressing/prefixes/{prefix_id}/delegations/{delegation_id}">client.addressing.prefixes.delegations.<a href="./src/cloudflare/resources/addressing/prefixes/delegations.py">delete</a>(delegation_id, \*, account_id, prefix_id) -> <a href="./src/cloudflare/types/addressing/prefixes/delegation_delete_response.py">Optional[DelegationDeleteResponse]</a></code>
