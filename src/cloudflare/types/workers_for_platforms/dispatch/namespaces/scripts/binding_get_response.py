# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ......_models import BaseModel

__all__ = [
    "BindingGetResponse",
    "WorkersBindingKindAny",
    "WorkersBindingKindAI",
    "WorkersBindingKindAnalyticsEngine",
    "WorkersBindingKindAssets",
    "WorkersBindingKindBrowserRendering",
    "WorkersBindingKindD1",
    "WorkersBindingKindDispatchNamespace",
    "WorkersBindingKindDispatchNamespaceOutbound",
    "WorkersBindingKindDispatchNamespaceOutboundWorker",
    "WorkersBindingKindDo",
    "WorkersBindingKindHyperdrive",
    "WorkersBindingKindJson",
    "WorkersBindingKindKVNamespace",
    "WorkersBindingKindMTLSCERT",
    "WorkersBindingKindPlainText",
    "WorkersBindingKindQueue",
    "WorkersBindingKindR2",
    "WorkersBindingKindSecret",
    "WorkersBindingKindService",
    "WorkersBindingKindTailConsumer",
    "WorkersBindingKindVectorize",
    "WorkersBindingKindVersionMetadata",
]


class WorkersBindingKindAny(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: str
    """The kind of resource that the binding provides."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class WorkersBindingKindAI(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["ai"]
    """The kind of resource that the binding provides."""


class WorkersBindingKindAnalyticsEngine(BaseModel):
    dataset: str
    """The dataset name to bind to."""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["analytics_engine"]
    """The kind of resource that the binding provides."""


class WorkersBindingKindAssets(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["assets"]
    """The kind of resource that the binding provides."""


class WorkersBindingKindBrowserRendering(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["browser_rendering"]
    """The kind of resource that the binding provides."""


class WorkersBindingKindD1(BaseModel):
    id: str
    """Identifier of the D1 database to bind to."""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["d1"]
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

    type: Literal["dispatch_namespace"]
    """The kind of resource that the binding provides."""

    outbound: Optional[WorkersBindingKindDispatchNamespaceOutbound] = None
    """Outbound worker."""


class WorkersBindingKindDo(BaseModel):
    class_name: str
    """The exported class name of the Durable Object."""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["durable_object_namespace"]
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

    type: Literal["hyperdrive"]
    """The kind of resource that the binding provides."""


class WorkersBindingKindJson(BaseModel):
    json_: str = FieldInfo(alias="json")
    """JSON data to use."""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["json"]
    """The kind of resource that the binding provides."""


class WorkersBindingKindKVNamespace(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    namespace_id: str
    """Namespace identifier tag."""

    type: Literal["kv_namespace"]
    """The kind of resource that the binding provides."""


class WorkersBindingKindMTLSCERT(BaseModel):
    certificate_id: str
    """Identifier of the certificate to bind to."""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["mtls_certificate"]
    """The kind of resource that the binding provides."""


class WorkersBindingKindPlainText(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    text: str
    """The text value to use."""

    type: Literal["plain_text"]
    """The kind of resource that the binding provides."""


class WorkersBindingKindQueue(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    queue_name: str
    """Name of the Queue to bind to."""

    type: Literal["queue"]
    """The kind of resource that the binding provides."""


class WorkersBindingKindR2(BaseModel):
    bucket_name: str
    """R2 bucket to bind to."""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["r2_bucket"]
    """The kind of resource that the binding provides."""


class WorkersBindingKindSecret(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    text: str
    """The secret value to use."""

    type: Literal["secret_text"]
    """The kind of resource that the binding provides."""


class WorkersBindingKindService(BaseModel):
    environment: str
    """Optional environment if the Worker utilizes one."""

    name: str
    """A JavaScript variable name for the binding."""

    service: str
    """Name of Worker to bind to."""

    type: Literal["service"]
    """The kind of resource that the binding provides."""


class WorkersBindingKindTailConsumer(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    service: str
    """Name of Tail Worker to bind to."""

    type: Literal["tail_consumer"]
    """The kind of resource that the binding provides."""


class WorkersBindingKindVectorize(BaseModel):
    index_name: str
    """Name of the Vectorize index to bind to."""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["vectorize"]
    """The kind of resource that the binding provides."""


class WorkersBindingKindVersionMetadata(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["version_metadata"]
    """The kind of resource that the binding provides."""


BindingGetResponse: TypeAlias = Union[
    WorkersBindingKindAny,
    WorkersBindingKindAI,
    WorkersBindingKindAnalyticsEngine,
    WorkersBindingKindAssets,
    WorkersBindingKindBrowserRendering,
    WorkersBindingKindD1,
    WorkersBindingKindDispatchNamespace,
    WorkersBindingKindDo,
    WorkersBindingKindHyperdrive,
    WorkersBindingKindJson,
    WorkersBindingKindKVNamespace,
    WorkersBindingKindMTLSCERT,
    WorkersBindingKindPlainText,
    WorkersBindingKindQueue,
    WorkersBindingKindR2,
    WorkersBindingKindSecret,
    WorkersBindingKindService,
    WorkersBindingKindTailConsumer,
    WorkersBindingKindVectorize,
    WorkersBindingKindVersionMetadata,
]
