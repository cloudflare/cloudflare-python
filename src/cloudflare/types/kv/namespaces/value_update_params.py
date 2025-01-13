# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ValueUpdateParams"]


class ValueUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    namespace_id: Required[str]
    """Namespace identifier tag."""

    metadata: Required[str]
    """Arbitrary JSON to be associated with a key/value pair."""

    value: Required[str]
    """A byte sequence to be stored, up to 25 MiB in length."""

    expiration: float
    """
    The time, measured in number of seconds since the UNIX epoch, at which the key
    should expire.
    """

    expiration_ttl: float
    """The number of seconds for which the key should be visible before it expires.

    At least 60.
    """
