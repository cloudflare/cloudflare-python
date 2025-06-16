# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ......_utils import PropertyInfo
from ......_models import BaseModel
from .....workers.migration_step import MigrationStep
from .....workers.single_step_migration import SingleStepMigration
from .....workers.scripts.consumer_script import ConsumerScript

__all__ = [
    "SettingEditResponse",
    "Binding",
    "BindingWorkersBindingKindAI",
    "BindingWorkersBindingKindAnalyticsEngine",
    "BindingWorkersBindingKindAssets",
    "BindingWorkersBindingKindBrowser",
    "BindingWorkersBindingKindD1",
    "BindingWorkersBindingKindDispatchNamespace",
    "BindingWorkersBindingKindDispatchNamespaceOutbound",
    "BindingWorkersBindingKindDispatchNamespaceOutboundWorker",
    "BindingWorkersBindingKindDurableObjectNamespace",
    "BindingWorkersBindingKindHyperdrive",
    "BindingWorkersBindingKindJson",
    "BindingWorkersBindingKindKVNamespace",
    "BindingWorkersBindingKindMTLSCertificate",
    "BindingWorkersBindingKindPlainText",
    "BindingWorkersBindingKindPipelines",
    "BindingWorkersBindingKindQueue",
    "BindingWorkersBindingKindR2Bucket",
    "BindingWorkersBindingKindSecretText",
    "BindingWorkersBindingKindService",
    "BindingWorkersBindingKindTailConsumer",
    "BindingWorkersBindingKindVectorize",
    "BindingWorkersBindingKindVersionMetadata",
    "BindingWorkersBindingKindSecretsStoreSecret",
    "BindingWorkersBindingKindSecretKey",
    "BindingWorkersBindingKindWorkflow",
    "Limits",
    "Migrations",
    "MigrationsWorkersMultipleStepMigrations",
    "Observability",
    "ObservabilityLogs",
    "Placement",
]


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


class BindingWorkersBindingKindDispatchNamespaceOutboundWorker(BaseModel):
    environment: Optional[str] = None
    """Environment of the outbound worker."""

    service: Optional[str] = None
    """Name of the outbound worker."""


class BindingWorkersBindingKindDispatchNamespaceOutbound(BaseModel):
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
    """Namespace to bind to."""

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


class BindingWorkersBindingKindSecretText(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["secret_text"]
    """The kind of resource that the binding provides."""


class BindingWorkersBindingKindService(BaseModel):
    environment: str
    """Optional environment if the Worker utilizes one."""

    name: str
    """A JavaScript variable name for the binding."""

    service: str
    """Name of Worker to bind to."""

    type: Literal["service"]
    """The kind of resource that the binding provides."""


class BindingWorkersBindingKindTailConsumer(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    service: str
    """Name of Tail Worker to bind to."""

    type: Literal["tail_consumer"]
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


Binding: TypeAlias = Annotated[
    Union[
        BindingWorkersBindingKindAI,
        BindingWorkersBindingKindAnalyticsEngine,
        BindingWorkersBindingKindAssets,
        BindingWorkersBindingKindBrowser,
        BindingWorkersBindingKindD1,
        BindingWorkersBindingKindDispatchNamespace,
        BindingWorkersBindingKindDurableObjectNamespace,
        BindingWorkersBindingKindHyperdrive,
        BindingWorkersBindingKindJson,
        BindingWorkersBindingKindKVNamespace,
        BindingWorkersBindingKindMTLSCertificate,
        BindingWorkersBindingKindPlainText,
        BindingWorkersBindingKindPipelines,
        BindingWorkersBindingKindQueue,
        BindingWorkersBindingKindR2Bucket,
        BindingWorkersBindingKindSecretText,
        BindingWorkersBindingKindService,
        BindingWorkersBindingKindTailConsumer,
        BindingWorkersBindingKindVectorize,
        BindingWorkersBindingKindVersionMetadata,
        BindingWorkersBindingKindSecretsStoreSecret,
        BindingWorkersBindingKindSecretKey,
        BindingWorkersBindingKindWorkflow,
    ],
    PropertyInfo(discriminator="type"),
]


class Limits(BaseModel):
    cpu_ms: Optional[int] = None
    """The amount of CPU time this Worker can use in milliseconds."""


class MigrationsWorkersMultipleStepMigrations(BaseModel):
    new_tag: Optional[str] = None
    """Tag to set as the latest migration tag."""

    old_tag: Optional[str] = None
    """Tag used to verify against the latest migration tag for this Worker.

    If they don't match, the upload is rejected.
    """

    steps: Optional[List[MigrationStep]] = None
    """Migrations to apply in order."""


Migrations: TypeAlias = Union[SingleStepMigration, MigrationsWorkersMultipleStepMigrations]


class ObservabilityLogs(BaseModel):
    enabled: bool
    """Whether logs are enabled for the Worker."""

    invocation_logs: bool
    """
    Whether
    [invocation logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs/#invocation-logs)
    are enabled for the Worker.
    """

    head_sampling_rate: Optional[float] = None
    """The sampling rate for logs. From 0 to 1 (1 = 100%, 0.1 = 10%). Default is 1."""


class Observability(BaseModel):
    enabled: bool
    """Whether observability is enabled for the Worker."""

    head_sampling_rate: Optional[float] = None
    """The sampling rate for incoming requests.

    From 0 to 1 (1 = 100%, 0.1 = 10%). Default is 1.
    """

    logs: Optional[ObservabilityLogs] = None
    """Log settings for the Worker."""


class Placement(BaseModel):
    mode: Optional[Literal["smart"]] = None
    """
    Enables
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    """


class SettingEditResponse(BaseModel):
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
    """Limits to apply for this Worker."""

    logpush: Optional[bool] = None
    """Whether Logpush is turned on for the Worker."""

    migrations: Optional[Migrations] = None
    """Migrations to apply for Durable Objects associated with this Worker."""

    observability: Optional[Observability] = None
    """Observability settings for the Worker."""

    placement: Optional[Placement] = None
    """
    Configuration for
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    """

    tags: Optional[List[str]] = None
    """Tags to help you manage your Workers."""

    tail_consumers: Optional[List[ConsumerScript]] = None
    """List of Workers that will consume logs from the attached Worker."""

    usage_model: Optional[Literal["standard"]] = None
    """Usage model for the Worker invocations."""
