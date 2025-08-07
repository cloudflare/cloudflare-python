# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ValueUpdateParams"]


class ValueUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    namespace_id: Required[str]
    """Namespace identifier tag."""

    value: Required[str]
    """A byte sequence to be stored, up to 25 MiB in length."""

    expiration: float
    """
    Expires the key at a certain time, measured in number of seconds since the UNIX
    epoch.
    """

    expiration_ttl: float
    """Expires the key after a number of seconds. Must be at least 60."""

    metadata: object
    """Associates arbitrary JSON data with a key/value pair."""
