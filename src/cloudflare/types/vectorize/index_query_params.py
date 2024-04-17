# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["IndexQueryParams"]


class IndexQueryParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    vector: Required[Iterable[float]]
    """The search vector that will be used to find the nearest neighbors."""

    filter: object
    """A metadata filter expression used to limit nearest neighbor results."""

    return_metadata: Annotated[bool, PropertyInfo(alias="returnMetadata")]
    """Whether to return the metadata associated with the closest vectors."""

    return_values: Annotated[bool, PropertyInfo(alias="returnValues")]
    """Whether to return the values associated with the closest vectors."""

    top_k: Annotated[float, PropertyInfo(alias="topK")]
    """The number of nearest neighbors to find."""
