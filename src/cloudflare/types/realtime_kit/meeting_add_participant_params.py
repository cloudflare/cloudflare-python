# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["MeetingAddParticipantParams"]


class MeetingAddParticipantParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    app_id: Required[str]
    """The app identifier tag."""

    custom_participant_id: Required[str]
    """A unique participant ID.

    You must specify a unique ID for the participant, for example, UUID, email
    address, and so on.
    """

    preset_name: Required[str]
    """Name of the preset to apply to this participant."""

    name: Optional[str]
    """(Optional) Name of the participant."""

    picture: Optional[str]
    """(Optional) A URL to a picture to be used for the participant."""
