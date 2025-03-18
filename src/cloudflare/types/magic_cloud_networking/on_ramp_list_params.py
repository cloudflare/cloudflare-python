# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["OnRampListParams"]


class OnRampListParams(TypedDict, total=False):
    account_id: Required[str]

    desc: bool

    order_by: str
    """one of ["updated_at", "id", "cloud_type", "name"]"""

    status: bool

    vpcs: bool
