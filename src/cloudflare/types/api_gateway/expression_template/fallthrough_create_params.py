# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["FallthroughCreateParams"]


class FallthroughCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    hosts: Required[List[str]]
    """List of hosts to be targeted in the expression"""
