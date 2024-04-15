# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .r2 import (
    R2,
    AsyncR2,
    R2WithRawResponse,
    AsyncR2WithRawResponse,
    R2WithStreamingResponse,
    AsyncR2WithStreamingResponse,
)
from .r2.r2 import R2, AsyncR2
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["EventNotifications", "AsyncEventNotifications"]


class EventNotifications(SyncAPIResource):
    @cached_property
    def r2(self) -> R2:
        return R2(self._client)

    @cached_property
    def with_raw_response(self) -> EventNotificationsWithRawResponse:
        return EventNotificationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventNotificationsWithStreamingResponse:
        return EventNotificationsWithStreamingResponse(self)


class AsyncEventNotifications(AsyncAPIResource):
    @cached_property
    def r2(self) -> AsyncR2:
        return AsyncR2(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEventNotificationsWithRawResponse:
        return AsyncEventNotificationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventNotificationsWithStreamingResponse:
        return AsyncEventNotificationsWithStreamingResponse(self)


class EventNotificationsWithRawResponse:
    def __init__(self, event_notifications: EventNotifications) -> None:
        self._event_notifications = event_notifications

    @cached_property
    def r2(self) -> R2WithRawResponse:
        return R2WithRawResponse(self._event_notifications.r2)


class AsyncEventNotificationsWithRawResponse:
    def __init__(self, event_notifications: AsyncEventNotifications) -> None:
        self._event_notifications = event_notifications

    @cached_property
    def r2(self) -> AsyncR2WithRawResponse:
        return AsyncR2WithRawResponse(self._event_notifications.r2)


class EventNotificationsWithStreamingResponse:
    def __init__(self, event_notifications: EventNotifications) -> None:
        self._event_notifications = event_notifications

    @cached_property
    def r2(self) -> R2WithStreamingResponse:
        return R2WithStreamingResponse(self._event_notifications.r2)


class AsyncEventNotificationsWithStreamingResponse:
    def __init__(self, event_notifications: AsyncEventNotifications) -> None:
        self._event_notifications = event_notifications

    @cached_property
    def r2(self) -> AsyncR2WithStreamingResponse:
        return AsyncR2WithStreamingResponse(self._event_notifications.r2)
