# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ....._models import BaseModel

__all__ = ["WebhookCreateResponse"]


class WebhookCreateResponse(BaseModel):
    id: Optional[str] = None
    """UUID"""
