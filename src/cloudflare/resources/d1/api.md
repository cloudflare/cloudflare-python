# D1

Types:

```python
from cloudflare.types.d1 import D1
```

## Database

Types:

```python
from cloudflare.types.d1 import (
    QueryResult,
    DatabaseListResponse,
    DatabaseExportResponse,
    DatabaseImportResponse,
    DatabaseRawResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/d1/database">client.d1.database.<a href="./src/cloudflare/resources/d1/database/database.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/d1/database_create_params.py">params</a>) -> <a href="./src/cloudflare/types/d1/d1.py">D1</a></code>
- <code title="put /accounts/{account_id}/d1/database/{database_id}">client.d1.database.<a href="./src/cloudflare/resources/d1/database/database.py">update</a>(database_id, \*, account_id, \*\*<a href="src/cloudflare/types/d1/database_update_params.py">params</a>) -> <a href="./src/cloudflare/types/d1/d1.py">D1</a></code>
- <code title="get /accounts/{account_id}/d1/database">client.d1.database.<a href="./src/cloudflare/resources/d1/database/database.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/d1/database_list_params.py">params</a>) -> <a href="./src/cloudflare/types/d1/database_list_response.py">SyncV4PagePaginationArray[DatabaseListResponse]</a></code>
- <code title="delete /accounts/{account_id}/d1/database/{database_id}">client.d1.database.<a href="./src/cloudflare/resources/d1/database/database.py">delete</a>(database_id, \*, account_id) -> object</code>
- <code title="patch /accounts/{account_id}/d1/database/{database_id}">client.d1.database.<a href="./src/cloudflare/resources/d1/database/database.py">edit</a>(database_id, \*, account_id, \*\*<a href="src/cloudflare/types/d1/database_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/d1/d1.py">D1</a></code>
- <code title="post /accounts/{account_id}/d1/database/{database_id}/export">client.d1.database.<a href="./src/cloudflare/resources/d1/database/database.py">export</a>(database_id, \*, account_id, \*\*<a href="src/cloudflare/types/d1/database_export_params.py">params</a>) -> <a href="./src/cloudflare/types/d1/database_export_response.py">DatabaseExportResponse</a></code>
- <code title="get /accounts/{account_id}/d1/database/{database_id}">client.d1.database.<a href="./src/cloudflare/resources/d1/database/database.py">get</a>(database_id, \*, account_id) -> <a href="./src/cloudflare/types/d1/d1.py">D1</a></code>
- <code title="post /accounts/{account_id}/d1/database/{database_id}/import">client.d1.database.<a href="./src/cloudflare/resources/d1/database/database.py">import\_</a>(database_id, \*, account_id, \*\*<a href="src/cloudflare/types/d1/database_import_params.py">params</a>) -> <a href="./src/cloudflare/types/d1/database_import_response.py">DatabaseImportResponse</a></code>
- <code title="post /accounts/{account_id}/d1/database/{database_id}/query">client.d1.database.<a href="./src/cloudflare/resources/d1/database/database.py">query</a>(database_id, \*, account_id, \*\*<a href="src/cloudflare/types/d1/database_query_params.py">params</a>) -> <a href="./src/cloudflare/types/d1/query_result.py">SyncSinglePage[QueryResult]</a></code>
- <code title="post /accounts/{account_id}/d1/database/{database_id}/raw">client.d1.database.<a href="./src/cloudflare/resources/d1/database/database.py">raw</a>(database_id, \*, account_id, \*\*<a href="src/cloudflare/types/d1/database_raw_params.py">params</a>) -> <a href="./src/cloudflare/types/d1/database_raw_response.py">SyncSinglePage[DatabaseRawResponse]</a></code>

### TimeTravel

Types:

```python
from cloudflare.types.d1.database import TimeTravelGetBookmarkResponse, TimeTravelRestoreResponse
```

Methods:

- <code title="get /accounts/{account_id}/d1/database/{database_id}/time_travel/bookmark">client.d1.database.time_travel.<a href="./src/cloudflare/resources/d1/database/time_travel.py">get_bookmark</a>(database_id, \*, account_id, \*\*<a href="src/cloudflare/types/d1/database/time_travel_get_bookmark_params.py">params</a>) -> <a href="./src/cloudflare/types/d1/database/time_travel_get_bookmark_response.py">TimeTravelGetBookmarkResponse</a></code>
- <code title="post /accounts/{account_id}/d1/database/{database_id}/time_travel/restore">client.d1.database.time_travel.<a href="./src/cloudflare/resources/d1/database/time_travel.py">restore</a>(database_id, \*, account_id, \*\*<a href="src/cloudflare/types/d1/database/time_travel_restore_params.py">params</a>) -> <a href="./src/cloudflare/types/d1/database/time_travel_restore_response.py">TimeTravelRestoreResponse</a></code>
