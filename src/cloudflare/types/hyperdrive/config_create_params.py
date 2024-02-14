# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["ConfigCreateParams"]


class ConfigCreateParams(TypedDict, total=False):
    password: Required[str]
    """The password required to access your origin database.

    This value is write-only and never returned by the API.
    """
