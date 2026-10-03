# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypedDict

from ...._types import FileTypes

__all__ = ["ValueUpdateParams"]


class ValueUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """ID of the Cloudflare account that owns the Workers KV namespaces."""

    namespace_id: Required[str]
    """ID of the Workers KV namespace."""

    value: Required[Union[str, FileTypes]]
    """A byte sequence to be stored, up to 25 MiB in length."""

    expiration: float
    """
    Expires the key at a certain time, measured in number of seconds since the UNIX
    epoch.
    """

    expiration_ttl: float
    """Number of seconds until the key expires.

    Must be at least 60. Takes precedence over `expiration` when both are specified.
    """

    metadata: object
    """Associates arbitrary JSON data with a key/value pair."""
