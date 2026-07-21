# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ....._models import BaseModel
from ....workers.scripts.consumer_script import ConsumerScript

__all__ = [
    "ScriptUpdateResponse",
    "CacheOptions",
    "Exports",
    "ExportsCache",
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


class ExportsCache(BaseModel):
    """Cache override for this entrypoint.

    It applies only to
    `type: worker` entries and overrides the Worker's global
    `cache_options.enabled` for that entrypoint.
    """

    enabled: bool
    """Whether caching is enabled for this entrypoint."""


class Exports(BaseModel):
    """
    A single entry in the `exports` map, keyed by export name (a
    `WorkerEntrypoint` class name, a Durable Object class name, or
    `default` for the Worker's default export). Worker entrypoint
    entries set `type: worker` and may carry `cache` configuration
    for that entrypoint. Durable Object entries set
    `type: durable-object` and carry additional provisioning fields.
    """

    type: Literal["worker", "durable-object"]
    """The kind of export."""

    cache: Optional[ExportsCache] = None
    """Cache override for this entrypoint.

    It applies only to `type: worker` entries and overrides the Worker's global
    `cache_options.enabled` for that entrypoint.
    """

    state: Optional[Literal["created", "deleted", "renamed", "transferred", "expecting-transfer"]] = None
    """Lifecycle state of the export entry.

    Defaults to `created` (a normal, live export) when omitted.

    `deleted`, `renamed`, and `transferred` are tombstones: write-only lifecycle
    operations that retire, rename, or hand off a provisioned Durable Object
    namespace. They are applied at upload and are filtered out of GET responses, so
    a read only ever returns `created` or `expecting-transfer`.

    `expecting-transfer` is a live export whose data is being received from another
    script via the two-phase transfer flow; it carries `storage` and
    `transfer_from`.
    """

    storage: Optional[Literal["sqlite", "legacy-kv"]] = None
    """Storage backend for a `type: durable-object` export.

    Required for live Durable Object entries (`created` and `expecting-transfer`).
    `sqlite` selects SQLite-backed storage; `legacy-kv` selects the legacy key-value
    storage.
    """

    transfer_from: Optional[str] = None
    """Source script for a `state: expecting-transfer` entry.

    The namespace on this script is materialised from the source script's data via
    the pending-transfer flow. Present on reads for `expecting-transfer` entries.
    """


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
