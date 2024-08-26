# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["IndexDimensionConfiguration"]


class IndexDimensionConfiguration(BaseModel):
    dimensions: int
    """Specifies the number of dimensions for the index"""

    metric: Literal["cosine", "euclidean", "dot-product"]
    """Specifies the type of metric to use calculating distance."""
