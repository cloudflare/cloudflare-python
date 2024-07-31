# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["QueueCreated"]


class QueueCreated(BaseModel):
    created_on: Optional[str] = None

    modified_on: Optional[str] = None

    queue_id: Optional[str] = None

    queue_name: Optional[str] = None
