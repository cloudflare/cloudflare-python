# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["R2Binding"]


class R2Binding(BaseModel):
    bucket_name: str
    """R2 bucket to bind to"""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["r2_bucket"]
    """The class of resource that the binding provides."""
