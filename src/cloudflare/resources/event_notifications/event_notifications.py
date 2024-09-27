# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .r2 import (
    R2Resource,
    AsyncR2Resource,
    R2ResourceWithRawResponse,
    AsyncR2ResourceWithRawResponse,
    R2ResourceWithStreamingResponse,
    AsyncR2ResourceWithStreamingResponse,
)
from .r2.r2 import R2Resource, AsyncR2Resource
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["EventNotificationsResource", "AsyncEventNotificationsResource"]


class EventNotificationsResource(SyncAPIResource):
    @cached_property
    def r2(self) -> R2Resource:
        return R2Resource(self._client)

    @cached_property
    def with_raw_response(self) -> EventNotificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return EventNotificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventNotificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return EventNotificationsResourceWithStreamingResponse(self)


class AsyncEventNotificationsResource(AsyncAPIResource):
    @cached_property
    def r2(self) -> AsyncR2Resource:
        return AsyncR2Resource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEventNotificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEventNotificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventNotificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncEventNotificationsResourceWithStreamingResponse(self)


class EventNotificationsResourceWithRawResponse:
    def __init__(self, event_notifications: EventNotificationsResource) -> None:
        self._event_notifications = event_notifications

    @cached_property
    def r2(self) -> R2ResourceWithRawResponse:
        return R2ResourceWithRawResponse(self._event_notifications.r2)


class AsyncEventNotificationsResourceWithRawResponse:
    def __init__(self, event_notifications: AsyncEventNotificationsResource) -> None:
        self._event_notifications = event_notifications

    @cached_property
    def r2(self) -> AsyncR2ResourceWithRawResponse:
        return AsyncR2ResourceWithRawResponse(self._event_notifications.r2)


class EventNotificationsResourceWithStreamingResponse:
    def __init__(self, event_notifications: EventNotificationsResource) -> None:
        self._event_notifications = event_notifications

    @cached_property
    def r2(self) -> R2ResourceWithStreamingResponse:
        return R2ResourceWithStreamingResponse(self._event_notifications.r2)


class AsyncEventNotificationsResourceWithStreamingResponse:
    def __init__(self, event_notifications: AsyncEventNotificationsResource) -> None:
        self._event_notifications = event_notifications

    @cached_property
    def r2(self) -> AsyncR2ResourceWithStreamingResponse:
        return AsyncR2ResourceWithStreamingResponse(self._event_notifications.r2)
