# Alerting

## AvailableAlerts

Types:

```python
from cloudflare.types.alerting import AvailableAlertListResponse
```

Methods:

- <code title="get /accounts/{account_id}/alerting/v3/available_alerts">client.alerting.available_alerts.<a href="./src/cloudflare/resources/alerting/available_alerts.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/alerting/available_alert_list_response.py">Optional[AvailableAlertListResponse]</a></code>

## Destinations

### Eligible

Types:

```python
from cloudflare.types.alerting.destinations import EligibleGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/alerting/v3/destinations/eligible">client.alerting.destinations.eligible.<a href="./src/cloudflare/resources/alerting/destinations/eligible.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/alerting/destinations/eligible_get_response.py">Optional[EligibleGetResponse]</a></code>

### Pagerduty

Types:

```python
from cloudflare.types.alerting.destinations import (
    Pagerduty,
    PagerdutyCreateResponse,
    PagerdutyDeleteResponse,
    PagerdutyLinkResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/alerting/v3/destinations/pagerduty/connect">client.alerting.destinations.pagerduty.<a href="./src/cloudflare/resources/alerting/destinations/pagerduty.py">create</a>(\*, account_id) -> <a href="./src/cloudflare/types/alerting/destinations/pagerduty_create_response.py">Optional[PagerdutyCreateResponse]</a></code>
- <code title="delete /accounts/{account_id}/alerting/v3/destinations/pagerduty">client.alerting.destinations.pagerduty.<a href="./src/cloudflare/resources/alerting/destinations/pagerduty.py">delete</a>(\*, account_id) -> <a href="./src/cloudflare/types/alerting/destinations/pagerduty_delete_response.py">PagerdutyDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/alerting/v3/destinations/pagerduty">client.alerting.destinations.pagerduty.<a href="./src/cloudflare/resources/alerting/destinations/pagerduty.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/alerting/destinations/pagerduty.py">SyncSinglePage[Pagerduty]</a></code>
- <code title="get /accounts/{account_id}/alerting/v3/destinations/pagerduty/connect/{token_id}">client.alerting.destinations.pagerduty.<a href="./src/cloudflare/resources/alerting/destinations/pagerduty.py">link</a>(token_id, \*, account_id) -> <a href="./src/cloudflare/types/alerting/destinations/pagerduty_link_response.py">Optional[PagerdutyLinkResponse]</a></code>

### Webhooks

Types:

```python
from cloudflare.types.alerting.destinations import (
    Webhooks,
    WebhookCreateResponse,
    WebhookUpdateResponse,
    WebhookDeleteResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/alerting/v3/destinations/webhooks">client.alerting.destinations.webhooks.<a href="./src/cloudflare/resources/alerting/destinations/webhooks.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/alerting/destinations/webhook_create_params.py">params</a>) -> <a href="./src/cloudflare/types/alerting/destinations/webhook_create_response.py">Optional[WebhookCreateResponse]</a></code>
- <code title="put /accounts/{account_id}/alerting/v3/destinations/webhooks/{webhook_id}">client.alerting.destinations.webhooks.<a href="./src/cloudflare/resources/alerting/destinations/webhooks.py">update</a>(webhook_id, \*, account_id, \*\*<a href="src/cloudflare/types/alerting/destinations/webhook_update_params.py">params</a>) -> <a href="./src/cloudflare/types/alerting/destinations/webhook_update_response.py">Optional[WebhookUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/alerting/v3/destinations/webhooks">client.alerting.destinations.webhooks.<a href="./src/cloudflare/resources/alerting/destinations/webhooks.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/alerting/destinations/webhooks.py">SyncSinglePage[Webhooks]</a></code>
- <code title="delete /accounts/{account_id}/alerting/v3/destinations/webhooks/{webhook_id}">client.alerting.destinations.webhooks.<a href="./src/cloudflare/resources/alerting/destinations/webhooks.py">delete</a>(webhook_id, \*, account_id) -> <a href="./src/cloudflare/types/alerting/destinations/webhook_delete_response.py">WebhookDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/alerting/v3/destinations/webhooks/{webhook_id}">client.alerting.destinations.webhooks.<a href="./src/cloudflare/resources/alerting/destinations/webhooks.py">get</a>(webhook_id, \*, account_id) -> <a href="./src/cloudflare/types/alerting/destinations/webhooks.py">Optional[Webhooks]</a></code>

## History

Types:

```python
from cloudflare.types.alerting import History
```

Methods:

- <code title="get /accounts/{account_id}/alerting/v3/history">client.alerting.history.<a href="./src/cloudflare/resources/alerting/history.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/alerting/history_list_params.py">params</a>) -> <a href="./src/cloudflare/types/alerting/history.py">SyncV4PagePaginationArray[History]</a></code>

## Policies

Types:

```python
from cloudflare.types.alerting import (
    Mechanism,
    Policy,
    PolicyFilter,
    PolicyCreateResponse,
    PolicyUpdateResponse,
    PolicyDeleteResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/alerting/v3/policies">client.alerting.policies.<a href="./src/cloudflare/resources/alerting/policies.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/alerting/policy_create_params.py">params</a>) -> <a href="./src/cloudflare/types/alerting/policy_create_response.py">Optional[PolicyCreateResponse]</a></code>
- <code title="put /accounts/{account_id}/alerting/v3/policies/{policy_id}">client.alerting.policies.<a href="./src/cloudflare/resources/alerting/policies.py">update</a>(policy_id, \*, account_id, \*\*<a href="src/cloudflare/types/alerting/policy_update_params.py">params</a>) -> <a href="./src/cloudflare/types/alerting/policy_update_response.py">Optional[PolicyUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/alerting/v3/policies">client.alerting.policies.<a href="./src/cloudflare/resources/alerting/policies.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/alerting/policy.py">SyncSinglePage[Policy]</a></code>
- <code title="delete /accounts/{account_id}/alerting/v3/policies/{policy_id}">client.alerting.policies.<a href="./src/cloudflare/resources/alerting/policies.py">delete</a>(policy_id, \*, account_id) -> <a href="./src/cloudflare/types/alerting/policy_delete_response.py">PolicyDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/alerting/v3/policies/{policy_id}">client.alerting.policies.<a href="./src/cloudflare/resources/alerting/policies.py">get</a>(policy_id, \*, account_id) -> <a href="./src/cloudflare/types/alerting/policy.py">Optional[Policy]</a></code>

## Silences

Types:

```python
from cloudflare.types.alerting import (
    SilenceCreateResponse,
    SilenceUpdateResponse,
    SilenceListResponse,
    SilenceDeleteResponse,
    SilenceGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/alerting/v3/silences">client.alerting.silences.<a href="./src/cloudflare/resources/alerting/silences.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/alerting/silence_create_params.py">params</a>) -> <a href="./src/cloudflare/types/alerting/silence_create_response.py">SilenceCreateResponse</a></code>
- <code title="put /accounts/{account_id}/alerting/v3/silences">client.alerting.silences.<a href="./src/cloudflare/resources/alerting/silences.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/alerting/silence_update_params.py">params</a>) -> <a href="./src/cloudflare/types/alerting/silence_update_response.py">SyncSinglePage[SilenceUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/alerting/v3/silences">client.alerting.silences.<a href="./src/cloudflare/resources/alerting/silences.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/alerting/silence_list_response.py">SyncSinglePage[SilenceListResponse]</a></code>
- <code title="delete /accounts/{account_id}/alerting/v3/silences/{silence_id}">client.alerting.silences.<a href="./src/cloudflare/resources/alerting/silences.py">delete</a>(silence_id, \*, account_id) -> <a href="./src/cloudflare/types/alerting/silence_delete_response.py">SilenceDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/alerting/v3/silences/{silence_id}">client.alerting.silences.<a href="./src/cloudflare/resources/alerting/silences.py">get</a>(silence_id, \*, account_id) -> <a href="./src/cloudflare/types/alerting/silence_get_response.py">Optional[SilenceGetResponse]</a></code>
