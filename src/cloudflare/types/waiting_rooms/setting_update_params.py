# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SettingUpdateParams"]


class SettingUpdateParams(TypedDict, total=False):
    search_engine_crawler_bypass: bool
    """
    Whether to allow verified search engine crawlers to bypass all waiting rooms on
    this zone. Verified search engine crawlers will not be tracked or counted by the
    waiting room system, and will not appear in waiting room analytics.
    """
