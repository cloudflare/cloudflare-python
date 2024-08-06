# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import TypeAlias, TypedDict

__all__ = ["MechanismParam", "MechanismParamItem"]


class MechanismParamItem(TypedDict, total=False):
    id: str
    """UUID"""


MechanismParam: TypeAlias = Dict[str, Iterable[MechanismParamItem]]
