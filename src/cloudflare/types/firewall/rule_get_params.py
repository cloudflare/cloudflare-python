# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RuleGetParams"]


class RuleGetParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: str
    """The unique identifier of the firewall rule."""
