# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ResponseBuffering"]


class ResponseBuffering(BaseModel):
    id: Optional[Literal["response_buffering"]] = None
    """
    Turn on or off whether Cloudflare should wait for an entire file from the origin
    server before forwarding it to the site visitor. By default, Cloudflare sends
    packets to the client as they arrive from the origin server.
    """

    value: Optional[Literal["on", "off"]] = None
    """The status of Response Buffering"""
