# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IndicatorFeedSnapshotParams"]


class IndicatorFeedSnapshotParams(TypedDict, total=False):
    account_identifier: Required[str]
    """Identifier"""

    source: str
    """The file to upload"""
