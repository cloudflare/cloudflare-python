# DNS

## DNSSEC

Types:

```python
from cloudflare.types.dns import DNSSEC, DNSSECDeleteResponse
```

Methods:

- <code title="delete /zones/{zone_id}/dnssec">client.dns.dnssec.<a href="./src/cloudflare/resources/dns/dnssec.py">delete</a>(\*, zone_id) -> <a href="./src/cloudflare/types/dns/dnssec_delete_response.py">str</a></code>
- <code title="patch /zones/{zone_id}/dnssec">client.dns.dnssec.<a href="./src/cloudflare/resources/dns/dnssec.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/dns/dnssec_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/dnssec.py">Optional[DNSSEC]</a></code>
- <code title="get /zones/{zone_id}/dnssec">client.dns.dnssec.<a href="./src/cloudflare/resources/dns/dnssec.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/dns/dnssec.py">Optional[DNSSEC]</a></code>

## Records

Types:

```python
from cloudflare.types.dns import (
    ARecord,
    AAAARecord,
    BatchPatch,
    BatchPut,
    CAARecord,
    CERTRecord,
    CNAMERecord,
    DNSKEYRecord,
    DSRecord,
    HTTPSRecord,
    LOCRecord,
    MXRecord,
    NAPTRRecord,
    NSRecord,
    PTRRecord,
    Record,
    RecordResponse,
    RecordTags,
    SMIMEARecord,
    SRVRecord,
    SSHFPRecord,
    SVCBRecord,
    TLSARecord,
    TTL,
    TXTRecord,
    URIRecord,
    RecordDeleteResponse,
    RecordBatchResponse,
    RecordExportResponse,
    RecordImportResponse,
    RecordScanResponse,
    RecordScanReviewResponse,
    RecordScanTriggerResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/dns_records">client.dns.records.<a href="./src/cloudflare/resources/dns/records.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/dns/record_create_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/record_response.py">Optional[RecordResponse]</a></code>
- <code title="put /zones/{zone_id}/dns_records/{dns_record_id}">client.dns.records.<a href="./src/cloudflare/resources/dns/records.py">update</a>(dns_record_id, \*, zone_id, \*\*<a href="src/cloudflare/types/dns/record_update_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/record_response.py">Optional[RecordResponse]</a></code>
- <code title="get /zones/{zone_id}/dns_records">client.dns.records.<a href="./src/cloudflare/resources/dns/records.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/dns/record_list_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/record_response.py">SyncV4PagePaginationArray[RecordResponse]</a></code>
- <code title="delete /zones/{zone_id}/dns_records/{dns_record_id}">client.dns.records.<a href="./src/cloudflare/resources/dns/records.py">delete</a>(dns_record_id, \*, zone_id) -> <a href="./src/cloudflare/types/dns/record_delete_response.py">Optional[RecordDeleteResponse]</a></code>
- <code title="post /zones/{zone_id}/dns_records/batch">client.dns.records.<a href="./src/cloudflare/resources/dns/records.py">batch</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/dns/record_batch_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/record_batch_response.py">Optional[RecordBatchResponse]</a></code>
- <code title="patch /zones/{zone_id}/dns_records/{dns_record_id}">client.dns.records.<a href="./src/cloudflare/resources/dns/records.py">edit</a>(dns_record_id, \*, zone_id, \*\*<a href="src/cloudflare/types/dns/record_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/record_response.py">Optional[RecordResponse]</a></code>
- <code title="get /zones/{zone_id}/dns_records/export">client.dns.records.<a href="./src/cloudflare/resources/dns/records.py">export</a>(\*, zone_id) -> str</code>
- <code title="get /zones/{zone_id}/dns_records/{dns_record_id}">client.dns.records.<a href="./src/cloudflare/resources/dns/records.py">get</a>(dns_record_id, \*, zone_id) -> <a href="./src/cloudflare/types/dns/record_response.py">Optional[RecordResponse]</a></code>
- <code title="post /zones/{zone_id}/dns_records/import">client.dns.records.<a href="./src/cloudflare/resources/dns/records.py">import\_</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/dns/record_import_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/record_import_response.py">Optional[RecordImportResponse]</a></code>
- <code title="post /zones/{zone_id}/dns_records/scan">client.dns.records.<a href="./src/cloudflare/resources/dns/records.py">scan</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/dns/record_scan_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/record_scan_response.py">Optional[RecordScanResponse]</a></code>
- <code title="get /zones/{zone_id}/dns_records/scan/review">client.dns.records.<a href="./src/cloudflare/resources/dns/records.py">scan_list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/dns/record_response.py">SyncSinglePage[RecordResponse]</a></code>
- <code title="post /zones/{zone_id}/dns_records/scan/review">client.dns.records.<a href="./src/cloudflare/resources/dns/records.py">scan_review</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/dns/record_scan_review_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/record_scan_review_response.py">Optional[RecordScanReviewResponse]</a></code>
- <code title="post /zones/{zone_id}/dns_records/scan/trigger">client.dns.records.<a href="./src/cloudflare/resources/dns/records.py">scan_trigger</a>(\*, zone_id) -> <a href="./src/cloudflare/types/dns/record_scan_trigger_response.py">RecordScanTriggerResponse</a></code>

## Settings

### Zone

Types:

```python
from cloudflare.types.dns.settings import ZoneEditResponse, ZoneGetResponse
```

Methods:

- <code title="patch /zones/{zone_id}/dns_settings">client.dns.settings.zone.<a href="./src/cloudflare/resources/dns/settings/zone.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/dns/settings/zone_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/settings/zone_edit_response.py">Optional[ZoneEditResponse]</a></code>
- <code title="get /zones/{zone_id}/dns_settings">client.dns.settings.zone.<a href="./src/cloudflare/resources/dns/settings/zone.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/dns/settings/zone_get_response.py">Optional[ZoneGetResponse]</a></code>

### Account

Types:

```python
from cloudflare.types.dns.settings import AccountEditResponse, AccountGetResponse
```

Methods:

- <code title="patch /accounts/{account_id}/dns_settings">client.dns.settings.account.<a href="./src/cloudflare/resources/dns/settings/account/account.py">edit</a>(\*, account_id, \*\*<a href="src/cloudflare/types/dns/settings/account_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/settings/account_edit_response.py">Optional[AccountEditResponse]</a></code>
- <code title="get /accounts/{account_id}/dns_settings">client.dns.settings.account.<a href="./src/cloudflare/resources/dns/settings/account/account.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/dns/settings/account_get_response.py">Optional[AccountGetResponse]</a></code>

#### Views

Types:

```python
from cloudflare.types.dns.settings.account import (
    ViewCreateResponse,
    ViewListResponse,
    ViewDeleteResponse,
    ViewEditResponse,
    ViewGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/dns_settings/views">client.dns.settings.account.views.<a href="./src/cloudflare/resources/dns/settings/account/views.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/dns/settings/account/view_create_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/settings/account/view_create_response.py">Optional[ViewCreateResponse]</a></code>
- <code title="get /accounts/{account_id}/dns_settings/views">client.dns.settings.account.views.<a href="./src/cloudflare/resources/dns/settings/account/views.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/dns/settings/account/view_list_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/settings/account/view_list_response.py">SyncV4PagePaginationArray[ViewListResponse]</a></code>
- <code title="delete /accounts/{account_id}/dns_settings/views/{view_id}">client.dns.settings.account.views.<a href="./src/cloudflare/resources/dns/settings/account/views.py">delete</a>(view_id, \*, account_id) -> <a href="./src/cloudflare/types/dns/settings/account/view_delete_response.py">Optional[ViewDeleteResponse]</a></code>
- <code title="patch /accounts/{account_id}/dns_settings/views/{view_id}">client.dns.settings.account.views.<a href="./src/cloudflare/resources/dns/settings/account/views.py">edit</a>(view_id, \*, account_id, \*\*<a href="src/cloudflare/types/dns/settings/account/view_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/settings/account/view_edit_response.py">Optional[ViewEditResponse]</a></code>
- <code title="get /accounts/{account_id}/dns_settings/views/{view_id}">client.dns.settings.account.views.<a href="./src/cloudflare/resources/dns/settings/account/views.py">get</a>(view_id, \*, account_id) -> <a href="./src/cloudflare/types/dns/settings/account/view_get_response.py">Optional[ViewGetResponse]</a></code>

## Analytics

### Reports

Types:

```python
from cloudflare.types.dns.analytics import Report
```

Methods:

- <code title="get /zones/{zone_id}/dns_analytics/report">client.dns.analytics.reports.<a href="./src/cloudflare/resources/dns/analytics/reports/reports.py">get</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/dns/analytics/report_get_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/analytics/report.py">Optional[Report]</a></code>

#### Bytimes

Types:

```python
from cloudflare.types.dns.analytics.reports import ByTime
```

Methods:

- <code title="get /zones/{zone_id}/dns_analytics/report/bytime">client.dns.analytics.reports.bytimes.<a href="./src/cloudflare/resources/dns/analytics/reports/bytimes.py">get</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/dns/analytics/reports/bytime_get_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/analytics/reports/by_time.py">Optional[ByTime]</a></code>

## ZoneTransfers

### ForceAXFR

Types:

```python
from cloudflare.types.dns.zone_transfers import ForceAXFR
```

Methods:

- <code title="post /zones/{zone_id}/secondary_dns/force_axfr">client.dns.zone_transfers.force_axfr.<a href="./src/cloudflare/resources/dns/zone_transfers/force_axfr.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/dns/zone_transfers/force_axfr_create_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/zone_transfers/force_axfr.py">str</a></code>

### Incoming

Types:

```python
from cloudflare.types.dns.zone_transfers import (
    Incoming,
    IncomingCreateResponse,
    IncomingUpdateResponse,
    IncomingDeleteResponse,
    IncomingGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/secondary_dns/incoming">client.dns.zone_transfers.incoming.<a href="./src/cloudflare/resources/dns/zone_transfers/incoming.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/dns/zone_transfers/incoming_create_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/zone_transfers/incoming_create_response.py">Optional[IncomingCreateResponse]</a></code>
- <code title="put /zones/{zone_id}/secondary_dns/incoming">client.dns.zone_transfers.incoming.<a href="./src/cloudflare/resources/dns/zone_transfers/incoming.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/dns/zone_transfers/incoming_update_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/zone_transfers/incoming_update_response.py">Optional[IncomingUpdateResponse]</a></code>
- <code title="delete /zones/{zone_id}/secondary_dns/incoming">client.dns.zone_transfers.incoming.<a href="./src/cloudflare/resources/dns/zone_transfers/incoming.py">delete</a>(\*, zone_id) -> <a href="./src/cloudflare/types/dns/zone_transfers/incoming_delete_response.py">Optional[IncomingDeleteResponse]</a></code>
- <code title="get /zones/{zone_id}/secondary_dns/incoming">client.dns.zone_transfers.incoming.<a href="./src/cloudflare/resources/dns/zone_transfers/incoming.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/dns/zone_transfers/incoming_get_response.py">Optional[IncomingGetResponse]</a></code>

### Outgoing

Types:

```python
from cloudflare.types.dns.zone_transfers import (
    DisableTransfer,
    EnableTransfer,
    Outgoing,
    OutgoingStatus,
    OutgoingCreateResponse,
    OutgoingUpdateResponse,
    OutgoingDeleteResponse,
    OutgoingForceNotifyResponse,
    OutgoingGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/secondary_dns/outgoing">client.dns.zone_transfers.outgoing.<a href="./src/cloudflare/resources/dns/zone_transfers/outgoing/outgoing.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/dns/zone_transfers/outgoing_create_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/zone_transfers/outgoing_create_response.py">Optional[OutgoingCreateResponse]</a></code>
- <code title="put /zones/{zone_id}/secondary_dns/outgoing">client.dns.zone_transfers.outgoing.<a href="./src/cloudflare/resources/dns/zone_transfers/outgoing/outgoing.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/dns/zone_transfers/outgoing_update_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/zone_transfers/outgoing_update_response.py">Optional[OutgoingUpdateResponse]</a></code>
- <code title="delete /zones/{zone_id}/secondary_dns/outgoing">client.dns.zone_transfers.outgoing.<a href="./src/cloudflare/resources/dns/zone_transfers/outgoing/outgoing.py">delete</a>(\*, zone_id) -> <a href="./src/cloudflare/types/dns/zone_transfers/outgoing_delete_response.py">Optional[OutgoingDeleteResponse]</a></code>
- <code title="post /zones/{zone_id}/secondary_dns/outgoing/disable">client.dns.zone_transfers.outgoing.<a href="./src/cloudflare/resources/dns/zone_transfers/outgoing/outgoing.py">disable</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/dns/zone_transfers/outgoing_disable_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/zone_transfers/disable_transfer.py">str</a></code>
- <code title="post /zones/{zone_id}/secondary_dns/outgoing/enable">client.dns.zone_transfers.outgoing.<a href="./src/cloudflare/resources/dns/zone_transfers/outgoing/outgoing.py">enable</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/dns/zone_transfers/outgoing_enable_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/zone_transfers/enable_transfer.py">str</a></code>
- <code title="post /zones/{zone_id}/secondary_dns/outgoing/force_notify">client.dns.zone_transfers.outgoing.<a href="./src/cloudflare/resources/dns/zone_transfers/outgoing/outgoing.py">force_notify</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/dns/zone_transfers/outgoing_force_notify_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/zone_transfers/outgoing_force_notify_response.py">str</a></code>
- <code title="get /zones/{zone_id}/secondary_dns/outgoing">client.dns.zone_transfers.outgoing.<a href="./src/cloudflare/resources/dns/zone_transfers/outgoing/outgoing.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/dns/zone_transfers/outgoing_get_response.py">Optional[OutgoingGetResponse]</a></code>

#### Status

Methods:

- <code title="get /zones/{zone_id}/secondary_dns/outgoing/status">client.dns.zone_transfers.outgoing.status.<a href="./src/cloudflare/resources/dns/zone_transfers/outgoing/status.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/dns/zone_transfers/enable_transfer.py">str</a></code>

### ACLs

Types:

```python
from cloudflare.types.dns.zone_transfers import ACL, ACLDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/secondary_dns/acls">client.dns.zone_transfers.acls.<a href="./src/cloudflare/resources/dns/zone_transfers/acls.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/dns/zone_transfers/acl_create_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/zone_transfers/acl.py">Optional[ACL]</a></code>
- <code title="put /accounts/{account_id}/secondary_dns/acls/{acl_id}">client.dns.zone_transfers.acls.<a href="./src/cloudflare/resources/dns/zone_transfers/acls.py">update</a>(acl_id, \*, account_id, \*\*<a href="src/cloudflare/types/dns/zone_transfers/acl_update_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/zone_transfers/acl.py">Optional[ACL]</a></code>
- <code title="get /accounts/{account_id}/secondary_dns/acls">client.dns.zone_transfers.acls.<a href="./src/cloudflare/resources/dns/zone_transfers/acls.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/dns/zone_transfers/acl.py">SyncSinglePage[ACL]</a></code>
- <code title="delete /accounts/{account_id}/secondary_dns/acls/{acl_id}">client.dns.zone_transfers.acls.<a href="./src/cloudflare/resources/dns/zone_transfers/acls.py">delete</a>(acl_id, \*, account_id) -> <a href="./src/cloudflare/types/dns/zone_transfers/acl_delete_response.py">Optional[ACLDeleteResponse]</a></code>
- <code title="get /accounts/{account_id}/secondary_dns/acls/{acl_id}">client.dns.zone_transfers.acls.<a href="./src/cloudflare/resources/dns/zone_transfers/acls.py">get</a>(acl_id, \*, account_id) -> <a href="./src/cloudflare/types/dns/zone_transfers/acl.py">Optional[ACL]</a></code>

### Peers

Types:

```python
from cloudflare.types.dns.zone_transfers import Peer, PeerDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/secondary_dns/peers">client.dns.zone_transfers.peers.<a href="./src/cloudflare/resources/dns/zone_transfers/peers.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/dns/zone_transfers/peer_create_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/zone_transfers/peer.py">Optional[Peer]</a></code>
- <code title="put /accounts/{account_id}/secondary_dns/peers/{peer_id}">client.dns.zone_transfers.peers.<a href="./src/cloudflare/resources/dns/zone_transfers/peers.py">update</a>(peer_id, \*, account_id, \*\*<a href="src/cloudflare/types/dns/zone_transfers/peer_update_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/zone_transfers/peer.py">Optional[Peer]</a></code>
- <code title="get /accounts/{account_id}/secondary_dns/peers">client.dns.zone_transfers.peers.<a href="./src/cloudflare/resources/dns/zone_transfers/peers.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/dns/zone_transfers/peer.py">SyncSinglePage[Peer]</a></code>
- <code title="delete /accounts/{account_id}/secondary_dns/peers/{peer_id}">client.dns.zone_transfers.peers.<a href="./src/cloudflare/resources/dns/zone_transfers/peers.py">delete</a>(peer_id, \*, account_id) -> <a href="./src/cloudflare/types/dns/zone_transfers/peer_delete_response.py">Optional[PeerDeleteResponse]</a></code>
- <code title="get /accounts/{account_id}/secondary_dns/peers/{peer_id}">client.dns.zone_transfers.peers.<a href="./src/cloudflare/resources/dns/zone_transfers/peers.py">get</a>(peer_id, \*, account_id) -> <a href="./src/cloudflare/types/dns/zone_transfers/peer.py">Optional[Peer]</a></code>

### TSIGs

Types:

```python
from cloudflare.types.dns.zone_transfers import TSIG, TSIGDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/secondary_dns/tsigs">client.dns.zone_transfers.tsigs.<a href="./src/cloudflare/resources/dns/zone_transfers/tsigs.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/dns/zone_transfers/tsig_create_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/zone_transfers/tsig.py">Optional[TSIG]</a></code>
- <code title="put /accounts/{account_id}/secondary_dns/tsigs/{tsig_id}">client.dns.zone_transfers.tsigs.<a href="./src/cloudflare/resources/dns/zone_transfers/tsigs.py">update</a>(tsig_id, \*, account_id, \*\*<a href="src/cloudflare/types/dns/zone_transfers/tsig_update_params.py">params</a>) -> <a href="./src/cloudflare/types/dns/zone_transfers/tsig.py">Optional[TSIG]</a></code>
- <code title="get /accounts/{account_id}/secondary_dns/tsigs">client.dns.zone_transfers.tsigs.<a href="./src/cloudflare/resources/dns/zone_transfers/tsigs.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/dns/zone_transfers/tsig.py">SyncSinglePage[TSIG]</a></code>
- <code title="delete /accounts/{account_id}/secondary_dns/tsigs/{tsig_id}">client.dns.zone_transfers.tsigs.<a href="./src/cloudflare/resources/dns/zone_transfers/tsigs.py">delete</a>(tsig_id, \*, account_id) -> <a href="./src/cloudflare/types/dns/zone_transfers/tsig_delete_response.py">Optional[TSIGDeleteResponse]</a></code>
- <code title="get /accounts/{account_id}/secondary_dns/tsigs/{tsig_id}">client.dns.zone_transfers.tsigs.<a href="./src/cloudflare/resources/dns/zone_transfers/tsigs.py">get</a>(tsig_id, \*, account_id) -> <a href="./src/cloudflare/types/dns/zone_transfers/tsig.py">Optional[TSIG]</a></code>
