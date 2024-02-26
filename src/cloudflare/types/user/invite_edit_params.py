# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["InviteEditParams"]


class InviteEditParams(TypedDict, total=False):
    status: Required[Literal["accepted", "rejected"]]
    """Status of your response to the invitation (rejected or accepted)."""
