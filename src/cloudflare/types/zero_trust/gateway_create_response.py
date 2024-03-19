# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["GatewayCreateResponse"]


class GatewayCreateResponse(BaseModel):
    id: Optional[str] = None
    """Cloudflare account ID."""

    gateway_tag: Optional[str] = None
    """Gateway internal ID."""

    provider_name: Optional[str] = None
    """The name of the provider. Usually Cloudflare."""
