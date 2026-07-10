# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .zone import (
    ZoneResource,
    AsyncZoneResource,
    ZoneResourceWithRawResponse,
    AsyncZoneResourceWithRawResponse,
    ZoneResourceWithStreamingResponse,
    AsyncZoneResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .account.account import (
    AccountResource,
    AsyncAccountResource,
    AccountResourceWithRawResponse,
    AsyncAccountResourceWithRawResponse,
    AccountResourceWithStreamingResponse,
    AsyncAccountResourceWithStreamingResponse,
)

__all__ = ["SettingsResource", "AsyncSettingsResource"]


class SettingsResource(SyncAPIResource):
    @cached_property
    def zone(self) -> ZoneResource:
        return ZoneResource(self._client)

    @cached_property
    def account(self) -> AccountResource:
        return AccountResource(self._client)

    @cached_property
    def with_raw_response(self) -> SettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SettingsResourceWithStreamingResponse(self)


class AsyncSettingsResource(AsyncAPIResource):
    @cached_property
    def zone(self) -> AsyncZoneResource:
        return AsyncZoneResource(self._client)

    @cached_property
    def account(self) -> AsyncAccountResource:
        return AsyncAccountResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSettingsResourceWithStreamingResponse(self)


class SettingsResourceWithRawResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

    @cached_property
    def zone(self) -> ZoneResourceWithRawResponse:
        return ZoneResourceWithRawResponse(self._settings.zone)

    @cached_property
    def account(self) -> AccountResourceWithRawResponse:
        return AccountResourceWithRawResponse(self._settings.account)


class AsyncSettingsResourceWithRawResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

    @cached_property
    def zone(self) -> AsyncZoneResourceWithRawResponse:
        return AsyncZoneResourceWithRawResponse(self._settings.zone)

    @cached_property
    def account(self) -> AsyncAccountResourceWithRawResponse:
        return AsyncAccountResourceWithRawResponse(self._settings.account)


class SettingsResourceWithStreamingResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

    @cached_property
    def zone(self) -> ZoneResourceWithStreamingResponse:
        return ZoneResourceWithStreamingResponse(self._settings.zone)

    @cached_property
    def account(self) -> AccountResourceWithStreamingResponse:
        return AccountResourceWithStreamingResponse(self._settings.account)


class AsyncSettingsResourceWithStreamingResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

    @cached_property
    def zone(self) -> AsyncZoneResourceWithStreamingResponse:
        return AsyncZoneResourceWithStreamingResponse(self._settings.zone)

    @cached_property
    def account(self) -> AsyncAccountResourceWithStreamingResponse:
        return AsyncAccountResourceWithStreamingResponse(self._settings.account)
