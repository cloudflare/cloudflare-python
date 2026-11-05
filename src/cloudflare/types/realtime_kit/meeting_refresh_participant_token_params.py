# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MeetingRefreshParticipantTokenParams"]


class MeetingRefreshParticipantTokenParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    app_id: Required[str]
    """The app identifier tag."""

    meeting_id: Required[str]

    expires_on: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """RFC 3339 timestamp with a timezone at or after which the token cannot be used.

    Must be in the future. Defaults to not_before plus 100 days.
    """

    not_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """RFC 3339 timestamp with a timezone before which the token cannot be used.

    Defaults to the current time. May be in the past.
    """
