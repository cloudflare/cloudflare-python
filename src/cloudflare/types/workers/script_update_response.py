# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .scripts.consumer_script import ConsumerScript

__all__ = [
    "ScriptUpdateResponse",
    "CacheOptions",
    "Exports",
    "ExportsWorkersWorkerExport",
    "ExportsWorkersWorkerExportCache",
    "ExportsWorkersDurableObjectExport",
    "ExportsWorkersDurableObjectDeletedExport",
    "ExportsWorkersDurableObjectRenamedExport",
    "ExportsWorkersDurableObjectTransferredExport",
    "ExportsWorkersDurableObjectExpectingTransferExport",
    "NamedHandler",
    "Observability",
    "ObservabilityLogs",
    "ObservabilityTraces",
    "Placement",
    "PlacementUnionMember0",
    "PlacementUnionMember1",
    "PlacementUnionMember2",
    "PlacementUnionMember3",
    "PlacementUnionMember4",
    "PlacementUnionMember5",
    "PlacementUnionMember6",
    "PlacementUnionMember7",
    "PlacementUnionMember7Target",
    "PlacementUnionMember7TargetRegion",
    "PlacementUnionMember7TargetHostname",
    "PlacementUnionMember7TargetHost",
]


class CacheOptions(BaseModel):
    """Global CacheW configuration for the Worker.

    When caching is on,
    the platform provisions a `cloudflare.app` zone for the Worker.
    A `type: worker` entry in the `exports` map can override this
    value for a single entrypoint.
    """

    enabled: bool
    """Whether caching is enabled for this Worker."""

    cross_version_cache: Optional[bool] = None
    """Whether cached responses are shared across Worker version uploads.

    This is independent of `enabled`. It can stay true while caching is off, so the
    preference survives turning caching off and back on.
    """


class ExportsWorkersWorkerExportCache(BaseModel):
    """Cache override for this entrypoint.

    Overrides the Worker's
    global `cache_options.enabled` for this entrypoint only.
    """

    enabled: bool
    """Whether caching is enabled for this entrypoint."""


class ExportsWorkersWorkerExport(BaseModel):
    """A named Worker entrypoint export (`type: worker`).

    Worker
    entrypoints are always live (`state: created`) and carry no
    storage or lifecycle fields. The optional `cache` block overrides
    the Worker's global `cache_options.enabled` for this entrypoint.
    """

    type: Literal["worker"]
    """Marks this entry as a Worker entrypoint export."""

    cache: Optional[ExportsWorkersWorkerExportCache] = None
    """Cache override for this entrypoint.

    Overrides the Worker's global `cache_options.enabled` for this entrypoint only.
    """

    state: Optional[Literal["created"]] = None
    """Live export. May be omitted; defaults to `created`."""


class ExportsWorkersDurableObjectExport(BaseModel):
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


class ExportsWorkersDurableObjectDeletedExport(BaseModel):
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


class ExportsWorkersDurableObjectRenamedExport(BaseModel):
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


class ExportsWorkersDurableObjectTransferredExport(BaseModel):
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


class ExportsWorkersDurableObjectExpectingTransferExport(BaseModel):
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


Exports: TypeAlias = Annotated[
    Union[
        ExportsWorkersWorkerExport,
        ExportsWorkersDurableObjectExport,
        ExportsWorkersDurableObjectDeletedExport,
        ExportsWorkersDurableObjectRenamedExport,
        ExportsWorkersDurableObjectTransferredExport,
        ExportsWorkersDurableObjectExpectingTransferExport,
    ],
    PropertyInfo(discriminator="type"),
]


class NamedHandler(BaseModel):
    handlers: Optional[List[str]] = None
    """The names of handlers exported as part of the named export."""

    name: Optional[str] = None
    """The name of the export."""


class ObservabilityLogs(BaseModel):
    """Log settings for the Worker."""

    enabled: bool
    """Whether logs are enabled for the Worker."""

    invocation_logs: bool
    """
    Whether
    [invocation logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs/#invocation-logs)
    are enabled for the Worker.
    """

    destinations: Optional[List[str]] = None
    """A list of destinations where logs will be exported to."""

    head_sampling_rate: Optional[float] = None
    """The sampling rate for logs. From 0 to 1 (1 = 100%, 0.1 = 10%). Default is 1."""

    persist: Optional[bool] = None
    """Whether log persistence is enabled for the Worker."""


class ObservabilityTraces(BaseModel):
    """Trace settings for the Worker."""

    destinations: Optional[List[str]] = None
    """A list of destinations where traces will be exported to."""

    enabled: Optional[bool] = None
    """Whether traces are enabled for the Worker."""

    head_sampling_rate: Optional[float] = None
    """The sampling rate for traces. From 0 to 1 (1 = 100%, 0.1 = 10%). Default is 1."""

    persist: Optional[bool] = None
    """Whether trace persistence is enabled for the Worker."""

    propagation_policy: Optional[Literal["authenticated", "accept"]] = None
    """
    Controls how inbound trace context (traceparent/tracestate) headers on incoming
    requests are handled. "authenticated" (default) honors inbound trace context
    only when accompanied by a valid trace auth token. "accept" unconditionally
    accepts inbound trace context. Requires the trace propagation feature to be
    enabled.
    """


class Observability(BaseModel):
    """Observability settings for the Worker."""

    enabled: bool
    """Whether observability is enabled for the Worker."""

    head_sampling_rate: Optional[float] = None
    """The sampling rate for incoming requests.

    From 0 to 1 (1 = 100%, 0.1 = 10%). Default is 1.
    """

    logs: Optional[ObservabilityLogs] = None
    """Log settings for the Worker."""

    traces: Optional[ObservabilityTraces] = None
    """Trace settings for the Worker."""


class PlacementUnionMember0(BaseModel):
    mode: Literal["smart"]
    """
    Enables
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    """

    last_analyzed_at: Optional[datetime] = None
    """
    The last time the script was analyzed for
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    """

    status: Optional[Literal["SUCCESS", "UNSUPPORTED_APPLICATION", "INSUFFICIENT_INVOCATIONS"]] = None
    """
    Status of
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    """


class PlacementUnionMember1(BaseModel):
    region: str
    """Cloud region for targeted placement in format 'provider:region'."""

    last_analyzed_at: Optional[datetime] = None
    """
    The last time the script was analyzed for
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    """

    status: Optional[Literal["SUCCESS", "UNSUPPORTED_APPLICATION", "INSUFFICIENT_INVOCATIONS"]] = None
    """
    Status of
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    """


class PlacementUnionMember2(BaseModel):
    hostname: str
    """HTTP hostname for targeted placement."""

    last_analyzed_at: Optional[datetime] = None
    """
    The last time the script was analyzed for
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    """

    status: Optional[Literal["SUCCESS", "UNSUPPORTED_APPLICATION", "INSUFFICIENT_INVOCATIONS"]] = None
    """
    Status of
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    """


class PlacementUnionMember3(BaseModel):
    host: str
    """TCP host and port for targeted placement."""

    last_analyzed_at: Optional[datetime] = None
    """
    The last time the script was analyzed for
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    """

    status: Optional[Literal["SUCCESS", "UNSUPPORTED_APPLICATION", "INSUFFICIENT_INVOCATIONS"]] = None
    """
    Status of
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    """


class PlacementUnionMember4(BaseModel):
    mode: Literal["targeted"]
    """Targeted placement mode."""

    region: str
    """Cloud region for targeted placement in format 'provider:region'."""

    last_analyzed_at: Optional[datetime] = None
    """
    The last time the script was analyzed for
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    """

    status: Optional[Literal["SUCCESS", "UNSUPPORTED_APPLICATION", "INSUFFICIENT_INVOCATIONS"]] = None
    """
    Status of
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    """


class PlacementUnionMember5(BaseModel):
    hostname: str
    """HTTP hostname for targeted placement."""

    mode: Literal["targeted"]
    """Targeted placement mode."""

    last_analyzed_at: Optional[datetime] = None
    """
    The last time the script was analyzed for
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    """

    status: Optional[Literal["SUCCESS", "UNSUPPORTED_APPLICATION", "INSUFFICIENT_INVOCATIONS"]] = None
    """
    Status of
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    """


class PlacementUnionMember6(BaseModel):
    host: str
    """TCP host and port for targeted placement."""

    mode: Literal["targeted"]
    """Targeted placement mode."""

    last_analyzed_at: Optional[datetime] = None
    """
    The last time the script was analyzed for
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    """

    status: Optional[Literal["SUCCESS", "UNSUPPORTED_APPLICATION", "INSUFFICIENT_INVOCATIONS"]] = None
    """
    Status of
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    """


class PlacementUnionMember7TargetRegion(BaseModel):
    region: str
    """Cloud region in format 'provider:region'."""


class PlacementUnionMember7TargetHostname(BaseModel):
    hostname: str
    """HTTP hostname for targeted placement."""


class PlacementUnionMember7TargetHost(BaseModel):
    host: str
    """TCP host:port for targeted placement."""


PlacementUnionMember7Target: TypeAlias = Union[
    PlacementUnionMember7TargetRegion, PlacementUnionMember7TargetHostname, PlacementUnionMember7TargetHost
]


class PlacementUnionMember7(BaseModel):
    mode: Literal["targeted"]
    """Targeted placement mode."""

    target: List[PlacementUnionMember7Target]
    """Array of placement targets (currently limited to single target)."""

    last_analyzed_at: Optional[datetime] = None
    """
    The last time the script was analyzed for
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    """

    status: Optional[Literal["SUCCESS", "UNSUPPORTED_APPLICATION", "INSUFFICIENT_INVOCATIONS"]] = None
    """
    Status of
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    """


Placement: TypeAlias = Union[
    PlacementUnionMember0,
    PlacementUnionMember1,
    PlacementUnionMember2,
    PlacementUnionMember3,
    PlacementUnionMember4,
    PlacementUnionMember5,
    PlacementUnionMember6,
    PlacementUnionMember7,
]


class ScriptUpdateResponse(BaseModel):
    startup_time_ms: int

    id: Optional[str] = None
    """The name used to identify the script."""

    cache_options: Optional[CacheOptions] = None
    """Global CacheW configuration for the Worker.

    When caching is on, the platform provisions a `cloudflare.app` zone for the
    Worker. A `type: worker` entry in the `exports` map can override this value for
    a single entrypoint.
    """

    compatibility_date: Optional[str] = None
    """Date indicating targeted support in the Workers runtime.

    Backwards incompatible fixes to the runtime following this date will not affect
    this Worker.
    """

    compatibility_flags: Optional[List[str]] = None
    """Flags that enable or disable certain features in the Workers runtime.

    Used to enable upcoming features or opt in or out of specific changes not
    included in a `compatibility_date`.
    """

    created_on: Optional[datetime] = None
    """When the script was created."""

    entry_point: Optional[str] = None
    """The entry point for the script."""

    etag: Optional[str] = None
    """Hashed script content, can be used in a If-None-Match header when updating."""

    exports: Optional[Dict[str, Exports]] = None
    """
    Declarative exports for the Worker's most recent version, including Durable
    Object classes (with their `storage` backend) and named Worker entrypoints.
    Tombstoned lifecycle entries are omitted, so only live exports (`created` and
    `expecting-transfer`) are returned.
    """

    handlers: Optional[List[str]] = None
    """The names of handlers exported as part of the default export."""

    has_assets: Optional[bool] = None
    """Whether a Worker contains assets."""

    has_modules: Optional[bool] = None
    """Whether a Worker contains modules."""

    last_deployed_from: Optional[str] = None
    """The client most recently used to deploy this Worker."""

    logpush: Optional[bool] = None
    """Whether Logpush is turned on for the Worker."""

    migration_tag: Optional[str] = None
    """
    The tag of the Durable Object migration that was most recently applied for this
    Worker.
    """

    modified_on: Optional[datetime] = None
    """When the script was last modified."""

    named_handlers: Optional[List[NamedHandler]] = None
    """
    Named exports, such as Durable Object class implementations and named
    entrypoints.
    """

    observability: Optional[Observability] = None
    """Observability settings for the Worker."""

    placement: Optional[Placement] = None
    """
    Configuration for
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    Specify mode='smart' for Smart Placement, or one of region/hostname/host.
    """

    placement_mode: Optional[Literal["smart", "targeted"]] = None

    placement_status: Optional[Literal["SUCCESS", "UNSUPPORTED_APPLICATION", "INSUFFICIENT_INVOCATIONS"]] = None

    tag: Optional[str] = None
    """The immutable ID of the script."""

    tags: Optional[List[str]] = None
    """Tags associated with the Worker."""

    tail_consumers: Optional[List[ConsumerScript]] = None
    """List of Workers that will consume logs from the attached Worker."""

    usage_model: Optional[Literal["standard", "bundled", "unbound"]] = None
    """Usage model for the Worker invocations."""
