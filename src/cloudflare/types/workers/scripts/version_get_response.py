# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ...._utils import PropertyInfo
from ...._models import BaseModel

__all__ = [
    "VersionGetResponse",
    "Resources",
    "ResourcesBindings",
    "ResourcesScript",
    "ResourcesScriptNamedHandler",
    "ResourcesScriptRuntime",
    "ResourcesScriptRuntimeExports",
    "ResourcesScriptRuntimeExportsWorkersWorkerExport",
    "ResourcesScriptRuntimeExportsWorkersWorkerExportCache",
    "ResourcesScriptRuntimeExportsWorkersDurableObjectExport",
    "ResourcesScriptRuntimeExportsWorkersDurableObjectDeletedExport",
    "ResourcesScriptRuntimeExportsWorkersDurableObjectRenamedExport",
    "ResourcesScriptRuntimeExportsWorkersDurableObjectTransferredExport",
    "ResourcesScriptRuntimeExportsWorkersDurableObjectExpectingTransferExport",
    "ResourcesScriptRuntimeLimits",
    "Metadata",
]


class ResourcesBindings:
    """List of bindings attached to a Worker.

    You can find more about bindings on our docs: https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/#bindings.
    """

    pass


class ResourcesScriptNamedHandler(BaseModel):
    handlers: Optional[List[str]] = None
    """The names of handlers exported as part of the named export."""

    name: Optional[str] = None
    """The name of the exported class or entrypoint."""


class ResourcesScript(BaseModel):
    etag: Optional[str] = None
    """Hashed script content"""

    handlers: Optional[List[str]] = None
    """The names of handlers exported as part of the default export."""

    last_deployed_from: Optional[str] = None
    """The client most recently used to deploy this Worker."""

    named_handlers: Optional[List[ResourcesScriptNamedHandler]] = None
    """
    Named exports, such as Durable Object class implementations and named
    entrypoints.
    """


class ResourcesScriptRuntimeExportsWorkersWorkerExportCache(BaseModel):
    """Cache override for this entrypoint.

    Overrides the Worker's
    global `cache_options.enabled` for this entrypoint only.
    """

    enabled: bool
    """Whether caching is enabled for this entrypoint."""


class ResourcesScriptRuntimeExportsWorkersWorkerExport(BaseModel):
    """A named Worker entrypoint export (`type: worker`).

    Worker
    entrypoints are always live (`state: created`) and carry no
    storage or lifecycle fields. The optional `cache` block overrides
    the Worker's global `cache_options.enabled` for this entrypoint.
    """

    type: Literal["worker"]
    """Marks this entry as a Worker entrypoint export."""

    cache: Optional[ResourcesScriptRuntimeExportsWorkersWorkerExportCache] = None
    """Cache override for this entrypoint.

    Overrides the Worker's global `cache_options.enabled` for this entrypoint only.
    """

    state: Optional[Literal["created"]] = None
    """Live export. May be omitted; defaults to `created`."""


class ResourcesScriptRuntimeExportsWorkersDurableObjectExport(BaseModel):
    """A live Durable Object export (`state: created`, the default).

    The
    platform auto-provisions the namespace on first deploy, matches it
    on subsequent deploys, and never mutates or deletes it as a side
    effect of a code-only change. `storage` is required; `renamed_to`,
    `transferred_to` and `transfer_from` are not allowed on a live
    entry.
    """

    storage: Literal["sqlite", "legacy-kv"]
    """Durable Object storage backend.

    `sqlite` is the recommended (and only) backend for new namespaces. `legacy-kv`
    is accepted only for a class whose namespace already exists as KV-backed; the
    `exports` flow never provisions a new `legacy-kv` namespace.
    """

    type: Literal["durable-object"]
    """Marks this entry as a Durable Object export."""

    container: Optional[str] = None
    """
    Name of the container (declared in the upload's `metadata.containers`) that
    backs this Durable Object. When set, the namespace is container-enabled. Valid
    only on live entries.
    """

    state: Optional[Literal["created"]] = None
    """Live export. May be omitted; defaults to `created`."""


class ResourcesScriptRuntimeExportsWorkersDurableObjectDeletedExport(BaseModel):
    """
    A `deleted` tombstone: retires the provisioned namespace for this
    class and all of its data. The class must be absent from the
    uploaded code and no other Worker in the account may bind to the
    namespace, otherwise the deploy is rejected. No other fields are
    allowed. Deletion is irreversible.
    """

    state: Literal["deleted"]
    """Tombstone that deletes the namespace."""

    type: Literal["durable-object"]
    """Marks this entry as a Durable Object export."""


class ResourcesScriptRuntimeExportsWorkersDurableObjectRenamedExport(BaseModel):
    """
    A `renamed` tombstone: rewrites the provisioned namespace's class
    name from this map key to `renamed_to`. The source class may stay
    in code during the rollout window (an info notice is emitted).
    `storage`, `transferred_to` and `transfer_from` are not allowed.
    """

    state: Literal["renamed"]
    """Tombstone that renames the namespace's class."""

    type: Literal["durable-object"]
    """Marks this entry as a Durable Object export."""


class ResourcesScriptRuntimeExportsWorkersDurableObjectTransferredExport(BaseModel):
    """
    A `transferred` tombstone (source side of a two-phase transfer):
    hands ownership of the provisioned namespace to another script in
    the same account, named by `transferred_to`. The target must have
    already deployed a matching `expecting-transfer` entry. The source
    class may stay in code during the rollout window (an info notice
    is emitted). `storage`, `renamed_to` and `transfer_from` are not
    allowed.
    """

    state: Literal["transferred"]
    """Tombstone that transfers the namespace to another script."""

    type: Literal["durable-object"]
    """Marks this entry as a Durable Object export."""


class ResourcesScriptRuntimeExportsWorkersDurableObjectExpectingTransferExport(BaseModel):
    """The target side of a two-phase transfer (`state:
    expecting-transfer`).

    Declares that this script expects to receive
    a namespace for this class from the `transfer_from` script. This
    is a live entry, not a tombstone: bindings resolve through the
    source's namespace until the source commits with a `transferred`
    tombstone. `storage` and `transfer_from` are required; `renamed_to`
    and `transferred_to` are not allowed.
    """

    state: Literal["expecting-transfer"]
    """Target side of a two-phase transfer."""

    storage: Literal["sqlite", "legacy-kv"]
    """Durable Object storage backend.

    `sqlite` is the recommended (and only) backend for new namespaces. `legacy-kv`
    is accepted only for a class whose namespace already exists as KV-backed; the
    `exports` flow never provisions a new `legacy-kv` namespace.
    """

    transfer_from: str
    """The source script name to receive the namespace from.

    Must be in the same account and dispatch-namespace context. Present on reads for
    `expecting-transfer` entries.
    """

    type: Literal["durable-object"]
    """Marks this entry as a Durable Object export."""

    container: Optional[str] = None
    """
    Name of the container (declared in the upload's `metadata.containers`) that
    backs this Durable Object once the transfer settles. Valid only on live entries.
    """


ResourcesScriptRuntimeExports: TypeAlias = Annotated[
    Union[
        ResourcesScriptRuntimeExportsWorkersWorkerExport,
        ResourcesScriptRuntimeExportsWorkersDurableObjectExport,
        ResourcesScriptRuntimeExportsWorkersDurableObjectDeletedExport,
        ResourcesScriptRuntimeExportsWorkersDurableObjectRenamedExport,
        ResourcesScriptRuntimeExportsWorkersDurableObjectTransferredExport,
        ResourcesScriptRuntimeExportsWorkersDurableObjectExpectingTransferExport,
    ],
    PropertyInfo(discriminator="type"),
]


class ResourcesScriptRuntimeLimits(BaseModel):
    """Resource limits for the Worker."""

    cpu_ms: Optional[int] = None
    """The amount of CPU time this Worker can use in milliseconds."""


class ResourcesScriptRuntime(BaseModel):
    """Runtime configuration for the Worker."""

    compatibility_date: Optional[str] = None
    """Date indicating targeted support in the Workers runtime.

    Backwards incompatible fixes to the runtime following this date will not affect
    this Worker.
    """

    compatibility_flags: Optional[List[str]] = None
    """Flags that enable or disable certain features in the Workers runtime."""

    exports: Optional[Dict[str, ResourcesScriptRuntimeExports]] = None
    """
    Declarative exports for this version, including Durable Object classes (with
    their `storage` backend) and named Worker entrypoints. Tombstoned lifecycle
    entries are omitted, so only live exports (`created` and `expecting-transfer`)
    are returned.
    """

    limits: Optional[ResourcesScriptRuntimeLimits] = None
    """Resource limits for the Worker."""

    migration_tag: Optional[str] = None
    """
    The tag of the Durable Object migration that was most recently applied for this
    Worker.
    """

    usage_model: Optional[Literal["bundled", "unbound", "standard"]] = None
    """Usage model for the Worker invocations."""


class Resources(BaseModel):
    bindings: Optional[ResourcesBindings] = None
    """List of bindings attached to a Worker.

    You can find more about bindings on our docs:
    https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/#bindings.
    """

    script: Optional[ResourcesScript] = None

    script_runtime: Optional[ResourcesScriptRuntime] = None
    """Runtime configuration for the Worker."""


class Metadata(BaseModel):
    author_email: Optional[str] = None
    """Email of the user who created the version."""

    author_id: Optional[str] = None
    """Identifier of the user who created the version."""

    created_on: Optional[str] = None
    """When the version was created."""

    has_preview: Optional[bool] = FieldInfo(alias="hasPreview", default=None)
    """Whether the version can be previewed."""

    modified_on: Optional[str] = None
    """When the version was last modified."""

    source: Optional[
        Literal[
            "unknown",
            "api",
            "wrangler",
            "terraform",
            "dash",
            "cf_cli",
            "dash_template",
            "integration",
            "quick_editor",
            "playground",
            "workersci",
        ]
    ] = None
    """The source of the version upload."""


class VersionGetResponse(BaseModel):
    resources: Resources

    id: Optional[str] = None
    """Unique identifier for the version."""

    metadata: Optional[Metadata] = None

    number: Optional[float] = None
    """Sequential version number."""
