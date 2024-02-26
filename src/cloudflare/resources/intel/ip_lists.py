# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Optional, cast

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
from ..._wrappers import ResultWrapper
from ...types.intel import IPListGetResponse
from ..._base_client import (
    make_request_options,
)

__all__ = ["IPLists", "AsyncIPLists"]


class IPLists(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IPListsWithRawResponse:
        return IPListsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IPListsWithStreamingResponse:
        return IPListsWithStreamingResponse(self)

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
    ) -> Optional[IPListGetResponse]:
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
        return self._get(
            f"/accounts/{account_id}/intel/ip-list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[IPListGetResponse]], ResultWrapper[IPListGetResponse]),
        )


class AsyncIPLists(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIPListsWithRawResponse:
        return AsyncIPListsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIPListsWithStreamingResponse:
        return AsyncIPListsWithStreamingResponse(self)

    async def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IPListGetResponse]:
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
        return await self._get(
            f"/accounts/{account_id}/intel/ip-list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[IPListGetResponse]], ResultWrapper[IPListGetResponse]),
        )


class IPListsWithRawResponse:
    def __init__(self, ip_lists: IPLists) -> None:
        self._ip_lists = ip_lists

        self.get = to_raw_response_wrapper(
            ip_lists.get,
        )


class AsyncIPListsWithRawResponse:
    def __init__(self, ip_lists: AsyncIPLists) -> None:
        self._ip_lists = ip_lists

        self.get = async_to_raw_response_wrapper(
            ip_lists.get,
        )


class IPListsWithStreamingResponse:
    def __init__(self, ip_lists: IPLists) -> None:
        self._ip_lists = ip_lists

        self.get = to_streamed_response_wrapper(
            ip_lists.get,
        )


class AsyncIPListsWithStreamingResponse:
    def __init__(self, ip_lists: AsyncIPLists) -> None:
        self._ip_lists = ip_lists

        self.get = async_to_streamed_response_wrapper(
            ip_lists.get,
        )
