# BrowserRendering

## Content

Types:

```python
from cloudflare.types.browser_rendering import ContentCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/browser-rendering/content">client.browser_rendering.content.<a href="./src/cloudflare/resources/browser_rendering/content.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/browser_rendering/content_create_params.py">params</a>) -> <a href="./src/cloudflare/types/browser_rendering/content_create_response.py">str</a></code>

## PDF

Methods:

- <code title="post /accounts/{account_id}/browser-rendering/pdf">client.browser_rendering.pdf.<a href="./src/cloudflare/resources/browser_rendering/pdf.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/browser_rendering/pdf_create_params.py">params</a>) -> BinaryAPIResponse</code>

## Scrape

Types:

```python
from cloudflare.types.browser_rendering import ScrapeCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/browser-rendering/scrape">client.browser_rendering.scrape.<a href="./src/cloudflare/resources/browser_rendering/scrape.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/browser_rendering/scrape_create_params.py">params</a>) -> <a href="./src/cloudflare/types/browser_rendering/scrape_create_response.py">ScrapeCreateResponse</a></code>

## Screenshot

Types:

```python
from cloudflare.types.browser_rendering import ScreenshotCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/browser-rendering/screenshot">client.browser_rendering.screenshot.<a href="./src/cloudflare/resources/browser_rendering/screenshot.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/browser_rendering/screenshot_create_params.py">params</a>) -> <a href="./src/cloudflare/types/browser_rendering/screenshot_create_response.py">ScreenshotCreateResponse</a></code>

## Snapshot

Types:

```python
from cloudflare.types.browser_rendering import SnapshotCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/browser-rendering/snapshot">client.browser_rendering.snapshot.<a href="./src/cloudflare/resources/browser_rendering/snapshot.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/browser_rendering/snapshot_create_params.py">params</a>) -> <a href="./src/cloudflare/types/browser_rendering/snapshot_create_response.py">Optional[SnapshotCreateResponse]</a></code>

## Json

Types:

```python
from cloudflare.types.browser_rendering import JsonCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/browser-rendering/json">client.browser_rendering.json.<a href="./src/cloudflare/resources/browser_rendering/json.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/browser_rendering/json_create_params.py">params</a>) -> <a href="./src/cloudflare/types/browser_rendering/json_create_response.py">JsonCreateResponse</a></code>

## Links

Types:

```python
from cloudflare.types.browser_rendering import LinkCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/browser-rendering/links">client.browser_rendering.links.<a href="./src/cloudflare/resources/browser_rendering/links.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/browser_rendering/link_create_params.py">params</a>) -> <a href="./src/cloudflare/types/browser_rendering/link_create_response.py">LinkCreateResponse</a></code>

## Markdown

Types:

```python
from cloudflare.types.browser_rendering import MarkdownCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/browser-rendering/markdown">client.browser_rendering.markdown.<a href="./src/cloudflare/resources/browser_rendering/markdown.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/browser_rendering/markdown_create_params.py">params</a>) -> <a href="./src/cloudflare/types/browser_rendering/markdown_create_response.py">str</a></code>

## Crawl

Types:

```python
from cloudflare.types.browser_rendering import (
    CrawlCreateResponse,
    CrawlDeleteResponse,
    CrawlGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/browser-rendering/crawl">client.browser_rendering.crawl.<a href="./src/cloudflare/resources/browser_rendering/crawl.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/browser_rendering/crawl_create_params.py">params</a>) -> <a href="./src/cloudflare/types/browser_rendering/crawl_create_response.py">str</a></code>
- <code title="delete /accounts/{account_id}/browser-rendering/crawl/{job_id}">client.browser_rendering.crawl.<a href="./src/cloudflare/resources/browser_rendering/crawl.py">delete</a>(job_id, \*, account_id) -> <a href="./src/cloudflare/types/browser_rendering/crawl_delete_response.py">CrawlDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/browser-rendering/crawl/{job_id}">client.browser_rendering.crawl.<a href="./src/cloudflare/resources/browser_rendering/crawl.py">get</a>(job_id, \*, account_id, \*\*<a href="src/cloudflare/types/browser_rendering/crawl_get_params.py">params</a>) -> <a href="./src/cloudflare/types/browser_rendering/crawl_get_response.py">CrawlGetResponse</a></code>

## Devtools

### Session

Types:

```python
from cloudflare.types.browser_rendering.devtools import SessionListResponse, SessionGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/browser-rendering/devtools/session">client.browser_rendering.devtools.session.<a href="./src/cloudflare/resources/browser_rendering/devtools/session.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/browser_rendering/devtools/session_list_params.py">params</a>) -> <a href="./src/cloudflare/types/browser_rendering/devtools/session_list_response.py">SessionListResponse</a></code>
- <code title="get /accounts/{account_id}/browser-rendering/devtools/session/{session_id}">client.browser_rendering.devtools.session.<a href="./src/cloudflare/resources/browser_rendering/devtools/session.py">get</a>(session_id, \*, account_id) -> <a href="./src/cloudflare/types/browser_rendering/devtools/session_get_response.py">Optional[SessionGetResponse]</a></code>

### Browser

Types:

```python
from cloudflare.types.browser_rendering.devtools import (
    BrowserCreateResponse,
    BrowserDeleteResponse,
    BrowserProtocolResponse,
    BrowserVersionResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/browser-rendering/devtools/browser">client.browser_rendering.devtools.browser.<a href="./src/cloudflare/resources/browser_rendering/devtools/browser/browser.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/browser_rendering/devtools/browser_create_params.py">params</a>) -> <a href="./src/cloudflare/types/browser_rendering/devtools/browser_create_response.py">BrowserCreateResponse</a></code>
- <code title="delete /accounts/{account_id}/browser-rendering/devtools/browser/{session_id}">client.browser_rendering.devtools.browser.<a href="./src/cloudflare/resources/browser_rendering/devtools/browser/browser.py">delete</a>(session_id, \*, account_id) -> <a href="./src/cloudflare/types/browser_rendering/devtools/browser_delete_response.py">BrowserDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/browser-rendering/devtools/browser/{session_id}">client.browser_rendering.devtools.browser.<a href="./src/cloudflare/resources/browser_rendering/devtools/browser/browser.py">connect</a>(session_id, \*, account_id, \*\*<a href="src/cloudflare/types/browser_rendering/devtools/browser_connect_params.py">params</a>) -> None</code>
- <code title="get /accounts/{account_id}/browser-rendering/devtools/browser">client.browser_rendering.devtools.browser.<a href="./src/cloudflare/resources/browser_rendering/devtools/browser/browser.py">launch</a>(\*, account_id, \*\*<a href="src/cloudflare/types/browser_rendering/devtools/browser_launch_params.py">params</a>) -> None</code>
- <code title="get /accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/json/protocol">client.browser_rendering.devtools.browser.<a href="./src/cloudflare/resources/browser_rendering/devtools/browser/browser.py">protocol</a>(session_id, \*, account_id) -> <a href="./src/cloudflare/types/browser_rendering/devtools/browser_protocol_response.py">BrowserProtocolResponse</a></code>
- <code title="get /accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/json/version">client.browser_rendering.devtools.browser.<a href="./src/cloudflare/resources/browser_rendering/devtools/browser/browser.py">version</a>(session_id, \*, account_id) -> <a href="./src/cloudflare/types/browser_rendering/devtools/browser_version_response.py">BrowserVersionResponse</a></code>

#### Page

Methods:

- <code title="get /accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/page/{target_id}">client.browser_rendering.devtools.browser.page.<a href="./src/cloudflare/resources/browser_rendering/devtools/browser/page.py">get</a>(target_id, \*, account_id, session_id) -> None</code>

#### Targets

Types:

```python
from cloudflare.types.browser_rendering.devtools.browser import (
    TargetCreateResponse,
    TargetListResponse,
    TargetActivateResponse,
    TargetGetResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/json/new">client.browser_rendering.devtools.browser.targets.<a href="./src/cloudflare/resources/browser_rendering/devtools/browser/targets.py">create</a>(session_id, \*, account_id, \*\*<a href="src/cloudflare/types/browser_rendering/devtools/browser/target_create_params.py">params</a>) -> <a href="./src/cloudflare/types/browser_rendering/devtools/browser/target_create_response.py">TargetCreateResponse</a></code>
- <code title="get /accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/json/list">client.browser_rendering.devtools.browser.targets.<a href="./src/cloudflare/resources/browser_rendering/devtools/browser/targets.py">list</a>(session_id, \*, account_id) -> <a href="./src/cloudflare/types/browser_rendering/devtools/browser/target_list_response.py">TargetListResponse</a></code>
- <code title="get /accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/json/activate/{target_id}">client.browser_rendering.devtools.browser.targets.<a href="./src/cloudflare/resources/browser_rendering/devtools/browser/targets.py">activate</a>(target_id, \*, account_id, session_id) -> <a href="./src/cloudflare/types/browser_rendering/devtools/browser/target_activate_response.py">TargetActivateResponse</a></code>
- <code title="get /accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/json/list/{target_id}">client.browser_rendering.devtools.browser.targets.<a href="./src/cloudflare/resources/browser_rendering/devtools/browser/targets.py">get</a>(target_id, \*, account_id, session_id) -> <a href="./src/cloudflare/types/browser_rendering/devtools/browser/target_get_response.py">TargetGetResponse</a></code>
