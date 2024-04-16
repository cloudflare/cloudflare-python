# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MembershipUpdateParams"]


class MembershipUpdateParams(TypedDict, total=False):
    status: Required[Literal["accepted", "rejected"]]
    """Whether to accept or reject this account invitation."""
