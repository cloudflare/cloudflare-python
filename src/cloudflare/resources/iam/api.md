# IAM

## PermissionGroups

Types:

```python
from cloudflare.types.iam import PermissionGroupListResponse, PermissionGroupGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/iam/permission_groups">client.iam.permission_groups.<a href="./src/cloudflare/resources/iam/permission_groups.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/iam/permission_group_list_params.py">params</a>) -> <a href="./src/cloudflare/types/iam/permission_group_list_response.py">SyncV4PagePaginationArray[PermissionGroupListResponse]</a></code>
- <code title="get /accounts/{account_id}/iam/permission_groups/{permission_group_id}">client.iam.permission_groups.<a href="./src/cloudflare/resources/iam/permission_groups.py">get</a>(permission_group_id, \*, account_id) -> <a href="./src/cloudflare/types/iam/permission_group_get_response.py">Optional[PermissionGroupGetResponse]</a></code>

## ResourceGroups

Types:

```python
from cloudflare.types.iam import (
    ResourceGroupCreateResponse,
    ResourceGroupUpdateResponse,
    ResourceGroupListResponse,
    ResourceGroupDeleteResponse,
    ResourceGroupGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/iam/resource_groups">client.iam.resource_groups.<a href="./src/cloudflare/resources/iam/resource_groups.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/iam/resource_group_create_params.py">params</a>) -> <a href="./src/cloudflare/types/iam/resource_group_create_response.py">Optional[ResourceGroupCreateResponse]</a></code>
- <code title="put /accounts/{account_id}/iam/resource_groups/{resource_group_id}">client.iam.resource_groups.<a href="./src/cloudflare/resources/iam/resource_groups.py">update</a>(resource_group_id, \*, account_id, \*\*<a href="src/cloudflare/types/iam/resource_group_update_params.py">params</a>) -> <a href="./src/cloudflare/types/iam/resource_group_update_response.py">Optional[ResourceGroupUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/iam/resource_groups">client.iam.resource_groups.<a href="./src/cloudflare/resources/iam/resource_groups.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/iam/resource_group_list_params.py">params</a>) -> <a href="./src/cloudflare/types/iam/resource_group_list_response.py">SyncSinglePage[ResourceGroupListResponse]</a></code>
- <code title="delete /accounts/{account_id}/iam/resource_groups/{resource_group_id}">client.iam.resource_groups.<a href="./src/cloudflare/resources/iam/resource_groups.py">delete</a>(resource_group_id, \*, account_id) -> <a href="./src/cloudflare/types/iam/resource_group_delete_response.py">Optional[ResourceGroupDeleteResponse]</a></code>
- <code title="get /accounts/{account_id}/iam/resource_groups/{resource_group_id}">client.iam.resource_groups.<a href="./src/cloudflare/resources/iam/resource_groups.py">get</a>(resource_group_id, \*, account_id) -> <a href="./src/cloudflare/types/iam/resource_group_get_response.py">Optional[ResourceGroupGetResponse]</a></code>

## UserGroups

Types:

```python
from cloudflare.types.iam import (
    UserGroupCreateResponse,
    UserGroupUpdateResponse,
    UserGroupListResponse,
    UserGroupDeleteResponse,
    UserGroupGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/iam/user_groups">client.iam.user_groups.<a href="./src/cloudflare/resources/iam/user_groups/user_groups.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/iam/user_group_create_params.py">params</a>) -> <a href="./src/cloudflare/types/iam/user_group_create_response.py">Optional[UserGroupCreateResponse]</a></code>
- <code title="put /accounts/{account_id}/iam/user_groups/{user_group_id}">client.iam.user_groups.<a href="./src/cloudflare/resources/iam/user_groups/user_groups.py">update</a>(user_group_id, \*, account_id, \*\*<a href="src/cloudflare/types/iam/user_group_update_params.py">params</a>) -> <a href="./src/cloudflare/types/iam/user_group_update_response.py">Optional[UserGroupUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/iam/user_groups">client.iam.user_groups.<a href="./src/cloudflare/resources/iam/user_groups/user_groups.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/iam/user_group_list_params.py">params</a>) -> <a href="./src/cloudflare/types/iam/user_group_list_response.py">SyncV4PagePaginationArray[UserGroupListResponse]</a></code>
- <code title="delete /accounts/{account_id}/iam/user_groups/{user_group_id}">client.iam.user_groups.<a href="./src/cloudflare/resources/iam/user_groups/user_groups.py">delete</a>(user_group_id, \*, account_id) -> <a href="./src/cloudflare/types/iam/user_group_delete_response.py">Optional[UserGroupDeleteResponse]</a></code>
- <code title="get /accounts/{account_id}/iam/user_groups/{user_group_id}">client.iam.user_groups.<a href="./src/cloudflare/resources/iam/user_groups/user_groups.py">get</a>(user_group_id, \*, account_id) -> <a href="./src/cloudflare/types/iam/user_group_get_response.py">Optional[UserGroupGetResponse]</a></code>

### Members

Types:

```python
from cloudflare.types.iam.user_groups import (
    MemberCreateResponse,
    MemberUpdateResponse,
    MemberListResponse,
    MemberDeleteResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/iam/user_groups/{user_group_id}/members">client.iam.user_groups.members.<a href="./src/cloudflare/resources/iam/user_groups/members.py">create</a>(user_group_id, \*, account_id, \*\*<a href="src/cloudflare/types/iam/user_groups/member_create_params.py">params</a>) -> <a href="./src/cloudflare/types/iam/user_groups/member_create_response.py">Optional[MemberCreateResponse]</a></code>
- <code title="put /accounts/{account_id}/iam/user_groups/{user_group_id}/members">client.iam.user_groups.members.<a href="./src/cloudflare/resources/iam/user_groups/members.py">update</a>(user_group_id, \*, account_id, \*\*<a href="src/cloudflare/types/iam/user_groups/member_update_params.py">params</a>) -> <a href="./src/cloudflare/types/iam/user_groups/member_update_response.py">SyncSinglePage[MemberUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/iam/user_groups/{user_group_id}/members">client.iam.user_groups.members.<a href="./src/cloudflare/resources/iam/user_groups/members.py">list</a>(user_group_id, \*, account_id, \*\*<a href="src/cloudflare/types/iam/user_groups/member_list_params.py">params</a>) -> <a href="./src/cloudflare/types/iam/user_groups/member_list_response.py">SyncV4PagePaginationArray[MemberListResponse]</a></code>
- <code title="delete /accounts/{account_id}/iam/user_groups/{user_group_id}/members/{member_id}">client.iam.user_groups.members.<a href="./src/cloudflare/resources/iam/user_groups/members.py">delete</a>(member_id, \*, account_id, user_group_id) -> <a href="./src/cloudflare/types/iam/user_groups/member_delete_response.py">Optional[MemberDeleteResponse]</a></code>

## SSO

Types:

```python
from cloudflare.types.iam import (
    SSOCreateResponse,
    SSOUpdateResponse,
    SSOListResponse,
    SSODeleteResponse,
    SSOBeginVerificationResponse,
    SSOGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/sso_connectors">client.iam.sso.<a href="./src/cloudflare/resources/iam/sso.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/iam/sso_create_params.py">params</a>) -> <a href="./src/cloudflare/types/iam/sso_create_response.py">Optional[SSOCreateResponse]</a></code>
- <code title="patch /accounts/{account_id}/sso_connectors/{sso_connector_id}">client.iam.sso.<a href="./src/cloudflare/resources/iam/sso.py">update</a>(sso_connector_id, \*, account_id, \*\*<a href="src/cloudflare/types/iam/sso_update_params.py">params</a>) -> <a href="./src/cloudflare/types/iam/sso_update_response.py">Optional[SSOUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/sso_connectors">client.iam.sso.<a href="./src/cloudflare/resources/iam/sso.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/iam/sso_list_response.py">SyncSinglePage[SSOListResponse]</a></code>
- <code title="delete /accounts/{account_id}/sso_connectors/{sso_connector_id}">client.iam.sso.<a href="./src/cloudflare/resources/iam/sso.py">delete</a>(sso_connector_id, \*, account_id) -> <a href="./src/cloudflare/types/iam/sso_delete_response.py">Optional[SSODeleteResponse]</a></code>
- <code title="post /accounts/{account_id}/sso_connectors/{sso_connector_id}/begin_verification">client.iam.sso.<a href="./src/cloudflare/resources/iam/sso.py">begin_verification</a>(sso_connector_id, \*, account_id) -> <a href="./src/cloudflare/types/iam/sso_begin_verification_response.py">SSOBeginVerificationResponse</a></code>
- <code title="get /accounts/{account_id}/sso_connectors/{sso_connector_id}">client.iam.sso.<a href="./src/cloudflare/resources/iam/sso.py">get</a>(sso_connector_id, \*, account_id) -> <a href="./src/cloudflare/types/iam/sso_get_response.py">Optional[SSOGetResponse]</a></code>
