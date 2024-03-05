# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from .._models import BaseModel

__all__ = ["WorkersQueueUpdated"]


class WorkersQueueUpdated(BaseModel):
    created_on: Optional[object] = None

    modified_on: Optional[object] = None

    queue_id: Optional[object] = None

    queue_name: Optional[str] = None
