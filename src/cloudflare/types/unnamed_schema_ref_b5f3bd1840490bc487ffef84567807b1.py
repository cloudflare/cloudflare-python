# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["UnnamedSchemaRefB5f3bd1840490bc487ffef84567807b1"]


class UnnamedSchemaRefB5f3bd1840490bc487ffef84567807b1(BaseModel):
    data_source: str = FieldInfo(alias="dataSource")

    description: str

    event_type: str = FieldInfo(alias="eventType")

    is_instantaneous: object = FieldInfo(alias="isInstantaneous")

    end_time: Optional[datetime] = FieldInfo(alias="endTime", default=None)

    linked_url: Optional[str] = FieldInfo(alias="linkedUrl", default=None)

    start_time: Optional[datetime] = FieldInfo(alias="startTime", default=None)
