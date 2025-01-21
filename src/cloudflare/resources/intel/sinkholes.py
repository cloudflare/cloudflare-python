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
from ...types.intel.sinkhole import Sinkhole

__all__ = ["SinkholesResource", "AsyncSinkholesResource"]


class SinkholesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SinkholesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SinkholesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SinkholesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SinkholesResourceWithStreamingResponse(self)

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
    ) -> SyncSinglePage[Sinkhole]:
        """
        List sinkholes owned by this account

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
            f"/accounts/{account_id}/intel/sinkholes",
            page=SyncSinglePage[Sinkhole],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Sinkhole,
        )


class AsyncSinkholesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSinkholesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSinkholesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSinkholesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSinkholesResourceWithStreamingResponse(self)

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
    ) -> AsyncPaginator[Sinkhole, AsyncSinglePage[Sinkhole]]:
        """
        List sinkholes owned by this account

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
            f"/accounts/{account_id}/intel/sinkholes",
            page=AsyncSinglePage[Sinkhole],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Sinkhole,
        )


class SinkholesResourceWithRawResponse:
    def __init__(self, sinkholes: SinkholesResource) -> None:
        self._sinkholes = sinkholes

        self.list = to_raw_response_wrapper(
            sinkholes.list,
        )


class AsyncSinkholesResourceWithRawResponse:
    def __init__(self, sinkholes: AsyncSinkholesResource) -> None:
        self._sinkholes = sinkholes

        self.list = async_to_raw_response_wrapper(
            sinkholes.list,
        )


class SinkholesResourceWithStreamingResponse:
    def __init__(self, sinkholes: SinkholesResource) -> None:
        self._sinkholes = sinkholes

        self.list = to_streamed_response_wrapper(
            sinkholes.list,
        )


class AsyncSinkholesResourceWithStreamingResponse:
    def __init__(self, sinkholes: AsyncSinkholesResource) -> None:
        self._sinkholes = sinkholes

        self.list = async_to_streamed_response_wrapper(
            sinkholes.list,
        )
