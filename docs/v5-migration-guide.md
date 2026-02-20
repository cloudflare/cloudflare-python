# Migration Guide: v4.3.1 → v5

This guide helps you migrate your code from v4.3.1 to v5 of the Cloudflare Python SDK.

## Overview

Version 5 introduces several breaking changes across multiple resources. This guide provides detailed migration instructions for each affected resource.

**Important**: This is a beta release. APIs and types may change before the final v5.0.0 release.

## Quick Reference

Resources with breaking changes:

- [Abuse Reports](#abuse-reports)
- [ACM Total TLS](#acm-total-tls)
- [API Gateway Configurations](#api-gateway-configurations)
- [Cloudforce One Threat Events](#cloudforce-one-threat-events)
- [D1 Database](#d1-database)
- [Intel Indicator Feeds](#intel-indicator-feeds)
- [Logpush Edge](#logpush-edge)
- [Origin TLS Client Auth Hostnames](#origin-tls-client-auth-hostnames)
- [Queues Consumers](#queues-consumers)
- [Radar BGP](#radar-bgp)
- [Rulesets Rules](#rulesets-rules)
- [Schema Validation Schemas](#schema-validation-schemas)
- [Snippets](#snippets)
- [Zero Trust DLP](#zero-trust-dlp)
- [Zero Trust Networks](#zero-trust-networks)

---

## Abuse Reports

**Resource**: `abusereports`

### Overview

This resource has breaking changes.

### Changes

#### 1. `create()` endpoint changed from `post /accounts/{account_id}/abuse-reports/{report_type}` to `post /accounts/{account_id}/abuse-reports/{report_param}`

**Actions Needed:**

Review the changes above and update your code accordingly.

---

## ACM Total TLS

**Resource**: `acm.totaltls`

### Overview

The ACM Total TLS resource has undergone a method restructuring in v5. The `create()` method has been removed and replaced with two new methods: `update()` and `edit()`, both of which perform similar functionality but with slightly different semantics.

### Changes

#### 1. Removed `create()` Method

**What changed:**

The `create()` method has been completely removed and replaced with `update()` and `edit()` methods. Both new methods use the same endpoint (`POST /zones/{zone_id}/acm/total_tls`) and similar parameters.

**Before (v4.3.1):**

```python
client.acm.total_tls.create(
    zone_id="023e105f4ecef8ad9ca31a8372d0c353",
    enabled=True,
    certificate_authority="google"
)
```

**After (v5):**

```python
# Option 1: Use update()
client.acm.total_tls.update(
    zone_id="023e105f4ecef8ad9ca31a8372d0c353",
    enabled=True,
    certificate_authority="google"
)

# Option 2: Use edit()
client.acm.total_tls.edit(
    zone_id="023e105f4ecef8ad9ca31a8372d0c353",
    enabled=True,
    certificate_authority="google"
)
```

**Actions Needed:**

1. Replace all calls to `create()` with either `update()` or `edit()`
2. The parameters remain the same: `zone_id`, `enabled`, and optional `certificate_authority`
3. Update import statements if needed:
   - Remove: `from cloudflare.types.acm.total_tls_create_response import TotalTLSCreateResponse`
   - Add: `from cloudflare.types.acm.total_tls_update_response import TotalTLSUpdateResponse`
   - Or: `from cloudflare.types.acm.total_tls_edit_response import TotalTLSEditResponse`

---

#### 2. Updated Default Value Handling

**What changed:**

The optional parameter `certificate_authority` now uses the `Omit` type instead of `NotGiven`, and its default value changed from `NOT_GIVEN` to `omit`.

**Before (v4.3.1):**

```python
from cloudflare._types import NOT_GIVEN

result = client.acm.total_tls.create(
    zone_id="023e105f4ecef8ad9ca31a8372d0c353",
    enabled=True,
    certificate_authority=NOT_GIVEN  # Old sentinel value
)
```

**After (v5):**

```python
from cloudflare._types import omit

result = client.acm.total_tls.update(
    zone_id="023e105f4ecef8ad9ca31a8372d0c353",
    enabled=True,
    certificate_authority=omit  # New sentinel value
)
```

**Actions Needed:**

1. If you explicitly used `NOT_GIVEN`, replace it with `omit`
2. Update imports from `NOT_GIVEN` to `omit`
3. If you relied on the default behavior (not passing the parameter), no changes are needed

This is part of a broader SDK improvement to provide more precise type hints and better distinguish between omitted parameters and null values.

---

#### 3. Response Type Changes

**What changed:**

The response type has changed from `TotalTLSCreateResponse` to either `TotalTLSUpdateResponse` or `TotalTLSEditResponse`.

**Before (v4.3.1):**

```python
from cloudflare.types.acm.total_tls_create_response import TotalTLSCreateResponse

result: TotalTLSCreateResponse = client.acm.total_tls.create(
    zone_id="023e105f4ecef8ad9ca31a8372d0c353",
    enabled=True
)
```

**After (v5):**

```python
from cloudflare.types.acm.total_tls_update_response import TotalTLSUpdateResponse

result: TotalTLSUpdateResponse = client.acm.total_tls.update(
    zone_id="023e105f4ecef8ad9ca31a8372d0c353",
    enabled=True
)
```

**Actions Needed:**

1. Update type annotations in your code
2. Update import statements to use the new response types
3. The response structure remains the same, only the type name has changed

Response types were renamed to match the new method names for consistency across the SDK.

---

## API Gateway Configurations

**Resource**: `apigateway.configurations`

### Overview

This resource has breaking changes.

### Changes

#### 1. `ConfigurationUpdateResponse` type removed

**Actions Needed:**

Review the changes above and update your code accordingly.

---

## Cloudforce One Threat Events

**Resource**: `cloudforceone.threatevents`

### Overview

The Cloudforce One Threat Events resource has undergone significant changes in v5. The `insights` and `crons` sub-resources have been completely removed, and the `get()` method has been deprecated. Several method signatures have been updated to make previously required parameters optional and add support for new features like multiple indicators per event.

### Changes

#### 1. Removed `insights` Sub-Resource

**What changed:**

The entire `insights` sub-resource has been removed, including all associated methods (`create()`, `delete()`, `edit()`, `get()`) and their response types.

**Before (v4.3.1):**

```python
from cloudflare import Cloudflare

client = Cloudflare()

insights = client.cloudforce_one.threat_events.insights

result = insights.create(
    account_id="abc123",
)
```

**After (v5):**

```python
# Use the 'insight' parameter when creating events:

result = client.cloudforce_one.threat_events.create(
    path_account_id="abc123",
    category="malware",
    date="2024-01-01T00:00:00Z",
    event="event description",
    raw={"key": "value"},
    tlp="green",
    insight="your insight text here"  # New parameter
)
```

**Actions Needed:**

1. Replace all `insights` sub-resource calls with the main threat events API
2. Use the new `insight` parameter when creating or editing events
3. Update import statements to remove insight-related types:
   - Remove: `InsightCreateResponse`, `InsightDeleteResponse`, `InsightEditResponse`, `InsightGetResponse`
4. Refactor code that accessed `client.cloudforce_one.threat_events.insights` to use the main API

Insights functionality was consolidated into the main threat events resource to simplify the API structure and make it easier to attach insights directly to events.

---

#### 2. Removed `crons` Sub-Resource

**What changed:**

The entire `crons` sub-resource has been completely removed from the threat events API.

**Before (v4.3.1):**

```python
from cloudflare import Cloudflare

client = Cloudflare()

crons = client.cloudforce_one.threat_events.crons
```

**After (v5):**

```python

```

**Actions Needed:**

1. Remove all references to `client.cloudforce_one.threat_events.crons`
2. If you relied on cron functionality, contact Cloudflare support for alternative scheduling solutions
3. Consider using external scheduling mechanisms if needed

The crons functionality was removed as part of the API restructuring. Scheduling operations should be handled outside the threat events API.

---

#### 3. Parameter Changes in `create()` Method

**What changed:**

Several parameters in the `create()` method changed from required to optional, and new parameters were added. The `dataset_id` parameter now has different default behavior.

**Before (v4.3.1):**

```python
result = client.cloudforce_one.threat_events.create(
    path_account_id="abc123",
    attacker="attacker-name",  # Required
    attacker_country="US",      # Required
    category="malware",
    date="2024-01-01T00:00:00Z",
    event="event description",
    indicator_type="ipv4",      # Required
    raw={"key": "value"},
    tlp="green",
    dataset_id="dataset-123"    # Must be specified
)
```

**After (v5):**

```python
result = client.cloudforce_one.threat_events.create(
    path_account_id="abc123",
    category="malware",
    date="2024-01-01T00:00:00Z",
    event="event description",
    raw={"key": "value"},
    tlp="green",
    # Optional parameters:
    attacker="attacker-name",   # Now optional, can be None
    attacker_country="US",       # Now optional
    indicator_type="ipv4",       # Now optional
    dataset_id="dataset-123",    # Optional - uses default if omitted
    indicator="192.168.1.1",     # Single indicator (legacy)
    indicators=[                 # New: Multiple indicators support
        {"type": "ipv4", "value": "192.168.1.1"},
        {"type": "domain", "value": "malicious.com"}
    ],
    insight="threat intelligence insight"  # New parameter
)
```

**Actions Needed:**

1. Update method calls - `attacker`, `attacker_country`, and `indicator_type` are now optional
2. If you want to omit the attacker, set it to `None` explicitly or use the `omit` sentinel
3. Consider using the new `indicators` array parameter for events with multiple indicators
4. If you were always specifying `dataset_id`, continue doing so; if not specified, events will be created in the default "Cloudforce One Threat Events" dataset
5. Add `insight` parameter when you want to attach insights to events

The changes make the API more flexible by allowing events to be created without always specifying an attacker, and enable more complex scenarios like events with multiple indicators. The default dataset behavior simplifies usage for common cases.

---

#### 4. Parameter Changes in `list()` Method

**What changed:**

The `list()` method now supports cursor-based pagination and STIX2 format export. The `dataset_id` parameter behavior changed.

**Before (v4.3.1):**

```python
from typing import List

result = client.cloudforce_one.threat_events.list(
    account_id="abc123",
    dataset_id=["dataset-123"],  # Required, as List[str]
    page=1,
    page_size=50
)
```

**After (v5):**

```python
from cloudflare._types import SequenceNotStr

result = client.cloudforce_one.threat_events.list(
    account_id="abc123",
    dataset_id=["dataset-123"],  # Optional, now SequenceNotStr[str]
    cursor="cursor-token",        # New: cursor-based pagination
    format="json",                # New: "json" or "stix2"
    page=1,
    page_size=50
)
```

**Actions Needed:**

1. The `dataset_id` parameter is now optional - omit it to list from the default dataset
2. Update type hints from `List[str]` to `SequenceNotStr[str]` if you have explicit type annotations
3. For large result sets (beyond 100,000 records), use the new `cursor` parameter for better performance:
   ```python
   # First request
   result = client.cloudforce_one.threat_events.list(
       account_id="abc123",
       page_size=50
   )

   # Get next page using cursor
   next_cursor = result.result_info.cursor
   result = client.cloudforce_one.threat_events.list(
       account_id="abc123",
       cursor=next_cursor,
       page_size=50
   )
   ```
4. Use `format="stix2"` if you need STIX2-formatted output

Cursor-based pagination provides better performance and supports deep pagination beyond the 100,000 record limit of offset-based pagination. STIX2 format support enables better integration with threat intelligence platforms.

---

#### 5. Deprecated `get()` Method

**What changed:**

The `get()` method is now deprecated and marked for removal in a future version.

**Before (v4.3.1):**

```python
result = client.cloudforce_one.threat_events.get(
    event_id="event-123",
    account_id="abc123"
)
```

**After (v5):**

```python
result = client.cloudforce_one.threat_events.get(
    event_id="event-123",
    account_id="abc123"
)

# Use the dataset-specific endpoint via the datasets sub-resource:
result = client.cloudforce_one.threat_events.datasets.events.get(
    dataset_id="dataset-123",
    event_id="event-123",
    account_id="abc123"
)
```

**Actions Needed:**

1. Migrate away from the deprecated `get()` method as soon as possible
2. Use the dataset-specific events endpoint: `/events/dataset/:dataset_id/events/:event_id`
3. Access this via the datasets sub-resource API (refer to datasets documentation)
4. Update your code to handle the new endpoint structure

The new API structure requires dataset context for retrieving individual events, providing better data organization and access control.

---

#### 6. Parameter Changes in `edit()` Method

**What changed:**

The `edit()` method now supports additional optional parameters including `created_at`, `dataset_id`, `insight`, and `raw`.

**Before (v4.3.1):**

```python
result = client.cloudforce_one.threat_events.edit(
    event_id="event-123",
    account_id="abc123",
    attacker="new-attacker",
    category="malware",
    date="2024-01-01T00:00:00Z"
)
```

**After (v5):**

```python
result = client.cloudforce_one.threat_events.edit(
    event_id="event-123",
    account_id="abc123",
    attacker="new-attacker",  # Can now be None
    category="malware",
    date="2024-01-01T00:00:00Z",
    # New optional parameters:
    created_at="2024-01-01T00:00:00Z",
    dataset_id="dataset-123",
    insight="updated insight",
    raw={"updated": "data"}
)
```

**Actions Needed:**

1. No changes required for existing code
2. Optionally use new parameters to update additional fields:
   - Use `created_at` to set the creation timestamp
   - Use `dataset_id` to move events between datasets
   - Use `insight` to update or add insights
   - Use `raw` to update raw event data
3. The `attacker` parameter can now be set to `None` to remove the attacker

Additional parameters provide more comprehensive event editing capabilities and better align with the new event model that includes insights and dataset references.

---

#### 7. Parameter Changes in `bulk_create()` Method

**What changed:**

The `bulk_create()` method now supports an optional `include_created_events` parameter.

**Before (v4.3.1):**

```python
result = client.cloudforce_one.threat_events.bulk_create(
    account_id="abc123",
    data=[
        {"category": "malware", "date": "2024-01-01T00:00:00Z", ...},
        {"category": "phishing", "date": "2024-01-02T00:00:00Z", ...}
    ],
    dataset_id="dataset-123"
)
```

**After (v5):**

```python
result = client.cloudforce_one.threat_events.bulk_create(
    account_id="abc123",
    data=[
        {"category": "malware", "date": "2024-01-01T00:00:00Z", ...},
        {"category": "phishing", "date": "2024-01-02T00:00:00Z", ...}
    ],
    dataset_id="dataset-123",
    include_created_events=True  # New parameter
)

```

**Actions Needed:**

1. No changes required for existing code
2. Set `include_created_events=True` if you need to track which events were created and their locations:
   ```python
   result = client.cloudforce_one.threat_events.bulk_create(
       account_id="abc123",
       data=events_data,
       dataset_id="dataset-123",
       include_created_events=True
   )

   # Access created event details
   for event in result.created_events:
       print(f"Created event {event.uuid} on shard {event.shard_id}")
   ```

The new parameter provides better tracking and debugging capabilities for bulk operations, allowing developers to verify which events were successfully created and where they're stored.

---

## D1 Database

**Resource**: `d1.database`

### Overview

The D1 Database resource has been **completely rewritten** in v5. While the new implementation provides all the same core functionality, the API surface has changed significantly. All methods that existed in v4.3.1 have been removed and replaced with new implementations that have different signatures, particularly around path structure and method organization.

**IMPORTANT:** Despite methods having the same names (e.g., `create()`, `delete()`, etc.), the new implementation is **not** a drop-in replacement. The path parameter structure has changed, requiring code updates.

### Changes

#### 1. Complete Resource Reimplementation

**What changed:**

The entire D1 Database resource was regenerated from the updated OpenAPI specification. While method names remain similar, the internal implementation and some signatures have changed.

**Impact:**
This affects all methods: `create()`, `update()`, `list()`, `delete()`, `edit()`, `export()`, `get()`, `params()`, `query()`, `raw()`, and `import_()`.

---

#### 2. Changed Path Structure for `create()` Method

**What changed:**

The endpoint path and parameter structure for creating databases has changed.

**Before (v4.3.1):**

```python
from cloudflare import Cloudflare

client = Cloudflare()

result = client.d1.database.create(
    account_id="abc123",
    name="my-database",
)
```

**After (v5):**

```python
from cloudflare import Cloudflare

client = Cloudflare()

result = client.d1.database.create(
    account_id="abc123",
    name="my-database",
    jurisdiction="eu",                    # Optional
    primary_location_hint="weur"          # Optional
)
```

**Actions Needed:**

1. Update the `create()` method call to use the new parameter structure
2. Use the optional `jurisdiction` parameter to restrict where the D1 database runs and stores data:
   - Values: `"eu"` or `"fedramp"`
3. Use the optional `primary_location_hint` parameter to specify the region:
   - Values: `"wnam"`, `"enam"`, `"weur"`, `"eeur"`, `"apac"`, `"oc"`
4. Note: If `jurisdiction` is specified, the `primary_location_hint` is ignored

The new implementation provides explicit control over data residency and regional placement, which is important for compliance and performance requirements.

---

#### 3. New `update()` Method with Different Purpose

**What changed:**

The `update()` method now specifically handles read replication configuration.

**Before (v4.3.1):**

```python
result = client.d1.database.update(
)
```

**After (v5):**

```python
result = client.d1.database.update(
    database_id="def456",
    account_id="abc123",
    read_replication={
        "enabled": True,
        "regions": ["weur", "enam"]
    }
)
```

**Actions Needed:**

1. The `update()` method now requires a `database_id` as the first positional parameter
2. The method specifically handles read replication configuration
3. For other database updates, use the new `edit()` method (PATCH) instead
4. The `read_replication` parameter is required and must include:
   - `enabled`: Boolean flag
   - `regions`: Optional list of regions for read replicas

The separation of `update()` (PUT - full updates) and `edit()` (PATCH - partial updates) follows RESTful conventions more closely and provides clearer semantics for different types of updates.

---

#### 4. New `edit()` Method for Partial Updates

**What changed:**

A new `edit()` method was added for partial updates using HTTP PATCH.

**Before (v4.3.1):**

```python

```

**After (v5):**

```python
result = client.d1.database.edit(
    database_id="def456",
    account_id="abc123",
    read_replication={
        "enabled": True
    }
)
```

**Actions Needed:**

1. Use `edit()` for partial updates where you want to modify specific fields
2. Use `update()` when you want to replace the entire configuration
3. Both methods currently support `read_replication` configuration
4. The `database_id` is required as the first positional parameter

Having both `update()` and `edit()` methods provides flexibility for different update scenarios and follows standard REST API patterns.

---

#### 5. Updated `list()` Method Return Type

**What changed:**

The `list()` method now returns a paginated response type instead of a simple list.

**Before (v4.3.1):**

```python
result = client.d1.database.list(
    account_id="abc123"
)
```

**After (v5):**

```python
from cloudflare.pagination import SyncV4PagePaginationArray

result = client.d1.database.list(
    account_id="abc123",
    name="search-term",  # Optional: filter by name
    page=1,              # Optional: page number
    per_page=20          # Optional: items per page
)

for database in result:
    print(database.name)
```

**Actions Needed:**

1. Update code that expects a simple list to handle pagination
2. Use the new optional parameters for filtering and pagination:
   - `name`: Search for databases by name
   - `page`: Specify page number (1-indexed)
   - `per_page`: Set number of items per page
3. Iterate through the paginated results or convert to a list if needed:
   ```python
   all_databases = list(result)
   ```

Pagination support allows efficient handling of large numbers of databases and follows the standard pattern used across the Cloudflare API.

---

#### 6. Changed `delete()` Method Return Type

**What changed:**

The `delete()` method now returns a generic `object` type instead of a specific response type.

**Before (v4.3.1):**

```python
result = client.d1.database.delete(
    database_id="def456",
    account_id="abc123"
)
```

**After (v5):**

```python
result = client.d1.database.delete(
    database_id="def456",
    account_id="abc123"
)
```

**Actions Needed:**

1. Update type annotations to expect `object` instead of a specific response type
2. The method signature requires `database_id` as the first positional parameter
3. The operation still returns a confirmation, but without a specific type structure

The generic return type simplifies the API and aligns with the actual API behavior.

---

#### 7. Enhanced `export()` Method

**What changed:**

The `export()` method now has a clearer parameter structure with required and optional fields.

**Before (v4.3.1):**

```python
result = client.d1.database.export(
)
```

**After (v5):**

```python
result = client.d1.database.export(
    database_id="def456",
    account_id="abc123",
    output_format="polling",      # Required: must be "polling"
    current_bookmark="bookmark",  # Optional: for polling in-progress export
    dump_options={                # Optional: export configuration
        "no_data": False,
        "no_schema": False,
        "tables": ["table1", "table2"]
    }
)

while result.status == "in_progress":
    result = client.d1.database.export(
        database_id="def456",
        account_id="abc123",
        output_format="polling",
        current_bookmark=result.bookmark
    )

if result.status == "complete":
    download_url = result.url
```

**Actions Needed:**

1. Always specify `output_format="polling"` (currently the only supported format)
2. Use the `current_bookmark` parameter to poll for export completion
3. Configure export options using `dump_options`:
   - `no_data`: Set to `True` to export schema only
   - `no_schema`: Set to `True` to export data only
   - `tables`: List specific tables to export
4. Implement polling logic to wait for export completion
5. Note: Exports block the database, so continue polling to avoid automatic cancellation

The new structure makes the async export process more explicit and provides better control over what gets exported.

---

#### 8. Restructured `import_()` Method with Overloads

**What changed:**

The `import_()` method now uses overloaded signatures for different import actions.

**Before (v4.3.1):**

```python
result = client.d1.database.import_(
)
```

**After (v5):**

```python

result = client.d1.database.import_(
    database_id="def456",
    account_id="abc123",
    action="init",
    etag="md5-hash-of-file"
)
upload_url = result.upload_url

result = client.d1.database.import_(
    database_id="def456",
    account_id="abc123",
    action="ingest",
    etag="md5-hash-of-file",
    filename="uploaded-filename"
)

result = client.d1.database.import_(
    database_id="def456",
    account_id="abc123",
    action="poll",
    current_bookmark="bookmark-from-ingest"
)
```

**Actions Needed:**

1. Break your import logic into three stages:

   **Stage 1: Initialize**
   ```python
   import hashlib

   # Calculate MD5 hash
   with open("database.sql", "rb") as f:
       etag = hashlib.md5(f.read()).hexdigest()

   # Get upload URL
   result = client.d1.database.import_(
       database_id="def456",
       account_id="abc123",
       action="init",
       etag=etag
   )
   ```

   **Stage 2: Upload and Ingest**
   ```python
   # Upload file to the URL (use requests or similar)
   import requests
   with open("database.sql", "rb") as f:
       requests.put(result.upload_url, data=f)

   # Trigger import
   result = client.d1.database.import_(
       database_id="def456",
       account_id="abc123",
       action="ingest",
       etag=etag,
       filename="database.sql"
   )
   bookmark = result.bookmark
   ```

   **Stage 3: Poll for Completion**
   ```python
   while True:
       status = client.d1.database.import_(
           database_id="def456",
           account_id="abc123",
           action="poll",
           current_bookmark=bookmark
       )
       if status.status == "complete":
           break
       time.sleep(5)
   ```

2. Always calculate and provide the MD5 etag of your SQL file
3. Use the `current_bookmark` to track import progress
4. Note: Imports block the database for their duration

The overloaded signatures make each import stage explicit and type-safe, reducing errors and making the multi-step process clearer.

---

#### 9. Enhanced `query()` Method with Overloads

**What changed:**

The `query()` method now supports both single-query and batch-query modes via overloads.

**Before (v4.3.1):**

```python
result = client.d1.database.query(
)
```

**After (v5):**

```python
from cloudflare.pagination import SyncSinglePage

result = client.d1.database.query(
    database_id="def456",
    account_id="abc123",
    sql="SELECT * FROM users WHERE id = ?",
    params=["123"]  # Optional: parameterized query
)

result = client.d1.database.query(
    database_id="def456",
    account_id="abc123",
    batch=[
        {"sql": "SELECT * FROM users", "params": []},
        {"sql": "SELECT * FROM posts", "params": []}
    ]
)

for query_result in result:
    for row in query_result.results:
        print(row)
```

**Actions Needed:**

1. For single queries, use the `sql` parameter with optional `params`:
   ```python
   result = client.d1.database.query(
       database_id="def456",
       account_id="abc123",
       sql="SELECT * FROM users WHERE active = ?",
       params=["true"]
   )
   ```

2. For batch queries, use the `batch` parameter:
   ```python
   result = client.d1.database.query(
       database_id="def456",
       account_id="abc123",
       batch=[
           {"sql": "BEGIN TRANSACTION"},
           {"sql": "INSERT INTO users (name) VALUES (?)", "params": ["John"]},
           {"sql": "COMMIT"}
       ]
   )
   ```

3. The return type is now `SyncSinglePage[QueryResult]` for pagination support
4. Use parameterized queries (the `params` array) to prevent SQL injection
5. Multiple statements in a single SQL string (separated by semicolons) are also supported

Overloads provide type safety for different query modes, and the batch mode enables efficient execution of multiple queries with transaction support.

---

#### 10. Enhanced `raw()` Method with Overloads

**What changed:**

The `raw()` method now supports both single-query and batch-query modes, similar to `query()`, but returns results as arrays instead of objects for better performance.

**Before (v4.3.1):**

```python
result = client.d1.database.raw(
)
```

**After (v5):**

```python
from cloudflare.pagination import SyncSinglePage

result = client.d1.database.raw(
    database_id="def456",
    account_id="abc123",
    sql="SELECT id, name, email FROM users",
    params=[]
)

for query_result in result:
    for row in query_result.results:
        # row = [1, "John", "john@example.com"]
        user_id, name, email = row
        print(f"{user_id}: {name} <{email}>")

result = client.d1.database.raw(
    database_id="def456",
    account_id="abc123",
    batch=[
        {"sql": "SELECT * FROM users"},
        {"sql": "SELECT * FROM posts"}
    ]
)
```

**Actions Needed:**

1. Use `raw()` instead of `query()` when you need better performance
2. Adapt your code to handle array results instead of object results:

   **Before (with query()):**
   ```python
   result = client.d1.database.query(
       database_id="def456",
       account_id="abc123",
       sql="SELECT id, name FROM users"
   )
   for row in result[0].results:
       print(row.id, row.name)  # Object access
   ```

   **After (with raw()):**
   ```python
   result = client.d1.database.raw(
       database_id="def456",
       account_id="abc123",
       sql="SELECT id, name FROM users"
   )
   for row in result[0].results:
       print(row[0], row[1])  # Array access
       # Or use tuple unpacking:
       user_id, name = row
       print(user_id, name)
   ```

3. Use the `columns` field to map array indices to column names if needed:
   ```python
   query_result = list(result)[0]
   columns = {name: idx for idx, name in enumerate(query_result.columns)}

   for row in query_result.results:
       user_id = row[columns["id"]]
       name = row[columns["name"]]
   ```

4. Batch queries work the same way as in `query()`

The `raw()` method provides a performance-optimized alternative to `query()` by returning results as arrays instead of objects, reducing memory overhead and serialization time for large result sets.

---

#### 11. Removed `params()` Method

**What changed:**

The `params()` method has been completely removed with no direct replacement.

**Before (v4.3.1):**

```python
result = client.d1.database.params(
)
```

**After (v5):**

```python
# Use query() or raw() methods with the params parameter instead

result = client.d1.database.query(
    database_id="def456",
    account_id="abc123",
    sql="SELECT * FROM users WHERE id = ?",
    params=["123"]  # Pass params here
)
```

**Actions Needed:**

1. Remove all calls to `params()`
2. Use parameterized queries in `query()` or `raw()` methods:
   ```python
   # Instead of a separate params() call, pass params inline:
   result = client.d1.database.query(
       database_id="def456",
       account_id="abc123",
       sql="SELECT * FROM users WHERE active = ? AND role = ?",
       params=["true", "admin"]
   )
   ```

The functionality was consolidated into the query methods themselves, making parameterized queries more intuitive and eliminating an unnecessary separate method.

---

#### 12. Type Changes: Response Types Removed and Replaced

**What changed:**

Several response types were removed and replaced with new ones.

**Removed Types:**
- `DatabaseImportResponse`
- `DatabaseExportResponse`
- `DatabaseListResponse`
- `DatabaseRawResponse`
- `QueryResult`

**Before (v4.3.1):**

```python
from cloudflare.types.d1 import (
    DatabaseImportResponse,
    DatabaseExportResponse,
    DatabaseListResponse,
    DatabaseRawResponse,
    QueryResult
)
```

**After (v5):**

```python
from cloudflare.types.d1.database_import_response import DatabaseImportResponse
from cloudflare.types.d1.database_export_response import DatabaseExportResponse
from cloudflare.types.d1.database_list_response import DatabaseListResponse
from cloudflare.types.d1.database_raw_response import DatabaseRawResponse
from cloudflare.types.d1.query_result import QueryResult
```

**Actions Needed:**

1. Update import statements to use the new module paths if you import types directly
2. The types themselves may have internal structural changes - review your code that accesses response fields
3. Most code should work without changes if you don't rely on specific type annotations

Types were regenerated from the updated OpenAPI spec to ensure accuracy and maintain consistency with the API.

---

#### 13. Path Parameter Changes Across All Methods

**What changed:**

All methods now require explicit `database_id` where appropriate, moving from a potentially different parameter structure.

**Before (v4.3.1):**

```python
result = client.d1.database.get(
    account_id="abc123",
    database_id="def456"
)
```

**After (v5):**

```python
result = client.d1.database.get(
    database_id="def456",  # First positional parameter
    account_id="abc123"     # Named parameter
)
```

**Actions Needed:**

1. Review all D1 database method calls
2. Ensure `database_id` is passed as the first parameter (after `self`) for methods that operate on specific databases
3. Methods that operate on a specific database:
   - `update(database_id, ...)`
   - `delete(database_id, ...)`
   - `edit(database_id, ...)`
   - `export(database_id, ...)`
   - `get(database_id, ...)`
   - `import_(database_id, ...)`
   - `query(database_id, ...)`
   - `raw(database_id, ...)`

4. Methods that operate at the account level:
   - `create(account_id, ...)` - Creates a new database
   - `list(account_id, ...)` - Lists all databases

Consistent parameter ordering improves API usability and follows RESTful conventions where resource identifiers appear earlier in the method signature.

---

## General Migration Strategy

Given the extensive nature of changes to the D1 Database resource, we recommend the following migration approach:

1. **Audit Your Code:** Identify all locations where you use `client.d1.database.*` methods

2. **Update Method Calls:** Go through each method call and update according to the specific breaking changes documented above

3. **Test Thoroughly:** The reimplementation means you should test all D1-related functionality, even if the method names haven't changed

4. **Update Type Annotations:** If you use explicit type hints, update them to match the new response types

5. **Handle Pagination:** Update code to handle paginated responses from `list()` and query methods

6. **Review Error Handling:** Error responses may have changed; update your error handling code accordingly

7. **Consider Using Raw Queries:** If performance is critical, evaluate switching from `query()` to `raw()` for read operations

## Summary

The D1 Database resource has been completely overhauled in v5. While this provides a more robust and feature-rich API, it requires careful migration. The key changes are:

- All methods have new implementations with updated signatures
- Path parameters are now consistently ordered
- Query methods support both single and batch modes
- Pagination support for list operations
- Better type safety with overloaded method signatures
- Removed `params()` method in favor of inline parameterization
- New `edit()` method for partial updates
- Enhanced import/export workflows with explicit multi-step processes

Plan for significant testing time when migrating D1 Database code to v5.

---

## Intel Indicator Feeds

**Resource**: `intel.indicatorfeeds`

### Overview

The Intel Indicator Feeds resource has undergone a structural change in v5 with the removal of the `downloads` sub-resource. The `get()` method that was previously available under the downloads sub-resource has been removed. The main indicator feeds functionality remains largely intact with minor parameter handling improvements.

### Changes

#### 1. Removed `downloads` Sub-Resource

**What changed:**

The entire `downloads` sub-resource has been completely removed, along with its `get()` method.

**Before (v4.3.1):**

```python
from cloudflare import Cloudflare

client = Cloudflare()

downloads = client.intel.indicator_feeds.downloads

result = downloads.get(
    feed_id=123,
    account_id="abc123"
)
```

**After (v5):**

```python
# Use the main data() method instead:

data = client.intel.indicator_feeds.data(
    feed_id=123,
    account_id="abc123"
)
```

**Actions Needed:**

1. Replace all references to `client.intel.indicator_feeds.downloads` with the main resource
2. Replace `downloads.get()` calls with `indicator_feeds.data()`:

   **Before:**
   ```python
   downloads = client.intel.indicator_feeds.downloads
   result = downloads.get(
       feed_id=123,
       account_id="abc123"
   )
   ```

   **After:**
   ```python
   result = client.intel.indicator_feeds.data(
       feed_id=123,
       account_id="abc123"
   )
   ```

3. Remove any imports related to the downloads sub-resource:
   ```python
   # Remove these imports
   from cloudflare.resources.intel.indicator_feeds.downloads import (
       DownloadsResource,
       AsyncDownloadsResource
   )
   from cloudflare.types.intel.indicator_feeds.download_get_response import (
       DownloadGetResponse
   )
   ```

4. Update type annotations if you were using `DownloadGetResponse`:
   ```python
   # The data() method returns str
   result: str = client.intel.indicator_feeds.data(
       feed_id=123,
       account_id="abc123"
   )
   ```

The downloads functionality was consolidated into the main indicator feeds resource through the `data()` method, simplifying the API structure and eliminating redundant resource nesting.

---

#### 2. Updated Default Value Handling

**What changed:**

Optional parameters now use the `Omit` type instead of `NotGiven`, and default values changed from `NOT_GIVEN` to `omit`.

**Before (v4.3.1):**

```python
from cloudflare._types import NOT_GIVEN, NotGiven

result = client.intel.indicator_feeds.create(
    account_id="abc123",
    name="My Feed",
    description=NOT_GIVEN  # Old sentinel value
)
```

**After (v5):**

```python
from cloudflare._types import omit, Omit

result = client.intel.indicator_feeds.create(
    account_id="abc123",
    name="My Feed",
    description=omit  # New sentinel value
)
```

**Actions Needed:**

1. If you explicitly used `NOT_GIVEN`, replace it with `omit`:
   ```python
   # Before
   from cloudflare._types import NOT_GIVEN

   result = client.intel.indicator_feeds.create(
       account_id="abc123",
       name="My Feed",
       description=NOT_GIVEN
   )

   # After
   from cloudflare._types import omit

   result = client.intel.indicator_feeds.create(
       account_id="abc123",
       name="My Feed",
       description=omit
   )
   ```

2. Update type hints from `NotGiven` to `Omit`:
   ```python
   # Before
   from cloudflare._types import NotGiven

   def create_feed(name: str, description: str | NotGiven = NOT_GIVEN):
       pass

   # After
   from cloudflare._types import Omit, omit

   def create_feed(name: str, description: str | Omit = omit):
       pass
   ```

3. If you relied on the default behavior (not passing optional parameters), no changes are needed:
   ```python
   # This works in both versions
   result = client.intel.indicator_feeds.create(
       account_id="abc123",
       name="My Feed"
   )
   ```

The `Omit` type provides more precise type hints and better distinguishes between omitted parameters and explicit null values, improving type safety across the SDK.

---

#### 3. Consistent Timeout Parameter Type

**What changed:**

The timeout parameter default value changed from `NOT_GIVEN` to `not_given` (note the lowercase).

**Before (v4.3.1):**

```python
from cloudflare._types import NOT_GIVEN

result = client.intel.indicator_feeds.list(
    account_id="abc123",
    timeout=NOT_GIVEN
)
```

**After (v5):**

```python
from cloudflare._types import not_given

result = client.intel.indicator_feeds.list(
    account_id="abc123",
    timeout=not_given
)
```

**Actions Needed:**

1. Replace `NOT_GIVEN` with `not_given` for timeout parameters:
   ```python
   from cloudflare._types import not_given

   # Explicitly set timeout
   result = client.intel.indicator_feeds.list(
       account_id="abc123",
       timeout=30.0  # 30 seconds
   )

   # Or use default
   result = client.intel.indicator_feeds.list(
       account_id="abc123"
       # timeout defaults to not_given
   )
   ```

2. In practice, you rarely need to explicitly pass the sentinel value - just omit the parameter:
   ```python
   # Preferred approach
   result = client.intel.indicator_feeds.list(
       account_id="abc123"
   )
   ```

The lowercase `not_given` is used consistently for timeout parameters across the SDK, while `omit` is used for business logic parameters, providing clearer semantic meaning.

---

#### 4. Updated Method Signatures (Non-Breaking Changes)

**What changed:**

Several methods had their signatures updated to use the new `Omit` type, but the actual behavior remains the same.

**Methods affected:**
- `create()`
- `update()`
- `list()`
- `data()`
- `get()`

**Example - create() method:**
```python
# v4.3.1 signature:
def create(
    self,
    *,
    account_id: str,
    description: str | NotGiven = NOT_GIVEN,
    name: str | NotGiven = NOT_GIVEN,
    ...
) -> Optional[IndicatorFeedCreateResponse]:

# v5 signature:
def create(
    self,
    *,
    account_id: str,
    description: str | Omit = omit,
    name: str | Omit = omit,
    ...
) -> Optional[IndicatorFeedCreateResponse]:
```

**Before (v4.3.1):**

```python
from cloudflare import Cloudflare
from cloudflare._types import NOT_GIVEN

client = Cloudflare()
account_id = "abc123"

feed = client.intel.indicator_feeds.create(
    account_id=account_id,
    name="My Threat Feed",
    description="Threat intelligence feed"
)

downloads = client.intel.indicator_feeds.downloads
data = downloads.get(
    feed_id=feed.id,
    account_id=account_id
)

updated = client.intel.indicator_feeds.update(
    feed_id=feed.id,
    account_id=account_id,
    name="Updated Feed Name",
    description=NOT_GIVEN
)

feeds = client.intel.indicator_feeds.list(
    account_id=account_id
)
```

**After (v5):**

```python
from cloudflare import Cloudflare
from cloudflare._types import omit

client = Cloudflare()
account_id = "abc123"

feed = client.intel.indicator_feeds.create(
    account_id=account_id,
    name="My Threat Feed",
    description="Threat intelligence feed"
)

# Get feed data (no longer uses downloads sub-resource)
data = client.intel.indicator_feeds.data(
    feed_id=feed.id,
    account_id=account_id
)

updated = client.intel.indicator_feeds.update(
    feed_id=feed.id,
    account_id=account_id,
    name="Updated Feed Name",
    description=omit  # Or simply omit the parameter
)

# Or better: just omit optional parameters
updated = client.intel.indicator_feeds.update(
    feed_id=feed.id,
    account_id=account_id,
    name="Updated Feed Name"
)

feeds = client.intel.indicator_feeds.list(
    account_id=account_id
)

# Use new permissions sub-resource
permissions = client.intel.indicator_feeds.permissions.list(
    account_id=account_id
)
```

**Actions Needed:**

These changes are largely transparent if you're using the methods normally:

```python
# This code works in both versions
result = client.intel.indicator_feeds.create(
    account_id="abc123",
    name="My Indicator Feed",
    description="Feed description"
)

# Optional parameters can be omitted
result = client.intel.indicator_feeds.create(
    account_id="abc123",
    name="My Indicator Feed"
)
```

If you have explicit type annotations:
```python
# Before
from cloudflare._types import NotGiven, NOT_GIVEN

def create_feed(
    name: str,
    description: str | NotGiven = NOT_GIVEN
) -> None:
    pass

# After
from cloudflare._types import Omit, omit

def create_feed(
    name: str,
    description: str | Omit = omit
) -> None:
    pass
```

Consistent use of `Omit` across all methods improves type safety and provides better IDE support.

---

## New Features in v5

While not breaking changes, the indicator feeds resource gained new functionality through the permissions sub-resource:

---

## Logpush Edge

**Resource**: `logpush.edge`

### Overview

This resource has breaking changes.

### Changes

#### 1. `get()` endpoint changed from `get /zones/{zone_id}/logpush/edge` to `get /zones/{zone_id}/logpush/edge/jobs`

**Actions Needed:**

Review the changes above and update your code accordingly.

---

## Origin TLS Client Auth Hostnames

**Resource**: `origintlsclientauth.hostnames`

### Overview

This resource has breaking changes.

### Changes

#### 1. `create()` method removed

**Actions Needed:**

Review the changes above and update your code accordingly.

#### 2. `delete()` method removed

**Actions Needed:**

Review the changes above and update your code accordingly.

#### 3. `list()` method removed

**Actions Needed:**

Review the changes above and update your code accordingly.

#### 4. `get()` endpoint changed from `get /zones/{zone_id}/origin_tls_client_auth/hostnames/certificates/{certificate_id}` to `get /zones/{zone_id}/origin_tls_client_auth/hostnames/{hostname}`

**Actions Needed:**

Review the changes above and update your code accordingly.

#### 5. `Certificate` type removed

**Actions Needed:**

Review the changes above and update your code accordingly.

#### 6. `CertificateCreateResponse` type removed

**Actions Needed:**

Review the changes above and update your code accordingly.

#### 7. `CertificateDeleteResponse` type removed

**Actions Needed:**

Review the changes above and update your code accordingly.

#### 8. `CertificateGetResponse` type removed

**Actions Needed:**

Review the changes above and update your code accordingly.

#### 9. `CertificateListResponse` type removed

**Actions Needed:**

Review the changes above and update your code accordingly.

---

## Queues Consumers

**Resource**: `queues.consumers`

### Overview

The Queues Consumers resource has undergone a significant restructuring in v5. The primary breaking change is the modification of the `get()` method endpoint and the addition of a new `list()` method. This change better aligns with RESTful conventions by separating the concerns of listing all consumers from fetching a specific consumer.

### Changes

#### 1. Changed `get()` Method Endpoint and Signature

**What changed:**

The `get()` method endpoint changed from listing all consumers to fetching a specific consumer by ID. A new `list()` method was added to replace the old `get()` behavior.

**Before (v4.3.1):**

```python
from cloudflare import Cloudflare

client = Cloudflare()

consumers = client.queues.consumers.get(
    queue_id="abc123",
    account_id="def456"
)

for consumer in consumers:
    print(f"Consumer: {consumer.consumer_id}")
```

**After (v5):**

```python
from cloudflare import Cloudflare

client = Cloudflare()

consumer = client.queues.consumers.get(
    consumer_id="consumer-123",  # New required parameter
    account_id="def456",
    queue_id="abc123"
)

print(f"Consumer: {consumer.consumer_id}")
```

**Actions Needed:**

1. **If you were listing all consumers**, replace `get()` with `list()`:
   ```python
   # Before
   consumers = client.queues.consumers.get(
       queue_id="abc123",
       account_id="def456"
   )

   # After
   consumers = client.queues.consumers.list(
       queue_id="abc123",
       account_id="def456"
   )

   # Both return an iterable of consumers
   for consumer in consumers:
       print(consumer.consumer_id)
   ```

2. **If you were getting a specific consumer** (by filtering the list), use the new `get()` directly:
   ```python
   # Before (inefficient)
   consumers = client.queues.consumers.get(
       queue_id="abc123",
       account_id="def456"
   )
   consumer = next(c for c in consumers if c.consumer_id == "consumer-123")

   # After (efficient)
   consumer = client.queues.consumers.get(
       consumer_id="consumer-123",
       account_id="def456",
       queue_id="abc123"
   )
   ```

3. **Update type annotations**:
   ```python
   # Before
   from cloudflare.pagination import SyncSinglePage
   from cloudflare.types.queues import Consumer

   consumers: SyncSinglePage[Consumer] = client.queues.consumers.get(...)

   # After - for list()
   from cloudflare.pagination import SyncSinglePage
   from cloudflare.types.queues import Consumer

   consumers: SyncSinglePage[Consumer] = client.queues.consumers.list(...)

   # After - for get()
   from cloudflare.types.queues import Consumer
   from typing import Optional

   consumer: Optional[Consumer] = client.queues.consumers.get(...)
   ```

The change aligns with RESTful API conventions where:
- `GET /resource` returns a list of resources
- `GET /resource/{id}` returns a specific resource by ID

The previous implementation had `get()` returning a list, which was semantically incorrect. Now:
- `list()` returns all consumers for a queue
- `get()` returns a specific consumer by ID

---

#### 2. Added `list()` Method

**What changed:**

A new `list()` method was added to retrieve all consumers for a queue.

**Before (v4.3.1):**

```python
consumers = client.queues.consumers.get(
    queue_id="abc123",
    account_id="def456"
)
```

**After (v5):**

```python
# Use list() to list consumers
consumers = client.queues.consumers.list(
    queue_id="abc123",
    account_id="def456"
)
```

**Actions Needed:**

Simply replace `get()` calls with `list()` when you need all consumers:

```python
from cloudflare import Cloudflare

client = Cloudflare()

# List all consumers for a queue
consumers = client.queues.consumers.list(
    queue_id="abc123",
    account_id="def456"
)

# Iterate through consumers
for consumer in consumers:
    print(f"Consumer ID: {consumer.consumer_id}")
    print(f"Script: {consumer.script_name}")
    print(f"Type: {consumer.type}")
```

The `list()` method name clearly indicates its purpose of listing multiple resources, improving API discoverability and consistency with other Cloudflare resources.

---

#### 3. Updated Default Value Handling

**What changed:**

Optional parameters now use the `Omit` type instead of `NotGiven`, and default values changed from `NOT_GIVEN` to `omit`.

**Before (v4.3.1):**

```python
from cloudflare._types import NOT_GIVEN, NotGiven

result = client.queues.consumers.create(
    queue_id="abc123",
    account_id="def456",
    script_name="my-worker",
    dead_letter_queue=NOT_GIVEN,
    settings=NOT_GIVEN
)
```

**After (v5):**

```python
from cloudflare._types import omit, Omit

result = client.queues.consumers.create(
    queue_id="abc123",
    account_id="def456",
    script_name="my-worker",
    dead_letter_queue=omit,
    settings=omit
)
```

**Actions Needed:**

1. **Replace imports**:
   ```python
   # Before
   from cloudflare._types import NOT_GIVEN, NotGiven

   # After
   from cloudflare._types import omit, Omit
   ```

2. **Replace sentinel values**:
   ```python
   # Before
   result = client.queues.consumers.create(
       queue_id="abc123",
       account_id="def456",
       dead_letter_queue=NOT_GIVEN
   )

   # After
   result = client.queues.consumers.create(
       queue_id="abc123",
       account_id="def456",
       dead_letter_queue=omit
   )
   ```

3. **Update type hints**:
   ```python
   # Before
   from cloudflare._types import NotGiven

   def create_consumer(
       script_name: str,
       settings: dict | NotGiven = NOT_GIVEN
   ) -> None:
       pass

   # After
   from cloudflare._types import Omit, omit

   def create_consumer(
       script_name: str,
       settings: dict | Omit = omit
   ) -> None:
       pass
   ```

4. **Preferred approach - omit optional parameters entirely**:
   ```python
   # Best practice: just don't pass optional parameters
   result = client.queues.consumers.create(
       queue_id="abc123",
       account_id="def456",
       script_name="my-worker"
       # No need to explicitly pass omit for optional parameters
   )
   ```

The `Omit` type provides better type safety and clearer semantics for distinguishing between omitted parameters and explicit null values.

---

#### 4. Consistent Timeout Parameter Handling

**What changed:**

The timeout parameter default value changed from `NOT_GIVEN` to `not_given` (lowercase).

**Before (v4.3.1):**

```python
from cloudflare._types import NOT_GIVEN

result = client.queues.consumers.list(
    queue_id="abc123",
    account_id="def456",
    timeout=NOT_GIVEN
)
```

**After (v5):**

```python
from cloudflare._types import not_given

result = client.queues.consumers.list(
    queue_id="abc123",
    account_id="def456",
    timeout=not_given
)
```

**Actions Needed:**

In practice, you rarely need to explicitly pass the sentinel value:

```python
# Specify a custom timeout
result = client.queues.consumers.list(
    queue_id="abc123",
    account_id="def456",
    timeout=30.0  # 30 seconds
)

# Or use default (preferred)
result = client.queues.consumers.list(
    queue_id="abc123",
    account_id="def456"
    # timeout defaults to not_given
)
```

Consistent use of lowercase `not_given` for infrastructure parameters like timeout improves consistency across the SDK.

---

## Non-Breaking Changes

The following methods retain the same functionality with updated type signatures:

---

## Radar BGP

**Resource**: `radar.bgp`

### Overview

This resource has breaking changes.

### Changes

#### 1. `timeseries()` endpoint changed from `get /radar/bgp/ips/timeseries` to `get /radar/bgp/rpki/aspa/timeseries`

**Actions Needed:**

Review the changes above and update your code accordingly.

#### 2. `IPTimeseriesResponse` type removed

**Actions Needed:**

Review the changes above and update your code accordingly.

---

## Rulesets Rules

**Resource**: `rulesets.rules`

### Overview

This resource has breaking changes.

### Changes

#### 1. `RewriteURIPart` type removed

**Actions Needed:**

Review the changes above and update your code accordingly.

---

## Schema Validation Schemas

**Resource**: `schemavalidation.schemas`

### Overview

This resource has breaking changes.

### Changes

#### 1. `SchemaCreateResponse` type removed

**Actions Needed:**

Review the changes above and update your code accordingly.

#### 2. `SchemaEditResponse` type removed

**Actions Needed:**

Review the changes above and update your code accordingly.

#### 3. `SchemaGetResponse` type removed

**Actions Needed:**

Review the changes above and update your code accordingly.

#### 4. `SchemaListResponse` type removed

**Actions Needed:**

Review the changes above and update your code accordingly.

---

## Snippets

**Resource**: `snippets`

### Overview

This resource has breaking changes.

### Changes

#### 1. `Snippet` type removed

**Actions Needed:**

Review the changes above and update your code accordingly.

---

## Zero Trust DLP

**Resource**: `zerotrust.dlp`

### Overview

This resource has breaking changes.

### Changes

#### 1. `update()` endpoint changed from `put /accounts/{account_id}/dlp/entries/{entry_id}` to `put /accounts/{account_id}/dlp/entries/integration/{entry_id}`

**Actions Needed:**

Review the changes above and update your code accordingly.

#### 2. `EntryCreateResponse` type removed

**Actions Needed:**

Review the changes above and update your code accordingly.

#### 3. `EntryGetResponse` type removed

**Actions Needed:**

Review the changes above and update your code accordingly.

#### 4. `EntryListResponse` type removed

**Actions Needed:**

Review the changes above and update your code accordingly.

#### 5. `EntryUpdateResponse` type removed

**Actions Needed:**

Review the changes above and update your code accordingly.

---

## Zero Trust Networks

**Resource**: `zerotrust.networks`

### Overview

This resource has breaking changes.

### Changes

#### 1. `update()` method removed

**Actions Needed:**

Review the changes above and update your code accordingly.

#### 2. `CloudflareSourceUpdateResponse` type removed

**Actions Needed:**

Review the changes above and update your code accordingly.

---
