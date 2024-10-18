# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IndicatorFeedUpdateParams"]


class IndicatorFeedUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    description: str
    """The new description of the feed"""

    is_attributable: bool
    """The new is_attributable value of the feed"""

    is_downloadable: bool
    """The new is_downloadable value of the feed"""

    is_public: bool
    """The new is_public value of the feed"""

    name: str
    """The new name of the feed"""
