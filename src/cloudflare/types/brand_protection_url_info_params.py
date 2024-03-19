# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BrandProtectionURLInfoParams", "URLIDParam"]


class BrandProtectionURLInfoParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    url: str

    url_id_param: URLIDParam


class URLIDParam(TypedDict, total=False):
    url_id: int
    """Submission ID(s) to filter submission results by."""
