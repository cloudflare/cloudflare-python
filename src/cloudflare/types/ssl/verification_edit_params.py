# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["VerificationEditParams"]


class VerificationEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    validation_method: Required[Literal["http", "cname", "txt", "email"]]
    """Desired validation method."""
