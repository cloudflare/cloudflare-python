# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

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
from ..._base_client import (
    make_request_options,
)
from ...types.magic_transit.cf_interconnect_list_response import CfInterconnectListResponse

__all__ = ["CfInterconnectsResource", "AsyncCfInterconnectsResource"]


class CfInterconnectsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CfInterconnectsResourceWithRawResponse:
        return CfInterconnectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CfInterconnectsResourceWithStreamingResponse:
        return CfInterconnectsResourceWithStreamingResponse(self)

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
    ) -> CfInterconnectListResponse:
        """
        Lists interconnects associated with an account.

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
            f"/accounts/{account_id}/magic/cf_interconnects",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CfInterconnectListResponse]._unwrapper,
            ),
            cast_to=cast(Type[CfInterconnectListResponse], ResultWrapper[CfInterconnectListResponse]),
        )


class AsyncCfInterconnectsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCfInterconnectsResourceWithRawResponse:
        return AsyncCfInterconnectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCfInterconnectsResourceWithStreamingResponse:
        return AsyncCfInterconnectsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CfInterconnectListResponse:
        """
        Lists interconnects associated with an account.

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
            f"/accounts/{account_id}/magic/cf_interconnects",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CfInterconnectListResponse]._unwrapper,
            ),
            cast_to=cast(Type[CfInterconnectListResponse], ResultWrapper[CfInterconnectListResponse]),
        )


class CfInterconnectsResourceWithRawResponse:
    def __init__(self, cf_interconnects: CfInterconnectsResource) -> None:
        self._cf_interconnects = cf_interconnects

        self.list = to_raw_response_wrapper(
            cf_interconnects.list,
        )


class AsyncCfInterconnectsResourceWithRawResponse:
    def __init__(self, cf_interconnects: AsyncCfInterconnectsResource) -> None:
        self._cf_interconnects = cf_interconnects

        self.list = async_to_raw_response_wrapper(
            cf_interconnects.list,
        )


class CfInterconnectsResourceWithStreamingResponse:
    def __init__(self, cf_interconnects: CfInterconnectsResource) -> None:
        self._cf_interconnects = cf_interconnects

        self.list = to_streamed_response_wrapper(
            cf_interconnects.list,
        )


class AsyncCfInterconnectsResourceWithStreamingResponse:
    def __init__(self, cf_interconnects: AsyncCfInterconnectsResource) -> None:
        self._cf_interconnects = cf_interconnects

        self.list = async_to_streamed_response_wrapper(
            cf_interconnects.list,
        )
