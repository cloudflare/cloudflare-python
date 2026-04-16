# DNSFirewall

Types:

```python
from cloudflare.types.dns_firewall import (
    AttackMitigation,
    FirewallIPs,
    UpstreamIPs,
    DNSFirewallCreateResponse,
    DNSFirewallListResponse,
    DNSFirewallDeleteResponse,
    DNSFirewallEditResponse,
    DNSFirewallGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/dns_firewall">client.dns_firewall.<a href="./src/cloudflare/resources/dns_firewall/dns_firewall.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/dns_firewall/dns_firewall_create_params.py">params</a>) -> <a href="./src/cloudflare/types/dns_firewall/dns_firewall_create_response.py">Optional[DNSFirewallCreateResponse]</a></code>
- <code title="get /accounts/{account_id}/dns_firewall">client.dns_firewall.<a href="./src/cloudflare/resources/dns_firewall/dns_firewall.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/dns_firewall/dns_firewall_list_params.py">params</a>) -> <a href="./src/cloudflare/types/dns_firewall/dns_firewall_list_response.py">SyncV4PagePaginationArray[DNSFirewallListResponse]</a></code>
- <code title="delete /accounts/{account_id}/dns_firewall/{dns_firewall_id}">client.dns_firewall.<a href="./src/cloudflare/resources/dns_firewall/dns_firewall.py">delete</a>(dns_firewall_id, \*, account_id) -> <a href="./src/cloudflare/types/dns_firewall/dns_firewall_delete_response.py">Optional[DNSFirewallDeleteResponse]</a></code>
- <code title="patch /accounts/{account_id}/dns_firewall/{dns_firewall_id}">client.dns_firewall.<a href="./src/cloudflare/resources/dns_firewall/dns_firewall.py">edit</a>(dns_firewall_id, \*, account_id, \*\*<a href="src/cloudflare/types/dns_firewall/dns_firewall_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/dns_firewall/dns_firewall_edit_response.py">Optional[DNSFirewallEditResponse]</a></code>
- <code title="get /accounts/{account_id}/dns_firewall/{dns_firewall_id}">client.dns_firewall.<a href="./src/cloudflare/resources/dns_firewall/dns_firewall.py">get</a>(dns_firewall_id, \*, account_id) -> <a href="./src/cloudflare/types/dns_firewall/dns_firewall_get_response.py">Optional[DNSFirewallGetResponse]</a></code>

## Analytics

### Reports

Methods:

- <code title="get /accounts/{account_id}/dns_firewall/{dns_firewall_id}/dns_analytics/report">client.dns_firewall.analytics.reports.<a href="./src/cloudflare/resources/dns_firewall/analytics/reports/reports.py">get</a>(dns_firewall_id, \*, account_id, \*\*<a href="src/cloudflare/types/dns_firewall/analytics/report_get_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/analytics/report.py">Optional[Report]</a></code>

#### Bytimes

Methods:

- <code title="get /accounts/{account_id}/dns_firewall/{dns_firewall_id}/dns_analytics/report/bytime">client.dns_firewall.analytics.reports.bytimes.<a href="./src/cloudflare/resources/dns_firewall/analytics/reports/bytimes.py">get</a>(dns_firewall_id, \*, account_id, \*\*<a href="src/cloudflare/types/dns_firewall/analytics/reports/bytime_get_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/analytics/reports/by_time.py">Optional[ByTime]</a></code>

## ReverseDNS

Types:

```python
from cloudflare.types.dns_firewall import ReverseDNSEditResponse, ReverseDNSGetResponse
```

Methods:

- <code title="patch /accounts/{account_id}/dns_firewall/{dns_firewall_id}/reverse_dns">client.dns_firewall.reverse_dns.<a href="./src/cloudflare/resources/dns_firewall/reverse_dns.py">edit</a>(dns_firewall_id, \*, account_id, \*\*<a href="src/cloudflare/types/dns_firewall/reverse_dns_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/dns_firewall/reverse_dns_edit_response.py">Optional[ReverseDNSEditResponse]</a></code>
- <code title="get /accounts/{account_id}/dns_firewall/{dns_firewall_id}/reverse_dns">client.dns_firewall.reverse_dns.<a href="./src/cloudflare/resources/dns_firewall/reverse_dns.py">get</a>(dns_firewall_id, \*, account_id) -> <a href="./src/cloudflare/types/dns_firewall/reverse_dns_get_response.py">Optional[ReverseDNSGetResponse]</a></code>
