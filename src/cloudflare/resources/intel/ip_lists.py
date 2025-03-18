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
from ...types.intel.ip_list import IPList

__all__ = ["IPListsResource", "AsyncIPListsResource"]


class IPListsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IPListsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return IPListsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IPListsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return IPListsResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[IPList]:
        """
        Get IP Lists

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/intel/ip-list",
            page=SyncSinglePage[IPList],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=IPList,
        )


class AsyncIPListsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIPListsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIPListsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIPListsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncIPListsResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[IPList, AsyncSinglePage[IPList]]:
        """
        Get IP Lists

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/intel/ip-list",
            page=AsyncSinglePage[IPList],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=IPList,
        )


class IPListsResourceWithRawResponse:
    def __init__(self, ip_lists: IPListsResource) -> None:
        self._ip_lists = ip_lists

        self.get = to_raw_response_wrapper(
            ip_lists.get,
        )


class AsyncIPListsResourceWithRawResponse:
    def __init__(self, ip_lists: AsyncIPListsResource) -> None:
        self._ip_lists = ip_lists

        self.get = async_to_raw_response_wrapper(
            ip_lists.get,
        )


class IPListsResourceWithStreamingResponse:
    def __init__(self, ip_lists: IPListsResource) -> None:
        self._ip_lists = ip_lists

        self.get = to_streamed_response_wrapper(
            ip_lists.get,
        )


class AsyncIPListsResourceWithStreamingResponse:
    def __init__(self, ip_lists: AsyncIPListsResource) -> None:
        self._ip_lists = ip_lists

        self.get = async_to_streamed_response_wrapper(
            ip_lists.get,
        )
