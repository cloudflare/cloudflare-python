# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import (
    make_request_options,
)
from ....types.intel.domains import bulk_get_params
from ....types.intel.domains.bulk_get_response import BulkGetResponse

__all__ = ["BulksResource", "AsyncBulksResource"]


class BulksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BulksResourceWithRawResponse:
        return BulksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BulksResourceWithStreamingResponse:
        return BulksResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        account_id: str,
        domain: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[BulkGetResponse]:
        """
        Get Multiple Domain Details

        Args:
          account_id: Identifier

          domain: Accepts multiple values, i.e. `?domain=cloudflare.com&domain=example.com`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/intel/domain/bulk",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"domain": domain}, bulk_get_params.BulkGetParams),
                post_parser=ResultWrapper[Optional[BulkGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[BulkGetResponse]], ResultWrapper[BulkGetResponse]),
        )


class AsyncBulksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBulksResourceWithRawResponse:
        return AsyncBulksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBulksResourceWithStreamingResponse:
        return AsyncBulksResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        account_id: str,
        domain: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[BulkGetResponse]:
        """
        Get Multiple Domain Details

        Args:
          account_id: Identifier

          domain: Accepts multiple values, i.e. `?domain=cloudflare.com&domain=example.com`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/intel/domain/bulk",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"domain": domain}, bulk_get_params.BulkGetParams),
                post_parser=ResultWrapper[Optional[BulkGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[BulkGetResponse]], ResultWrapper[BulkGetResponse]),
        )


class BulksResourceWithRawResponse:
    def __init__(self, bulks: BulksResource) -> None:
        self._bulks = bulks

        self.get = to_raw_response_wrapper(
            bulks.get,
        )


class AsyncBulksResourceWithRawResponse:
    def __init__(self, bulks: AsyncBulksResource) -> None:
        self._bulks = bulks

        self.get = async_to_raw_response_wrapper(
            bulks.get,
        )


class BulksResourceWithStreamingResponse:
    def __init__(self, bulks: BulksResource) -> None:
        self._bulks = bulks

        self.get = to_streamed_response_wrapper(
            bulks.get,
        )


class AsyncBulksResourceWithStreamingResponse:
    def __init__(self, bulks: AsyncBulksResource) -> None:
        self._bulks = bulks

        self.get = async_to_streamed_response_wrapper(
            bulks.get,
        )
