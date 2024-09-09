# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["Mechanism", "MechanismItem"]


class MechanismItem(BaseModel):
    id: Optional[str] = None
    """UUID"""


Mechanism: TypeAlias = Dict[str, List[MechanismItem]]
