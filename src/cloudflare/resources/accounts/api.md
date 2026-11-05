# Accounts

Types:

```python
from cloudflare.types.accounts import Account, AccountDeleteResponse
```

Methods:

- <code title="post /accounts">client.accounts.<a href="./src/cloudflare/resources/accounts/accounts.py">create</a>(\*\*<a href="src/cloudflare/types/accounts/account_create_params.py">params</a>) -> <a href="./src/cloudflare/types/accounts/account.py">Optional[Account]</a></code>
- <code title="put /accounts/{account_id}">client.accounts.<a href="./src/cloudflare/resources/accounts/accounts.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/accounts/account_update_params.py">params</a>) -> <a href="./src/cloudflare/types/accounts/account.py">Optional[Account]</a></code>
- <code title="get /accounts">client.accounts.<a href="./src/cloudflare/resources/accounts/accounts.py">list</a>(\*\*<a href="src/cloudflare/types/accounts/account_list_params.py">params</a>) -> <a href="./src/cloudflare/types/accounts/account.py">SyncV4PagePaginationArray[Account]</a></code>
- <code title="delete /accounts/{account_id}">client.accounts.<a href="./src/cloudflare/resources/accounts/accounts.py">delete</a>(\*, account_id) -> <a href="./src/cloudflare/types/accounts/account_delete_response.py">Optional[AccountDeleteResponse]</a></code>
- <code title="get /accounts/{account_id}">client.accounts.<a href="./src/cloudflare/resources/accounts/accounts.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/accounts/account.py">Optional[Account]</a></code>

## Members

Types:

```python
from cloudflare.types.accounts import Status, MemberDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/members">client.accounts.members.<a href="./src/cloudflare/resources/accounts/members.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/accounts/member_create_params.py">params</a>) -> <a href="./src/cloudflare/types/shared/member.py">Optional[Member]</a></code>
- <code title="put /accounts/{account_id}/members/{member_id}">client.accounts.members.<a href="./src/cloudflare/resources/accounts/members.py">update</a>(member_id, \*, account_id, \*\*<a href="src/cloudflare/types/accounts/member_update_params.py">params</a>) -> <a href="./src/cloudflare/types/shared/member.py">Optional[Member]</a></code>
- <code title="get /accounts/{account_id}/members">client.accounts.members.<a href="./src/cloudflare/resources/accounts/members.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/accounts/member_list_params.py">params</a>) -> <a href="./src/cloudflare/types/shared/member.py">SyncV4PagePaginationArray[Member]</a></code>
- <code title="delete /accounts/{account_id}/members/{member_id}">client.accounts.members.<a href="./src/cloudflare/resources/accounts/members.py">delete</a>(member_id, \*, account_id) -> <a href="./src/cloudflare/types/accounts/member_delete_response.py">Optional[MemberDeleteResponse]</a></code>
- <code title="get /accounts/{account_id}/members/{member_id}">client.accounts.members.<a href="./src/cloudflare/resources/accounts/members.py">get</a>(member_id, \*, account_id) -> <a href="./src/cloudflare/types/shared/member.py">Optional[Member]</a></code>

## Roles

Methods:

- <code title="get /accounts/{account_id}/roles">client.accounts.roles.<a href="./src/cloudflare/resources/accounts/roles.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/accounts/role_list_params.py">params</a>) -> <a href="./src/cloudflare/types/shared/role.py">SyncV4PagePaginationArray[Role]</a></code>
- <code title="get /accounts/{account_id}/roles/{role_id}">client.accounts.roles.<a href="./src/cloudflare/resources/accounts/roles.py">get</a>(role_id, \*, account_id) -> <a href="./src/cloudflare/types/shared/role.py">Optional[Role]</a></code>

## Subscriptions

Types:

```python
from cloudflare.types.accounts import (
    SubscriptionDeleteResponse,
    SubscriptionCancelDowngradeResponse,
)
```

Methods:

- <code title="post /{accounts_or_zones}/{account_or_zone_id}/subscriptions">client.accounts.subscriptions.<a href="./src/cloudflare/resources/accounts/subscriptions/subscriptions.py">create</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/accounts/subscription_create_params.py">params</a>) -> <a href="./src/cloudflare/types/shared/subscription.py">Subscription</a></code>
- <code title="put /accounts/{account_id}/subscriptions/{subscription_identifier}">client.accounts.subscriptions.<a href="./src/cloudflare/resources/accounts/subscriptions/subscriptions.py">update</a>(subscription_identifier, \*, account_id, \*\*<a href="src/cloudflare/types/accounts/subscription_update_params.py">params</a>) -> <a href="./src/cloudflare/types/shared/subscription.py">Subscription</a></code>
- <code title="delete /accounts/{account_id}/subscriptions/{subscription_identifier}">client.accounts.subscriptions.<a href="./src/cloudflare/resources/accounts/subscriptions/subscriptions.py">delete</a>(subscription_identifier, \*, account_id) -> <a href="./src/cloudflare/types/accounts/subscription_delete_response.py">SubscriptionDeleteResponse</a></code>
- <code title="post /accounts/{account_id}/subscriptions/cancel-downgrade">client.accounts.subscriptions.<a href="./src/cloudflare/resources/accounts/subscriptions/subscriptions.py">cancel_downgrade</a>(\*, account_id, \*\*<a href="src/cloudflare/types/accounts/subscription_cancel_downgrade_params.py">params</a>) -> <a href="./src/cloudflare/types/accounts/subscription_cancel_downgrade_response.py">SubscriptionCancelDowngradeResponse</a></code>
- <code title="get /{accounts_or_zones}/{account_or_zone_id}/subscriptions">client.accounts.subscriptions.<a href="./src/cloudflare/resources/accounts/subscriptions/subscriptions.py">get</a>(\*, account_id, zone_id) -> <a href="./src/cloudflare/types/shared/subscription.py">SyncSinglePage[Subscription]</a></code>
- <code title="get /accounts/{account_id}/subscriptions/{subscription_identifier}">client.accounts.subscriptions.<a href="./src/cloudflare/resources/accounts/subscriptions/subscriptions.py">get_by_identifier</a>(subscription_identifier, \*, account_id) -> <a href="./src/cloudflare/types/shared/subscription.py">Subscription</a></code>

### CancelReason

Types:

```python
from cloudflare.types.accounts.subscriptions import (
    CancelReasonCreateResponse,
    CancelReasonGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/subscriptions/{subscription_identifier}/cancel-reason">client.accounts.subscriptions.cancel_reason.<a href="./src/cloudflare/resources/accounts/subscriptions/cancel_reason.py">create</a>(subscription_identifier, \*, account_id, \*\*<a href="src/cloudflare/types/accounts/subscriptions/cancel_reason_create_params.py">params</a>) -> <a href="./src/cloudflare/types/accounts/subscriptions/cancel_reason_create_response.py">CancelReasonCreateResponse</a></code>
- <code title="get /accounts/{account_id}/subscriptions/{subscription_identifier}/cancel-reason">client.accounts.subscriptions.cancel_reason.<a href="./src/cloudflare/resources/accounts/subscriptions/cancel_reason.py">get</a>(subscription_identifier, \*, account_id) -> <a href="./src/cloudflare/types/accounts/subscriptions/cancel_reason_get_response.py">CancelReasonGetResponse</a></code>

### Actions

Methods:

- <code title="post /accounts/{account_id}/subscriptions/{subscription_identifier}/action/append">client.accounts.subscriptions.actions.<a href="./src/cloudflare/resources/accounts/subscriptions/actions.py">append</a>(subscription_identifier, \*, account_id, \*\*<a href="src/cloudflare/types/accounts/subscriptions/action_append_params.py">params</a>) -> <a href="./src/cloudflare/types/shared/subscription.py">Subscription</a></code>

### Bulk

Types:

```python
from cloudflare.types.accounts.subscriptions import BulkCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/bulk/subscriptions">client.accounts.subscriptions.bulk.<a href="./src/cloudflare/resources/accounts/subscriptions/bulk.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/accounts/subscriptions/bulk_create_params.py">params</a>) -> <a href="./src/cloudflare/types/accounts/subscriptions/bulk_create_response.py">BulkCreateResponse</a></code>

## Tokens

Types:

```python
from cloudflare.types.accounts import TokenCreateResponse, TokenDeleteResponse, TokenVerifyResponse
```

Methods:

- <code title="post /accounts/{account_id}/tokens">client.accounts.tokens.<a href="./src/cloudflare/resources/accounts/tokens/tokens.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/accounts/token_create_params.py">params</a>) -> <a href="./src/cloudflare/types/accounts/token_create_response.py">Optional[TokenCreateResponse]</a></code>
- <code title="put /accounts/{account_id}/tokens/{token_id}">client.accounts.tokens.<a href="./src/cloudflare/resources/accounts/tokens/tokens.py">update</a>(token_id, \*, account_id, \*\*<a href="src/cloudflare/types/accounts/token_update_params.py">params</a>) -> <a href="./src/cloudflare/types/shared/token.py">Optional[Token]</a></code>
- <code title="get /accounts/{account_id}/tokens">client.accounts.tokens.<a href="./src/cloudflare/resources/accounts/tokens/tokens.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/accounts/token_list_params.py">params</a>) -> <a href="./src/cloudflare/types/shared/token.py">SyncV4PagePaginationArray[Token]</a></code>
- <code title="delete /accounts/{account_id}/tokens/{token_id}">client.accounts.tokens.<a href="./src/cloudflare/resources/accounts/tokens/tokens.py">delete</a>(token_id, \*, account_id) -> <a href="./src/cloudflare/types/accounts/token_delete_response.py">Optional[TokenDeleteResponse]</a></code>
- <code title="get /accounts/{account_id}/tokens/{token_id}">client.accounts.tokens.<a href="./src/cloudflare/resources/accounts/tokens/tokens.py">get</a>(token_id, \*, account_id) -> <a href="./src/cloudflare/types/shared/token.py">Optional[Token]</a></code>
- <code title="get /accounts/{account_id}/tokens/verify">client.accounts.tokens.<a href="./src/cloudflare/resources/accounts/tokens/tokens.py">verify</a>(\*, account_id) -> <a href="./src/cloudflare/types/accounts/token_verify_response.py">Optional[TokenVerifyResponse]</a></code>

### PermissionGroups

Types:

```python
from cloudflare.types.accounts.tokens import PermissionGroupListResponse, PermissionGroupGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/tokens/permission_groups">client.accounts.tokens.permission_groups.<a href="./src/cloudflare/resources/accounts/tokens/permission_groups.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/accounts/tokens/permission_group_list_params.py">params</a>) -> <a href="./src/cloudflare/types/accounts/tokens/permission_group_list_response.py">SyncSinglePage[PermissionGroupListResponse]</a></code>
- <code title="get /accounts/{account_id}/tokens/permission_groups">client.accounts.tokens.permission_groups.<a href="./src/cloudflare/resources/accounts/tokens/permission_groups.py">get</a>(\*, account_id, \*\*<a href="src/cloudflare/types/accounts/tokens/permission_group_get_params.py">params</a>) -> <a href="./src/cloudflare/types/accounts/tokens/permission_group_get_response.py">Optional[PermissionGroupGetResponse]</a></code>

### Value

Methods:

- <code title="put /accounts/{account_id}/tokens/{token_id}/value">client.accounts.tokens.value.<a href="./src/cloudflare/resources/accounts/tokens/value.py">update</a>(token_id, \*, account_id) -> <a href="./src/cloudflare/types/shared/token_value.py">str</a></code>

## Logs

### Audit

Types:

```python
from cloudflare.types.accounts.logs import (
    AuditListResponse,
    AuditHistoryResponse,
    AuditProductCategoriesResponse,
)
```

Methods:

- <code title="get /accounts/{account_id}/logs/audit">client.accounts.logs.audit.<a href="./src/cloudflare/resources/accounts/logs/audit.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/accounts/logs/audit_list_params.py">params</a>) -> <a href="./src/cloudflare/types/accounts/logs/audit_list_response.py">SyncCursorPaginationAfter[AuditListResponse]</a></code>
- <code title="get /accounts/{account_id}/logs/audit/{id}/history">client.accounts.logs.audit.<a href="./src/cloudflare/resources/accounts/logs/audit.py">history</a>(id, \*, account_id, \*\*<a href="src/cloudflare/types/accounts/logs/audit_history_params.py">params</a>) -> <a href="./src/cloudflare/types/accounts/logs/audit_history_response.py">AuditHistoryResponse</a></code>
- <code title="get /accounts/{account_id}/logs/audit/product_categories">client.accounts.logs.audit.<a href="./src/cloudflare/resources/accounts/logs/audit.py">product_categories</a>(\*, account_id) -> <a href="./src/cloudflare/types/accounts/logs/audit_product_categories_response.py">SyncSinglePage[AuditProductCategoriesResponse]</a></code>

## Entitlements

Types:

```python
from cloudflare.types.accounts import EntitlementListResponse
```

Methods:

- <code title="get /accounts/{account_id}/entitlements">client.accounts.entitlements.<a href="./src/cloudflare/resources/accounts/entitlements.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/accounts/entitlement_list_response.py">SyncSinglePage[EntitlementListResponse]</a></code>

## SpeedSettings

### Transformations

Types:

```python
from cloudflare.types.accounts.speed_settings import TransformationsConfig
```

Methods:

- <code title="get /accounts/{account_id}/settings/transformations">client.accounts.speed_settings.transformations.<a href="./src/cloudflare/resources/accounts/speed_settings/transformations.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/accounts/speed_settings/transformations_config.py">SyncSinglePage[TransformationsConfig]</a></code>

## PaymentMethods

Types:

```python
from cloudflare.types.accounts import (
    PaymentMethodCreateResponse,
    PaymentMethodUpdateResponse,
    PaymentMethodListResponse,
    PaymentMethodDeleteResponse,
    PaymentMethodGetResponse,
    PaymentMethodSetAsDefaultResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/payment-methods">client.accounts.payment_methods.<a href="./src/cloudflare/resources/accounts/payment_methods.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/accounts/payment_method_create_params.py">params</a>) -> <a href="./src/cloudflare/types/accounts/payment_method_create_response.py">PaymentMethodCreateResponse</a></code>
- <code title="put /accounts/{account_id}/payment-methods/{payment_method_id}">client.accounts.payment_methods.<a href="./src/cloudflare/resources/accounts/payment_methods.py">update</a>(payment_method_id, \*, account_id, \*\*<a href="src/cloudflare/types/accounts/payment_method_update_params.py">params</a>) -> <a href="./src/cloudflare/types/accounts/payment_method_update_response.py">PaymentMethodUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/payment-methods">client.accounts.payment_methods.<a href="./src/cloudflare/resources/accounts/payment_methods.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/accounts/payment_method_list_params.py">params</a>) -> <a href="./src/cloudflare/types/accounts/payment_method_list_response.py">SyncV4PagePaginationArray[PaymentMethodListResponse]</a></code>
- <code title="delete /accounts/{account_id}/payment-methods/{payment_method_id}">client.accounts.payment_methods.<a href="./src/cloudflare/resources/accounts/payment_methods.py">delete</a>(payment_method_id, \*, account_id) -> <a href="./src/cloudflare/types/accounts/payment_method_delete_response.py">PaymentMethodDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/payment-methods/{payment_method_id}">client.accounts.payment_methods.<a href="./src/cloudflare/resources/accounts/payment_methods.py">get</a>(payment_method_id, \*, account_id) -> <a href="./src/cloudflare/types/accounts/payment_method_get_response.py">PaymentMethodGetResponse</a></code>
- <code title="post /accounts/{account_id}/payment-methods/{payment_method_id}/set-as-default">client.accounts.payment_methods.<a href="./src/cloudflare/resources/accounts/payment_methods.py">set_as_default</a>(payment_method_id, \*, account_id) -> <a href="./src/cloudflare/types/accounts/payment_method_set_as_default_response.py">PaymentMethodSetAsDefaultResponse</a></code>

## PayInvoice

Types:

```python
from cloudflare.types.accounts import PayInvoiceCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/pay-invoice">client.accounts.pay_invoice.<a href="./src/cloudflare/resources/accounts/pay_invoice.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/accounts/pay_invoice_create_params.py">params</a>) -> <a href="./src/cloudflare/types/accounts/pay_invoice_create_response.py">PayInvoiceCreateResponse</a></code>

## Receipts

Methods:

- <code title="get /accounts/{account_id}/receipts/{receipt_id}/pdf">client.accounts.receipts.<a href="./src/cloudflare/resources/accounts/receipts.py">pdf</a>(receipt_id, \*, account_id, \*\*<a href="src/cloudflare/types/accounts/receipt_pdf_params.py">params</a>) -> BinaryAPIResponse</code>

## Invoices

Types:

```python
from cloudflare.types.accounts import InvoiceEditResponse
```

Methods:

- <code title="patch /accounts/{account_id}/invoices">client.accounts.invoices.<a href="./src/cloudflare/resources/accounts/invoices.py">edit</a>(\*, account_id, \*\*<a href="src/cloudflare/types/accounts/invoice_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/accounts/invoice_edit_response.py">InvoiceEditResponse</a></code>

## ClientSecret

Types:

```python
from cloudflare.types.accounts import ClientSecretCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/client-secret">client.accounts.client_secret.<a href="./src/cloudflare/resources/accounts/client_secret.py">create</a>(\*, account_id) -> <a href="./src/cloudflare/types/accounts/client_secret_create_response.py">ClientSecretCreateResponse</a></code>
