# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .site_location_param import SiteLocationParam

__all__ = ["SiteUpdateParams"]


class SiteUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    connector_id: str
    """Magic Connector identifier tag."""

    description: str

    location: SiteLocationParam
    """Location of site in latitude and longitude."""

    name: str
    """The name of the site."""

    secondary_connector_id: str
    """Magic Connector identifier tag. Used when high availability mode is on."""
