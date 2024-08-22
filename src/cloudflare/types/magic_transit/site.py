# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from .site_location import SiteLocation

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Site"]

class Site(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    connector_id: Optional[str] = None
    """Magic Connector identifier tag."""

    description: Optional[str] = None

    ha_mode: Optional[bool] = None
    """Site high availability mode.

    If set to true, the site can have two connectors and runs in high availability
    mode.
    """

    location: Optional[SiteLocation] = None
    """Location of site in latitude and longitude."""

    name: Optional[str] = None
    """The name of the site."""

    secondary_connector_id: Optional[str] = None
    """Magic Connector identifier tag. Used when high availability mode is on."""