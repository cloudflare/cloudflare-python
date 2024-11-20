# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["OriginErrorPagePassThruParam", "Value"]


class Value(TypedDict, total=False):
    value: Literal["on", "off"]
    """The status of Origin Error Page Passthru."""


class OriginErrorPagePassThruParam(TypedDict, total=False):
    id: Literal["origin_error_page_pass_thru"]
    """
    Turn on or off Cloudflare error pages generated from issues sent from the origin
    server. If enabled, this setting triggers error pages issued by the origin.
    """

    value: Value
