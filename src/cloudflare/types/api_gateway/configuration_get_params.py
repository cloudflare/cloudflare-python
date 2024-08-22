# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ConfigurationGetParams"]


class ConfigurationGetParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    properties: List[Literal["auth_id_characteristics"]]
    """Requests information about certain properties."""
