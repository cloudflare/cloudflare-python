# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ThreatEventCreateResponse"]


class ThreatEventCreateResponse(BaseModel):
    attacker: str

    attacker_country: str = FieldInfo(alias="attackerCountry")

    category: str

    date: str

    event: str

    indicator_type: str = FieldInfo(alias="indicatorType")

    kill_chain: float = FieldInfo(alias="killChain")

    mitre_attack: List[str] = FieldInfo(alias="mitreAttack")

    num_referenced: float = FieldInfo(alias="numReferenced")

    num_references: float = FieldInfo(alias="numReferences")

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
