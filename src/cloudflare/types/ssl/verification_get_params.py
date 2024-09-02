# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["VerificationGetParams"]


class VerificationGetParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    retry: Literal[True]
    """Immediately retry SSL Verification."""
