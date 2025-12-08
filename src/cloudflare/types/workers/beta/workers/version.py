# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ....._utils import PropertyInfo
from ....._models import BaseModel
from ...single_step_migration import SingleStepMigration

__all__ = [
    "Version",
    "Annotations",
    "Assets",
    "AssetsConfig",
    "Binding",
    "BindingWorkersBindingKindAI",
    "BindingWorkersBindingKindAnalyticsEngine",
    "BindingWorkersBindingKindAssets",
    "BindingWorkersBindingKindBrowser",
    "BindingWorkersBindingKindD1",
    "BindingWorkersBindingKindDataBlob",
    "BindingWorkersBindingKindDispatchNamespace",
    "BindingWorkersBindingKindDispatchNamespaceOutbound",
    "BindingWorkersBindingKindDispatchNamespaceOutboundWorker",
    "BindingWorkersBindingKindDurableObjectNamespace",
    "BindingWorkersBindingKindHyperdrive",
    "BindingWorkersBindingKindInherit",
    "BindingWorkersBindingKindImages",
    "BindingWorkersBindingKindJson",
    "BindingWorkersBindingKindKVNamespace",
    "BindingWorkersBindingKindMTLSCertificate",
    "BindingWorkersBindingKindPlainText",
    "BindingWorkersBindingKindPipelines",
    "BindingWorkersBindingKindQueue",
    "BindingWorkersBindingKindR2Bucket",
    "BindingWorkersBindingKindSecretText",
    "BindingWorkersBindingKindSendEmail",
    "BindingWorkersBindingKindService",
    "BindingWorkersBindingKindTextBlob",
    "BindingWorkersBindingKindVectorize",
    "BindingWorkersBindingKindVersionMetadata",
    "BindingWorkersBindingKindSecretsStoreSecret",
    "BindingWorkersBindingKindSecretKey",
    "BindingWorkersBindingKindWorkflow",
    "BindingWorkersBindingKindWasmModule",
    "Limits",
    "Migrations",
    "MigrationsWorkersMultipleStepMigrations",
    "Module",
    "Placement",
]


class Annotations(BaseModel):
    """Metadata about the version."""

    workers_message: Optional[str] = FieldInfo(alias="workers/message", default=None)
    """Human-readable message about the version."""

    workers_tag: Optional[str] = FieldInfo(alias="workers/tag", default=None)
    """User-provided identifier for the version."""

    workers_triggered_by: Optional[str] = FieldInfo(alias="workers/triggered_by", default=None)
    """Operation that triggered the creation of the version."""


class AssetsConfig(BaseModel):
    """Configuration for assets within a Worker."""

    html_handling: Optional[Literal["auto-trailing-slash", "force-trailing-slash", "drop-trailing-slash", "none"]] = (
        None
    )
    """Determines the redirects and rewrites of requests for HTML content."""

    not_found_handling: Optional[Literal["none", "404-page", "single-page-application"]] = None
    """
    Determines the response when a request does not match a static asset, and there
    is no Worker script.
    """

    run_worker_first: Union[List[str], bool, None] = None
    """Contains a list path rules to control routing to either the Worker or assets.

    Glob (\\**) and negative (!) rules are supported. Rules must start with either '/'
    or '!/'. At least one non-negative rule must be provided, and negative rules
    have higher precedence than non-negative rules.
    """


class Assets(BaseModel):
    """Configuration for assets within a Worker.

    [`_headers`](https://developers.cloudflare.com/workers/static-assets/headers/#custom-headers) and
    [`_redirects`](https://developers.cloudflare.com/workers/static-assets/redirects/) files should be
    included as modules named `_headers` and `_redirects` with content type `text/plain`.
    """

    config: Optional[AssetsConfig] = None
    """Configuration for assets within a Worker."""

    jwt: Optional[str] = None
    """Token provided upon successful upload of all files from a registered manifest."""


class BindingWorkersBindingKindAI(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["ai"]
    """The kind of resource that the binding provides."""


class BindingWorkersBindingKindAnalyticsEngine(BaseModel):
    dataset: str
    """The name of the dataset to bind to."""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["analytics_engine"]
    """The kind of resource that the binding provides."""


class BindingWorkersBindingKindAssets(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["assets"]
    """The kind of resource that the binding provides."""


class BindingWorkersBindingKindBrowser(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["browser"]
    """The kind of resource that the binding provides."""


class BindingWorkersBindingKindD1(BaseModel):
    id: str
    """Identifier of the D1 database to bind to."""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["d1"]
    """The kind of resource that the binding provides."""


class BindingWorkersBindingKindDataBlob(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    part: str
    """The name of the file containing the data content.

    Only accepted for `service worker syntax` Workers.
    """

    type: Literal["data_blob"]
    """The kind of resource that the binding provides."""


class BindingWorkersBindingKindDispatchNamespaceOutboundWorker(BaseModel):
    """Outbound worker."""

    environment: Optional[str] = None
    """Environment of the outbound worker."""

    service: Optional[str] = None
    """Name of the outbound worker."""


class BindingWorkersBindingKindDispatchNamespaceOutbound(BaseModel):
    """Outbound worker."""

    params: Optional[List[str]] = None
    """
    Pass information from the Dispatch Worker to the Outbound Worker through the
    parameters.
    """

    worker: Optional[BindingWorkersBindingKindDispatchNamespaceOutboundWorker] = None
    """Outbound worker."""


class BindingWorkersBindingKindDispatchNamespace(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    namespace: str
    """The name of the dispatch namespace."""

    type: Literal["dispatch_namespace"]
    """The kind of resource that the binding provides."""

    outbound: Optional[BindingWorkersBindingKindDispatchNamespaceOutbound] = None
    """Outbound worker."""


class BindingWorkersBindingKindDurableObjectNamespace(BaseModel):
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


class BindingWorkersBindingKindHyperdrive(BaseModel):
    id: str
    """Identifier of the Hyperdrive connection to bind to."""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["hyperdrive"]
    """The kind of resource that the binding provides."""


class BindingWorkersBindingKindInherit(BaseModel):
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


class BindingWorkersBindingKindImages(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["images"]
    """The kind of resource that the binding provides."""


class BindingWorkersBindingKindJson(BaseModel):
    json_: str = FieldInfo(alias="json")
    """JSON data to use."""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["json"]
    """The kind of resource that the binding provides."""


class BindingWorkersBindingKindKVNamespace(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    namespace_id: str
    """Namespace identifier tag."""

    type: Literal["kv_namespace"]
    """The kind of resource that the binding provides."""


class BindingWorkersBindingKindMTLSCertificate(BaseModel):
    certificate_id: str
    """Identifier of the certificate to bind to."""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["mtls_certificate"]
    """The kind of resource that the binding provides."""


class BindingWorkersBindingKindPlainText(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    text: str
    """The text value to use."""

    type: Literal["plain_text"]
    """The kind of resource that the binding provides."""


class BindingWorkersBindingKindPipelines(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    pipeline: str
    """Name of the Pipeline to bind to."""

    type: Literal["pipelines"]
    """The kind of resource that the binding provides."""


class BindingWorkersBindingKindQueue(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    queue_name: str
    """Name of the Queue to bind to."""

    type: Literal["queue"]
    """The kind of resource that the binding provides."""


class BindingWorkersBindingKindR2Bucket(BaseModel):
    bucket_name: str
    """R2 bucket to bind to."""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["r2_bucket"]
    """The kind of resource that the binding provides."""

    jurisdiction: Optional[Literal["eu", "fedramp"]] = None
    """
    The
    [jurisdiction](https://developers.cloudflare.com/r2/reference/data-location/#jurisdictional-restrictions)
    of the R2 bucket.
    """


class BindingWorkersBindingKindSecretText(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["secret_text"]
    """The kind of resource that the binding provides."""


class BindingWorkersBindingKindSendEmail(BaseModel):
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


class BindingWorkersBindingKindService(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    service: str
    """Name of Worker to bind to."""

    type: Literal["service"]
    """The kind of resource that the binding provides."""

    environment: Optional[str] = None
    """Optional environment if the Worker utilizes one."""


class BindingWorkersBindingKindTextBlob(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    part: str
    """The name of the file containing the text content.

    Only accepted for `service worker syntax` Workers.
    """

    type: Literal["text_blob"]
    """The kind of resource that the binding provides."""


class BindingWorkersBindingKindVectorize(BaseModel):
    index_name: str
    """Name of the Vectorize index to bind to."""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["vectorize"]
    """The kind of resource that the binding provides."""


class BindingWorkersBindingKindVersionMetadata(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["version_metadata"]
    """The kind of resource that the binding provides."""


class BindingWorkersBindingKindSecretsStoreSecret(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    secret_name: str
    """Name of the secret in the store."""

    store_id: str
    """ID of the store containing the secret."""

    type: Literal["secrets_store_secret"]
    """The kind of resource that the binding provides."""


class BindingWorkersBindingKindSecretKey(BaseModel):
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


class BindingWorkersBindingKindWorkflow(BaseModel):
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


class BindingWorkersBindingKindWasmModule(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    part: str
    """The name of the file containing the WebAssembly module content.

    Only accepted for `service worker syntax` Workers.
    """

    type: Literal["wasm_module"]
    """The kind of resource that the binding provides."""


Binding: TypeAlias = Annotated[
    Union[
        BindingWorkersBindingKindAI,
        BindingWorkersBindingKindAnalyticsEngine,
        BindingWorkersBindingKindAssets,
        BindingWorkersBindingKindBrowser,
        BindingWorkersBindingKindD1,
        BindingWorkersBindingKindDataBlob,
        BindingWorkersBindingKindDispatchNamespace,
        BindingWorkersBindingKindDurableObjectNamespace,
        BindingWorkersBindingKindHyperdrive,
        BindingWorkersBindingKindInherit,
        BindingWorkersBindingKindImages,
        BindingWorkersBindingKindJson,
        BindingWorkersBindingKindKVNamespace,
        BindingWorkersBindingKindMTLSCertificate,
        BindingWorkersBindingKindPlainText,
        BindingWorkersBindingKindPipelines,
        BindingWorkersBindingKindQueue,
        BindingWorkersBindingKindR2Bucket,
        BindingWorkersBindingKindSecretText,
        BindingWorkersBindingKindSendEmail,
        BindingWorkersBindingKindService,
        BindingWorkersBindingKindTextBlob,
        BindingWorkersBindingKindVectorize,
        BindingWorkersBindingKindVersionMetadata,
        BindingWorkersBindingKindSecretsStoreSecret,
        BindingWorkersBindingKindSecretKey,
        BindingWorkersBindingKindWorkflow,
        BindingWorkersBindingKindWasmModule,
    ],
    PropertyInfo(discriminator="type"),
]


class Limits(BaseModel):
    """Resource limits enforced at runtime."""

    cpu_ms: int
    """CPU time limit in milliseconds."""


class MigrationsWorkersMultipleStepMigrations(BaseModel):
    pass


Migrations: TypeAlias = Union[SingleStepMigration, MigrationsWorkersMultipleStepMigrations]


class Module(BaseModel):
    content_base64: str
    """The base64-encoded module content."""

    content_type: str
    """The content type of the module."""

    name: str
    """The name of the module."""


class Placement(BaseModel):
    """Placement settings for the version."""

    mode: Optional[Literal["smart"]] = None
    """Placement mode for the version."""


class Version(BaseModel):
    id: str
    """Version identifier."""

    created_on: datetime
    """When the version was created."""

    number: int
    """The integer version number, starting from one."""

    annotations: Optional[Annotations] = None
    """Metadata about the version."""

    assets: Optional[Assets] = None
    """Configuration for assets within a Worker.

    [`_headers`](https://developers.cloudflare.com/workers/static-assets/headers/#custom-headers)
    and
    [`_redirects`](https://developers.cloudflare.com/workers/static-assets/redirects/)
    files should be included as modules named `_headers` and `_redirects` with
    content type `text/plain`.
    """

    bindings: Optional[List[Binding]] = None
    """List of bindings attached to a Worker.

    You can find more about bindings on our docs:
    https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/#bindings.
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

    limits: Optional[Limits] = None
    """Resource limits enforced at runtime."""

    main_module: Optional[str] = None
    """The name of the main module in the `modules` array (e.g.

    the name of the module that exports a `fetch` handler).
    """

    migrations: Optional[Migrations] = None
    """Migrations for Durable Objects associated with the version.

    Migrations are applied when the version is deployed.
    """

    modules: Optional[List[Module]] = None
    """Code, sourcemaps, and other content used at runtime.

    This includes
    [`_headers`](https://developers.cloudflare.com/workers/static-assets/headers/#custom-headers)
    and
    [`_redirects`](https://developers.cloudflare.com/workers/static-assets/redirects/)
    files used to configure
    [Static Assets](https://developers.cloudflare.com/workers/static-assets/).
    `_headers` and `_redirects` files should be included as modules named `_headers`
    and `_redirects` with content type `text/plain`.
    """

    placement: Optional[Placement] = None
    """Placement settings for the version."""

    source: Optional[str] = None
    """The client used to create the version."""

    usage_model: Optional[Literal["standard", "bundled", "unbound"]] = None
    """Usage model for the version."""
