# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["GroupEditParams"]


class GroupEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Defines an identifier of a schema."""

    package_id: Required[str]
    """Defines the unique identifier of a WAF package."""

    mode: Literal["on", "off"]
    """Defines the state of the rules contained in the rule group.

    When `on`, the rules in the group are configurable/usable.
    """
