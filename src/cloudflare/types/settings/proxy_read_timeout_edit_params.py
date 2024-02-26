# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ProxyReadTimeoutEditParams", "Value"]


class ProxyReadTimeoutEditParams(TypedDict, total=False):
    value: Required[Value]
    """Maximum time between two read operations from origin."""


class Value(TypedDict, total=False):
    id: Required[Literal["proxy_read_timeout"]]
    """ID of the zone setting."""

    value: Required[float]
    """Current value of the zone setting."""
