# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import Optional

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["PrefixCreateParams"]

class PrefixCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    asn: Required[Optional[int]]
    """Autonomous System Number (ASN) the prefix will be advertised under."""

    cidr: Required[str]
    """IP Prefix in Classless Inter-Domain Routing format."""

    loa_document_id: Required[Optional[str]]
    """Identifier for the uploaded LOA document."""