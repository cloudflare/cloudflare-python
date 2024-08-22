# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal, Annotated

from ...._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["MetadataIndexCreateParams"]

class MetadataIndexCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    index_type: Required[Annotated[Literal["string", "number", "boolean"], PropertyInfo(alias="indexType")]]
    """Specifies the type of metadata property to index."""

    property_name: Required[Annotated[str, PropertyInfo(alias="propertyName")]]
    """Specifies the metadata property to index."""