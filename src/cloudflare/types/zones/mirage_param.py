# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["MirageParam", "Value"]


class Value(TypedDict, total=False):
    value: Literal["on", "off"]
    """The status of Mirage."""


class MirageParam(TypedDict, total=False):
    id: Literal["mirage"]
    """
    Cloudflare Mirage reduces bandwidth used by images in mobile browsers. It can
    accelerate loading of image-heavy websites on very slow mobile connections and
    HTTP/1.
    """

    value: Value
