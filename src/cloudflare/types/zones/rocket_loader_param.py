# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["RocketLoaderParam"]


class RocketLoaderParam(TypedDict, total=False):
    id: Literal["rocket_loader"]
    """Turn on or off Rocket Loader in the Cloudflare Speed app."""

    value: Literal["on", "off"]
    """The status of Rocket Loader"""
