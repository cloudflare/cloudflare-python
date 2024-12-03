# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["IPGeolocation"]


class IPGeolocation(BaseModel):
    id: Optional[Literal["ip_geolocation"]] = None
    """
    Cloudflare adds a CF-IPCountry HTTP header containing the country code that
    corresponds to the visitor.
    """

    value: Optional[Literal["on", "off"]] = None
    """The status of adding the IP Geolocation Header."""
