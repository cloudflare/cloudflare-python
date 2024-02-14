# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["IndicatorFeedCreateParams"]


class IndicatorFeedCreateParams(TypedDict, total=False):
    description: str
    """The description of the example test"""

    name: str
    """The name of the indicator feed"""
