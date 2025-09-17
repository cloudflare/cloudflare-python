# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ...._types import FileTypes, SequenceNotStr
from ...._utils import PropertyInfo

__all__ = [
    "VersionCreateParams",
    "Metadata",
    "MetadataAnnotations",
    "MetadataBinding",
    "MetadataBindingWorkersBindingKindAI",
    "MetadataBindingWorkersBindingKindAnalyticsEngine",
    "MetadataBindingWorkersBindingKindAssets",
    "MetadataBindingWorkersBindingKindBrowser",
    "MetadataBindingWorkersBindingKindD1",
    "MetadataBindingWorkersBindingKindDataBlob",
    "MetadataBindingWorkersBindingKindDispatchNamespace",
    "MetadataBindingWorkersBindingKindDispatchNamespaceOutbound",
    "MetadataBindingWorkersBindingKindDispatchNamespaceOutboundWorker",
    "MetadataBindingWorkersBindingKindDurableObjectNamespace",
    "MetadataBindingWorkersBindingKindHyperdrive",
    "MetadataBindingWorkersBindingKindInherit",
    "MetadataBindingWorkersBindingKindImages",
    "MetadataBindingWorkersBindingKindJson",
    "MetadataBindingWorkersBindingKindKVNamespace",
    "MetadataBindingWorkersBindingKindMTLSCertificate",
    "MetadataBindingWorkersBindingKindPlainText",
    "MetadataBindingWorkersBindingKindPipelines",
    "MetadataBindingWorkersBindingKindQueue",
    "MetadataBindingWorkersBindingKindR2Bucket",
    "MetadataBindingWorkersBindingKindSecretText",
    "MetadataBindingWorkersBindingKindSendEmail",
    "MetadataBindingWorkersBindingKindService",
    "MetadataBindingWorkersBindingKindTailConsumer",
    "MetadataBindingWorkersBindingKindTextBlob",
    "MetadataBindingWorkersBindingKindVectorize",
    "MetadataBindingWorkersBindingKindVersionMetadata",
    "MetadataBindingWorkersBindingKindSecretsStoreSecret",
    "MetadataBindingWorkersBindingKindSecretKey",
    "MetadataBindingWorkersBindingKindWorkflow",
    "MetadataBindingWorkersBindingKindWasmModule",
]


class VersionCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    metadata: Required[Metadata]
    """JSON-encoded metadata about the uploaded parts and Worker configuration."""

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
    workers_message: Annotated[str, PropertyInfo(alias="workers/message")]
    """Human-readable message about the version. Truncated to 100 bytes."""

    workers_tag: Annotated[str, PropertyInfo(alias="workers/tag")]
    """User-provided identifier for the version."""


class MetadataBindingWorkersBindingKindAI(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["ai"]]
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
    id: Required[str]
    """Identifier of the D1 database to bind to."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["d1"]]
    """The kind of resource that the binding provides."""


class MetadataBindingWorkersBindingKindDataBlob(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    part: Required[str]
    """The name of the file containing the data content.

    Only accepted for `service worker syntax` Workers.
    """

    type: Required[Literal["data_blob"]]
    """The kind of resource that the binding provides."""


class MetadataBindingWorkersBindingKindDispatchNamespaceOutboundWorker(TypedDict, total=False):
    environment: str
    """Environment of the outbound worker."""

    service: str
    """Name of the outbound worker."""


class MetadataBindingWorkersBindingKindDispatchNamespaceOutbound(TypedDict, total=False):
    params: SequenceNotStr[str]
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
    """Namespace to bind to."""

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
    json: Required[str]
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


class MetadataBindingWorkersBindingKindR2Bucket(TypedDict, total=False):
    bucket_name: Required[str]
    """R2 bucket to bind to."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["r2_bucket"]]
    """The kind of resource that the binding provides."""


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

    environment: str
    """Optional environment if the Worker utilizes one."""


class MetadataBindingWorkersBindingKindTailConsumer(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    service: Required[str]
    """Name of Tail Worker to bind to."""

    type: Required[Literal["tail_consumer"]]
    """The kind of resource that the binding provides."""


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


MetadataBinding: TypeAlias = Union[
    MetadataBindingWorkersBindingKindAI,
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
    MetadataBindingWorkersBindingKindMTLSCertificate,
    MetadataBindingWorkersBindingKindPlainText,
    MetadataBindingWorkersBindingKindPipelines,
    MetadataBindingWorkersBindingKindQueue,
    MetadataBindingWorkersBindingKindR2Bucket,
    MetadataBindingWorkersBindingKindSecretText,
    MetadataBindingWorkersBindingKindSendEmail,
    MetadataBindingWorkersBindingKindService,
    MetadataBindingWorkersBindingKindTailConsumer,
    MetadataBindingWorkersBindingKindTextBlob,
    MetadataBindingWorkersBindingKindVectorize,
    MetadataBindingWorkersBindingKindVersionMetadata,
    MetadataBindingWorkersBindingKindSecretsStoreSecret,
    MetadataBindingWorkersBindingKindSecretKey,
    MetadataBindingWorkersBindingKindWorkflow,
    MetadataBindingWorkersBindingKindWasmModule,
]


class Metadata(TypedDict, total=False):
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

    keep_bindings: SequenceNotStr[str]
    """List of binding types to keep from previous_upload."""

    usage_model: Literal["standard", "bundled", "unbound"]
    """Usage model for the Worker invocations."""
