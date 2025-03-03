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
    "MetadataBindingWorkersBindingKindBrowserRendering",
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
    "MetadataBindingWorkersBindingKindQueue",
    "MetadataBindingWorkersBindingKindR2Bucket",
    "MetadataBindingWorkersBindingKindSecretText",
    "MetadataBindingWorkersBindingKindService",
    "MetadataBindingWorkersBindingKindTailConsumer",
    "MetadataBindingWorkersBindingKindVectorize",
    "MetadataBindingWorkersBindingKindVersionMetadata",
    "MetadataMigrations",
    "MetadataMigrationsWorkersMultipleStepMigrations",
    "MetadataObservability",
    "MetadataPlacement",
]


class ScriptUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    metadata: Required[Metadata]
    """JSON encoded metadata about the uploaded parts and Worker configuration."""


class MetadataAssetsConfig(TypedDict, total=False):
    html_handling: Literal["auto-trailing-slash", "force-trailing-slash", "drop-trailing-slash", "none"]
    """Determines the redirects and rewrites of requests for HTML content."""

    not_found_handling: Literal["none", "404-page", "single-page-application"]
    """
    Determines the response when a request does not match a static asset, and there
    is no Worker script.
    """

    run_worker_first: bool
    """When true, requests will always invoke the Worker script.

    Otherwise, attempt to serve an asset matching the request, falling back to the
    Worker script.
    """

    serve_directly: bool
    """
    When true and the incoming request matches an asset, that will be served instead
    of invoking the Worker script. When false, requests will always invoke the
    Worker script.
    """


class MetadataAssets(TypedDict, total=False):
    config: MetadataAssetsConfig
    """Configuration for assets within a Worker."""

    jwt: str
    """Token provided upon successful upload of all files from a registered manifest."""


class MetadataBindingWorkersBindingKindAI(TypedDict, total=False):
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


class MetadataBindingWorkersBindingKindAnalyticsEngine(TypedDict, total=False):
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


class MetadataBindingWorkersBindingKindAssets(TypedDict, total=False):
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


class MetadataBindingWorkersBindingKindBrowserRendering(TypedDict, total=False):
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


class MetadataBindingWorkersBindingKindD1(TypedDict, total=False):
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

    outbound: MetadataBindingWorkersBindingKindDispatchNamespaceOutbound
    """Outbound worker."""


class MetadataBindingWorkersBindingKindDurableObjectNamespace(TypedDict, total=False):
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


class MetadataBindingWorkersBindingKindHyperdrive(TypedDict, total=False):
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


class MetadataBindingWorkersBindingKindJson(TypedDict, total=False):
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


class MetadataBindingWorkersBindingKindKVNamespace(TypedDict, total=False):
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


class MetadataBindingWorkersBindingKindMTLSCertificate(TypedDict, total=False):
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


class MetadataBindingWorkersBindingKindPlainText(TypedDict, total=False):
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


class MetadataBindingWorkersBindingKindQueue(TypedDict, total=False):
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


class MetadataBindingWorkersBindingKindR2Bucket(TypedDict, total=False):
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


class MetadataBindingWorkersBindingKindSecretText(TypedDict, total=False):
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


class MetadataBindingWorkersBindingKindService(TypedDict, total=False):
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


class MetadataBindingWorkersBindingKindTailConsumer(TypedDict, total=False):
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


class MetadataBindingWorkersBindingKindVectorize(TypedDict, total=False):
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


class MetadataBindingWorkersBindingKindVersionMetadata(TypedDict, total=False):
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


MetadataBinding: TypeAlias = Union[
    MetadataBindingWorkersBindingKindAI,
    MetadataBindingWorkersBindingKindAnalyticsEngine,
    MetadataBindingWorkersBindingKindAssets,
    MetadataBindingWorkersBindingKindBrowserRendering,
    MetadataBindingWorkersBindingKindD1,
    MetadataBindingWorkersBindingKindDispatchNamespace,
    MetadataBindingWorkersBindingKindDurableObjectNamespace,
    MetadataBindingWorkersBindingKindHyperdrive,
    MetadataBindingWorkersBindingKindJson,
    MetadataBindingWorkersBindingKindKVNamespace,
    MetadataBindingWorkersBindingKindMTLSCertificate,
    MetadataBindingWorkersBindingKindPlainText,
    MetadataBindingWorkersBindingKindQueue,
    MetadataBindingWorkersBindingKindR2Bucket,
    MetadataBindingWorkersBindingKindSecretText,
    MetadataBindingWorkersBindingKindService,
    MetadataBindingWorkersBindingKindTailConsumer,
    MetadataBindingWorkersBindingKindVectorize,
    MetadataBindingWorkersBindingKindVersionMetadata,
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


class MetadataObservability(TypedDict, total=False):
    enabled: Required[bool]
    """Whether observability is enabled for the Worker."""

    head_sampling_rate: Optional[float]
    """The sampling rate for incoming requests.

    From 0 to 1 (1 = 100%, 0.1 = 10%). Default is 1.
    """


class MetadataPlacement(TypedDict, total=False):
    mode: Literal["smart"]
    """
    Enables
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    """


class Metadata(TypedDict, total=False):
    assets: MetadataAssets
    """Configuration for assets within a Worker"""

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
