# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.images.v1.stat import Stat

from ...._wrappers import ResultWrapper

from ...._base_client import make_request_options

from typing import Type

from ...._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from typing import cast
from typing import cast

__all__ = ["StatsResource", "AsyncStatsResource"]

class StatsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StatsResourceWithRawResponse:
        return StatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StatsResourceWithStreamingResponse:
        return StatsResourceWithStreamingResponse(self)

    def get(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Stat:
        """
        Fetch usage statistics details for Cloudflare Images.

        Args:
          account_id: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._get(
            f"/accounts/{account_id}/images/v1/stats",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Stat]._unwrapper),
            cast_to=cast(Type[Stat], ResultWrapper[Stat]),
        )

class AsyncStatsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStatsResourceWithRawResponse:
        return AsyncStatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStatsResourceWithStreamingResponse:
        return AsyncStatsResourceWithStreamingResponse(self)

    async def get(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Stat:
        """
        Fetch usage statistics details for Cloudflare Images.

        Args:
          account_id: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return await self._get(
            f"/accounts/{account_id}/images/v1/stats",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Stat]._unwrapper),
            cast_to=cast(Type[Stat], ResultWrapper[Stat]),
        )

class StatsResourceWithRawResponse:
    def __init__(self, stats: StatsResource) -> None:
        self._stats = stats

        self.get = to_raw_response_wrapper(
            stats.get,
        )

class AsyncStatsResourceWithRawResponse:
    def __init__(self, stats: AsyncStatsResource) -> None:
        self._stats = stats

        self.get = async_to_raw_response_wrapper(
            stats.get,
        )

class StatsResourceWithStreamingResponse:
    def __init__(self, stats: StatsResource) -> None:
        self._stats = stats

        self.get = to_streamed_response_wrapper(
            stats.get,
        )

class AsyncStatsResourceWithStreamingResponse:
    def __init__(self, stats: AsyncStatsResource) -> None:
        self._stats = stats

        self.get = async_to_streamed_response_wrapper(
            stats.get,
        )