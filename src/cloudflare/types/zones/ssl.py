# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SSL"]


class SSL(BaseModel):
    id: Optional[Literal["ssl"]] = None
    """
    Control options for the SSL feature of the Edge Certificates tab in the
    Cloudflare SSL/TLS app.
    """

    value: Optional[Literal["off", "flexible", "full", "strict", "origin_pull"]] = None
    """The encryption mode that Cloudflare uses to connect to your origin server."""
