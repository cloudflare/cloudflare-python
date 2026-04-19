# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PacfileUpdateParams"]


class PacfileUpdateParams(TypedDict, total=False):
    account_id: str

    contents: Required[str]
    """Actual contents of the PAC file"""

    description: Required[str]
    """Detailed description of the PAC file."""

    name: Required[str]
    """Name of the PAC file."""
