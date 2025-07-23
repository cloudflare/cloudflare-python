# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["EndpointHealthcheckUpdateResponse"]


class EndpointHealthcheckUpdateResponse(BaseModel):
    check_type: Literal["icmp"]
    """type of check to perform"""

    endpoint: str
    """the IP address of the host to perform checks against"""

    id: Optional[str] = None
    """UUID."""

    name: Optional[str] = None
    """Optional name associated with this check"""
