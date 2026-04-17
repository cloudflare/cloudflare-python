# Rulesets

Types:

```python
from cloudflare.types.rulesets import (
    Kind,
    Phase,
    Ruleset,
    RulesetCreateResponse,
    RulesetUpdateResponse,
    RulesetListResponse,
    RulesetGetResponse,
)
```

Methods:

- <code title="post /{accounts_or_zones}/{account_or_zone_id}/rulesets">client.rulesets.<a href="./src/cloudflare/resources/rulesets/rulesets.py">create</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/rulesets/ruleset_create_params.py">params</a>) -> <a href="./src/cloudflare/types/rulesets/ruleset_create_response.py">RulesetCreateResponse</a></code>
- <code title="put /{accounts_or_zones}/{account_or_zone_id}/rulesets/{ruleset_id}">client.rulesets.<a href="./src/cloudflare/resources/rulesets/rulesets.py">update</a>(ruleset_id, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/rulesets/ruleset_update_params.py">params</a>) -> <a href="./src/cloudflare/types/rulesets/ruleset_update_response.py">RulesetUpdateResponse</a></code>
- <code title="get /{accounts_or_zones}/{account_or_zone_id}/rulesets">client.rulesets.<a href="./src/cloudflare/resources/rulesets/rulesets.py">list</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/rulesets/ruleset_list_params.py">params</a>) -> <a href="./src/cloudflare/types/rulesets/ruleset_list_response.py">SyncCursorPagination[RulesetListResponse]</a></code>
- <code title="delete /{accounts_or_zones}/{account_or_zone_id}/rulesets/{ruleset_id}">client.rulesets.<a href="./src/cloudflare/resources/rulesets/rulesets.py">delete</a>(ruleset_id, \*, account_id, zone_id) -> None</code>
- <code title="get /{accounts_or_zones}/{account_or_zone_id}/rulesets/{ruleset_id}">client.rulesets.<a href="./src/cloudflare/resources/rulesets/rulesets.py">get</a>(ruleset_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/rulesets/ruleset_get_response.py">RulesetGetResponse</a></code>

## Phases

Types:

```python
from cloudflare.types.rulesets import PhaseUpdateResponse, PhaseGetResponse
```

Methods:

- <code title="put /{accounts_or_zones}/{account_or_zone_id}/rulesets/phases/{ruleset_phase}/entrypoint">client.rulesets.phases.<a href="./src/cloudflare/resources/rulesets/phases/phases.py">update</a>(ruleset_phase, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/rulesets/phase_update_params.py">params</a>) -> <a href="./src/cloudflare/types/rulesets/phase_update_response.py">PhaseUpdateResponse</a></code>
- <code title="get /{accounts_or_zones}/{account_or_zone_id}/rulesets/phases/{ruleset_phase}/entrypoint">client.rulesets.phases.<a href="./src/cloudflare/resources/rulesets/phases/phases.py">get</a>(ruleset_phase, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/rulesets/phase_get_response.py">PhaseGetResponse</a></code>

### Versions

Types:

```python
from cloudflare.types.rulesets.phases import VersionListResponse, VersionGetResponse
```

Methods:

- <code title="get /{accounts_or_zones}/{account_or_zone_id}/rulesets/phases/{ruleset_phase}/entrypoint/versions">client.rulesets.phases.versions.<a href="./src/cloudflare/resources/rulesets/phases/versions.py">list</a>(ruleset_phase, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/rulesets/phases/version_list_response.py">SyncSinglePage[VersionListResponse]</a></code>
- <code title="get /{accounts_or_zones}/{account_or_zone_id}/rulesets/phases/{ruleset_phase}/entrypoint/versions/{ruleset_version}">client.rulesets.phases.versions.<a href="./src/cloudflare/resources/rulesets/phases/versions.py">get</a>(ruleset_version, \*, ruleset_phase, account_id, zone_id) -> <a href="./src/cloudflare/types/rulesets/phases/version_get_response.py">VersionGetResponse</a></code>

## Rules

Types:

```python
from cloudflare.types.rulesets import (
    BlockRule,
    CompressResponseRule,
    DDoSDynamicRule,
    ExecuteRule,
    ForceConnectionCloseRule,
    LogCustomFieldRule,
    LogRule,
    Logging,
    ManagedChallengeRule,
    RedirectRule,
    RewriteRule,
    RouteRule,
    RulesetRule,
    ScoreRule,
    ServeErrorRule,
    SetCacheSettingsRule,
    SetConfigRule,
    SkipRule,
    RuleCreateResponse,
    RuleDeleteResponse,
    RuleEditResponse,
)
```

Methods:

- <code title="post /{accounts_or_zones}/{account_or_zone_id}/rulesets/{ruleset_id}/rules">client.rulesets.rules.<a href="./src/cloudflare/resources/rulesets/rules.py">create</a>(ruleset_id, \*, account_id, zone_id, \*\*<a href="src/cloudflare/types/rulesets/rule_create_params.py">params</a>) -> <a href="./src/cloudflare/types/rulesets/rule_create_response.py">RuleCreateResponse</a></code>
- <code title="delete /{accounts_or_zones}/{account_or_zone_id}/rulesets/{ruleset_id}/rules/{rule_id}">client.rulesets.rules.<a href="./src/cloudflare/resources/rulesets/rules.py">delete</a>(rule_id, \*, ruleset_id, account_id, zone_id) -> <a href="./src/cloudflare/types/rulesets/rule_delete_response.py">RuleDeleteResponse</a></code>
- <code title="patch /{accounts_or_zones}/{account_or_zone_id}/rulesets/{ruleset_id}/rules/{rule_id}">client.rulesets.rules.<a href="./src/cloudflare/resources/rulesets/rules.py">edit</a>(rule_id, \*, ruleset_id, account_id, zone_id, \*\*<a href="src/cloudflare/types/rulesets/rule_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/rulesets/rule_edit_response.py">RuleEditResponse</a></code>

## Versions

Types:

```python
from cloudflare.types.rulesets import VersionListResponse, VersionGetResponse
```

Methods:

- <code title="get /{accounts_or_zones}/{account_or_zone_id}/rulesets/{ruleset_id}/versions">client.rulesets.versions.<a href="./src/cloudflare/resources/rulesets/versions.py">list</a>(ruleset_id, \*, account_id, zone_id) -> <a href="./src/cloudflare/types/rulesets/version_list_response.py">SyncSinglePage[VersionListResponse]</a></code>
- <code title="delete /{accounts_or_zones}/{account_or_zone_id}/rulesets/{ruleset_id}/versions/{ruleset_version}">client.rulesets.versions.<a href="./src/cloudflare/resources/rulesets/versions.py">delete</a>(ruleset_version, \*, ruleset_id, account_id, zone_id) -> None</code>
- <code title="get /{accounts_or_zones}/{account_or_zone_id}/rulesets/{ruleset_id}/versions/{ruleset_version}">client.rulesets.versions.<a href="./src/cloudflare/resources/rulesets/versions.py">get</a>(ruleset_version, \*, ruleset_id, account_id, zone_id) -> <a href="./src/cloudflare/types/rulesets/version_get_response.py">VersionGetResponse</a></code>
