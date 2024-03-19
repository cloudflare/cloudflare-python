# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["OriginMaxHTTPVersionGetResponse"]


class OriginMaxHTTPVersionGetResponse(BaseModel):
    id: Literal["origin_max_http_version"]
    """Value of the zone setting."""

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""

    value: Literal["2", "1"]
    """Value of the Origin Max HTTP Version Setting."""
