# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .site_location_param import SiteLocationParam

__all__ = ["SiteCreateParams"]


class SiteCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    name: Required[str]
    """The name of the site."""

    connector_id: str
    """Magic Connector identifier tag."""

    description: str

    ha_mode: bool
    """Site high availability mode.

    If set to true, the site can have two connectors and runs in high availability
    mode.
    """

    location: SiteLocationParam
    """Location of site in latitude and longitude."""

    secondary_connector_id: str
    """Magic Connector identifier tag. Used when high availability mode is on."""
