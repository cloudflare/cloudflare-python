# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ....._types import FileTypes
from ....._utils import PropertyInfo
from .....types import shared_params

__all__ = ["WebhookNotificationWebhooksCreateAWebhookParams"]


class WebhookNotificationWebhooksCreateAWebhookParams(TypedDict, total=False):
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
