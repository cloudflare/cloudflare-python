# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AgentReadinessSummaryResponse", "Meta", "MetaDomainCategory", "MetaUnit"]


class MetaDomainCategory(BaseModel):
    name: str
    """Sub-category name."""

    value: int
    """Number of successfully scanned domains in this sub-category."""


class MetaUnit(BaseModel):
    name: str

    value: str


class Meta(BaseModel):
    date: str
    """Date of the returned scan (YYYY-MM-DD).

    May differ from the requested date if no scan exists for that exact date.
    """

    domain_categories: List[MetaDomainCategory] = FieldInfo(alias="domainCategories")
    """Available domain sub-categories with their scan counts.

    Use as filter options for the domainCategory parameter.
    """

    last_updated: datetime = FieldInfo(alias="lastUpdated")
    """Timestamp of the last dataset update."""

    normalization: Literal[
        "PERCENTAGE",
        "MIN0_MAX",
        "MIN_MAX",
        "RAW_VALUES",
        "PERCENTAGE_CHANGE",
        "ROLLING_AVERAGE",
        "OVERLAPPED_PERCENTAGE",
        "RATIO",
    ]
    """Normalization method applied to the results.

    Refer to
    [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).
    """

    successful_domains: int = FieldInfo(alias="successfulDomains")
    """Domains successfully scanned (excludes errors)."""

    total_domains: int = FieldInfo(alias="totalDomains")
    """Total domains attempted in the scan."""

    units: List[MetaUnit]
    """Measurement units for the results."""


class AgentReadinessSummaryResponse(BaseModel):
    meta: Meta

    summary_0: Dict[str, str]
