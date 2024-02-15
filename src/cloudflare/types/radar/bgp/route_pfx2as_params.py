# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

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
