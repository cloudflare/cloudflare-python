# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["EventCreateResponse"]


class EventCreateResponse(BaseModel):
    instance_id: str = FieldInfo(alias="instanceId")

    timestamp: datetime
    """Accepts ISO 8601 with no timezone offsets and in UTC."""
