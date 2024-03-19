# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SiteDeleteResponse", "DeletedSite", "DeletedSiteLocation"]


class DeletedSiteLocation(BaseModel):
    lat: Optional[str] = None
    """Latitude"""

    lon: Optional[str] = None
    """Longitude"""


class DeletedSite(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    connector_id: Optional[str] = None
    """Magic WAN Connector identifier tag."""

    description: Optional[str] = None

    ha_mode: Optional[bool] = None
    """Site high availability mode.

    If set to true, the site can have two connectors and runs in high availability
    mode.
    """

    location: Optional[DeletedSiteLocation] = None
    """Location of site in latitude and longitude."""

    name: Optional[str] = None
    """The name of the site."""

    secondary_connector_id: Optional[str] = None
    """Magic WAN Connector identifier tag. Used when high availability mode is on."""


class SiteDeleteResponse(BaseModel):
    deleted: Optional[bool] = None

    deleted_site: Optional[DeletedSite] = None
