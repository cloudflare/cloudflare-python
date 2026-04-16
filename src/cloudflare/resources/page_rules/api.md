# PageRules

Types:

```python
from cloudflare.types.page_rules import (
    PageRule,
    Target,
    PageRuleListResponse,
    PageRuleDeleteResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/pagerules">client.page_rules.<a href="./src/cloudflare/resources/page_rules/page_rules.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/page_rules/page_rule_create_params.py">params</a>) -> <a href="./src/cloudflare/types/page_rules/page_rule.py">Optional[PageRule]</a></code>
- <code title="put /zones/{zone_id}/pagerules/{pagerule_id}">client.page_rules.<a href="./src/cloudflare/resources/page_rules/page_rules.py">update</a>(pagerule_id, \*, zone_id, \*\*<a href="src/cloudflare/types/page_rules/page_rule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/page_rules/page_rule.py">Optional[PageRule]</a></code>
- <code title="get /zones/{zone_id}/pagerules">client.page_rules.<a href="./src/cloudflare/resources/page_rules/page_rules.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/page_rules/page_rule_list_params.py">params</a>) -> <a href="./src/cloudflare/types/page_rules/page_rule_list_response.py">Optional[PageRuleListResponse]</a></code>
- <code title="delete /zones/{zone_id}/pagerules/{pagerule_id}">client.page_rules.<a href="./src/cloudflare/resources/page_rules/page_rules.py">delete</a>(pagerule_id, \*, zone_id) -> <a href="./src/cloudflare/types/page_rules/page_rule_delete_response.py">Optional[PageRuleDeleteResponse]</a></code>
- <code title="patch /zones/{zone_id}/pagerules/{pagerule_id}">client.page_rules.<a href="./src/cloudflare/resources/page_rules/page_rules.py">edit</a>(pagerule_id, \*, zone_id, \*\*<a href="src/cloudflare/types/page_rules/page_rule_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/page_rules/page_rule.py">Optional[PageRule]</a></code>
- <code title="get /zones/{zone_id}/pagerules/{pagerule_id}">client.page_rules.<a href="./src/cloudflare/resources/page_rules/page_rules.py">get</a>(pagerule_id, \*, zone_id) -> <a href="./src/cloudflare/types/page_rules/page_rule.py">Optional[PageRule]</a></code>
