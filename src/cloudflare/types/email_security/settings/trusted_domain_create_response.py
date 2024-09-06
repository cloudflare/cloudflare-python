# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

from datetime import datetime

from typing_extensions import TypeAlias

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["TrustedDomainCreateResponse", "EmailSecurityTrustedDomain", "UnionMember1"]


class EmailSecurityTrustedDomain(BaseModel):
    id: int

    created_at: datetime

    is_recent: bool

    is_regex: bool

    is_similarity: bool

    last_modified: datetime

    pattern: str

    comments: Optional[str] = None


class UnionMember1(BaseModel):
    id: int

    created_at: datetime

    is_recent: bool

    is_regex: bool

    is_similarity: bool

    last_modified: datetime

    pattern: str

    comments: Optional[str] = None


TrustedDomainCreateResponse: TypeAlias = Union[EmailSecurityTrustedDomain, List[UnionMember1]]
