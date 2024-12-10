# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .consumer import Consumer
from ..._models import BaseModel

__all__ = ["Queue", "Producer", "ProducerMqWorkerProducer", "ProducerMqR2Producer", "Settings"]


class ProducerMqWorkerProducer(BaseModel):
    script: Optional[str] = None

    type: Optional[Literal["worker"]] = None


class ProducerMqR2Producer(BaseModel):
    bucket_name: Optional[str] = None

    type: Optional[Literal["r2_bucket"]] = None


Producer: TypeAlias = Union[ProducerMqWorkerProducer, ProducerMqR2Producer]


class Settings(BaseModel):
    delivery_delay: Optional[float] = None
    """Number of seconds to delay delivery of all messages to consumers."""

    message_retention_period: Optional[float] = None
    """Number of seconds after which an unconsumed message will be delayed."""


class Queue(BaseModel):
    consumers: Optional[List[Consumer]] = None

    consumers_total_count: Optional[float] = None

    created_on: Optional[str] = None

    modified_on: Optional[str] = None

    producers: Optional[List[Producer]] = None

    producers_total_count: Optional[float] = None

    queue_id: Optional[str] = None

    queue_name: Optional[str] = None

    settings: Optional[Settings] = None
