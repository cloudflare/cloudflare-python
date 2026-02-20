# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PacfileCreateParams"]


class PacfileCreateParams(TypedDict, total=False):
    account_id: Required[str]

    contents: Required[str]
    """Actual contents of the PAC file"""

    name: Required[str]
    """Name of the PAC file."""

    description: str
    """Detailed description of the PAC file."""

    slug: str
    """URL-friendly version of the PAC file name.

    If not provided, it will be auto-generated
    """
