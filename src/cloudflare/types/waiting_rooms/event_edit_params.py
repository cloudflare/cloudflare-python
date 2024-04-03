# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["EventEditParams"]


class EventEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    waiting_room_id: Required[str]

    event_end_time: Required[str]
    """An ISO 8601 timestamp that marks the end of the event."""

    event_start_time: Required[str]
    """An ISO 8601 timestamp that marks the start of the event.

    At this time, queued users will be processed with the event's configuration. The
    start time must be at least one minute before `event_end_time`.
    """

    name: Required[str]
    """A unique name to identify the event.

    Only alphanumeric characters, hyphens and underscores are allowed.
    """

    custom_page_html: Optional[str]
    """
    If set, the event will override the waiting room's `custom_page_html` property
    while it is active. If null, the event will inherit it.
    """

    description: str
    """A note that you can use to add more details about the event."""

    disable_session_renewal: Optional[bool]
    """
    If set, the event will override the waiting room's `disable_session_renewal`
    property while it is active. If null, the event will inherit it.
    """

    new_users_per_minute: Optional[int]
    """
    If set, the event will override the waiting room's `new_users_per_minute`
    property while it is active. If null, the event will inherit it. This can only
    be set if the event's `total_active_users` property is also set.
    """

    prequeue_start_time: Optional[str]
    """
    An ISO 8601 timestamp that marks when to begin queueing all users before the
    event starts. The prequeue must start at least five minutes before
    `event_start_time`.
    """

    queueing_method: Optional[str]
    """
    If set, the event will override the waiting room's `queueing_method` property
    while it is active. If null, the event will inherit it.
    """

    session_duration: Optional[int]
    """
    If set, the event will override the waiting room's `session_duration` property
    while it is active. If null, the event will inherit it.
    """

    shuffle_at_event_start: bool
    """
    If enabled, users in the prequeue will be shuffled randomly at the
    `event_start_time`. Requires that `prequeue_start_time` is not null. This is
    useful for situations when many users will join the event prequeue at the same
    time and you want to shuffle them to ensure fairness. Naturally, it makes the
    most sense to enable this feature when the `queueing_method` during the event
    respects ordering such as **fifo**, or else the shuffling may be unnecessary.
    """

    suspended: bool
    """Suspends or allows an event.

    If set to `true`, the event is ignored and traffic will be handled based on the
    waiting room configuration.
    """

    total_active_users: Optional[int]
    """
    If set, the event will override the waiting room's `total_active_users` property
    while it is active. If null, the event will inherit it. This can only be set if
    the event's `new_users_per_minute` property is also set.
    """
