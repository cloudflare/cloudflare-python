# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["RecordingStartTrackRecordingParams", "Layers"]


class RecordingStartTrackRecordingParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    meeting_id: Required[str]
    """ID of the meeting to record."""

    layers: Dict[str, Layers]
    """Optional audio layer configuration.

    If omitted, RealtimeKit records all participant audio using the default file
    name prefix.
    """

    user_ids: SequenceNotStr[str]
    """Optional list of participant user IDs to record.

    Selective track recording (`user_ids`) is in early beta contact support to use
    this feature.
    """


class Layers(TypedDict, total=False):
    file_name_prefix: str
    """A file name prefix to apply for files generated from this layer"""

    media_kind: Literal["audio"]
    """Media kind to record. Track recording currently supports audio only."""
