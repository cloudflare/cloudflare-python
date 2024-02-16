# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["CustomNCreateParams"]


class CustomNCreateParams(TypedDict, total=False):
    ns_name: Required[str]
    """The FQDN of the name server."""

    ns_set: float
    """The number of the set that this name server belongs to."""
