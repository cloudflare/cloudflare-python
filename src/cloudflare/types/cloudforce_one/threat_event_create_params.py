# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ThreatEventCreateParams", "Raw", "Indicator"]


class ThreatEventCreateParams(TypedDict, total=False):
    path_account_id: Required[Annotated[str, PropertyInfo(alias="account_id")]]
    """Account ID."""

    category: Required[str]

    date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    event: Required[str]

    raw: Required[Raw]

    tlp: Required[str]

    body_account_id: Annotated[float, PropertyInfo(alias="accountId")]

    attacker: Optional[str]

    attacker_country: Annotated[str, PropertyInfo(alias="attackerCountry")]

    dataset_id: Annotated[str, PropertyInfo(alias="datasetId")]

    indicator: str

    indicators: Iterable[Indicator]
    """Array of indicators for this event.

    Supports multiple indicators per event for complex scenarios.
    """

    indicator_type: Annotated[str, PropertyInfo(alias="indicatorType")]

    insight: str

    tags: SequenceNotStr[str]

    target_country: Annotated[str, PropertyInfo(alias="targetCountry")]

    target_industry: Annotated[str, PropertyInfo(alias="targetIndustry")]


class Raw(TypedDict, total=False):
    data: Required[Optional[Dict[str, object]]]

    source: str

    tlp: str


class Indicator(TypedDict, total=False):
    indicator_type: Required[Annotated[str, PropertyInfo(alias="indicatorType")]]
    """The type of indicator (e.g., DOMAIN, IP, JA3, HASH)"""

    value: Required[str]
    """The indicator value (e.g., domain name, IP address, hash)"""
