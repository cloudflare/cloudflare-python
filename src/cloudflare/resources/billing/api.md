# Billing

Types:

```python
from cloudflare.types.billing import BillingAddressValidationResponse
```

Methods:

- <code title="post /billing/address-validation">client.billing.<a href="./src/cloudflare/resources/billing/billing.py">address_validation</a>(\*\*<a href="src/cloudflare/types/billing/billing_address_validation_params.py">params</a>) -> <a href="./src/cloudflare/types/billing/billing_address_validation_response.py">BillingAddressValidationResponse</a></code>

## SpendPolicies

Types:

```python
from cloudflare.types.billing import (
    SpendPolicyCreateResponse,
    SpendPolicyUpdateResponse,
    SpendPolicyListResponse,
    SpendPolicyDeleteResponse,
    SpendPolicyGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/billing/spend-policies">client.billing.spend_policies.<a href="./src/cloudflare/resources/billing/spend_policies/spend_policies.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/billing/spend_policy_create_params.py">params</a>) -> <a href="./src/cloudflare/types/billing/spend_policy_create_response.py">SpendPolicyCreateResponse</a></code>
- <code title="put /accounts/{account_id}/billing/spend-policies/{policy_id}">client.billing.spend_policies.<a href="./src/cloudflare/resources/billing/spend_policies/spend_policies.py">update</a>(policy_id, \*, account_id, \*\*<a href="src/cloudflare/types/billing/spend_policy_update_params.py">params</a>) -> <a href="./src/cloudflare/types/billing/spend_policy_update_response.py">SpendPolicyUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/billing/spend-policies">client.billing.spend_policies.<a href="./src/cloudflare/resources/billing/spend_policies/spend_policies.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/billing/spend_policy_list_response.py">SyncSinglePage[SpendPolicyListResponse]</a></code>
- <code title="delete /accounts/{account_id}/billing/spend-policies/{policy_id}">client.billing.spend_policies.<a href="./src/cloudflare/resources/billing/spend_policies/spend_policies.py">delete</a>(policy_id, \*, account_id) -> <a href="./src/cloudflare/types/billing/spend_policy_delete_response.py">SpendPolicyDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/billing/spend-policies/{policy_id}">client.billing.spend_policies.<a href="./src/cloudflare/resources/billing/spend_policies/spend_policies.py">get</a>(policy_id, \*, account_id) -> <a href="./src/cloudflare/types/billing/spend_policy_get_response.py">SpendPolicyGetResponse</a></code>

### Audit

Types:

```python
from cloudflare.types.billing.spend_policies import AuditListResponse
```

Methods:

- <code title="get /accounts/{account_id}/billing/spend-policies/{policy_id}/audit">client.billing.spend_policies.audit.<a href="./src/cloudflare/resources/billing/spend_policies/audit.py">list</a>(policy_id, \*, account_id, \*\*<a href="src/cloudflare/types/billing/spend_policies/audit_list_params.py">params</a>) -> <a href="./src/cloudflare/types/billing/spend_policies/audit_list_response.py">SyncSinglePage[AuditListResponse]</a></code>

### Activity

Types:

```python
from cloudflare.types.billing.spend_policies import ActivityListResponse
```

Methods:

- <code title="get /accounts/{account_id}/billing/spend-policies/activity">client.billing.spend_policies.activity.<a href="./src/cloudflare/resources/billing/spend_policies/activity.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/billing/spend_policies/activity_list_params.py">params</a>) -> <a href="./src/cloudflare/types/billing/spend_policies/activity_list_response.py">SyncCursorPaginationAfter[ActivityListResponse]</a></code>

## Profiles

Types:

```python
from cloudflare.types.billing import (
    ProfileCreateResponse,
    ProfileUpdateResponse,
    ProfileGetResponse,
    ProfileUpdateBillingEmailResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/billing/profile">client.billing.profiles.<a href="./src/cloudflare/resources/billing/profiles/profiles.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/billing/profile_create_params.py">params</a>) -> <a href="./src/cloudflare/types/billing/profile_create_response.py">ProfileCreateResponse</a></code>
- <code title="put /accounts/{account_id}/billing/profile">client.billing.profiles.<a href="./src/cloudflare/resources/billing/profiles/profiles.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/billing/profile_update_params.py">params</a>) -> <a href="./src/cloudflare/types/billing/profile_update_response.py">ProfileUpdateResponse</a></code>
- <code title="delete /accounts/{account_id}/billing/profile">client.billing.profiles.<a href="./src/cloudflare/resources/billing/profiles/profiles.py">delete</a>(\*, account_id) -> None</code>
- <code title="get /accounts/{account_id}/billing/profile">client.billing.profiles.<a href="./src/cloudflare/resources/billing/profiles/profiles.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/billing/profile_get_response.py">ProfileGetResponse</a></code>
- <code title="patch /accounts/{account_id}/billing/profile">client.billing.profiles.<a href="./src/cloudflare/resources/billing/profiles/profiles.py">update_billing_email</a>(\*, account_id, \*\*<a href="src/cloudflare/types/billing/profile_update_billing_email_params.py">params</a>) -> <a href="./src/cloudflare/types/billing/profile_update_billing_email_response.py">ProfileUpdateBillingEmailResponse</a></code>

### PaymentMethod

Types:

```python
from cloudflare.types.billing.profiles import PaymentMethodCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/billing/profile/payment-method">client.billing.profiles.payment_method.<a href="./src/cloudflare/resources/billing/profiles/payment_method.py">create</a>(\*, account_id) -> <a href="./src/cloudflare/types/billing/profiles/payment_method_create_response.py">PaymentMethodCreateResponse</a></code>

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

## Credits

Types:

```python
from cloudflare.types.billing import CreditGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/billing/credits">client.billing.credits.<a href="./src/cloudflare/resources/billing/credits.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/billing/credit_get_response.py">CreditGetResponse</a></code>

## History

Types:

```python
from cloudflare.types.billing import HistoryListResponse
```

Methods:

- <code title="get /accounts/{account_id}/billing/history">client.billing.history.<a href="./src/cloudflare/resources/billing/history.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/billing/history_list_params.py">params</a>) -> <a href="./src/cloudflare/types/billing/history_list_response.py">SyncV4PagePaginationArray[HistoryListResponse]</a></code>

## BadDebt

Types:

```python
from cloudflare.types.billing import BadDebtGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/billing/bad-debt">client.billing.bad_debt.<a href="./src/cloudflare/resources/billing/bad_debt.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/billing/bad_debt_get_response.py">BadDebtGetResponse</a></code>

## UnpaidInvoice

Types:

```python
from cloudflare.types.billing import UnpaidInvoiceGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/billing/unpaid-invoice">client.billing.unpaid_invoice.<a href="./src/cloudflare/resources/billing/unpaid_invoice.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/billing/unpaid_invoice_get_response.py">UnpaidInvoiceGetResponse</a></code>

## RatePlans

Types:

```python
from cloudflare.types.billing import RatePlanGetResponse
```

Methods:

- <code title="get /billing/rate_plans/{public_key}">client.billing.rate_plans.<a href="./src/cloudflare/resources/billing/rate_plans.py">get</a>(public_key) -> <a href="./src/cloudflare/types/billing/rate_plan_get_response.py">RatePlanGetResponse</a></code>
