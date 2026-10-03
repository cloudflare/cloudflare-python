# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["TrustedDomainBatchParams", "Delete", "Patch", "Post", "Put"]


class TrustedDomainBatchParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    deletes: Required[Iterable[Delete]]
    """IDs of the trusted domain patterns to delete."""

    patches: Required[Iterable[Patch]]
    """
    Partial updates to apply — each entry carries the pattern's ID and only the
    fields to change.
    """

    posts: Required[Iterable[Post]]
    """Trusted domain patterns to create."""

    puts: Required[Iterable[Put]]
    """
    Full replacements to apply — each entry carries the pattern's ID and every field
    of its new value.
    """


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
    """Whether `pattern` is a regular expression instead of a literal domain."""

    is_similarity: bool
    """
    Select for partner or other approved domains that have similar spelling to your
    connected domains. Prevents listed domains from triggering a Spoof disposition.
    """

    pattern: str
    """The domain pattern to trust, e.g. `example.com`."""


class Post(TypedDict, total=False):
    """Create a trusted domain."""

    is_recent: Required[bool]
    """
    Select to prevent recently registered domains from triggering a Suspicious or
    Malicious disposition.
    """

    is_regex: Required[bool]
    """Whether `pattern` is a regular expression instead of a literal domain."""

    is_similarity: Required[bool]
    """
    Select for partner or other approved domains that have similar spelling to your
    connected domains. Prevents listed domains from triggering a Spoof disposition.
    """

    pattern: Required[str]
    """The domain pattern to trust, e.g. `example.com`."""

    comments: Optional[str]


class Put(TypedDict, total=False):
    """A trusted email domain."""

    is_recent: Required[bool]
    """
    Select to prevent recently registered domains from triggering a Suspicious or
    Malicious disposition.
    """

    is_regex: Required[bool]
    """Whether `pattern` is a regular expression instead of a literal domain."""

    is_similarity: Required[bool]
    """
    Select for partner or other approved domains that have similar spelling to your
    connected domains. Prevents listed domains from triggering a Spoof disposition.
    """

    pattern: Required[str]
    """The domain pattern to trust, e.g. `example.com`."""

    comments: Optional[str]
