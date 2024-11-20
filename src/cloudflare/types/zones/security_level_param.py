# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SecurityLevelParam"]


class SecurityLevelParam(TypedDict, total=False):
    id: Literal["security_level"]
    """Control options for the **Security Level** feature from the **Security** app."""

    value: Literal["off", "essentially_off", "low", "medium", "high", "under_attack"]
