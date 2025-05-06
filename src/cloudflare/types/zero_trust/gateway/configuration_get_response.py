# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["ConfigurationGetResponse"]


class ConfigurationGetResponse(BaseModel):
    created_at: Optional[datetime] = None

    settings: Optional[object] = None

    updated_at: Optional[datetime] = None
