# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...types.cache import (
    CacheReserveGetResponse,
    CacheReserveEditResponse,
    CacheReserveClearResponse,
    CacheReserveStatusResponse,
    cache_reserve_edit_params,
)
from ..._base_client import (
    make_request_options,
)

__all__ = ["CacheReserve", "AsyncCacheReserve"]


class CacheReserve(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CacheReserveWithRawResponse:
        return CacheReserveWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CacheReserveWithStreamingResponse:
        return CacheReserveWithStreamingResponse(self)

    def clear(
        self,
        *,
        zone_id: str,
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
        return self._post(
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
    ) -> CacheReserveEditResponse:
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
            body=maybe_transform({"value": value}, cache_reserve_edit_params.CacheReserveEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CacheReserveEditResponse], ResultWrapper[CacheReserveEditResponse]),
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
    ) -> CacheReserveGetResponse:
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
            cast_to=cast(Type[CacheReserveGetResponse], ResultWrapper[CacheReserveGetResponse]),
        )

    def status(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CacheReserveStatusResponse:
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
            cast_to=cast(Type[CacheReserveStatusResponse], ResultWrapper[CacheReserveStatusResponse]),
        )


class AsyncCacheReserve(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCacheReserveWithRawResponse:
        return AsyncCacheReserveWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCacheReserveWithStreamingResponse:
        return AsyncCacheReserveWithStreamingResponse(self)

    async def clear(
        self,
        *,
        zone_id: str,
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
        return await self._post(
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
    ) -> CacheReserveEditResponse:
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
            body=await async_maybe_transform({"value": value}, cache_reserve_edit_params.CacheReserveEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CacheReserveEditResponse], ResultWrapper[CacheReserveEditResponse]),
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
    ) -> CacheReserveGetResponse:
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
            cast_to=cast(Type[CacheReserveGetResponse], ResultWrapper[CacheReserveGetResponse]),
        )

    async def status(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CacheReserveStatusResponse:
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
            cast_to=cast(Type[CacheReserveStatusResponse], ResultWrapper[CacheReserveStatusResponse]),
        )


class CacheReserveWithRawResponse:
    def __init__(self, cache_reserve: CacheReserve) -> None:
        self._cache_reserve = cache_reserve

        self.clear = to_raw_response_wrapper(
            cache_reserve.clear,
        )
        self.edit = to_raw_response_wrapper(
            cache_reserve.edit,
        )
        self.get = to_raw_response_wrapper(
            cache_reserve.get,
        )
        self.status = to_raw_response_wrapper(
            cache_reserve.status,
        )


class AsyncCacheReserveWithRawResponse:
    def __init__(self, cache_reserve: AsyncCacheReserve) -> None:
        self._cache_reserve = cache_reserve

        self.clear = async_to_raw_response_wrapper(
            cache_reserve.clear,
        )
        self.edit = async_to_raw_response_wrapper(
            cache_reserve.edit,
        )
        self.get = async_to_raw_response_wrapper(
            cache_reserve.get,
        )
        self.status = async_to_raw_response_wrapper(
            cache_reserve.status,
        )


class CacheReserveWithStreamingResponse:
    def __init__(self, cache_reserve: CacheReserve) -> None:
        self._cache_reserve = cache_reserve

        self.clear = to_streamed_response_wrapper(
            cache_reserve.clear,
        )
        self.edit = to_streamed_response_wrapper(
            cache_reserve.edit,
        )
        self.get = to_streamed_response_wrapper(
            cache_reserve.get,
        )
        self.status = to_streamed_response_wrapper(
            cache_reserve.status,
        )


class AsyncCacheReserveWithStreamingResponse:
    def __init__(self, cache_reserve: AsyncCacheReserve) -> None:
        self._cache_reserve = cache_reserve

        self.clear = async_to_streamed_response_wrapper(
            cache_reserve.clear,
        )
        self.edit = async_to_streamed_response_wrapper(
            cache_reserve.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            cache_reserve.get,
        )
        self.status = async_to_streamed_response_wrapper(
            cache_reserve.status,
        )
