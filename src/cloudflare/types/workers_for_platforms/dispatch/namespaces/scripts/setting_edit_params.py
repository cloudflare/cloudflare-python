# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .....workers.migration_step_param import MigrationStepParam
from .....workers.single_step_migration_param import SingleStepMigrationParam
from .....workers.scripts.consumer_script_param import ConsumerScriptParam

__all__ = [
    "SettingEditParams",
    "Settings",
    "SettingsBinding",
    "SettingsBindingWorkersBindingKindAI",
    "SettingsBindingWorkersBindingKindAnalyticsEngine",
    "SettingsBindingWorkersBindingKindAssets",
    "SettingsBindingWorkersBindingKindBrowserRendering",
    "SettingsBindingWorkersBindingKindD1",
    "SettingsBindingWorkersBindingKindDispatchNamespace",
    "SettingsBindingWorkersBindingKindDispatchNamespaceOutbound",
    "SettingsBindingWorkersBindingKindDispatchNamespaceOutboundWorker",
    "SettingsBindingWorkersBindingKindDurableObjectNamespace",
    "SettingsBindingWorkersBindingKindHyperdrive",
    "SettingsBindingWorkersBindingKindJson",
    "SettingsBindingWorkersBindingKindKVNamespace",
    "SettingsBindingWorkersBindingKindMTLSCertificate",
    "SettingsBindingWorkersBindingKindPlainText",
    "SettingsBindingWorkersBindingKindQueue",
    "SettingsBindingWorkersBindingKindR2Bucket",
    "SettingsBindingWorkersBindingKindSecretText",
    "SettingsBindingWorkersBindingKindService",
    "SettingsBindingWorkersBindingKindTailConsumer",
    "SettingsBindingWorkersBindingKindVectorize",
    "SettingsBindingWorkersBindingKindVersionMetadata",
    "SettingsLimits",
    "SettingsMigrations",
    "SettingsMigrationsWorkersMultipleStepMigrations",
    "SettingsObservability",
    "SettingsPlacement",
]


class SettingEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    dispatch_namespace: Required[str]
    """Name of the Workers for Platforms dispatch namespace."""

    settings: Settings


class SettingsBindingWorkersBindingKindAI(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[
        Literal[
            "ai",
            "analytics_engine",
            "assets",
            "browser_rendering",
            "d1",
            "dispatch_namespace",
            "durable_object_namespace",
            "hyperdrive",
            "json",
            "kv_namespace",
            "mtls_certificate",
            "plain_text",
            "queue",
            "r2_bucket",
            "secret_text",
            "service",
            "tail_consumer",
            "vectorize",
            "version_metadata",
        ]
    ]
    """The kind of resource that the binding provides."""


class SettingsBindingWorkersBindingKindAnalyticsEngine(TypedDict, total=False):
    dataset: Required[str]
    """The name of the dataset to bind to."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[
        Literal[
            "ai",
            "analytics_engine",
            "assets",
            "browser_rendering",
            "d1",
            "dispatch_namespace",
            "durable_object_namespace",
            "hyperdrive",
            "json",
            "kv_namespace",
            "mtls_certificate",
            "plain_text",
            "queue",
            "r2_bucket",
            "secret_text",
            "service",
            "tail_consumer",
            "vectorize",
            "version_metadata",
        ]
    ]
    """The kind of resource that the binding provides."""


class SettingsBindingWorkersBindingKindAssets(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[
        Literal[
            "ai",
            "analytics_engine",
            "assets",
            "browser_rendering",
            "d1",
            "dispatch_namespace",
            "durable_object_namespace",
            "hyperdrive",
            "json",
            "kv_namespace",
            "mtls_certificate",
            "plain_text",
            "queue",
            "r2_bucket",
            "secret_text",
            "service",
            "tail_consumer",
            "vectorize",
            "version_metadata",
        ]
    ]
    """The kind of resource that the binding provides."""


class SettingsBindingWorkersBindingKindBrowserRendering(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[
        Literal[
            "ai",
            "analytics_engine",
            "assets",
            "browser_rendering",
            "d1",
            "dispatch_namespace",
            "durable_object_namespace",
            "hyperdrive",
            "json",
            "kv_namespace",
            "mtls_certificate",
            "plain_text",
            "queue",
            "r2_bucket",
            "secret_text",
            "service",
            "tail_consumer",
            "vectorize",
            "version_metadata",
        ]
    ]
    """The kind of resource that the binding provides."""


class SettingsBindingWorkersBindingKindD1(TypedDict, total=False):
    id: Required[str]
    """Identifier of the D1 database to bind to."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[
        Literal[
            "ai",
            "analytics_engine",
            "assets",
            "browser_rendering",
            "d1",
            "dispatch_namespace",
            "durable_object_namespace",
            "hyperdrive",
            "json",
            "kv_namespace",
            "mtls_certificate",
            "plain_text",
            "queue",
            "r2_bucket",
            "secret_text",
            "service",
            "tail_consumer",
            "vectorize",
            "version_metadata",
        ]
    ]
    """The kind of resource that the binding provides."""


class SettingsBindingWorkersBindingKindDispatchNamespaceOutboundWorker(TypedDict, total=False):
    environment: str
    """Environment of the outbound worker."""

    service: str
    """Name of the outbound worker."""


class SettingsBindingWorkersBindingKindDispatchNamespaceOutbound(TypedDict, total=False):
    params: List[str]
    """
    Pass information from the Dispatch Worker to the Outbound Worker through the
    parameters.
    """

    worker: SettingsBindingWorkersBindingKindDispatchNamespaceOutboundWorker
    """Outbound worker."""


class SettingsBindingWorkersBindingKindDispatchNamespace(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    namespace: Required[str]
    """Namespace to bind to."""

    type: Required[
        Literal[
            "ai",
            "analytics_engine",
            "assets",
            "browser_rendering",
            "d1",
            "dispatch_namespace",
            "durable_object_namespace",
            "hyperdrive",
            "json",
            "kv_namespace",
            "mtls_certificate",
            "plain_text",
            "queue",
            "r2_bucket",
            "secret_text",
            "service",
            "tail_consumer",
            "vectorize",
            "version_metadata",
        ]
    ]
    """The kind of resource that the binding provides."""

    outbound: SettingsBindingWorkersBindingKindDispatchNamespaceOutbound
    """Outbound worker."""


class SettingsBindingWorkersBindingKindDurableObjectNamespace(TypedDict, total=False):
    class_name: Required[str]
    """The exported class name of the Durable Object."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[
        Literal[
            "ai",
            "analytics_engine",
            "assets",
            "browser_rendering",
            "d1",
            "dispatch_namespace",
            "durable_object_namespace",
            "hyperdrive",
            "json",
            "kv_namespace",
            "mtls_certificate",
            "plain_text",
            "queue",
            "r2_bucket",
            "secret_text",
            "service",
            "tail_consumer",
            "vectorize",
            "version_metadata",
        ]
    ]
    """The kind of resource that the binding provides."""

    environment: str
    """The environment of the script_name to bind to."""

    namespace_id: str
    """Namespace identifier tag."""

    script_name: str
    """
    The script where the Durable Object is defined, if it is external to this
    Worker.
    """


class SettingsBindingWorkersBindingKindHyperdrive(TypedDict, total=False):
    id: Required[str]
    """Identifier of the Hyperdrive connection to bind to."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[
        Literal[
            "ai",
            "analytics_engine",
            "assets",
            "browser_rendering",
            "d1",
            "dispatch_namespace",
            "durable_object_namespace",
            "hyperdrive",
            "json",
            "kv_namespace",
            "mtls_certificate",
            "plain_text",
            "queue",
            "r2_bucket",
            "secret_text",
            "service",
            "tail_consumer",
            "vectorize",
            "version_metadata",
        ]
    ]
    """The kind of resource that the binding provides."""


class SettingsBindingWorkersBindingKindJson(TypedDict, total=False):
    json: Required[str]
    """JSON data to use."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[
        Literal[
            "ai",
            "analytics_engine",
            "assets",
            "browser_rendering",
            "d1",
            "dispatch_namespace",
            "durable_object_namespace",
            "hyperdrive",
            "json",
            "kv_namespace",
            "mtls_certificate",
            "plain_text",
            "queue",
            "r2_bucket",
            "secret_text",
            "service",
            "tail_consumer",
            "vectorize",
            "version_metadata",
        ]
    ]
    """The kind of resource that the binding provides."""


class SettingsBindingWorkersBindingKindKVNamespace(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    namespace_id: Required[str]
    """Namespace identifier tag."""

    type: Required[
        Literal[
            "ai",
            "analytics_engine",
            "assets",
            "browser_rendering",
            "d1",
            "dispatch_namespace",
            "durable_object_namespace",
            "hyperdrive",
            "json",
            "kv_namespace",
            "mtls_certificate",
            "plain_text",
            "queue",
            "r2_bucket",
            "secret_text",
            "service",
            "tail_consumer",
            "vectorize",
            "version_metadata",
        ]
    ]
    """The kind of resource that the binding provides."""


class SettingsBindingWorkersBindingKindMTLSCertificate(TypedDict, total=False):
    certificate_id: Required[str]
    """Identifier of the certificate to bind to."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[
        Literal[
            "ai",
            "analytics_engine",
            "assets",
            "browser_rendering",
            "d1",
            "dispatch_namespace",
            "durable_object_namespace",
            "hyperdrive",
            "json",
            "kv_namespace",
            "mtls_certificate",
            "plain_text",
            "queue",
            "r2_bucket",
            "secret_text",
            "service",
            "tail_consumer",
            "vectorize",
            "version_metadata",
        ]
    ]
    """The kind of resource that the binding provides."""


class SettingsBindingWorkersBindingKindPlainText(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    text: Required[str]
    """The text value to use."""

    type: Required[
        Literal[
            "ai",
            "analytics_engine",
            "assets",
            "browser_rendering",
            "d1",
            "dispatch_namespace",
            "durable_object_namespace",
            "hyperdrive",
            "json",
            "kv_namespace",
            "mtls_certificate",
            "plain_text",
            "queue",
            "r2_bucket",
            "secret_text",
            "service",
            "tail_consumer",
            "vectorize",
            "version_metadata",
        ]
    ]
    """The kind of resource that the binding provides."""


class SettingsBindingWorkersBindingKindQueue(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    queue_name: Required[str]
    """Name of the Queue to bind to."""

    type: Required[
        Literal[
            "ai",
            "analytics_engine",
            "assets",
            "browser_rendering",
            "d1",
            "dispatch_namespace",
            "durable_object_namespace",
            "hyperdrive",
            "json",
            "kv_namespace",
            "mtls_certificate",
            "plain_text",
            "queue",
            "r2_bucket",
            "secret_text",
            "service",
            "tail_consumer",
            "vectorize",
            "version_metadata",
        ]
    ]
    """The kind of resource that the binding provides."""


class SettingsBindingWorkersBindingKindR2Bucket(TypedDict, total=False):
    bucket_name: Required[str]
    """R2 bucket to bind to."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[
        Literal[
            "ai",
            "analytics_engine",
            "assets",
            "browser_rendering",
            "d1",
            "dispatch_namespace",
            "durable_object_namespace",
            "hyperdrive",
            "json",
            "kv_namespace",
            "mtls_certificate",
            "plain_text",
            "queue",
            "r2_bucket",
            "secret_text",
            "service",
            "tail_consumer",
            "vectorize",
            "version_metadata",
        ]
    ]
    """The kind of resource that the binding provides."""


class SettingsBindingWorkersBindingKindSecretText(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    text: Required[str]
    """The secret value to use."""

    type: Required[
        Literal[
            "ai",
            "analytics_engine",
            "assets",
            "browser_rendering",
            "d1",
            "dispatch_namespace",
            "durable_object_namespace",
            "hyperdrive",
            "json",
            "kv_namespace",
            "mtls_certificate",
            "plain_text",
            "queue",
            "r2_bucket",
            "secret_text",
            "service",
            "tail_consumer",
            "vectorize",
            "version_metadata",
        ]
    ]
    """The kind of resource that the binding provides."""


class SettingsBindingWorkersBindingKindService(TypedDict, total=False):
    environment: Required[str]
    """Optional environment if the Worker utilizes one."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    service: Required[str]
    """Name of Worker to bind to."""

    type: Required[
        Literal[
            "ai",
            "analytics_engine",
            "assets",
            "browser_rendering",
            "d1",
            "dispatch_namespace",
            "durable_object_namespace",
            "hyperdrive",
            "json",
            "kv_namespace",
            "mtls_certificate",
            "plain_text",
            "queue",
            "r2_bucket",
            "secret_text",
            "service",
            "tail_consumer",
            "vectorize",
            "version_metadata",
        ]
    ]
    """The kind of resource that the binding provides."""


class SettingsBindingWorkersBindingKindTailConsumer(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    service: Required[str]
    """Name of Tail Worker to bind to."""

    type: Required[
        Literal[
            "ai",
            "analytics_engine",
            "assets",
            "browser_rendering",
            "d1",
            "dispatch_namespace",
            "durable_object_namespace",
            "hyperdrive",
            "json",
            "kv_namespace",
            "mtls_certificate",
            "plain_text",
            "queue",
            "r2_bucket",
            "secret_text",
            "service",
            "tail_consumer",
            "vectorize",
            "version_metadata",
        ]
    ]
    """The kind of resource that the binding provides."""


class SettingsBindingWorkersBindingKindVectorize(TypedDict, total=False):
    index_name: Required[str]
    """Name of the Vectorize index to bind to."""

    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[
        Literal[
            "ai",
            "analytics_engine",
            "assets",
            "browser_rendering",
            "d1",
            "dispatch_namespace",
            "durable_object_namespace",
            "hyperdrive",
            "json",
            "kv_namespace",
            "mtls_certificate",
            "plain_text",
            "queue",
            "r2_bucket",
            "secret_text",
            "service",
            "tail_consumer",
            "vectorize",
            "version_metadata",
        ]
    ]
    """The kind of resource that the binding provides."""


class SettingsBindingWorkersBindingKindVersionMetadata(TypedDict, total=False):
    name: Required[str]
    """A JavaScript variable name for the binding."""

    type: Required[
        Literal[
            "ai",
            "analytics_engine",
            "assets",
            "browser_rendering",
            "d1",
            "dispatch_namespace",
            "durable_object_namespace",
            "hyperdrive",
            "json",
            "kv_namespace",
            "mtls_certificate",
            "plain_text",
            "queue",
            "r2_bucket",
            "secret_text",
            "service",
            "tail_consumer",
            "vectorize",
            "version_metadata",
        ]
    ]
    """The kind of resource that the binding provides."""


SettingsBinding: TypeAlias = Union[
    SettingsBindingWorkersBindingKindAI,
    SettingsBindingWorkersBindingKindAnalyticsEngine,
    SettingsBindingWorkersBindingKindAssets,
    SettingsBindingWorkersBindingKindBrowserRendering,
    SettingsBindingWorkersBindingKindD1,
    SettingsBindingWorkersBindingKindDispatchNamespace,
    SettingsBindingWorkersBindingKindDurableObjectNamespace,
    SettingsBindingWorkersBindingKindHyperdrive,
    SettingsBindingWorkersBindingKindJson,
    SettingsBindingWorkersBindingKindKVNamespace,
    SettingsBindingWorkersBindingKindMTLSCertificate,
    SettingsBindingWorkersBindingKindPlainText,
    SettingsBindingWorkersBindingKindQueue,
    SettingsBindingWorkersBindingKindR2Bucket,
    SettingsBindingWorkersBindingKindSecretText,
    SettingsBindingWorkersBindingKindService,
    SettingsBindingWorkersBindingKindTailConsumer,
    SettingsBindingWorkersBindingKindVectorize,
    SettingsBindingWorkersBindingKindVersionMetadata,
]


class SettingsLimits(TypedDict, total=False):
    cpu_ms: int
    """The amount of CPU time this Worker can use in milliseconds."""


class SettingsMigrationsWorkersMultipleStepMigrations(TypedDict, total=False):
    new_tag: str
    """Tag to set as the latest migration tag."""

    old_tag: str
    """Tag used to verify against the latest migration tag for this Worker.

    If they don't match, the upload is rejected.
    """

    steps: Iterable[MigrationStepParam]
    """Migrations to apply in order."""


SettingsMigrations: TypeAlias = Union[SingleStepMigrationParam, SettingsMigrationsWorkersMultipleStepMigrations]


class SettingsObservability(TypedDict, total=False):
    enabled: Required[bool]
    """Whether observability is enabled for the Worker."""

    head_sampling_rate: Optional[float]
    """The sampling rate for incoming requests.

    From 0 to 1 (1 = 100%, 0.1 = 10%). Default is 1.
    """


class SettingsPlacement(TypedDict, total=False):
    mode: Literal["smart"]
    """
    Enables
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    """


class Settings(TypedDict, total=False):
    bindings: Iterable[SettingsBinding]
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

    limits: SettingsLimits
    """Limits to apply for this Worker."""

    logpush: bool
    """Whether Logpush is turned on for the Worker."""

    migrations: SettingsMigrations
    """Migrations to apply for Durable Objects associated with this Worker."""

    observability: SettingsObservability
    """Observability settings for the Worker."""

    placement: SettingsPlacement
    """
    Configuration for
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    """

    tags: List[str]
    """Tags to help you manage your Workers"""

    tail_consumers: Iterable[ConsumerScriptParam]
    """List of Workers that will consume logs from the attached Worker."""

    usage_model: Literal["standard"]
    """Usage model for the Worker invocations."""
