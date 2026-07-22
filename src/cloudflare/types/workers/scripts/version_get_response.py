# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ...._utils import PropertyInfo
from ...._models import BaseModel

__all__ = [
    "VersionGetResponse",
    "Resources",
    "ResourcesBinding",
    "ResourcesBindingWorkersBindingKindAI",
    "ResourcesBindingWorkersBindingKindAISearch",
    "ResourcesBindingWorkersBindingKindAISearchNamespace",
    "ResourcesBindingWorkersBindingKindAnalyticsEngine",
    "ResourcesBindingWorkersBindingKindAssets",
    "ResourcesBindingWorkersBindingKindBrowser",
    "ResourcesBindingWorkersBindingKindD1",
    "ResourcesBindingWorkersBindingKindDataBlob",
    "ResourcesBindingWorkersBindingKindDispatchNamespace",
    "ResourcesBindingWorkersBindingKindDispatchNamespaceOutbound",
    "ResourcesBindingWorkersBindingKindDispatchNamespaceOutboundParam",
    "ResourcesBindingWorkersBindingKindDispatchNamespaceOutboundWorker",
    "ResourcesBindingWorkersBindingKindDurableObjectNamespace",
    "ResourcesBindingWorkersBindingKindHyperdrive",
    "ResourcesBindingWorkersBindingKindInherit",
    "ResourcesBindingWorkersBindingKindImages",
    "ResourcesBindingWorkersBindingKindJson",
    "ResourcesBindingWorkersBindingKindKVNamespace",
    "ResourcesBindingWorkersBindingKindMedia",
    "ResourcesBindingWorkersBindingKindMTLSCertificate",
    "ResourcesBindingWorkersBindingKindPlainText",
    "ResourcesBindingWorkersBindingKindPipelines",
    "ResourcesBindingWorkersBindingKindQueue",
    "ResourcesBindingWorkersBindingKindRatelimit",
    "ResourcesBindingWorkersBindingKindRatelimitSimple",
    "ResourcesBindingWorkersBindingKindR2Bucket",
    "ResourcesBindingWorkersBindingKindSecretText",
    "ResourcesBindingWorkersBindingKindSendEmail",
    "ResourcesBindingWorkersBindingKindService",
    "ResourcesBindingWorkersBindingKindTextBlob",
    "ResourcesBindingWorkersBindingKindVectorize",
    "ResourcesBindingWorkersBindingKindVersionMetadata",
    "ResourcesBindingWorkersBindingKindSecretsStoreSecret",
    "ResourcesBindingWorkersBindingKindFlagship",
    "ResourcesBindingWorkersBindingKindSecretKey",
    "ResourcesBindingWorkersBindingKindWorkflow",
    "ResourcesBindingWorkersBindingKindWasmModule",
    "ResourcesBindingWorkersBindingKindVPCService",
    "ResourcesBindingWorkersBindingKindVPCNetwork",
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


class ResourcesBindingWorkersBindingKindAI(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["ai"]
    """The kind of resource that the binding provides."""


class ResourcesBindingWorkersBindingKindAISearch(BaseModel):
    instance_name: str
    """The user-chosen instance name.

    Must exist at deploy time. The worker can search, chat, update, and manage
    items/jobs on this instance.
    """

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["ai_search"]
    """The kind of resource that the binding provides."""

    namespace: Optional[str] = None
    """The namespace the instance belongs to.

    Defaults to "default" if omitted. Customers who don't use namespaces can simply
    omit this field.
    """


class ResourcesBindingWorkersBindingKindAISearchNamespace(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    namespace: str
    """The user-chosen namespace name.

    Must exist before deploy -- Wrangler handles auto-creation on deploy failure (R2
    bucket pattern). The "default" namespace is auto-created by config-api for new
    accounts. Grants full access (CRUD + search + chat) to all instances within the
    namespace.
    """

    type: Literal["ai_search_namespace"]
    """The kind of resource that the binding provides."""


class ResourcesBindingWorkersBindingKindAnalyticsEngine(BaseModel):
    dataset: str
    """The name of the dataset to bind to."""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["analytics_engine"]
    """The kind of resource that the binding provides."""


class ResourcesBindingWorkersBindingKindAssets(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["assets"]
    """The kind of resource that the binding provides."""


class ResourcesBindingWorkersBindingKindBrowser(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["browser"]
    """The kind of resource that the binding provides."""


class ResourcesBindingWorkersBindingKindD1(BaseModel):
    database_id: str
    """Identifier of the D1 database to bind to."""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["d1"]
    """The kind of resource that the binding provides."""

    id: Optional[str] = None
    """Identifier of the D1 database to bind to."""


class ResourcesBindingWorkersBindingKindDataBlob(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    part: str
    """The name of the file containing the data content.

    Only accepted for `service worker syntax` Workers.
    """

    type: Literal["data_blob"]
    """The kind of resource that the binding provides."""


class ResourcesBindingWorkersBindingKindDispatchNamespaceOutboundParam(BaseModel):
    name: str
    """Name of the parameter."""


class ResourcesBindingWorkersBindingKindDispatchNamespaceOutboundWorker(BaseModel):
    """Outbound worker."""

    entrypoint: Optional[str] = None
    """Entrypoint to invoke on the outbound worker."""

    environment: Optional[str] = None
    """Environment of the outbound worker."""

    service: Optional[str] = None
    """Name of the outbound worker."""


class ResourcesBindingWorkersBindingKindDispatchNamespaceOutbound(BaseModel):
    """Outbound worker."""

    params: Optional[List[ResourcesBindingWorkersBindingKindDispatchNamespaceOutboundParam]] = None
    """
    Pass information from the Dispatch Worker to the Outbound Worker through the
    parameters.
    """

    worker: Optional[ResourcesBindingWorkersBindingKindDispatchNamespaceOutboundWorker] = None
    """Outbound worker."""


class ResourcesBindingWorkersBindingKindDispatchNamespace(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    namespace: str
    """The name of the dispatch namespace."""

    type: Literal["dispatch_namespace"]
    """The kind of resource that the binding provides."""

    outbound: Optional[ResourcesBindingWorkersBindingKindDispatchNamespaceOutbound] = None
    """Outbound worker."""


class ResourcesBindingWorkersBindingKindDurableObjectNamespace(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["durable_object_namespace"]
    """The kind of resource that the binding provides."""

    class_name: Optional[str] = None
    """The exported class name of the Durable Object."""

    dispatch_namespace: Optional[str] = None
    """The dispatch namespace the Durable Object script belongs to."""

    environment: Optional[str] = None
    """The environment of the script_name to bind to."""

    namespace_id: Optional[str] = None
    """Namespace identifier tag."""

    script_name: Optional[str] = None
    """
    The script where the Durable Object is defined, if it is external to this
    Worker.
    """


class ResourcesBindingWorkersBindingKindHyperdrive(BaseModel):
    id: str
    """Identifier of the Hyperdrive connection to bind to."""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["hyperdrive"]
    """The kind of resource that the binding provides."""


class ResourcesBindingWorkersBindingKindInherit(BaseModel):
    name: str
    """The name of the inherited binding."""

    type: Literal["inherit"]
    """The kind of resource that the binding provides."""

    old_name: Optional[str] = None
    """The old name of the inherited binding.

    If set, the binding will be renamed from `old_name` to `name` in the new
    version. If not set, the binding will keep the same name between versions.
    """

    version_id: Optional[str] = None
    """
    Identifier for the version to inherit the binding from, which can be the version
    ID or the literal "latest" to inherit from the latest version. Defaults to
    inheriting the binding from the latest version.
    """


class ResourcesBindingWorkersBindingKindImages(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["images"]
    """The kind of resource that the binding provides."""


class ResourcesBindingWorkersBindingKindJson(BaseModel):
    json_: object = FieldInfo(alias="json")
    """JSON data to use."""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["json"]
    """The kind of resource that the binding provides."""


class ResourcesBindingWorkersBindingKindKVNamespace(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    namespace_id: str
    """Namespace identifier tag."""

    type: Literal["kv_namespace"]
    """The kind of resource that the binding provides."""


class ResourcesBindingWorkersBindingKindMedia(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["media"]
    """The kind of resource that the binding provides."""


class ResourcesBindingWorkersBindingKindMTLSCertificate(BaseModel):
    certificate_id: str
    """Identifier of the certificate to bind to."""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["mtls_certificate"]
    """The kind of resource that the binding provides."""


class ResourcesBindingWorkersBindingKindPlainText(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    text: str
    """The text value to use."""

    type: Literal["plain_text"]
    """The kind of resource that the binding provides."""


class ResourcesBindingWorkersBindingKindPipelines(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    pipeline: str
    """Name of the Pipeline to bind to."""

    type: Literal["pipelines"]
    """The kind of resource that the binding provides."""


class ResourcesBindingWorkersBindingKindQueue(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    queue_name: str
    """Name of the Queue to bind to."""

    type: Literal["queue"]
    """The kind of resource that the binding provides."""


class ResourcesBindingWorkersBindingKindRatelimitSimple(BaseModel):
    """The rate limit configuration."""

    limit: float
    """The limit (requests per period)."""

    period: int
    """The period in seconds."""

    mitigation_timeout: Optional[int] = None
    """
    Duration in seconds to apply the mitigation action after the rate limit is
    exceeded. Valid values are 0 (disabled), 10, or multiples of 60 up to 86400.
    Must be greater than or equal to the period when non-zero.
    """


class ResourcesBindingWorkersBindingKindRatelimit(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    namespace_id: str
    """Identifier of the rate limit namespace to bind to."""

    simple: ResourcesBindingWorkersBindingKindRatelimitSimple
    """The rate limit configuration."""

    type: Literal["ratelimit"]
    """The kind of resource that the binding provides."""


class ResourcesBindingWorkersBindingKindR2Bucket(BaseModel):
    bucket_name: str
    """R2 bucket to bind to."""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["r2_bucket"]
    """The kind of resource that the binding provides."""

    jurisdiction: Optional[Literal["eu", "fedramp", "fedramp-high"]] = None
    """
    The
    [jurisdiction](https://developers.cloudflare.com/r2/reference/data-location/#jurisdictional-restrictions)
    of the R2 bucket.
    """


class ResourcesBindingWorkersBindingKindSecretText(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["secret_text"]
    """The kind of resource that the binding provides."""


class ResourcesBindingWorkersBindingKindSendEmail(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["send_email"]
    """The kind of resource that the binding provides."""

    allowed_destination_addresses: Optional[List[str]] = None
    """List of allowed destination addresses."""

    allowed_sender_addresses: Optional[List[str]] = None
    """List of allowed sender addresses."""

    destination_address: Optional[str] = None
    """Destination address for the email."""


class ResourcesBindingWorkersBindingKindService(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    service: str
    """Name of Worker to bind to."""

    type: Literal["service"]
    """The kind of resource that the binding provides."""

    entrypoint: Optional[str] = None
    """Entrypoint to invoke on the target Worker."""

    environment: Optional[str] = None
    """Optional environment if the Worker utilizes one."""


class ResourcesBindingWorkersBindingKindTextBlob(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    part: str
    """The name of the file containing the text content.

    Only accepted for `service worker syntax` Workers.
    """

    type: Literal["text_blob"]
    """The kind of resource that the binding provides."""


class ResourcesBindingWorkersBindingKindVectorize(BaseModel):
    index_name: str
    """Name of the Vectorize index to bind to."""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["vectorize"]
    """The kind of resource that the binding provides."""


class ResourcesBindingWorkersBindingKindVersionMetadata(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["version_metadata"]
    """The kind of resource that the binding provides."""


class ResourcesBindingWorkersBindingKindSecretsStoreSecret(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    secret_name: str
    """Name of the secret in the store."""

    store_id: str
    """ID of the store containing the secret."""

    type: Literal["secrets_store_secret"]
    """The kind of resource that the binding provides."""


class ResourcesBindingWorkersBindingKindFlagship(BaseModel):
    app_id: str
    """ID of the Flagship app to bind to for feature flag evaluation."""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["flagship"]
    """The kind of resource that the binding provides."""


class ResourcesBindingWorkersBindingKindSecretKey(BaseModel):
    algorithm: object
    """Algorithm-specific key parameters.

    [Learn more](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#algorithm).
    """

    format: Literal["raw", "pkcs8", "spki", "jwk"]
    """Data format of the key.

    [Learn more](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#format).
    """

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["secret_key"]
    """The kind of resource that the binding provides."""

    usages: List[Literal["encrypt", "decrypt", "sign", "verify", "deriveKey", "deriveBits", "wrapKey", "unwrapKey"]]
    """Allowed operations with the key.

    [Learn more](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#keyUsages).
    """


class ResourcesBindingWorkersBindingKindWorkflow(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["workflow"]
    """The kind of resource that the binding provides."""

    workflow_name: str
    """Name of the Workflow to bind to."""

    class_name: Optional[str] = None
    """Class name of the Workflow.

    Should only be provided if the Workflow belongs to this script.
    """

    script_name: Optional[str] = None
    """Script name that contains the Workflow.

    If not provided, defaults to this script name.
    """


class ResourcesBindingWorkersBindingKindWasmModule(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    part: str
    """The name of the file containing the WebAssembly module content.

    Only accepted for `service worker syntax` Workers.
    """

    type: Literal["wasm_module"]
    """The kind of resource that the binding provides."""


class ResourcesBindingWorkersBindingKindVPCService(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    service_id: str
    """Identifier of the VPC service to bind to."""

    type: Literal["vpc_service"]
    """The kind of resource that the binding provides."""


class ResourcesBindingWorkersBindingKindVPCNetwork(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["vpc_network"]
    """The kind of resource that the binding provides."""

    network_id: Optional[str] = None
    """Identifier of the network to bind to.

    Only "cf1:network" is currently supported. Mutually exclusive with tunnel_id.
    """

    tunnel_id: Optional[str] = None
    """UUID of the Cloudflare Tunnel to bind to. Mutually exclusive with network_id."""


ResourcesBinding: TypeAlias = Annotated[
    Union[
        ResourcesBindingWorkersBindingKindAI,
        ResourcesBindingWorkersBindingKindAISearch,
        ResourcesBindingWorkersBindingKindAISearchNamespace,
        ResourcesBindingWorkersBindingKindAnalyticsEngine,
        ResourcesBindingWorkersBindingKindAssets,
        ResourcesBindingWorkersBindingKindBrowser,
        ResourcesBindingWorkersBindingKindD1,
        ResourcesBindingWorkersBindingKindDataBlob,
        ResourcesBindingWorkersBindingKindDispatchNamespace,
        ResourcesBindingWorkersBindingKindDurableObjectNamespace,
        ResourcesBindingWorkersBindingKindHyperdrive,
        ResourcesBindingWorkersBindingKindInherit,
        ResourcesBindingWorkersBindingKindImages,
        ResourcesBindingWorkersBindingKindJson,
        ResourcesBindingWorkersBindingKindKVNamespace,
        ResourcesBindingWorkersBindingKindMedia,
        ResourcesBindingWorkersBindingKindMTLSCertificate,
        ResourcesBindingWorkersBindingKindPlainText,
        ResourcesBindingWorkersBindingKindPipelines,
        ResourcesBindingWorkersBindingKindQueue,
        ResourcesBindingWorkersBindingKindRatelimit,
        ResourcesBindingWorkersBindingKindR2Bucket,
        ResourcesBindingWorkersBindingKindSecretText,
        ResourcesBindingWorkersBindingKindSendEmail,
        ResourcesBindingWorkersBindingKindService,
        ResourcesBindingWorkersBindingKindTextBlob,
        ResourcesBindingWorkersBindingKindVectorize,
        ResourcesBindingWorkersBindingKindVersionMetadata,
        ResourcesBindingWorkersBindingKindSecretsStoreSecret,
        ResourcesBindingWorkersBindingKindFlagship,
        ResourcesBindingWorkersBindingKindSecretKey,
        ResourcesBindingWorkersBindingKindWorkflow,
        ResourcesBindingWorkersBindingKindWasmModule,
        ResourcesBindingWorkersBindingKindVPCService,
        ResourcesBindingWorkersBindingKindVPCNetwork,
    ],
    PropertyInfo(discriminator="type"),
]


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
    bindings: Optional[List[ResourcesBinding]] = None
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
