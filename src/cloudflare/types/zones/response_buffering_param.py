# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ResponseBufferingParam"]


class ResponseBufferingParam(TypedDict, total=False):
    id: Literal["response_buffering"]
    """
    Turn on or off whether Cloudflare should wait for an entire file from the origin
    server before forwarding it to the site visitor. By default, Cloudflare sends
    packets to the client as they arrive from the origin server.
    """

    value: Literal["on", "off"]
    """The status of Response Buffering"""
