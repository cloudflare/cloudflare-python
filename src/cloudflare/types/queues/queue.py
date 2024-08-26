# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .consumer import Consumer
from ..._models import BaseModel

__all__ = ["Queue", "Producer"]


class Producer(BaseModel):
    environment: Optional[str] = None

    service: Optional[str] = None


class Queue(BaseModel):
    consumers: Optional[List[Consumer]] = None

    consumers_total_count: Optional[float] = None

    created_on: Optional[str] = None

    modified_on: Optional[str] = None

    producers: Optional[List[Producer]] = None

    producers_total_count: Optional[float] = None

    queue_id: Optional[str] = None

    queue_name: Optional[str] = None
