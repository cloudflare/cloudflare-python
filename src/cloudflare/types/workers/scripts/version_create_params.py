# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ...._types import FileTypes, SequenceNotStr
from ...._utils import PropertyInfo

__all__ = [
    "VersionCreateParams",
    "Metadata",
    "MetadataAnnotations",
    "MetadataBinding",
    "MetadataBindingWorkersBindingKindAI",
    "MetadataBindingWorkersBindingKindAISearch",
    "MetadataBindingWorkersBindingKindAISearchNamespace",
    "MetadataBindingWorkersBindingKindAnalyticsEngine",
    "MetadataBindingWorkersBindingKindAssets",
    "MetadataBindingWorkersBindingKindBrowser",
    "MetadataBindingWorkersBindingKindD1",
    "MetadataBindingWorkersBindingKindDataBlob",
    "MetadataBindingWorkersBindingKindDispatchNamespace",
    "MetadataBindingWorkersBindingKindDispatchNamespaceOutbound",
    "MetadataBindingWorkersBindingKindDispatchNamespaceOutboundParam",
    "MetadataBindingWorkersBindingKindDispatchNamespaceOutboundWorker",
    "MetadataBindingWorkersBindingKindDurableObjectNamespace",
    "MetadataBindingWorkersBindingKindHyperdrive",
    "MetadataBindingWorkersBindingKindInherit",
    "MetadataBindingWorkersBindingKindImages",
    "MetadataBindingWorkersBindingKindJson",
    "MetadataBindingWorkersBindingKindKVNamespace",
    "MetadataBindingWorkersBindingKindMedia",
    "MetadataBindingWorkersBindingKindMTLSCertificate",
    "MetadataBindingWorkersBindingKindPlainText",
    "MetadataBindingWorkersBindingKindPipelines",
    "MetadataBindingWorkersBindingKindQueue",
    "MetadataBindingWorkersBindingKindRatelimit",
    "MetadataBindingWorkersBindingKindRatelimitSimple",
    "MetadataBindingWorkersBindingKindR2Bucket",
    "MetadataBindingWorkersBindingKindSecretText",
    "MetadataBindingWorkersBindingKindSendEmail",
    "MetadataBindingWorkersBindingKindService",
    "MetadataBindingWorkersBindingKindTextBlob",
    "MetadataBindingWorkersBindingKindVectorize",
    "MetadataBindingWorkersBindingKindVersionMetadata",
    "MetadataBindingWorkersBindingKindSecretsStoreSecret",
    "MetadataBindingWorkersBindingKindFlagship",
    "MetadataBindingWorkersBindingKindSecretKey",
    "MetadataBindingWorkersBindingKindWorkflow",
    "MetadataBindingWorkersBindingKindWasmModule",
    "MetadataBindingWorkersBindingKindVPCService",
    "MetadataBindingWorkersBindingKindVPCNetwork",
    "MetadataCacheOptions",
    "MetadataExports",
    "MetadataExportsCache",
    "MetadataPackageDependency",
]


class VersionCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    metadata: Required[Metadata]
    """JSON-encoded metadata about the uploaded parts and Worker configuration."""

    bindings_inherit: Literal["strict"]
    """
    When set to "strict", the upload will fail if any `inherit` type bindings cannot
    be resolved against the previous version of the Worker. Without this,
    unresolvable inherit bindings are silently dropped.
    """

    files: SequenceNotStr[FileTypes]
    """An array of modules (often JavaScript files) comprising a Worker script.

    At least one module must be present and referenced in the metadata as
    `main_module` or `body_part` by filename.<br/>Possible Content-Type(s) are:
    `application/javascript+module`, `text/javascript+module`,
    `application/javascript`, `text/javascript`, `text/x-python`,
    `text/x-python-requirement`, `application/wasm`, `text/plain`,
    `application/octet-stream`, `application/source-map`.
    """


class MetadataAnnotations(TypedDict, total=False):
    workers_alias: Annotated[str, PropertyInfo(alias="workers/alias")]
    """Associated alias for a version."""

    workers_message: Annotated[str, PropertyInfo(alias="workers/message")]
    """Human-readable message about the version. Truncated to 1000 bytes if longer."""

    workers_tag: Annotated[str, PropertyInfo(alias="workers/tag")]
    """User-provided identifier for the version. Maximum 100 bytes."""


class MetadataBindingWorkersBindingKindAI(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["ai"]]
    """The kind of resource that the binding provides."""


class MetadataBindingWorkersBindingKindAISearch(TypedDict, total=False):
    instance_name: Required[str]
    """The user-chosen instance name.

    Must exist at deploy time. The worker can search, chat, update, and manage
    items/jobs on this instance.
    """

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["ai_search"]]
    """The kind of resource that the binding provides."""

    namespace: str
    """The namespace the instance belongs to.

    Defaults to "default" if omitted. Customers who don't use namespaces can simply
    omit this field.
    """


class MetadataBindingWorkersBindingKindAISearchNamespace(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    namespace: Required[str]
    """The user-chosen namespace name.

    Must exist before deploy -- Wrangler handles auto-creation on deploy failure (R2
    bucket pattern). The "default" namespace is auto-created by config-api for new
    accounts. Grants full access (CRUD + search + chat) to all instances within the
    namespace.
    """

    type: Required[Literal["ai_search_namespace"]]
    """The kind of resource that the binding provides."""


class MetadataBindingWorkersBindingKindAnalyticsEngine(TypedDict, total=False):
    dataset: Required[str]
    """The name of the dataset to bind to."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["analytics_engine"]]
    """The kind of resource that the binding provides."""


class MetadataBindingWorkersBindingKindAssets(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["assets"]]
    """The kind of resource that the binding provides."""


class MetadataBindingWorkersBindingKindBrowser(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["browser"]]
    """The kind of resource that the binding provides."""


class MetadataBindingWorkersBindingKindD1(TypedDict, total=False):
    database_id: Required[str]
    """Identifier of the D1 database to bind to."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["d1"]]
    """The kind of resource that the binding provides."""

    id: str
    """Identifier of the D1 database to bind to."""


class MetadataBindingWorkersBindingKindDataBlob(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    part: Required[str]
    """The name of the file containing the data content.

    Only accepted for `service worker syntax` Workers.
    """

    type: Required[Literal["data_blob"]]
    """The kind of resource that the binding provides."""


class MetadataBindingWorkersBindingKindDispatchNamespaceOutboundParam(TypedDict, total=False):
    name: Required[str]
    """Name of the parameter."""


class MetadataBindingWorkersBindingKindDispatchNamespaceOutboundWorker(TypedDict, total=False):
    """Outbound worker."""

    entrypoint: str
    """Entrypoint to invoke on the outbound worker."""

    environment: str
    """Environment of the outbound worker."""

    service: str
    """Name of the outbound worker."""


class MetadataBindingWorkersBindingKindDispatchNamespaceOutbound(TypedDict, total=False):
    """Outbound worker."""

    params: Iterable[MetadataBindingWorkersBindingKindDispatchNamespaceOutboundParam]
    """
    Pass information from the Dispatch Worker to the Outbound Worker through the
    parameters.
    """

    worker: MetadataBindingWorkersBindingKindDispatchNamespaceOutboundWorker
    """Outbound worker."""


class MetadataBindingWorkersBindingKindDispatchNamespace(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    namespace: Required[str]
    """The name of the dispatch namespace."""

    type: Required[Literal["dispatch_namespace"]]
    """The kind of resource that the binding provides."""

    outbound: MetadataBindingWorkersBindingKindDispatchNamespaceOutbound
    """Outbound worker."""


class MetadataBindingWorkersBindingKindDurableObjectNamespace(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["durable_object_namespace"]]
    """The kind of resource that the binding provides."""

    class_name: str
    """The exported class name of the Durable Object."""

    dispatch_namespace: str
    """The dispatch namespace the Durable Object script belongs to."""

    environment: str
    """The environment of the script_name to bind to."""

    namespace_id: str
    """Namespace identifier tag."""

    script_name: str
    """
    The script where the Durable Object is defined, if it is external to this
    Worker.
    """


class MetadataBindingWorkersBindingKindHyperdrive(TypedDict, total=False):
    id: Required[str]
    """Identifier of the Hyperdrive connection to bind to."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["hyperdrive"]]
    """The kind of resource that the binding provides."""


class MetadataBindingWorkersBindingKindInherit(TypedDict, total=False):
    name: Required[str]
    """The name of the inherited binding."""

    type: Required[Literal["inherit"]]
    """The kind of resource that the binding provides."""

    old_name: str
    """The old name of the inherited binding.

    If set, the binding will be renamed from `old_name` to `name` in the new
    version. If not set, the binding will keep the same name between versions.
    """

    version_id: str
    """
    Identifier for the version to inherit the binding from, which can be the version
    ID or the literal "latest" to inherit from the latest version. Defaults to
    inheriting the binding from the latest version.
    """


class MetadataBindingWorkersBindingKindImages(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["images"]]
    """The kind of resource that the binding provides."""


class MetadataBindingWorkersBindingKindJson(TypedDict, total=False):
    json: Required[object]
    """JSON data to use."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["json"]]
    """The kind of resource that the binding provides."""


class MetadataBindingWorkersBindingKindKVNamespace(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    namespace_id: Required[str]
    """Namespace identifier tag."""

    type: Required[Literal["kv_namespace"]]
    """The kind of resource that the binding provides."""


class MetadataBindingWorkersBindingKindMedia(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["media"]]
    """The kind of resource that the binding provides."""


class MetadataBindingWorkersBindingKindMTLSCertificate(TypedDict, total=False):
    certificate_id: Required[str]
    """Identifier of the certificate to bind to."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["mtls_certificate"]]
    """The kind of resource that the binding provides."""


class MetadataBindingWorkersBindingKindPlainText(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    text: Required[str]
    """The text value to use."""

    type: Required[Literal["plain_text"]]
    """The kind of resource that the binding provides."""


class MetadataBindingWorkersBindingKindPipelines(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    pipeline: Required[str]
    """Name of the Pipeline to bind to."""

    type: Required[Literal["pipelines"]]
    """The kind of resource that the binding provides."""


class MetadataBindingWorkersBindingKindQueue(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    queue_name: Required[str]
    """Name of the Queue to bind to."""

    type: Required[Literal["queue"]]
    """The kind of resource that the binding provides."""


class MetadataBindingWorkersBindingKindRatelimitSimple(TypedDict, total=False):
    """The rate limit configuration."""

    limit: Required[float]
    """The limit (requests per period)."""

    period: Required[int]
    """The period in seconds."""

    mitigation_timeout: int
    """
    Duration in seconds to apply the mitigation action after the rate limit is
    exceeded. Valid values are 0 (disabled), 10, or multiples of 60 up to 86400.
    Must be greater than or equal to the period when non-zero.
    """


class MetadataBindingWorkersBindingKindRatelimit(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    namespace_id: Required[str]
    """Identifier of the rate limit namespace to bind to."""

    simple: Required[MetadataBindingWorkersBindingKindRatelimitSimple]
    """The rate limit configuration."""

    type: Required[Literal["ratelimit"]]
    """The kind of resource that the binding provides."""


class MetadataBindingWorkersBindingKindR2Bucket(TypedDict, total=False):
    bucket_name: Required[str]
    """R2 bucket to bind to."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["r2_bucket"]]
    """The kind of resource that the binding provides."""

    jurisdiction: Literal["eu", "fedramp", "fedramp-high"]
    """
    The
    [jurisdiction](https://developers.cloudflare.com/r2/reference/data-location/#jurisdictional-restrictions)
    of the R2 bucket.
    """


class MetadataBindingWorkersBindingKindSecretText(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    text: Required[str]
    """The secret value to use."""

    type: Required[Literal["secret_text"]]
    """The kind of resource that the binding provides."""


class MetadataBindingWorkersBindingKindSendEmail(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["send_email"]]
    """The kind of resource that the binding provides."""

    allowed_destination_addresses: SequenceNotStr[str]
    """List of allowed destination addresses."""

    allowed_sender_addresses: SequenceNotStr[str]
    """List of allowed sender addresses."""

    destination_address: str
    """Destination address for the email."""


class MetadataBindingWorkersBindingKindService(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    service: Required[str]
    """Name of Worker to bind to."""

    type: Required[Literal["service"]]
    """The kind of resource that the binding provides."""

    entrypoint: str
    """Entrypoint to invoke on the target Worker."""

    environment: str
    """Optional environment if the Worker utilizes one."""


class MetadataBindingWorkersBindingKindTextBlob(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    part: Required[str]
    """The name of the file containing the text content.

    Only accepted for `service worker syntax` Workers.
    """

    type: Required[Literal["text_blob"]]
    """The kind of resource that the binding provides."""


class MetadataBindingWorkersBindingKindVectorize(TypedDict, total=False):
    index_name: Required[str]
    """Name of the Vectorize index to bind to."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["vectorize"]]
    """The kind of resource that the binding provides."""


class MetadataBindingWorkersBindingKindVersionMetadata(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["version_metadata"]]
    """The kind of resource that the binding provides."""


class MetadataBindingWorkersBindingKindSecretsStoreSecret(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    secret_name: Required[str]
    """Name of the secret in the store."""

    store_id: Required[str]
    """ID of the store containing the secret."""

    type: Required[Literal["secrets_store_secret"]]
    """The kind of resource that the binding provides."""


class MetadataBindingWorkersBindingKindFlagship(TypedDict, total=False):
    app_id: Required[str]
    """ID of the Flagship app to bind to for feature flag evaluation."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["flagship"]]
    """The kind of resource that the binding provides."""


class MetadataBindingWorkersBindingKindSecretKey(TypedDict, total=False):
    algorithm: Required[object]
    """Algorithm-specific key parameters.

    [Learn more](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#algorithm).
    """

    format: Required[Literal["raw", "pkcs8", "spki", "jwk"]]
    """Data format of the key.

    [Learn more](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#format).
    """

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["secret_key"]]
    """The kind of resource that the binding provides."""

    usages: Required[
        List[Literal["encrypt", "decrypt", "sign", "verify", "deriveKey", "deriveBits", "wrapKey", "unwrapKey"]]
    ]
    """Allowed operations with the key.

    [Learn more](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#keyUsages).
    """

    key_base64: str
    """Base64-encoded key data. Required if `format` is "raw", "pkcs8", or "spki"."""

    key_jwk: object
    """
    Key data in
    [JSON Web Key](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#json_web_key)
    format. Required if `format` is "jwk".
    """


class MetadataBindingWorkersBindingKindWorkflow(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["workflow"]]
    """The kind of resource that the binding provides."""

    workflow_name: Required[str]
    """Name of the Workflow to bind to."""

    class_name: str
    """Class name of the Workflow.

    Should only be provided if the Workflow belongs to this script.
    """

    script_name: str
    """Script name that contains the Workflow.

    If not provided, defaults to this script name.
    """


class MetadataBindingWorkersBindingKindWasmModule(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    part: Required[str]
    """The name of the file containing the WebAssembly module content.

    Only accepted for `service worker syntax` Workers.
    """

    type: Required[Literal["wasm_module"]]
    """The kind of resource that the binding provides."""


class MetadataBindingWorkersBindingKindVPCService(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    service_id: Required[str]
    """Identifier of the VPC service to bind to."""

    type: Required[Literal["vpc_service"]]
    """The kind of resource that the binding provides."""


class MetadataBindingWorkersBindingKindVPCNetwork(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["vpc_network"]]
    """The kind of resource that the binding provides."""

    network_id: str
    """Identifier of the network to bind to.

    Only "cf1:network" is currently supported. Mutually exclusive with tunnel_id.
    """

    tunnel_id: str
    """UUID of the Cloudflare Tunnel to bind to. Mutually exclusive with network_id."""


MetadataBinding: TypeAlias = Union[
    MetadataBindingWorkersBindingKindAI,
    MetadataBindingWorkersBindingKindAISearch,
    MetadataBindingWorkersBindingKindAISearchNamespace,
    MetadataBindingWorkersBindingKindAnalyticsEngine,
    MetadataBindingWorkersBindingKindAssets,
    MetadataBindingWorkersBindingKindBrowser,
    MetadataBindingWorkersBindingKindD1,
    MetadataBindingWorkersBindingKindDataBlob,
    MetadataBindingWorkersBindingKindDispatchNamespace,
    MetadataBindingWorkersBindingKindDurableObjectNamespace,
    MetadataBindingWorkersBindingKindHyperdrive,
    MetadataBindingWorkersBindingKindInherit,
    MetadataBindingWorkersBindingKindImages,
    MetadataBindingWorkersBindingKindJson,
    MetadataBindingWorkersBindingKindKVNamespace,
    MetadataBindingWorkersBindingKindMedia,
    MetadataBindingWorkersBindingKindMTLSCertificate,
    MetadataBindingWorkersBindingKindPlainText,
    MetadataBindingWorkersBindingKindPipelines,
    MetadataBindingWorkersBindingKindQueue,
    MetadataBindingWorkersBindingKindRatelimit,
    MetadataBindingWorkersBindingKindR2Bucket,
    MetadataBindingWorkersBindingKindSecretText,
    MetadataBindingWorkersBindingKindSendEmail,
    MetadataBindingWorkersBindingKindService,
    MetadataBindingWorkersBindingKindTextBlob,
    MetadataBindingWorkersBindingKindVectorize,
    MetadataBindingWorkersBindingKindVersionMetadata,
    MetadataBindingWorkersBindingKindSecretsStoreSecret,
    MetadataBindingWorkersBindingKindFlagship,
    MetadataBindingWorkersBindingKindSecretKey,
    MetadataBindingWorkersBindingKindWorkflow,
    MetadataBindingWorkersBindingKindWasmModule,
    MetadataBindingWorkersBindingKindVPCService,
    MetadataBindingWorkersBindingKindVPCNetwork,
]


class MetadataCacheOptions(TypedDict, total=False):
    """Global CacheW configuration for the Worker.

    When caching is on,
    the platform provisions a `cloudflare.app` zone for the Worker.
    A `type: worker` entry in the `exports` map can override this
    value for a single entrypoint.
    """

    enabled: Required[bool]
    """Whether caching is enabled for this Worker."""

    cross_version_cache: bool
    """Whether cached responses are shared across Worker version uploads.

    This is independent of `enabled`. It can stay true while caching is off, so the
    preference survives turning caching off and back on.
    """


class MetadataExportsCache(TypedDict, total=False):
    """Cache override for this entrypoint.

    It applies only to
    `type: worker` entries and overrides the Worker's global
    `cache_options.enabled` for that entrypoint.
    """

    enabled: Required[bool]
    """Whether caching is enabled for this entrypoint."""


class MetadataExports(TypedDict, total=False):
    """
    A single entry in the `exports` map, keyed by export name (a
    `WorkerEntrypoint` class name, a Durable Object class name, or
    `default` for the Worker's default export). Worker entrypoint
    entries set `type: worker` and may carry `cache` configuration
    for that entrypoint. Durable Object entries set
    `type: durable-object` and carry additional provisioning fields.
    """

    type: Required[Literal["worker", "durable-object"]]
    """The kind of export."""

    cache: MetadataExportsCache
    """Cache override for this entrypoint.

    It applies only to `type: worker` entries and overrides the Worker's global
    `cache_options.enabled` for that entrypoint.
    """

    renamed_to: str
    """Destination class name for a `state: renamed` tombstone.

    The target must appear as a live (`created`) entry in the same `exports` map.
    Write-only: never present in GET responses.
    """

    state: Literal["created", "deleted", "renamed", "transferred", "expecting-transfer"]
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

    storage: Literal["sqlite", "legacy-kv"]
    """Storage backend for a `type: durable-object` export.

    Required for live Durable Object entries (`created` and `expecting-transfer`).
    `sqlite` selects SQLite-backed storage; `legacy-kv` selects the legacy key-value
    storage.
    """

    transfer_from: str
    """Source script for a `state: expecting-transfer` entry.

    The namespace on this script is materialised from the source script's data via
    the pending-transfer flow. Present on reads for `expecting-transfer` entries.
    """

    transferred_to: str
    """Destination script for a `state: transferred` tombstone.

    Must reference a script in the same account; cross-dispatch-namespace transfers
    are rejected. Write-only: never present in GET responses.
    """


class MetadataPackageDependency(TypedDict, total=False):
    installed_version: Required[Annotated[str, PropertyInfo(alias="installedVersion")]]
    """The exact version that was resolved and installed by the package manager."""

    name: Required[str]
    """The npm package name."""

    package_json_version: Required[Annotated[str, PropertyInfo(alias="packageJsonVersion")]]
    """The version constraint as written in package.json."""


class Metadata(TypedDict, total=False):
    """JSON-encoded metadata about the uploaded parts and Worker configuration."""

    main_module: Required[str]
    """Name of the uploaded file that contains the main module (e.g.

    the file exporting a `fetch` handler). Indicates a `module syntax` Worker, which
    is required for Version Upload.
    """

    annotations: MetadataAnnotations

    bindings: Iterable[MetadataBinding]
    """List of bindings attached to a Worker.

    You can find more about bindings on our docs:
    https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/#bindings.
    """

    cache_options: MetadataCacheOptions
    """Global CacheW configuration for the Worker.

    When caching is on, the platform provisions a `cloudflare.app` zone for the
    Worker. A `type: worker` entry in the `exports` map can override this value for
    a single entrypoint.
    """

    compatibility_date: str
    """Date indicating targeted support in the Workers runtime.

    Backwards incompatible fixes to the runtime following this date will not affect
    this Worker.
    """

    compatibility_flags: SequenceNotStr[str]
    """Flags that enable or disable certain features in the Workers runtime.

    Used to enable upcoming features or opt in or out of specific changes not
    included in a `compatibility_date`.
    """

    exports: Dict[str, MetadataExports]
    """Declarative exports for this version.

    Worker entrypoint entries (`type: worker`) carry cache configuration for that
    entrypoint.
    """

    keep_bindings: SequenceNotStr[str]
    """List of binding types to keep from previous_upload."""

    package_dependencies: Iterable[MetadataPackageDependency]
    """
    The list of npm packages that were installed and used when this Worker version
    was built.
    """

    usage_model: Literal["standard", "bundled", "unbound"]
    """Usage model for the Worker invocations."""
