# Fraud

Types:

```python
from cloudflare.types.fraud import FraudSettings
```

Methods:

- <code title="put /zones/{zone_id}/fraud_detection/settings">client.fraud.<a href="./src/cloudflare/resources/fraud/fraud.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/fraud/fraud_update_params.py">params</a>) -> <a href="./src/cloudflare/types/fraud/fraud_settings.py">Optional[FraudSettings]</a></code>
- <code title="get /zones/{zone_id}/fraud_detection/settings">client.fraud.<a href="./src/cloudflare/resources/fraud/fraud.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/fraud/fraud_settings.py">Optional[FraudSettings]</a></code>
