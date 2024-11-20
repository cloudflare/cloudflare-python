# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["PolishParam", "Value"]


class Value(TypedDict, total=False):
    value: Literal["off", "lossless", "lossy"]
    """The level of Polish you want applied to your origin."""


class PolishParam(TypedDict, total=False):
    id: Literal["polish"]
    """Apply options from the Polish feature of the Cloudflare Speed app."""

    value: Value
