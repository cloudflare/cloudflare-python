# URLScanner

Types:

```python
from cloudflare.types.url_scanner import URLScannerDomain, URLScannerTask
```

## Responses

Types:

```python
from cloudflare.types.url_scanner import ResponseGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/urlscanner/v2/responses/{response_id}">client.url_scanner.responses.<a href="./src/cloudflare/resources/url_scanner/responses.py">get</a>(response_id, \*, account_id) -> str</code>

## Scans

Types:

```python
from cloudflare.types.url_scanner import (
    ScanCreateResponse,
    ScanListResponse,
    ScanBulkCreateResponse,
    ScanDOMResponse,
    ScanGetResponse,
    ScanHARResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/urlscanner/v2/scan">client.url_scanner.scans.<a href="./src/cloudflare/resources/url_scanner/scans.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/url_scanner/scan_create_params.py">params</a>) -> <a href="./src/cloudflare/types/url_scanner/scan_create_response.py">ScanCreateResponse</a></code>
- <code title="get /accounts/{account_id}/urlscanner/v2/search">client.url_scanner.scans.<a href="./src/cloudflare/resources/url_scanner/scans.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/url_scanner/scan_list_params.py">params</a>) -> <a href="./src/cloudflare/types/url_scanner/scan_list_response.py">ScanListResponse</a></code>
- <code title="post /accounts/{account_id}/urlscanner/v2/bulk">client.url_scanner.scans.<a href="./src/cloudflare/resources/url_scanner/scans.py">bulk_create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/url_scanner/scan_bulk_create_params.py">params</a>) -> <a href="./src/cloudflare/types/url_scanner/scan_bulk_create_response.py">ScanBulkCreateResponse</a></code>
- <code title="get /accounts/{account_id}/urlscanner/v2/dom/{scan_id}">client.url_scanner.scans.<a href="./src/cloudflare/resources/url_scanner/scans.py">dom</a>(scan_id, \*, account_id) -> str</code>
- <code title="get /accounts/{account_id}/urlscanner/v2/result/{scan_id}">client.url_scanner.scans.<a href="./src/cloudflare/resources/url_scanner/scans.py">get</a>(scan_id, \*, account_id) -> <a href="./src/cloudflare/types/url_scanner/scan_get_response.py">ScanGetResponse</a></code>
- <code title="get /accounts/{account_id}/urlscanner/v2/har/{scan_id}">client.url_scanner.scans.<a href="./src/cloudflare/resources/url_scanner/scans.py">har</a>(scan_id, \*, account_id) -> <a href="./src/cloudflare/types/url_scanner/scan_har_response.py">ScanHARResponse</a></code>
- <code title="get /accounts/{account_id}/urlscanner/v2/screenshots/{scan_id}.png">client.url_scanner.scans.<a href="./src/cloudflare/resources/url_scanner/scans.py">screenshot</a>(scan_id, \*, account_id, \*\*<a href="src/cloudflare/types/url_scanner/scan_screenshot_params.py">params</a>) -> BinaryAPIResponse</code>
