# EmailSending

Types:

```python
from cloudflare.types.email_sending import EmailSendingSendResponse, EmailSendingSendRawResponse
```

Methods:

- <code title="post /accounts/{account_id}/email/sending/send">client.email_sending.<a href="./src/cloudflare/resources/email_sending/email_sending.py">send</a>(\*, account_id, \*\*<a href="src/cloudflare/types/email_sending/email_sending_send_params.py">params</a>) -> <a href="./src/cloudflare/types/email_sending/email_sending_send_response.py">EmailSendingSendResponse</a></code>
- <code title="post /accounts/{account_id}/email/sending/send_raw">client.email_sending.<a href="./src/cloudflare/resources/email_sending/email_sending.py">send_raw</a>(\*, account_id, \*\*<a href="src/cloudflare/types/email_sending/email_sending_send_raw_params.py">params</a>) -> <a href="./src/cloudflare/types/email_sending/email_sending_send_raw_response.py">EmailSendingSendRawResponse</a></code>

## Suppressions

Types:

```python
from cloudflare.types.email_sending import (
    SuppressionCreateResponse,
    SuppressionListResponse,
    SuppressionDeleteResponse,
    SuppressionEditResponse,
    SuppressionGetResponse,
    SuppressionImportResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/email/sending/suppressions">client.email_sending.suppressions.<a href="./src/cloudflare/resources/email_sending/suppressions.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/email_sending/suppression_create_params.py">params</a>) -> <a href="./src/cloudflare/types/email_sending/suppression_create_response.py">SuppressionCreateResponse</a></code>
- <code title="get /accounts/{account_id}/email/sending/suppressions">client.email_sending.suppressions.<a href="./src/cloudflare/resources/email_sending/suppressions.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/email_sending/suppression_list_params.py">params</a>) -> <a href="./src/cloudflare/types/email_sending/suppression_list_response.py">SyncCursorPagination[SuppressionListResponse]</a></code>
- <code title="delete /accounts/{account_id}/email/sending/suppressions/{suppression_id}">client.email_sending.suppressions.<a href="./src/cloudflare/resources/email_sending/suppressions.py">delete</a>(suppression_id, \*, account_id) -> <a href="./src/cloudflare/types/email_sending/suppression_delete_response.py">SuppressionDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/email/sending/suppressions/{suppression_id}">client.email_sending.suppressions.<a href="./src/cloudflare/resources/email_sending/suppressions.py">edit</a>(suppression_id, \*, account_id, \*\*<a href="src/cloudflare/types/email_sending/suppression_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/email_sending/suppression_edit_response.py">SuppressionEditResponse</a></code>
- <code title="get /accounts/{account_id}/email/sending/suppressions/{suppression_id}">client.email_sending.suppressions.<a href="./src/cloudflare/resources/email_sending/suppressions.py">get</a>(suppression_id, \*, account_id) -> <a href="./src/cloudflare/types/email_sending/suppression_get_response.py">SuppressionGetResponse</a></code>
- <code title="post /accounts/{account_id}/email/sending/suppressions/bulk">client.email*sending.suppressions.<a href="./src/cloudflare/resources/email_sending/suppressions.py">import*</a>(\*, account_id, \*\*<a href="src/cloudflare/types/email_sending/suppression_import_params.py">params</a>) -> <a href="./src/cloudflare/types/email_sending/suppression_import_response.py">SuppressionImportResponse</a></code>

## Subdomains

Types:

```python
from cloudflare.types.email_sending import (
    SubdomainCreateResponse,
    SubdomainListResponse,
    SubdomainDeleteResponse,
    SubdomainEditResponse,
    SubdomainGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/email/sending/subdomains">client.email_sending.subdomains.<a href="./src/cloudflare/resources/email_sending/subdomains/subdomains.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/email_sending/subdomain_create_params.py">params</a>) -> <a href="./src/cloudflare/types/email_sending/subdomain_create_response.py">Optional[SubdomainCreateResponse]</a></code>
- <code title="get /zones/{zone_id}/email/sending/subdomains">client.email_sending.subdomains.<a href="./src/cloudflare/resources/email_sending/subdomains/subdomains.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/email_sending/subdomain_list_response.py">SyncSinglePage[SubdomainListResponse]</a></code>
- <code title="delete /zones/{zone_id}/email/sending/subdomains/{subdomain_id}">client.email_sending.subdomains.<a href="./src/cloudflare/resources/email_sending/subdomains/subdomains.py">delete</a>(subdomain_id, \*, zone_id) -> <a href="./src/cloudflare/types/email_sending/subdomain_delete_response.py">SubdomainDeleteResponse</a></code>
- <code title="patch /zones/{zone_id}/email/sending/subdomains/{subdomain_id}">client.email_sending.subdomains.<a href="./src/cloudflare/resources/email_sending/subdomains/subdomains.py">edit</a>(subdomain_id, \*, zone_id, \*\*<a href="src/cloudflare/types/email_sending/subdomain_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/email_sending/subdomain_edit_response.py">Optional[SubdomainEditResponse]</a></code>
- <code title="get /zones/{zone_id}/email/sending/subdomains/{subdomain_id}">client.email_sending.subdomains.<a href="./src/cloudflare/resources/email_sending/subdomains/subdomains.py">get</a>(subdomain_id, \*, zone_id) -> <a href="./src/cloudflare/types/email_sending/subdomain_get_response.py">Optional[SubdomainGetResponse]</a></code>

### DNS

Methods:

- <code title="get /zones/{zone_id}/email/sending/subdomains/{subdomain_id}/dns">client.email_sending.subdomains.dns.<a href="./src/cloudflare/resources/email_sending/subdomains/dns.py">get</a>(subdomain_id, \*, zone_id) -> <a href="./src/cloudflare/types/email_routing/dns_record.py">SyncSinglePage[DNSRecord]</a></code>
