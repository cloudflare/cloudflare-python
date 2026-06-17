# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .relays.relays import (
    RelaysResource,
    AsyncRelaysResource,
    RelaysResourceWithRawResponse,
    AsyncRelaysResourceWithRawResponse,
    RelaysResourceWithStreamingResponse,
    AsyncRelaysResourceWithStreamingResponse,
)

__all__ = ["MoqResource", "AsyncMoqResource"]


class MoqResource(SyncAPIResource):
    @cached_property
    def relays(self) -> RelaysResource:
        return RelaysResource(self._client)

    @cached_property
    def with_raw_response(self) -> MoqResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return MoqResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MoqResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return MoqResourceWithStreamingResponse(self)


class AsyncMoqResource(AsyncAPIResource):
    @cached_property
    def relays(self) -> AsyncRelaysResource:
        return AsyncRelaysResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMoqResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMoqResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMoqResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncMoqResourceWithStreamingResponse(self)


class MoqResourceWithRawResponse:
    def __init__(self, moq: MoqResource) -> None:
        self._moq = moq

    @cached_property
    def relays(self) -> RelaysResourceWithRawResponse:
        return RelaysResourceWithRawResponse(self._moq.relays)


class AsyncMoqResourceWithRawResponse:
    def __init__(self, moq: AsyncMoqResource) -> None:
        self._moq = moq

    @cached_property
    def relays(self) -> AsyncRelaysResourceWithRawResponse:
        return AsyncRelaysResourceWithRawResponse(self._moq.relays)


class MoqResourceWithStreamingResponse:
    def __init__(self, moq: MoqResource) -> None:
        self._moq = moq

    @cached_property
    def relays(self) -> RelaysResourceWithStreamingResponse:
        return RelaysResourceWithStreamingResponse(self._moq.relays)


class AsyncMoqResourceWithStreamingResponse:
    def __init__(self, moq: AsyncMoqResource) -> None:
        self._moq = moq

    @cached_property
    def relays(self) -> AsyncRelaysResourceWithStreamingResponse:
        return AsyncRelaysResourceWithStreamingResponse(self._moq.relays)
