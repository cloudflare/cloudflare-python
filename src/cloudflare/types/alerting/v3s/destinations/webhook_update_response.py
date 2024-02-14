# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ....._models import BaseModel

__all__ = ["WebhookUpdateResponse"]


class WebhookUpdateResponse(BaseModel):
    id: Optional[str] = None
    """UUID"""
