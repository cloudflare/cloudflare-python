# DDoSProtection

## AdvancedTCPProtection

### Allowlist

Types:

```python
from cloudflare.types.ddos_protection.advanced_tcp_protection import (
    AllowlistCreateResponse,
    AllowlistListResponse,
    AllowlistBulkDeleteResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/magic/advanced_tcp_protection/configs/allowlist">client.ddos_protection.advanced_tcp_protection.allowlist.<a href="./src/cloudflare/resources/ddos_protection/advanced_tcp_protection/allowlist/allowlist.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/ddos_protection/advanced_tcp_protection/allowlist_create_params.py">params</a>) -> <a href="./src/cloudflare/types/ddos_protection/advanced_tcp_protection/allowlist_create_response.py">Optional[AllowlistCreateResponse]</a></code>
- <code title="get /accounts/{account_id}/magic/advanced_tcp_protection/configs/allowlist">client.ddos_protection.advanced_tcp_protection.allowlist.<a href="./src/cloudflare/resources/ddos_protection/advanced_tcp_protection/allowlist/allowlist.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/ddos_protection/advanced_tcp_protection/allowlist_list_params.py">params</a>) -> <a href="./src/cloudflare/types/ddos_protection/advanced_tcp_protection/allowlist_list_response.py">SyncV4PagePaginationArray[AllowlistListResponse]</a></code>
- <code title="delete /accounts/{account_id}/magic/advanced_tcp_protection/configs/allowlist">client.ddos_protection.advanced_tcp_protection.allowlist.<a href="./src/cloudflare/resources/ddos_protection/advanced_tcp_protection/allowlist/allowlist.py">bulk_delete</a>(\*, account_id) -> <a href="./src/cloudflare/types/ddos_protection/advanced_tcp_protection/allowlist_bulk_delete_response.py">AllowlistBulkDeleteResponse</a></code>

#### Items

Types:

```python
from cloudflare.types.ddos_protection.advanced_tcp_protection.allowlist import (
    ItemDeleteResponse,
    ItemEditResponse,
    ItemGetResponse,
)
```

Methods:

- <code title="delete /accounts/{account_id}/magic/advanced_tcp_protection/configs/allowlist/{prefix_id}">client.ddos_protection.advanced_tcp_protection.allowlist.items.<a href="./src/cloudflare/resources/ddos_protection/advanced_tcp_protection/allowlist/items.py">delete</a>(prefix_id, \*, account_id) -> <a href="./src/cloudflare/types/ddos_protection/advanced_tcp_protection/allowlist/item_delete_response.py">ItemDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/magic/advanced_tcp_protection/configs/allowlist/{prefix_id}">client.ddos_protection.advanced_tcp_protection.allowlist.items.<a href="./src/cloudflare/resources/ddos_protection/advanced_tcp_protection/allowlist/items.py">edit</a>(prefix_id, \*, account_id, \*\*<a href="src/cloudflare/types/ddos_protection/advanced_tcp_protection/allowlist/item_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/ddos_protection/advanced_tcp_protection/allowlist/item_edit_response.py">Optional[ItemEditResponse]</a></code>
- <code title="get /accounts/{account_id}/magic/advanced_tcp_protection/configs/allowlist/{prefix_id}">client.ddos_protection.advanced_tcp_protection.allowlist.items.<a href="./src/cloudflare/resources/ddos_protection/advanced_tcp_protection/allowlist/items.py">get</a>(prefix_id, \*, account_id) -> <a href="./src/cloudflare/types/ddos_protection/advanced_tcp_protection/allowlist/item_get_response.py">Optional[ItemGetResponse]</a></code>

### Prefixes

Types:

```python
from cloudflare.types.ddos_protection.advanced_tcp_protection import (
    PrefixCreateResponse,
    PrefixListResponse,
    PrefixBulkCreateResponse,
    PrefixBulkDeleteResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/magic/advanced_tcp_protection/configs/prefixes">client.ddos_protection.advanced_tcp_protection.prefixes.<a href="./src/cloudflare/resources/ddos_protection/advanced_tcp_protection/prefixes/prefixes.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/ddos_protection/advanced_tcp_protection/prefix_create_params.py">params</a>) -> <a href="./src/cloudflare/types/ddos_protection/advanced_tcp_protection/prefix_create_response.py">Optional[PrefixCreateResponse]</a></code>
- <code title="get /accounts/{account_id}/magic/advanced_tcp_protection/configs/prefixes">client.ddos_protection.advanced_tcp_protection.prefixes.<a href="./src/cloudflare/resources/ddos_protection/advanced_tcp_protection/prefixes/prefixes.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/ddos_protection/advanced_tcp_protection/prefix_list_params.py">params</a>) -> <a href="./src/cloudflare/types/ddos_protection/advanced_tcp_protection/prefix_list_response.py">SyncV4PagePaginationArray[PrefixListResponse]</a></code>
- <code title="post /accounts/{account_id}/magic/advanced_tcp_protection/configs/prefixes/bulk">client.ddos_protection.advanced_tcp_protection.prefixes.<a href="./src/cloudflare/resources/ddos_protection/advanced_tcp_protection/prefixes/prefixes.py">bulk_create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/ddos_protection/advanced_tcp_protection/prefix_bulk_create_params.py">params</a>) -> <a href="./src/cloudflare/types/ddos_protection/advanced_tcp_protection/prefix_bulk_create_response.py">SyncSinglePage[PrefixBulkCreateResponse]</a></code>
- <code title="delete /accounts/{account_id}/magic/advanced_tcp_protection/configs/prefixes">client.ddos_protection.advanced_tcp_protection.prefixes.<a href="./src/cloudflare/resources/ddos_protection/advanced_tcp_protection/prefixes/prefixes.py">bulk_delete</a>(\*, account_id) -> <a href="./src/cloudflare/types/ddos_protection/advanced_tcp_protection/prefix_bulk_delete_response.py">PrefixBulkDeleteResponse</a></code>

#### Items

Types:

```python
from cloudflare.types.ddos_protection.advanced_tcp_protection.prefixes import (
    ItemDeleteResponse,
    ItemEditResponse,
    ItemGetResponse,
)
```

Methods:

- <code title="delete /accounts/{account_id}/magic/advanced_tcp_protection/configs/prefixes/{prefix_id}">client.ddos_protection.advanced_tcp_protection.prefixes.items.<a href="./src/cloudflare/resources/ddos_protection/advanced_tcp_protection/prefixes/items.py">delete</a>(prefix_id, \*, account_id) -> <a href="./src/cloudflare/types/ddos_protection/advanced_tcp_protection/prefixes/item_delete_response.py">ItemDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/magic/advanced_tcp_protection/configs/prefixes/{prefix_id}">client.ddos_protection.advanced_tcp_protection.prefixes.items.<a href="./src/cloudflare/resources/ddos_protection/advanced_tcp_protection/prefixes/items.py">edit</a>(prefix_id, \*, account_id, \*\*<a href="src/cloudflare/types/ddos_protection/advanced_tcp_protection/prefixes/item_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/ddos_protection/advanced_tcp_protection/prefixes/item_edit_response.py">Optional[ItemEditResponse]</a></code>
- <code title="get /accounts/{account_id}/magic/advanced_tcp_protection/configs/prefixes/{prefix_id}">client.ddos_protection.advanced_tcp_protection.prefixes.items.<a href="./src/cloudflare/resources/ddos_protection/advanced_tcp_protection/prefixes/items.py">get</a>(prefix_id, \*, account_id) -> <a href="./src/cloudflare/types/ddos_protection/advanced_tcp_protection/prefixes/item_get_response.py">Optional[ItemGetResponse]</a></code>

### SynProtection

#### Filters

Types:

```python
from cloudflare.types.ddos_protection.advanced_tcp_protection.syn_protection import (
    FilterCreateResponse,
    FilterListResponse,
    FilterBulkDeleteResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/filters">client.ddos_protection.advanced_tcp_protection.syn_protection.filters.<a href="./src/cloudflare/resources/ddos_protection/advanced_tcp_protection/syn_protection/filters/filters.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/ddos_protection/advanced_tcp_protection/syn_protection/filter_create_params.py">params</a>) -> <a href="./src/cloudflare/types/ddos_protection/advanced_tcp_protection/syn_protection/filter_create_response.py">Optional[FilterCreateResponse]</a></code>
- <code title="get /accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/filters">client.ddos_protection.advanced_tcp_protection.syn_protection.filters.<a href="./src/cloudflare/resources/ddos_protection/advanced_tcp_protection/syn_protection/filters/filters.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/ddos_protection/advanced_tcp_protection/syn_protection/filter_list_params.py">params</a>) -> <a href="./src/cloudflare/types/ddos_protection/advanced_tcp_protection/syn_protection/filter_list_response.py">SyncV4PagePaginationArray[FilterListResponse]</a></code>
- <code title="delete /accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/filters">client.ddos_protection.advanced_tcp_protection.syn_protection.filters.<a href="./src/cloudflare/resources/ddos_protection/advanced_tcp_protection/syn_protection/filters/filters.py">bulk_delete</a>(\*, account_id) -> <a href="./src/cloudflare/types/ddos_protection/advanced_tcp_protection/syn_protection/filter_bulk_delete_response.py">FilterBulkDeleteResponse</a></code>

##### Items

Types:

```python
from cloudflare.types.ddos_protection.advanced_tcp_protection.syn_protection.filters import (
    ItemDeleteResponse,
    ItemEditResponse,
    ItemGetResponse,
)
```

Methods:

- <code title="delete /accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/filters/{filter_id}">client.ddos_protection.advanced_tcp_protection.syn_protection.filters.items.<a href="./src/cloudflare/resources/ddos_protection/advanced_tcp_protection/syn_protection/filters/items.py">delete</a>(filter_id, \*, account_id) -> <a href="./src/cloudflare/types/ddos_protection/advanced_tcp_protection/syn_protection/filters/item_delete_response.py">ItemDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/filters/{filter_id}">client.ddos_protection.advanced_tcp_protection.syn_protection.filters.items.<a href="./src/cloudflare/resources/ddos_protection/advanced_tcp_protection/syn_protection/filters/items.py">edit</a>(filter_id, \*, account_id, \*\*<a href="src/cloudflare/types/ddos_protection/advanced_tcp_protection/syn_protection/filters/item_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/ddos_protection/advanced_tcp_protection/syn_protection/filters/item_edit_response.py">Optional[ItemEditResponse]</a></code>
- <code title="get /accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/filters/{filter_id}">client.ddos_protection.advanced_tcp_protection.syn_protection.filters.items.<a href="./src/cloudflare/resources/ddos_protection/advanced_tcp_protection/syn_protection/filters/items.py">get</a>(filter_id, \*, account_id) -> <a href="./src/cloudflare/types/ddos_protection/advanced_tcp_protection/syn_protection/filters/item_get_response.py">Optional[ItemGetResponse]</a></code>

#### Rules

Types:

```python
from cloudflare.types.ddos_protection.advanced_tcp_protection.syn_protection import (
    RuleCreateResponse,
    RuleListResponse,
    RuleBulkDeleteResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/rules">client.ddos_protection.advanced_tcp_protection.syn_protection.rules.<a href="./src/cloudflare/resources/ddos_protection/advanced_tcp_protection/syn_protection/rules/rules.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/ddos_protection/advanced_tcp_protection/syn_protection/rule_create_params.py">params</a>) -> <a href="./src/cloudflare/types/ddos_protection/advanced_tcp_protection/syn_protection/rule_create_response.py">Optional[RuleCreateResponse]</a></code>
- <code title="get /accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/rules">client.ddos_protection.advanced_tcp_protection.syn_protection.rules.<a href="./src/cloudflare/resources/ddos_protection/advanced_tcp_protection/syn_protection/rules/rules.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/ddos_protection/advanced_tcp_protection/syn_protection/rule_list_params.py">params</a>) -> <a href="./src/cloudflare/types/ddos_protection/advanced_tcp_protection/syn_protection/rule_list_response.py">SyncV4PagePaginationArray[RuleListResponse]</a></code>
- <code title="delete /accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/rules">client.ddos_protection.advanced_tcp_protection.syn_protection.rules.<a href="./src/cloudflare/resources/ddos_protection/advanced_tcp_protection/syn_protection/rules/rules.py">bulk_delete</a>(\*, account_id) -> <a href="./src/cloudflare/types/ddos_protection/advanced_tcp_protection/syn_protection/rule_bulk_delete_response.py">RuleBulkDeleteResponse</a></code>

##### Items

Types:

```python
from cloudflare.types.ddos_protection.advanced_tcp_protection.syn_protection.rules import (
    ItemDeleteResponse,
    ItemEditResponse,
    ItemGetResponse,
)
```

Methods:

- <code title="delete /accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/rules/{rule_id}">client.ddos_protection.advanced_tcp_protection.syn_protection.rules.items.<a href="./src/cloudflare/resources/ddos_protection/advanced_tcp_protection/syn_protection/rules/items.py">delete</a>(rule_id, \*, account_id) -> <a href="./src/cloudflare/types/ddos_protection/advanced_tcp_protection/syn_protection/rules/item_delete_response.py">ItemDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/rules/{rule_id}">client.ddos_protection.advanced_tcp_protection.syn_protection.rules.items.<a href="./src/cloudflare/resources/ddos_protection/advanced_tcp_protection/syn_protection/rules/items.py">edit</a>(rule_id, \*, account_id, \*\*<a href="src/cloudflare/types/ddos_protection/advanced_tcp_protection/syn_protection/rules/item_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/ddos_protection/advanced_tcp_protection/syn_protection/rules/item_edit_response.py">Optional[ItemEditResponse]</a></code>
- <code title="get /accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/rules/{rule_id}">client.ddos_protection.advanced_tcp_protection.syn_protection.rules.items.<a href="./src/cloudflare/resources/ddos_protection/advanced_tcp_protection/syn_protection/rules/items.py">get</a>(rule_id, \*, account_id) -> <a href="./src/cloudflare/types/ddos_protection/advanced_tcp_protection/syn_protection/rules/item_get_response.py">Optional[ItemGetResponse]</a></code>

### TCPFlowProtection

#### Filters

Types:

```python
from cloudflare.types.ddos_protection.advanced_tcp_protection.tcp_flow_protection import (
    FilterCreateResponse,
    FilterListResponse,
    FilterBulkDeleteResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/filters">client.ddos_protection.advanced_tcp_protection.tcp_flow_protection.filters.<a href="./src/cloudflare/resources/ddos_protection/advanced_tcp_protection/tcp_flow_protection/filters/filters.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/ddos_protection/advanced_tcp_protection/tcp_flow_protection/filter_create_params.py">params</a>) -> <a href="./src/cloudflare/types/ddos_protection/advanced_tcp_protection/tcp_flow_protection/filter_create_response.py">Optional[FilterCreateResponse]</a></code>
- <code title="get /accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/filters">client.ddos_protection.advanced_tcp_protection.tcp_flow_protection.filters.<a href="./src/cloudflare/resources/ddos_protection/advanced_tcp_protection/tcp_flow_protection/filters/filters.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/ddos_protection/advanced_tcp_protection/tcp_flow_protection/filter_list_params.py">params</a>) -> <a href="./src/cloudflare/types/ddos_protection/advanced_tcp_protection/tcp_flow_protection/filter_list_response.py">SyncV4PagePaginationArray[FilterListResponse]</a></code>
- <code title="delete /accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/filters">client.ddos_protection.advanced_tcp_protection.tcp_flow_protection.filters.<a href="./src/cloudflare/resources/ddos_protection/advanced_tcp_protection/tcp_flow_protection/filters/filters.py">bulk_delete</a>(\*, account_id) -> <a href="./src/cloudflare/types/ddos_protection/advanced_tcp_protection/tcp_flow_protection/filter_bulk_delete_response.py">FilterBulkDeleteResponse</a></code>

##### Items

Types:

```python
from cloudflare.types.ddos_protection.advanced_tcp_protection.tcp_flow_protection.filters import (
    ItemDeleteResponse,
    ItemEditResponse,
    ItemGetResponse,
)
```

Methods:

- <code title="delete /accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/filters/{filter_id}">client.ddos_protection.advanced_tcp_protection.tcp_flow_protection.filters.items.<a href="./src/cloudflare/resources/ddos_protection/advanced_tcp_protection/tcp_flow_protection/filters/items.py">delete</a>(filter_id, \*, account_id) -> <a href="./src/cloudflare/types/ddos_protection/advanced_tcp_protection/tcp_flow_protection/filters/item_delete_response.py">ItemDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/filters/{filter_id}">client.ddos_protection.advanced_tcp_protection.tcp_flow_protection.filters.items.<a href="./src/cloudflare/resources/ddos_protection/advanced_tcp_protection/tcp_flow_protection/filters/items.py">edit</a>(filter_id, \*, account_id, \*\*<a href="src/cloudflare/types/ddos_protection/advanced_tcp_protection/tcp_flow_protection/filters/item_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/ddos_protection/advanced_tcp_protection/tcp_flow_protection/filters/item_edit_response.py">Optional[ItemEditResponse]</a></code>
- <code title="get /accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/filters/{filter_id}">client.ddos_protection.advanced_tcp_protection.tcp_flow_protection.filters.items.<a href="./src/cloudflare/resources/ddos_protection/advanced_tcp_protection/tcp_flow_protection/filters/items.py">get</a>(filter_id, \*, account_id) -> <a href="./src/cloudflare/types/ddos_protection/advanced_tcp_protection/tcp_flow_protection/filters/item_get_response.py">Optional[ItemGetResponse]</a></code>

#### Rules

Types:

```python
from cloudflare.types.ddos_protection.advanced_tcp_protection.tcp_flow_protection import (
    RuleCreateResponse,
    RuleListResponse,
    RuleBulkDeleteResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/rules">client.ddos_protection.advanced_tcp_protection.tcp_flow_protection.rules.<a href="./src/cloudflare/resources/ddos_protection/advanced_tcp_protection/tcp_flow_protection/rules/rules.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/ddos_protection/advanced_tcp_protection/tcp_flow_protection/rule_create_params.py">params</a>) -> <a href="./src/cloudflare/types/ddos_protection/advanced_tcp_protection/tcp_flow_protection/rule_create_response.py">Optional[RuleCreateResponse]</a></code>
- <code title="get /accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/rules">client.ddos_protection.advanced_tcp_protection.tcp_flow_protection.rules.<a href="./src/cloudflare/resources/ddos_protection/advanced_tcp_protection/tcp_flow_protection/rules/rules.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/ddos_protection/advanced_tcp_protection/tcp_flow_protection/rule_list_params.py">params</a>) -> <a href="./src/cloudflare/types/ddos_protection/advanced_tcp_protection/tcp_flow_protection/rule_list_response.py">SyncV4PagePaginationArray[RuleListResponse]</a></code>
- <code title="delete /accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/rules">client.ddos_protection.advanced_tcp_protection.tcp_flow_protection.rules.<a href="./src/cloudflare/resources/ddos_protection/advanced_tcp_protection/tcp_flow_protection/rules/rules.py">bulk_delete</a>(\*, account_id) -> <a href="./src/cloudflare/types/ddos_protection/advanced_tcp_protection/tcp_flow_protection/rule_bulk_delete_response.py">RuleBulkDeleteResponse</a></code>

##### Items

Types:

```python
from cloudflare.types.ddos_protection.advanced_tcp_protection.tcp_flow_protection.rules import (
    ItemDeleteResponse,
    ItemEditResponse,
    ItemGetResponse,
)
```

Methods:

- <code title="delete /accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/rules/{rule_id}">client.ddos_protection.advanced_tcp_protection.tcp_flow_protection.rules.items.<a href="./src/cloudflare/resources/ddos_protection/advanced_tcp_protection/tcp_flow_protection/rules/items.py">delete</a>(rule_id, \*, account_id) -> <a href="./src/cloudflare/types/ddos_protection/advanced_tcp_protection/tcp_flow_protection/rules/item_delete_response.py">ItemDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/rules/{rule_id}">client.ddos_protection.advanced_tcp_protection.tcp_flow_protection.rules.items.<a href="./src/cloudflare/resources/ddos_protection/advanced_tcp_protection/tcp_flow_protection/rules/items.py">edit</a>(rule_id, \*, account_id, \*\*<a href="src/cloudflare/types/ddos_protection/advanced_tcp_protection/tcp_flow_protection/rules/item_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/ddos_protection/advanced_tcp_protection/tcp_flow_protection/rules/item_edit_response.py">Optional[ItemEditResponse]</a></code>
- <code title="get /accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/rules/{rule_id}">client.ddos_protection.advanced_tcp_protection.tcp_flow_protection.rules.items.<a href="./src/cloudflare/resources/ddos_protection/advanced_tcp_protection/tcp_flow_protection/rules/items.py">get</a>(rule_id, \*, account_id) -> <a href="./src/cloudflare/types/ddos_protection/advanced_tcp_protection/tcp_flow_protection/rules/item_get_response.py">Optional[ItemGetResponse]</a></code>

### Status

Types:

```python
from cloudflare.types.ddos_protection.advanced_tcp_protection import (
    StatusEditResponse,
    StatusGetResponse,
)
```

Methods:

- <code title="patch /accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_protection_status">client.ddos_protection.advanced_tcp_protection.status.<a href="./src/cloudflare/resources/ddos_protection/advanced_tcp_protection/status.py">edit</a>(\*, account_id, \*\*<a href="src/cloudflare/types/ddos_protection/advanced_tcp_protection/status_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/ddos_protection/advanced_tcp_protection/status_edit_response.py">Optional[StatusEditResponse]</a></code>
- <code title="get /accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_protection_status">client.ddos_protection.advanced_tcp_protection.status.<a href="./src/cloudflare/resources/ddos_protection/advanced_tcp_protection/status.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/ddos_protection/advanced_tcp_protection/status_get_response.py">Optional[StatusGetResponse]</a></code>
