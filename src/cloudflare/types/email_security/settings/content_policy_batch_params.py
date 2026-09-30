# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ContentPolicyBatchParams", "Delete", "Patch", "Post", "Put"]


class ContentPolicyBatchParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    deletes: Required[Iterable[Delete]]
    """IDs of the content policies to delete."""

    patches: Required[Iterable[Patch]]
    """
    Partial updates to apply — each entry carries the policy's ID and only the
    fields to change.
    """

    posts: Required[Iterable[Post]]
    """Content policies to create."""

    puts: Required[Iterable[Put]]
    """
    Full replacements to apply — each entry carries the policy's ID and every field
    of its new value.
    """


class Delete(TypedDict, total=False):
    id: Required[str]
    """Content policy identifier."""


class Patch(TypedDict, total=False):
    """A content policy pattern that matches against the subject or body of an email."""

    enabled: bool
    """Whether the policy is active."""

    name: str
    """Human-readable name of the policy."""

    notes: Optional[str]
    """Optional note describing the purpose of the policy."""

    pattern: str
    """Regular expression the policy matches against."""

    targets: List[Literal["SUBJECT", "BODY"]]
    """Parts of the email the pattern is matched against."""


class Post(TypedDict, total=False):
    """Create a content policy."""

    enabled: Required[bool]
    """Whether the policy is active."""

    name: Required[str]
    """Human-readable name of the policy."""

    pattern: Required[str]
    """Regular expression the policy matches against."""

    targets: Required[List[Literal["SUBJECT", "BODY"]]]
    """Parts of the email the pattern is matched against."""

    notes: Optional[str]
    """Optional note describing the purpose of the policy."""


class Put(TypedDict, total=False):
    """A content policy pattern that matches against the subject or body of an email."""

    enabled: Required[bool]
    """Whether the policy is active."""

    name: Required[str]
    """Human-readable name of the policy."""

    pattern: Required[str]
    """Regular expression the policy matches against."""

    targets: Required[List[Literal["SUBJECT", "BODY"]]]
    """Parts of the email the pattern is matched against."""

    notes: Optional[str]
    """Optional note describing the purpose of the policy."""
