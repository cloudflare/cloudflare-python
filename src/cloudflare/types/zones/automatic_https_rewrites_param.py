# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AutomaticHTTPSRewritesParam"]


class AutomaticHTTPSRewritesParam(TypedDict, total=False):
    id: Literal["automatic_https_rewrites"]
    """Turn on or off Automatic HTTPS Rewrites."""

    value: Literal["on", "off"]
    """The status of Automatic HTTPS Rewrites."""
