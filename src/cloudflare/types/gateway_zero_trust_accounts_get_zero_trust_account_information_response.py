# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from .._models import BaseModel
from ..types import shared

__all__ = ["GatewayZeroTrustAccountsGetZeroTrustAccountInformationResponse"]


class GatewayZeroTrustAccountsGetZeroTrustAccountInformationResponse(BaseModel):
    id: Optional[str] = None
    """Cloudflare account ID."""

    gateway_tag: Optional[str] = None
    """Gateway internal ID."""

    provider_name: Optional[str] = None
    """The name of the provider. Usually Cloudflare."""
