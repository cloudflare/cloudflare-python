# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, TypeAlias

from typing import Iterable, Dict

__all__ = ["MechanismParam", "MechanismParamItem"]


class MechanismParamItem(TypedDict, total=False):
    id: str
    """UUID"""


MechanismParam: TypeAlias = Dict[str, Iterable[MechanismParamItem]]
