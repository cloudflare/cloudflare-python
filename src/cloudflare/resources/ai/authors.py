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
from ...pagination import SyncSinglePage, AsyncSinglePage
from ..._base_client import AsyncPaginator, make_request_options

__all__ = ["AuthorsResource", "AsyncAuthorsResource"]


class AuthorsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuthorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AuthorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AuthorsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[object]:
        """
        Author Search

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/ai/authors/search",
            page=SyncSinglePage[object],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=object,
        )


class AsyncAuthorsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuthorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAuthorsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[object, AsyncSinglePage[object]]:
        """
        Author Search

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/ai/authors/search",
            page=AsyncSinglePage[object],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=object,
        )


class AuthorsResourceWithRawResponse:
    def __init__(self, authors: AuthorsResource) -> None:
        self._authors = authors

        self.list = to_raw_response_wrapper(
            authors.list,
        )


class AsyncAuthorsResourceWithRawResponse:
    def __init__(self, authors: AsyncAuthorsResource) -> None:
        self._authors = authors

        self.list = async_to_raw_response_wrapper(
            authors.list,
        )


class AuthorsResourceWithStreamingResponse:
    def __init__(self, authors: AuthorsResource) -> None:
        self._authors = authors

        self.list = to_streamed_response_wrapper(
            authors.list,
        )


class AsyncAuthorsResourceWithStreamingResponse:
    def __init__(self, authors: AsyncAuthorsResource) -> None:
        self._authors = authors

        self.list = async_to_streamed_response_wrapper(
            authors.list,
        )
