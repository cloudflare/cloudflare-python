# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["WAFParam"]


class WAFParam(TypedDict, total=False):
    id: Literal["waf"]
    """
    Turn on or off
    [WAF managed rules (previous version, deprecated)](https://developers.cloudflare.com/waf/reference/legacy/old-waf-managed-rules/).
    You cannot enable or disable individual WAF managed rules via Page Rules.
    """

    value: Literal["on", "off"]
    """The status of WAF managed rules (previous version)."""
