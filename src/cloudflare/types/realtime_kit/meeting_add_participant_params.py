# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MeetingAddParticipantParams", "Token"]


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

    token: Token
    """Validity window of the participant authentication token.

    The window is [not_before, expires_on) and cannot be longer than 100 days.
    Defaults to a token valid from now for 100 days.
    """

    name: Optional[str]
    """(Optional) Name of the participant."""

    picture: Optional[str]
    """(Optional) A URL to a picture to be used for the participant."""


class Token(TypedDict, total=False):
    """Validity window of the participant authentication token.

    The window is [not_before, expires_on) and cannot be longer than 100 days. Defaults to a token valid from now for 100 days.
    """

    expires_on: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """RFC 3339 timestamp with a timezone at or after which the token cannot be used.

    Must be in the future. Defaults to not_before plus 100 days.
    """

    not_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """RFC 3339 timestamp with a timezone before which the token cannot be used.

    Defaults to the current time. May be in the past.
    """
