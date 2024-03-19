# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_custom_raw_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ..._base_client import (
    make_request_options,
)

__all__ = ["Content", "AsyncContent"]


class Content(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContentWithRawResponse:
        return ContentWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContentWithStreamingResponse:
        return ContentWithStreamingResponse(self)

    def get(
        self,
        snippet_name: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """
        Snippet Content

        Args:
          zone_identifier: Identifier

          snippet_name: Snippet identifying name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not snippet_name:
            raise ValueError(f"Expected a non-empty value for `snippet_name` but received {snippet_name!r}")
        extra_headers = {"Accept": "multipart/form-data", **(extra_headers or {})}
        return self._get(
            f"/zones/{zone_identifier}/snippets/{snippet_name}/content",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncContent(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContentWithRawResponse:
        return AsyncContentWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContentWithStreamingResponse:
        return AsyncContentWithStreamingResponse(self)

    async def get(
        self,
        snippet_name: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """
        Snippet Content

        Args:
          zone_identifier: Identifier

          snippet_name: Snippet identifying name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not snippet_name:
            raise ValueError(f"Expected a non-empty value for `snippet_name` but received {snippet_name!r}")
        extra_headers = {"Accept": "multipart/form-data", **(extra_headers or {})}
        return await self._get(
            f"/zones/{zone_identifier}/snippets/{snippet_name}/content",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class ContentWithRawResponse:
    def __init__(self, content: Content) -> None:
        self._content = content

        self.get = to_custom_raw_response_wrapper(
            content.get,
            BinaryAPIResponse,
        )


class AsyncContentWithRawResponse:
    def __init__(self, content: AsyncContent) -> None:
        self._content = content

        self.get = async_to_custom_raw_response_wrapper(
            content.get,
            AsyncBinaryAPIResponse,
        )


class ContentWithStreamingResponse:
    def __init__(self, content: Content) -> None:
        self._content = content

        self.get = to_custom_streamed_response_wrapper(
            content.get,
            StreamedBinaryAPIResponse,
        )


class AsyncContentWithStreamingResponse:
    def __init__(self, content: AsyncContent) -> None:
        self._content = content

        self.get = async_to_custom_streamed_response_wrapper(
            content.get,
            AsyncStreamedBinaryAPIResponse,
        )
