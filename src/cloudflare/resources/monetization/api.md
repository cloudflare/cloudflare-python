# Monetization

Types:

```python
from cloudflare.types.monetization import (
    MonetizationAccountEligibilityCheckInput,
    MonetizationAccountEligibilityCheckResponse,
    MonetizationEligibilityResponse,
    MonetizationEligibilityResult,
    MonetizationZoneEligibilityCheckResponse,
)
```

## Rules

Types:

```python
from cloudflare.types.monetization import (
    MonetizationRule,
    MonetizationRuleCollection,
    MonetizationRuleInput,
    MonetizationRuleInputFixedPrice,
    MonetizationRuleInputOriginControlled,
    MonetizationRulePatch,
    MonetizationRulesetInput,
)
```

Methods:

- <code title="put /zones/{zone_id}/monetization/rules">client.monetization.rules.<a href="./src/cloudflare/resources/monetization/rules.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/monetization/rule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/monetization/monetization_rule_collection.py">MonetizationRuleCollection</a></code>
- <code title="delete /zones/{zone_id}/monetization/rules">client.monetization.rules.<a href="./src/cloudflare/resources/monetization/rules.py">delete</a>(\*, zone_id) -> <a href="./src/cloudflare/types/monetization/monetization_rule_collection.py">MonetizationRuleCollection</a></code>
- <code title="delete /zones/{zone_id}/monetization/rules/{rule_id}">client.monetization.rules.<a href="./src/cloudflare/resources/monetization/rules.py">delete_rule</a>(rule_id, \*, zone_id) -> <a href="./src/cloudflare/types/monetization/monetization_rule_collection.py">MonetizationRuleCollection</a></code>
- <code title="patch /zones/{zone_id}/monetization/rules/{rule_id}">client.monetization.rules.<a href="./src/cloudflare/resources/monetization/rules.py">edit_rule</a>(rule_id, \*, zone_id, \*\*<a href="src/cloudflare/types/monetization/rule_edit_rule_params.py">params</a>) -> <a href="./src/cloudflare/types/monetization/monetization_rule_collection.py">MonetizationRuleCollection</a></code>
- <code title="get /zones/{zone_id}/monetization/rules">client.monetization.rules.<a href="./src/cloudflare/resources/monetization/rules.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/monetization/monetization_rule_collection.py">MonetizationRuleCollection</a></code>
- <code title="get /zones/{zone_id}/monetization/rules/{rule_id}">client.monetization.rules.<a href="./src/cloudflare/resources/monetization/rules.py">get_rule</a>(rule_id, \*, zone_id) -> <a href="./src/cloudflare/types/monetization/monetization_rule.py">MonetizationRule</a></code>
