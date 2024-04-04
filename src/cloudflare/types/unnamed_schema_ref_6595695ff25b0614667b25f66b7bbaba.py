# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["UnnamedSchemaRef6595695ff25b0614667b25f66b7bbaba"]


class UnnamedSchemaRef6595695ff25b0614667b25f66b7bbaba(BaseModel):
    dimensions: List[str]
    """
    Array of dimension values, representing the combination of dimension values
    corresponding to this row.
    """

    metrics: List[float]
    """Array with one item per requested metric. Each item is a single value."""
