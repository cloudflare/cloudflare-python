# AbuseReports

Types:

```python
from cloudflare.types.abuse_reports import (
    AbuseReportCreateResponse,
    AbuseReportListResponse,
    AbuseReportGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/abuse-reports/{report_param}">client.abuse_reports.<a href="./src/cloudflare/resources/abuse_reports/abuse_reports.py">create</a>(report_param, \*, account_id, \*\*<a href="src/cloudflare/types/abuse_reports/abuse_report_create_params.py">params</a>) -> <a href="./src/cloudflare/types/abuse_reports/abuse_report_create_response.py">str</a></code>
- <code title="get /accounts/{account_id}/abuse-reports">client.abuse_reports.<a href="./src/cloudflare/resources/abuse_reports/abuse_reports.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/abuse_reports/abuse_report_list_params.py">params</a>) -> <a href="./src/cloudflare/types/abuse_reports/abuse_report_list_response.py">SyncV4PagePagination[Optional[AbuseReportListResponse]]</a></code>
- <code title="get /accounts/{account_id}/abuse-reports/{report_param}">client.abuse_reports.<a href="./src/cloudflare/resources/abuse_reports/abuse_reports.py">get</a>(report_param, \*, account_id) -> <a href="./src/cloudflare/types/abuse_reports/abuse_report_get_response.py">AbuseReportGetResponse</a></code>

## Mitigations

Types:

```python
from cloudflare.types.abuse_reports import MitigationListResponse, MitigationReviewResponse
```

Methods:

- <code title="get /accounts/{account_id}/abuse-reports/{report_id}/mitigations">client.abuse_reports.mitigations.<a href="./src/cloudflare/resources/abuse_reports/mitigations.py">list</a>(report_id, \*, account_id, \*\*<a href="src/cloudflare/types/abuse_reports/mitigation_list_params.py">params</a>) -> <a href="./src/cloudflare/types/abuse_reports/mitigation_list_response.py">SyncV4PagePagination[Optional[MitigationListResponse]]</a></code>
- <code title="post /accounts/{account_id}/abuse-reports/{report_id}/mitigations/appeal">client.abuse_reports.mitigations.<a href="./src/cloudflare/resources/abuse_reports/mitigations.py">review</a>(report_id, \*, account_id, \*\*<a href="src/cloudflare/types/abuse_reports/mitigation_review_params.py">params</a>) -> <a href="./src/cloudflare/types/abuse_reports/mitigation_review_response.py">SyncSinglePage[MitigationReviewResponse]</a></code>
