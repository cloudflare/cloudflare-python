# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["AlertingEditParams"]


class AlertingEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    enabled: Required[bool]
    """Whether CT alerting is enabled for the zone."""

    emails: SequenceNotStr[str]
    """Email addresses that receive CT alert notifications.

    Only present and configurable for Business and Enterprise zones. Maximum of 10
    addresses. For Free and Pro zones, notifications are sent to all users with SSL
    permissions on the zone.
    """
