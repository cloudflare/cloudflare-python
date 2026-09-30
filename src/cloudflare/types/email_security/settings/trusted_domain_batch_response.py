# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["TrustedDomainBatchResponse", "Delete", "Patch", "Post", "Put"]


class Delete(BaseModel):
    id: str
    """Trusted domain identifier."""


class Patch(BaseModel):
    """A trusted email domain."""

    id: Optional[str] = None
    """Trusted domain identifier."""

    comments: Optional[str] = None

    created_at: Optional[datetime] = None

    is_recent: Optional[bool] = None
    """
    Select to prevent recently registered domains from triggering a Suspicious or
    Malicious disposition.
    """

    is_regex: Optional[bool] = None
    """Whether `pattern` is a regular expression instead of a literal domain."""

    is_similarity: Optional[bool] = None
    """
    Select for partner or other approved domains that have similar spelling to your
    connected domains. Prevents listed domains from triggering a Spoof disposition.
    """

    last_modified: Optional[datetime] = None
    """Deprecated, use `modified_at` instead. End of life: November 1, 2026."""

    modified_at: Optional[datetime] = None

    pattern: Optional[str] = None
    """The domain pattern to trust, e.g. `example.com`."""


class Post(BaseModel):
    """A trusted email domain."""

    id: Optional[str] = None
    """Trusted domain identifier."""

    comments: Optional[str] = None

    created_at: Optional[datetime] = None

    is_recent: Optional[bool] = None
    """
    Select to prevent recently registered domains from triggering a Suspicious or
    Malicious disposition.
    """

    is_regex: Optional[bool] = None
    """Whether `pattern` is a regular expression instead of a literal domain."""

    is_similarity: Optional[bool] = None
    """
    Select for partner or other approved domains that have similar spelling to your
    connected domains. Prevents listed domains from triggering a Spoof disposition.
    """

    last_modified: Optional[datetime] = None
    """Deprecated, use `modified_at` instead. End of life: November 1, 2026."""

    modified_at: Optional[datetime] = None

    pattern: Optional[str] = None
    """The domain pattern to trust, e.g. `example.com`."""


class Put(BaseModel):
    """A trusted email domain."""

    id: Optional[str] = None
    """Trusted domain identifier."""

    comments: Optional[str] = None

    created_at: Optional[datetime] = None

    is_recent: Optional[bool] = None
    """
    Select to prevent recently registered domains from triggering a Suspicious or
    Malicious disposition.
    """

    is_regex: Optional[bool] = None
    """Whether `pattern` is a regular expression instead of a literal domain."""

    is_similarity: Optional[bool] = None
    """
    Select for partner or other approved domains that have similar spelling to your
    connected domains. Prevents listed domains from triggering a Spoof disposition.
    """

    last_modified: Optional[datetime] = None
    """Deprecated, use `modified_at` instead. End of life: November 1, 2026."""

    modified_at: Optional[datetime] = None

    pattern: Optional[str] = None
    """The domain pattern to trust, e.g. `example.com`."""


class TrustedDomainBatchResponse(BaseModel):
    deletes: Optional[List[Delete]] = None

    patches: Optional[List[Patch]] = None

    posts: Optional[List[Post]] = None

    puts: Optional[List[Put]] = None
