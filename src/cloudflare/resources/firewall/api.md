# Firewall

## Lockdowns

Types:

```python
from cloudflare.types.firewall import (
    Configuration,
    Lockdown,
    LockdownCIDRConfiguration,
    LockdownIPConfiguration,
    LockdownURL,
    LockdownDeleteResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/firewall/lockdowns">client.firewall.lockdowns.<a href="./src/cloudflare/resources/firewall/lockdowns.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/firewall/lockdown_create_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/lockdown.py">Lockdown</a></code>
- <code title="put /zones/{zone_id}/firewall/lockdowns/{lock_downs_id}">client.firewall.lockdowns.<a href="./src/cloudflare/resources/firewall/lockdowns.py">update</a>(lock_downs_id, \*, zone_id, \*\*<a href="src/cloudflare/types/firewall/lockdown_update_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/lockdown.py">Lockdown</a></code>
- <code title="get /zones/{zone_id}/firewall/lockdowns">client.firewall.lockdowns.<a href="./src/cloudflare/resources/firewall/lockdowns.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/firewall/lockdown_list_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/lockdown.py">SyncV4PagePaginationArray[Lockdown]</a></code>
- <code title="delete /zones/{zone_id}/firewall/lockdowns/{lock_downs_id}">client.firewall.lockdowns.<a href="./src/cloudflare/resources/firewall/lockdowns.py">delete</a>(lock_downs_id, \*, zone_id) -> <a href="./src/cloudflare/types/firewall/lockdown_delete_response.py">Optional[LockdownDeleteResponse]</a></code>
- <code title="get /zones/{zone_id}/firewall/lockdowns/{lock_downs_id}">client.firewall.lockdowns.<a href="./src/cloudflare/resources/firewall/lockdowns.py">get</a>(lock_downs_id, \*, zone_id) -> <a href="./src/cloudflare/types/firewall/lockdown.py">Lockdown</a></code>

## Rules

Types:

```python
from cloudflare.types.firewall import DeletedFilter, FirewallRule, Product
```

Methods:

- <code title="post /zones/{zone_id}/firewall/rules">client.firewall.rules.<a href="./src/cloudflare/resources/firewall/rules.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/firewall/rule_create_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/firewall_rule.py">SyncSinglePage[FirewallRule]</a></code>
- <code title="put /zones/{zone_id}/firewall/rules/{rule_id}">client.firewall.rules.<a href="./src/cloudflare/resources/firewall/rules.py">update</a>(rule_id, \*, zone_id, \*\*<a href="src/cloudflare/types/firewall/rule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/firewall_rule.py">FirewallRule</a></code>
- <code title="get /zones/{zone_id}/firewall/rules">client.firewall.rules.<a href="./src/cloudflare/resources/firewall/rules.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/firewall/rule_list_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/firewall_rule.py">SyncV4PagePaginationArray[FirewallRule]</a></code>
- <code title="delete /zones/{zone_id}/firewall/rules/{rule_id}">client.firewall.rules.<a href="./src/cloudflare/resources/firewall/rules.py">delete</a>(rule_id, \*, zone_id) -> <a href="./src/cloudflare/types/firewall/firewall_rule.py">FirewallRule</a></code>
- <code title="delete /zones/{zone_id}/firewall/rules">client.firewall.rules.<a href="./src/cloudflare/resources/firewall/rules.py">bulk_delete</a>(\*, zone_id) -> <a href="./src/cloudflare/types/firewall/firewall_rule.py">SyncSinglePage[FirewallRule]</a></code>
- <code title="patch /zones/{zone_id}/firewall/rules">client.firewall.rules.<a href="./src/cloudflare/resources/firewall/rules.py">bulk_edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/firewall/rule_bulk_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/firewall_rule.py">SyncSinglePage[FirewallRule]</a></code>
- <code title="put /zones/{zone_id}/firewall/rules">client.firewall.rules.<a href="./src/cloudflare/resources/firewall/rules.py">bulk_update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/firewall/rule_bulk_update_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/firewall_rule.py">SyncSinglePage[FirewallRule]</a></code>
- <code title="patch /zones/{zone_id}/firewall/rules/{rule_id}">client.firewall.rules.<a href="./src/cloudflare/resources/firewall/rules.py">edit</a>(rule_id, \*, zone_id) -> <a href="./src/cloudflare/types/firewall/firewall_rule.py">SyncSinglePage[FirewallRule]</a></code>
- <code title="get /zones/{zone_id}/firewall/rules/{rule_id}">client.firewall.rules.<a href="./src/cloudflare/resources/firewall/rules.py">get</a>(rule_id, \*, zone_id) -> <a href="./src/cloudflare/types/firewall/firewall_rule.py">FirewallRule</a></code>

## AccessRules

Types:

```python
from cloudflare.types.firewall import (
    AccessRuleCIDRConfiguration,
    AccessRuleIPConfiguration,
    ASNConfiguration,
    CountryConfiguration,
    IPV6Configuration,
    AccessRuleCreateResponse,
    AccessRuleListResponse,
    AccessRuleDeleteResponse,
    AccessRuleEditResponse,
    AccessRuleGetResponse,
)
```

Methods:

- <code title="post /{accounts_or_zones}/{account_or_zone_id}/firewall/access_rules/rules">client.firewall.access_rules.<a href="./src/cloudflare/resources/firewall/access_rules.py">create</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/firewall/access_rule_create_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/access_rule_create_response.py">AccessRuleCreateResponse</a></code>
- <code title="get /{accounts_or_zones}/{account_or_zone_id}/firewall/access_rules/rules">client.firewall.access_rules.<a href="./src/cloudflare/resources/firewall/access_rules.py">list</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/firewall/access_rule_list_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/access_rule_list_response.py">SyncV4PagePaginationArray[AccessRuleListResponse]</a></code>
- <code title="delete /{accounts_or_zones}/{account_or_zone_id}/firewall/access_rules/rules/{rule_id}">client.firewall.access_rules.<a href="./src/cloudflare/resources/firewall/access_rules.py">delete</a>(rule_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/firewall/access_rule_delete_response.py">Optional[AccessRuleDeleteResponse]</a></code>
- <code title="patch /{accounts_or_zones}/{account_or_zone_id}/firewall/access_rules/rules/{rule_id}">client.firewall.access_rules.<a href="./src/cloudflare/resources/firewall/access_rules.py">edit</a>(rule_id, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/firewall/access_rule_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/access_rule_edit_response.py">AccessRuleEditResponse</a></code>
- <code title="get /{accounts_or_zones}/{account_or_zone_id}/firewall/access_rules/rules/{rule_id}">client.firewall.access_rules.<a href="./src/cloudflare/resources/firewall/access_rules.py">get</a>(rule_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/firewall/access_rule_get_response.py">AccessRuleGetResponse</a></code>

## UARules

Types:

```python
from cloudflare.types.firewall import (
    UARuleCreateResponse,
    UARuleUpdateResponse,
    UARuleListResponse,
    UARuleDeleteResponse,
    UARuleGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/firewall/ua_rules">client.firewall.ua_rules.<a href="./src/cloudflare/resources/firewall/ua_rules.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/firewall/ua_rule_create_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/ua_rule_create_response.py">UARuleCreateResponse</a></code>
- <code title="put /zones/{zone_id}/firewall/ua_rules/{ua_rule_id}">client.firewall.ua_rules.<a href="./src/cloudflare/resources/firewall/ua_rules.py">update</a>(ua_rule_id, \*, zone_id, \*\*<a href="src/cloudflare/types/firewall/ua_rule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/ua_rule_update_response.py">UARuleUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/firewall/ua_rules">client.firewall.ua_rules.<a href="./src/cloudflare/resources/firewall/ua_rules.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/firewall/ua_rule_list_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/ua_rule_list_response.py">SyncV4PagePaginationArray[UARuleListResponse]</a></code>
- <code title="delete /zones/{zone_id}/firewall/ua_rules/{ua_rule_id}">client.firewall.ua_rules.<a href="./src/cloudflare/resources/firewall/ua_rules.py">delete</a>(ua_rule_id, \*, zone_id) -> <a href="./src/cloudflare/types/firewall/ua_rule_delete_response.py">UARuleDeleteResponse</a></code>
- <code title="get /zones/{zone_id}/firewall/ua_rules/{ua_rule_id}">client.firewall.ua_rules.<a href="./src/cloudflare/resources/firewall/ua_rules.py">get</a>(ua_rule_id, \*, zone_id) -> <a href="./src/cloudflare/types/firewall/ua_rule_get_response.py">UARuleGetResponse</a></code>

## WAF

### Overrides

Types:

```python
from cloudflare.types.firewall.waf import (
    Override,
    OverrideURL,
    RewriteAction,
    WAFRule,
    OverrideDeleteResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/firewall/waf/overrides">client.firewall.waf.overrides.<a href="./src/cloudflare/resources/firewall/waf/overrides.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/firewall/waf/override_create_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/waf/override.py">Override</a></code>
- <code title="put /zones/{zone_id}/firewall/waf/overrides/{overrides_id}">client.firewall.waf.overrides.<a href="./src/cloudflare/resources/firewall/waf/overrides.py">update</a>(overrides_id, \*, zone_id, \*\*<a href="src/cloudflare/types/firewall/waf/override_update_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/waf/override.py">Override</a></code>
- <code title="get /zones/{zone_id}/firewall/waf/overrides">client.firewall.waf.overrides.<a href="./src/cloudflare/resources/firewall/waf/overrides.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/firewall/waf/override_list_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/waf/override.py">SyncV4PagePaginationArray[Override]</a></code>
- <code title="delete /zones/{zone_id}/firewall/waf/overrides/{overrides_id}">client.firewall.waf.overrides.<a href="./src/cloudflare/resources/firewall/waf/overrides.py">delete</a>(overrides_id, \*, zone_id) -> <a href="./src/cloudflare/types/firewall/waf/override_delete_response.py">Optional[OverrideDeleteResponse]</a></code>
- <code title="get /zones/{zone_id}/firewall/waf/overrides/{overrides_id}">client.firewall.waf.overrides.<a href="./src/cloudflare/resources/firewall/waf/overrides.py">get</a>(overrides_id, \*, zone_id) -> <a href="./src/cloudflare/types/firewall/waf/override.py">Override</a></code>

### Packages

Types:

```python
from cloudflare.types.firewall.waf import PackageGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/firewall/waf/packages">client.firewall.waf.packages.<a href="./src/cloudflare/resources/firewall/waf/packages/packages.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/firewall/waf/package_list_params.py">params</a>) -> SyncV4PagePaginationArray[object]</code>
- <code title="get /zones/{zone_id}/firewall/waf/packages/{package_id}">client.firewall.waf.packages.<a href="./src/cloudflare/resources/firewall/waf/packages/packages.py">get</a>(package_id, \*, zone_id) -> <a href="./src/cloudflare/types/firewall/waf/package_get_response.py">PackageGetResponse</a></code>

#### Groups

Types:

```python
from cloudflare.types.firewall.waf.packages import Group, GroupEditResponse, GroupGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/firewall/waf/packages/{package_id}/groups">client.firewall.waf.packages.groups.<a href="./src/cloudflare/resources/firewall/waf/packages/groups.py">list</a>(package_id, \*, zone_id, \*\*<a href="src/cloudflare/types/firewall/waf/packages/group_list_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/waf/packages/group.py">SyncV4PagePaginationArray[Group]</a></code>
- <code title="patch /zones/{zone_id}/firewall/waf/packages/{package_id}/groups/{group_id}">client.firewall.waf.packages.groups.<a href="./src/cloudflare/resources/firewall/waf/packages/groups.py">edit</a>(group_id, \*, zone_id, package_id, \*\*<a href="src/cloudflare/types/firewall/waf/packages/group_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/waf/packages/group_edit_response.py">GroupEditResponse</a></code>
- <code title="get /zones/{zone_id}/firewall/waf/packages/{package_id}/groups/{group_id}">client.firewall.waf.packages.groups.<a href="./src/cloudflare/resources/firewall/waf/packages/groups.py">get</a>(group_id, \*, zone_id, package_id) -> <a href="./src/cloudflare/types/firewall/waf/packages/group_get_response.py">GroupGetResponse</a></code>

#### Rules

Types:

```python
from cloudflare.types.firewall.waf.packages import (
    AllowedModesAnomaly,
    WAFRuleGroup,
    RuleListResponse,
    RuleEditResponse,
    RuleGetResponse,
)
```

Methods:

- <code title="get /zones/{zone_id}/firewall/waf/packages/{package_id}/rules">client.firewall.waf.packages.rules.<a href="./src/cloudflare/resources/firewall/waf/packages/rules.py">list</a>(package_id, \*, zone_id, \*\*<a href="src/cloudflare/types/firewall/waf/packages/rule_list_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/waf/packages/rule_list_response.py">SyncV4PagePaginationArray[RuleListResponse]</a></code>
- <code title="patch /zones/{zone_id}/firewall/waf/packages/{package_id}/rules/{rule_id}">client.firewall.waf.packages.rules.<a href="./src/cloudflare/resources/firewall/waf/packages/rules.py">edit</a>(rule_id, \*, zone_id, package_id, \*\*<a href="src/cloudflare/types/firewall/waf/packages/rule_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/firewall/waf/packages/rule_edit_response.py">RuleEditResponse</a></code>
- <code title="get /zones/{zone_id}/firewall/waf/packages/{package_id}/rules/{rule_id}">client.firewall.waf.packages.rules.<a href="./src/cloudflare/resources/firewall/waf/packages/rules.py">get</a>(rule_id, \*, zone_id, package_id) -> <a href="./src/cloudflare/types/firewall/waf/packages/rule_get_response.py">RuleGetResponse</a></code>
