# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["LivestreamStartLivestreamingAMeetingParams", "VideoConfig"]


class LivestreamStartLivestreamingAMeetingParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    app_id: Required[str]
    """The app identifier tag."""

    name: Optional[str]

    video_config: VideoConfig


class VideoConfig(TypedDict, total=False):
    height: int
    """Height of the livestreaming video in pixels"""

    width: int
    """Width of the livestreaming video in pixels"""
