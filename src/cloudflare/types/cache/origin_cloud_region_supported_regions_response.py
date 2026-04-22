# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from ..._models import BaseModel

__all__ = ["OriginCloudRegionSupportedRegionsResponse", "Vendor"]


class Vendor(BaseModel):
    """
    A single supported cloud region with associated Tiered Cache upper-tier colocations.
    """

    name: str
    """Cloud vendor region identifier."""

    upper_tier_colos: List[str]
    """
    Cloudflare Tiered Cache upper-tier colocation codes co-located with this cloud
    region. Requests from zones with a matching origin mapping will be routed
    through these colos.
    """


class OriginCloudRegionSupportedRegionsResponse(BaseModel):
    """Cloud vendors and their supported regions for origin cloud region mappings."""

    obtained_codes: bool
    """
    Whether Cloudflare airport codes (IATA colo identifiers) were successfully
    resolved for the `upper_tier_colos` field on each region. When `false`, the
    `upper_tier_colos` arrays may be empty or incomplete.
    """

    vendors: Dict[str, List[Vendor]]
    """Map of vendor name to list of supported regions."""
