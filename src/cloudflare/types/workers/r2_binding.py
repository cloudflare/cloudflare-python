# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["R2Binding"]


class R2Binding(BaseModel):
    bucket_name: str
    """R2 bucket to bind to"""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["r2_bucket"]
    """The class of resource that the binding provides."""
