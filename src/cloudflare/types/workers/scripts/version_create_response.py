# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ...._utils import PropertyInfo
from ...._models import BaseModel

__all__ = [
    "VersionCreateResponse",
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
    "ExportsReconciliation",
    "ExportsReconciliationInfo",
    "ExportsReconciliationRenamed",
    "ExportsReconciliationTransferPending",
    "ExportsReconciliationTransferred",
    "ExportsReconciliationWarning",
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


class ExportsReconciliationInfo(BaseModel):
    """A non-blocking reconciliation info entry.

    Emitted for stale
    tombstones (a no-op on this deploy) and for tombstones applied
    with the source class still in code (the supported zero-downtime
    rollout pattern).
    """

    class_: str = FieldInfo(alias="class")
    """The class name the info entry is about."""

    message: str
    """Human-readable explanation."""

    scenario: Literal[
        "code_class_not_in_exports",
        "provisioned_class_missing_from_config",
        "config_export_not_in_code",
        "config_references_nonexistent_class",
        "orphaned_provisioned_namespace",
        "storage_type_mismatch",
        "free_tier_requires_sqlite",
        "invalid_export",
        "tombstone_delete_class_still_in_code",
        "tombstone_delete_blocked_by_external_bindings",
        "tombstone_renamed_to_occupied",
        "transferred_pending_not_found",
        "transferred_target_missing",
        "transferred_target_mismatch",
        "phase_one_transfer_source_missing",
        "phase_one_transfer_source_namespace_missing",
        "phase_one_transfer_target_class_provisioned",
        "phase_one_transfer_after_commit_mismatch",
        "phase_one_transfer_duplicate",
        "phase_one_transfer_target_in_dispatch_namespace",
        "phase_one_transfer_source_in_dispatch_namespace",
        "transferred_source_in_dispatch_namespace",
        "transferred_target_in_dispatch_namespace",
        "container_undeclared_reference",
        "container_class_not_durable_object",
        "container_wiring_inconsistent",
        "container_multiple_durable_objects",
        "transfer_container_parity_mismatch",
        "transfer_container_parity_mismatch_on_commit",
        "tombstone_class_still_in_code",
        "stale_tombstone",
        "transfer_receive_already_applied",
        "transfer_receive_cleanup_complete",
    ]
    """
    Stable, machine-readable tag identifying which reconciliation scenario produced
    an error, warning, or info entry. Clients may branch on this value instead of
    parsing `message`.
    """

    namespace_id: Optional[str] = None
    """The provisioned namespace the entry relates to, when applicable."""

    referencing_scripts: Optional[List[str]] = None
    """Other Workers in the account that still bind to the affected class.

    Advisory: while non-empty the tombstone is not yet safe to remove — redeploy
    these Workers with bindings re-pointed first.
    """


class ExportsReconciliationRenamed(BaseModel):
    """A single applied `renamed` tombstone."""

    from_: str = FieldInfo(alias="from")
    """The original (source) class name."""

    to: str
    """The new class name (`renamed_to`)."""


class ExportsReconciliationTransferPending(BaseModel):
    """
    A single phase-1 transfer hint recorded on the target side (a live
    `expecting-transfer` entry).
    """

    class_: str = FieldInfo(alias="class")
    """The target-side class name awaiting transfer."""

    from_: str = FieldInfo(alias="from")
    """The source script the namespace will be transferred from."""


class ExportsReconciliationTransferred(BaseModel):
    """A single committed `transferred` tombstone (phase-2 commit)."""

    class_: str = FieldInfo(alias="class")
    """The source class name that was transferred."""

    phase: Literal["committed"]
    """The transfer phase. Currently always `committed`."""

    to: str
    """The destination script that now owns the namespace."""


class ExportsReconciliationWarning(BaseModel):
    """A non-blocking reconciliation warning.

    Reserved: no scenario
    populates this array today (`code_class_not_in_exports` is
    surfaced as info and `provisioned_class_missing_from_config` is a
    hard error). Clients should still surface any entries that appear.
    """

    class_: str = FieldInfo(alias="class")
    """The class name the warning is about."""

    message: str
    """Human-readable explanation of the warning."""

    scenario: Literal[
        "code_class_not_in_exports",
        "provisioned_class_missing_from_config",
        "config_export_not_in_code",
        "config_references_nonexistent_class",
        "orphaned_provisioned_namespace",
        "storage_type_mismatch",
        "free_tier_requires_sqlite",
        "invalid_export",
        "tombstone_delete_class_still_in_code",
        "tombstone_delete_blocked_by_external_bindings",
        "tombstone_renamed_to_occupied",
        "transferred_pending_not_found",
        "transferred_target_missing",
        "transferred_target_mismatch",
        "phase_one_transfer_source_missing",
        "phase_one_transfer_source_namespace_missing",
        "phase_one_transfer_target_class_provisioned",
        "phase_one_transfer_after_commit_mismatch",
        "phase_one_transfer_duplicate",
        "phase_one_transfer_target_in_dispatch_namespace",
        "phase_one_transfer_source_in_dispatch_namespace",
        "transferred_source_in_dispatch_namespace",
        "transferred_target_in_dispatch_namespace",
        "container_undeclared_reference",
        "container_class_not_durable_object",
        "container_wiring_inconsistent",
        "container_multiple_durable_objects",
        "transfer_container_parity_mismatch",
        "transfer_container_parity_mismatch_on_commit",
        "tombstone_class_still_in_code",
        "stale_tombstone",
        "transfer_receive_already_applied",
        "transfer_receive_cleanup_complete",
    ]
    """
    Stable, machine-readable tag identifying which reconciliation scenario produced
    an error, warning, or info entry. Clients may branch on this value instead of
    parsing `message`.
    """

    namespace_id: Optional[str] = None
    """The provisioned namespace the warning relates to, when applicable."""


class ExportsReconciliation(BaseModel):
    """Summary of the declarative exports reconciliation that
    ran on this upload.

    Populated only when the uploaded
    metadata included an `exports` block. Durable Object
    entries drive reconciliation; `type: worker` entries do
    not contribute to this summary.
    """

    created: List[str]
    """Class names for which a new namespace was provisioned."""

    deleted: List[str]
    """Class names whose namespace was deleted by a `deleted` tombstone."""

    info: List[ExportsReconciliationInfo]
    """
    Non-blocking info entries (stale tombstones, tombstone applied with class still
    in code). See `exports_reconciliation_info`.
    """

    removable_entries: List[str]
    """
    Source class names whose tombstone entry is now stale and safe to delete from
    `exports` (no remaining referencing scripts).
    """

    renamed: List[ExportsReconciliationRenamed]
    """Applied `renamed` tombstones."""

    transfer_pending: List[ExportsReconciliationTransferPending]
    """Phase-1 transfer hints recorded on the target side."""

    transferred: List[ExportsReconciliationTransferred]
    """Committed `transferred` tombstones (phase-2)."""

    updated: List[str]
    """Class names whose provisioned namespace was mutated in place."""

    warnings: List[ExportsReconciliationWarning]
    """Non-blocking warnings. See `exports_reconciliation_warning`."""


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


class VersionCreateResponse(BaseModel):
    resources: Resources

    id: Optional[str] = None
    """Unique identifier for the version."""

    exports_reconciliation: Optional[ExportsReconciliation] = None
    """Summary of the declarative exports reconciliation that ran on this upload.

    Populated only when the uploaded metadata included an `exports` block. Durable
    Object entries drive reconciliation; `type: worker` entries do not contribute to
    this summary.
    """

    metadata: Optional[Metadata] = None

    number: Optional[float] = None
    """Sequential version number."""

    startup_time_ms: Optional[int] = None
    """
    Time in milliseconds spent on
    [Worker startup](https://developers.cloudflare.com/workers/platform/limits/#worker-startup-time).
    """
