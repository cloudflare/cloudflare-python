# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel

__all__ = ["QueueUpdateResponse"]


class QueueUpdateResponse(BaseModel):
    event_notification_detail_id: Optional[str] = None
