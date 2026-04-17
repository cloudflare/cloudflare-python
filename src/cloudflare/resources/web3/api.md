# Web3

## Hostnames

Types:

```python
from cloudflare.types.web3 import Hostname, HostnameDeleteResponse
```

Methods:

- <code title="post /zones/{zone_id}/web3/hostnames">client.web3.hostnames.<a href="./src/cloudflare/resources/web3/hostnames/hostnames.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/web3/hostname_create_params.py">params</a>) -> <a href="./src/cloudflare/types/web3/hostname.py">Hostname</a></code>
- <code title="get /zones/{zone_id}/web3/hostnames">client.web3.hostnames.<a href="./src/cloudflare/resources/web3/hostnames/hostnames.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/web3/hostname.py">SyncSinglePage[Hostname]</a></code>
- <code title="delete /zones/{zone_id}/web3/hostnames/{identifier}">client.web3.hostnames.<a href="./src/cloudflare/resources/web3/hostnames/hostnames.py">delete</a>(identifier, \*, zone_id) -> <a href="./src/cloudflare/types/web3/hostname_delete_response.py">Optional[HostnameDeleteResponse]</a></code>
- <code title="patch /zones/{zone_id}/web3/hostnames/{identifier}">client.web3.hostnames.<a href="./src/cloudflare/resources/web3/hostnames/hostnames.py">edit</a>(identifier, \*, zone_id, \*\*<a href="src/cloudflare/types/web3/hostname_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/web3/hostname.py">Hostname</a></code>
- <code title="get /zones/{zone_id}/web3/hostnames/{identifier}">client.web3.hostnames.<a href="./src/cloudflare/resources/web3/hostnames/hostnames.py">get</a>(identifier, \*, zone_id) -> <a href="./src/cloudflare/types/web3/hostname.py">Hostname</a></code>

### IPFSUniversalPaths

#### ContentLists

Types:

```python
from cloudflare.types.web3.hostnames.ipfs_universal_paths import ContentList
```

Methods:

- <code title="put /zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list">client.web3.hostnames.ipfs_universal_paths.content_lists.<a href="./src/cloudflare/resources/web3/hostnames/ipfs_universal_paths/content_lists/content_lists.py">update</a>(identifier, \*, zone_id, \*\*<a href="src/cloudflare/types/web3/hostnames/ipfs_universal_paths/content_list_update_params.py">params</a>) -> <a href="./src/cloudflare/types/web3/hostnames/ipfs_universal_paths/content_list.py">ContentList</a></code>
- <code title="get /zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list">client.web3.hostnames.ipfs_universal_paths.content_lists.<a href="./src/cloudflare/resources/web3/hostnames/ipfs_universal_paths/content_lists/content_lists.py">get</a>(identifier, \*, zone_id) -> <a href="./src/cloudflare/types/web3/hostnames/ipfs_universal_paths/content_list.py">ContentList</a></code>

##### Entries

Types:

```python
from cloudflare.types.web3.hostnames.ipfs_universal_paths.content_lists import (
    EntryCreateResponse,
    EntryUpdateResponse,
    EntryListResponse,
    EntryDeleteResponse,
    EntryGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries">client.web3.hostnames.ipfs_universal_paths.content_lists.entries.<a href="./src/cloudflare/resources/web3/hostnames/ipfs_universal_paths/content_lists/entries.py">create</a>(identifier, \*, zone_id, \*\*<a href="src/cloudflare/types/web3/hostnames/ipfs_universal_paths/content_lists/entry_create_params.py">params</a>) -> <a href="./src/cloudflare/types/web3/hostnames/ipfs_universal_paths/content_lists/entry_create_response.py">EntryCreateResponse</a></code>
- <code title="put /zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries/{content_list_entry_identifier}">client.web3.hostnames.ipfs_universal_paths.content_lists.entries.<a href="./src/cloudflare/resources/web3/hostnames/ipfs_universal_paths/content_lists/entries.py">update</a>(content_list_entry_identifier, \*, zone_id, identifier, \*\*<a href="src/cloudflare/types/web3/hostnames/ipfs_universal_paths/content_lists/entry_update_params.py">params</a>) -> <a href="./src/cloudflare/types/web3/hostnames/ipfs_universal_paths/content_lists/entry_update_response.py">EntryUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries">client.web3.hostnames.ipfs_universal_paths.content_lists.entries.<a href="./src/cloudflare/resources/web3/hostnames/ipfs_universal_paths/content_lists/entries.py">list</a>(identifier, \*, zone_id) -> <a href="./src/cloudflare/types/web3/hostnames/ipfs_universal_paths/content_lists/entry_list_response.py">Optional[EntryListResponse]</a></code>
- <code title="delete /zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries/{content_list_entry_identifier}">client.web3.hostnames.ipfs_universal_paths.content_lists.entries.<a href="./src/cloudflare/resources/web3/hostnames/ipfs_universal_paths/content_lists/entries.py">delete</a>(content_list_entry_identifier, \*, zone_id, identifier) -> <a href="./src/cloudflare/types/web3/hostnames/ipfs_universal_paths/content_lists/entry_delete_response.py">Optional[EntryDeleteResponse]</a></code>
- <code title="get /zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries/{content_list_entry_identifier}">client.web3.hostnames.ipfs_universal_paths.content_lists.entries.<a href="./src/cloudflare/resources/web3/hostnames/ipfs_universal_paths/content_lists/entries.py">get</a>(content_list_entry_identifier, \*, zone_id, identifier) -> <a href="./src/cloudflare/types/web3/hostnames/ipfs_universal_paths/content_lists/entry_get_response.py">EntryGetResponse</a></code>
