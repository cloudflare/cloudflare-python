# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["Schedule"]


class Schedule(BaseModel):
    created_on: Optional[str] = None

    cron: Optional[str] = None

    modified_on: Optional[str] = None
