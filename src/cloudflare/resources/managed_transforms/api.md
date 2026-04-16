# ManagedTransforms

Types:

```python
from cloudflare.types.managed_transforms import (
    ManagedTransformListResponse,
    ManagedTransformEditResponse,
)
```

Methods:

- <code title="get /zones/{zone_id}/managed_headers">client.managed_transforms.<a href="./src/cloudflare/resources/managed_transforms/managed_transforms.py">list</a>(\*, zone_id) -> <a href="./src/cloudflare/types/managed_transforms/managed_transform_list_response.py">ManagedTransformListResponse</a></code>
- <code title="delete /zones/{zone_id}/managed_headers">client.managed_transforms.<a href="./src/cloudflare/resources/managed_transforms/managed_transforms.py">delete</a>(\*, zone_id) -> None</code>
- <code title="patch /zones/{zone_id}/managed_headers">client.managed_transforms.<a href="./src/cloudflare/resources/managed_transforms/managed_transforms.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/managed_transforms/managed_transform_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/managed_transforms/managed_transform_edit_response.py">ManagedTransformEditResponse</a></code>
