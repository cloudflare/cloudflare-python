# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "SubscriptionDeleteResponse",
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


class Destination(BaseModel):
    """Destination configuration for the subscription"""

    queue_id: str
    """ID of the target queue"""

    type: Literal["queues.queue"]
    """Type of destination"""


class SourceMqEventSourceImages(BaseModel):
    type: Optional[Literal["images"]] = None
    """Type of source"""


class SourceMqEventSourceKV(BaseModel):
    type: Optional[Literal["kv"]] = None
    """Type of source"""


class SourceMqEventSourceR2(BaseModel):
    type: Optional[Literal["r2"]] = None
    """Type of source"""


class SourceMqEventSourceSuperSlurper(BaseModel):
    type: Optional[Literal["superSlurper"]] = None
    """Type of source"""


class SourceMqEventSourceVectorize(BaseModel):
    type: Optional[Literal["vectorize"]] = None
    """Type of source"""


class SourceMqEventSourceWorkersAIModel(BaseModel):
    ai_model_name: Optional[str] = FieldInfo(alias="model_name", default=None)
    """Name of the Workers AI model"""

    type: Optional[Literal["workersAi.model"]] = None
    """Type of source"""


class SourceMqEventSourceWorkersBuildsWorker(BaseModel):
    type: Optional[Literal["workersBuilds.worker"]] = None
    """Type of source"""

    worker_name: Optional[str] = None
    """Name of the worker"""


class SourceMqEventSourceWorkflowsWorkflow(BaseModel):
    type: Optional[Literal["workflows.workflow"]] = None
    """Type of source"""

    workflow_name: Optional[str] = None
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


class SubscriptionDeleteResponse(BaseModel):
    id: str
    """Unique identifier for the subscription"""

    created_at: datetime
    """When the subscription was created"""

    destination: Destination
    """Destination configuration for the subscription"""

    enabled: bool
    """Whether the subscription is active"""

    events: List[str]
    """List of event types this subscription handles"""

    modified_at: datetime
    """When the subscription was last modified"""

    name: str
    """Name of the subscription"""

    source: Source
    """Source configuration for the subscription"""
