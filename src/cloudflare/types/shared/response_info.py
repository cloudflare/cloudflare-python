# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ResponseInfo", "Source"]


class Source(BaseModel):
    pointer: Optional[str] = None


class ResponseInfo(BaseModel):
    code: int

    message: str

    documentation_url: Optional[str] = None

    source: Optional[Source] = None
