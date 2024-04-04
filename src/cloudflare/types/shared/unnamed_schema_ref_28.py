# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["UnnamedSchemaRef28"]


class UnnamedSchemaRef28(BaseModel):
    dns: Optional[object] = None
    """Logging settings for DNS firewall."""

    http: Optional[object] = None
    """Logging settings for HTTP/HTTPS firewall."""

    l4: Optional[object] = None
    """Logging settings for Network firewall."""
