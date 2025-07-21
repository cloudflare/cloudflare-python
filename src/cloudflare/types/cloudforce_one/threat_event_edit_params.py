# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ThreatEventEditParams", "Raw"]


class ThreatEventEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID."""

    attacker: str

    attacker_country: Annotated[str, PropertyInfo(alias="attackerCountry")]

    category: str

    date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    event: str

    indicator: str

    indicator_type: Annotated[str, PropertyInfo(alias="indicatorType")]

    insight: str

    raw: Raw

    target_country: Annotated[str, PropertyInfo(alias="targetCountry")]

    target_industry: Annotated[str, PropertyInfo(alias="targetIndustry")]

    tlp: str


class Raw(TypedDict, total=False):
    data: Optional[Dict[str, object]]

    source: str

    tlp: str
