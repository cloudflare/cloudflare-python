# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SessionGetParticipantDataFromPeerIDParams"]


class SessionGetParticipantDataFromPeerIDParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    app_id: Required[str]
    """The app identifier tag."""

    filters: Literal["device_info", "ip_information", "precall_network_information", "events", "quality_stats"]
    """Filter to apply to the peer report."""

    include_peer_events: bool
    """if true, response includes all the peer events of participant."""
