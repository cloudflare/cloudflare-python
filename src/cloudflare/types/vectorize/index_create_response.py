# File generated from our OpenAPI spec by Stainless.

from typing_extensions import Literal

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["IndexCreateResponse", "Config"]


class Config(BaseModel):
    dimensions: int
    """Specifies the number of dimensions for the index"""

    metric: Literal["cosine", "euclidean", "dot-product"]
    """Specifies the type of metric to use calculating distance."""


class IndexCreateResponse(BaseModel):
    config: Optional[Config] = None

    created_on: Optional[object] = None
    """Specifies the timestamp the resource was created as an ISO8601 string."""

    description: Optional[str] = None
    """Specifies the description of the index."""

    modified_on: Optional[object] = None
    """Specifies the timestamp the resource was modified as an ISO8601 string."""

    name: Optional[str] = None
