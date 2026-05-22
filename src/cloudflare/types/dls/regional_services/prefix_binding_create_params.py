# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PrefixBindingCreateParams"]


class PrefixBindingCreateParams(TypedDict, total=False):
    account_id: Required[int]

    cidr: Required[str]
    """IP prefix in CIDR notation to bind."""

    prefix_id: Required[str]
    """The ID of the parent IP prefix that contains the CIDR."""

    region_key: Required[str]
    """Region key from managed regions (e.g., "us", "eu")."""
