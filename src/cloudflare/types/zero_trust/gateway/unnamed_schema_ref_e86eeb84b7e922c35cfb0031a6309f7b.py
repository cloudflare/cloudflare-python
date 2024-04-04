# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["UnnamedSchemaRefE86eeb84b7e922c35cfb0031a6309f7b"]


class UnnamedSchemaRefE86eeb84b7e922c35cfb0031a6309f7b(BaseModel):
    dns: Optional[object] = None
    """Logging settings for DNS firewall."""

    http: Optional[object] = None
    """Logging settings for HTTP/HTTPS firewall."""

    l4: Optional[object] = None
    """Logging settings for Network firewall."""
