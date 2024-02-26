# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["H2PrioritizationEditParams", "Value"]


class H2PrioritizationEditParams(TypedDict, total=False):
    value: Required[Value]
    """
    HTTP/2 Edge Prioritization optimises the delivery of resources served through
    HTTP/2 to improve page load performance. It also supports fine control of
    content delivery when used in conjunction with Workers.
    """


class Value(TypedDict, total=False):
    id: Required[Literal["h2_prioritization"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off", "custom"]]
    """Current value of the zone setting."""
