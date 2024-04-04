# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["UnnamedSchemaRef22"]


class UnnamedSchemaRef22(BaseModel):
    dimensions: List[str]
    """
    Array of dimension values, representing the combination of dimension values
    corresponding to this row.
    """

    metrics: List[float]
    """Array with one item per requested metric. Each item is a single value."""
