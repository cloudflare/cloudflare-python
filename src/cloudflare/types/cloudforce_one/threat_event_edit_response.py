# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ThreatEventEditResponse"]


class ThreatEventEditResponse(BaseModel):
    id: float

    account_id: float = FieldInfo(alias="accountId")

    attacker: str

    attacker_country: str = FieldInfo(alias="attackerCountry")

    category: str

    category_id: float = FieldInfo(alias="categoryId")

    date: str

    event: str

    indicator: str

    indicator_type: str = FieldInfo(alias="indicatorType")

    indicator_type_id: float = FieldInfo(alias="indicatorTypeId")

    kill_chain: float = FieldInfo(alias="killChain")

    mitre_attack: List[str] = FieldInfo(alias="mitreAttack")

    num_referenced: float = FieldInfo(alias="numReferenced")

    num_references: float = FieldInfo(alias="numReferences")

    raw_id: str = FieldInfo(alias="rawId")

    referenced: List[str]

    referenced_ids: List[float] = FieldInfo(alias="referencedIds")

    references: List[str]

    references_ids: List[float] = FieldInfo(alias="referencesIds")

    tags: List[str]

    target_country: str = FieldInfo(alias="targetCountry")

    target_industry: str = FieldInfo(alias="targetIndustry")

    tlp: str

    uuid: str

    insight: Optional[str] = None

    releasability_id: Optional[str] = FieldInfo(alias="releasabilityId", default=None)
