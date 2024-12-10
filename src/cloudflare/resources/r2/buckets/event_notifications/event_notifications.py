# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from .configuration import (
    ConfigurationResource,
    AsyncConfigurationResource,
    ConfigurationResourceWithRawResponse,
    AsyncConfigurationResourceWithRawResponse,
    ConfigurationResourceWithStreamingResponse,
    AsyncConfigurationResourceWithStreamingResponse,
)
from .configuration.configuration import ConfigurationResource, AsyncConfigurationResource

__all__ = ["EventNotificationsResource", "AsyncEventNotificationsResource"]


class EventNotificationsResource(SyncAPIResource):
    @cached_property
    def configuration(self) -> ConfigurationResource:
        return ConfigurationResource(self._client)

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
    def configuration(self) -> AsyncConfigurationResource:
        return AsyncConfigurationResource(self._client)

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
    def configuration(self) -> ConfigurationResourceWithRawResponse:
        return ConfigurationResourceWithRawResponse(self._event_notifications.configuration)


class AsyncEventNotificationsResourceWithRawResponse:
    def __init__(self, event_notifications: AsyncEventNotificationsResource) -> None:
        self._event_notifications = event_notifications

    @cached_property
    def configuration(self) -> AsyncConfigurationResourceWithRawResponse:
        return AsyncConfigurationResourceWithRawResponse(self._event_notifications.configuration)


class EventNotificationsResourceWithStreamingResponse:
    def __init__(self, event_notifications: EventNotificationsResource) -> None:
        self._event_notifications = event_notifications

    @cached_property
    def configuration(self) -> ConfigurationResourceWithStreamingResponse:
        return ConfigurationResourceWithStreamingResponse(self._event_notifications.configuration)


class AsyncEventNotificationsResourceWithStreamingResponse:
    def __init__(self, event_notifications: AsyncEventNotificationsResource) -> None:
        self._event_notifications = event_notifications

    @cached_property
    def configuration(self) -> AsyncConfigurationResourceWithStreamingResponse:
        return AsyncConfigurationResourceWithStreamingResponse(self._event_notifications.configuration)
