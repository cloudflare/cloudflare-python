# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
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
from ...types.caches import (
    CacheReserveListResponse,
    CacheReserveZoneCacheSettingsChangeCacheReserveSettingResponse,
    cache_reserve_zone_cache_settings_change_cache_reserve_setting_params,
)

__all__ = ["CacheReserves", "AsyncCacheReserves"]


class CacheReserves(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CacheReservesWithRawResponse:
        return CacheReservesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CacheReservesWithStreamingResponse:
        return CacheReservesWithStreamingResponse(self)

    def list(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CacheReserveListResponse:
        """
        Increase cache lifetimes by automatically storing all cacheable files into
        Cloudflare's persistent object storage buckets. Requires Cache Reserve
        subscription. Note: using Tiered Cache with Cache Reserve is highly recommended
        to reduce Reserve operations costs. See the
        [developer docs](https://developers.cloudflare.com/cache/about/cache-reserve)
        for more information.

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
            f"/zones/{zone_id}/cache/cache_reserve",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CacheReserveListResponse], ResultWrapper[CacheReserveListResponse]),
        )

    def zone_cache_settings_change_cache_reserve_setting(
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
    ) -> CacheReserveZoneCacheSettingsChangeCacheReserveSettingResponse:
        """
        Increase cache lifetimes by automatically storing all cacheable files into
        Cloudflare's persistent object storage buckets. Requires Cache Reserve
        subscription. Note: using Tiered Cache with Cache Reserve is highly recommended
        to reduce Reserve operations costs. See the
        [developer docs](https://developers.cloudflare.com/cache/about/cache-reserve)
        for more information.

        Args:
          zone_id: Identifier

          value: Value of the Cache Reserve zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/cache/cache_reserve",
            body=maybe_transform(
                {"value": value},
                cache_reserve_zone_cache_settings_change_cache_reserve_setting_params.CacheReserveZoneCacheSettingsChangeCacheReserveSettingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[CacheReserveZoneCacheSettingsChangeCacheReserveSettingResponse],
                ResultWrapper[CacheReserveZoneCacheSettingsChangeCacheReserveSettingResponse],
            ),
        )


class AsyncCacheReserves(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCacheReservesWithRawResponse:
        return AsyncCacheReservesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCacheReservesWithStreamingResponse:
        return AsyncCacheReservesWithStreamingResponse(self)

    async def list(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CacheReserveListResponse:
        """
        Increase cache lifetimes by automatically storing all cacheable files into
        Cloudflare's persistent object storage buckets. Requires Cache Reserve
        subscription. Note: using Tiered Cache with Cache Reserve is highly recommended
        to reduce Reserve operations costs. See the
        [developer docs](https://developers.cloudflare.com/cache/about/cache-reserve)
        for more information.

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
            f"/zones/{zone_id}/cache/cache_reserve",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CacheReserveListResponse], ResultWrapper[CacheReserveListResponse]),
        )

    async def zone_cache_settings_change_cache_reserve_setting(
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
    ) -> CacheReserveZoneCacheSettingsChangeCacheReserveSettingResponse:
        """
        Increase cache lifetimes by automatically storing all cacheable files into
        Cloudflare's persistent object storage buckets. Requires Cache Reserve
        subscription. Note: using Tiered Cache with Cache Reserve is highly recommended
        to reduce Reserve operations costs. See the
        [developer docs](https://developers.cloudflare.com/cache/about/cache-reserve)
        for more information.

        Args:
          zone_id: Identifier

          value: Value of the Cache Reserve zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/cache/cache_reserve",
            body=maybe_transform(
                {"value": value},
                cache_reserve_zone_cache_settings_change_cache_reserve_setting_params.CacheReserveZoneCacheSettingsChangeCacheReserveSettingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[CacheReserveZoneCacheSettingsChangeCacheReserveSettingResponse],
                ResultWrapper[CacheReserveZoneCacheSettingsChangeCacheReserveSettingResponse],
            ),
        )


class CacheReservesWithRawResponse:
    def __init__(self, cache_reserves: CacheReserves) -> None:
        self._cache_reserves = cache_reserves

        self.list = to_raw_response_wrapper(
            cache_reserves.list,
        )
        self.zone_cache_settings_change_cache_reserve_setting = to_raw_response_wrapper(
            cache_reserves.zone_cache_settings_change_cache_reserve_setting,
        )


class AsyncCacheReservesWithRawResponse:
    def __init__(self, cache_reserves: AsyncCacheReserves) -> None:
        self._cache_reserves = cache_reserves

        self.list = async_to_raw_response_wrapper(
            cache_reserves.list,
        )
        self.zone_cache_settings_change_cache_reserve_setting = async_to_raw_response_wrapper(
            cache_reserves.zone_cache_settings_change_cache_reserve_setting,
        )


class CacheReservesWithStreamingResponse:
    def __init__(self, cache_reserves: CacheReserves) -> None:
        self._cache_reserves = cache_reserves

        self.list = to_streamed_response_wrapper(
            cache_reserves.list,
        )
        self.zone_cache_settings_change_cache_reserve_setting = to_streamed_response_wrapper(
            cache_reserves.zone_cache_settings_change_cache_reserve_setting,
        )


class AsyncCacheReservesWithStreamingResponse:
    def __init__(self, cache_reserves: AsyncCacheReserves) -> None:
        self._cache_reserves = cache_reserves

        self.list = async_to_streamed_response_wrapper(
            cache_reserves.list,
        )
        self.zone_cache_settings_change_cache_reserve_setting = async_to_streamed_response_wrapper(
            cache_reserves.zone_cache_settings_change_cache_reserve_setting,
        )
