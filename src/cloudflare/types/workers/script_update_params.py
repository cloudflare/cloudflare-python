# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .migration_step_param import MigrationStepParam
from .single_step_migration_param import SingleStepMigrationParam
from .scripts.consumer_script_param import ConsumerScriptParam

__all__ = [
    "ScriptUpdateParams",
    "Metadata",
    "MetadataAssets",
    "MetadataAssetsConfig",
    "MetadataBinding",
    "MetadataBindingWorkersBindingKindAI",
    "MetadataBindingWorkersBindingKindAnalyticsEngine",
    "MetadataBindingWorkersBindingKindAssets",
    "MetadataBindingWorkersBindingKindBrowser",
    "MetadataBindingWorkersBindingKindD1",
    "MetadataBindingWorkersBindingKindDispatchNamespace",
    "MetadataBindingWorkersBindingKindDispatchNamespaceOutbound",
    "MetadataBindingWorkersBindingKindDispatchNamespaceOutboundWorker",
    "MetadataBindingWorkersBindingKindDurableObjectNamespace",
    "MetadataBindingWorkersBindingKindHyperdrive",
    "MetadataBindingWorkersBindingKindJson",
    "MetadataBindingWorkersBindingKindKVNamespace",
    "MetadataBindingWorkersBindingKindMTLSCertificate",
    "MetadataBindingWorkersBindingKindPlainText",
    "MetadataBindingWorkersBindingKindPipelines",
    "MetadataBindingWorkersBindingKindQueue",
    "MetadataBindingWorkersBindingKindR2Bucket",
    "MetadataBindingWorkersBindingKindSecretText",
    "MetadataBindingWorkersBindingKindService",
    "MetadataBindingWorkersBindingKindTailConsumer",
    "MetadataBindingWorkersBindingKindVectorize",
    "MetadataBindingWorkersBindingKindVersionMetadata",
    "MetadataBindingWorkersBindingKindSecretsStoreSecret",
    "MetadataBindingWorkersBindingKindSecretKey",
    "MetadataBindingWorkersBindingKindWorkflow",
    "MetadataMigrations",
    "MetadataMigrationsWorkersMultipleStepMigrations",
    "MetadataObservability",
    "MetadataObservabilityLogs",
    "MetadataPlacement",
]


class ScriptUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    metadata: Required[Metadata]
    """JSON encoded metadata about the uploaded parts and Worker configuration."""


class MetadataAssetsConfig(TypedDict, total=False):
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

    run_worker_first: List[str]
    """Contains a list path rules to control routing to either the Worker or assets.

    Glob (\\**) and negative (!) rules are supported. Rules must start with either '/'
    or '!/'. At least one non-negative rule must be provided, and negative rules
    have higher precedence than non-negative rules.
    """


class MetadataAssets(TypedDict, total=False):
    config: MetadataAssetsConfig
    """Configuration for assets within a Worker."""

    jwt: str
    """Token provided upon successful upload of all files from a registered manifest."""


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


class MetadataBindingWorkersBindingKindDispatchNamespaceOutboundWorker(TypedDict, total=False):
    environment: str
    """Environment of the outbound worker."""

    service: str
    """Name of the outbound worker."""


class MetadataBindingWorkersBindingKindDispatchNamespaceOutbound(TypedDict, total=False):
    params: List[str]
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


class MetadataBindingWorkersBindingKindService(TypedDict, total=False):
    environment: Required[str]
    """Optional environment if the Worker utilizes one."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    service: Required[str]
    """Name of Worker to bind to."""

    type: Required[Literal["service"]]
    """The kind of resource that the binding provides."""


class MetadataBindingWorkersBindingKindTailConsumer(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    service: Required[str]
    """Name of Tail Worker to bind to."""

    type: Required[Literal["tail_consumer"]]
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


MetadataBinding: TypeAlias = Union[
    MetadataBindingWorkersBindingKindAI,
    MetadataBindingWorkersBindingKindAnalyticsEngine,
    MetadataBindingWorkersBindingKindAssets,
    MetadataBindingWorkersBindingKindBrowser,
    MetadataBindingWorkersBindingKindD1,
    MetadataBindingWorkersBindingKindDispatchNamespace,
    MetadataBindingWorkersBindingKindDurableObjectNamespace,
    MetadataBindingWorkersBindingKindHyperdrive,
    MetadataBindingWorkersBindingKindJson,
    MetadataBindingWorkersBindingKindKVNamespace,
    MetadataBindingWorkersBindingKindMTLSCertificate,
    MetadataBindingWorkersBindingKindPlainText,
    MetadataBindingWorkersBindingKindPipelines,
    MetadataBindingWorkersBindingKindQueue,
    MetadataBindingWorkersBindingKindR2Bucket,
    MetadataBindingWorkersBindingKindSecretText,
    MetadataBindingWorkersBindingKindService,
    MetadataBindingWorkersBindingKindTailConsumer,
    MetadataBindingWorkersBindingKindVectorize,
    MetadataBindingWorkersBindingKindVersionMetadata,
    MetadataBindingWorkersBindingKindSecretsStoreSecret,
    MetadataBindingWorkersBindingKindSecretKey,
    MetadataBindingWorkersBindingKindWorkflow,
]


class MetadataMigrationsWorkersMultipleStepMigrations(TypedDict, total=False):
    new_tag: str
    """Tag to set as the latest migration tag."""

    old_tag: str
    """Tag used to verify against the latest migration tag for this Worker.

    If they don't match, the upload is rejected.
    """

    steps: Iterable[MigrationStepParam]
    """Migrations to apply in order."""


MetadataMigrations: TypeAlias = Union[SingleStepMigrationParam, MetadataMigrationsWorkersMultipleStepMigrations]


class MetadataObservabilityLogs(TypedDict, total=False):
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


class MetadataObservability(TypedDict, total=False):
    enabled: Required[bool]
    """Whether observability is enabled for the Worker."""

    head_sampling_rate: Optional[float]
    """The sampling rate for incoming requests.

    From 0 to 1 (1 = 100%, 0.1 = 10%). Default is 1.
    """

    logs: Optional[MetadataObservabilityLogs]
    """Log settings for the Worker."""


class MetadataPlacement(TypedDict, total=False):
    mode: Literal["smart"]
    """
    Enables
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    """


class Metadata(TypedDict, total=False):
    assets: MetadataAssets
    """Configuration for assets within a Worker."""

    bindings: Iterable[MetadataBinding]
    """List of bindings attached to a Worker.

    You can find more about bindings on our docs:
    https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/#bindings.
    """

    body_part: str
    """Name of the part in the multipart request that contains the script (e.g.

    the file adding a listener to the `fetch` event). Indicates a
    `service worker syntax` Worker.
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

    main_module: str
    """Name of the part in the multipart request that contains the main module (e.g.

    the file exporting a `fetch` handler). Indicates a `module syntax` Worker.
    """

    migrations: MetadataMigrations
    """Migrations to apply for Durable Objects associated with this Worker."""

    observability: MetadataObservability
    """Observability settings for the Worker."""

    placement: MetadataPlacement
    """
    Configuration for
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    """

    tags: List[str]
    """List of strings to use as tags for this Worker."""

    tail_consumers: Iterable[ConsumerScriptParam]
    """List of Workers that will consume logs from the attached Worker."""

    usage_model: Literal["standard"]
    """Usage model for the Worker invocations."""
