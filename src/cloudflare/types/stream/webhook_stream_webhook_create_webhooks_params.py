# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated, Required

from ..._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["WebhookStreamWebhookCreateWebhooksParams"]


class WebhookStreamWebhookCreateWebhooksParams(TypedDict, total=False):
    notification_url: Required[Annotated[str, PropertyInfo(alias="notificationUrl")]]
    """The URL where webhooks will be sent."""
