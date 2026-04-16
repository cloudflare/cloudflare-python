# Images

## V1

Types:

```python
from cloudflare.types.images import Image, V1ListResponse, V1DeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/images/v1">client.images.v1.<a href="./src/cloudflare/resources/images/v1/v1.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/images/v1_create_params.py">params</a>) -> <a href="./src/cloudflare/types/images/image.py">Image</a></code>
- <code title="get /accounts/{account_id}/images/v1">client.images.v1.<a href="./src/cloudflare/resources/images/v1/v1.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/images/v1_list_params.py">params</a>) -> <a href="./src/cloudflare/types/images/v1_list_response.py">SyncV4PagePagination[V1ListResponse]</a></code>
- <code title="delete /accounts/{account_id}/images/v1/{image_id}">client.images.v1.<a href="./src/cloudflare/resources/images/v1/v1.py">delete</a>(image_id, \*, account_id) -> <a href="./src/cloudflare/types/images/v1_delete_response.py">V1DeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/images/v1/{image_id}">client.images.v1.<a href="./src/cloudflare/resources/images/v1/v1.py">edit</a>(image_id, \*, account_id, \*\*<a href="src/cloudflare/types/images/v1_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/images/image.py">Image</a></code>
- <code title="get /accounts/{account_id}/images/v1/{image_id}">client.images.v1.<a href="./src/cloudflare/resources/images/v1/v1.py">get</a>(image_id, \*, account_id) -> <a href="./src/cloudflare/types/images/image.py">Image</a></code>

### Keys

Types:

```python
from cloudflare.types.images.v1 import Key, KeyUpdateResponse, KeyListResponse, KeyDeleteResponse
```

Methods:

- <code title="put /accounts/{account_id}/images/v1/keys/{signing_key_name}">client.images.v1.keys.<a href="./src/cloudflare/resources/images/v1/keys.py">update</a>(signing_key_name, \*, account_id) -> <a href="./src/cloudflare/types/images/v1/key_update_response.py">KeyUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/images/v1/keys">client.images.v1.keys.<a href="./src/cloudflare/resources/images/v1/keys.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/images/v1/key_list_response.py">KeyListResponse</a></code>
- <code title="delete /accounts/{account_id}/images/v1/keys/{signing_key_name}">client.images.v1.keys.<a href="./src/cloudflare/resources/images/v1/keys.py">delete</a>(signing_key_name, \*, account_id) -> <a href="./src/cloudflare/types/images/v1/key_delete_response.py">KeyDeleteResponse</a></code>

### Stats

Types:

```python
from cloudflare.types.images.v1 import Stat
```

Methods:

- <code title="get /accounts/{account_id}/images/v1/stats">client.images.v1.stats.<a href="./src/cloudflare/resources/images/v1/stats.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/images/v1/stat.py">Stat</a></code>

### Variants

Types:

```python
from cloudflare.types.images.v1 import (
    Variant,
    VariantCreateResponse,
    VariantDeleteResponse,
    VariantEditResponse,
    VariantGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/images/v1/variants">client.images.v1.variants.<a href="./src/cloudflare/resources/images/v1/variants.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/images/v1/variant_create_params.py">params</a>) -> <a href="./src/cloudflare/types/images/v1/variant_create_response.py">VariantCreateResponse</a></code>
- <code title="get /accounts/{account_id}/images/v1/variants">client.images.v1.variants.<a href="./src/cloudflare/resources/images/v1/variants.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/images/v1/variant.py">Variant</a></code>
- <code title="delete /accounts/{account_id}/images/v1/variants/{variant_id}">client.images.v1.variants.<a href="./src/cloudflare/resources/images/v1/variants.py">delete</a>(variant_id, \*, account_id) -> <a href="./src/cloudflare/types/images/v1/variant_delete_response.py">VariantDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/images/v1/variants/{variant_id}">client.images.v1.variants.<a href="./src/cloudflare/resources/images/v1/variants.py">edit</a>(variant_id, \*, account_id, \*\*<a href="src/cloudflare/types/images/v1/variant_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/images/v1/variant_edit_response.py">VariantEditResponse</a></code>
- <code title="get /accounts/{account_id}/images/v1/variants/{variant_id}">client.images.v1.variants.<a href="./src/cloudflare/resources/images/v1/variants.py">get</a>(variant_id, \*, account_id) -> <a href="./src/cloudflare/types/images/v1/variant_get_response.py">VariantGetResponse</a></code>

### Blobs

Methods:

- <code title="get /accounts/{account_id}/images/v1/{image_id}/blob">client.images.v1.blobs.<a href="./src/cloudflare/resources/images/v1/blobs.py">get</a>(image_id, \*, account_id) -> BinaryAPIResponse</code>

## V2

Types:

```python
from cloudflare.types.images import V2ListResponse
```

Methods:

- <code title="get /accounts/{account_id}/images/v2">client.images.v2.<a href="./src/cloudflare/resources/images/v2/v2.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/images/v2_list_params.py">params</a>) -> <a href="./src/cloudflare/types/images/v2_list_response.py">V2ListResponse</a></code>

### DirectUploads

Types:

```python
from cloudflare.types.images.v2 import DirectUploadCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/images/v2/direct_upload">client.images.v2.direct_uploads.<a href="./src/cloudflare/resources/images/v2/direct_uploads.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/images/v2/direct_upload_create_params.py">params</a>) -> <a href="./src/cloudflare/types/images/v2/direct_upload_create_response.py">DirectUploadCreateResponse</a></code>
