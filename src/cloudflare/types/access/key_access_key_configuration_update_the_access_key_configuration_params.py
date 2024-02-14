# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["KeyAccessKeyConfigurationUpdateTheAccessKeyConfigurationParams"]


class KeyAccessKeyConfigurationUpdateTheAccessKeyConfigurationParams(TypedDict, total=False):
    key_rotation_interval_days: Required[float]
    """The number of days between key rotations."""
