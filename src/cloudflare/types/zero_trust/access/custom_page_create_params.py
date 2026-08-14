# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CustomPageCreateParams"]


class CustomPageCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    custom_html: Required[str]
    """Custom page HTML."""

    name: Required[str]
    """Custom page name."""

    type: Required[Literal["identity_denied", "forbidden", "login", "interstitial"]]
    """Custom page type."""

    contract_version: int
    """Contract version of the page's Liquid template.

    Present (>= 1) marks a sanitized template; absent or 0 marks a legacy page
    served verbatim.
    """
