# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["HostnameUpdateParams", "Config"]


class HostnameUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    config: Required[Iterable[Config]]


class Config(TypedDict, total=False):
    cert_id: str
    """Certificate identifier tag."""

    enabled: Optional[bool]
    """Indicates whether hostname-level authenticated origin pulls is enabled.

    A null value voids the association.
    """

    hostname: str
    """
    The hostname on the origin for which the client certificate uploaded will be
    used.
    """
