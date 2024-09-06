# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["WAFRule"]

WAFRule: TypeAlias = Dict[str, Literal["challenge", "block", "simulate", "disable", "default"]]
