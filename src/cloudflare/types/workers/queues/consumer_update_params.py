# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo
from ....types import shared_params

__all__ = ["ConsumerUpdateParams"]


class ConsumerUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    name: Required[str]

    body: Required[object]
