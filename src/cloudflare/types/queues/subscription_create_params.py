# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "SubscriptionCreateParams",
    "Destination",
    "Source",
    "SourceMqEventSourceImages",
    "SourceMqEventSourceKV",
    "SourceMqEventSourceR2",
    "SourceMqEventSourceSuperSlurper",
    "SourceMqEventSourceVectorize",
    "SourceMqEventSourceWorkersAIModel",
    "SourceMqEventSourceWorkersBuildsWorker",
    "SourceMqEventSourceWorkflowsWorkflow",
]


class SubscriptionCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """A Resource identifier."""

    destination: Destination
    """Destination configuration for the subscription"""

    enabled: bool
    """Whether the subscription is active"""

    events: SequenceNotStr[str]
    """List of event types this subscription handles"""

    name: str
    """Name of the subscription"""

    source: Source
    """Source configuration for the subscription"""


class Destination(TypedDict, total=False):
    """Destination configuration for the subscription"""

    queue_id: Required[str]
    """ID of the target queue"""

    type: Required[Literal["queues.queue"]]
    """Type of destination"""


class SourceMqEventSourceImages(TypedDict, total=False):
    type: Literal["images"]
    """Type of source"""


class SourceMqEventSourceKV(TypedDict, total=False):
    type: Literal["kv"]
    """Type of source"""


class SourceMqEventSourceR2(TypedDict, total=False):
    type: Literal["r2"]
    """Type of source"""


class SourceMqEventSourceSuperSlurper(TypedDict, total=False):
    type: Literal["superSlurper"]
    """Type of source"""


class SourceMqEventSourceVectorize(TypedDict, total=False):
    type: Literal["vectorize"]
    """Type of source"""


class SourceMqEventSourceWorkersAIModel(TypedDict, total=False):
    model_name: str
    """Name of the Workers AI model"""

    type: Literal["workersAi.model"]
    """Type of source"""


class SourceMqEventSourceWorkersBuildsWorker(TypedDict, total=False):
    type: Literal["workersBuilds.worker"]
    """Type of source"""

    worker_name: str
    """Name of the worker"""


class SourceMqEventSourceWorkflowsWorkflow(TypedDict, total=False):
    type: Literal["workflows.workflow"]
    """Type of source"""

    workflow_name: str
    """Name of the workflow"""


Source: TypeAlias = Union[
    SourceMqEventSourceImages,
    SourceMqEventSourceKV,
    SourceMqEventSourceR2,
    SourceMqEventSourceSuperSlurper,
    SourceMqEventSourceVectorize,
    SourceMqEventSourceWorkersAIModel,
    SourceMqEventSourceWorkersBuildsWorker,
    SourceMqEventSourceWorkflowsWorkflow,
]
