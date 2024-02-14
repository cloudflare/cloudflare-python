# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LiveListParams"]


class LiveListParams(TypedDict, total=False):
    since_minutes: Required[float]
    """Number of minutes before current time"""
