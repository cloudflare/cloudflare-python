# User

Types:

```python
from cloudflare.types.user import UserEditResponse, UserGetResponse
```

Methods:

- <code title="patch /user">client.user.<a href="./src/cloudflare/resources/user/user.py">edit</a>(\*\*<a href="src/cloudflare/types/user/user_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/user/user_edit_response.py">Optional[UserEditResponse]</a></code>
- <code title="get /user">client.user.<a href="./src/cloudflare/resources/user/user.py">get</a>() -> <a href="./src/cloudflare/types/user/user_get_response.py">Optional[UserGetResponse]</a></code>

## AuditLogs

Methods:

- <code title="get /user/audit_logs">client.user.audit_logs.<a href="./src/cloudflare/resources/user/audit_logs.py">list</a>(\*\*<a href="src/cloudflare/types/user/audit_log_list_params.py">params</a>) -> <a href="./src/cloudflare/types/shared/audit_log.py">SyncV4PagePaginationArray[AuditLog]</a></code>

## Billing

### History

Types:

```python
from cloudflare.types.user.billing import BillingHistory
```

Methods:

- <code title="get /user/billing/history">client.user.billing.history.<a href="./src/cloudflare/resources/user/billing/history.py">list</a>(\*\*<a href="src/cloudflare/types/user/billing/history_list_params.py">params</a>) -> <a href="./src/cloudflare/types/user/billing/billing_history.py">SyncV4PagePaginationArray[BillingHistory]</a></code>

### Profile

Types:

```python
from cloudflare.types.user.billing import ProfileGetResponse
```

Methods:

- <code title="get /user/billing/profile">client.user.billing.profile.<a href="./src/cloudflare/resources/user/billing/profile.py">get</a>() -> <a href="./src/cloudflare/types/user/billing/profile_get_response.py">ProfileGetResponse</a></code>

## Invites

Types:

```python
from cloudflare.types.user import Invite
```

Methods:

- <code title="get /user/invites">client.user.invites.<a href="./src/cloudflare/resources/user/invites.py">list</a>() -> <a href="./src/cloudflare/types/user/invite.py">SyncSinglePage[Invite]</a></code>
- <code title="patch /user/invites/{invite_id}">client.user.invites.<a href="./src/cloudflare/resources/user/invites.py">edit</a>(invite_id, \*\*<a href="src/cloudflare/types/user/invite_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/user/invite.py">Optional[Invite]</a></code>
- <code title="get /user/invites/{invite_id}">client.user.invites.<a href="./src/cloudflare/resources/user/invites.py">get</a>(invite_id) -> <a href="./src/cloudflare/types/user/invite.py">Optional[Invite]</a></code>

## Organizations

Types:

```python
from cloudflare.types.user import Organization, OrganizationDeleteResponse
```

Methods:

- <code title="get /user/organizations">client.user.organizations.<a href="./src/cloudflare/resources/user/organizations.py">list</a>(\*\*<a href="src/cloudflare/types/user/organization_list_params.py">params</a>) -> <a href="./src/cloudflare/types/user/organization.py">SyncV4PagePaginationArray[Organization]</a></code>
- <code title="delete /user/organizations/{organization_id}">client.user.organizations.<a href="./src/cloudflare/resources/user/organizations.py">delete</a>(organization_id) -> <a href="./src/cloudflare/types/user/organization_delete_response.py">OrganizationDeleteResponse</a></code>
- <code title="get /user/organizations/{organization_id}">client.user.organizations.<a href="./src/cloudflare/resources/user/organizations.py">get</a>(organization_id) -> object</code>

## Subscriptions

Types:

```python
from cloudflare.types.user import SubscriptionUpdateResponse, SubscriptionDeleteResponse
```

Methods:

- <code title="put /user/subscriptions/{identifier}">client.user.subscriptions.<a href="./src/cloudflare/resources/user/subscriptions.py">update</a>(identifier, \*\*<a href="src/cloudflare/types/user/subscription_update_params.py">params</a>) -> <a href="./src/cloudflare/types/user/subscription_update_response.py">SubscriptionUpdateResponse</a></code>
- <code title="delete /user/subscriptions/{identifier}">client.user.subscriptions.<a href="./src/cloudflare/resources/user/subscriptions.py">delete</a>(identifier) -> <a href="./src/cloudflare/types/user/subscription_delete_response.py">SubscriptionDeleteResponse</a></code>
- <code title="get /user/subscriptions">client.user.subscriptions.<a href="./src/cloudflare/resources/user/subscriptions.py">get</a>() -> <a href="./src/cloudflare/types/shared/subscription.py">SyncSinglePage[Subscription]</a></code>

## Tokens

Types:

```python
from cloudflare.types.user import TokenCreateResponse, TokenDeleteResponse, TokenVerifyResponse
```

Methods:

- <code title="post /user/tokens">client.user.tokens.<a href="./src/cloudflare/resources/user/tokens/tokens.py">create</a>(\*\*<a href="src/cloudflare/types/user/token_create_params.py">params</a>) -> <a href="./src/cloudflare/types/user/token_create_response.py">Optional[TokenCreateResponse]</a></code>
- <code title="put /user/tokens/{token_id}">client.user.tokens.<a href="./src/cloudflare/resources/user/tokens/tokens.py">update</a>(token_id, \*\*<a href="src/cloudflare/types/user/token_update_params.py">params</a>) -> <a href="./src/cloudflare/types/shared/token.py">Optional[Token]</a></code>
- <code title="get /user/tokens">client.user.tokens.<a href="./src/cloudflare/resources/user/tokens/tokens.py">list</a>(\*\*<a href="src/cloudflare/types/user/token_list_params.py">params</a>) -> <a href="./src/cloudflare/types/shared/token.py">SyncV4PagePaginationArray[Token]</a></code>
- <code title="delete /user/tokens/{token_id}">client.user.tokens.<a href="./src/cloudflare/resources/user/tokens/tokens.py">delete</a>(token_id) -> <a href="./src/cloudflare/types/user/token_delete_response.py">Optional[TokenDeleteResponse]</a></code>
- <code title="get /user/tokens/{token_id}">client.user.tokens.<a href="./src/cloudflare/resources/user/tokens/tokens.py">get</a>(token_id) -> <a href="./src/cloudflare/types/shared/token.py">Optional[Token]</a></code>
- <code title="get /user/tokens/verify">client.user.tokens.<a href="./src/cloudflare/resources/user/tokens/tokens.py">verify</a>() -> <a href="./src/cloudflare/types/user/token_verify_response.py">Optional[TokenVerifyResponse]</a></code>

### PermissionGroups

Types:

```python
from cloudflare.types.user.tokens import PermissionGroupListResponse
```

Methods:

- <code title="get /user/tokens/permission_groups">client.user.tokens.permission_groups.<a href="./src/cloudflare/resources/user/tokens/permission_groups.py">list</a>(\*\*<a href="src/cloudflare/types/user/tokens/permission_group_list_params.py">params</a>) -> <a href="./src/cloudflare/types/user/tokens/permission_group_list_response.py">SyncSinglePage[PermissionGroupListResponse]</a></code>

### Value

Methods:

- <code title="put /user/tokens/{token_id}/value">client.user.tokens.value.<a href="./src/cloudflare/resources/user/tokens/value.py">update</a>(token_id, \*\*<a href="src/cloudflare/types/user/tokens/value_update_params.py">params</a>) -> <a href="./src/cloudflare/types/shared/token_value.py">str</a></code>
