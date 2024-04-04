# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["UnnamedSchemaRefBaac9d7da12de53e99142f8ecd3982e5"]


class UnnamedSchemaRefBaac9d7da12de53e99142f8ecd3982e5(BaseModel):
    end_time: datetime = FieldInfo(alias="endTime")
    """Adjusted end of date range."""

    start_time: datetime = FieldInfo(alias="startTime")
    """Adjusted start of date range."""
