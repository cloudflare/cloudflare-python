# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .zones_h2_prioritization_param import ZonesH2PrioritizationParam

__all__ = ["H2PrioritizationEditParams"]


class H2PrioritizationEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    value: Required[ZonesH2PrioritizationParam]
    """
    HTTP/2 Edge Prioritization optimises the delivery of resources served through
    HTTP/2 to improve page load performance. It also supports fine control of
    content delivery when used in conjunction with Workers.
    """
