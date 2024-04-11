# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["UniqueClientIDInputParam"]


class UniqueClientIDInputParam(TypedDict, total=False):
    id: Required[str]
    """List ID."""

    operating_system: Required[Literal["android", "ios", "chromeos"]]
    """Operating System"""
