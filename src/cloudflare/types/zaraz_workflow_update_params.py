# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Literal, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["ZarazWorkflowUpdateParams"]


class ZarazWorkflowUpdateParams(TypedDict, total=False):
    body: Required[Literal["realtime", "preview"]]
    """Zaraz workflow"""
