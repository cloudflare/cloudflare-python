# LeakedCredentialChecks

Types:

```python
from cloudflare.types.leaked_credential_checks import (
    LeakedCredentialCheckCreateResponse,
    LeakedCredentialCheckGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/leaked-credential-checks">client.leaked_credential_checks.<a href="./src/cloudflare/resources/leaked_credential_checks/leaked_credential_checks.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/leaked_credential_checks/leaked_credential_check_create_params.py">params</a>) -> <a href="./src/cloudflare/types/leaked_credential_checks/leaked_credential_check_create_response.py">LeakedCredentialCheckCreateResponse</a></code>
- <code title="get /zones/{zone_id}/leaked-credential-checks">client.leaked_credential_checks.<a href="./src/cloudflare/resources/leaked_credential_checks/leaked_credential_checks.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/leaked_credential_checks/leaked_credential_check_get_response.py">LeakedCredentialCheckGetResponse</a></code>

## Detections

Types:

```python
from cloudflare.types.leaked_credential_checks import (
    DetectionCreateResponse,
    DetectionUpdateResponse,
    DetectionListResponse,
    DetectionGetResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/leaked-credential-checks/detections">client.leaked_credential_checks.detections.<a href="./src/cloudflare/resources/leaked_credential_checks/detections.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/leaked_credential_checks/detection_create_params.py">params</a>) -> <a href="./src/cloudflare/types/leaked_credential_checks/detection_create_response.py">DetectionCreateResponse</a></code>
- <code title="put /zones/{zone_id}/leaked-credential-checks/detections/{detection_id}">client.leaked_credential_checks.detections.<a href="./src/cloudflare/resources/leaked_credential_checks/detections.py">update</a>(detection_id, \*, zone_id, \*\*<a href="src/cloudflare/types/leaked_credential_checks/detection_update_params.py">params</a>) -> <a href="./src/cloudflare/types/leaked_credential_checks/detection_update_response.py">DetectionUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/leaked-credential-checks/detections">client.leaked_credential_checks.detections.<a href="./src/cloudflare/resources/leaked_credential_checks/detections.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/leaked_credential_checks/detection_list_response.py">SyncSinglePage[DetectionListResponse]</a></code>
- <code title="delete /zones/{zone_id}/leaked-credential-checks/detections/{detection_id}">client.leaked_credential_checks.detections.<a href="./src/cloudflare/resources/leaked_credential_checks/detections.py">delete</a>(detection_id, \*, zone_id) -> object</code>
- <code title="get /zones/{zone_id}/leaked-credential-checks/detections/{detection_id}">client.leaked_credential_checks.detections.<a href="./src/cloudflare/resources/leaked_credential_checks/detections.py">get</a>(detection_id, \*, zone_id) -> <a href="./src/cloudflare/types/leaked_credential_checks/detection_get_response.py">DetectionGetResponse</a></code>
