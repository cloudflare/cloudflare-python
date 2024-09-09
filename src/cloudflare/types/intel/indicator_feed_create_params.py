# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IndicatorFeedCreateParams"]


class IndicatorFeedCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    description: str
    """The description of the example test"""

    name: str
    """The name of the indicator feed"""
