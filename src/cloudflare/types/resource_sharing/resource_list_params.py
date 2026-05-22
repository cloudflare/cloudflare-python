# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ResourceListParams"]


class ResourceListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier."""

    page: int
    """Page number.

    Defaults to `1` when `per_page` is supplied without `page`. May be omitted
    entirely along with `per_page` to receive a non-paginated response.
    """

    per_page: int
    """Number of objects to return per page.

    Defaults to `20` when `page` is supplied without `per_page`. May be omitted
    entirely along with `page` to receive a non-paginated response.
    """

    resource_type: Literal[
        "custom-ruleset",
        "gateway-policy",
        "gateway-destination-ip",
        "gateway-block-page-settings",
        "gateway-extended-email-matching",
        "idp-federation-grant",
    ]
    """Filter share resources by resource_type."""

    status: Literal["active", "deleting", "deleted"]
    """Filter share resources by status."""
