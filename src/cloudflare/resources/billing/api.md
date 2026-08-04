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
from cloudflare.types.billing import (
    UsageGetResponse,
    UsageGetAccountUsageInfoV1Response,
    UsageGetAccountUsageV1Response,
    UsageGetAccountUsageV2Response,
    UsagePaygoResponse,
    UsagePaygoInfoResponse,
)
```

Methods:

- <code title="get /accounts/{account_id}/billable/usage">client.billing.usage.<a href="./src/cloudflare/resources/billing/usage.py">get</a>(\*, account_id, \*\*<a href="src/cloudflare/types/billing/usage_get_params.py">params</a>) -> <a href="./src/cloudflare/types/billing/usage_get_response.py">UsageGetResponse</a></code>
- <code title="get /accounts/{account_id}/billable-usage/info">client.billing.usage.<a href="./src/cloudflare/resources/billing/usage.py">get_account_usage_info_v1</a>(\*, account_id) -> <a href="./src/cloudflare/types/billing/usage_get_account_usage_info_v1_response.py">UsageGetAccountUsageInfoV1Response</a></code>
- <code title="get /accounts/{account_id}/billable-usage">client.billing.usage.<a href="./src/cloudflare/resources/billing/usage.py">get_account_usage_v1</a>(\*, account_id, \*\*<a href="src/cloudflare/types/billing/usage_get_account_usage_v1_params.py">params</a>) -> <a href="./src/cloudflare/types/billing/usage_get_account_usage_v1_response.py">UsageGetAccountUsageV1Response</a></code>
- <code title="get /accounts/{account_id}/billable/usage">client.billing.usage.<a href="./src/cloudflare/resources/billing/usage.py">get_account_usage_v2</a>(\*, account_id, \*\*<a href="src/cloudflare/types/billing/usage_get_account_usage_v2_params.py">params</a>) -> <a href="./src/cloudflare/types/billing/usage_get_account_usage_v2_response.py">UsageGetAccountUsageV2Response</a></code>
- <code title="get /accounts/{account_id}/billable-usage">client.billing.usage.<a href="./src/cloudflare/resources/billing/usage.py">paygo</a>(\*, account_id, \*\*<a href="src/cloudflare/types/billing/usage_paygo_params.py">params</a>) -> <a href="./src/cloudflare/types/billing/usage_paygo_response.py">UsagePaygoResponse</a></code>
- <code title="get /accounts/{account_id}/billable-usage/info">client.billing.usage.<a href="./src/cloudflare/resources/billing/usage.py">paygo_info</a>(\*, account_id) -> <a href="./src/cloudflare/types/billing/usage_paygo_info_response.py">UsagePaygoInfoResponse</a></code>
