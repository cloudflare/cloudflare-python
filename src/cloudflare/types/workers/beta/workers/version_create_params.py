# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ....._types import SequenceNotStr, Base64FileInput
from ....._utils import PropertyInfo
from ....._models import set_pydantic_config
from ...migration_step_param import MigrationStepParam
from ...single_step_migration_param import SingleStepMigrationParam

__all__ = [
    "VersionCreateParams",
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


class VersionCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    deploy: bool
    """
    If true, a deployment will be created that sends 100% of traffic to the new
    version.
    """

    annotations: Annotations
    """Metadata about the version."""

    assets: Assets
    """Configuration for assets within a Worker.

    [`_headers`](https://developers.cloudflare.com/workers/static-assets/headers/#custom-headers)
    and
    [`_redirects`](https://developers.cloudflare.com/workers/static-assets/redirects/)
    files should be included as modules named `_headers` and `_redirects` with
    content type `text/plain`.
    """

    bindings: Iterable[Binding]
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

    limits: Limits
    """Resource limits enforced at runtime."""

    main_module: str
    """The name of the main module in the `modules` array (e.g.

    the name of the module that exports a `fetch` handler).
    """

    migrations: Migrations
    """Migrations for Durable Objects associated with the version.

    Migrations are applied when the version is deployed.
    """

    modules: Iterable[Module]
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

    placement: Placement
    """Placement settings for the version."""

    usage_model: Literal["standard", "bundled", "unbound"]
    """Usage model for the version."""


class Annotations(TypedDict, total=False):
    """Metadata about the version."""

    workers_message: Annotated[str, PropertyInfo(alias="workers/message")]
    """Human-readable message about the version."""

    workers_tag: Annotated[str, PropertyInfo(alias="workers/tag")]
    """User-provided identifier for the version."""


class AssetsConfig(TypedDict, total=False):
    """Configuration for assets within a Worker."""

    html_handling: Literal["auto-trailing-slash", "force-trailing-slash", "drop-trailing-slash", "none"]
    """Determines the redirects and rewrites of requests for HTML content."""

    not_found_handling: Literal["none", "404-page", "single-page-application"]
    """
    Determines the response when a request does not match a static asset, and there
    is no Worker script.
    """

    run_worker_first: Union[SequenceNotStr[str], bool]
    """Contains a list path rules to control routing to either the Worker or assets.

    Glob (\\**) and negative (!) rules are supported. Rules must start with either '/'
    or '!/'. At least one non-negative rule must be provided, and negative rules
    have higher precedence than non-negative rules.
    """


class Assets(TypedDict, total=False):
    """Configuration for assets within a Worker.

    [`_headers`](https://developers.cloudflare.com/workers/static-assets/headers/#custom-headers) and
    [`_redirects`](https://developers.cloudflare.com/workers/static-assets/redirects/) files should be
    included as modules named `_headers` and `_redirects` with content type `text/plain`.
    """

    config: AssetsConfig
    """Configuration for assets within a Worker."""

    jwt: str
    """Token provided upon successful upload of all files from a registered manifest."""


class BindingWorkersBindingKindAI(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["ai"]]
    """The kind of resource that the binding provides."""


class BindingWorkersBindingKindAnalyticsEngine(TypedDict, total=False):
    dataset: Required[str]
    """The name of the dataset to bind to."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["analytics_engine"]]
    """The kind of resource that the binding provides."""


class BindingWorkersBindingKindAssets(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["assets"]]
    """The kind of resource that the binding provides."""


class BindingWorkersBindingKindBrowser(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["browser"]]
    """The kind of resource that the binding provides."""


class BindingWorkersBindingKindD1(TypedDict, total=False):
    id: Required[str]
    """Identifier of the D1 database to bind to."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["d1"]]
    """The kind of resource that the binding provides."""


class BindingWorkersBindingKindDataBlob(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    part: Required[str]
    """The name of the file containing the data content.

    Only accepted for `service worker syntax` Workers.
    """

    type: Required[Literal["data_blob"]]
    """The kind of resource that the binding provides."""


class BindingWorkersBindingKindDispatchNamespaceOutboundWorker(TypedDict, total=False):
    """Outbound worker."""

    environment: str
    """Environment of the outbound worker."""

    service: str
    """Name of the outbound worker."""


class BindingWorkersBindingKindDispatchNamespaceOutbound(TypedDict, total=False):
    """Outbound worker."""

    params: SequenceNotStr[str]
    """
    Pass information from the Dispatch Worker to the Outbound Worker through the
    parameters.
    """

    worker: BindingWorkersBindingKindDispatchNamespaceOutboundWorker
    """Outbound worker."""


class BindingWorkersBindingKindDispatchNamespace(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    namespace: Required[str]
    """The name of the dispatch namespace."""

    type: Required[Literal["dispatch_namespace"]]
    """The kind of resource that the binding provides."""

    outbound: BindingWorkersBindingKindDispatchNamespaceOutbound
    """Outbound worker."""


class BindingWorkersBindingKindDurableObjectNamespace(TypedDict, total=False):
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


class BindingWorkersBindingKindHyperdrive(TypedDict, total=False):
    id: Required[str]
    """Identifier of the Hyperdrive connection to bind to."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["hyperdrive"]]
    """The kind of resource that the binding provides."""


class BindingWorkersBindingKindInherit(TypedDict, total=False):
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


class BindingWorkersBindingKindImages(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["images"]]
    """The kind of resource that the binding provides."""


class BindingWorkersBindingKindJson(TypedDict, total=False):
    json: Required[str]
    """JSON data to use."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["json"]]
    """The kind of resource that the binding provides."""


class BindingWorkersBindingKindKVNamespace(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    namespace_id: Required[str]
    """Namespace identifier tag."""

    type: Required[Literal["kv_namespace"]]
    """The kind of resource that the binding provides."""


class BindingWorkersBindingKindMTLSCertificate(TypedDict, total=False):
    certificate_id: Required[str]
    """Identifier of the certificate to bind to."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["mtls_certificate"]]
    """The kind of resource that the binding provides."""


class BindingWorkersBindingKindPlainText(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    text: Required[str]
    """The text value to use."""

    type: Required[Literal["plain_text"]]
    """The kind of resource that the binding provides."""


class BindingWorkersBindingKindPipelines(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    pipeline: Required[str]
    """Name of the Pipeline to bind to."""

    type: Required[Literal["pipelines"]]
    """The kind of resource that the binding provides."""


class BindingWorkersBindingKindQueue(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    queue_name: Required[str]
    """Name of the Queue to bind to."""

    type: Required[Literal["queue"]]
    """The kind of resource that the binding provides."""


class BindingWorkersBindingKindR2Bucket(TypedDict, total=False):
    bucket_name: Required[str]
    """R2 bucket to bind to."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["r2_bucket"]]
    """The kind of resource that the binding provides."""

    jurisdiction: Literal["eu", "fedramp"]
    """
    The
    [jurisdiction](https://developers.cloudflare.com/r2/reference/data-location/#jurisdictional-restrictions)
    of the R2 bucket.
    """


class BindingWorkersBindingKindSecretText(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    text: Required[str]
    """The secret value to use."""

    type: Required[Literal["secret_text"]]
    """The kind of resource that the binding provides."""


class BindingWorkersBindingKindSendEmail(TypedDict, total=False):
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


class BindingWorkersBindingKindService(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    service: Required[str]
    """Name of Worker to bind to."""

    type: Required[Literal["service"]]
    """The kind of resource that the binding provides."""

    environment: str
    """Optional environment if the Worker utilizes one."""


class BindingWorkersBindingKindTextBlob(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    part: Required[str]
    """The name of the file containing the text content.

    Only accepted for `service worker syntax` Workers.
    """

    type: Required[Literal["text_blob"]]
    """The kind of resource that the binding provides."""


class BindingWorkersBindingKindVectorize(TypedDict, total=False):
    index_name: Required[str]
    """Name of the Vectorize index to bind to."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["vectorize"]]
    """The kind of resource that the binding provides."""


class BindingWorkersBindingKindVersionMetadata(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["version_metadata"]]
    """The kind of resource that the binding provides."""


class BindingWorkersBindingKindSecretsStoreSecret(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    secret_name: Required[str]
    """Name of the secret in the store."""

    store_id: Required[str]
    """ID of the store containing the secret."""

    type: Required[Literal["secrets_store_secret"]]
    """The kind of resource that the binding provides."""


class BindingWorkersBindingKindSecretKey(TypedDict, total=False):
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


class BindingWorkersBindingKindWorkflow(TypedDict, total=False):
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


class BindingWorkersBindingKindWasmModule(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    part: Required[str]
    """The name of the file containing the WebAssembly module content.

    Only accepted for `service worker syntax` Workers.
    """

    type: Required[Literal["wasm_module"]]
    """The kind of resource that the binding provides."""


Binding: TypeAlias = Union[
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
]


class Limits(TypedDict, total=False):
    """Resource limits enforced at runtime."""

    cpu_ms: Required[int]
    """CPU time limit in milliseconds."""


class MigrationsWorkersMultipleStepMigrations(TypedDict, total=False):
    new_tag: str
    """Tag to set as the latest migration tag."""

    old_tag: str
    """Tag used to verify against the latest migration tag for this Worker.

    If they don't match, the upload is rejected.
    """

    steps: Iterable[MigrationStepParam]
    """Migrations to apply in order."""


Migrations: TypeAlias = Union[SingleStepMigrationParam, MigrationsWorkersMultipleStepMigrations]


class Module(TypedDict, total=False):
    content_base64: Required[Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]]
    """The base64-encoded module content."""

    content_type: Required[str]
    """The content type of the module."""

    name: Required[str]
    """The name of the module."""


set_pydantic_config(Module, {"arbitrary_types_allowed": True})


class Placement(TypedDict, total=False):
    """Placement settings for the version."""

    mode: Literal["smart"]
    """Placement mode for the version."""
