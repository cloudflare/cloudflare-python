# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CustomPageValidateParams"]


class CustomPageValidateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    template: Required[str]
    """The Liquid template to validate."""

    type: Required[Literal["identity_denied", "forbidden", "login", "interstitial"]]
    """Custom page type."""

    version: int
    """Contract version to validate against; omit for the latest."""
