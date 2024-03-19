# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

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
from ....types.zones.settings import ZonesSortQueryStringForCache, sort_query_string_for_cache_edit_params

__all__ = ["SortQueryStringForCache", "AsyncSortQueryStringForCache"]


class SortQueryStringForCache(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SortQueryStringForCacheWithRawResponse:
        return SortQueryStringForCacheWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SortQueryStringForCacheWithStreamingResponse:
        return SortQueryStringForCacheWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZonesSortQueryStringForCache]:
        """
        Cloudflare will treat files with the same query strings as the same file in
        cache, regardless of the order of the query strings. This is limited to
        Enterprise Zones.

        Args:
          zone_id: Identifier

          value: Value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/sort_query_string_for_cache",
            body=maybe_transform(
                {"value": value}, sort_query_string_for_cache_edit_params.SortQueryStringForCacheEditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesSortQueryStringForCache]], ResultWrapper[ZonesSortQueryStringForCache]),
        )

    def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZonesSortQueryStringForCache]:
        """
        Cloudflare will treat files with the same query strings as the same file in
        cache, regardless of the order of the query strings. This is limited to
        Enterprise Zones.

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
            f"/zones/{zone_id}/settings/sort_query_string_for_cache",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesSortQueryStringForCache]], ResultWrapper[ZonesSortQueryStringForCache]),
        )


class AsyncSortQueryStringForCache(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSortQueryStringForCacheWithRawResponse:
        return AsyncSortQueryStringForCacheWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSortQueryStringForCacheWithStreamingResponse:
        return AsyncSortQueryStringForCacheWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZonesSortQueryStringForCache]:
        """
        Cloudflare will treat files with the same query strings as the same file in
        cache, regardless of the order of the query strings. This is limited to
        Enterprise Zones.

        Args:
          zone_id: Identifier

          value: Value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/sort_query_string_for_cache",
            body=await async_maybe_transform(
                {"value": value}, sort_query_string_for_cache_edit_params.SortQueryStringForCacheEditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesSortQueryStringForCache]], ResultWrapper[ZonesSortQueryStringForCache]),
        )

    async def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZonesSortQueryStringForCache]:
        """
        Cloudflare will treat files with the same query strings as the same file in
        cache, regardless of the order of the query strings. This is limited to
        Enterprise Zones.

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
            f"/zones/{zone_id}/settings/sort_query_string_for_cache",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesSortQueryStringForCache]], ResultWrapper[ZonesSortQueryStringForCache]),
        )


class SortQueryStringForCacheWithRawResponse:
    def __init__(self, sort_query_string_for_cache: SortQueryStringForCache) -> None:
        self._sort_query_string_for_cache = sort_query_string_for_cache

        self.edit = to_raw_response_wrapper(
            sort_query_string_for_cache.edit,
        )
        self.get = to_raw_response_wrapper(
            sort_query_string_for_cache.get,
        )


class AsyncSortQueryStringForCacheWithRawResponse:
    def __init__(self, sort_query_string_for_cache: AsyncSortQueryStringForCache) -> None:
        self._sort_query_string_for_cache = sort_query_string_for_cache

        self.edit = async_to_raw_response_wrapper(
            sort_query_string_for_cache.edit,
        )
        self.get = async_to_raw_response_wrapper(
            sort_query_string_for_cache.get,
        )


class SortQueryStringForCacheWithStreamingResponse:
    def __init__(self, sort_query_string_for_cache: SortQueryStringForCache) -> None:
        self._sort_query_string_for_cache = sort_query_string_for_cache

        self.edit = to_streamed_response_wrapper(
            sort_query_string_for_cache.edit,
        )
        self.get = to_streamed_response_wrapper(
            sort_query_string_for_cache.get,
        )


class AsyncSortQueryStringForCacheWithStreamingResponse:
    def __init__(self, sort_query_string_for_cache: AsyncSortQueryStringForCache) -> None:
        self._sort_query_string_for_cache = sort_query_string_for_cache

        self.edit = async_to_streamed_response_wrapper(
            sort_query_string_for_cache.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            sort_query_string_for_cache.get,
        )
