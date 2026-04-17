# Intel

## ASN

Methods:

- <code title="get /accounts/{account_id}/intel/asn/{asn}">client.intel.asn.<a href="./src/cloudflare/resources/intel/asn/asn.py">get</a>(asn, \*, account_id) -> <a href="./src/cloudflare/types/shared/asn.py">Optional[ASN]</a></code>

### Subnets

Types:

```python
from cloudflare.types.intel.asn import SubnetGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/intel/asn/{asn}/subnets">client.intel.asn.subnets.<a href="./src/cloudflare/resources/intel/asn/subnets.py">get</a>(asn, \*, account_id) -> <a href="./src/cloudflare/types/intel/asn/subnet_get_response.py">SubnetGetResponse</a></code>

## DNS

Types:

```python
from cloudflare.types.intel import DNS
```

Methods:

- <code title="get /accounts/{account_id}/intel/dns">client.intel.dns.<a href="./src/cloudflare/resources/intel/dns.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/intel/dns_list_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/dns.py">SyncV4PagePagination[Optional[DNS]]</a></code>

## Domains

Types:

```python
from cloudflare.types.intel import Domain
```

Methods:

- <code title="get /accounts/{account_id}/intel/domain">client.intel.domains.<a href="./src/cloudflare/resources/intel/domains/domains.py">get</a>(\*, account_id, \*\*<a href="src/cloudflare/types/intel/domain_get_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/domain.py">Optional[Domain]</a></code>

### Bulks

Types:

```python
from cloudflare.types.intel.domains import BulkGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/intel/domain/bulk">client.intel.domains.bulks.<a href="./src/cloudflare/resources/intel/domains/bulks.py">get</a>(\*, account_id, \*\*<a href="src/cloudflare/types/intel/domains/bulk_get_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/domains/bulk_get_response.py">Optional[BulkGetResponse]</a></code>

## DomainHistory

Types:

```python
from cloudflare.types.intel import DomainHistory, DomainHistoryGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/intel/domain-history">client.intel.domain_history.<a href="./src/cloudflare/resources/intel/domain_history.py">get</a>(\*, account_id, \*\*<a href="src/cloudflare/types/intel/domain_history_get_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/domain_history_get_response.py">Optional[DomainHistoryGetResponse]</a></code>

## IPs

Types:

```python
from cloudflare.types.intel import IP, IPGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/intel/ip">client.intel.ips.<a href="./src/cloudflare/resources/intel/ips.py">get</a>(\*, account_id, \*\*<a href="src/cloudflare/types/intel/ip_get_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/ip_get_response.py">Optional[IPGetResponse]</a></code>

## IPLists

Types:

```python
from cloudflare.types.intel import IPList
```

## Miscategorizations

Types:

```python
from cloudflare.types.intel import MiscategorizationCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/intel/miscategorization">client.intel.miscategorizations.<a href="./src/cloudflare/resources/intel/miscategorizations.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/intel/miscategorization_create_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/miscategorization_create_response.py">MiscategorizationCreateResponse</a></code>

## Whois

Types:

```python
from cloudflare.types.intel import Whois, WhoisGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/intel/whois">client.intel.whois.<a href="./src/cloudflare/resources/intel/whois.py">get</a>(\*, account_id, \*\*<a href="src/cloudflare/types/intel/whois_get_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/whois_get_response.py">Optional[WhoisGetResponse]</a></code>

## IndicatorFeeds

Types:

```python
from cloudflare.types.intel import (
    IndicatorFeedCreateResponse,
    IndicatorFeedUpdateResponse,
    IndicatorFeedListResponse,
    IndicatorFeedDataResponse,
    IndicatorFeedGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/intel/indicator-feeds">client.intel.indicator_feeds.<a href="./src/cloudflare/resources/intel/indicator_feeds/indicator_feeds.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/intel/indicator_feed_create_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/indicator_feed_create_response.py">Optional[IndicatorFeedCreateResponse]</a></code>
- <code title="put /accounts/{account_id}/intel/indicator-feeds/{feed_id}">client.intel.indicator_feeds.<a href="./src/cloudflare/resources/intel/indicator_feeds/indicator_feeds.py">update</a>(feed_id, \*, account_id, \*\*<a href="src/cloudflare/types/intel/indicator_feed_update_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/indicator_feed_update_response.py">Optional[IndicatorFeedUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/intel/indicator-feeds">client.intel.indicator_feeds.<a href="./src/cloudflare/resources/intel/indicator_feeds/indicator_feeds.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/intel/indicator_feed_list_response.py">SyncSinglePage[IndicatorFeedListResponse]</a></code>
- <code title="get /accounts/{account_id}/intel/indicator-feeds/{feed_id}/data">client.intel.indicator_feeds.<a href="./src/cloudflare/resources/intel/indicator_feeds/indicator_feeds.py">data</a>(feed_id, \*, account_id) -> str</code>
- <code title="get /accounts/{account_id}/intel/indicator-feeds/{feed_id}">client.intel.indicator_feeds.<a href="./src/cloudflare/resources/intel/indicator_feeds/indicator_feeds.py">get</a>(feed_id, \*, account_id) -> <a href="./src/cloudflare/types/intel/indicator_feed_get_response.py">Optional[IndicatorFeedGetResponse]</a></code>

### Snapshots

Types:

```python
from cloudflare.types.intel.indicator_feeds import SnapshotUpdateResponse
```

Methods:

- <code title="put /accounts/{account_id}/intel/indicator-feeds/{feed_id}/snapshot">client.intel.indicator_feeds.snapshots.<a href="./src/cloudflare/resources/intel/indicator_feeds/snapshots.py">update</a>(feed_id, \*, account_id, \*\*<a href="src/cloudflare/types/intel/indicator_feeds/snapshot_update_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/indicator_feeds/snapshot_update_response.py">Optional[SnapshotUpdateResponse]</a></code>

### Permissions

Types:

```python
from cloudflare.types.intel.indicator_feeds import (
    PermissionCreateResponse,
    PermissionListResponse,
    PermissionDeleteResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/intel/indicator-feeds/permissions/add">client.intel.indicator_feeds.permissions.<a href="./src/cloudflare/resources/intel/indicator_feeds/permissions.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/intel/indicator_feeds/permission_create_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/indicator_feeds/permission_create_response.py">Optional[PermissionCreateResponse]</a></code>
- <code title="get /accounts/{account_id}/intel/indicator-feeds/permissions/view">client.intel.indicator_feeds.permissions.<a href="./src/cloudflare/resources/intel/indicator_feeds/permissions.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/intel/indicator_feeds/permission_list_response.py">Optional[PermissionListResponse]</a></code>
- <code title="put /accounts/{account_id}/intel/indicator-feeds/permissions/remove">client.intel.indicator_feeds.permissions.<a href="./src/cloudflare/resources/intel/indicator_feeds/permissions.py">delete</a>(\*, account_id, \*\*<a href="src/cloudflare/types/intel/indicator_feeds/permission_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/indicator_feeds/permission_delete_response.py">Optional[PermissionDeleteResponse]</a></code>

## Sinkholes

Types:

```python
from cloudflare.types.intel import Sinkhole
```

Methods:

- <code title="get /accounts/{account_id}/intel/sinkholes">client.intel.sinkholes.<a href="./src/cloudflare/resources/intel/sinkholes.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/intel/sinkhole.py">SyncSinglePage[Sinkhole]</a></code>

## AttackSurfaceReport

### IssueTypes

Types:

```python
from cloudflare.types.intel.attack_surface_report import IssueTypeGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/intel/attack-surface-report/issue-types">client.intel.attack_surface_report.issue_types.<a href="./src/cloudflare/resources/intel/attack_surface_report/issue_types.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/intel/attack_surface_report/issue_type_get_response.py">SyncSinglePage[IssueTypeGetResponse]</a></code>

### Issues

Types:

```python
from cloudflare.types.intel.attack_surface_report import (
    IssueType,
    SeverityQueryParam,
    IssueListResponse,
    IssueClassResponse,
    IssueDismissResponse,
    IssueSeverityResponse,
    IssueTypeResponse,
)
```

Methods:

- <code title="get /accounts/{account_id}/intel/attack-surface-report/issues">client.intel.attack_surface_report.issues.<a href="./src/cloudflare/resources/intel/attack_surface_report/issues.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/intel/attack_surface_report/issue_list_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/attack_surface_report/issue_list_response.py">SyncV4PagePagination[Optional[IssueListResponse]]</a></code>
- <code title="get /accounts/{account_id}/intel/attack-surface-report/issues/class">client.intel.attack*surface_report.issues.<a href="./src/cloudflare/resources/intel/attack_surface_report/issues.py">class*</a>(\*, account_id, \*\*<a href="src/cloudflare/types/intel/attack_surface_report/issue_class_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/attack_surface_report/issue_class_response.py">Optional[IssueClassResponse]</a></code>
- <code title="put /accounts/{account_id}/intel/attack-surface-report/{issue_id}/dismiss">client.intel.attack_surface_report.issues.<a href="./src/cloudflare/resources/intel/attack_surface_report/issues.py">dismiss</a>(issue_id, \*, account_id, \*\*<a href="src/cloudflare/types/intel/attack_surface_report/issue_dismiss_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/attack_surface_report/issue_dismiss_response.py">IssueDismissResponse</a></code>
- <code title="get /accounts/{account_id}/intel/attack-surface-report/issues/severity">client.intel.attack_surface_report.issues.<a href="./src/cloudflare/resources/intel/attack_surface_report/issues.py">severity</a>(\*, account_id, \*\*<a href="src/cloudflare/types/intel/attack_surface_report/issue_severity_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/attack_surface_report/issue_severity_response.py">Optional[IssueSeverityResponse]</a></code>
- <code title="get /accounts/{account_id}/intel/attack-surface-report/issues/type">client.intel.attack_surface_report.issues.<a href="./src/cloudflare/resources/intel/attack_surface_report/issues.py">type</a>(\*, account_id, \*\*<a href="src/cloudflare/types/intel/attack_surface_report/issue_type_params.py">params</a>) -> <a href="./src/cloudflare/types/intel/attack_surface_report/issue_type_response.py">Optional[IssueTypeResponse]</a></code>
