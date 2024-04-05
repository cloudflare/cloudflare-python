# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import TypedDict

__all__ = ["MechanismsParam", "MechanismsParamItem"]


class MechanismsParamItem(TypedDict, total=False):
    id: Union[str, str]
    """UUID"""


MechanismsParam = Dict[str, Iterable[MechanismsParamItem]]
