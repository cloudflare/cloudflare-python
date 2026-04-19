# Workers

Types:

```python
from cloudflare.types.workers import MigrationStep, SingleStepMigration, WorkerMetadata
```

## Beta

### Workers

Types:

```python
from cloudflare.types.workers.beta import Worker, WorkerDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/workers/workers">client.workers.beta.workers.<a href="./src/cloudflare/resources/workers/beta/workers/workers.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/workers/beta/worker_create_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/beta/worker.py">Worker</a></code>
- <code title="put /accounts/{account_id}/workers/workers/{worker_id}">client.workers.beta.workers.<a href="./src/cloudflare/resources/workers/beta/workers/workers.py">update</a>(worker_id, \*, account_id, \*\*<a href="src/cloudflare/types/workers/beta/worker_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/beta/worker.py">Worker</a></code>
- <code title="get /accounts/{account_id}/workers/workers">client.workers.beta.workers.<a href="./src/cloudflare/resources/workers/beta/workers/workers.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/workers/beta/worker_list_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/beta/worker.py">SyncV4PagePaginationArray[Worker]</a></code>
- <code title="delete /accounts/{account_id}/workers/workers/{worker_id}">client.workers.beta.workers.<a href="./src/cloudflare/resources/workers/beta/workers/workers.py">delete</a>(worker_id, \*, account_id) -> <a href="./src/cloudflare/types/workers/beta/worker_delete_response.py">WorkerDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/workers/workers/{worker_id}">client.workers.beta.workers.<a href="./src/cloudflare/resources/workers/beta/workers/workers.py">edit</a>(worker_id, \*, account_id, \*\*<a href="src/cloudflare/types/workers/beta/worker_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/beta/worker.py">Worker</a></code>
- <code title="get /accounts/{account_id}/workers/workers/{worker_id}">client.workers.beta.workers.<a href="./src/cloudflare/resources/workers/beta/workers/workers.py">get</a>(worker_id, \*, account_id) -> <a href="./src/cloudflare/types/workers/beta/worker.py">Worker</a></code>

#### Versions

Types:

```python
from cloudflare.types.workers.beta.workers import Version, VersionDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/workers/workers/{worker_id}/versions">client.workers.beta.workers.versions.<a href="./src/cloudflare/resources/workers/beta/workers/versions.py">create</a>(worker_id, \*, account_id, \*\*<a href="src/cloudflare/types/workers/beta/workers/version_create_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/beta/workers/version.py">Version</a></code>
- <code title="get /accounts/{account_id}/workers/workers/{worker_id}/versions">client.workers.beta.workers.versions.<a href="./src/cloudflare/resources/workers/beta/workers/versions.py">list</a>(worker_id, \*, account_id, \*\*<a href="src/cloudflare/types/workers/beta/workers/version_list_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/beta/workers/version.py">SyncV4PagePaginationArray[Version]</a></code>
- <code title="delete /accounts/{account_id}/workers/workers/{worker_id}/versions/{version_id}">client.workers.beta.workers.versions.<a href="./src/cloudflare/resources/workers/beta/workers/versions.py">delete</a>(version_id, \*, account_id, worker_id) -> <a href="./src/cloudflare/types/workers/beta/workers/version_delete_response.py">VersionDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/workers/workers/{worker_id}/versions/{version_id}">client.workers.beta.workers.versions.<a href="./src/cloudflare/resources/workers/beta/workers/versions.py">get</a>(version_id, \*, account_id, worker_id, \*\*<a href="src/cloudflare/types/workers/beta/workers/version_get_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/beta/workers/version.py">Version</a></code>

## Routes

Types:

```python
from cloudflare.types.workers import (
    RouteCreateResponse,
    RouteUpdateResponse,
    RouteListResponse,
    RouteDeleteResponse,
    RouteGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/workers/routes">client.workers.routes.<a href="./src/cloudflare/resources/workers/routes.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/workers/route_create_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/route_create_response.py">RouteCreateResponse</a></code>
- <code title="put /zones/{zone_id}/workers/routes/{route_id}">client.workers.routes.<a href="./src/cloudflare/resources/workers/routes.py">update</a>(route_id, \*, zone_id, \*\*<a href="src/cloudflare/types/workers/route_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/route_update_response.py">RouteUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/workers/routes">client.workers.routes.<a href="./src/cloudflare/resources/workers/routes.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/workers/route_list_response.py">SyncSinglePage[RouteListResponse]</a></code>
- <code title="delete /zones/{zone_id}/workers/routes/{route_id}">client.workers.routes.<a href="./src/cloudflare/resources/workers/routes.py">delete</a>(route_id, \*, zone_id) -> <a href="./src/cloudflare/types/workers/route_delete_response.py">RouteDeleteResponse</a></code>
- <code title="get /zones/{zone_id}/workers/routes/{route_id}">client.workers.routes.<a href="./src/cloudflare/resources/workers/routes.py">get</a>(route_id, \*, zone_id) -> <a href="./src/cloudflare/types/workers/route_get_response.py">RouteGetResponse</a></code>

## Assets

### Upload

Types:

```python
from cloudflare.types.workers.assets import UploadCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/workers/assets/upload">client.workers.assets.upload.<a href="./src/cloudflare/resources/workers/assets/upload.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/workers/assets/upload_create_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/assets/upload_create_response.py">Optional[UploadCreateResponse]</a></code>

## Scripts

Types:

```python
from cloudflare.types.workers import (
    Script,
    ScriptSetting,
    ScriptUpdateResponse,
    ScriptListResponse,
    ScriptGetResponse,
    ScriptSearchResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/workers/scripts/{script_name}">client.workers.scripts.<a href="./src/cloudflare/resources/workers/scripts/scripts.py">update</a>(script_name, \*, account_id, \*\*<a href="src/cloudflare/types/workers/script_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/script_update_response.py">ScriptUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/workers/scripts">client.workers.scripts.<a href="./src/cloudflare/resources/workers/scripts/scripts.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/workers/script_list_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/script_list_response.py">SyncSinglePage[ScriptListResponse]</a></code>
- <code title="delete /accounts/{account_id}/workers/scripts/{script_name}">client.workers.scripts.<a href="./src/cloudflare/resources/workers/scripts/scripts.py">delete</a>(script_name, \*, account_id, \*\*<a href="src/cloudflare/types/workers/script_delete_params.py">params</a>) -> object</code>
- <code title="get /accounts/{account_id}/workers/scripts/{script_name}">client.workers.scripts.<a href="./src/cloudflare/resources/workers/scripts/scripts.py">get</a>(script_name, \*, account_id) -> str</code>
- <code title="get /accounts/{account_id}/workers/scripts-search">client.workers.scripts.<a href="./src/cloudflare/resources/workers/scripts/scripts.py">search</a>(\*, account_id, \*\*<a href="src/cloudflare/types/workers/script_search_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/script_search_response.py">ScriptSearchResponse</a></code>

### Assets

#### Upload

Types:

```python
from cloudflare.types.workers.scripts.assets import UploadCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/workers/scripts/{script_name}/assets-upload-session">client.workers.scripts.assets.upload.<a href="./src/cloudflare/resources/workers/scripts/assets/upload.py">create</a>(script_name, \*, account_id, \*\*<a href="src/cloudflare/types/workers/scripts/assets/upload_create_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/scripts/assets/upload_create_response.py">Optional[UploadCreateResponse]</a></code>

### Subdomain

Types:

```python
from cloudflare.types.workers.scripts import (
    SubdomainCreateResponse,
    SubdomainDeleteResponse,
    SubdomainGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/workers/scripts/{script_name}/subdomain">client.workers.scripts.subdomain.<a href="./src/cloudflare/resources/workers/scripts/subdomain.py">create</a>(script_name, \*, account_id, \*\*<a href="src/cloudflare/types/workers/scripts/subdomain_create_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/scripts/subdomain_create_response.py">SubdomainCreateResponse</a></code>
- <code title="delete /accounts/{account_id}/workers/scripts/{script_name}/subdomain">client.workers.scripts.subdomain.<a href="./src/cloudflare/resources/workers/scripts/subdomain.py">delete</a>(script_name, \*, account_id) -> <a href="./src/cloudflare/types/workers/scripts/subdomain_delete_response.py">SubdomainDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/workers/scripts/{script_name}/subdomain">client.workers.scripts.subdomain.<a href="./src/cloudflare/resources/workers/scripts/subdomain.py">get</a>(script_name, \*, account_id) -> <a href="./src/cloudflare/types/workers/scripts/subdomain_get_response.py">SubdomainGetResponse</a></code>

### Schedules

Types:

```python
from cloudflare.types.workers.scripts import ScheduleUpdateResponse, ScheduleGetResponse
```

Methods:

- <code title="put /accounts/{account_id}/workers/scripts/{script_name}/schedules">client.workers.scripts.schedules.<a href="./src/cloudflare/resources/workers/scripts/schedules.py">update</a>(script_name, \*, account_id, \*\*<a href="src/cloudflare/types/workers/scripts/schedule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/scripts/schedule_update_response.py">ScheduleUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/workers/scripts/{script_name}/schedules">client.workers.scripts.schedules.<a href="./src/cloudflare/resources/workers/scripts/schedules.py">get</a>(script_name, \*, account_id) -> <a href="./src/cloudflare/types/workers/scripts/schedule_get_response.py">ScheduleGetResponse</a></code>

### Tail

Types:

```python
from cloudflare.types.workers.scripts import (
    ConsumerScript,
    TailCreateResponse,
    TailDeleteResponse,
    TailGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/workers/scripts/{script_name}/tails">client.workers.scripts.tail.<a href="./src/cloudflare/resources/workers/scripts/tail.py">create</a>(script_name, \*, account_id, \*\*<a href="src/cloudflare/types/workers/scripts/tail_create_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/scripts/tail_create_response.py">TailCreateResponse</a></code>
- <code title="delete /accounts/{account_id}/workers/scripts/{script_name}/tails/{id}">client.workers.scripts.tail.<a href="./src/cloudflare/resources/workers/scripts/tail.py">delete</a>(id, \*, account_id, script_name) -> <a href="./src/cloudflare/types/workers/scripts/tail_delete_response.py">TailDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/workers/scripts/{script_name}/tails">client.workers.scripts.tail.<a href="./src/cloudflare/resources/workers/scripts/tail.py">get</a>(script_name, \*, account_id) -> <a href="./src/cloudflare/types/workers/scripts/tail_get_response.py">TailGetResponse</a></code>

### Content

Methods:

- <code title="put /accounts/{account_id}/workers/scripts/{script_name}/content">client.workers.scripts.content.<a href="./src/cloudflare/resources/workers/scripts/content.py">update</a>(script_name, \*, account_id, \*\*<a href="src/cloudflare/types/workers/scripts/content_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/script.py">Script</a></code>
- <code title="get /accounts/{account_id}/workers/scripts/{script_name}/content/v2">client.workers.scripts.content.<a href="./src/cloudflare/resources/workers/scripts/content.py">get</a>(script_name, \*, account_id) -> BinaryAPIResponse</code>

### Settings

Methods:

- <code title="patch /accounts/{account_id}/workers/scripts/{script_name}/script-settings">client.workers.scripts.settings.<a href="./src/cloudflare/resources/workers/scripts/settings.py">edit</a>(script_name, \*, account_id, \*\*<a href="src/cloudflare/types/workers/scripts/setting_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/script_setting.py">ScriptSetting</a></code>
- <code title="get /accounts/{account_id}/workers/scripts/{script_name}/script-settings">client.workers.scripts.settings.<a href="./src/cloudflare/resources/workers/scripts/settings.py">get</a>(script_name, \*, account_id) -> <a href="./src/cloudflare/types/workers/script_setting.py">ScriptSetting</a></code>

### Deployments

Types:

```python
from cloudflare.types.workers.scripts import (
    Deployment,
    DeploymentListResponse,
    DeploymentDeleteResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/workers/scripts/{script_name}/deployments">client.workers.scripts.deployments.<a href="./src/cloudflare/resources/workers/scripts/deployments.py">create</a>(script_name, \*, account_id, \*\*<a href="src/cloudflare/types/workers/scripts/deployment_create_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/scripts/deployment.py">Deployment</a></code>
- <code title="get /accounts/{account_id}/workers/scripts/{script_name}/deployments">client.workers.scripts.deployments.<a href="./src/cloudflare/resources/workers/scripts/deployments.py">list</a>(script_name, \*, account_id) -> <a href="./src/cloudflare/types/workers/scripts/deployment_list_response.py">DeploymentListResponse</a></code>
- <code title="delete /accounts/{account_id}/workers/scripts/{script_name}/deployments/{deployment_id}">client.workers.scripts.deployments.<a href="./src/cloudflare/resources/workers/scripts/deployments.py">delete</a>(deployment_id, \*, account_id, script_name) -> <a href="./src/cloudflare/types/workers/scripts/deployment_delete_response.py">DeploymentDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/workers/scripts/{script_name}/deployments/{deployment_id}">client.workers.scripts.deployments.<a href="./src/cloudflare/resources/workers/scripts/deployments.py">get</a>(deployment_id, \*, account_id, script_name) -> <a href="./src/cloudflare/types/workers/scripts/deployment.py">Deployment</a></code>

### Versions

Types:

```python
from cloudflare.types.workers.scripts import (
    VersionCreateResponse,
    VersionListResponse,
    VersionGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/workers/scripts/{script_name}/versions">client.workers.scripts.versions.<a href="./src/cloudflare/resources/workers/scripts/versions.py">create</a>(script_name, \*, account_id, \*\*<a href="src/cloudflare/types/workers/scripts/version_create_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/scripts/version_create_response.py">VersionCreateResponse</a></code>
- <code title="get /accounts/{account_id}/workers/scripts/{script_name}/versions">client.workers.scripts.versions.<a href="./src/cloudflare/resources/workers/scripts/versions.py">list</a>(script_name, \*, account_id, \*\*<a href="src/cloudflare/types/workers/scripts/version_list_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/scripts/version_list_response.py">SyncV4PagePagination[VersionListResponse]</a></code>
- <code title="get /accounts/{account_id}/workers/scripts/{script_name}/versions/{version_id}">client.workers.scripts.versions.<a href="./src/cloudflare/resources/workers/scripts/versions.py">get</a>(version_id, \*, account_id, script_name) -> <a href="./src/cloudflare/types/workers/scripts/version_get_response.py">VersionGetResponse</a></code>

### Secrets

Types:

```python
from cloudflare.types.workers.scripts import (
    SecretUpdateResponse,
    SecretListResponse,
    SecretGetResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/workers/scripts/{script_name}/secrets">client.workers.scripts.secrets.<a href="./src/cloudflare/resources/workers/scripts/secrets.py">update</a>(script_name, \*, account_id, \*\*<a href="src/cloudflare/types/workers/scripts/secret_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/scripts/secret_update_response.py">Optional[SecretUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/workers/scripts/{script_name}/secrets">client.workers.scripts.secrets.<a href="./src/cloudflare/resources/workers/scripts/secrets.py">list</a>(script_name, \*, account_id) -> <a href="./src/cloudflare/types/workers/scripts/secret_list_response.py">SyncSinglePage[SecretListResponse]</a></code>
- <code title="delete /accounts/{account_id}/workers/scripts/{script_name}/secrets/{secret_name}">client.workers.scripts.secrets.<a href="./src/cloudflare/resources/workers/scripts/secrets.py">delete</a>(secret_name, \*, account_id, script_name, \*\*<a href="src/cloudflare/types/workers/scripts/secret_delete_params.py">params</a>) -> object</code>
- <code title="get /accounts/{account_id}/workers/scripts/{script_name}/secrets/{secret_name}">client.workers.scripts.secrets.<a href="./src/cloudflare/resources/workers/scripts/secrets.py">get</a>(secret_name, \*, account_id, script_name, \*\*<a href="src/cloudflare/types/workers/scripts/secret_get_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/scripts/secret_get_response.py">Optional[SecretGetResponse]</a></code>

### ScriptAndVersionSettings

Types:

```python
from cloudflare.types.workers.scripts import (
    ScriptAndVersionSettingEditResponse,
    ScriptAndVersionSettingGetResponse,
)
```

Methods:

- <code title="patch /accounts/{account_id}/workers/scripts/{script_name}/settings">client.workers.scripts.script_and_version_settings.<a href="./src/cloudflare/resources/workers/scripts/script_and_version_settings.py">edit</a>(script_name, \*, account_id, \*\*<a href="src/cloudflare/types/workers/scripts/script_and_version_setting_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/scripts/script_and_version_setting_edit_response.py">ScriptAndVersionSettingEditResponse</a></code>
- <code title="get /accounts/{account_id}/workers/scripts/{script_name}/settings">client.workers.scripts.script_and_version_settings.<a href="./src/cloudflare/resources/workers/scripts/script_and_version_settings.py">get</a>(script_name, \*, account_id) -> <a href="./src/cloudflare/types/workers/scripts/script_and_version_setting_get_response.py">ScriptAndVersionSettingGetResponse</a></code>

## AccountSettings

Types:

```python
from cloudflare.types.workers import AccountSettingUpdateResponse, AccountSettingGetResponse
```

Methods:

- <code title="put /accounts/{account_id}/workers/account-settings">client.workers.account_settings.<a href="./src/cloudflare/resources/workers/account_settings.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/workers/account_setting_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/account_setting_update_response.py">AccountSettingUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/workers/account-settings">client.workers.account_settings.<a href="./src/cloudflare/resources/workers/account_settings.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/workers/account_setting_get_response.py">AccountSettingGetResponse</a></code>

## Domains

Types:

```python
from cloudflare.types.workers import (
    DomainUpdateResponse,
    DomainListResponse,
    DomainDeleteResponse,
    DomainGetResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/workers/domains">client.workers.domains.<a href="./src/cloudflare/resources/workers/domains.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/workers/domain_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/domain_update_response.py">DomainUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/workers/domains">client.workers.domains.<a href="./src/cloudflare/resources/workers/domains.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/workers/domain_list_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/domain_list_response.py">SyncSinglePage[DomainListResponse]</a></code>
- <code title="delete /accounts/{account_id}/workers/domains/{domain_id}">client.workers.domains.<a href="./src/cloudflare/resources/workers/domains.py">delete</a>(domain_id, \*, account_id) -> <a href="./src/cloudflare/types/workers/domain_delete_response.py">DomainDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/workers/domains/{domain_id}">client.workers.domains.<a href="./src/cloudflare/resources/workers/domains.py">get</a>(domain_id, \*, account_id) -> <a href="./src/cloudflare/types/workers/domain_get_response.py">DomainGetResponse</a></code>

## Subdomains

Types:

```python
from cloudflare.types.workers import SubdomainUpdateResponse, SubdomainGetResponse
```

Methods:

- <code title="put /accounts/{account_id}/workers/subdomain">client.workers.subdomains.<a href="./src/cloudflare/resources/workers/subdomains.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/workers/subdomain_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/subdomain_update_response.py">SubdomainUpdateResponse</a></code>
- <code title="delete /accounts/{account_id}/workers/subdomain">client.workers.subdomains.<a href="./src/cloudflare/resources/workers/subdomains.py">delete</a>(\*, account_id) -> None</code>
- <code title="get /accounts/{account_id}/workers/subdomain">client.workers.subdomains.<a href="./src/cloudflare/resources/workers/subdomains.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/workers/subdomain_get_response.py">SubdomainGetResponse</a></code>

## Observability

### Telemetry

Types:

```python
from cloudflare.types.workers.observability import (
    TelemetryKeysResponse,
    TelemetryQueryResponse,
    TelemetryValuesResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/workers/observability/telemetry/keys">client.workers.observability.telemetry.<a href="./src/cloudflare/resources/workers/observability/telemetry.py">keys</a>(\*, account_id, \*\*<a href="src/cloudflare/types/workers/observability/telemetry_keys_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/observability/telemetry_keys_response.py">SyncSinglePage[TelemetryKeysResponse]</a></code>
- <code title="post /accounts/{account_id}/workers/observability/telemetry/query">client.workers.observability.telemetry.<a href="./src/cloudflare/resources/workers/observability/telemetry.py">query</a>(\*, account_id, \*\*<a href="src/cloudflare/types/workers/observability/telemetry_query_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/observability/telemetry_query_response.py">TelemetryQueryResponse</a></code>
- <code title="post /accounts/{account_id}/workers/observability/telemetry/values">client.workers.observability.telemetry.<a href="./src/cloudflare/resources/workers/observability/telemetry.py">values</a>(\*, account_id, \*\*<a href="src/cloudflare/types/workers/observability/telemetry_values_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/observability/telemetry_values_response.py">SyncSinglePage[TelemetryValuesResponse]</a></code>

### Destinations

Types:

```python
from cloudflare.types.workers.observability import (
    DestinationCreateResponse,
    DestinationUpdateResponse,
    DestinationListResponse,
    DestinationDeleteResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/workers/observability/destinations">client.workers.observability.destinations.<a href="./src/cloudflare/resources/workers/observability/destinations.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/workers/observability/destination_create_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/observability/destination_create_response.py">DestinationCreateResponse</a></code>
- <code title="patch /accounts/{account_id}/workers/observability/destinations/{slug}">client.workers.observability.destinations.<a href="./src/cloudflare/resources/workers/observability/destinations.py">update</a>(slug, \*, account_id, \*\*<a href="src/cloudflare/types/workers/observability/destination_update_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/observability/destination_update_response.py">DestinationUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/workers/observability/destinations">client.workers.observability.destinations.<a href="./src/cloudflare/resources/workers/observability/destinations.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/workers/observability/destination_list_params.py">params</a>) -> <a href="./src/cloudflare/types/workers/observability/destination_list_response.py">SyncSinglePage[DestinationListResponse]</a></code>
- <code title="delete /accounts/{account_id}/workers/observability/destinations/{slug}">client.workers.observability.destinations.<a href="./src/cloudflare/resources/workers/observability/destinations.py">delete</a>(slug, \*, account_id) -> <a href="./src/cloudflare/types/workers/observability/destination_delete_response.py">Optional[DestinationDeleteResponse]</a></code>
