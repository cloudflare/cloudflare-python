# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ThreatEventBulkCreateParams", "Data", "DataRaw", "DataIndicator"]


class ThreatEventBulkCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID."""

    data: Required[Iterable[Data]]

    dataset_id: Required[Annotated[str, PropertyInfo(alias="datasetId")]]

    preserve_uuid: Annotated[bool, PropertyInfo(alias="preserveUuid")]
    """When true, use provided UUIDs from event data instead of generating new ones.

    Used for migration scenarios where original UUIDs must be preserved. Duplicate
    UUIDs will be skipped.
    """


class DataRaw(TypedDict, total=False):
    data: Required[Optional[Dict[str, object]]]

    source: str

    tlp: str


class DataIndicator(TypedDict, total=False):
    indicator_type: Required[Annotated[str, PropertyInfo(alias="indicatorType")]]
    """The type of indicator (e.g., DOMAIN, IP, JA3, HASH)"""

    value: Required[str]
    """The indicator value (e.g., domain name, IP address, hash)"""


class Data(TypedDict, total=False):
    category: Required[str]

    date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    event: Required[str]

    raw: Required[DataRaw]

    tlp: Required[str]

    account_id: Annotated[float, PropertyInfo(alias="accountId")]

    attacker: Optional[str]

    attacker_country: Annotated[str, PropertyInfo(alias="attackerCountry")]

    dataset_id: Annotated[str, PropertyInfo(alias="datasetId")]

    indicator: str

    indicators: Iterable[DataIndicator]
    """Array of indicators for this event.

    Supports multiple indicators per event for complex scenarios.
    """

    indicator_type: Annotated[str, PropertyInfo(alias="indicatorType")]

    insight: str

    tags: SequenceNotStr[str]

    target_country: Annotated[str, PropertyInfo(alias="targetCountry")]

    target_industry: Annotated[str, PropertyInfo(alias="targetIndustry")]

    uuid: str
    """Optional UUID for the event.

    Only used when preserveUuid=true in bulk create. Must be a valid UUID format.
    """
