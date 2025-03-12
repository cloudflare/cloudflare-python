# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ThreatEventEditParams"]


class ThreatEventEditParams(TypedDict, total=False):
    account_id: Required[float]
    """Account ID"""

    attacker: str

    attacker_country: Annotated[str, PropertyInfo(alias="attackerCountry")]

    category: str

    date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    event: str

    indicator: str

    indicator_type: Annotated[str, PropertyInfo(alias="indicatorType")]

    target_country: Annotated[str, PropertyInfo(alias="targetCountry")]

    target_industry: Annotated[str, PropertyInfo(alias="targetIndustry")]

    tlp: str
