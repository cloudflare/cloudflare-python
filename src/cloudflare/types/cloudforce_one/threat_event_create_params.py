# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ThreatEventCreateParams", "Raw"]


class ThreatEventCreateParams(TypedDict, total=False):
    path_account_id: Required[Annotated[float, PropertyInfo(alias="account_id")]]
    """Account ID"""

    attacker: Required[str]

    attacker_country: Required[Annotated[str, PropertyInfo(alias="attackerCountry")]]

    category: Required[str]

    date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    event: Required[str]

    indicator_type: Required[Annotated[str, PropertyInfo(alias="indicatorType")]]

    raw: Required[Raw]

    tlp: Required[str]

    body_account_id: Annotated[float, PropertyInfo(alias="accountId")]

    dataset_id: Annotated[str, PropertyInfo(alias="datasetId")]

    indicator: str

    tags: List[str]

    target_country: Annotated[str, PropertyInfo(alias="targetCountry")]

    target_industry: Annotated[str, PropertyInfo(alias="targetIndustry")]


class Raw(TypedDict, total=False):
    data: object

    source: str

    tlp: str
