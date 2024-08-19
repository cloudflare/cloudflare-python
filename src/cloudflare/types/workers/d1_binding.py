# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["D1Binding"]


class D1Binding(BaseModel):
    id: str
    """ID of the D1 database to bind to"""

    binding: str
    """A JavaScript variable name for the binding."""

    name: str
    """The name of the D1 database associated with the 'id' provided."""

    type: Literal["d1"]
    """The class of resource that the binding provides."""
