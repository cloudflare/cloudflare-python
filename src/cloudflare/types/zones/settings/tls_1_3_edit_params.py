# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TLS1_3EditParams"]


class TLS1_3EditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    value: Required[Literal["on", "off", "zrt"]]
    """
    Value of the zone setting. Notes: Default value depends on the zone's plan
    level.
    """
