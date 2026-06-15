# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["IPSECTunnelPSKSetParams", "PSK"]


class IPSECTunnelPSKSetParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    psks: Required[Iterable[PSK]]
    """List of tunnel ID and PSK pairs."""

    validate_only: bool
    """If `true`, only run validation without persisting changes."""


class PSK(TypedDict, total=False):
    """A PSK entry for a specific IPsec tunnel."""

    id: Required[str]
    """The ID of the IPsec tunnel."""

    psk: Required[str]
    """A randomly generated or provided string for use in the IPsec tunnel."""
