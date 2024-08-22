# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["GatewayListResponse"]

class GatewayListResponse(BaseModel):
    id: Optional[str] = None
    """Cloudflare account ID."""

    gateway_tag: Optional[str] = None
    """Gateway internal ID."""

    provider_name: Optional[str] = None
    """The name of the provider. Usually Cloudflare."""