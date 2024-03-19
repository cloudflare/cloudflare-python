# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SiteCreateParams", "Site", "SiteLocation"]


class SiteCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    site: Site


class SiteLocation(TypedDict, total=False):
    lat: str
    """Latitude"""

    lon: str
    """Longitude"""


class Site(TypedDict, total=False):
    name: Required[str]
    """The name of the site."""

    connector_id: str
    """Magic WAN Connector identifier tag."""

    description: str

    ha_mode: bool
    """Site high availability mode.

    If set to true, the site can have two connectors and runs in high availability
    mode.
    """

    location: SiteLocation
    """Location of site in latitude and longitude."""

    secondary_connector_id: str
    """Magic WAN Connector identifier tag. Used when high availability mode is on."""
