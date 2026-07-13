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

__all__ = ["MoQResource", "AsyncMoQResource"]


class MoQResource(SyncAPIResource):
    @cached_property
    def relays(self) -> RelaysResource:
        return RelaysResource(self._client)

    @cached_property
    def with_raw_response(self) -> MoQResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return MoQResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MoQResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return MoQResourceWithStreamingResponse(self)


class AsyncMoQResource(AsyncAPIResource):
    @cached_property
    def relays(self) -> AsyncRelaysResource:
        return AsyncRelaysResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMoQResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMoQResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMoQResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncMoQResourceWithStreamingResponse(self)


class MoQResourceWithRawResponse:
    def __init__(self, moq: MoQResource) -> None:
        self._moq = moq

    @cached_property
    def relays(self) -> RelaysResourceWithRawResponse:
        return RelaysResourceWithRawResponse(self._moq.relays)


class AsyncMoQResourceWithRawResponse:
    def __init__(self, moq: AsyncMoQResource) -> None:
        self._moq = moq

    @cached_property
    def relays(self) -> AsyncRelaysResourceWithRawResponse:
        return AsyncRelaysResourceWithRawResponse(self._moq.relays)


class MoQResourceWithStreamingResponse:
    def __init__(self, moq: MoQResource) -> None:
        self._moq = moq

    @cached_property
    def relays(self) -> RelaysResourceWithStreamingResponse:
        return RelaysResourceWithStreamingResponse(self._moq.relays)


class AsyncMoQResourceWithStreamingResponse:
    def __init__(self, moq: AsyncMoQResource) -> None:
        self._moq = moq

    @cached_property
    def relays(self) -> AsyncRelaysResourceWithStreamingResponse:
        return AsyncRelaysResourceWithStreamingResponse(self._moq.relays)
