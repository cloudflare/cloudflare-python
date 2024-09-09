# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["RequestCreateParams"]


class RequestCreateParams(TypedDict, total=False):
    content: str
    """Request content"""

    priority: str
    """Priority for analyzing the request"""

    request_type: str
    """Requested information from request"""

    summary: str
    """Brief description of the request"""

    tlp: Literal["clear", "amber", "amber-strict", "green", "red"]
    """The CISA defined Traffic Light Protocol (TLP)"""
