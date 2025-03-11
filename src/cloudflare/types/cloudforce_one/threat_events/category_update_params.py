# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CategoryUpdateParams"]


class CategoryUpdateParams(TypedDict, total=False):
    account_id: Required[Annotated[float, PropertyInfo(alias="accountId")]]
    """Account ID"""

    kill_chain: Annotated[float, PropertyInfo(alias="killChain")]

    mitre_attack: Annotated[List[str], PropertyInfo(alias="mitreAttack")]

    name: str

    shortname: str
