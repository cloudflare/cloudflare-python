# EmailRouting

Types:

```python
from cloudflare.types.email_routing import Settings
```

Methods:

- <code title="post /zones/{zone_id}/email/routing/disable">client.email_routing.<a href="./src/cloudflare/resources/email_routing/email_routing.py">disable</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/email_routing/email_routing_disable_params.py">params</a>) -> <a href="./src/cloudflare/types/email_routing/settings.py">Optional[Settings]</a></code>
- <code title="post /zones/{zone_id}/email/routing/enable">client.email_routing.<a href="./src/cloudflare/resources/email_routing/email_routing.py">enable</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/email_routing/email_routing_enable_params.py">params</a>) -> <a href="./src/cloudflare/types/email_routing/settings.py">Optional[Settings]</a></code>
- <code title="get /zones/{zone_id}/email/routing">client.email_routing.<a href="./src/cloudflare/resources/email_routing/email_routing.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/email_routing/settings.py">Optional[Settings]</a></code>

## DNS

Types:

```python
from cloudflare.types.email_routing import DNSRecord, DNSGetResponse
```

Methods:

- <code title="post /zones/{zone_id}/email/routing/dns">client.email_routing.dns.<a href="./src/cloudflare/resources/email_routing/dns.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/email_routing/dns_create_params.py">params</a>) -> <a href="./src/cloudflare/types/email_routing/settings.py">Optional[Settings]</a></code>
- <code title="delete /zones/{zone_id}/email/routing/dns">client.email_routing.dns.<a href="./src/cloudflare/resources/email_routing/dns.py">delete</a>(\*, zone_id) -> <a href="./src/cloudflare/types/email_routing/dns_record.py">SyncSinglePage[DNSRecord]</a></code>
- <code title="patch /zones/{zone_id}/email/routing/dns">client.email_routing.dns.<a href="./src/cloudflare/resources/email_routing/dns.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/email_routing/dns_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/email_routing/settings.py">Optional[Settings]</a></code>
- <code title="get /zones/{zone_id}/email/routing/dns">client.email_routing.dns.<a href="./src/cloudflare/resources/email_routing/dns.py">get</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/email_routing/dns_get_params.py">params</a>) -> <a href="./src/cloudflare/types/email_routing/dns_get_response.py">DNSGetResponse</a></code>

## Rules

Types:

```python
from cloudflare.types.email_routing import Action, EmailRoutingRule, Matcher
```

Methods:

- <code title="post /zones/{zone_id}/email/routing/rules">client.email_routing.rules.<a href="./src/cloudflare/resources/email_routing/rules/rules.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/email_routing/rule_create_params.py">params</a>) -> <a href="./src/cloudflare/types/email_routing/email_routing_rule.py">Optional[EmailRoutingRule]</a></code>
- <code title="put /zones/{zone_id}/email/routing/rules/{rule_identifier}">client.email_routing.rules.<a href="./src/cloudflare/resources/email_routing/rules/rules.py">update</a>(rule_identifier, \*, zone_id, \*\*<a href="src/cloudflare/types/email_routing/rule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/email_routing/email_routing_rule.py">Optional[EmailRoutingRule]</a></code>
- <code title="get /zones/{zone_id}/email/routing/rules">client.email_routing.rules.<a href="./src/cloudflare/resources/email_routing/rules/rules.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/email_routing/rule_list_params.py">params</a>) -> <a href="./src/cloudflare/types/email_routing/email_routing_rule.py">SyncV4PagePaginationArray[EmailRoutingRule]</a></code>
- <code title="delete /zones/{zone_id}/email/routing/rules/{rule_identifier}">client.email_routing.rules.<a href="./src/cloudflare/resources/email_routing/rules/rules.py">delete</a>(rule_identifier, \*, zone_id) -> <a href="./src/cloudflare/types/email_routing/email_routing_rule.py">Optional[EmailRoutingRule]</a></code>
- <code title="get /zones/{zone_id}/email/routing/rules/{rule_identifier}">client.email_routing.rules.<a href="./src/cloudflare/resources/email_routing/rules/rules.py">get</a>(rule_identifier, \*, zone_id) -> <a href="./src/cloudflare/types/email_routing/email_routing_rule.py">Optional[EmailRoutingRule]</a></code>

### CatchAlls

Types:

```python
from cloudflare.types.email_routing.rules import (
    CatchAllAction,
    CatchAllMatcher,
    CatchAllUpdateResponse,
    CatchAllGetResponse,
)
```

Methods:

- <code title="put /zones/{zone_id}/email/routing/rules/catch_all">client.email_routing.rules.catch_alls.<a href="./src/cloudflare/resources/email_routing/rules/catch_alls.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/email_routing/rules/catch_all_update_params.py">params</a>) -> <a href="./src/cloudflare/types/email_routing/rules/catch_all_update_response.py">Optional[CatchAllUpdateResponse]</a></code>
- <code title="get /zones/{zone_id}/email/routing/rules/catch_all">client.email_routing.rules.catch_alls.<a href="./src/cloudflare/resources/email_routing/rules/catch_alls.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/email_routing/rules/catch_all_get_response.py">Optional[CatchAllGetResponse]</a></code>

## Addresses

Types:

```python
from cloudflare.types.email_routing import Address
```

Methods:

- <code title="post /accounts/{account_id}/email/routing/addresses">client.email_routing.addresses.<a href="./src/cloudflare/resources/email_routing/addresses.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/email_routing/address_create_params.py">params</a>) -> <a href="./src/cloudflare/types/email_routing/address.py">Optional[Address]</a></code>
- <code title="get /accounts/{account_id}/email/routing/addresses">client.email_routing.addresses.<a href="./src/cloudflare/resources/email_routing/addresses.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/email_routing/address_list_params.py">params</a>) -> <a href="./src/cloudflare/types/email_routing/address.py">SyncV4PagePaginationArray[Address]</a></code>
- <code title="delete /accounts/{account_id}/email/routing/addresses/{destination_address_identifier}">client.email_routing.addresses.<a href="./src/cloudflare/resources/email_routing/addresses.py">delete</a>(destination_address_identifier, \*, account_id) -> <a href="./src/cloudflare/types/email_routing/address.py">Optional[Address]</a></code>
- <code title="get /accounts/{account_id}/email/routing/addresses/{destination_address_identifier}">client.email_routing.addresses.<a href="./src/cloudflare/resources/email_routing/addresses.py">get</a>(destination_address_identifier, \*, account_id) -> <a href="./src/cloudflare/types/email_routing/address.py">Optional[Address]</a></code>
