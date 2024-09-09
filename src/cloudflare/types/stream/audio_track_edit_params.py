# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AudioTrackEditParams"]


class AudioTrackEditParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    identifier: Required[str]
    """A Cloudflare-generated unique identifier for a media item."""

    default: bool
    """Denotes whether the audio track will be played by default in a player."""

    label: str
    """
    A string to uniquely identify the track amongst other audio track labels for the
    specified video.
    """
