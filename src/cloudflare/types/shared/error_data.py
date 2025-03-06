# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ErrorData", "Source"]


class Source(BaseModel):
    pointer: Optional[str] = None


class ErrorData(BaseModel):
    code: Optional[int] = None

    documentation_url: Optional[str] = None

    message: Optional[str] = None

    source: Optional[Source] = None
