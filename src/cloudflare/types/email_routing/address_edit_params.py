# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AddressEditParams"]


class AddressEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    status: Required[Literal["unverified", "verified"]]
    """Destination address status.

    Non-admin callers may only set verified addresses back to unverified; setting to
    verified requires admin privileges.
    """
