# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CustomPageUpdateParams"]


class CustomPageUpdateParams(TypedDict, total=False):
    state: Required[Literal["default", "customized"]]
    """The custom page state."""

    url: Required[str]
    """The URL associated with the custom page."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""
