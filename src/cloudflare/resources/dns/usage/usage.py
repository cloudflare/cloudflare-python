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
from .account import (
    AccountResource,
    AsyncAccountResource,
    AccountResourceWithRawResponse,
    AsyncAccountResourceWithRawResponse,
    AccountResourceWithStreamingResponse,
    AsyncAccountResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["UsageResource", "AsyncUsageResource"]


class UsageResource(SyncAPIResource):
    @cached_property
    def zone(self) -> ZoneResource:
        return ZoneResource(self._client)

    @cached_property
    def account(self) -> AccountResource:
        return AccountResource(self._client)

    @cached_property
    def with_raw_response(self) -> UsageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return UsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return UsageResourceWithStreamingResponse(self)


class AsyncUsageResource(AsyncAPIResource):
    @cached_property
    def zone(self) -> AsyncZoneResource:
        return AsyncZoneResource(self._client)

    @cached_property
    def account(self) -> AsyncAccountResource:
        return AsyncAccountResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUsageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncUsageResourceWithStreamingResponse(self)


class UsageResourceWithRawResponse:
    def __init__(self, usage: UsageResource) -> None:
        self._usage = usage

    @cached_property
    def zone(self) -> ZoneResourceWithRawResponse:
        return ZoneResourceWithRawResponse(self._usage.zone)

    @cached_property
    def account(self) -> AccountResourceWithRawResponse:
        return AccountResourceWithRawResponse(self._usage.account)


class AsyncUsageResourceWithRawResponse:
    def __init__(self, usage: AsyncUsageResource) -> None:
        self._usage = usage

    @cached_property
    def zone(self) -> AsyncZoneResourceWithRawResponse:
        return AsyncZoneResourceWithRawResponse(self._usage.zone)

    @cached_property
    def account(self) -> AsyncAccountResourceWithRawResponse:
        return AsyncAccountResourceWithRawResponse(self._usage.account)


class UsageResourceWithStreamingResponse:
    def __init__(self, usage: UsageResource) -> None:
        self._usage = usage

    @cached_property
    def zone(self) -> ZoneResourceWithStreamingResponse:
        return ZoneResourceWithStreamingResponse(self._usage.zone)

    @cached_property
    def account(self) -> AccountResourceWithStreamingResponse:
        return AccountResourceWithStreamingResponse(self._usage.account)


class AsyncUsageResourceWithStreamingResponse:
    def __init__(self, usage: AsyncUsageResource) -> None:
        self._usage = usage

    @cached_property
    def zone(self) -> AsyncZoneResourceWithStreamingResponse:
        return AsyncZoneResourceWithStreamingResponse(self._usage.zone)

    @cached_property
    def account(self) -> AsyncAccountResourceWithStreamingResponse:
        return AsyncAccountResourceWithStreamingResponse(self._usage.account)
