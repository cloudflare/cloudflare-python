# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import (
    make_request_options,
)

__all__ = ["Embed", "AsyncEmbed"]


class Embed(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmbedWithRawResponse:
        return EmbedWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmbedWithStreamingResponse:
        return EmbedWithStreamingResponse(self)

    def get(
        self,
        identifier: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Fetches an HTML code snippet to embed a video in a web page delivered through
        Cloudflare. On success, returns an HTML fragment for use on web pages to display
        a video. On failure, returns a JSON response body.

        Args:
          account_id: The account identifier tag.

          identifier: A Cloudflare-generated unique identifier for a media item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._get(
            f"/accounts/{account_id}/stream/{identifier}/embed",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncEmbed(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmbedWithRawResponse:
        return AsyncEmbedWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmbedWithStreamingResponse:
        return AsyncEmbedWithStreamingResponse(self)

    async def get(
        self,
        identifier: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Fetches an HTML code snippet to embed a video in a web page delivered through
        Cloudflare. On success, returns an HTML fragment for use on web pages to display
        a video. On failure, returns a JSON response body.

        Args:
          account_id: The account identifier tag.

          identifier: A Cloudflare-generated unique identifier for a media item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return await self._get(
            f"/accounts/{account_id}/stream/{identifier}/embed",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class EmbedWithRawResponse:
    def __init__(self, embed: Embed) -> None:
        self._embed = embed

        self.get = to_raw_response_wrapper(
            embed.get,
        )


class AsyncEmbedWithRawResponse:
    def __init__(self, embed: AsyncEmbed) -> None:
        self._embed = embed

        self.get = async_to_raw_response_wrapper(
            embed.get,
        )


class EmbedWithStreamingResponse:
    def __init__(self, embed: Embed) -> None:
        self._embed = embed

        self.get = to_streamed_response_wrapper(
            embed.get,
        )


class AsyncEmbedWithStreamingResponse:
    def __init__(self, embed: AsyncEmbed) -> None:
        self._embed = embed

        self.get = async_to_streamed_response_wrapper(
            embed.get,
        )
