# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Annotated

from ..._utils import PropertyInfo

from typing import Iterable

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["IndexQueryParams"]


class IndexQueryParams(TypedDict, total=False):
    account_identifier: Required[str]
    """Identifier"""

    return_metadata: Annotated[bool, PropertyInfo(alias="returnMetadata")]
    """Whether to return the metadata associated with the closest vectors."""

    return_values: Annotated[bool, PropertyInfo(alias="returnValues")]
    """Whether to return the values associated with the closest vectors."""

    top_k: Annotated[float, PropertyInfo(alias="topK")]
    """The number of nearest neighbors to find."""

    vector: Iterable[float]
    """The search vector that will be used to find the nearest neighbors."""
