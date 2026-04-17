# NetworkInterconnects

## CNIs

Types:

```python
from cloudflare.types.network_interconnects import (
    CNICreateResponse,
    CNIUpdateResponse,
    CNIListResponse,
    CNIGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/cni/cnis">client.network_interconnects.cnis.<a href="./src/cloudflare/resources/network_interconnects/cnis.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/network_interconnects/cni_create_params.py">params</a>) -> <a href="./src/cloudflare/types/network_interconnects/cni_create_response.py">CNICreateResponse</a></code>
- <code title="put /accounts/{account_id}/cni/cnis/{cni}">client.network_interconnects.cnis.<a href="./src/cloudflare/resources/network_interconnects/cnis.py">update</a>(cni, \*, account_id, \*\*<a href="src/cloudflare/types/network_interconnects/cni_update_params.py">params</a>) -> <a href="./src/cloudflare/types/network_interconnects/cni_update_response.py">CNIUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/cni/cnis">client.network_interconnects.cnis.<a href="./src/cloudflare/resources/network_interconnects/cnis.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/network_interconnects/cni_list_params.py">params</a>) -> <a href="./src/cloudflare/types/network_interconnects/cni_list_response.py">CNIListResponse</a></code>
- <code title="delete /accounts/{account_id}/cni/cnis/{cni}">client.network_interconnects.cnis.<a href="./src/cloudflare/resources/network_interconnects/cnis.py">delete</a>(cni, \*, account_id) -> None</code>
- <code title="get /accounts/{account_id}/cni/cnis/{cni}">client.network_interconnects.cnis.<a href="./src/cloudflare/resources/network_interconnects/cnis.py">get</a>(cni, \*, account_id) -> <a href="./src/cloudflare/types/network_interconnects/cni_get_response.py">CNIGetResponse</a></code>

## Interconnects

Types:

```python
from cloudflare.types.network_interconnects import (
    InterconnectCreateResponse,
    InterconnectListResponse,
    InterconnectGetResponse,
    InterconnectStatusResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/cni/interconnects">client.network_interconnects.interconnects.<a href="./src/cloudflare/resources/network_interconnects/interconnects.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/network_interconnects/interconnect_create_params.py">params</a>) -> <a href="./src/cloudflare/types/network_interconnects/interconnect_create_response.py">InterconnectCreateResponse</a></code>
- <code title="get /accounts/{account_id}/cni/interconnects">client.network_interconnects.interconnects.<a href="./src/cloudflare/resources/network_interconnects/interconnects.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/network_interconnects/interconnect_list_params.py">params</a>) -> <a href="./src/cloudflare/types/network_interconnects/interconnect_list_response.py">InterconnectListResponse</a></code>
- <code title="delete /accounts/{account_id}/cni/interconnects/{icon}">client.network_interconnects.interconnects.<a href="./src/cloudflare/resources/network_interconnects/interconnects.py">delete</a>(icon, \*, account_id) -> None</code>
- <code title="get /accounts/{account_id}/cni/interconnects/{icon}">client.network_interconnects.interconnects.<a href="./src/cloudflare/resources/network_interconnects/interconnects.py">get</a>(icon, \*, account_id) -> <a href="./src/cloudflare/types/network_interconnects/interconnect_get_response.py">InterconnectGetResponse</a></code>
- <code title="get /accounts/{account_id}/cni/interconnects/{icon}/loa">client.network_interconnects.interconnects.<a href="./src/cloudflare/resources/network_interconnects/interconnects.py">loa</a>(icon, \*, account_id) -> None</code>
- <code title="get /accounts/{account_id}/cni/interconnects/{icon}/status">client.network_interconnects.interconnects.<a href="./src/cloudflare/resources/network_interconnects/interconnects.py">status</a>(icon, \*, account_id) -> <a href="./src/cloudflare/types/network_interconnects/interconnect_status_response.py">InterconnectStatusResponse</a></code>

## Settings

Types:

```python
from cloudflare.types.network_interconnects import SettingUpdateResponse, SettingGetResponse
```

Methods:

- <code title="put /accounts/{account_id}/cni/settings">client.network_interconnects.settings.<a href="./src/cloudflare/resources/network_interconnects/settings.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/network_interconnects/setting_update_params.py">params</a>) -> <a href="./src/cloudflare/types/network_interconnects/setting_update_response.py">SettingUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/cni/settings">client.network_interconnects.settings.<a href="./src/cloudflare/resources/network_interconnects/settings.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/network_interconnects/setting_get_response.py">SettingGetResponse</a></code>

## Slots

Types:

```python
from cloudflare.types.network_interconnects import SlotListResponse, SlotGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/cni/slots">client.network_interconnects.slots.<a href="./src/cloudflare/resources/network_interconnects/slots.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/network_interconnects/slot_list_params.py">params</a>) -> <a href="./src/cloudflare/types/network_interconnects/slot_list_response.py">SlotListResponse</a></code>
- <code title="get /accounts/{account_id}/cni/slots/{slot}">client.network_interconnects.slots.<a href="./src/cloudflare/resources/network_interconnects/slots.py">get</a>(slot, \*, account_id) -> <a href="./src/cloudflare/types/network_interconnects/slot_get_response.py">SlotGetResponse</a></code>
