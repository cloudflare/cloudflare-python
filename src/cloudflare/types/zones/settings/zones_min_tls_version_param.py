# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ZonesMinTLSVersionParam"]


class ZonesMinTLSVersionParam(TypedDict, total=False):
    id: Required[Literal["min_tls_version"]]
    """ID of the zone setting."""

    value: Required[Literal["1.0", "1.1", "1.2", "1.3"]]
    """Current value of the zone setting."""
