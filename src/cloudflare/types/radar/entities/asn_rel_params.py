# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ASNRelParams"]


class ASNRelParams(TypedDict, total=False):
    asn2: int
    """Retrieves the AS relationship of ASN2 with respect to the given ASN."""

    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""
