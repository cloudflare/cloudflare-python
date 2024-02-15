# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["AudioTrackUpdateParams"]


class AudioTrackUpdateParams(TypedDict, total=False):
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
