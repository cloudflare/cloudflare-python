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
from cloudflare.types.accounts import SubscriptionDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/subscriptions">client.accounts.subscriptions.<a href="./src/cloudflare/resources/accounts/subscriptions.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/accounts/subscription_create_params.py">params</a>) -> <a href="./src/cloudflare/types/shared/subscription.py">Subscription</a></code>
- <code title="put /accounts/{account_id}/subscriptions/{subscription_identifier}">client.accounts.subscriptions.<a href="./src/cloudflare/resources/accounts/subscriptions.py">update</a>(subscription_identifier, \*, account_id, \*\*<a href="src/cloudflare/types/accounts/subscription_update_params.py">params</a>) -> <a href="./src/cloudflare/types/shared/subscription.py">Subscription</a></code>
- <code title="delete /accounts/{account_id}/subscriptions/{subscription_identifier}">client.accounts.subscriptions.<a href="./src/cloudflare/resources/accounts/subscriptions.py">delete</a>(subscription_identifier, \*, account_id) -> <a href="./src/cloudflare/types/accounts/subscription_delete_response.py">SubscriptionDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/subscriptions">client.accounts.subscriptions.<a href="./src/cloudflare/resources/accounts/subscriptions.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/shared/subscription.py">SyncSinglePage[Subscription]</a></code>

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

- <code title="put /accounts/{account_id}/tokens/{token_id}/value">client.accounts.tokens.value.<a href="./src/cloudflare/resources/accounts/tokens/value.py">update</a>(token_id, \*, account_id, \*\*<a href="src/cloudflare/types/accounts/tokens/value_update_params.py">params</a>) -> <a href="./src/cloudflare/types/shared/token_value.py">str</a></code>

## Logs

### Audit

Types:

```python
from cloudflare.types.accounts.logs import AuditListResponse
```

Methods:

- <code title="get /accounts/{account_id}/logs/audit">client.accounts.logs.audit.<a href="./src/cloudflare/resources/accounts/logs/audit.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/accounts/logs/audit_list_params.py">params</a>) -> <a href="./src/cloudflare/types/accounts/logs/audit_list_response.py">SyncCursorPaginationAfter[AuditListResponse]</a></code>
