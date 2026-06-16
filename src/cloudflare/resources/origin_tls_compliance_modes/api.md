# OriginTLSComplianceModes

Types:

```python
from cloudflare.types.origin_tls_compliance_modes import (
    OriginTLSComplianceModeUpdateResponse,
    OriginTLSComplianceModeDeleteResponse,
    OriginTLSComplianceModeEditResponse,
    OriginTLSComplianceModeGetResponse,
)
```

Methods:

- <code title="put /zones/{zone_id}/settings/origin_tls_compliance_modes">client.origin_tls_compliance_modes.<a href="./src/cloudflare/resources/origin_tls_compliance_modes/origin_tls_compliance_modes.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/origin_tls_compliance_modes/origin_tls_compliance_mode_update_params.py">params</a>) -> <a href="./src/cloudflare/types/origin_tls_compliance_modes/origin_tls_compliance_mode_update_response.py">Optional[OriginTLSComplianceModeUpdateResponse]</a></code>
- <code title="delete /zones/{zone_id}/settings/origin_tls_compliance_modes">client.origin_tls_compliance_modes.<a href="./src/cloudflare/resources/origin_tls_compliance_modes/origin_tls_compliance_modes.py">delete</a>(\*, zone_id) -> <a href="./src/cloudflare/types/origin_tls_compliance_modes/origin_tls_compliance_mode_delete_response.py">Optional[OriginTLSComplianceModeDeleteResponse]</a></code>
- <code title="patch /zones/{zone_id}/settings/origin_tls_compliance_modes">client.origin_tls_compliance_modes.<a href="./src/cloudflare/resources/origin_tls_compliance_modes/origin_tls_compliance_modes.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/origin_tls_compliance_modes/origin_tls_compliance_mode_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/origin_tls_compliance_modes/origin_tls_compliance_mode_edit_response.py">Optional[OriginTLSComplianceModeEditResponse]</a></code>
- <code title="get /zones/{zone_id}/settings/origin_tls_compliance_modes">client.origin_tls_compliance_modes.<a href="./src/cloudflare/resources/origin_tls_compliance_modes/origin_tls_compliance_modes.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/origin_tls_compliance_modes/origin_tls_compliance_mode_get_response.py">Optional[OriginTLSComplianceModeGetResponse]</a></code>
