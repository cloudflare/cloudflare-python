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
    """Email addresses that receive CT alert notifications for the zone.

    A maximum of 100 addresses may be configured. Each address must be a valid RFC
    5322 email address and must not contain a comma.
    """
