# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["LogoCreateResponse"]


class LogoCreateResponse(BaseModel):
    id: Optional[int] = None

    tag: Optional[str] = None

    upload_path: Optional[str] = None
