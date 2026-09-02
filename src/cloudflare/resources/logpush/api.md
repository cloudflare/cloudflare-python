# Logpush

## Datasets

### Fields

Types:

```python
from cloudflare.types.logpush.datasets import FieldGetResponse
```

Methods:

- <code title="get /{accounts_or_zones}/{account_or_zone_id}/logpush/datasets/{dataset_id}/fields">client.logpush.datasets.fields.<a href="./src/cloudflare/resources/logpush/datasets/fields.py">get</a>(dataset_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/logpush/datasets/field_get_response.py">Optional[FieldGetResponse]</a></code>

### Jobs

Methods:

- <code title="get /{accounts_or_zones}/{account_or_zone_id}/logpush/datasets/{dataset_id}/jobs">client.logpush.datasets.jobs.<a href="./src/cloudflare/resources/logpush/datasets/jobs.py">get</a>(dataset_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/logpush/logpush_job.py">SyncSinglePage[Optional[LogpushJob]]</a></code>

## Edge

Types:

```python
from cloudflare.types.logpush import InstantLogpushJob
```

Methods:

- <code title="post /zones/{zone_id}/logpush/edge/jobs">client.logpush.edge.<a href="./src/cloudflare/resources/logpush/edge.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/logpush/edge_create_params.py">params</a>) -> <a href="./src/cloudflare/types/logpush/instant_logpush_job.py">Optional[InstantLogpushJob]</a></code>
- <code title="get /zones/{zone_id}/logpush/edge/jobs">client.logpush.edge.<a href="./src/cloudflare/resources/logpush/edge.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/logpush/instant_logpush_job.py">SyncSinglePage[Optional[InstantLogpushJob]]</a></code>

## Jobs

Types:

```python
from cloudflare.types.logpush import LogpushJob, OutputOptions, JobDeleteResponse
```

Methods:

- <code title="post /{accounts_or_zones}/{account_or_zone_id}/logpush/jobs">client.logpush.jobs.<a href="./src/cloudflare/resources/logpush/jobs.py">create</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/logpush/job_create_params.py">params</a>) -> <a href="./src/cloudflare/types/logpush/logpush_job.py">Optional[LogpushJob]</a></code>
- <code title="put /{accounts_or_zones}/{account_or_zone_id}/logpush/jobs/{job_id}">client.logpush.jobs.<a href="./src/cloudflare/resources/logpush/jobs.py">update</a>(job_id, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/logpush/job_update_params.py">params</a>) -> <a href="./src/cloudflare/types/logpush/logpush_job.py">Optional[LogpushJob]</a></code>
- <code title="get /{accounts_or_zones}/{account_or_zone_id}/logpush/jobs">client.logpush.jobs.<a href="./src/cloudflare/resources/logpush/jobs.py">list</a>(\*, account_id, zone_id) -> <a href="./src/cloudflare/types/logpush/logpush_job.py">SyncSinglePage[Optional[LogpushJob]]</a></code>
- <code title="delete /{accounts_or_zones}/{account_or_zone_id}/logpush/jobs/{job_id}">client.logpush.jobs.<a href="./src/cloudflare/resources/logpush/jobs.py">delete</a>(job_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/logpush/job_delete_response.py">Optional[JobDeleteResponse]</a></code>
- <code title="get /{accounts_or_zones}/{account_or_zone_id}/logpush/jobs/{job_id}">client.logpush.jobs.<a href="./src/cloudflare/resources/logpush/jobs.py">get</a>(job_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/logpush/logpush_job.py">Optional[LogpushJob]</a></code>

## Ownership

Types:

```python
from cloudflare.types.logpush import OwnershipValidation, OwnershipCreateResponse
```

Methods:

- <code title="post /{accounts_or_zones}/{account_or_zone_id}/logpush/ownership">client.logpush.ownership.<a href="./src/cloudflare/resources/logpush/ownership.py">create</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/logpush/ownership_create_params.py">params</a>) -> <a href="./src/cloudflare/types/logpush/ownership_create_response.py">Optional[OwnershipCreateResponse]</a></code>
- <code title="post /{accounts_or_zones}/{account_or_zone_id}/logpush/ownership/validate">client.logpush.ownership.<a href="./src/cloudflare/resources/logpush/ownership.py">validate</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/logpush/ownership_validate_params.py">params</a>) -> <a href="./src/cloudflare/types/logpush/ownership_validation.py">Optional[OwnershipValidation]</a></code>

## Transformers

Types:

```python
from cloudflare.types.logpush import (
    TransformerCreateResponse,
    TransformerUpdateResponse,
    TransformerListResponse,
    TransformerDeleteResponse,
    TransformerGetResponse,
    TransformerPreviewResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/logpush/transformers">client.logpush.transformers.<a href="./src/cloudflare/resources/logpush/transformers/transformers.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/logpush/transformer_create_params.py">params</a>) -> <a href="./src/cloudflare/types/logpush/transformer_create_response.py">Optional[TransformerCreateResponse]</a></code>
- <code title="put /accounts/{account_id}/logpush/transformers/{transformer_id}">client.logpush.transformers.<a href="./src/cloudflare/resources/logpush/transformers/transformers.py">update</a>(transformer_id, \*, account_id, \*\*<a href="src/cloudflare/types/logpush/transformer_update_params.py">params</a>) -> <a href="./src/cloudflare/types/logpush/transformer_update_response.py">Optional[TransformerUpdateResponse]</a></code>
- <code title="get /accounts/{account_id}/logpush/transformers">client.logpush.transformers.<a href="./src/cloudflare/resources/logpush/transformers/transformers.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/logpush/transformer_list_response.py">SyncSinglePage[TransformerListResponse]</a></code>
- <code title="delete /accounts/{account_id}/logpush/transformers/{transformer_id}">client.logpush.transformers.<a href="./src/cloudflare/resources/logpush/transformers/transformers.py">delete</a>(transformer_id, \*, account_id) -> <a href="./src/cloudflare/types/logpush/transformer_delete_response.py">Optional[TransformerDeleteResponse]</a></code>
- <code title="get /accounts/{account_id}/logpush/transformers/{transformer_id}">client.logpush.transformers.<a href="./src/cloudflare/resources/logpush/transformers/transformers.py">get</a>(transformer_id, \*, account_id) -> <a href="./src/cloudflare/types/logpush/transformer_get_response.py">Optional[TransformerGetResponse]</a></code>
- <code title="post /accounts/{account_id}/logpush/transformers/preview">client.logpush.transformers.<a href="./src/cloudflare/resources/logpush/transformers/transformers.py">preview</a>(\*, account_id, \*\*<a href="src/cloudflare/types/logpush/transformer_preview_params.py">params</a>) -> <a href="./src/cloudflare/types/logpush/transformer_preview_response.py">SyncSinglePage[TransformerPreviewResponse]</a></code>

### Content

Types:

```python
from cloudflare.types.logpush.transformers import ContentGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/logpush/transformers/{transformer_id}/content">client.logpush.transformers.content.<a href="./src/cloudflare/resources/logpush/transformers/content.py">get</a>(transformer_id, \*, account_id, \*\*<a href="src/cloudflare/types/logpush/transformers/content_get_params.py">params</a>) -> <a href="./src/cloudflare/types/logpush/transformers/content_get_response.py">Optional[ContentGetResponse]</a></code>

### Versions

Types:

```python
from cloudflare.types.logpush.transformers import VersionListResponse
```

Methods:

- <code title="get /accounts/{account_id}/logpush/transformers/{transformer_id}/versions">client.logpush.transformers.versions.<a href="./src/cloudflare/resources/logpush/transformers/versions.py">list</a>(transformer_id, \*, account_id, \*\*<a href="src/cloudflare/types/logpush/transformers/version_list_params.py">params</a>) -> <a href="./src/cloudflare/types/logpush/transformers/version_list_response.py">SyncSinglePage[VersionListResponse]</a></code>

## Validate

Types:

```python
from cloudflare.types.logpush import (
    ValidateDestinationResponse,
    ValidateDestinationExistsResponse,
    ValidateOriginResponse,
)
```

Methods:

- <code title="post /{accounts_or_zones}/{account_or_zone_id}/logpush/validate/destination">client.logpush.validate.<a href="./src/cloudflare/resources/logpush/validate.py">destination</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/logpush/validate_destination_params.py">params</a>) -> <a href="./src/cloudflare/types/logpush/validate_destination_response.py">Optional[ValidateDestinationResponse]</a></code>
- <code title="post /{accounts_or_zones}/{account_or_zone_id}/logpush/validate/destination/exists">client.logpush.validate.<a href="./src/cloudflare/resources/logpush/validate.py">destination_exists</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/logpush/validate_destination_exists_params.py">params</a>) -> <a href="./src/cloudflare/types/logpush/validate_destination_exists_response.py">Optional[ValidateDestinationExistsResponse]</a></code>
- <code title="post /{accounts_or_zones}/{account_or_zone_id}/logpush/validate/origin">client.logpush.validate.<a href="./src/cloudflare/resources/logpush/validate.py">origin</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/logpush/validate_origin_params.py">params</a>) -> <a href="./src/cloudflare/types/logpush/validate_origin_response.py">Optional[ValidateOriginResponse]</a></code>
