# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options

__all__ = ["PageResource", "AsyncPageResource"]


class PageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PageResourceWithStreamingResponse(self)

    def get(
        self,
        target_id: str,
        *,
        account_id: str,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Establishes a WebSocket connection to a specific Chrome DevTools target or page.

        Args:
          account_id: Account ID.

          session_id: Browser session ID.

          target_id: Target ID, e.g. page ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not target_id:
            raise ValueError(f"Expected a non-empty value for `target_id` but received {target_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/page/{target_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncPageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPageResourceWithStreamingResponse(self)

    async def get(
        self,
        target_id: str,
        *,
        account_id: str,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Establishes a WebSocket connection to a specific Chrome DevTools target or page.

        Args:
          account_id: Account ID.

          session_id: Browser session ID.

          target_id: Target ID, e.g. page ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not target_id:
            raise ValueError(f"Expected a non-empty value for `target_id` but received {target_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/page/{target_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class PageResourceWithRawResponse:
    def __init__(self, page: PageResource) -> None:
        self._page = page

        self.get = to_raw_response_wrapper(
            page.get,
        )


class AsyncPageResourceWithRawResponse:
    def __init__(self, page: AsyncPageResource) -> None:
        self._page = page

        self.get = async_to_raw_response_wrapper(
            page.get,
        )


class PageResourceWithStreamingResponse:
    def __init__(self, page: PageResource) -> None:
        self._page = page

        self.get = to_streamed_response_wrapper(
            page.get,
        )


class AsyncPageResourceWithStreamingResponse:
    def __init__(self, page: AsyncPageResource) -> None:
        self._page = page

        self.get = async_to_streamed_response_wrapper(
            page.get,
        )
