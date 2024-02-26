# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["ExcludeUpdateParams", "Body"]


class ExcludeUpdateParams(TypedDict, total=False):
    body: Required[Iterable[Body]]


class Body(TypedDict, total=False):
    address: Required[str]
    """The address in CIDR format to exclude from the tunnel.

    If `address` is present, `host` must not be present.
    """

    description: Required[str]
    """A description of the Split Tunnel item, displayed in the client UI."""

    host: str
    """The domain name to exclude from the tunnel.

    If `host` is present, `address` must not be present.
    """
