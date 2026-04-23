# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["WebhookUpdateParams"]


class WebhookUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    body_notification_url_1: Annotated[str, PropertyInfo(alias="notification_url")]
    """The URL where webhooks will be sent."""

    body_notification_url_2: Annotated[str, PropertyInfo(alias="notificationUrl")]
    """The URL where webhooks will be sent."""
