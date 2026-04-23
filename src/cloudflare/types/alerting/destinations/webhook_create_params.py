# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WebhookCreateParams"]


class WebhookCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The account id"""

    name: Required[str]
    """The name of the webhook destination.

    This will be included in the request body when you receive a webhook
    notification.
    """

    url: Required[str]
    """The POST endpoint to call when dispatching a notification."""

    secret: str
    """
    Optional secret that will be passed in the `cf-webhook-auth` header when
    dispatching generic webhook notifications or formatted for supported
    destinations. Secrets are not returned in any API response body.
    """
