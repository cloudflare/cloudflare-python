# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["IPList"]


class IPList(BaseModel):
    id: Optional[int] = None

    description: Optional[str] = None

    name: Optional[str] = None
