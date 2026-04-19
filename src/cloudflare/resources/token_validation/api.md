# TokenValidation

## Configuration

Types:

```python
from cloudflare.types.token_validation import (
    TokenConfig,
    ConfigurationDeleteResponse,
    ConfigurationEditResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/token_validation/config">client.token_validation.configuration.<a href="./src/cloudflare/resources/token_validation/configuration/configuration.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/token_validation/configuration_create_params.py">params</a>) -> <a href="./src/cloudflare/types/token_validation/token_config.py">TokenConfig</a></code>
- <code title="get /zones/{zone_id}/token_validation/config">client.token_validation.configuration.<a href="./src/cloudflare/resources/token_validation/configuration/configuration.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/token_validation/configuration_list_params.py">params</a>) -> <a href="./src/cloudflare/types/token_validation/token_config.py">SyncV4PagePaginationArray[TokenConfig]</a></code>
- <code title="delete /zones/{zone_id}/token_validation/config/{config_id}">client.token_validation.configuration.<a href="./src/cloudflare/resources/token_validation/configuration/configuration.py">delete</a>(config_id, \*, zone_id) -> <a href="./src/cloudflare/types/token_validation/configuration_delete_response.py">ConfigurationDeleteResponse</a></code>
- <code title="patch /zones/{zone_id}/token_validation/config/{config_id}">client.token_validation.configuration.<a href="./src/cloudflare/resources/token_validation/configuration/configuration.py">edit</a>(config_id, \*, zone_id, \*\*<a href="src/cloudflare/types/token_validation/configuration_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/token_validation/configuration_edit_response.py">ConfigurationEditResponse</a></code>
- <code title="get /zones/{zone_id}/token_validation/config/{config_id}">client.token_validation.configuration.<a href="./src/cloudflare/resources/token_validation/configuration/configuration.py">get</a>(config_id, \*, zone_id) -> <a href="./src/cloudflare/types/token_validation/token_config.py">TokenConfig</a></code>

### Credentials

Types:

```python
from cloudflare.types.token_validation.configuration import CredentialUpdateResponse
```

Methods:

- <code title="put /zones/{zone_id}/token_validation/config/{config_id}/credentials">client.token_validation.configuration.credentials.<a href="./src/cloudflare/resources/token_validation/configuration/credentials.py">update</a>(config_id, \*, zone_id, \*\*<a href="src/cloudflare/types/token_validation/configuration/credential_update_params.py">params</a>) -> <a href="./src/cloudflare/types/token_validation/configuration/credential_update_response.py">CredentialUpdateResponse</a></code>

## Rules

Types:

```python
from cloudflare.types.token_validation import TokenValidationRule
```

Methods:

- <code title="post /zones/{zone_id}/token_validation/rules">client.token_validation.rules.<a href="./src/cloudflare/resources/token_validation/rules.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/token_validation/rule_create_params.py">params</a>) -> <a href="./src/cloudflare/types/token_validation/token_validation_rule.py">TokenValidationRule</a></code>
- <code title="get /zones/{zone_id}/token_validation/rules">client.token_validation.rules.<a href="./src/cloudflare/resources/token_validation/rules.py">list</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/token_validation/rule_list_params.py">params</a>) -> <a href="./src/cloudflare/types/token_validation/token_validation_rule.py">SyncV4PagePaginationArray[TokenValidationRule]</a></code>
- <code title="delete /zones/{zone_id}/token_validation/rules/{rule_id}">client.token_validation.rules.<a href="./src/cloudflare/resources/token_validation/rules.py">delete</a>(rule_id, \*, zone_id) -> object</code>
- <code title="post /zones/{zone_id}/token_validation/rules/bulk">client.token_validation.rules.<a href="./src/cloudflare/resources/token_validation/rules.py">bulk_create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/token_validation/rule_bulk_create_params.py">params</a>) -> <a href="./src/cloudflare/types/token_validation/token_validation_rule.py">SyncSinglePage[TokenValidationRule]</a></code>
- <code title="patch /zones/{zone_id}/token_validation/rules/bulk">client.token_validation.rules.<a href="./src/cloudflare/resources/token_validation/rules.py">bulk_edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/token_validation/rule_bulk_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/token_validation/token_validation_rule.py">SyncSinglePage[TokenValidationRule]</a></code>
- <code title="patch /zones/{zone_id}/token_validation/rules/{rule_id}">client.token_validation.rules.<a href="./src/cloudflare/resources/token_validation/rules.py">edit</a>(rule_id, \*, zone_id, \*\*<a href="src/cloudflare/types/token_validation/rule_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/token_validation/token_validation_rule.py">TokenValidationRule</a></code>
- <code title="get /zones/{zone_id}/token_validation/rules/{rule_id}">client.token_validation.rules.<a href="./src/cloudflare/resources/token_validation/rules.py">get</a>(rule_id, \*, zone_id) -> <a href="./src/cloudflare/types/token_validation/token_validation_rule.py">TokenValidationRule</a></code>
