# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["NamespaceBulkUpdateParams", "Body"]


class NamespaceBulkUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    body: Required[Iterable[Body]]


class Body(TypedDict, total=False):
    key: Required[str]
    """A key's name.

    The name may be at most 512 bytes. All printable, non-whitespace characters are
    valid.
    """

    value: Required[str]
    """A UTF-8 encoded string to be stored, up to 25 MiB in length."""

    base64: bool
    """
    Indicates whether or not the server should base64 decode the value before
    storing it. Useful for writing values that wouldn't otherwise be valid JSON
    strings, such as images.
    """

    expiration: float
    """
    Expires the key at a certain time, measured in number of seconds since the UNIX
    epoch.
    """

    expiration_ttl: float
    """Expires the key after a number of seconds. Must be at least 60."""

    metadata: object
    """Arbitrary JSON that is associated with a key."""
