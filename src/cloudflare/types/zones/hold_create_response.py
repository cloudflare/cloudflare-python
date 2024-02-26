# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["HoldCreateResponse"]


class HoldCreateResponse(BaseModel):
    hold: Optional[bool] = None

    hold_after: Optional[str] = None

    include_subdomains: Optional[str] = None
