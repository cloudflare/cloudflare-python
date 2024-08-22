# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["DNS"]


class DNS(BaseModel):
    name: Optional[str] = None
    """The name of the DNS record associated with the application."""

    type: Optional[Literal["CNAME", "ADDRESS"]] = None
    """The type of DNS record associated with the application."""
