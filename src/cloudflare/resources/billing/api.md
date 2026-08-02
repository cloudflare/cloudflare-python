# Billing

## Profiles

Types:

```python
from cloudflare.types.billing import ProfileGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/billing/profile">client.billing.profiles.<a href="./src/cloudflare/resources/billing/profiles.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/billing/profile_get_response.py">ProfileGetResponse</a></code>

## Usage

Types:

```python
from cloudflare.types.billing import UsageGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/billable/usage">client.billing.usage.<a href="./src/cloudflare/resources/billing/usage.py">get</a>(\*, account_id, \*\*<a href="src/cloudflare/types/billing/usage_get_params.py">params</a>) -> <a href="./src/cloudflare/types/billing/usage_get_response.py">UsageGetResponse</a></code>
