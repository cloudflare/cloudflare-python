# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["OnRampGetParams"]


class OnRampGetParams(TypedDict, total=False):
    account_id: Required[str]

    planned_resources: bool

    post_apply_resources: bool

    status: bool

    vpcs: bool
