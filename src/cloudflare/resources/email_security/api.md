# EmailSecurity

## Investigate

Types:

```python
from cloudflare.types.email_security import InvestigateListResponse, InvestigateGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/email-security/investigate">client.email_security.investigate.<a href="./src/cloudflare/resources/email_security/investigate/investigate.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/email_security/investigate_list_params.py">params</a>) -> <a href="./src/cloudflare/types/email_security/investigate_list_response.py">SyncV4PagePaginationArray[InvestigateListResponse]</a></code>
- <code title="get /accounts/{account_id}/email-security/investigate/{postfix_id}">client.email_security.investigate.<a href="./src/cloudflare/resources/email_security/investigate/investigate.py">get</a>(postfix_id, \*, account_id, \*\*<a href="src/cloudflare/types/email_security/investigate_get_params.py">params</a>) -> <a href="./src/cloudflare/types/email_security/investigate_get_response.py">InvestigateGetResponse</a></code>

### Detections

Types:

```python
from cloudflare.types.email_security.investigate import DetectionGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/email-security/investigate/{postfix_id}/detections">client.email_security.investigate.detections.<a href="./src/cloudflare/resources/email_security/investigate/detections.py">get</a>(postfix_id, \*, account_id) -> <a href="./src/cloudflare/types/email_security/investigate/detection_get_response.py">DetectionGetResponse</a></code>

### Preview

Types:

```python
from cloudflare.types.email_security.investigate import PreviewCreateResponse, PreviewGetResponse
```

Methods:

- <code title="post /accounts/{account_id}/email-security/investigate/preview">client.email_security.investigate.preview.<a href="./src/cloudflare/resources/email_security/investigate/preview.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/email_security/investigate/preview_create_params.py">params</a>) -> <a href="./src/cloudflare/types/email_security/investigate/preview_create_response.py">PreviewCreateResponse</a></code>
- <code title="get /accounts/{account_id}/email-security/investigate/{postfix_id}/preview">client.email_security.investigate.preview.<a href="./src/cloudflare/resources/email_security/investigate/preview.py">get</a>(postfix_id, \*, account_id) -> <a href="./src/cloudflare/types/email_security/investigate/preview_get_response.py">PreviewGetResponse</a></code>

### Raw

Types:

```python
from cloudflare.types.email_security.investigate import RawGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/email-security/investigate/{postfix_id}/raw">client.email_security.investigate.raw.<a href="./src/cloudflare/resources/email_security/investigate/raw.py">get</a>(postfix_id, \*, account_id) -> <a href="./src/cloudflare/types/email_security/investigate/raw_get_response.py">RawGetResponse</a></code>

### Trace

Types:

```python
from cloudflare.types.email_security.investigate import TraceGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/email-security/investigate/{postfix_id}/trace">client.email_security.investigate.trace.<a href="./src/cloudflare/resources/email_security/investigate/trace.py">get</a>(postfix_id, \*, account_id, \*\*<a href="src/cloudflare/types/email_security/investigate/trace_get_params.py">params</a>) -> <a href="./src/cloudflare/types/email_security/investigate/trace_get_response.py">TraceGetResponse</a></code>

### Move

Types:

```python
from cloudflare.types.email_security.investigate import MoveCreateResponse, MoveBulkResponse
```

Methods:

- <code title="post /accounts/{account_id}/email-security/investigate/{postfix_id}/move">client.email_security.investigate.move.<a href="./src/cloudflare/resources/email_security/investigate/move.py">create</a>(postfix_id, \*, account_id, \*\*<a href="src/cloudflare/types/email_security/investigate/move_create_params.py">params</a>) -> <a href="./src/cloudflare/types/email_security/investigate/move_create_response.py">MoveCreateResponse</a></code>
- <code title="post /accounts/{account_id}/email-security/investigate/move">client.email_security.investigate.move.<a href="./src/cloudflare/resources/email_security/investigate/move.py">bulk</a>(\*, account_id, \*\*<a href="src/cloudflare/types/email_security/investigate/move_bulk_params.py">params</a>) -> <a href="./src/cloudflare/types/email_security/investigate/move_bulk_response.py">SyncSinglePage[MoveBulkResponse]</a></code>

### Reclassify

Methods:

- <code title="post /accounts/{account_id}/email-security/investigate/{postfix_id}/reclassify">client.email_security.investigate.reclassify.<a href="./src/cloudflare/resources/email_security/investigate/reclassify.py">create</a>(postfix_id, \*, account_id, \*\*<a href="src/cloudflare/types/email_security/investigate/reclassify_create_params.py">params</a>) -> object</code>

### Release

Types:

```python
from cloudflare.types.email_security.investigate import ReleaseBulkResponse
```

Methods:

- <code title="post /accounts/{account_id}/email-security/investigate/release">client.email_security.investigate.release.<a href="./src/cloudflare/resources/email_security/investigate/release.py">bulk</a>(\*, account_id, \*\*<a href="src/cloudflare/types/email_security/investigate/release_bulk_params.py">params</a>) -> <a href="./src/cloudflare/types/email_security/investigate/release_bulk_response.py">SyncSinglePage[ReleaseBulkResponse]</a></code>

## Phishguard

### Reports

Types:

```python
from cloudflare.types.email_security.phishguard import ReportListResponse
```

Methods:

- <code title="get /accounts/{account_id}/email-security/phishguard/reports">client.email_security.phishguard.reports.<a href="./src/cloudflare/resources/email_security/phishguard/reports.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/email_security/phishguard/report_list_params.py">params</a>) -> <a href="./src/cloudflare/types/email_security/phishguard/report_list_response.py">SyncSinglePage[ReportListResponse]</a></code>

## Settings

### AllowPolicies

Types:

```python
from cloudflare.types.email_security.settings import (
    AllowPolicyCreateResponse,
    AllowPolicyListResponse,
    AllowPolicyDeleteResponse,
    AllowPolicyEditResponse,
    AllowPolicyGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/email-security/settings/allow_policies">client.email_security.settings.allow_policies.<a href="./src/cloudflare/resources/email_security/settings/allow_policies.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/email_security/settings/allow_policy_create_params.py">params</a>) -> <a href="./src/cloudflare/types/email_security/settings/allow_policy_create_response.py">AllowPolicyCreateResponse</a></code>
- <code title="get /accounts/{account_id}/email-security/settings/allow_policies">client.email_security.settings.allow_policies.<a href="./src/cloudflare/resources/email_security/settings/allow_policies.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/email_security/settings/allow_policy_list_params.py">params</a>) -> <a href="./src/cloudflare/types/email_security/settings/allow_policy_list_response.py">SyncV4PagePaginationArray[AllowPolicyListResponse]</a></code>
- <code title="delete /accounts/{account_id}/email-security/settings/allow_policies/{policy_id}">client.email_security.settings.allow_policies.<a href="./src/cloudflare/resources/email_security/settings/allow_policies.py">delete</a>(policy_id, \*, account_id) -> <a href="./src/cloudflare/types/email_security/settings/allow_policy_delete_response.py">AllowPolicyDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/email-security/settings/allow_policies/{policy_id}">client.email_security.settings.allow_policies.<a href="./src/cloudflare/resources/email_security/settings/allow_policies.py">edit</a>(policy_id, \*, account_id, \*\*<a href="src/cloudflare/types/email_security/settings/allow_policy_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/email_security/settings/allow_policy_edit_response.py">AllowPolicyEditResponse</a></code>
- <code title="get /accounts/{account_id}/email-security/settings/allow_policies/{policy_id}">client.email_security.settings.allow_policies.<a href="./src/cloudflare/resources/email_security/settings/allow_policies.py">get</a>(policy_id, \*, account_id) -> <a href="./src/cloudflare/types/email_security/settings/allow_policy_get_response.py">AllowPolicyGetResponse</a></code>

### BlockSenders

Types:

```python
from cloudflare.types.email_security.settings import (
    BlockSenderCreateResponse,
    BlockSenderListResponse,
    BlockSenderDeleteResponse,
    BlockSenderEditResponse,
    BlockSenderGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/email-security/settings/block_senders">client.email_security.settings.block_senders.<a href="./src/cloudflare/resources/email_security/settings/block_senders.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/email_security/settings/block_sender_create_params.py">params</a>) -> <a href="./src/cloudflare/types/email_security/settings/block_sender_create_response.py">BlockSenderCreateResponse</a></code>
- <code title="get /accounts/{account_id}/email-security/settings/block_senders">client.email_security.settings.block_senders.<a href="./src/cloudflare/resources/email_security/settings/block_senders.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/email_security/settings/block_sender_list_params.py">params</a>) -> <a href="./src/cloudflare/types/email_security/settings/block_sender_list_response.py">SyncV4PagePaginationArray[BlockSenderListResponse]</a></code>
- <code title="delete /accounts/{account_id}/email-security/settings/block_senders/{pattern_id}">client.email_security.settings.block_senders.<a href="./src/cloudflare/resources/email_security/settings/block_senders.py">delete</a>(pattern_id, \*, account_id) -> <a href="./src/cloudflare/types/email_security/settings/block_sender_delete_response.py">BlockSenderDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/email-security/settings/block_senders/{pattern_id}">client.email_security.settings.block_senders.<a href="./src/cloudflare/resources/email_security/settings/block_senders.py">edit</a>(pattern_id, \*, account_id, \*\*<a href="src/cloudflare/types/email_security/settings/block_sender_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/email_security/settings/block_sender_edit_response.py">BlockSenderEditResponse</a></code>
- <code title="get /accounts/{account_id}/email-security/settings/block_senders/{pattern_id}">client.email_security.settings.block_senders.<a href="./src/cloudflare/resources/email_security/settings/block_senders.py">get</a>(pattern_id, \*, account_id) -> <a href="./src/cloudflare/types/email_security/settings/block_sender_get_response.py">BlockSenderGetResponse</a></code>

### Domains

Types:

```python
from cloudflare.types.email_security.settings import (
    DomainListResponse,
    DomainDeleteResponse,
    DomainBulkDeleteResponse,
    DomainEditResponse,
    DomainGetResponse,
)
```

Methods:

- <code title="get /accounts/{account_id}/email-security/settings/domains">client.email_security.settings.domains.<a href="./src/cloudflare/resources/email_security/settings/domains.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/email_security/settings/domain_list_params.py">params</a>) -> <a href="./src/cloudflare/types/email_security/settings/domain_list_response.py">SyncV4PagePaginationArray[DomainListResponse]</a></code>
- <code title="delete /accounts/{account_id}/email-security/settings/domains/{domain_id}">client.email_security.settings.domains.<a href="./src/cloudflare/resources/email_security/settings/domains.py">delete</a>(domain_id, \*, account_id) -> <a href="./src/cloudflare/types/email_security/settings/domain_delete_response.py">DomainDeleteResponse</a></code>
- <code title="delete /accounts/{account_id}/email-security/settings/domains">client.email_security.settings.domains.<a href="./src/cloudflare/resources/email_security/settings/domains.py">bulk_delete</a>(\*, account_id) -> <a href="./src/cloudflare/types/email_security/settings/domain_bulk_delete_response.py">SyncSinglePage[DomainBulkDeleteResponse]</a></code>
- <code title="patch /accounts/{account_id}/email-security/settings/domains/{domain_id}">client.email_security.settings.domains.<a href="./src/cloudflare/resources/email_security/settings/domains.py">edit</a>(domain_id, \*, account_id, \*\*<a href="src/cloudflare/types/email_security/settings/domain_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/email_security/settings/domain_edit_response.py">DomainEditResponse</a></code>
- <code title="get /accounts/{account_id}/email-security/settings/domains/{domain_id}">client.email_security.settings.domains.<a href="./src/cloudflare/resources/email_security/settings/domains.py">get</a>(domain_id, \*, account_id) -> <a href="./src/cloudflare/types/email_security/settings/domain_get_response.py">DomainGetResponse</a></code>

### ImpersonationRegistry

Types:

```python
from cloudflare.types.email_security.settings import (
    ImpersonationRegistryCreateResponse,
    ImpersonationRegistryListResponse,
    ImpersonationRegistryDeleteResponse,
    ImpersonationRegistryEditResponse,
    ImpersonationRegistryGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/email-security/settings/impersonation_registry">client.email_security.settings.impersonation_registry.<a href="./src/cloudflare/resources/email_security/settings/impersonation_registry.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/email_security/settings/impersonation_registry_create_params.py">params</a>) -> <a href="./src/cloudflare/types/email_security/settings/impersonation_registry_create_response.py">ImpersonationRegistryCreateResponse</a></code>
- <code title="get /accounts/{account_id}/email-security/settings/impersonation_registry">client.email_security.settings.impersonation_registry.<a href="./src/cloudflare/resources/email_security/settings/impersonation_registry.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/email_security/settings/impersonation_registry_list_params.py">params</a>) -> <a href="./src/cloudflare/types/email_security/settings/impersonation_registry_list_response.py">SyncV4PagePaginationArray[ImpersonationRegistryListResponse]</a></code>
- <code title="delete /accounts/{account_id}/email-security/settings/impersonation_registry/{display_name_id}">client.email_security.settings.impersonation_registry.<a href="./src/cloudflare/resources/email_security/settings/impersonation_registry.py">delete</a>(display_name_id, \*, account_id) -> <a href="./src/cloudflare/types/email_security/settings/impersonation_registry_delete_response.py">ImpersonationRegistryDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/email-security/settings/impersonation_registry/{display_name_id}">client.email_security.settings.impersonation_registry.<a href="./src/cloudflare/resources/email_security/settings/impersonation_registry.py">edit</a>(display_name_id, \*, account_id, \*\*<a href="src/cloudflare/types/email_security/settings/impersonation_registry_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/email_security/settings/impersonation_registry_edit_response.py">ImpersonationRegistryEditResponse</a></code>
- <code title="get /accounts/{account_id}/email-security/settings/impersonation_registry/{display_name_id}">client.email_security.settings.impersonation_registry.<a href="./src/cloudflare/resources/email_security/settings/impersonation_registry.py">get</a>(display_name_id, \*, account_id) -> <a href="./src/cloudflare/types/email_security/settings/impersonation_registry_get_response.py">ImpersonationRegistryGetResponse</a></code>

### TrustedDomains

Types:

```python
from cloudflare.types.email_security.settings import (
    TrustedDomainCreateResponse,
    TrustedDomainListResponse,
    TrustedDomainDeleteResponse,
    TrustedDomainEditResponse,
    TrustedDomainGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/email-security/settings/trusted_domains">client.email_security.settings.trusted_domains.<a href="./src/cloudflare/resources/email_security/settings/trusted_domains.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/email_security/settings/trusted_domain_create_params.py">params</a>) -> <a href="./src/cloudflare/types/email_security/settings/trusted_domain_create_response.py">TrustedDomainCreateResponse</a></code>
- <code title="get /accounts/{account_id}/email-security/settings/trusted_domains">client.email_security.settings.trusted_domains.<a href="./src/cloudflare/resources/email_security/settings/trusted_domains.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/email_security/settings/trusted_domain_list_params.py">params</a>) -> <a href="./src/cloudflare/types/email_security/settings/trusted_domain_list_response.py">SyncV4PagePaginationArray[TrustedDomainListResponse]</a></code>
- <code title="delete /accounts/{account_id}/email-security/settings/trusted_domains/{trusted_domain_id}">client.email_security.settings.trusted_domains.<a href="./src/cloudflare/resources/email_security/settings/trusted_domains.py">delete</a>(trusted_domain_id, \*, account_id) -> <a href="./src/cloudflare/types/email_security/settings/trusted_domain_delete_response.py">TrustedDomainDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/email-security/settings/trusted_domains/{trusted_domain_id}">client.email_security.settings.trusted_domains.<a href="./src/cloudflare/resources/email_security/settings/trusted_domains.py">edit</a>(trusted_domain_id, \*, account_id, \*\*<a href="src/cloudflare/types/email_security/settings/trusted_domain_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/email_security/settings/trusted_domain_edit_response.py">TrustedDomainEditResponse</a></code>
- <code title="get /accounts/{account_id}/email-security/settings/trusted_domains/{trusted_domain_id}">client.email_security.settings.trusted_domains.<a href="./src/cloudflare/resources/email_security/settings/trusted_domains.py">get</a>(trusted_domain_id, \*, account_id) -> <a href="./src/cloudflare/types/email_security/settings/trusted_domain_get_response.py">TrustedDomainGetResponse</a></code>

## Submissions

Types:

```python
from cloudflare.types.email_security import SubmissionListResponse
```

Methods:

- <code title="get /accounts/{account_id}/email-security/submissions">client.email_security.submissions.<a href="./src/cloudflare/resources/email_security/submissions.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/email_security/submission_list_params.py">params</a>) -> <a href="./src/cloudflare/types/email_security/submission_list_response.py">SyncV4PagePaginationArray[SubmissionListResponse]</a></code>
