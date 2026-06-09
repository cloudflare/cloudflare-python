# Flagship

## Apps

Types:

```python
from cloudflare.types.flagship import (
    AppCreateResponse,
    AppUpdateResponse,
    AppListResponse,
    AppDeleteResponse,
    AppGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/flagship/apps">client.flagship.apps.<a href="./src/cloudflare/resources/flagship/apps/apps.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/flagship/app_create_params.py">params</a>) -> <a href="./src/cloudflare/types/flagship/app_create_response.py">AppCreateResponse</a></code>
- <code title="put /accounts/{account_id}/flagship/apps/{app_id}">client.flagship.apps.<a href="./src/cloudflare/resources/flagship/apps/apps.py">update</a>(app_id, \*, account_id, \*\*<a href="src/cloudflare/types/flagship/app_update_params.py">params</a>) -> <a href="./src/cloudflare/types/flagship/app_update_response.py">AppUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/flagship/apps">client.flagship.apps.<a href="./src/cloudflare/resources/flagship/apps/apps.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/flagship/app_list_response.py">SyncSinglePage[AppListResponse]</a></code>
- <code title="delete /accounts/{account_id}/flagship/apps/{app_id}">client.flagship.apps.<a href="./src/cloudflare/resources/flagship/apps/apps.py">delete</a>(app_id, \*, account_id) -> <a href="./src/cloudflare/types/flagship/app_delete_response.py">AppDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/flagship/apps/{app_id}">client.flagship.apps.<a href="./src/cloudflare/resources/flagship/apps/apps.py">get</a>(app_id, \*, account_id) -> <a href="./src/cloudflare/types/flagship/app_get_response.py">AppGetResponse</a></code>

### Flags

Types:

```python
from cloudflare.types.flagship.apps import (
    FlagCreateResponse,
    FlagUpdateResponse,
    FlagListResponse,
    FlagDeleteResponse,
    FlagGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/flagship/apps/{app_id}/flags">client.flagship.apps.flags.<a href="./src/cloudflare/resources/flagship/apps/flags/flags.py">create</a>(app_id, \*, account_id, \*\*<a href="src/cloudflare/types/flagship/apps/flag_create_params.py">params</a>) -> <a href="./src/cloudflare/types/flagship/apps/flag_create_response.py">FlagCreateResponse</a></code>
- <code title="put /accounts/{account_id}/flagship/apps/{app_id}/flags/{flag_key}">client.flagship.apps.flags.<a href="./src/cloudflare/resources/flagship/apps/flags/flags.py">update</a>(flag_key, \*, account_id, app_id, \*\*<a href="src/cloudflare/types/flagship/apps/flag_update_params.py">params</a>) -> <a href="./src/cloudflare/types/flagship/apps/flag_update_response.py">FlagUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/flagship/apps/{app_id}/flags">client.flagship.apps.flags.<a href="./src/cloudflare/resources/flagship/apps/flags/flags.py">list</a>(app_id, \*, account_id, \*\*<a href="src/cloudflare/types/flagship/apps/flag_list_params.py">params</a>) -> <a href="./src/cloudflare/types/flagship/apps/flag_list_response.py">SyncCursorPaginationAfter[FlagListResponse]</a></code>
- <code title="delete /accounts/{account_id}/flagship/apps/{app_id}/flags/{flag_key}">client.flagship.apps.flags.<a href="./src/cloudflare/resources/flagship/apps/flags/flags.py">delete</a>(flag_key, \*, account_id, app_id) -> <a href="./src/cloudflare/types/flagship/apps/flag_delete_response.py">FlagDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/flagship/apps/{app_id}/flags/{flag_key}">client.flagship.apps.flags.<a href="./src/cloudflare/resources/flagship/apps/flags/flags.py">get</a>(flag_key, \*, account_id, app_id) -> <a href="./src/cloudflare/types/flagship/apps/flag_get_response.py">FlagGetResponse</a></code>

#### Changelog

Types:

```python
from cloudflare.types.flagship.apps.flags import ChangelogListResponse
```

Methods:

- <code title="get /accounts/{account_id}/flagship/apps/{app_id}/flags/{flag_key}/changelog">client.flagship.apps.flags.changelog.<a href="./src/cloudflare/resources/flagship/apps/flags/changelog.py">list</a>(flag_key, \*, account_id, app_id, \*\*<a href="src/cloudflare/types/flagship/apps/flags/changelog_list_params.py">params</a>) -> <a href="./src/cloudflare/types/flagship/apps/flags/changelog_list_response.py">SyncCursorPaginationAfter[ChangelogListResponse]</a></code>

### Evaluate

Types:

```python
from cloudflare.types.flagship.apps import EvaluateGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/flagship/apps/{app_id}/evaluate">client.flagship.apps.evaluate.<a href="./src/cloudflare/resources/flagship/apps/evaluate.py">get</a>(app_id, \*, account_id, \*\*<a href="src/cloudflare/types/flagship/apps/evaluate_get_params.py">params</a>) -> <a href="./src/cloudflare/types/flagship/apps/evaluate_get_response.py">EvaluateGetResponse</a></code>
