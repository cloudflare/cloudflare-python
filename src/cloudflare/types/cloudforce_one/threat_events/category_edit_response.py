# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["CategoryEditResponse"]


class CategoryEditResponse(BaseModel):
    kill_chain: float = FieldInfo(alias="killChain")

    name: str

    uuid: str

    mitre_attack: Optional[List[str]] = FieldInfo(alias="mitreAttack", default=None)

    shortname: Optional[str] = None
