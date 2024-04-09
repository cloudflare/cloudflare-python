# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union

from ..._models import BaseModel

__all__ = ["Mechanism", "MechanismItem"]


class MechanismItem(BaseModel):
    id: Union[str, str, None] = None
    """UUID"""


Mechanism = Dict[str, List[MechanismItem]]
