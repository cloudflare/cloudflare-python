# EmailAuth

## DMARCReports

Types:

```python
from cloudflare.types.email_auth import DMARCReportEditResponse, DMARCReportGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/email/auth/dmarc-reports">client.email_auth.dmarc_reports.<a href="./src/cloudflare/resources/email_auth/dmarc_reports.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/email_auth/dmarc_report_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/email_auth/dmarc_report_edit_response.py">Optional[DMARCReportEditResponse]</a></code>
- <code title="get /zones/{zone_id}/email/auth/dmarc-reports">client.email_auth.dmarc_reports.<a href="./src/cloudflare/resources/email_auth/dmarc_reports.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/email_auth/dmarc_report_get_response.py">Optional[DMARCReportGetResponse]</a></code>

## SPF

### Inspect

Types:

```python
from cloudflare.types.email_auth.spf import InspectGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/email/auth/spf/inspect">client.email_auth.spf.inspect.<a href="./src/cloudflare/resources/email_auth/spf/inspect.py">get</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/email_auth/spf/inspect_get_params.py">params</a>) -> <a href="./src/cloudflare/types/email_auth/spf/inspect_get_response.py">Optional[InspectGetResponse]</a></code>
