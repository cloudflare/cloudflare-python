# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SiteUpdateParams", "Site", "SiteLocation"]


class SiteUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    site: Site


class SiteLocation(TypedDict, total=False):
    lat: str
    """Latitude"""

    lon: str
    """Longitude"""


class Site(TypedDict, total=False):
    connector_id: str
    """Magic WAN Connector identifier tag."""

    description: str

    location: SiteLocation
    """Location of site in latitude and longitude."""

    name: str
    """The name of the site."""

    secondary_connector_id: str
    """Magic WAN Connector identifier tag. Used when high availability mode is on."""
