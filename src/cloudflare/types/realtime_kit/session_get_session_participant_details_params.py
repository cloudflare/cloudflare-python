# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SessionGetSessionParticipantDetailsParams"]


class SessionGetSessionParticipantDetailsParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    app_id: Required[str]
    """The app identifier tag."""

    session_id: Required[str]

    filters: Literal["device_info", "ip_information", "precall_network_information", "events", "quality_stats"]
    """Comma separated list of filters to apply.

    Note that there must be no spaces between the filters.
    """

    include_peer_events: bool
    """if true, response includes all the peer events of participant."""
