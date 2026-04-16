# MagicTransit

Types:

```python
from cloudflare.types.magic_transit import HealthCheck, HealthCheckRate, HealthCheckType
```

## Apps

Types:

```python
from cloudflare.types.magic_transit import (
    AppCreateResponse,
    AppUpdateResponse,
    AppListResponse,
    AppDeleteResponse,
    AppEditResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/magic/apps">client.magic_transit.apps.<a href="./src/cloudflare/resources/magic_transit/apps.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/app_create_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/app_create_response.py">Optional[AppCreateResponse]</a></code>
- <code title="put /accounts/{account_id}/magic/apps/{account_app_id}">client.magic_transit.apps.<a href="./src/cloudflare/resources/magic_transit/apps.py">update</a>(account_app_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/app_update_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/app_update_response.py">Optional[AppUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/magic/apps">client.magic_transit.apps.<a href="./src/cloudflare/resources/magic_transit/apps.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/magic_transit/app_list_response.py">SyncSinglePage[AppListResponse]</a></code>
- <code title="delete /accounts/{account_id}/magic/apps/{account_app_id}">client.magic_transit.apps.<a href="./src/cloudflare/resources/magic_transit/apps.py">delete</a>(account_app_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_transit/app_delete_response.py">Optional[AppDeleteResponse]</a></code>
- <code title="patch /accounts/{account_id}/magic/apps/{account_app_id}">client.magic_transit.apps.<a href="./src/cloudflare/resources/magic_transit/apps.py">edit</a>(account_app_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/app_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/app_edit_response.py">Optional[AppEditResponse]</a></code>

## CfInterconnects

Types:

```python
from cloudflare.types.magic_transit import (
    CfInterconnectUpdateResponse,
    CfInterconnectListResponse,
    CfInterconnectBulkUpdateResponse,
    CfInterconnectGetResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/magic/cf_interconnects/{cf_interconnect_id}">client.magic_transit.cf_interconnects.<a href="./src/cloudflare/resources/magic_transit/cf_interconnects.py">update</a>(cf_interconnect_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/cf_interconnect_update_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/cf_interconnect_update_response.py">CfInterconnectUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/magic/cf_interconnects">client.magic_transit.cf_interconnects.<a href="./src/cloudflare/resources/magic_transit/cf_interconnects.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/magic_transit/cf_interconnect_list_response.py">CfInterconnectListResponse</a></code>
- <code title="put /accounts/{account_id}/magic/cf_interconnects">client.magic_transit.cf_interconnects.<a href="./src/cloudflare/resources/magic_transit/cf_interconnects.py">bulk_update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/cf_interconnect_bulk_update_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/cf_interconnect_bulk_update_response.py">CfInterconnectBulkUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/magic/cf_interconnects/{cf_interconnect_id}">client.magic_transit.cf_interconnects.<a href="./src/cloudflare/resources/magic_transit/cf_interconnects.py">get</a>(cf_interconnect_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_transit/cf_interconnect_get_response.py">CfInterconnectGetResponse</a></code>

## GRETunnels

Types:

```python
from cloudflare.types.magic_transit import (
    GRETunnelCreateResponse,
    GRETunnelUpdateResponse,
    GRETunnelListResponse,
    GRETunnelDeleteResponse,
    GRETunnelBulkUpdateResponse,
    GRETunnelGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/magic/gre_tunnels">client.magic_transit.gre_tunnels.<a href="./src/cloudflare/resources/magic_transit/gre_tunnels.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/gre_tunnel_create_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/gre_tunnel_create_response.py">GRETunnelCreateResponse</a></code>
- <code title="put /accounts/{account_id}/magic/gre_tunnels/{gre_tunnel_id}">client.magic_transit.gre_tunnels.<a href="./src/cloudflare/resources/magic_transit/gre_tunnels.py">update</a>(gre_tunnel_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/gre_tunnel_update_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/gre_tunnel_update_response.py">GRETunnelUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/magic/gre_tunnels">client.magic_transit.gre_tunnels.<a href="./src/cloudflare/resources/magic_transit/gre_tunnels.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/magic_transit/gre_tunnel_list_response.py">GRETunnelListResponse</a></code>
- <code title="delete /accounts/{account_id}/magic/gre_tunnels/{gre_tunnel_id}">client.magic_transit.gre_tunnels.<a href="./src/cloudflare/resources/magic_transit/gre_tunnels.py">delete</a>(gre_tunnel_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_transit/gre_tunnel_delete_response.py">GRETunnelDeleteResponse</a></code>
- <code title="put /accounts/{account_id}/magic/gre_tunnels">client.magic_transit.gre_tunnels.<a href="./src/cloudflare/resources/magic_transit/gre_tunnels.py">bulk_update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/gre_tunnel_bulk_update_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/gre_tunnel_bulk_update_response.py">GRETunnelBulkUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/magic/gre_tunnels/{gre_tunnel_id}">client.magic_transit.gre_tunnels.<a href="./src/cloudflare/resources/magic_transit/gre_tunnels.py">get</a>(gre_tunnel_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_transit/gre_tunnel_get_response.py">GRETunnelGetResponse</a></code>

## IPSECTunnels

Types:

```python
from cloudflare.types.magic_transit import (
    PSKMetadata,
    IPSECTunnelCreateResponse,
    IPSECTunnelUpdateResponse,
    IPSECTunnelListResponse,
    IPSECTunnelDeleteResponse,
    IPSECTunnelBulkUpdateResponse,
    IPSECTunnelGetResponse,
    IPSECTunnelPSKGenerateResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/magic/ipsec_tunnels">client.magic_transit.ipsec_tunnels.<a href="./src/cloudflare/resources/magic_transit/ipsec_tunnels.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/ipsec_tunnel_create_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/ipsec_tunnel_create_response.py">IPSECTunnelCreateResponse</a></code>
- <code title="put /accounts/{account_id}/magic/ipsec_tunnels/{ipsec_tunnel_id}">client.magic_transit.ipsec_tunnels.<a href="./src/cloudflare/resources/magic_transit/ipsec_tunnels.py">update</a>(ipsec_tunnel_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/ipsec_tunnel_update_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/ipsec_tunnel_update_response.py">IPSECTunnelUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/magic/ipsec_tunnels">client.magic_transit.ipsec_tunnels.<a href="./src/cloudflare/resources/magic_transit/ipsec_tunnels.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/magic_transit/ipsec_tunnel_list_response.py">IPSECTunnelListResponse</a></code>
- <code title="delete /accounts/{account_id}/magic/ipsec_tunnels/{ipsec_tunnel_id}">client.magic_transit.ipsec_tunnels.<a href="./src/cloudflare/resources/magic_transit/ipsec_tunnels.py">delete</a>(ipsec_tunnel_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_transit/ipsec_tunnel_delete_response.py">IPSECTunnelDeleteResponse</a></code>
- <code title="put /accounts/{account_id}/magic/ipsec_tunnels">client.magic_transit.ipsec_tunnels.<a href="./src/cloudflare/resources/magic_transit/ipsec_tunnels.py">bulk_update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/ipsec_tunnel_bulk_update_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/ipsec_tunnel_bulk_update_response.py">IPSECTunnelBulkUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/magic/ipsec_tunnels/{ipsec_tunnel_id}">client.magic_transit.ipsec_tunnels.<a href="./src/cloudflare/resources/magic_transit/ipsec_tunnels.py">get</a>(ipsec_tunnel_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_transit/ipsec_tunnel_get_response.py">IPSECTunnelGetResponse</a></code>
- <code title="post /accounts/{account_id}/magic/ipsec_tunnels/{ipsec_tunnel_id}/psk_generate">client.magic_transit.ipsec_tunnels.<a href="./src/cloudflare/resources/magic_transit/ipsec_tunnels.py">psk_generate</a>(ipsec_tunnel_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/ipsec_tunnel_psk_generate_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/ipsec_tunnel_psk_generate_response.py">IPSECTunnelPSKGenerateResponse</a></code>

## Routes

Types:

```python
from cloudflare.types.magic_transit import (
    Scope,
    RouteCreateResponse,
    RouteUpdateResponse,
    RouteListResponse,
    RouteDeleteResponse,
    RouteBulkUpdateResponse,
    RouteEmptyResponse,
    RouteGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/magic/routes">client.magic_transit.routes.<a href="./src/cloudflare/resources/magic_transit/routes.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/route_create_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/route_create_response.py">RouteCreateResponse</a></code>
- <code title="put /accounts/{account_id}/magic/routes/{route_id}">client.magic_transit.routes.<a href="./src/cloudflare/resources/magic_transit/routes.py">update</a>(route_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/route_update_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/route_update_response.py">RouteUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/magic/routes">client.magic_transit.routes.<a href="./src/cloudflare/resources/magic_transit/routes.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/magic_transit/route_list_response.py">RouteListResponse</a></code>
- <code title="delete /accounts/{account_id}/magic/routes/{route_id}">client.magic_transit.routes.<a href="./src/cloudflare/resources/magic_transit/routes.py">delete</a>(route_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_transit/route_delete_response.py">RouteDeleteResponse</a></code>
- <code title="put /accounts/{account_id}/magic/routes">client.magic_transit.routes.<a href="./src/cloudflare/resources/magic_transit/routes.py">bulk_update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/route_bulk_update_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/route_bulk_update_response.py">RouteBulkUpdateResponse</a></code>
- <code title="delete /accounts/{account_id}/magic/routes">client.magic_transit.routes.<a href="./src/cloudflare/resources/magic_transit/routes.py">empty</a>(\*, account_id) -> <a href="./src/cloudflare/types/magic_transit/route_empty_response.py">RouteEmptyResponse</a></code>
- <code title="get /accounts/{account_id}/magic/routes/{route_id}">client.magic_transit.routes.<a href="./src/cloudflare/resources/magic_transit/routes.py">get</a>(route_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_transit/route_get_response.py">RouteGetResponse</a></code>

## Sites

Types:

```python
from cloudflare.types.magic_transit import Site, SiteLocation
```

Methods:

- <code title="post /accounts/{account_id}/magic/sites">client.magic_transit.sites.<a href="./src/cloudflare/resources/magic_transit/sites/sites.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/site_create_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/site.py">Site</a></code>
- <code title="put /accounts/{account_id}/magic/sites/{site_id}">client.magic_transit.sites.<a href="./src/cloudflare/resources/magic_transit/sites/sites.py">update</a>(site_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/site_update_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/site.py">Site</a></code>
- <code title="get /accounts/{account_id}/magic/sites">client.magic_transit.sites.<a href="./src/cloudflare/resources/magic_transit/sites/sites.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/site_list_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/site.py">SyncSinglePage[Site]</a></code>
- <code title="delete /accounts/{account_id}/magic/sites/{site_id}">client.magic_transit.sites.<a href="./src/cloudflare/resources/magic_transit/sites/sites.py">delete</a>(site_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_transit/site.py">Site</a></code>
- <code title="patch /accounts/{account_id}/magic/sites/{site_id}">client.magic_transit.sites.<a href="./src/cloudflare/resources/magic_transit/sites/sites.py">edit</a>(site_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/site_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/site.py">Site</a></code>
- <code title="get /accounts/{account_id}/magic/sites/{site_id}">client.magic_transit.sites.<a href="./src/cloudflare/resources/magic_transit/sites/sites.py">get</a>(site_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_transit/site.py">Site</a></code>

### ACLs

Types:

```python
from cloudflare.types.magic_transit.sites import ACL, ACLConfiguration, AllowedProtocol, Subnet
```

Methods:

- <code title="post /accounts/{account_id}/magic/sites/{site_id}/acls">client.magic_transit.sites.acls.<a href="./src/cloudflare/resources/magic_transit/sites/acls.py">create</a>(site_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/sites/acl_create_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/sites/acl.py">ACL</a></code>
- <code title="put /accounts/{account_id}/magic/sites/{site_id}/acls/{acl_id}">client.magic_transit.sites.acls.<a href="./src/cloudflare/resources/magic_transit/sites/acls.py">update</a>(acl_id, \*, account_id, site_id, \*\*<a href="src/cloudflare/types/magic_transit/sites/acl_update_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/sites/acl.py">ACL</a></code>
- <code title="get /accounts/{account_id}/magic/sites/{site_id}/acls">client.magic_transit.sites.acls.<a href="./src/cloudflare/resources/magic_transit/sites/acls.py">list</a>(site_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_transit/sites/acl.py">SyncSinglePage[ACL]</a></code>
- <code title="delete /accounts/{account_id}/magic/sites/{site_id}/acls/{acl_id}">client.magic_transit.sites.acls.<a href="./src/cloudflare/resources/magic_transit/sites/acls.py">delete</a>(acl_id, \*, account_id, site_id) -> <a href="./src/cloudflare/types/magic_transit/sites/acl.py">ACL</a></code>
- <code title="patch /accounts/{account_id}/magic/sites/{site_id}/acls/{acl_id}">client.magic_transit.sites.acls.<a href="./src/cloudflare/resources/magic_transit/sites/acls.py">edit</a>(acl_id, \*, account_id, site_id, \*\*<a href="src/cloudflare/types/magic_transit/sites/acl_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/sites/acl.py">ACL</a></code>
- <code title="get /accounts/{account_id}/magic/sites/{site_id}/acls/{acl_id}">client.magic_transit.sites.acls.<a href="./src/cloudflare/resources/magic_transit/sites/acls.py">get</a>(acl_id, \*, account_id, site_id) -> <a href="./src/cloudflare/types/magic_transit/sites/acl.py">ACL</a></code>

### LANs

Types:

```python
from cloudflare.types.magic_transit.sites import (
    DHCPRelay,
    DHCPServer,
    LAN,
    LANStaticAddressing,
    Nat,
    RoutedSubnet,
)
```

Methods:

- <code title="post /accounts/{account_id}/magic/sites/{site_id}/lans">client.magic_transit.sites.lans.<a href="./src/cloudflare/resources/magic_transit/sites/lans.py">create</a>(site_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/sites/lan_create_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/sites/lan.py">SyncSinglePage[LAN]</a></code>
- <code title="put /accounts/{account_id}/magic/sites/{site_id}/lans/{lan_id}">client.magic_transit.sites.lans.<a href="./src/cloudflare/resources/magic_transit/sites/lans.py">update</a>(lan_id, \*, account_id, site_id, \*\*<a href="src/cloudflare/types/magic_transit/sites/lan_update_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/sites/lan.py">LAN</a></code>
- <code title="get /accounts/{account_id}/magic/sites/{site_id}/lans">client.magic_transit.sites.lans.<a href="./src/cloudflare/resources/magic_transit/sites/lans.py">list</a>(site_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_transit/sites/lan.py">SyncSinglePage[LAN]</a></code>
- <code title="delete /accounts/{account_id}/magic/sites/{site_id}/lans/{lan_id}">client.magic_transit.sites.lans.<a href="./src/cloudflare/resources/magic_transit/sites/lans.py">delete</a>(lan_id, \*, account_id, site_id) -> <a href="./src/cloudflare/types/magic_transit/sites/lan.py">LAN</a></code>
- <code title="patch /accounts/{account_id}/magic/sites/{site_id}/lans/{lan_id}">client.magic_transit.sites.lans.<a href="./src/cloudflare/resources/magic_transit/sites/lans.py">edit</a>(lan_id, \*, account_id, site_id, \*\*<a href="src/cloudflare/types/magic_transit/sites/lan_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/sites/lan.py">LAN</a></code>
- <code title="get /accounts/{account_id}/magic/sites/{site_id}/lans/{lan_id}">client.magic_transit.sites.lans.<a href="./src/cloudflare/resources/magic_transit/sites/lans.py">get</a>(lan_id, \*, account_id, site_id) -> <a href="./src/cloudflare/types/magic_transit/sites/lan.py">LAN</a></code>

### WANs

Types:

```python
from cloudflare.types.magic_transit.sites import WAN, WANStaticAddressing
```

Methods:

- <code title="post /accounts/{account_id}/magic/sites/{site_id}/wans">client.magic_transit.sites.wans.<a href="./src/cloudflare/resources/magic_transit/sites/wans.py">create</a>(site_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/sites/wan_create_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/sites/wan.py">SyncSinglePage[WAN]</a></code>
- <code title="put /accounts/{account_id}/magic/sites/{site_id}/wans/{wan_id}">client.magic_transit.sites.wans.<a href="./src/cloudflare/resources/magic_transit/sites/wans.py">update</a>(wan_id, \*, account_id, site_id, \*\*<a href="src/cloudflare/types/magic_transit/sites/wan_update_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/sites/wan.py">WAN</a></code>
- <code title="get /accounts/{account_id}/magic/sites/{site_id}/wans">client.magic_transit.sites.wans.<a href="./src/cloudflare/resources/magic_transit/sites/wans.py">list</a>(site_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_transit/sites/wan.py">SyncSinglePage[WAN]</a></code>
- <code title="delete /accounts/{account_id}/magic/sites/{site_id}/wans/{wan_id}">client.magic_transit.sites.wans.<a href="./src/cloudflare/resources/magic_transit/sites/wans.py">delete</a>(wan_id, \*, account_id, site_id) -> <a href="./src/cloudflare/types/magic_transit/sites/wan.py">WAN</a></code>
- <code title="patch /accounts/{account_id}/magic/sites/{site_id}/wans/{wan_id}">client.magic_transit.sites.wans.<a href="./src/cloudflare/resources/magic_transit/sites/wans.py">edit</a>(wan_id, \*, account_id, site_id, \*\*<a href="src/cloudflare/types/magic_transit/sites/wan_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/sites/wan.py">WAN</a></code>
- <code title="get /accounts/{account_id}/magic/sites/{site_id}/wans/{wan_id}">client.magic_transit.sites.wans.<a href="./src/cloudflare/resources/magic_transit/sites/wans.py">get</a>(wan_id, \*, account_id, site_id) -> <a href="./src/cloudflare/types/magic_transit/sites/wan.py">WAN</a></code>

## Connectors

Types:

```python
from cloudflare.types.magic_transit import (
    ConnectorCreateResponse,
    ConnectorUpdateResponse,
    ConnectorListResponse,
    ConnectorDeleteResponse,
    ConnectorEditResponse,
    ConnectorGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/magic/connectors">client.magic_transit.connectors.<a href="./src/cloudflare/resources/magic_transit/connectors/connectors.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/connector_create_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/connector_create_response.py">ConnectorCreateResponse</a></code>
- <code title="put /accounts/{account_id}/magic/connectors/{connector_id}">client.magic_transit.connectors.<a href="./src/cloudflare/resources/magic_transit/connectors/connectors.py">update</a>(connector_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/connector_update_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/connector_update_response.py">ConnectorUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/magic/connectors">client.magic_transit.connectors.<a href="./src/cloudflare/resources/magic_transit/connectors/connectors.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/magic_transit/connector_list_response.py">SyncSinglePage[ConnectorListResponse]</a></code>
- <code title="delete /accounts/{account_id}/magic/connectors/{connector_id}">client.magic_transit.connectors.<a href="./src/cloudflare/resources/magic_transit/connectors/connectors.py">delete</a>(connector_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_transit/connector_delete_response.py">ConnectorDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/magic/connectors/{connector_id}">client.magic_transit.connectors.<a href="./src/cloudflare/resources/magic_transit/connectors/connectors.py">edit</a>(connector_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/connector_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/connector_edit_response.py">ConnectorEditResponse</a></code>
- <code title="get /accounts/{account_id}/magic/connectors/{connector_id}">client.magic_transit.connectors.<a href="./src/cloudflare/resources/magic_transit/connectors/connectors.py">get</a>(connector_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_transit/connector_get_response.py">ConnectorGetResponse</a></code>

### Events

Types:

```python
from cloudflare.types.magic_transit.connectors import EventListResponse, EventGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/magic/connectors/{connector_id}/telemetry/events">client.magic_transit.connectors.events.<a href="./src/cloudflare/resources/magic_transit/connectors/events/events.py">list</a>(connector_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/connectors/event_list_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/connectors/event_list_response.py">EventListResponse</a></code>
- <code title="get /accounts/{account_id}/magic/connectors/{connector_id}/telemetry/events/{event_t}.{event_n}">client.magic_transit.connectors.events.<a href="./src/cloudflare/resources/magic_transit/connectors/events/events.py">get</a>(event_n, \*, account_id, connector_id, event_t) -> <a href="./src/cloudflare/types/magic_transit/connectors/event_get_response.py">EventGetResponse</a></code>

#### Latest

Types:

```python
from cloudflare.types.magic_transit.connectors.events import LatestListResponse
```

Methods:

- <code title="get /accounts/{account_id}/magic/connectors/{connector_id}/telemetry/events/latest">client.magic_transit.connectors.events.latest.<a href="./src/cloudflare/resources/magic_transit/connectors/events/latest.py">list</a>(connector_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_transit/connectors/events/latest_list_response.py">LatestListResponse</a></code>

### Snapshots

Types:

```python
from cloudflare.types.magic_transit.connectors import SnapshotListResponse, SnapshotGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/magic/connectors/{connector_id}/telemetry/snapshots">client.magic_transit.connectors.snapshots.<a href="./src/cloudflare/resources/magic_transit/connectors/snapshots/snapshots.py">list</a>(connector_id, \*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/connectors/snapshot_list_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/connectors/snapshot_list_response.py">SnapshotListResponse</a></code>
- <code title="get /accounts/{account_id}/magic/connectors/{connector_id}/telemetry/snapshots/{snapshot_t}">client.magic_transit.connectors.snapshots.<a href="./src/cloudflare/resources/magic_transit/connectors/snapshots/snapshots.py">get</a>(snapshot_t, \*, account_id, connector_id) -> <a href="./src/cloudflare/types/magic_transit/connectors/snapshot_get_response.py">SnapshotGetResponse</a></code>

#### Latest

Types:

```python
from cloudflare.types.magic_transit.connectors.snapshots import LatestListResponse
```

Methods:

- <code title="get /accounts/{account_id}/magic/connectors/{connector_id}/telemetry/snapshots/latest">client.magic_transit.connectors.snapshots.latest.<a href="./src/cloudflare/resources/magic_transit/connectors/snapshots/latest.py">list</a>(connector_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_transit/connectors/snapshots/latest_list_response.py">LatestListResponse</a></code>

## PCAPs

Types:

```python
from cloudflare.types.magic_transit import (
    PCAP,
    PCAPFilter,
    PCAPCreateResponse,
    PCAPListResponse,
    PCAPGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/pcaps">client.magic_transit.pcaps.<a href="./src/cloudflare/resources/magic_transit/pcaps/pcaps.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/pcap_create_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/pcap_create_response.py">PCAPCreateResponse</a></code>
- <code title="get /accounts/{account_id}/pcaps">client.magic_transit.pcaps.<a href="./src/cloudflare/resources/magic_transit/pcaps/pcaps.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/magic_transit/pcap_list_response.py">SyncSinglePage[PCAPListResponse]</a></code>
- <code title="get /accounts/{account_id}/pcaps/{pcap_id}">client.magic_transit.pcaps.<a href="./src/cloudflare/resources/magic_transit/pcaps/pcaps.py">get</a>(pcap_id, \*, account_id) -> <a href="./src/cloudflare/types/magic_transit/pcap_get_response.py">PCAPGetResponse</a></code>
- <code title="put /accounts/{account_id}/pcaps/{pcap_id}/stop">client.magic_transit.pcaps.<a href="./src/cloudflare/resources/magic_transit/pcaps/pcaps.py">stop</a>(pcap_id, \*, account_id) -> None</code>

### Ownership

Types:

```python
from cloudflare.types.magic_transit.pcaps import Ownership
```

Methods:

- <code title="post /accounts/{account_id}/pcaps/ownership">client.magic_transit.pcaps.ownership.<a href="./src/cloudflare/resources/magic_transit/pcaps/ownership.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/pcaps/ownership_create_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/pcaps/ownership.py">Ownership</a></code>
- <code title="delete /accounts/{account_id}/pcaps/ownership/{ownership_id}">client.magic_transit.pcaps.ownership.<a href="./src/cloudflare/resources/magic_transit/pcaps/ownership.py">delete</a>(ownership_id, \*, account_id) -> None</code>
- <code title="get /accounts/{account_id}/pcaps/ownership">client.magic_transit.pcaps.ownership.<a href="./src/cloudflare/resources/magic_transit/pcaps/ownership.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/magic_transit/pcaps/ownership.py">SyncSinglePage[Ownership]</a></code>
- <code title="post /accounts/{account_id}/pcaps/ownership/validate">client.magic_transit.pcaps.ownership.<a href="./src/cloudflare/resources/magic_transit/pcaps/ownership.py">validate</a>(\*, account_id, \*\*<a href="src/cloudflare/types/magic_transit/pcaps/ownership_validate_params.py">params</a>) -> <a href="./src/cloudflare/types/magic_transit/pcaps/ownership.py">Ownership</a></code>

### Download

Methods:

- <code title="get /accounts/{account_id}/pcaps/{pcap_id}/download">client.magic_transit.pcaps.download.<a href="./src/cloudflare/resources/magic_transit/pcaps/download.py">get</a>(pcap_id, \*, account_id) -> BinaryAPIResponse</code>
