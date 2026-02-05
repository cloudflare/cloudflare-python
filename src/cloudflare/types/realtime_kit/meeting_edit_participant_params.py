# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["MeetingEditParticipantParams"]


class MeetingEditParticipantParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    app_id: Required[str]
    """The app identifier tag."""

    meeting_id: Required[str]

    name: Optional[str]
    """(Optional) Name of the participant."""

    picture: Optional[str]
    """(Optional) A URL to a picture to be used for the participant."""

    preset_name: Optional[str]
    """(Optional) Name of the preset to apply to this participant."""
