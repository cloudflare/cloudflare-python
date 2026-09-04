# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ContentPolicyBatchParams", "Delete", "Patch", "Post", "Put"]


class ContentPolicyBatchParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    deletes: Required[Iterable[Delete]]

    patches: Required[Iterable[Patch]]

    posts: Required[Iterable[Post]]

    puts: Required[Iterable[Put]]


class Delete(TypedDict, total=False):
    id: Required[str]
    """Content policy identifier."""


class Patch(TypedDict, total=False):
    """A content policy pattern that matches against the subject or body of an email."""

    enabled: bool

    name: str

    notes: Optional[str]

    pattern: str

    targets: List[Literal["SUBJECT", "BODY"]]


class Post(TypedDict, total=False):
    """Create a content policy."""

    enabled: Required[bool]

    name: Required[str]

    pattern: Required[str]

    targets: Required[List[Literal["SUBJECT", "BODY"]]]

    notes: Optional[str]


class Put(TypedDict, total=False):
    """A content policy pattern that matches against the subject or body of an email."""

    enabled: Required[bool]

    name: Required[str]

    pattern: Required[str]

    targets: Required[List[Literal["SUBJECT", "BODY"]]]

    notes: Optional[str]
