# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["NamespaceBulkUpdateParams", "Body"]


class NamespaceBulkUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    body: Required[Iterable[Body]]


class Body(TypedDict, total=False):
    base64: bool
    """Whether or not the server should base64 decode the value before storing it.

    Useful for writing values that wouldn't otherwise be valid JSON strings, such as
    images.
    """

    expiration: float
    """
    The time, measured in number of seconds since the UNIX epoch, at which the key
    should expire.
    """

    expiration_ttl: float
    """The number of seconds for which the key should be visible before it expires.

    At least 60.
    """

    key: str
    """A key's name.

    The name may be at most 512 bytes. All printable, non-whitespace characters are
    valid.
    """

    metadata: Dict[str, object]
    """Arbitrary JSON that is associated with a key."""

    value: str
    """A UTF-8 encoded string to be stored, up to 25 MiB in length."""
