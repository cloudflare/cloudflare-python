# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Queue"]


class Queue(BaseModel):
    consumers: Optional[object] = None

    consumers_total_count: Optional[float] = None

    created_on: Optional[str] = None

    modified_on: Optional[str] = None

    producers: Optional[object] = None

    producers_total_count: Optional[float] = None

    queue_id: Optional[str] = None

    queue_name: Optional[str] = None
