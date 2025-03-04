# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SubnetListParams"]


class SubnetListParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID"""

    address_family: Literal["v4", "v6"]
    """If set, only include subnets in the given address family - `v4` or `v6`"""

    comment: str
    """If set, only list subnets with the given comment."""

    existed_at: str
    """
    If provided, include only resources that were created (and not deleted) before
    this time. URL encoded.
    """

    is_default_network: bool
    """If `true`, only include default subnets.

    If `false`, exclude default subnets subnets. If not set, all subnets will be
    included.
    """

    is_deleted: bool
    """If `true`, only include deleted subnets.

    If `false`, exclude deleted subnets. If not set, all subnets will be included.
    """

    name: str
    """If set, only list subnets with the given name"""

    network: str
    """If set, only list the subnet whose network exactly matches the given CIDR."""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Number of results to display."""

    sort_order: Literal["asc", "desc"]
    """Sort order of the results.

    `asc` means oldest to newest, `desc` means newest to oldest. If not set, they
    will not be in any particular order.
    """

    subnet_types: Literal["cloudflare_source", "warp"]
    """If set, the types of subnets to include, separated by comma."""
