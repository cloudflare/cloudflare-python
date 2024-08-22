# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

from datetime import datetime

from typing_extensions import Literal, TypeAlias

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["AllowPatternCreateResponse", "EmailSecurityAllowPattern", "UnionMember1"]

class EmailSecurityAllowPattern(BaseModel):
    id: int

    created_at: datetime

    is_recipient: bool

    is_regex: bool

    is_sender: bool

    is_spoof: bool

    last_modified: datetime

    pattern: str

    pattern_type: Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"]

    verify_sender: bool

    comments: Optional[str] = None

class UnionMember1(BaseModel):
    id: int

    created_at: datetime

    is_recipient: bool

    is_regex: bool

    is_sender: bool

    is_spoof: bool

    last_modified: datetime

    pattern: str

    pattern_type: Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"]

    verify_sender: bool

    comments: Optional[str] = None

AllowPatternCreateResponse: TypeAlias = Union[EmailSecurityAllowPattern, List[UnionMember1]]