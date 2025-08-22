# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import FileTypes
from .migration_step_param import MigrationStepParam
from .single_step_migration_param import SingleStepMigrationParam
from .scripts.consumer_script_param import ConsumerScriptParam

__all__ = [
    "ScriptUpdateParams",
    "Metadata",
    "MetadataUnionMember0",
    "MetadataUnionMember0Assets",
    "MetadataUnionMember0AssetsConfig",
    "MetadataUnionMember0Binding",
    "MetadataUnionMember0BindingWorkersBindingKindAI",
    "MetadataUnionMember0BindingWorkersBindingKindAnalyticsEngine",
    "MetadataUnionMember0BindingWorkersBindingKindAssets",
    "MetadataUnionMember0BindingWorkersBindingKindBrowser",
    "MetadataUnionMember0BindingWorkersBindingKindD1",
    "MetadataUnionMember0BindingWorkersBindingKindDispatchNamespace",
    "MetadataUnionMember0BindingWorkersBindingKindDispatchNamespaceOutbound",
    "MetadataUnionMember0BindingWorkersBindingKindDispatchNamespaceOutboundWorker",
    "MetadataUnionMember0BindingWorkersBindingKindDurableObjectNamespace",
    "MetadataUnionMember0BindingWorkersBindingKindHyperdrive",
    "MetadataUnionMember0BindingWorkersBindingKindJson",
    "MetadataUnionMember0BindingWorkersBindingKindKVNamespace",
    "MetadataUnionMember0BindingWorkersBindingKindMTLSCertificate",
    "MetadataUnionMember0BindingWorkersBindingKindPlainText",
    "MetadataUnionMember0BindingWorkersBindingKindPipelines",
    "MetadataUnionMember0BindingWorkersBindingKindQueue",
    "MetadataUnionMember0BindingWorkersBindingKindR2Bucket",
    "MetadataUnionMember0BindingWorkersBindingKindSecretText",
    "MetadataUnionMember0BindingWorkersBindingKindService",
    "MetadataUnionMember0BindingWorkersBindingKindTailConsumer",
    "MetadataUnionMember0BindingWorkersBindingKindVectorize",
    "MetadataUnionMember0BindingWorkersBindingKindVersionMetadata",
    "MetadataUnionMember0BindingWorkersBindingKindSecretsStoreSecret",
    "MetadataUnionMember0BindingWorkersBindingKindSecretKey",
    "MetadataUnionMember0BindingWorkersBindingKindWorkflow",
    "MetadataUnionMember0Migrations",
    "MetadataUnionMember0MigrationsWorkersMultipleStepMigrations",
    "MetadataUnionMember0Observability",
    "MetadataUnionMember0ObservabilityLogs",
    "MetadataUnionMember0Placement",
    "MetadataUnionMember1",
    "MetadataUnionMember1Assets",
    "MetadataUnionMember1AssetsConfig",
    "MetadataUnionMember1Binding",
    "MetadataUnionMember1BindingWorkersBindingKindAI",
    "MetadataUnionMember1BindingWorkersBindingKindAnalyticsEngine",
    "MetadataUnionMember1BindingWorkersBindingKindAssets",
    "MetadataUnionMember1BindingWorkersBindingKindBrowser",
    "MetadataUnionMember1BindingWorkersBindingKindD1",
    "MetadataUnionMember1BindingWorkersBindingKindDispatchNamespace",
    "MetadataUnionMember1BindingWorkersBindingKindDispatchNamespaceOutbound",
    "MetadataUnionMember1BindingWorkersBindingKindDispatchNamespaceOutboundWorker",
    "MetadataUnionMember1BindingWorkersBindingKindDurableObjectNamespace",
    "MetadataUnionMember1BindingWorkersBindingKindHyperdrive",
    "MetadataUnionMember1BindingWorkersBindingKindJson",
    "MetadataUnionMember1BindingWorkersBindingKindKVNamespace",
    "MetadataUnionMember1BindingWorkersBindingKindMTLSCertificate",
    "MetadataUnionMember1BindingWorkersBindingKindPlainText",
    "MetadataUnionMember1BindingWorkersBindingKindPipelines",
    "MetadataUnionMember1BindingWorkersBindingKindQueue",
    "MetadataUnionMember1BindingWorkersBindingKindR2Bucket",
    "MetadataUnionMember1BindingWorkersBindingKindSecretText",
    "MetadataUnionMember1BindingWorkersBindingKindService",
    "MetadataUnionMember1BindingWorkersBindingKindTailConsumer",
    "MetadataUnionMember1BindingWorkersBindingKindVectorize",
    "MetadataUnionMember1BindingWorkersBindingKindVersionMetadata",
    "MetadataUnionMember1BindingWorkersBindingKindSecretsStoreSecret",
    "MetadataUnionMember1BindingWorkersBindingKindSecretKey",
    "MetadataUnionMember1BindingWorkersBindingKindWorkflow",
    "MetadataUnionMember1Migrations",
    "MetadataUnionMember1MigrationsWorkersMultipleStepMigrations",
    "MetadataUnionMember1Observability",
    "MetadataUnionMember1ObservabilityLogs",
    "MetadataUnionMember1Placement",
]


class ScriptUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    metadata: Required[Metadata]
    """JSON-encoded metadata about the uploaded parts and Worker configuration."""

    files: List[FileTypes]
    """An array of modules (often JavaScript files) comprising a Worker script.

    At least one module must be present and referenced in the metadata as
    `main_module` or `body_part` by filename.<br/>Possible Content-Type(s) are:
    `application/javascript+module`, `text/javascript+module`,
    `application/javascript`, `text/javascript`, `text/x-python`,
    `text/x-python-requirement`, `application/wasm`, `text/plain`,
    `application/octet-stream`, `application/source-map`.
    """


class MetadataUnionMember0AssetsConfig(TypedDict, total=False):
    _headers: str
    """
    The contents of a \\__headers file (used to attach custom headers on asset
    responses).
    """

    _redirects: str
    """
    The contents of a \\__redirects file (used to apply redirects or proxy paths ahead
    of asset serving).
    """

    html_handling: Literal["auto-trailing-slash", "force-trailing-slash", "drop-trailing-slash", "none"]
    """Determines the redirects and rewrites of requests for HTML content."""

    not_found_handling: Literal["none", "404-page", "single-page-application"]
    """
    Determines the response when a request does not match a static asset, and there
    is no Worker script.
    """

    run_worker_first: Union[List[str], bool]
    """Contains a list path rules to control routing to either the Worker or assets.

    Glob (\\**) and negative (!) rules are supported. Rules must start with either '/'
    or '!/'. At least one non-negative rule must be provided, and negative rules
    have higher precedence than non-negative rules.
    """

    serve_directly: bool
    """
    When true and the incoming request matches an asset, that will be served instead
    of invoking the Worker script. When false, requests will always invoke the
    Worker script.
    """


class MetadataUnionMember0Assets(TypedDict, total=False):
    config: MetadataUnionMember0AssetsConfig
    """Configuration for assets within a Worker."""

    jwt: str
    """Token provided upon successful upload of all files from a registered manifest."""


class MetadataUnionMember0BindingWorkersBindingKindAI(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["ai"]]
    """The kind of resource that the binding provides."""


class MetadataUnionMember0BindingWorkersBindingKindAnalyticsEngine(TypedDict, total=False):
    dataset: Required[str]
    """The name of the dataset to bind to."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["analytics_engine"]]
    """The kind of resource that the binding provides."""


class MetadataUnionMember0BindingWorkersBindingKindAssets(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["assets"]]
    """The kind of resource that the binding provides."""


class MetadataUnionMember0BindingWorkersBindingKindBrowser(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["browser"]]
    """The kind of resource that the binding provides."""


class MetadataUnionMember0BindingWorkersBindingKindD1(TypedDict, total=False):
    id: Required[str]
    """Identifier of the D1 database to bind to."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["d1"]]
    """The kind of resource that the binding provides."""


class MetadataUnionMember0BindingWorkersBindingKindDispatchNamespaceOutboundWorker(TypedDict, total=False):
    environment: str
    """Environment of the outbound worker."""

    service: str
    """Name of the outbound worker."""


class MetadataUnionMember0BindingWorkersBindingKindDispatchNamespaceOutbound(TypedDict, total=False):
    params: List[str]
    """
    Pass information from the Dispatch Worker to the Outbound Worker through the
    parameters.
    """

    worker: MetadataUnionMember0BindingWorkersBindingKindDispatchNamespaceOutboundWorker
    """Outbound worker."""


class MetadataUnionMember0BindingWorkersBindingKindDispatchNamespace(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    namespace: Required[str]
    """Namespace to bind to."""

    type: Required[Literal["dispatch_namespace"]]
    """The kind of resource that the binding provides."""

    outbound: MetadataUnionMember0BindingWorkersBindingKindDispatchNamespaceOutbound
    """Outbound worker."""


class MetadataUnionMember0BindingWorkersBindingKindDurableObjectNamespace(TypedDict, total=False):
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


class MetadataUnionMember0BindingWorkersBindingKindHyperdrive(TypedDict, total=False):
    id: Required[str]
    """Identifier of the Hyperdrive connection to bind to."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["hyperdrive"]]
    """The kind of resource that the binding provides."""


class MetadataUnionMember0BindingWorkersBindingKindJson(TypedDict, total=False):
    json: Required[str]
    """JSON data to use."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["json"]]
    """The kind of resource that the binding provides."""


class MetadataUnionMember0BindingWorkersBindingKindKVNamespace(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    namespace_id: Required[str]
    """Namespace identifier tag."""

    type: Required[Literal["kv_namespace"]]
    """The kind of resource that the binding provides."""


class MetadataUnionMember0BindingWorkersBindingKindMTLSCertificate(TypedDict, total=False):
    certificate_id: Required[str]
    """Identifier of the certificate to bind to."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["mtls_certificate"]]
    """The kind of resource that the binding provides."""


class MetadataUnionMember0BindingWorkersBindingKindPlainText(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    text: Required[str]
    """The text value to use."""

    type: Required[Literal["plain_text"]]
    """The kind of resource that the binding provides."""


class MetadataUnionMember0BindingWorkersBindingKindPipelines(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    pipeline: Required[str]
    """Name of the Pipeline to bind to."""

    type: Required[Literal["pipelines"]]
    """The kind of resource that the binding provides."""


class MetadataUnionMember0BindingWorkersBindingKindQueue(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    queue_name: Required[str]
    """Name of the Queue to bind to."""

    type: Required[Literal["queue"]]
    """The kind of resource that the binding provides."""


class MetadataUnionMember0BindingWorkersBindingKindR2Bucket(TypedDict, total=False):
    bucket_name: Required[str]
    """R2 bucket to bind to."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["r2_bucket"]]
    """The kind of resource that the binding provides."""


class MetadataUnionMember0BindingWorkersBindingKindSecretText(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    text: Required[str]
    """The secret value to use."""

    type: Required[Literal["secret_text"]]
    """The kind of resource that the binding provides."""


class MetadataUnionMember0BindingWorkersBindingKindService(TypedDict, total=False):
    environment: Required[str]
    """Optional environment if the Worker utilizes one."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    service: Required[str]
    """Name of Worker to bind to."""

    type: Required[Literal["service"]]
    """The kind of resource that the binding provides."""


class MetadataUnionMember0BindingWorkersBindingKindTailConsumer(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    service: Required[str]
    """Name of Tail Worker to bind to."""

    type: Required[Literal["tail_consumer"]]
    """The kind of resource that the binding provides."""


class MetadataUnionMember0BindingWorkersBindingKindVectorize(TypedDict, total=False):
    index_name: Required[str]
    """Name of the Vectorize index to bind to."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["vectorize"]]
    """The kind of resource that the binding provides."""


class MetadataUnionMember0BindingWorkersBindingKindVersionMetadata(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["version_metadata"]]
    """The kind of resource that the binding provides."""


class MetadataUnionMember0BindingWorkersBindingKindSecretsStoreSecret(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    secret_name: Required[str]
    """Name of the secret in the store."""

    store_id: Required[str]
    """ID of the store containing the secret."""

    type: Required[Literal["secrets_store_secret"]]
    """The kind of resource that the binding provides."""


class MetadataUnionMember0BindingWorkersBindingKindSecretKey(TypedDict, total=False):
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


class MetadataUnionMember0BindingWorkersBindingKindWorkflow(TypedDict, total=False):
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


MetadataUnionMember0Binding: TypeAlias = Union[
    MetadataUnionMember0BindingWorkersBindingKindAI,
    MetadataUnionMember0BindingWorkersBindingKindAnalyticsEngine,
    MetadataUnionMember0BindingWorkersBindingKindAssets,
    MetadataUnionMember0BindingWorkersBindingKindBrowser,
    MetadataUnionMember0BindingWorkersBindingKindD1,
    MetadataUnionMember0BindingWorkersBindingKindDispatchNamespace,
    MetadataUnionMember0BindingWorkersBindingKindDurableObjectNamespace,
    MetadataUnionMember0BindingWorkersBindingKindHyperdrive,
    MetadataUnionMember0BindingWorkersBindingKindJson,
    MetadataUnionMember0BindingWorkersBindingKindKVNamespace,
    MetadataUnionMember0BindingWorkersBindingKindMTLSCertificate,
    MetadataUnionMember0BindingWorkersBindingKindPlainText,
    MetadataUnionMember0BindingWorkersBindingKindPipelines,
    MetadataUnionMember0BindingWorkersBindingKindQueue,
    MetadataUnionMember0BindingWorkersBindingKindR2Bucket,
    MetadataUnionMember0BindingWorkersBindingKindSecretText,
    MetadataUnionMember0BindingWorkersBindingKindService,
    MetadataUnionMember0BindingWorkersBindingKindTailConsumer,
    MetadataUnionMember0BindingWorkersBindingKindVectorize,
    MetadataUnionMember0BindingWorkersBindingKindVersionMetadata,
    MetadataUnionMember0BindingWorkersBindingKindSecretsStoreSecret,
    MetadataUnionMember0BindingWorkersBindingKindSecretKey,
    MetadataUnionMember0BindingWorkersBindingKindWorkflow,
]


class MetadataUnionMember0MigrationsWorkersMultipleStepMigrations(TypedDict, total=False):
    new_tag: str
    """Tag to set as the latest migration tag."""

    old_tag: str
    """Tag used to verify against the latest migration tag for this Worker.

    If they don't match, the upload is rejected.
    """

    steps: Iterable[MigrationStepParam]
    """Migrations to apply in order."""


MetadataUnionMember0Migrations: TypeAlias = Union[
    SingleStepMigrationParam, MetadataUnionMember0MigrationsWorkersMultipleStepMigrations
]


class MetadataUnionMember0ObservabilityLogs(TypedDict, total=False):
    enabled: Required[bool]
    """Whether logs are enabled for the Worker."""

    invocation_logs: Required[bool]
    """
    Whether
    [invocation logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs/#invocation-logs)
    are enabled for the Worker.
    """

    head_sampling_rate: Optional[float]
    """The sampling rate for logs. From 0 to 1 (1 = 100%, 0.1 = 10%). Default is 1."""


class MetadataUnionMember0Observability(TypedDict, total=False):
    enabled: Required[bool]
    """Whether observability is enabled for the Worker."""

    head_sampling_rate: Optional[float]
    """The sampling rate for incoming requests.

    From 0 to 1 (1 = 100%, 0.1 = 10%). Default is 1.
    """

    logs: Optional[MetadataUnionMember0ObservabilityLogs]
    """Log settings for the Worker."""


class MetadataUnionMember0Placement(TypedDict, total=False):
    mode: Literal["smart"]
    """
    Enables
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    """


class MetadataUnionMember0(TypedDict, total=False):
    main_module: Required[str]
    """Name of the uploaded file that contains the main module (e.g.

    the file exporting a `fetch` handler). Indicates a `module syntax` Worker.
    """

    assets: MetadataUnionMember0Assets
    """Configuration for assets within a Worker."""

    bindings: Iterable[MetadataUnionMember0Binding]
    """List of bindings attached to a Worker.

    You can find more about bindings on our docs:
    https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/#bindings.
    """

    compatibility_date: str
    """Date indicating targeted support in the Workers runtime.

    Backwards incompatible fixes to the runtime following this date will not affect
    this Worker.
    """

    compatibility_flags: List[str]
    """Flags that enable or disable certain features in the Workers runtime.

    Used to enable upcoming features or opt in or out of specific changes not
    included in a `compatibility_date`.
    """

    keep_assets: bool
    """
    Retain assets which exist for a previously uploaded Worker version; used in lieu
    of providing a completion token.
    """

    keep_bindings: List[str]
    """List of binding types to keep from previous_upload."""

    logpush: bool
    """Whether Logpush is turned on for the Worker."""

    migrations: MetadataUnionMember0Migrations
    """Migrations to apply for Durable Objects associated with this Worker."""

    observability: MetadataUnionMember0Observability
    """Observability settings for the Worker."""

    placement: MetadataUnionMember0Placement
    """
    Configuration for
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    """

    tags: List[str]
    """List of strings to use as tags for this Worker."""

    tail_consumers: Iterable[ConsumerScriptParam]
    """List of Workers that will consume logs from the attached Worker."""

    usage_model: Literal["standard", "bundled", "unbound"]
    """Usage model for the Worker invocations."""


class MetadataUnionMember1AssetsConfig(TypedDict, total=False):
    _headers: str
    """
    The contents of a \\__headers file (used to attach custom headers on asset
    responses).
    """

    _redirects: str
    """
    The contents of a \\__redirects file (used to apply redirects or proxy paths ahead
    of asset serving).
    """

    html_handling: Literal["auto-trailing-slash", "force-trailing-slash", "drop-trailing-slash", "none"]
    """Determines the redirects and rewrites of requests for HTML content."""

    not_found_handling: Literal["none", "404-page", "single-page-application"]
    """
    Determines the response when a request does not match a static asset, and there
    is no Worker script.
    """

    run_worker_first: Union[List[str], bool]
    """Contains a list path rules to control routing to either the Worker or assets.

    Glob (\\**) and negative (!) rules are supported. Rules must start with either '/'
    or '!/'. At least one non-negative rule must be provided, and negative rules
    have higher precedence than non-negative rules.
    """

    serve_directly: bool
    """
    When true and the incoming request matches an asset, that will be served instead
    of invoking the Worker script. When false, requests will always invoke the
    Worker script.
    """


class MetadataUnionMember1Assets(TypedDict, total=False):
    config: MetadataUnionMember1AssetsConfig
    """Configuration for assets within a Worker."""

    jwt: str
    """Token provided upon successful upload of all files from a registered manifest."""


class MetadataUnionMember1BindingWorkersBindingKindAI(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["ai"]]
    """The kind of resource that the binding provides."""


class MetadataUnionMember1BindingWorkersBindingKindAnalyticsEngine(TypedDict, total=False):
    dataset: Required[str]
    """The name of the dataset to bind to."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["analytics_engine"]]
    """The kind of resource that the binding provides."""


class MetadataUnionMember1BindingWorkersBindingKindAssets(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["assets"]]
    """The kind of resource that the binding provides."""


class MetadataUnionMember1BindingWorkersBindingKindBrowser(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["browser"]]
    """The kind of resource that the binding provides."""


class MetadataUnionMember1BindingWorkersBindingKindD1(TypedDict, total=False):
    id: Required[str]
    """Identifier of the D1 database to bind to."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["d1"]]
    """The kind of resource that the binding provides."""


class MetadataUnionMember1BindingWorkersBindingKindDispatchNamespaceOutboundWorker(TypedDict, total=False):
    environment: str
    """Environment of the outbound worker."""

    service: str
    """Name of the outbound worker."""


class MetadataUnionMember1BindingWorkersBindingKindDispatchNamespaceOutbound(TypedDict, total=False):
    params: List[str]
    """
    Pass information from the Dispatch Worker to the Outbound Worker through the
    parameters.
    """

    worker: MetadataUnionMember1BindingWorkersBindingKindDispatchNamespaceOutboundWorker
    """Outbound worker."""


class MetadataUnionMember1BindingWorkersBindingKindDispatchNamespace(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    namespace: Required[str]
    """Namespace to bind to."""

    type: Required[Literal["dispatch_namespace"]]
    """The kind of resource that the binding provides."""

    outbound: MetadataUnionMember1BindingWorkersBindingKindDispatchNamespaceOutbound
    """Outbound worker."""


class MetadataUnionMember1BindingWorkersBindingKindDurableObjectNamespace(TypedDict, total=False):
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


class MetadataUnionMember1BindingWorkersBindingKindHyperdrive(TypedDict, total=False):
    id: Required[str]
    """Identifier of the Hyperdrive connection to bind to."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["hyperdrive"]]
    """The kind of resource that the binding provides."""


class MetadataUnionMember1BindingWorkersBindingKindJson(TypedDict, total=False):
    json: Required[str]
    """JSON data to use."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["json"]]
    """The kind of resource that the binding provides."""


class MetadataUnionMember1BindingWorkersBindingKindKVNamespace(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    namespace_id: Required[str]
    """Namespace identifier tag."""

    type: Required[Literal["kv_namespace"]]
    """The kind of resource that the binding provides."""


class MetadataUnionMember1BindingWorkersBindingKindMTLSCertificate(TypedDict, total=False):
    certificate_id: Required[str]
    """Identifier of the certificate to bind to."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["mtls_certificate"]]
    """The kind of resource that the binding provides."""


class MetadataUnionMember1BindingWorkersBindingKindPlainText(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    text: Required[str]
    """The text value to use."""

    type: Required[Literal["plain_text"]]
    """The kind of resource that the binding provides."""


class MetadataUnionMember1BindingWorkersBindingKindPipelines(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    pipeline: Required[str]
    """Name of the Pipeline to bind to."""

    type: Required[Literal["pipelines"]]
    """The kind of resource that the binding provides."""


class MetadataUnionMember1BindingWorkersBindingKindQueue(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    queue_name: Required[str]
    """Name of the Queue to bind to."""

    type: Required[Literal["queue"]]
    """The kind of resource that the binding provides."""


class MetadataUnionMember1BindingWorkersBindingKindR2Bucket(TypedDict, total=False):
    bucket_name: Required[str]
    """R2 bucket to bind to."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["r2_bucket"]]
    """The kind of resource that the binding provides."""


class MetadataUnionMember1BindingWorkersBindingKindSecretText(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    text: Required[str]
    """The secret value to use."""

    type: Required[Literal["secret_text"]]
    """The kind of resource that the binding provides."""


class MetadataUnionMember1BindingWorkersBindingKindService(TypedDict, total=False):
    environment: Required[str]
    """Optional environment if the Worker utilizes one."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    service: Required[str]
    """Name of Worker to bind to."""

    type: Required[Literal["service"]]
    """The kind of resource that the binding provides."""


class MetadataUnionMember1BindingWorkersBindingKindTailConsumer(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    service: Required[str]
    """Name of Tail Worker to bind to."""

    type: Required[Literal["tail_consumer"]]
    """The kind of resource that the binding provides."""


class MetadataUnionMember1BindingWorkersBindingKindVectorize(TypedDict, total=False):
    index_name: Required[str]
    """Name of the Vectorize index to bind to."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["vectorize"]]
    """The kind of resource that the binding provides."""


class MetadataUnionMember1BindingWorkersBindingKindVersionMetadata(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[Literal["version_metadata"]]
    """The kind of resource that the binding provides."""


class MetadataUnionMember1BindingWorkersBindingKindSecretsStoreSecret(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    secret_name: Required[str]
    """Name of the secret in the store."""

    store_id: Required[str]
    """ID of the store containing the secret."""

    type: Required[Literal["secrets_store_secret"]]
    """The kind of resource that the binding provides."""


class MetadataUnionMember1BindingWorkersBindingKindSecretKey(TypedDict, total=False):
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


class MetadataUnionMember1BindingWorkersBindingKindWorkflow(TypedDict, total=False):
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


MetadataUnionMember1Binding: TypeAlias = Union[
    MetadataUnionMember1BindingWorkersBindingKindAI,
    MetadataUnionMember1BindingWorkersBindingKindAnalyticsEngine,
    MetadataUnionMember1BindingWorkersBindingKindAssets,
    MetadataUnionMember1BindingWorkersBindingKindBrowser,
    MetadataUnionMember1BindingWorkersBindingKindD1,
    MetadataUnionMember1BindingWorkersBindingKindDispatchNamespace,
    MetadataUnionMember1BindingWorkersBindingKindDurableObjectNamespace,
    MetadataUnionMember1BindingWorkersBindingKindHyperdrive,
    MetadataUnionMember1BindingWorkersBindingKindJson,
    MetadataUnionMember1BindingWorkersBindingKindKVNamespace,
    MetadataUnionMember1BindingWorkersBindingKindMTLSCertificate,
    MetadataUnionMember1BindingWorkersBindingKindPlainText,
    MetadataUnionMember1BindingWorkersBindingKindPipelines,
    MetadataUnionMember1BindingWorkersBindingKindQueue,
    MetadataUnionMember1BindingWorkersBindingKindR2Bucket,
    MetadataUnionMember1BindingWorkersBindingKindSecretText,
    MetadataUnionMember1BindingWorkersBindingKindService,
    MetadataUnionMember1BindingWorkersBindingKindTailConsumer,
    MetadataUnionMember1BindingWorkersBindingKindVectorize,
    MetadataUnionMember1BindingWorkersBindingKindVersionMetadata,
    MetadataUnionMember1BindingWorkersBindingKindSecretsStoreSecret,
    MetadataUnionMember1BindingWorkersBindingKindSecretKey,
    MetadataUnionMember1BindingWorkersBindingKindWorkflow,
]


class MetadataUnionMember1MigrationsWorkersMultipleStepMigrations(TypedDict, total=False):
    new_tag: str
    """Tag to set as the latest migration tag."""

    old_tag: str
    """Tag used to verify against the latest migration tag for this Worker.

    If they don't match, the upload is rejected.
    """

    steps: Iterable[MigrationStepParam]
    """Migrations to apply in order."""


MetadataUnionMember1Migrations: TypeAlias = Union[
    SingleStepMigrationParam, MetadataUnionMember1MigrationsWorkersMultipleStepMigrations
]


class MetadataUnionMember1ObservabilityLogs(TypedDict, total=False):
    enabled: Required[bool]
    """Whether logs are enabled for the Worker."""

    invocation_logs: Required[bool]
    """
    Whether
    [invocation logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs/#invocation-logs)
    are enabled for the Worker.
    """

    head_sampling_rate: Optional[float]
    """The sampling rate for logs. From 0 to 1 (1 = 100%, 0.1 = 10%). Default is 1."""


class MetadataUnionMember1Observability(TypedDict, total=False):
    enabled: Required[bool]
    """Whether observability is enabled for the Worker."""

    head_sampling_rate: Optional[float]
    """The sampling rate for incoming requests.

    From 0 to 1 (1 = 100%, 0.1 = 10%). Default is 1.
    """

    logs: Optional[MetadataUnionMember1ObservabilityLogs]
    """Log settings for the Worker."""


class MetadataUnionMember1Placement(TypedDict, total=False):
    mode: Literal["smart"]
    """
    Enables
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    """


class MetadataUnionMember1(TypedDict, total=False):
    body_part: Required[str]
    """Name of the uploaded file that contains the Worker script (e.g.

    the file adding a listener to the `fetch` event). Indicates a
    `service worker syntax` Worker.
    """

    assets: MetadataUnionMember1Assets
    """Configuration for assets within a Worker."""

    bindings: Iterable[MetadataUnionMember1Binding]
    """List of bindings attached to a Worker.

    You can find more about bindings on our docs:
    https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/#bindings.
    """

    compatibility_date: str
    """Date indicating targeted support in the Workers runtime.

    Backwards incompatible fixes to the runtime following this date will not affect
    this Worker.
    """

    compatibility_flags: List[str]
    """Flags that enable or disable certain features in the Workers runtime.

    Used to enable upcoming features or opt in or out of specific changes not
    included in a `compatibility_date`.
    """

    keep_assets: bool
    """
    Retain assets which exist for a previously uploaded Worker version; used in lieu
    of providing a completion token.
    """

    keep_bindings: List[str]
    """List of binding types to keep from previous_upload."""

    logpush: bool
    """Whether Logpush is turned on for the Worker."""

    migrations: MetadataUnionMember1Migrations
    """Migrations to apply for Durable Objects associated with this Worker."""

    observability: MetadataUnionMember1Observability
    """Observability settings for the Worker."""

    placement: MetadataUnionMember1Placement
    """
    Configuration for
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    """

    tags: List[str]
    """List of strings to use as tags for this Worker."""

    tail_consumers: Iterable[ConsumerScriptParam]
    """List of Workers that will consume logs from the attached Worker."""

    usage_model: Literal["standard", "bundled", "unbound"]
    """Usage model for the Worker invocations."""


Metadata: TypeAlias = Union[MetadataUnionMember0, MetadataUnionMember1]
