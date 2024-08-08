# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel

__all__ = ["BlockSenderCreateResponse", "EmailSecurityBlockedSender", "UnionMember1"]


class EmailSecurityBlockedSender(BaseModel):
    id: int

    created_at: datetime

    is_regex: bool

    last_modified: datetime

    pattern: str

    pattern_type: Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"]

    comments: Optional[str] = None


class UnionMember1(BaseModel):
    id: int

    created_at: datetime

    is_regex: bool

    last_modified: datetime

    pattern: str

    pattern_type: Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"]

    comments: Optional[str] = None


BlockSenderCreateResponse: TypeAlias = Union[EmailSecurityBlockedSender, List[UnionMember1]]
