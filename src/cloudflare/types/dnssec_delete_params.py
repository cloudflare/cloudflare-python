# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DNSSECDeleteParams"]


class DNSSECDeleteParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    body: Required[object]
