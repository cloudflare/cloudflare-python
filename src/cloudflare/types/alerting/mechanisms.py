# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union

from ..._models import BaseModel

__all__ = ["Mechanisms", "MechanismsItem"]


class MechanismsItem(BaseModel):
    id: Union[str, str, None] = None
    """UUID"""


Mechanisms = Dict[str, List[MechanismsItem]]
