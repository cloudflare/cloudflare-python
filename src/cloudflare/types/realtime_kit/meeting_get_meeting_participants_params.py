# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MeetingGetMeetingParticipantsParams"]


class MeetingGetMeetingParticipantsParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    app_id: Required[str]
    """The app identifier tag."""

    page_no: float
    """The page number from which you want your page search results to be displayed."""

    per_page: float
    """Number of results per page"""
