# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CustomNCreateParams"]


class CustomNCreateParams(TypedDict, total=False):
    ns_name: Required[str]
    """The FQDN of the name server."""

    ns_set: float
    """The number of the set that this name server belongs to."""
