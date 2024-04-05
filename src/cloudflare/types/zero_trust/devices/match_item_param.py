# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["MatchItemParam"]


class MatchItemParam(TypedDict, total=False):
    platform: Literal["windows", "mac", "linux", "android", "ios"]
