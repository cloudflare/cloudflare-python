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
from ....types.zones.settings import sort_query_string_for_cache_edit_params
from ....types.zones.settings.sort_query_string_for_cache import SortQueryStringForCache

__all__ = ["SortQueryStringForCacheResource", "AsyncSortQueryStringForCacheResource"]


class SortQueryStringForCacheResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SortQueryStringForCacheResourceWithRawResponse:
        return SortQueryStringForCacheResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SortQueryStringForCacheResourceWithStreamingResponse:
        return SortQueryStringForCacheResourceWithStreamingResponse(self)

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
    ) -> Optional[SortQueryStringForCache]:
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
                post_parser=ResultWrapper[Optional[SortQueryStringForCache]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SortQueryStringForCache]], ResultWrapper[SortQueryStringForCache]),
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
    ) -> Optional[SortQueryStringForCache]:
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
                post_parser=ResultWrapper[Optional[SortQueryStringForCache]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SortQueryStringForCache]], ResultWrapper[SortQueryStringForCache]),
        )


class AsyncSortQueryStringForCacheResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSortQueryStringForCacheResourceWithRawResponse:
        return AsyncSortQueryStringForCacheResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSortQueryStringForCacheResourceWithStreamingResponse:
        return AsyncSortQueryStringForCacheResourceWithStreamingResponse(self)

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
    ) -> Optional[SortQueryStringForCache]:
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
                post_parser=ResultWrapper[Optional[SortQueryStringForCache]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SortQueryStringForCache]], ResultWrapper[SortQueryStringForCache]),
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
    ) -> Optional[SortQueryStringForCache]:
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
                post_parser=ResultWrapper[Optional[SortQueryStringForCache]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SortQueryStringForCache]], ResultWrapper[SortQueryStringForCache]),
        )


class SortQueryStringForCacheResourceWithRawResponse:
    def __init__(self, sort_query_string_for_cache: SortQueryStringForCacheResource) -> None:
        self._sort_query_string_for_cache = sort_query_string_for_cache

        self.edit = to_raw_response_wrapper(
            sort_query_string_for_cache.edit,
        )
        self.get = to_raw_response_wrapper(
            sort_query_string_for_cache.get,
        )


class AsyncSortQueryStringForCacheResourceWithRawResponse:
    def __init__(self, sort_query_string_for_cache: AsyncSortQueryStringForCacheResource) -> None:
        self._sort_query_string_for_cache = sort_query_string_for_cache

        self.edit = async_to_raw_response_wrapper(
            sort_query_string_for_cache.edit,
        )
        self.get = async_to_raw_response_wrapper(
            sort_query_string_for_cache.get,
        )


class SortQueryStringForCacheResourceWithStreamingResponse:
    def __init__(self, sort_query_string_for_cache: SortQueryStringForCacheResource) -> None:
        self._sort_query_string_for_cache = sort_query_string_for_cache

        self.edit = to_streamed_response_wrapper(
            sort_query_string_for_cache.edit,
        )
        self.get = to_streamed_response_wrapper(
            sort_query_string_for_cache.get,
        )


class AsyncSortQueryStringForCacheResourceWithStreamingResponse:
    def __init__(self, sort_query_string_for_cache: AsyncSortQueryStringForCacheResource) -> None:
        self._sort_query_string_for_cache = sort_query_string_for_cache

        self.edit = async_to_streamed_response_wrapper(
            sort_query_string_for_cache.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            sort_query_string_for_cache.get,
        )
