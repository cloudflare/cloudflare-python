# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["GroupEditParams"]


class GroupEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    package_id: Required[str]
    """The unique identifier of a WAF package."""

    mode: Literal["on", "off"]
    """The state of the rules contained in the rule group.

    When `on`, the rules in the group are configurable/usable.
    """
