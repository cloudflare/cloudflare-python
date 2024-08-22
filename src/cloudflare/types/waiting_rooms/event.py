# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["Event"]


class Event(BaseModel):
    id: Optional[str] = None

    created_on: Optional[datetime] = None

    custom_page_html: Optional[str] = None
    """
    If set, the event will override the waiting room's `custom_page_html` property
    while it is active. If null, the event will inherit it.
    """

    description: Optional[str] = None
    """A note that you can use to add more details about the event."""

    disable_session_renewal: Optional[bool] = None
    """
    If set, the event will override the waiting room's `disable_session_renewal`
    property while it is active. If null, the event will inherit it.
    """

    event_end_time: Optional[str] = None
    """An ISO 8601 timestamp that marks the end of the event."""

    event_start_time: Optional[str] = None
    """An ISO 8601 timestamp that marks the start of the event.

    At this time, queued users will be processed with the event's configuration. The
    start time must be at least one minute before `event_end_time`.
    """

    modified_on: Optional[datetime] = None

    name: Optional[str] = None
    """A unique name to identify the event.

    Only alphanumeric characters, hyphens and underscores are allowed.
    """

    new_users_per_minute: Optional[int] = None
    """
    If set, the event will override the waiting room's `new_users_per_minute`
    property while it is active. If null, the event will inherit it. This can only
    be set if the event's `total_active_users` property is also set.
    """

    prequeue_start_time: Optional[str] = None
    """
    An ISO 8601 timestamp that marks when to begin queueing all users before the
    event starts. The prequeue must start at least five minutes before
    `event_start_time`.
    """

    queueing_method: Optional[str] = None
    """
    If set, the event will override the waiting room's `queueing_method` property
    while it is active. If null, the event will inherit it.
    """

    session_duration: Optional[int] = None
    """
    If set, the event will override the waiting room's `session_duration` property
    while it is active. If null, the event will inherit it.
    """

    shuffle_at_event_start: Optional[bool] = None
    """
    If enabled, users in the prequeue will be shuffled randomly at the
    `event_start_time`. Requires that `prequeue_start_time` is not null. This is
    useful for situations when many users will join the event prequeue at the same
    time and you want to shuffle them to ensure fairness. Naturally, it makes the
    most sense to enable this feature when the `queueing_method` during the event
    respects ordering such as **fifo**, or else the shuffling may be unnecessary.
    """

    suspended: Optional[bool] = None
    """Suspends or allows an event.

    If set to `true`, the event is ignored and traffic will be handled based on the
    waiting room configuration.
    """

    total_active_users: Optional[int] = None
    """
    If set, the event will override the waiting room's `total_active_users` property
    while it is active. If null, the event will inherit it. This can only be set if
    the event's `new_users_per_minute` property is also set.
    """
