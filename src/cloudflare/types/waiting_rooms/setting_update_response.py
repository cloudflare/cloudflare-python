# File generated from our OpenAPI spec by Stainless.

from ..._models import BaseModel

__all__ = ["SettingUpdateResponse"]


class SettingUpdateResponse(BaseModel):
    search_engine_crawler_bypass: bool
    """
    Whether to allow verified search engine crawlers to bypass all waiting rooms on
    this zone. Verified search engine crawlers will not be tracked or counted by the
    waiting room system, and will not appear in waiting room analytics.
    """
