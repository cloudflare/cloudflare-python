# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TrueClientIPHeader"]


class TrueClientIPHeader(BaseModel):
    id: Optional[Literal["true_client_ip_header"]] = None
    """Turn on or off the True-Client-IP Header feature of the Cloudflare Network app."""

    value: Optional[Literal["on", "off"]] = None
    """The status of True Client IP Header."""
