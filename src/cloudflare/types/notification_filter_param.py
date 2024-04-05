# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .filter_options_param import FilterOptionsParam

__all__ = ["NotificationFilterParam"]


class NotificationFilterParam(TypedDict, total=False):
    origin: Optional[FilterOptionsParam]
    """Filter options for a particular resource type (pool or origin).

    Use null to reset.
    """

    pool: Optional[FilterOptionsParam]
    """Filter options for a particular resource type (pool or origin).

    Use null to reset.
    """
