# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal, Annotated

from typing import Iterable

from ..._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["IndexQueryParams"]


class IndexQueryParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    vector: Required[Iterable[float]]
    """The search vector that will be used to find the nearest neighbors."""

    filter: object
    """A metadata filter expression used to limit nearest neighbor results."""

    return_metadata: Annotated[Literal["none", "indexed", "all"], PropertyInfo(alias="returnMetadata")]
    """
    Whether to return no metadata, indexed metadata or all metadata associated with
    the closest vectors.
    """

    return_values: Annotated[bool, PropertyInfo(alias="returnValues")]
    """Whether to return the values associated with the closest vectors."""

    top_k: Annotated[float, PropertyInfo(alias="topK")]
    """The number of nearest neighbors to find."""
