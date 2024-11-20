# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PoolBulkEditParams"]


class PoolBulkEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    notification_email: Literal[""]
    """The email address to send health status notifications to.

    This field is now deprecated in favor of Cloudflare Notifications for Load
    Balancing, so only resetting this field with an empty string `""` is accepted.
    """
