# RUM

## SiteInfo

Types:

```python
from cloudflare.types.rum import Site, SiteInfoDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/rum/site_info">client.rum.site_info.<a href="./src/cloudflare/resources/rum/site_info.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/rum/site_info_create_params.py">params</a>) -> <a href="./src/cloudflare/types/rum/site.py">Optional[Site]</a></code>
- <code title="put /accounts/{account_id}/rum/site_info/{site_id}">client.rum.site_info.<a href="./src/cloudflare/resources/rum/site_info.py">update</a>(site_id, \*, account_id, \*\*<a href="src/cloudflare/types/rum/site_info_update_params.py">params</a>) -> <a href="./src/cloudflare/types/rum/site.py">Optional[Site]</a></code>
- <code title="get /accounts/{account_id}/rum/site_info/list">client.rum.site_info.<a href="./src/cloudflare/resources/rum/site_info.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/rum/site_info_list_params.py">params</a>) -> <a href="./src/cloudflare/types/rum/site.py">SyncV4PagePaginationArray[Site]</a></code>
- <code title="delete /accounts/{account_id}/rum/site_info/{site_id}">client.rum.site_info.<a href="./src/cloudflare/resources/rum/site_info.py">delete</a>(site_id, \*, account_id) -> <a href="./src/cloudflare/types/rum/site_info_delete_response.py">Optional[SiteInfoDeleteResponse]</a></code>
- <code title="get /accounts/{account_id}/rum/site_info/{site_id}">client.rum.site_info.<a href="./src/cloudflare/resources/rum/site_info.py">get</a>(site_id, \*, account_id) -> <a href="./src/cloudflare/types/rum/site.py">Optional[Site]</a></code>

## Rules

Types:

```python
from cloudflare.types.rum import (
    RUMRule,
    RuleListResponse,
    RuleDeleteResponse,
    RuleBulkCreateResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/rum/v2/{ruleset_id}/rule">client.rum.rules.<a href="./src/cloudflare/resources/rum/rules.py">create</a>(ruleset_id, \*, account_id, \*\*<a href="src/cloudflare/types/rum/rule_create_params.py">params</a>) -> <a href="./src/cloudflare/types/rum/rum_rule.py">Optional[RUMRule]</a></code>
- <code title="put /accounts/{account_id}/rum/v2/{ruleset_id}/rule/{rule_id}">client.rum.rules.<a href="./src/cloudflare/resources/rum/rules.py">update</a>(rule_id, \*, account_id, ruleset_id, \*\*<a href="src/cloudflare/types/rum/rule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/rum/rum_rule.py">Optional[RUMRule]</a></code>
- <code title="get /accounts/{account_id}/rum/v2/{ruleset_id}/rules">client.rum.rules.<a href="./src/cloudflare/resources/rum/rules.py">list</a>(ruleset_id, \*, account_id) -> <a href="./src/cloudflare/types/rum/rule_list_response.py">Optional[RuleListResponse]</a></code>
- <code title="delete /accounts/{account_id}/rum/v2/{ruleset_id}/rule/{rule_id}">client.rum.rules.<a href="./src/cloudflare/resources/rum/rules.py">delete</a>(rule_id, \*, account_id, ruleset_id) -> <a href="./src/cloudflare/types/rum/rule_delete_response.py">Optional[RuleDeleteResponse]</a></code>
- <code title="post /accounts/{account_id}/rum/v2/{ruleset_id}/rules">client.rum.rules.<a href="./src/cloudflare/resources/rum/rules.py">bulk_create</a>(ruleset_id, \*, account_id, \*\*<a href="src/cloudflare/types/rum/rule_bulk_create_params.py">params</a>) -> <a href="./src/cloudflare/types/rum/rule_bulk_create_response.py">Optional[RuleBulkCreateResponse]</a></code>
