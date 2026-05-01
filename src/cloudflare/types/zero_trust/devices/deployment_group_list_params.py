# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DeploymentGroupListParams"]


class DeploymentGroupListParams(TypedDict, total=False):
    account_id: Required[str]

    page: int
    """The page number to return."""

    per_page: int
    """The maximum number of deployment groups to return per page."""
