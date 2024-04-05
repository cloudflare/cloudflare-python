# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Component"]


class Component(BaseModel):
    default: Optional[float] = None
    """The default amount allocated."""

    name: Optional[Literal["zones", "page_rules", "dedicated_certificates", "dedicated_certificates_custom"]] = None
    """The unique component."""

    unit_price: Optional[float] = None
    """The unit price of the addon."""
