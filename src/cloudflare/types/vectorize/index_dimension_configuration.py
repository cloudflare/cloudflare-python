# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["IndexDimensionConfiguration"]

class IndexDimensionConfiguration(BaseModel):
    dimensions: int
    """Specifies the number of dimensions for the index"""

    metric: Literal["cosine", "euclidean", "dot-product"]
    """Specifies the type of metric to use calculating distance."""