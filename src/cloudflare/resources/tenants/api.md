# Tenants

Types:

```python
from cloudflare.types.tenants import Tenant
```

Methods:

- <code title="get /tenants/{tenant_id}">client.tenants.<a href="./src/cloudflare/resources/tenants/tenants.py">get</a>(tenant_id) -> <a href="./src/cloudflare/types/tenants/tenant.py">Tenant</a></code>

## AccountTypes

Types:

```python
from cloudflare.types.tenants import AccountTypeListResponse
```

Methods:

- <code title="get /tenants/{tenant_id}/account_types">client.tenants.account_types.<a href="./src/cloudflare/resources/tenants/account_types.py">list</a>(tenant_id) -> <a href="./src/cloudflare/types/tenants/account_type_list_response.py">SyncSinglePage[AccountTypeListResponse]</a></code>

## Accounts

Types:

```python
from cloudflare.types.tenants import TenantAccount
```

Methods:

- <code title="get /tenants/{tenant_id}/accounts">client.tenants.accounts.<a href="./src/cloudflare/resources/tenants/accounts.py">list</a>(tenant_id) -> <a href="./src/cloudflare/types/tenants/tenant_account.py">SyncSinglePage[TenantAccount]</a></code>

## Entitlements

Types:

```python
from cloudflare.types.tenants import TenantEntitlements
```

Methods:

- <code title="get /tenants/{tenant_id}/entitlements">client.tenants.entitlements.<a href="./src/cloudflare/resources/tenants/entitlements.py">get</a>(tenant_id) -> <a href="./src/cloudflare/types/tenants/tenant_entitlements.py">TenantEntitlements</a></code>

## Memberships

Types:

```python
from cloudflare.types.tenants import TenantMembership
```

Methods:

- <code title="get /tenants/{tenant_id}/memberships">client.tenants.memberships.<a href="./src/cloudflare/resources/tenants/memberships.py">list</a>(tenant_id) -> <a href="./src/cloudflare/types/tenants/tenant_membership.py">SyncSinglePage[TenantMembership]</a></code>
