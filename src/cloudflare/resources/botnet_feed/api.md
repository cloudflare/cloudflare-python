# BotnetFeed

## ASN

Types:

```python
from cloudflare.types.botnet_feed import ASNDayReportResponse, ASNFullReportResponse
```

Methods:

- <code title="get /accounts/{account_id}/botnet_feed/asn/{asn_id}/day_report">client.botnet_feed.asn.<a href="./src/cloudflare/resources/botnet_feed/asn.py">day_report</a>(asn_id, \*, account_id, \*\*<a href="src/cloudflare/types/botnet_feed/asn_day_report_params.py">params</a>) -> <a href="./src/cloudflare/types/botnet_feed/asn_day_report_response.py">Optional[ASNDayReportResponse]</a></code>
- <code title="get /accounts/{account_id}/botnet_feed/asn/{asn_id}/full_report">client.botnet_feed.asn.<a href="./src/cloudflare/resources/botnet_feed/asn.py">full_report</a>(asn_id, \*, account_id) -> <a href="./src/cloudflare/types/botnet_feed/asn_full_report_response.py">Optional[ASNFullReportResponse]</a></code>

## Configs

### ASN

Types:

```python
from cloudflare.types.botnet_feed.configs import ASNDeleteResponse, ASNGetResponse
```

Methods:

- <code title="delete /accounts/{account_id}/botnet_feed/configs/asn/{asn_id}">client.botnet_feed.configs.asn.<a href="./src/cloudflare/resources/botnet_feed/configs/asn.py">delete</a>(asn_id, \*, account_id) -> <a href="./src/cloudflare/types/botnet_feed/configs/asn_delete_response.py">Optional[ASNDeleteResponse]</a></code>
- <code title="get /accounts/{account_id}/botnet_feed/configs/asn">client.botnet_feed.configs.asn.<a href="./src/cloudflare/resources/botnet_feed/configs/asn.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/botnet_feed/configs/asn_get_response.py">Optional[ASNGetResponse]</a></code>
