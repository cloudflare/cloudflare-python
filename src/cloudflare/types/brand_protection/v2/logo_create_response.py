# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["LogoCreateResponse"]


class LogoCreateResponse(BaseModel):
    message: str

    success: bool

    query_id: Optional[int] = None
