# R2

## Buckets

Types:

```python
from cloudflare.types.r2 import Bucket, BucketListResponse
```

Methods:

- <code title="post /accounts/{account_id}/r2/buckets">client.r2.buckets.<a href="./src/cloudflare/resources/r2/buckets/buckets.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/r2/bucket_create_params.py">params</a>) -> <a href="./src/cloudflare/types/r2/bucket.py">Bucket</a></code>
- <code title="get /accounts/{account_id}/r2/buckets">client.r2.buckets.<a href="./src/cloudflare/resources/r2/buckets/buckets.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/r2/bucket_list_params.py">params</a>) -> <a href="./src/cloudflare/types/r2/bucket_list_response.py">BucketListResponse</a></code>
- <code title="delete /accounts/{account_id}/r2/buckets/{bucket_name}">client.r2.buckets.<a href="./src/cloudflare/resources/r2/buckets/buckets.py">delete</a>(bucket_name, \*, account_id) -> object</code>
- <code title="patch /accounts/{account_id}/r2/buckets/{bucket_name}">client.r2.buckets.<a href="./src/cloudflare/resources/r2/buckets/buckets.py">edit</a>(bucket_name, \*, account_id) -> <a href="./src/cloudflare/types/r2/bucket.py">Bucket</a></code>
- <code title="get /accounts/{account_id}/r2/buckets/{bucket_name}">client.r2.buckets.<a href="./src/cloudflare/resources/r2/buckets/buckets.py">get</a>(bucket_name, \*, account_id) -> <a href="./src/cloudflare/types/r2/bucket.py">Bucket</a></code>

### Lifecycle

Types:

```python
from cloudflare.types.r2.buckets import LifecycleGetResponse
```

Methods:

- <code title="put /accounts/{account_id}/r2/buckets/{bucket_name}/lifecycle">client.r2.buckets.lifecycle.<a href="./src/cloudflare/resources/r2/buckets/lifecycle.py">update</a>(bucket_name, \*, account_id, \*\*<a href="src/cloudflare/types/r2/buckets/lifecycle_update_params.py">params</a>) -> object</code>
- <code title="get /accounts/{account_id}/r2/buckets/{bucket_name}/lifecycle">client.r2.buckets.lifecycle.<a href="./src/cloudflare/resources/r2/buckets/lifecycle.py">get</a>(bucket_name, \*, account_id) -> <a href="./src/cloudflare/types/r2/buckets/lifecycle_get_response.py">LifecycleGetResponse</a></code>

### CORS

Types:

```python
from cloudflare.types.r2.buckets import CORSGetResponse
```

Methods:

- <code title="put /accounts/{account_id}/r2/buckets/{bucket_name}/cors">client.r2.buckets.cors.<a href="./src/cloudflare/resources/r2/buckets/cors.py">update</a>(bucket_name, \*, account_id, \*\*<a href="src/cloudflare/types/r2/buckets/cors_update_params.py">params</a>) -> object</code>
- <code title="delete /accounts/{account_id}/r2/buckets/{bucket_name}/cors">client.r2.buckets.cors.<a href="./src/cloudflare/resources/r2/buckets/cors.py">delete</a>(bucket_name, \*, account_id) -> object</code>
- <code title="get /accounts/{account_id}/r2/buckets/{bucket_name}/cors">client.r2.buckets.cors.<a href="./src/cloudflare/resources/r2/buckets/cors.py">get</a>(bucket_name, \*, account_id) -> <a href="./src/cloudflare/types/r2/buckets/cors_get_response.py">CORSGetResponse</a></code>

### Domains

#### Custom

Types:

```python
from cloudflare.types.r2.buckets.domains import (
    CustomCreateResponse,
    CustomUpdateResponse,
    CustomListResponse,
    CustomDeleteResponse,
    CustomGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/r2/buckets/{bucket_name}/domains/custom">client.r2.buckets.domains.custom.<a href="./src/cloudflare/resources/r2/buckets/domains/custom.py">create</a>(bucket_name, \*, account_id, \*\*<a href="src/cloudflare/types/r2/buckets/domains/custom_create_params.py">params</a>) -> <a href="./src/cloudflare/types/r2/buckets/domains/custom_create_response.py">CustomCreateResponse</a></code>
- <code title="put /accounts/{account_id}/r2/buckets/{bucket_name}/domains/custom/{domain}">client.r2.buckets.domains.custom.<a href="./src/cloudflare/resources/r2/buckets/domains/custom.py">update</a>(domain, \*, account_id, bucket_name, \*\*<a href="src/cloudflare/types/r2/buckets/domains/custom_update_params.py">params</a>) -> <a href="./src/cloudflare/types/r2/buckets/domains/custom_update_response.py">CustomUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/r2/buckets/{bucket_name}/domains/custom">client.r2.buckets.domains.custom.<a href="./src/cloudflare/resources/r2/buckets/domains/custom.py">list</a>(bucket_name, \*, account_id) -> <a href="./src/cloudflare/types/r2/buckets/domains/custom_list_response.py">CustomListResponse</a></code>
- <code title="delete /accounts/{account_id}/r2/buckets/{bucket_name}/domains/custom/{domain}">client.r2.buckets.domains.custom.<a href="./src/cloudflare/resources/r2/buckets/domains/custom.py">delete</a>(domain, \*, account_id, bucket_name) -> <a href="./src/cloudflare/types/r2/buckets/domains/custom_delete_response.py">CustomDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/r2/buckets/{bucket_name}/domains/custom/{domain}">client.r2.buckets.domains.custom.<a href="./src/cloudflare/resources/r2/buckets/domains/custom.py">get</a>(domain, \*, account_id, bucket_name) -> <a href="./src/cloudflare/types/r2/buckets/domains/custom_get_response.py">CustomGetResponse</a></code>

#### Managed

Types:

```python
from cloudflare.types.r2.buckets.domains import ManagedUpdateResponse, ManagedListResponse
```

Methods:

- <code title="put /accounts/{account_id}/r2/buckets/{bucket_name}/domains/managed">client.r2.buckets.domains.managed.<a href="./src/cloudflare/resources/r2/buckets/domains/managed.py">update</a>(bucket_name, \*, account_id, \*\*<a href="src/cloudflare/types/r2/buckets/domains/managed_update_params.py">params</a>) -> <a href="./src/cloudflare/types/r2/buckets/domains/managed_update_response.py">ManagedUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/r2/buckets/{bucket_name}/domains/managed">client.r2.buckets.domains.managed.<a href="./src/cloudflare/resources/r2/buckets/domains/managed.py">list</a>(bucket_name, \*, account_id) -> <a href="./src/cloudflare/types/r2/buckets/domains/managed_list_response.py">ManagedListResponse</a></code>

### EventNotifications

Types:

```python
from cloudflare.types.r2.buckets import EventNotificationListResponse, EventNotificationGetResponse
```

Methods:

- <code title="put /accounts/{account_id}/event_notifications/r2/{bucket_name}/configuration/queues/{queue_id}">client.r2.buckets.event_notifications.<a href="./src/cloudflare/resources/r2/buckets/event_notifications.py">update</a>(queue_id, \*, account_id, bucket_name, \*\*<a href="src/cloudflare/types/r2/buckets/event_notification_update_params.py">params</a>) -> object</code>
- <code title="get /accounts/{account_id}/event_notifications/r2/{bucket_name}/configuration">client.r2.buckets.event_notifications.<a href="./src/cloudflare/resources/r2/buckets/event_notifications.py">list</a>(bucket_name, \*, account_id) -> <a href="./src/cloudflare/types/r2/buckets/event_notification_list_response.py">EventNotificationListResponse</a></code>
- <code title="delete /accounts/{account_id}/event_notifications/r2/{bucket_name}/configuration/queues/{queue_id}">client.r2.buckets.event_notifications.<a href="./src/cloudflare/resources/r2/buckets/event_notifications.py">delete</a>(queue_id, \*, account_id, bucket_name) -> object</code>
- <code title="get /accounts/{account_id}/event_notifications/r2/{bucket_name}/configuration/queues/{queue_id}">client.r2.buckets.event_notifications.<a href="./src/cloudflare/resources/r2/buckets/event_notifications.py">get</a>(queue_id, \*, account_id, bucket_name) -> <a href="./src/cloudflare/types/r2/buckets/event_notification_get_response.py">EventNotificationGetResponse</a></code>

### Locks

Types:

```python
from cloudflare.types.r2.buckets import LockGetResponse
```

Methods:

- <code title="put /accounts/{account_id}/r2/buckets/{bucket_name}/lock">client.r2.buckets.locks.<a href="./src/cloudflare/resources/r2/buckets/locks.py">update</a>(bucket_name, \*, account_id, \*\*<a href="src/cloudflare/types/r2/buckets/lock_update_params.py">params</a>) -> object</code>
- <code title="get /accounts/{account_id}/r2/buckets/{bucket_name}/lock">client.r2.buckets.locks.<a href="./src/cloudflare/resources/r2/buckets/locks.py">get</a>(bucket_name, \*, account_id) -> <a href="./src/cloudflare/types/r2/buckets/lock_get_response.py">LockGetResponse</a></code>

### Metrics

Types:

```python
from cloudflare.types.r2.buckets import MetricListResponse
```

Methods:

- <code title="get /accounts/{account_id}/r2/metrics">client.r2.buckets.metrics.<a href="./src/cloudflare/resources/r2/buckets/metrics.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/r2/buckets/metric_list_response.py">MetricListResponse</a></code>

### Sippy

Types:

```python
from cloudflare.types.r2.buckets import Provider, Sippy, SippyDeleteResponse
```

Methods:

- <code title="put /accounts/{account_id}/r2/buckets/{bucket_name}/sippy">client.r2.buckets.sippy.<a href="./src/cloudflare/resources/r2/buckets/sippy.py">update</a>(bucket_name, \*, account_id, \*\*<a href="src/cloudflare/types/r2/buckets/sippy_update_params.py">params</a>) -> <a href="./src/cloudflare/types/r2/buckets/sippy.py">Sippy</a></code>
- <code title="delete /accounts/{account_id}/r2/buckets/{bucket_name}/sippy">client.r2.buckets.sippy.<a href="./src/cloudflare/resources/r2/buckets/sippy.py">delete</a>(bucket_name, \*, account_id) -> <a href="./src/cloudflare/types/r2/buckets/sippy_delete_response.py">SippyDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/r2/buckets/{bucket_name}/sippy">client.r2.buckets.sippy.<a href="./src/cloudflare/resources/r2/buckets/sippy.py">get</a>(bucket_name, \*, account_id) -> <a href="./src/cloudflare/types/r2/buckets/sippy.py">Sippy</a></code>

## TemporaryCredentials

Types:

```python
from cloudflare.types.r2 import TemporaryCredential, TemporaryCredentialCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/r2/temp-access-credentials">client.r2.temporary_credentials.<a href="./src/cloudflare/resources/r2/temporary_credentials.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/r2/temporary_credential_create_params.py">params</a>) -> <a href="./src/cloudflare/types/r2/temporary_credential_create_response.py">TemporaryCredentialCreateResponse</a></code>

## SuperSlurper

### Jobs

Types:

```python
from cloudflare.types.r2.super_slurper import (
    JobCreateResponse,
    JobListResponse,
    JobAbortResponse,
    JobAbortAllResponse,
    JobGetResponse,
    JobPauseResponse,
    JobProgressResponse,
    JobResumeResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/slurper/jobs">client.r2.super_slurper.jobs.<a href="./src/cloudflare/resources/r2/super_slurper/jobs/jobs.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/r2/super_slurper/job_create_params.py">params</a>) -> <a href="./src/cloudflare/types/r2/super_slurper/job_create_response.py">Optional[JobCreateResponse]</a></code>
- <code title="get /accounts/{account_id}/slurper/jobs">client.r2.super_slurper.jobs.<a href="./src/cloudflare/resources/r2/super_slurper/jobs/jobs.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/r2/super_slurper/job_list_params.py">params</a>) -> <a href="./src/cloudflare/types/r2/super_slurper/job_list_response.py">SyncSinglePage[JobListResponse]</a></code>
- <code title="put /accounts/{account_id}/slurper/jobs/{job_id}/abort">client.r2.super_slurper.jobs.<a href="./src/cloudflare/resources/r2/super_slurper/jobs/jobs.py">abort</a>(job_id, \*, account_id) -> <a href="./src/cloudflare/types/r2/super_slurper/job_abort_response.py">str</a></code>
- <code title="put /accounts/{account_id}/slurper/jobs/abortAll">client.r2.super_slurper.jobs.<a href="./src/cloudflare/resources/r2/super_slurper/jobs/jobs.py">abort_all</a>(\*, account_id) -> <a href="./src/cloudflare/types/r2/super_slurper/job_abort_all_response.py">str</a></code>
- <code title="get /accounts/{account_id}/slurper/jobs/{job_id}">client.r2.super_slurper.jobs.<a href="./src/cloudflare/resources/r2/super_slurper/jobs/jobs.py">get</a>(job_id, \*, account_id) -> <a href="./src/cloudflare/types/r2/super_slurper/job_get_response.py">Optional[JobGetResponse]</a></code>
- <code title="put /accounts/{account_id}/slurper/jobs/{job_id}/pause">client.r2.super_slurper.jobs.<a href="./src/cloudflare/resources/r2/super_slurper/jobs/jobs.py">pause</a>(job_id, \*, account_id) -> <a href="./src/cloudflare/types/r2/super_slurper/job_pause_response.py">str</a></code>
- <code title="get /accounts/{account_id}/slurper/jobs/{job_id}/progress">client.r2.super_slurper.jobs.<a href="./src/cloudflare/resources/r2/super_slurper/jobs/jobs.py">progress</a>(job_id, \*, account_id) -> <a href="./src/cloudflare/types/r2/super_slurper/job_progress_response.py">Optional[JobProgressResponse]</a></code>
- <code title="put /accounts/{account_id}/slurper/jobs/{job_id}/resume">client.r2.super_slurper.jobs.<a href="./src/cloudflare/resources/r2/super_slurper/jobs/jobs.py">resume</a>(job_id, \*, account_id) -> <a href="./src/cloudflare/types/r2/super_slurper/job_resume_response.py">str</a></code>

#### Logs

Types:

```python
from cloudflare.types.r2.super_slurper.jobs import LogListResponse
```

Methods:

- <code title="get /accounts/{account_id}/slurper/jobs/{job_id}/logs">client.r2.super_slurper.jobs.logs.<a href="./src/cloudflare/resources/r2/super_slurper/jobs/logs.py">list</a>(job_id, \*, account_id, \*\*<a href="src/cloudflare/types/r2/super_slurper/jobs/log_list_params.py">params</a>) -> <a href="./src/cloudflare/types/r2/super_slurper/jobs/log_list_response.py">SyncSinglePage[LogListResponse]</a></code>

### ConnectivityPrecheck

Types:

```python
from cloudflare.types.r2.super_slurper import (
    ConnectivityPrecheckSourceResponse,
    ConnectivityPrecheckTargetResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/slurper/source/connectivity-precheck">client.r2.super_slurper.connectivity_precheck.<a href="./src/cloudflare/resources/r2/super_slurper/connectivity_precheck.py">source</a>(\*, account_id, \*\*<a href="src/cloudflare/types/r2/super_slurper/connectivity_precheck_source_params.py">params</a>) -> <a href="./src/cloudflare/types/r2/super_slurper/connectivity_precheck_source_response.py">Optional[ConnectivityPrecheckSourceResponse]</a></code>
- <code title="put /accounts/{account_id}/slurper/target/connectivity-precheck">client.r2.super_slurper.connectivity_precheck.<a href="./src/cloudflare/resources/r2/super_slurper/connectivity_precheck.py">target</a>(\*, account_id, \*\*<a href="src/cloudflare/types/r2/super_slurper/connectivity_precheck_target_params.py">params</a>) -> <a href="./src/cloudflare/types/r2/super_slurper/connectivity_precheck_target_response.py">Optional[ConnectivityPrecheckTargetResponse]</a></code>
