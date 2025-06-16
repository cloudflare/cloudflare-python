# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ...._utils import PropertyInfo
from ...._models import BaseModel

__all__ = [
    "VersionCreateResponse",
    "Resources",
    "ResourcesBindings",
    "ResourcesBindingsResult",
    "ResourcesBindingsResultWorkersBindingKindAI",
    "ResourcesBindingsResultWorkersBindingKindAnalyticsEngine",
    "ResourcesBindingsResultWorkersBindingKindAssets",
    "ResourcesBindingsResultWorkersBindingKindBrowser",
    "ResourcesBindingsResultWorkersBindingKindD1",
    "ResourcesBindingsResultWorkersBindingKindDispatchNamespace",
    "ResourcesBindingsResultWorkersBindingKindDispatchNamespaceOutbound",
    "ResourcesBindingsResultWorkersBindingKindDispatchNamespaceOutboundWorker",
    "ResourcesBindingsResultWorkersBindingKindDurableObjectNamespace",
    "ResourcesBindingsResultWorkersBindingKindHyperdrive",
    "ResourcesBindingsResultWorkersBindingKindJson",
    "ResourcesBindingsResultWorkersBindingKindKVNamespace",
    "ResourcesBindingsResultWorkersBindingKindMTLSCertificate",
    "ResourcesBindingsResultWorkersBindingKindPlainText",
    "ResourcesBindingsResultWorkersBindingKindPipelines",
    "ResourcesBindingsResultWorkersBindingKindQueue",
    "ResourcesBindingsResultWorkersBindingKindR2Bucket",
    "ResourcesBindingsResultWorkersBindingKindSecretText",
    "ResourcesBindingsResultWorkersBindingKindService",
    "ResourcesBindingsResultWorkersBindingKindTailConsumer",
    "ResourcesBindingsResultWorkersBindingKindVectorize",
    "ResourcesBindingsResultWorkersBindingKindVersionMetadata",
    "ResourcesBindingsResultWorkersBindingKindSecretsStoreSecret",
    "ResourcesBindingsResultWorkersBindingKindSecretKey",
    "ResourcesBindingsResultWorkersBindingKindWorkflow",
    "ResourcesScript",
    "ResourcesScriptNamedHandler",
    "ResourcesScriptRuntime",
    "ResourcesScriptRuntimeLimits",
    "Metadata",
]


class ResourcesBindingsResultWorkersBindingKindAI(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["ai"]
    """The kind of resource that the binding provides."""


class ResourcesBindingsResultWorkersBindingKindAnalyticsEngine(BaseModel):
    dataset: str
    """The name of the dataset to bind to."""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["analytics_engine"]
    """The kind of resource that the binding provides."""


class ResourcesBindingsResultWorkersBindingKindAssets(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["assets"]
    """The kind of resource that the binding provides."""


class ResourcesBindingsResultWorkersBindingKindBrowser(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["browser"]
    """The kind of resource that the binding provides."""


class ResourcesBindingsResultWorkersBindingKindD1(BaseModel):
    id: str
    """Identifier of the D1 database to bind to."""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["d1"]
    """The kind of resource that the binding provides."""


class ResourcesBindingsResultWorkersBindingKindDispatchNamespaceOutboundWorker(BaseModel):
    environment: Optional[str] = None
    """Environment of the outbound worker."""

    service: Optional[str] = None
    """Name of the outbound worker."""


class ResourcesBindingsResultWorkersBindingKindDispatchNamespaceOutbound(BaseModel):
    params: Optional[List[str]] = None
    """
    Pass information from the Dispatch Worker to the Outbound Worker through the
    parameters.
    """

    worker: Optional[ResourcesBindingsResultWorkersBindingKindDispatchNamespaceOutboundWorker] = None
    """Outbound worker."""


class ResourcesBindingsResultWorkersBindingKindDispatchNamespace(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    namespace: str
    """Namespace to bind to."""

    type: Literal["dispatch_namespace"]
    """The kind of resource that the binding provides."""

    outbound: Optional[ResourcesBindingsResultWorkersBindingKindDispatchNamespaceOutbound] = None
    """Outbound worker."""


class ResourcesBindingsResultWorkersBindingKindDurableObjectNamespace(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["durable_object_namespace"]
    """The kind of resource that the binding provides."""

    class_name: Optional[str] = None
    """The exported class name of the Durable Object."""

    environment: Optional[str] = None
    """The environment of the script_name to bind to."""

    namespace_id: Optional[str] = None
    """Namespace identifier tag."""

    script_name: Optional[str] = None
    """
    The script where the Durable Object is defined, if it is external to this
    Worker.
    """


class ResourcesBindingsResultWorkersBindingKindHyperdrive(BaseModel):
    id: str
    """Identifier of the Hyperdrive connection to bind to."""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["hyperdrive"]
    """The kind of resource that the binding provides."""


class ResourcesBindingsResultWorkersBindingKindJson(BaseModel):
    json_: str = FieldInfo(alias="json")
    """JSON data to use."""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["json"]
    """The kind of resource that the binding provides."""


class ResourcesBindingsResultWorkersBindingKindKVNamespace(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    namespace_id: str
    """Namespace identifier tag."""

    type: Literal["kv_namespace"]
    """The kind of resource that the binding provides."""


class ResourcesBindingsResultWorkersBindingKindMTLSCertificate(BaseModel):
    certificate_id: str
    """Identifier of the certificate to bind to."""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["mtls_certificate"]
    """The kind of resource that the binding provides."""


class ResourcesBindingsResultWorkersBindingKindPlainText(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    text: str
    """The text value to use."""

    type: Literal["plain_text"]
    """The kind of resource that the binding provides."""


class ResourcesBindingsResultWorkersBindingKindPipelines(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    pipeline: str
    """Name of the Pipeline to bind to."""

    type: Literal["pipelines"]
    """The kind of resource that the binding provides."""


class ResourcesBindingsResultWorkersBindingKindQueue(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    queue_name: str
    """Name of the Queue to bind to."""

    type: Literal["queue"]
    """The kind of resource that the binding provides."""


class ResourcesBindingsResultWorkersBindingKindR2Bucket(BaseModel):
    bucket_name: str
    """R2 bucket to bind to."""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["r2_bucket"]
    """The kind of resource that the binding provides."""


class ResourcesBindingsResultWorkersBindingKindSecretText(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["secret_text"]
    """The kind of resource that the binding provides."""


class ResourcesBindingsResultWorkersBindingKindService(BaseModel):
    environment: str
    """Optional environment if the Worker utilizes one."""

    name: str
    """A JavaScript variable name for the binding."""

    service: str
    """Name of Worker to bind to."""

    type: Literal["service"]
    """The kind of resource that the binding provides."""


class ResourcesBindingsResultWorkersBindingKindTailConsumer(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    service: str
    """Name of Tail Worker to bind to."""

    type: Literal["tail_consumer"]
    """The kind of resource that the binding provides."""


class ResourcesBindingsResultWorkersBindingKindVectorize(BaseModel):
    index_name: str
    """Name of the Vectorize index to bind to."""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["vectorize"]
    """The kind of resource that the binding provides."""


class ResourcesBindingsResultWorkersBindingKindVersionMetadata(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["version_metadata"]
    """The kind of resource that the binding provides."""


class ResourcesBindingsResultWorkersBindingKindSecretsStoreSecret(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    secret_name: str
    """Name of the secret in the store."""

    store_id: str
    """ID of the store containing the secret."""

    type: Literal["secrets_store_secret"]
    """The kind of resource that the binding provides."""


class ResourcesBindingsResultWorkersBindingKindSecretKey(BaseModel):
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


class ResourcesBindingsResultWorkersBindingKindWorkflow(BaseModel):
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


ResourcesBindingsResult: TypeAlias = Annotated[
    Union[
        ResourcesBindingsResultWorkersBindingKindAI,
        ResourcesBindingsResultWorkersBindingKindAnalyticsEngine,
        ResourcesBindingsResultWorkersBindingKindAssets,
        ResourcesBindingsResultWorkersBindingKindBrowser,
        ResourcesBindingsResultWorkersBindingKindD1,
        ResourcesBindingsResultWorkersBindingKindDispatchNamespace,
        ResourcesBindingsResultWorkersBindingKindDurableObjectNamespace,
        ResourcesBindingsResultWorkersBindingKindHyperdrive,
        ResourcesBindingsResultWorkersBindingKindJson,
        ResourcesBindingsResultWorkersBindingKindKVNamespace,
        ResourcesBindingsResultWorkersBindingKindMTLSCertificate,
        ResourcesBindingsResultWorkersBindingKindPlainText,
        ResourcesBindingsResultWorkersBindingKindPipelines,
        ResourcesBindingsResultWorkersBindingKindQueue,
        ResourcesBindingsResultWorkersBindingKindR2Bucket,
        ResourcesBindingsResultWorkersBindingKindSecretText,
        ResourcesBindingsResultWorkersBindingKindService,
        ResourcesBindingsResultWorkersBindingKindTailConsumer,
        ResourcesBindingsResultWorkersBindingKindVectorize,
        ResourcesBindingsResultWorkersBindingKindVersionMetadata,
        ResourcesBindingsResultWorkersBindingKindSecretsStoreSecret,
        ResourcesBindingsResultWorkersBindingKindSecretKey,
        ResourcesBindingsResultWorkersBindingKindWorkflow,
    ],
    PropertyInfo(discriminator="type"),
]


class ResourcesBindings(BaseModel):
    result: Optional[List[ResourcesBindingsResult]] = None
    """List of bindings attached to a Worker.

    You can find more about bindings on our docs:
    https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/#bindings.
    """


class ResourcesScriptNamedHandler(BaseModel):
    handlers: Optional[List[str]] = None

    name: Optional[str] = None


class ResourcesScript(BaseModel):
    etag: Optional[str] = None

    handlers: Optional[List[str]] = None

    last_deployed_from: Optional[str] = None

    named_handlers: Optional[List[ResourcesScriptNamedHandler]] = None


class ResourcesScriptRuntimeLimits(BaseModel):
    cpu_ms: Optional[int] = None


class ResourcesScriptRuntime(BaseModel):
    compatibility_date: Optional[str] = None

    compatibility_flags: Optional[List[str]] = None

    limits: Optional[ResourcesScriptRuntimeLimits] = None

    migration_tag: Optional[str] = None

    usage_model: Optional[Literal["bundled", "unbound", "standard"]] = None


class Resources(BaseModel):
    bindings: Optional[ResourcesBindings] = None

    script: Optional[ResourcesScript] = None

    script_runtime: Optional[ResourcesScriptRuntime] = None


class Metadata(BaseModel):
    author_email: Optional[str] = None

    author_id: Optional[str] = None

    created_on: Optional[str] = None

    has_preview: Optional[bool] = FieldInfo(alias="hasPreview", default=None)

    modified_on: Optional[str] = None

    source: Optional[
        Literal[
            "unknown",
            "api",
            "wrangler",
            "terraform",
            "dash",
            "dash_template",
            "integration",
            "quick_editor",
            "playground",
            "workersci",
        ]
    ] = None


class VersionCreateResponse(BaseModel):
    resources: Resources

    id: Optional[str] = None

    metadata: Optional[Metadata] = None

    number: Optional[float] = None

    startup_time_ms: Optional[int] = None
