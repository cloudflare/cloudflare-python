# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["IndexDimensionConfigurationParam"]


class IndexDimensionConfigurationParam(TypedDict, total=False):
    dimensions: Required[int]
    """Specifies the number of dimensions for the index"""

    metric: Required[Literal["cosine", "euclidean", "dot-product"]]
    """Specifies the type of metric to use calculating distance."""
