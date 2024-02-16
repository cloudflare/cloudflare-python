# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .._compat import cached_property

from ..types import CacheReserveCreateResponse, CacheReserveClearResponse

from typing import Type

from .._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from .._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from .._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ..types import shared_params
from .._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["CacheReserves", "AsyncCacheReserves"]


class CacheReserves(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CacheReservesWithRawResponse:
        return CacheReservesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CacheReservesWithStreamingResponse:
        return CacheReservesWithStreamingResponse(self)

    def create(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CacheReserveCreateResponse:
        """
        You can use Cache Reserve Clear to clear your Cache Reserve, but you must first
        disable Cache Reserve. In most cases, this will be accomplished within 24 hours.
        You cannot re-enable Cache Reserve while this process is ongoing. Keep in mind
        that you cannot undo or cancel this operation.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/cache/cache_reserve_clear",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CacheReserveCreateResponse], ResultWrapper[CacheReserveCreateResponse]),
        )

    def clear(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CacheReserveClearResponse:
        """
        You can use Cache Reserve Clear to clear your Cache Reserve, but you must first
        disable Cache Reserve. In most cases, this will be accomplished within 24 hours.
        You cannot re-enable Cache Reserve while this process is ongoing. Keep in mind
        that you cannot undo or cancel this operation.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/cache/cache_reserve_clear",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CacheReserveClearResponse], ResultWrapper[CacheReserveClearResponse]),
        )


class AsyncCacheReserves(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCacheReservesWithRawResponse:
        return AsyncCacheReservesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCacheReservesWithStreamingResponse:
        return AsyncCacheReservesWithStreamingResponse(self)

    async def create(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CacheReserveCreateResponse:
        """
        You can use Cache Reserve Clear to clear your Cache Reserve, but you must first
        disable Cache Reserve. In most cases, this will be accomplished within 24 hours.
        You cannot re-enable Cache Reserve while this process is ongoing. Keep in mind
        that you cannot undo or cancel this operation.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/cache/cache_reserve_clear",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CacheReserveCreateResponse], ResultWrapper[CacheReserveCreateResponse]),
        )

    async def clear(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CacheReserveClearResponse:
        """
        You can use Cache Reserve Clear to clear your Cache Reserve, but you must first
        disable Cache Reserve. In most cases, this will be accomplished within 24 hours.
        You cannot re-enable Cache Reserve while this process is ongoing. Keep in mind
        that you cannot undo or cancel this operation.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/cache/cache_reserve_clear",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CacheReserveClearResponse], ResultWrapper[CacheReserveClearResponse]),
        )


class CacheReservesWithRawResponse:
    def __init__(self, cache_reserves: CacheReserves) -> None:
        self._cache_reserves = cache_reserves

        self.create = to_raw_response_wrapper(
            cache_reserves.create,
        )
        self.clear = to_raw_response_wrapper(
            cache_reserves.clear,
        )


class AsyncCacheReservesWithRawResponse:
    def __init__(self, cache_reserves: AsyncCacheReserves) -> None:
        self._cache_reserves = cache_reserves

        self.create = async_to_raw_response_wrapper(
            cache_reserves.create,
        )
        self.clear = async_to_raw_response_wrapper(
            cache_reserves.clear,
        )


class CacheReservesWithStreamingResponse:
    def __init__(self, cache_reserves: CacheReserves) -> None:
        self._cache_reserves = cache_reserves

        self.create = to_streamed_response_wrapper(
            cache_reserves.create,
        )
        self.clear = to_streamed_response_wrapper(
            cache_reserves.clear,
        )


class AsyncCacheReservesWithStreamingResponse:
    def __init__(self, cache_reserves: AsyncCacheReserves) -> None:
        self._cache_reserves = cache_reserves

        self.create = async_to_streamed_response_wrapper(
            cache_reserves.create,
        )
        self.clear = async_to_streamed_response_wrapper(
            cache_reserves.clear,
        )
