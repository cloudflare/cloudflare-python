# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["TrustedDomainBatchParams", "Delete", "Patch", "Post", "Put"]


class TrustedDomainBatchParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    deletes: Required[Iterable[Delete]]

    patches: Required[Iterable[Patch]]

    posts: Required[Iterable[Post]]

    puts: Required[Iterable[Put]]


class Delete(TypedDict, total=False):
    id: Required[str]
    """Trusted domain identifier."""


class Patch(TypedDict, total=False):
    """A trusted email domain."""

    comments: Optional[str]

    is_recent: bool
    """
    Select to prevent recently registered domains from triggering a Suspicious or
    Malicious disposition.
    """

    is_regex: bool

    is_similarity: bool
    """
    Select for partner or other approved domains that have similar spelling to your
    connected domains. Prevents listed domains from triggering a Spoof disposition.
    """

    pattern: str


class Post(TypedDict, total=False):
    """Create a trusted domain."""

    is_recent: Required[bool]
    """
    Select to prevent recently registered domains from triggering a Suspicious or
    Malicious disposition.
    """

    is_regex: Required[bool]

    is_similarity: Required[bool]
    """
    Select for partner or other approved domains that have similar spelling to your
    connected domains. Prevents listed domains from triggering a Spoof disposition.
    """

    pattern: Required[str]

    comments: Optional[str]


class Put(TypedDict, total=False):
    """A trusted email domain."""

    is_recent: Required[bool]
    """
    Select to prevent recently registered domains from triggering a Suspicious or
    Malicious disposition.
    """

    is_regex: Required[bool]

    is_similarity: Required[bool]
    """
    Select for partner or other approved domains that have similar spelling to your
    connected domains. Prevents listed domains from triggering a Spoof disposition.
    """

    pattern: Required[str]

    comments: Optional[str]
