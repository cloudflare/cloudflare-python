# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["MessageUpdateParams"]

class MessageUpdateParams(TypedDict, total=False):
    account_identifier: Required[str]
    """Identifier"""

    request_identifier: Required[str]
    """UUID"""

    content: str
    """Request content"""

    priority: str
    """Priority for analyzing the request"""

    request_type: str
    """Requested information from request"""

    summary: str
    """Brief description of the request"""

    tlp: Literal["clear", "amber", "amber-strict", "green", "red"]
    """The CISA defined Traffic Light Protocol (TLP)"""