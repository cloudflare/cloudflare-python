# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .sfu import (
    SfuResource,
    AsyncSfuResource,
    SfuResourceWithRawResponse,
    AsyncSfuResourceWithRawResponse,
    SfuResourceWithStreamingResponse,
    AsyncSfuResourceWithStreamingResponse,
)
from .turn import (
    TURNResource,
    AsyncTURNResource,
    TURNResourceWithRawResponse,
    AsyncTURNResourceWithRawResponse,
    TURNResourceWithStreamingResponse,
    AsyncTURNResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["CallsResource", "AsyncCallsResource"]


class CallsResource(SyncAPIResource):
    @cached_property
    def sfu(self) -> SfuResource:
        return SfuResource(self._client)

    @cached_property
    def turn(self) -> TURNResource:
        return TURNResource(self._client)

    @cached_property
    def with_raw_response(self) -> CallsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CallsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CallsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CallsResourceWithStreamingResponse(self)


class AsyncCallsResource(AsyncAPIResource):
    @cached_property
    def sfu(self) -> AsyncSfuResource:
        return AsyncSfuResource(self._client)

    @cached_property
    def turn(self) -> AsyncTURNResource:
        return AsyncTURNResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCallsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCallsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCallsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCallsResourceWithStreamingResponse(self)


class CallsResourceWithRawResponse:
    def __init__(self, calls: CallsResource) -> None:
        self._calls = calls

    @cached_property
    def sfu(self) -> SfuResourceWithRawResponse:
        return SfuResourceWithRawResponse(self._calls.sfu)

    @cached_property
    def turn(self) -> TURNResourceWithRawResponse:
        return TURNResourceWithRawResponse(self._calls.turn)


class AsyncCallsResourceWithRawResponse:
    def __init__(self, calls: AsyncCallsResource) -> None:
        self._calls = calls

    @cached_property
    def sfu(self) -> AsyncSfuResourceWithRawResponse:
        return AsyncSfuResourceWithRawResponse(self._calls.sfu)

    @cached_property
    def turn(self) -> AsyncTURNResourceWithRawResponse:
        return AsyncTURNResourceWithRawResponse(self._calls.turn)


class CallsResourceWithStreamingResponse:
    def __init__(self, calls: CallsResource) -> None:
        self._calls = calls

    @cached_property
    def sfu(self) -> SfuResourceWithStreamingResponse:
        return SfuResourceWithStreamingResponse(self._calls.sfu)

    @cached_property
    def turn(self) -> TURNResourceWithStreamingResponse:
        return TURNResourceWithStreamingResponse(self._calls.turn)


class AsyncCallsResourceWithStreamingResponse:
    def __init__(self, calls: AsyncCallsResource) -> None:
        self._calls = calls

    @cached_property
    def sfu(self) -> AsyncSfuResourceWithStreamingResponse:
        return AsyncSfuResourceWithStreamingResponse(self._calls.sfu)

    @cached_property
    def turn(self) -> AsyncTURNResourceWithStreamingResponse:
        return AsyncTURNResourceWithStreamingResponse(self._calls.turn)
