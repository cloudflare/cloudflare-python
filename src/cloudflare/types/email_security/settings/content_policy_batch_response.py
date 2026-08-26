# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ContentPolicyBatchResponse", "Delete", "Patch", "Post", "Put"]


class Delete(BaseModel):
    id: str
    """Content policy identifier."""


class Patch(BaseModel):
    """A content policy pattern that matches against the subject or body of an email."""

    id: Optional[str] = None
    """Content policy identifier."""

    created_at: Optional[datetime] = None

    enabled: Optional[bool] = None

    modified_at: Optional[datetime] = None

    name: Optional[str] = None

    notes: Optional[str] = None

    pattern: Optional[str] = None

    targets: Optional[List[Literal["SUBJECT", "BODY"]]] = None


class Post(BaseModel):
    """A content policy pattern that matches against the subject or body of an email."""

    id: Optional[str] = None
    """Content policy identifier."""

    created_at: Optional[datetime] = None

    enabled: Optional[bool] = None

    modified_at: Optional[datetime] = None

    name: Optional[str] = None

    notes: Optional[str] = None

    pattern: Optional[str] = None

    targets: Optional[List[Literal["SUBJECT", "BODY"]]] = None


class Put(BaseModel):
    """A content policy pattern that matches against the subject or body of an email."""

    id: Optional[str] = None
    """Content policy identifier."""

    created_at: Optional[datetime] = None

    enabled: Optional[bool] = None

    modified_at: Optional[datetime] = None

    name: Optional[str] = None

    notes: Optional[str] = None

    pattern: Optional[str] = None

    targets: Optional[List[Literal["SUBJECT", "BODY"]]] = None


class ContentPolicyBatchResponse(BaseModel):
    deletes: Optional[List[Delete]] = None

    patches: Optional[List[Patch]] = None

    posts: Optional[List[Post]] = None

    puts: Optional[List[Put]] = None
