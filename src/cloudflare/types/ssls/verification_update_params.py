# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["VerificationUpdateParams"]


class VerificationUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    validation_method: Required[Literal["http", "cname", "txt", "email"]]
    """Desired validation method."""
