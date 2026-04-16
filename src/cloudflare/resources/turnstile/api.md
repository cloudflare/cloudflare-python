# Turnstile

## Widgets

Types:

```python
from cloudflare.types.turnstile import Widget, WidgetDomain, WidgetListResponse
```

Methods:

- <code title="post /accounts/{account_id}/challenges/widgets">client.turnstile.widgets.<a href="./src/cloudflare/resources/turnstile/widgets.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/turnstile/widget_create_params.py">params</a>) -> <a href="./src/cloudflare/types/turnstile/widget.py">Optional[Widget]</a></code>
- <code title="put /accounts/{account_id}/challenges/widgets/{sitekey}">client.turnstile.widgets.<a href="./src/cloudflare/resources/turnstile/widgets.py">update</a>(sitekey, \*, account_id, \*\*<a href="src/cloudflare/types/turnstile/widget_update_params.py">params</a>) -> <a href="./src/cloudflare/types/turnstile/widget.py">Optional[Widget]</a></code>
- <code title="get /accounts/{account_id}/challenges/widgets">client.turnstile.widgets.<a href="./src/cloudflare/resources/turnstile/widgets.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/turnstile/widget_list_params.py">params</a>) -> <a href="./src/cloudflare/types/turnstile/widget_list_response.py">SyncV4PagePaginationArray[WidgetListResponse]</a></code>
- <code title="delete /accounts/{account_id}/challenges/widgets/{sitekey}">client.turnstile.widgets.<a href="./src/cloudflare/resources/turnstile/widgets.py">delete</a>(sitekey, \*, account_id) -> <a href="./src/cloudflare/types/turnstile/widget.py">Optional[Widget]</a></code>
- <code title="get /accounts/{account_id}/challenges/widgets/{sitekey}">client.turnstile.widgets.<a href="./src/cloudflare/resources/turnstile/widgets.py">get</a>(sitekey, \*, account_id) -> <a href="./src/cloudflare/types/turnstile/widget.py">Optional[Widget]</a></code>
- <code title="post /accounts/{account_id}/challenges/widgets/{sitekey}/rotate_secret">client.turnstile.widgets.<a href="./src/cloudflare/resources/turnstile/widgets.py">rotate_secret</a>(sitekey, \*, account_id, \*\*<a href="src/cloudflare/types/turnstile/widget_rotate_secret_params.py">params</a>) -> <a href="./src/cloudflare/types/turnstile/widget.py">Optional[Widget]</a></code>
