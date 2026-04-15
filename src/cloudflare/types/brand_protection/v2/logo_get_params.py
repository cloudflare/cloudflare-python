# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["LogoGetParams"]


class LogoGetParams(TypedDict, total=False):
    account_id: str

    id: str
    """Optional query ID to retrieve a specific logo query"""

    download: str
    """If true, include base64-encoded image data in the response"""
