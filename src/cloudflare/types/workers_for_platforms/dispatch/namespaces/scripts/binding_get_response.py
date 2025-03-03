# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ......_models import BaseModel

__all__ = [
    "BindingGetResponse",
    "WorkersBindingKindAI",
    "WorkersBindingKindAnalyticsEngine",
    "WorkersBindingKindAssets",
    "WorkersBindingKindBrowserRendering",
    "WorkersBindingKindD1",
    "WorkersBindingKindDispatchNamespace",
    "WorkersBindingKindDispatchNamespaceOutbound",
    "WorkersBindingKindDispatchNamespaceOutboundWorker",
    "WorkersBindingKindDurableObjectNamespace",
    "WorkersBindingKindHyperdrive",
    "WorkersBindingKindJson",
    "WorkersBindingKindKVNamespace",
    "WorkersBindingKindMTLSCertificate",
    "WorkersBindingKindPlainText",
    "WorkersBindingKindQueue",
    "WorkersBindingKindR2Bucket",
    "WorkersBindingKindSecretText",
    "WorkersBindingKindService",
    "WorkersBindingKindTailConsumer",
    "WorkersBindingKindVectorize",
    "WorkersBindingKindVersionMetadata",
]


class WorkersBindingKindAI(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal[
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
    """The kind of resource that the binding provides."""


class WorkersBindingKindAnalyticsEngine(BaseModel):
    dataset: str
    """The name of the dataset to bind to."""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal[
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
    """The kind of resource that the binding provides."""


class WorkersBindingKindAssets(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal[
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
    """The kind of resource that the binding provides."""


class WorkersBindingKindBrowserRendering(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal[
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
    """The kind of resource that the binding provides."""


class WorkersBindingKindD1(BaseModel):
    id: str
    """Identifier of the D1 database to bind to."""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal[
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
    """The kind of resource that the binding provides."""


class WorkersBindingKindDispatchNamespaceOutboundWorker(BaseModel):
    environment: Optional[str] = None
    """Environment of the outbound worker."""

    service: Optional[str] = None
    """Name of the outbound worker."""


class WorkersBindingKindDispatchNamespaceOutbound(BaseModel):
    params: Optional[List[str]] = None
    """
    Pass information from the Dispatch Worker to the Outbound Worker through the
    parameters.
    """

    worker: Optional[WorkersBindingKindDispatchNamespaceOutboundWorker] = None
    """Outbound worker."""


class WorkersBindingKindDispatchNamespace(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    namespace: str
    """Namespace to bind to."""

    type: Literal[
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
    """The kind of resource that the binding provides."""

    outbound: Optional[WorkersBindingKindDispatchNamespaceOutbound] = None
    """Outbound worker."""


class WorkersBindingKindDurableObjectNamespace(BaseModel):
    class_name: str
    """The exported class name of the Durable Object."""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal[
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
    """The kind of resource that the binding provides."""

    environment: Optional[str] = None
    """The environment of the script_name to bind to."""

    namespace_id: Optional[str] = None
    """Namespace identifier tag."""

    script_name: Optional[str] = None
    """
    The script where the Durable Object is defined, if it is external to this
    Worker.
    """


class WorkersBindingKindHyperdrive(BaseModel):
    id: str
    """Identifier of the Hyperdrive connection to bind to."""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal[
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
    """The kind of resource that the binding provides."""


class WorkersBindingKindJson(BaseModel):
    json_: str = FieldInfo(alias="json")
    """JSON data to use."""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal[
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
    """The kind of resource that the binding provides."""


class WorkersBindingKindKVNamespace(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    namespace_id: str
    """Namespace identifier tag."""

    type: Literal[
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
    """The kind of resource that the binding provides."""


class WorkersBindingKindMTLSCertificate(BaseModel):
    certificate_id: str
    """Identifier of the certificate to bind to."""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal[
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
    """The kind of resource that the binding provides."""


class WorkersBindingKindPlainText(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    text: str
    """The text value to use."""

    type: Literal[
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
    """The kind of resource that the binding provides."""


class WorkersBindingKindQueue(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    queue_name: str
    """Name of the Queue to bind to."""

    type: Literal[
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
    """The kind of resource that the binding provides."""


class WorkersBindingKindR2Bucket(BaseModel):
    bucket_name: str
    """R2 bucket to bind to."""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal[
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
    """The kind of resource that the binding provides."""


class WorkersBindingKindSecretText(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    text: str
    """The secret value to use."""

    type: Literal[
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
    """The kind of resource that the binding provides."""


class WorkersBindingKindService(BaseModel):
    environment: str
    """Optional environment if the Worker utilizes one."""

    name: str
    """A JavaScript variable name for the binding."""

    service: str
    """Name of Worker to bind to."""

    type: Literal[
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
    """The kind of resource that the binding provides."""


class WorkersBindingKindTailConsumer(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    service: str
    """Name of Tail Worker to bind to."""

    type: Literal[
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
    """The kind of resource that the binding provides."""


class WorkersBindingKindVectorize(BaseModel):
    index_name: str
    """Name of the Vectorize index to bind to."""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal[
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
    """The kind of resource that the binding provides."""


class WorkersBindingKindVersionMetadata(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal[
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
    """The kind of resource that the binding provides."""


BindingGetResponse: TypeAlias = Union[
    WorkersBindingKindAI,
    WorkersBindingKindAnalyticsEngine,
    WorkersBindingKindAssets,
    WorkersBindingKindBrowserRendering,
    WorkersBindingKindD1,
    WorkersBindingKindDispatchNamespace,
    WorkersBindingKindDurableObjectNamespace,
    WorkersBindingKindHyperdrive,
    WorkersBindingKindJson,
    WorkersBindingKindKVNamespace,
    WorkersBindingKindMTLSCertificate,
    WorkersBindingKindPlainText,
    WorkersBindingKindQueue,
    WorkersBindingKindR2Bucket,
    WorkersBindingKindSecretText,
    WorkersBindingKindService,
    WorkersBindingKindTailConsumer,
    WorkersBindingKindVectorize,
    WorkersBindingKindVersionMetadata,
]
