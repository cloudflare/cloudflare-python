# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["KeyUpdateParams"]


class KeyUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    key_rotation_interval_days: Required[float]
    """The number of days between key rotations."""
