# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Literal, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["TrueClientIPHeaderUpdateParams"]


class TrueClientIPHeaderUpdateParams(TypedDict, total=False):
    value: Required[Literal["on", "off"]]
    """Value of the zone setting."""
