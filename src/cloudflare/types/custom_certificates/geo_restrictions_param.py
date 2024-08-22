# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["GeoRestrictionsParam"]


class GeoRestrictionsParam(TypedDict, total=False):
    label: Literal["us", "eu", "highest_security"]
