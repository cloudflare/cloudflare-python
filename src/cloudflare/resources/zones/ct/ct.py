# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .alerting import (
    AlertingResource,
    AsyncAlertingResource,
    AlertingResourceWithRawResponse,
    AsyncAlertingResourceWithRawResponse,
    AlertingResourceWithStreamingResponse,
    AsyncAlertingResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["CTResource", "AsyncCTResource"]


class CTResource(SyncAPIResource):
    @cached_property
    def alerting(self) -> AlertingResource:
        return AlertingResource(self._client)

    @cached_property
    def with_raw_response(self) -> CTResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CTResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CTResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CTResourceWithStreamingResponse(self)


class AsyncCTResource(AsyncAPIResource):
    @cached_property
    def alerting(self) -> AsyncAlertingResource:
        return AsyncAlertingResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCTResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCTResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCTResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCTResourceWithStreamingResponse(self)


class CTResourceWithRawResponse:
    def __init__(self, ct: CTResource) -> None:
        self._ct = ct

    @cached_property
    def alerting(self) -> AlertingResourceWithRawResponse:
        return AlertingResourceWithRawResponse(self._ct.alerting)


class AsyncCTResourceWithRawResponse:
    def __init__(self, ct: AsyncCTResource) -> None:
        self._ct = ct

    @cached_property
    def alerting(self) -> AsyncAlertingResourceWithRawResponse:
        return AsyncAlertingResourceWithRawResponse(self._ct.alerting)


class CTResourceWithStreamingResponse:
    def __init__(self, ct: CTResource) -> None:
        self._ct = ct

    @cached_property
    def alerting(self) -> AlertingResourceWithStreamingResponse:
        return AlertingResourceWithStreamingResponse(self._ct.alerting)


class AsyncCTResourceWithStreamingResponse:
    def __init__(self, ct: AsyncCTResource) -> None:
        self._ct = ct

    @cached_property
    def alerting(self) -> AsyncAlertingResourceWithStreamingResponse:
        return AsyncAlertingResourceWithStreamingResponse(self._ct.alerting)
