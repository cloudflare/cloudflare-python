# BrandProtection

Types:

```python
from cloudflare.types.brand_protection import (
    Info,
    Submit,
    BrandProtectionSubmitResponse,
    BrandProtectionURLInfoResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/brand-protection/submit">client.brand_protection.<a href="./src/cloudflare/resources/brand_protection/brand_protection.py">submit</a>(\*, account_id) -> <a href="./src/cloudflare/types/brand_protection/brand_protection_submit_response.py">BrandProtectionSubmitResponse</a></code>
- <code title="get /accounts/{account_id}/brand-protection/url-info">client.brand_protection.<a href="./src/cloudflare/resources/brand_protection/brand_protection.py">url_info</a>(\*, account_id) -> <a href="./src/cloudflare/types/brand_protection/brand_protection_url_info_response.py">SyncSinglePage[BrandProtectionURLInfoResponse]</a></code>

## Queries

Methods:

- <code title="post /accounts/{account_id}/brand-protection/queries">client.brand_protection.queries.<a href="./src/cloudflare/resources/brand_protection/queries.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/brand_protection/query_create_params.py">params</a>) -> None</code>
- <code title="delete /accounts/{account_id}/brand-protection/queries">client.brand_protection.queries.<a href="./src/cloudflare/resources/brand_protection/queries.py">delete</a>(\*, account_id, \*\*<a href="src/cloudflare/types/brand_protection/query_delete_params.py">params</a>) -> None</code>
- <code title="post /accounts/{account_id}/brand-protection/queries/bulk">client.brand_protection.queries.<a href="./src/cloudflare/resources/brand_protection/queries.py">bulk</a>(\*, account_id, \*\*<a href="src/cloudflare/types/brand_protection/query_bulk_params.py">params</a>) -> None</code>

## Matches

Types:

```python
from cloudflare.types.brand_protection import MatchDownloadResponse, MatchGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/brand-protection/matches/download">client.brand_protection.matches.<a href="./src/cloudflare/resources/brand_protection/matches.py">download</a>(\*, account_id, \*\*<a href="src/cloudflare/types/brand_protection/match_download_params.py">params</a>) -> <a href="./src/cloudflare/types/brand_protection/match_download_response.py">MatchDownloadResponse</a></code>
- <code title="get /accounts/{account_id}/brand-protection/matches">client.brand_protection.matches.<a href="./src/cloudflare/resources/brand_protection/matches.py">get</a>(\*, account_id, \*\*<a href="src/cloudflare/types/brand_protection/match_get_params.py">params</a>) -> <a href="./src/cloudflare/types/brand_protection/match_get_response.py">MatchGetResponse</a></code>

## Logos

Types:

```python
from cloudflare.types.brand_protection import LogoCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/brand-protection/logos">client.brand_protection.logos.<a href="./src/cloudflare/resources/brand_protection/logos.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/brand_protection/logo_create_params.py">params</a>) -> <a href="./src/cloudflare/types/brand_protection/logo_create_response.py">LogoCreateResponse</a></code>
- <code title="delete /accounts/{account_id}/brand-protection/logos/{logo_id}">client.brand_protection.logos.<a href="./src/cloudflare/resources/brand_protection/logos.py">delete</a>(logo_id, \*, account_id) -> None</code>

## LogoMatches

Types:

```python
from cloudflare.types.brand_protection import LogoMatchDownloadResponse, LogoMatchGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/brand-protection/logo-matches/download">client.brand_protection.logo_matches.<a href="./src/cloudflare/resources/brand_protection/logo_matches.py">download</a>(\*, account_id, \*\*<a href="src/cloudflare/types/brand_protection/logo_match_download_params.py">params</a>) -> <a href="./src/cloudflare/types/brand_protection/logo_match_download_response.py">LogoMatchDownloadResponse</a></code>
- <code title="get /accounts/{account_id}/brand-protection/logo-matches">client.brand_protection.logo_matches.<a href="./src/cloudflare/resources/brand_protection/logo_matches.py">get</a>(\*, account_id, \*\*<a href="src/cloudflare/types/brand_protection/logo_match_get_params.py">params</a>) -> <a href="./src/cloudflare/types/brand_protection/logo_match_get_response.py">LogoMatchGetResponse</a></code>

## V2

### Queries

Types:

```python
from cloudflare.types.brand_protection.v2 import QueryGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/cloudforce-one/v2/brand-protection/domain/queries">client.brand_protection.v2.queries.<a href="./src/cloudflare/resources/brand_protection/v2/queries.py">get</a>(\*, account_id, \*\*<a href="src/cloudflare/types/brand_protection/v2/query_get_params.py">params</a>) -> <a href="./src/cloudflare/types/brand_protection/v2/query_get_response.py">QueryGetResponse</a></code>

### Matches

Types:

```python
from cloudflare.types.brand_protection.v2 import MatchGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/cloudforce-one/v2/brand-protection/domain/matches">client.brand_protection.v2.matches.<a href="./src/cloudflare/resources/brand_protection/v2/matches.py">get</a>(\*, account_id, \*\*<a href="src/cloudflare/types/brand_protection/v2/match_get_params.py">params</a>) -> <a href="./src/cloudflare/types/brand_protection/v2/match_get_response.py">MatchGetResponse</a></code>

### Logos

Types:

```python
from cloudflare.types.brand_protection.v2 import (
    LogoCreateResponse,
    LogoDeleteResponse,
    LogoGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/cloudforce-one/v2/brand-protection/logo/queries">client.brand_protection.v2.logos.<a href="./src/cloudflare/resources/brand_protection/v2/logos.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/brand_protection/v2/logo_create_params.py">params</a>) -> <a href="./src/cloudflare/types/brand_protection/v2/logo_create_response.py">LogoCreateResponse</a></code>
- <code title="delete /accounts/{account_id}/cloudforce-one/v2/brand-protection/logo/queries/{query_id}">client.brand_protection.v2.logos.<a href="./src/cloudflare/resources/brand_protection/v2/logos.py">delete</a>(query_id, \*, account_id) -> <a href="./src/cloudflare/types/brand_protection/v2/logo_delete_response.py">LogoDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/cloudforce-one/v2/brand-protection/logo/queries">client.brand_protection.v2.logos.<a href="./src/cloudflare/resources/brand_protection/v2/logos.py">get</a>(\*, account_id, \*\*<a href="src/cloudflare/types/brand_protection/v2/logo_get_params.py">params</a>) -> <a href="./src/cloudflare/types/brand_protection/v2/logo_get_response.py">LogoGetResponse</a></code>

### LogoMatches

Types:

```python
from cloudflare.types.brand_protection.v2 import LogoMatchGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/cloudforce-one/v2/brand-protection/logo/matches">client.brand_protection.v2.logo_matches.<a href="./src/cloudflare/resources/brand_protection/v2/logo_matches.py">get</a>(\*, account_id, \*\*<a href="src/cloudflare/types/brand_protection/v2/logo_match_get_params.py">params</a>) -> <a href="./src/cloudflare/types/brand_protection/v2/logo_match_get_response.py">LogoMatchGetResponse</a></code>
