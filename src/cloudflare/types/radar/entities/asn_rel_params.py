# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo
from ....types import shared_params

__all__ = ["AsnRelParams"]


class AsnRelParams(TypedDict, total=False):
    asn2: int
    """Get the AS relationship of ASN2 with respect to the given ASN"""

    format: Literal["JSON", "CSV"]
    """Format results are returned in."""
