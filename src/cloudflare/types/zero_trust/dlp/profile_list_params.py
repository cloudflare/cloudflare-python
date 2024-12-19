# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ProfileListParams"]


class ProfileListParams(TypedDict, total=False):
    account_id: Required[str]

    all: bool
    """
    Return all profiles, including those that current account does not have access
    to.
    """
