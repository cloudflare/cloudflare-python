# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CustomNameserverUpdateParams"]


class CustomNameserverUpdateParams(TypedDict, total=False):
    enabled: bool
    """Whether zone uses account-level custom nameservers."""

    ns_set: float
    """The number of the name server set to assign to the zone."""
