# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from ..types import (
    CacheRegionalTieredCachesResponse,
    CacheUpdateRegionalTieredCacheResponse,
    cache_update_regional_tiered_cache_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._wrappers import ResultWrapper
from .._base_client import (
    make_request_options,
)

__all__ = ["Cache", "AsyncCache"]


class Cache(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CacheWithRawResponse:
        return CacheWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CacheWithStreamingResponse:
        return CacheWithStreamingResponse(self)

    def regional_tiered_caches(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CacheRegionalTieredCachesResponse:
        """
        Instructs Cloudflare to check a regional hub data center on the way to your
        upper tier. This can help improve performance for smart and custom tiered cache
        topologies.

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
            f"/zones/{zone_id}/cache/regional_tiered_cache",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CacheRegionalTieredCachesResponse], ResultWrapper[CacheRegionalTieredCachesResponse]),
        )

    def update_regional_tiered_cache(
        self,
        zone_id: str,
        *,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CacheUpdateRegionalTieredCacheResponse:
        """
        Instructs Cloudflare to check a regional hub data center on the way to your
        upper tier. This can help improve performance for smart and custom tiered cache
        topologies.

        Args:
          zone_id: Identifier

          value: Value of the Regional Tiered Cache zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/cache/regional_tiered_cache",
            body=maybe_transform(
                {"value": value}, cache_update_regional_tiered_cache_params.CacheUpdateRegionalTieredCacheParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[CacheUpdateRegionalTieredCacheResponse], ResultWrapper[CacheUpdateRegionalTieredCacheResponse]
            ),
        )


class AsyncCache(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCacheWithRawResponse:
        return AsyncCacheWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCacheWithStreamingResponse:
        return AsyncCacheWithStreamingResponse(self)

    async def regional_tiered_caches(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CacheRegionalTieredCachesResponse:
        """
        Instructs Cloudflare to check a regional hub data center on the way to your
        upper tier. This can help improve performance for smart and custom tiered cache
        topologies.

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
            f"/zones/{zone_id}/cache/regional_tiered_cache",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CacheRegionalTieredCachesResponse], ResultWrapper[CacheRegionalTieredCachesResponse]),
        )

    async def update_regional_tiered_cache(
        self,
        zone_id: str,
        *,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CacheUpdateRegionalTieredCacheResponse:
        """
        Instructs Cloudflare to check a regional hub data center on the way to your
        upper tier. This can help improve performance for smart and custom tiered cache
        topologies.

        Args:
          zone_id: Identifier

          value: Value of the Regional Tiered Cache zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/cache/regional_tiered_cache",
            body=maybe_transform(
                {"value": value}, cache_update_regional_tiered_cache_params.CacheUpdateRegionalTieredCacheParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[CacheUpdateRegionalTieredCacheResponse], ResultWrapper[CacheUpdateRegionalTieredCacheResponse]
            ),
        )


class CacheWithRawResponse:
    def __init__(self, cache: Cache) -> None:
        self._cache = cache

        self.regional_tiered_caches = to_raw_response_wrapper(
            cache.regional_tiered_caches,
        )
        self.update_regional_tiered_cache = to_raw_response_wrapper(
            cache.update_regional_tiered_cache,
        )


class AsyncCacheWithRawResponse:
    def __init__(self, cache: AsyncCache) -> None:
        self._cache = cache

        self.regional_tiered_caches = async_to_raw_response_wrapper(
            cache.regional_tiered_caches,
        )
        self.update_regional_tiered_cache = async_to_raw_response_wrapper(
            cache.update_regional_tiered_cache,
        )


class CacheWithStreamingResponse:
    def __init__(self, cache: Cache) -> None:
        self._cache = cache

        self.regional_tiered_caches = to_streamed_response_wrapper(
            cache.regional_tiered_caches,
        )
        self.update_regional_tiered_cache = to_streamed_response_wrapper(
            cache.update_regional_tiered_cache,
        )


class AsyncCacheWithStreamingResponse:
    def __init__(self, cache: AsyncCache) -> None:
        self._cache = cache

        self.regional_tiered_caches = async_to_streamed_response_wrapper(
            cache.regional_tiered_caches,
        )
        self.update_regional_tiered_cache = async_to_streamed_response_wrapper(
            cache.update_regional_tiered_cache,
        )
