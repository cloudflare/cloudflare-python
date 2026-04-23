# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SessionGetSessionParticipantsParams"]


class SessionGetSessionParticipantsParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    app_id: Required[str]
    """The app identifier tag."""

    include_peer_events: bool
    """if true, response includes all the peer events of participants."""

    page_no: float
    """The page number from which you want your page search results to be displayed."""

    per_page: float
    """Number of results per page"""

    search: str
    """The search query string. You can search using the meeting ID or title."""

    sort_by: Literal["joinedAt", "duration"]

    sort_order: Literal["ASC", "DESC"]

    view: Literal["raw", "consolidated"]
    """
    In breakout room sessions, the view parameter can be set to `raw` for session
    specific duration for participants or `consolidated` to accumulate breakout room
    durations.
    """
