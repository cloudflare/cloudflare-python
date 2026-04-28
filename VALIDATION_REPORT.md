# Python SDK Validation Report

**Branch:** `next` (at `9707100e1`)
**Date:** 2026-04-24
**Checkers:** pyright 1.1.399, mypy 1.17, ruff

---

## Summary

| Check   | Result |
|---------|--------|
| ruff    | PASS   |
| pyright | FAIL - 55 errors |
| mypy    | FAIL - 12 errors |

All failures are type-checking errors. There are **4 distinct issues** across 6 source files (+1 test file),
producing the full error count due to cascading type-unknown propagation.

---

## Issue 1: Missing `Required` import in `asset_create_params.py`

**Files:** `src/cloudflare/types/ai/finetunes/asset_create_params.py`
**Error count:** 3 (pyright) + 3 (mypy)
**Error type:** `reportUndefinedVariable` / `name-defined`

### What's wrong

`Required` is used on lines 13, 15, and 18 but is not imported. The import line reads:

```python
from typing_extensions import TypedDict
```

It should be:

```python
from typing_extensions import Required, TypedDict
```

### Change history

| Date       | Commit      | What happened |
|------------|-------------|---------------|
| 2025-01-02 | `4493d6c28` | File created with `Required` import and `Required[str]` on `account_id` |
| 2026-04-19 | `3b83baa3b` | Codegen removed `Required` import AND `Required` usage (made fields optional) |
| 2026-04-23 | `988df8632` | Codegen re-added `Required` to 3 fields BUT did not restore the import |

### Root cause

The `988df8632` commit ("remove account_id and zone_id client options") re-promoted `account_id`, `file`, and
`file_name` back to `Required` status but the codegen output omitted the corresponding
`from typing_extensions import Required` update. This is a Stainless codegen bug -- it emitted `Required` usage
without the import.

### Fix

Add `Required` to the import:

```python
from typing_extensions import Required, TypedDict
```

---

## Issue 2: `SchemaFieldStruct` and `SchemaFieldList` missing `TypedDict` base class

**Files:**
- `src/cloudflare/types/pipelines/sink_create_params.py` (lines 293, 297)
- `src/cloudflare/types/pipelines/stream_create_params.py` (lines 201, 205)

**Error count:** 4 (pyright) + 4 (mypy)
**Error type:** `reportGeneralTypeIssues` + `reportCallIssue` / `call-arg`

### What's wrong

Both classes are declared as:

```python
class SchemaFieldStruct(total=False):
    pass

class SchemaFieldList(total=False):
    pass
```

They should inherit from `TypedDict`:

```python
class SchemaFieldStruct(TypedDict, total=False):
    ...

class SchemaFieldList(TypedDict, total=False):
    ...
```

Without `TypedDict`, these are plain class definitions. `total=False` is passed to
`object.__init_subclass__()` which does not accept that keyword argument.

### Change history

| Date       | Commit      | What happened |
|------------|-------------|---------------|
| 2025-11-12 | `008556f6a` | Pipelines feature introduced these types (generated with stub bodies, had pyright ignores) |
| 2026-02-11 | `1c415a2dd` | **Manual fix**: added `TypedDict` base class, proper `type`, `name`, `fields`/`element` fields |
| 2026-04-19 | `3b83baa3b` | Codegen overwrote the manual fix, regenerating stubs without `TypedDict` base class |

### Root cause

Stainless codegen is emitting empty stub classes for the `struct` and `list` schema field variants. The OpenAPI
spec likely defines these as recursive types (struct has `fields: [SchemaField]`, list has `element: SchemaField`)
which the codegen can't fully resolve, so it emits empty stubs. A previous manual fix (`1c415a2dd`) was
overwritten by subsequent codegen runs.

### Fix

Restore the `TypedDict` base class and proper fields as done in `1c415a2dd`. For both
`sink_create_params.py` and `stream_create_params.py`:

```python
class SchemaFieldStruct(TypedDict, total=False):
    type: Required[Literal["struct"]]
    metadata_key: Optional[str]
    name: str
    required: bool
    sql_name: str
    fields: Optional[List["SchemaField"]]

class SchemaFieldList(TypedDict, total=False):
    type: Required[Literal["list"]]
    metadata_key: Optional[str]
    name: str
    required: bool
    sql_name: str
    element: Optional["SchemaField"]
```

This fix will be overwritten by the next codegen run unless the Stainless config or upstream OpenAPI spec is also
fixed to properly model these recursive types.

---

## Issue 3: Missing `organization_profile_get_params` module

**Files:**
- `src/cloudflare/resources/organizations/organization_profile.py` (line 22)
- `tests/api_resources/organizations/test_organization_profile.py` (line 12)

**Error count:** 22 (pyright) + 1 (mypy) -- most pyright errors are cascading `Unknown` type propagation
**Error type:** `reportMissingImports` / `import-not-found`

### What's wrong

Both the resource module and its test file import:

```python
from ...types.organizations.organization_profile_get_params import Result
```

But the file `organization_profile_get_params.py` does not exist. It was deleted by codegen.

### Change history

| Date       | Commit      | What happened |
|------------|-------------|---------------|
| 2026-02-11 | `1c415a2dd` | **Manual fix**: created `organization_profile_get_params.py` with `Result = OrganizationProfile` |
| 2026-04-19 | `3b83baa3b` | Codegen created `organization_profile.py` resource file, importing `Result` from get_params |
| 2026-04-22 | `0d6464258` | Codegen **deleted** `organization_profile_get_params.py` and removed it from `__init__.py` |
| 2026-04-23 | `988df8632` | Resource file unchanged -- still imports from deleted module |

### Root cause

There is a sequencing inconsistency in the codegen output. The resource file (`organization_profile.py`) was
generated expecting a `Result` type alias from a params file, but a later codegen run deleted that params file
without updating the resource file's import. The `Result` type was just an alias for `OrganizationProfile`.

### Fix

Option A -- Recreate the deleted file:

Create `src/cloudflare/types/organizations/organization_profile_get_params.py`:
```python
from __future__ import annotations
from typing_extensions import TypeAlias
from .organization_profile import OrganizationProfile

__all__ = ["Result"]

Result: TypeAlias = OrganizationProfile
```

And add to `src/cloudflare/types/organizations/__init__.py`:
```python
from .organization_profile import OrganizationProfile as OrganizationProfile
```

Option B -- Inline the import (smaller diff):

In `organization_profile.py` and the test file, replace:
```python
from ...types.organizations.organization_profile_get_params import Result
```
with:
```python
from ...types.organizations.organization_profile import OrganizationProfile as Result
```

Option A is preferred since it matches the pattern codegen expects and is more durable.

---

## Issue 4: `_get_api_list` called with unsupported `files` parameter

**Files:**
- `src/cloudflare/resources/ai/to_markdown.py` (lines 118, 217)

**Error count:** 4 (pyright) + 2 (mypy)  (2 calls x sync/async variants)
**Error type:** `reportCallIssue` + `reportUnknownVariableType` / `call-arg`

### What's wrong

The `transform` method passes `files=files` to `self._get_api_list()`:

```python
return self._get_api_list(
    ...,
    body=maybe_transform(body, ...),
    files=files,        # <-- not in get_api_list signature
    options=...,
    model=...,
    method="post",
)
```

The `get_api_list` method signature in `_base_client.py` is:

```python
def get_api_list(self, path, *, model, page, body=None, options={}, method="get") -> SyncPageT
```

There is no `files` parameter. The kwargs likely pass through to the underlying request options via `**options`,
but the type signature rejects it.

### Change history

| Date       | Commit      | What happened |
|------------|-------------|---------------|
| 2026-02-11 | `f280942f4` | Added `# pyright: ignore` / `# type: ignore` to the **same pattern** in `radar/ai/to_markdown.py` |
| 2026-04-19 | `3b83baa3b` | Codegen created the new `ai/to_markdown.py` with same `files=` pattern but **without** suppression comments |

### Root cause

This is a known Stainless codegen limitation: `_get_api_list` does not accept `files` in its typed signature, but
multipart file upload endpoints that also return paginated lists need to pass files through. The older
`radar/ai/to_markdown.py` has manual suppression comments that survive codegen. The newly generated
`ai/to_markdown.py` was created fresh and lacks them.

### Fix

Add type-checker suppression comments matching the pattern in `radar/ai/to_markdown.py`:

```python
files=files,  # pyright: ignore[reportCallIssue]  # type: ignore[call-arg]
```

On both line 118 (sync) and line 217 (async) in `src/cloudflare/resources/ai/to_markdown.py`.

---

## Cross-cutting observations

1. **Manual fixes are fragile.** Issues 2, 3, and 4 all stem from manual fixes (commits `1c415a2dd` and
   `f280942f4`) being overwritten by subsequent Stainless codegen runs. Any fix applied here will face the same
   risk on the next codegen sync unless the upstream Stainless config or OpenAPI spec is also corrected.

2. **Upstream Stainless bugs to track:**
   - Missing `Required` import when re-promoting fields (Issue 1)
   - Empty stub classes for recursive TypedDict types in pipelines (Issue 2)
   - Inconsistent file deletion without updating dependents (Issue 3)
   - Missing `files` parameter in `_get_api_list` signature for multipart paginated endpoints (Issue 4)

3. **Recommended durable fixes:**
   - Issues 1, 3, 4: File Stainless bug reports so codegen output is correct
   - Issue 2: Fix the OpenAPI spec for pipelines to properly model recursive struct/list types, or add Stainless
     config overrides to emit correct TypedDict stubs
