# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Literal, Annotated

from ...._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo
from ....types import shared_params

__all__ = ["RoutePfx2asParams"]


class RoutePfx2asParams(TypedDict, total=False):
    format: Literal["JSON", "CSV"]
    """Format results are returned in."""

    origin: int
    """Lookup prefixes originated by the given ASN"""

    prefix: str
    """Lookup origins of the given prefix"""

    rpki_status: Annotated[Literal["VALID", "INVALID", "UNKNOWN"], PropertyInfo(alias="rpkiStatus")]
    """Return only results with matching rpki status: valid, invalid or unknown"""
