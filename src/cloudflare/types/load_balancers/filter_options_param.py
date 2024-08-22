# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["FilterOptionsParam"]


class FilterOptionsParam(TypedDict, total=False):
    disable: bool
    """If set true, disable notifications for this type of resource (pool or origin)."""

    healthy: Optional[bool]
    """If present, send notifications only for this health status (e.g.

    false for only DOWN events). Use null to reset (all events).
    """
