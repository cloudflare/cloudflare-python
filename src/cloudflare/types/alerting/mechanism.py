# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, List

from typing_extensions import TypeAlias

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Mechanism", "MechanismItem"]


class MechanismItem(BaseModel):
    id: Optional[str] = None
    """UUID"""


Mechanism: TypeAlias = Dict[str, List[MechanismItem]]
