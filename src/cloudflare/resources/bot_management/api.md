# BotManagement

Types:

```python
from cloudflare.types.bot_management import (
    BotFightModeConfiguration,
    SubscriptionConfiguration,
    SuperBotFightModeDefinitelyConfiguration,
    SuperBotFightModeLikelyConfiguration,
    BotManagementUpdateResponse,
    BotManagementGetResponse,
)
```

Methods:

- <code title="put /zones/{zone_id}/bot_management">client.bot_management.<a href="./src/cloudflare/resources/bot_management/bot_management.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/bot_management/bot_management_update_params.py">params</a>) -> <a href="./src/cloudflare/types/bot_management/bot_management_update_response.py">Optional[BotManagementUpdateResponse]</a></code>
- <code title="get /zones/{zone_id}/bot_management">client.bot_management.<a href="./src/cloudflare/resources/bot_management/bot_management.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/bot_management/bot_management_get_response.py">Optional[BotManagementGetResponse]</a></code>
