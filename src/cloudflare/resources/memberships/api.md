# Memberships

Types:

```python
from cloudflare.types.memberships import (
    Membership,
    MembershipUpdateResponse,
    MembershipDeleteResponse,
    MembershipGetResponse,
)
```

Methods:

- <code title="put /memberships/{membership_id}">client.memberships.<a href="./src/cloudflare/resources/memberships/memberships.py">update</a>(membership_id, \*\*<a href="src/cloudflare/types/memberships/membership_update_params.py">params</a>) -> <a href="./src/cloudflare/types/memberships/membership_update_response.py">Optional[MembershipUpdateResponse]</a></code>
- <code title="get /memberships">client.memberships.<a href="./src/cloudflare/resources/memberships/memberships.py">list</a>(\*\*<a href="src/cloudflare/types/memberships/membership_list_params.py">params</a>) -> <a href="./src/cloudflare/types/memberships/membership.py">SyncV4PagePaginationArray[Membership]</a></code>
- <code title="delete /memberships/{membership_id}">client.memberships.<a href="./src/cloudflare/resources/memberships/memberships.py">delete</a>(membership_id) -> <a href="./src/cloudflare/types/memberships/membership_delete_response.py">Optional[MembershipDeleteResponse]</a></code>
- <code title="get /memberships/{membership_id}">client.memberships.<a href="./src/cloudflare/resources/memberships/memberships.py">get</a>(membership_id) -> <a href="./src/cloudflare/types/memberships/membership_get_response.py">Optional[MembershipGetResponse]</a></code>
