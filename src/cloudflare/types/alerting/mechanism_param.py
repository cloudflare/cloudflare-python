# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import TypedDict

__all__ = ["MechanismParam", "MechanismParamItem"]


class MechanismParamItem(TypedDict, total=False):
    id: Union[str, str]
    """UUID"""


MechanismParam = Dict[str, Iterable[MechanismParamItem]]
