# File generated from our OpenAPI spec by Stainless.

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["WaitingroomZoneSettingsResponse", "Result"]


class Result(BaseModel):
    search_engine_crawler_bypass: bool
    """
    Whether to allow verified search engine crawlers to bypass all waiting rooms on
    this zone. Verified search engine crawlers will not be tracked or counted by the
    waiting room system, and will not appear in waiting room analytics.
    """


class WaitingroomZoneSettingsResponse(BaseModel):
    result: Result
