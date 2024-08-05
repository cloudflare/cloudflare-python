# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from typing_extensions import Literal, TypeAlias

__all__ = ["WAFRule"]

WAFRule: TypeAlias = Dict[str, Literal["challenge", "block", "simulate", "disable", "default"]]
