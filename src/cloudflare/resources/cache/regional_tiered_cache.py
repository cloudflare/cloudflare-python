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
    RegionalTieredCacheGetResponse,
    RegionalTieredCacheEditResponse,
    regional_tiered_cache_edit_params,
)
from ..._base_client import (
    make_request_options,
)

__all__ = ["RegionalTieredCache", "AsyncRegionalTieredCache"]


class RegionalTieredCache(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RegionalTieredCacheWithRawResponse:
        return RegionalTieredCacheWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RegionalTieredCacheWithStreamingResponse:
        return RegionalTieredCacheWithStreamingResponse(self)

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
    ) -> RegionalTieredCacheEditResponse:
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
            body=maybe_transform({"value": value}, regional_tiered_cache_edit_params.RegionalTieredCacheEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RegionalTieredCacheEditResponse], ResultWrapper[RegionalTieredCacheEditResponse]),
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
    ) -> RegionalTieredCacheGetResponse:
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
            cast_to=cast(Type[RegionalTieredCacheGetResponse], ResultWrapper[RegionalTieredCacheGetResponse]),
        )


class AsyncRegionalTieredCache(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRegionalTieredCacheWithRawResponse:
        return AsyncRegionalTieredCacheWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRegionalTieredCacheWithStreamingResponse:
        return AsyncRegionalTieredCacheWithStreamingResponse(self)

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
    ) -> RegionalTieredCacheEditResponse:
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
            body=await async_maybe_transform(
                {"value": value}, regional_tiered_cache_edit_params.RegionalTieredCacheEditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RegionalTieredCacheEditResponse], ResultWrapper[RegionalTieredCacheEditResponse]),
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
    ) -> RegionalTieredCacheGetResponse:
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
            cast_to=cast(Type[RegionalTieredCacheGetResponse], ResultWrapper[RegionalTieredCacheGetResponse]),
        )


class RegionalTieredCacheWithRawResponse:
    def __init__(self, regional_tiered_cache: RegionalTieredCache) -> None:
        self._regional_tiered_cache = regional_tiered_cache

        self.edit = to_raw_response_wrapper(
            regional_tiered_cache.edit,
        )
        self.get = to_raw_response_wrapper(
            regional_tiered_cache.get,
        )


class AsyncRegionalTieredCacheWithRawResponse:
    def __init__(self, regional_tiered_cache: AsyncRegionalTieredCache) -> None:
        self._regional_tiered_cache = regional_tiered_cache

        self.edit = async_to_raw_response_wrapper(
            regional_tiered_cache.edit,
        )
        self.get = async_to_raw_response_wrapper(
            regional_tiered_cache.get,
        )


class RegionalTieredCacheWithStreamingResponse:
    def __init__(self, regional_tiered_cache: RegionalTieredCache) -> None:
        self._regional_tiered_cache = regional_tiered_cache

        self.edit = to_streamed_response_wrapper(
            regional_tiered_cache.edit,
        )
        self.get = to_streamed_response_wrapper(
            regional_tiered_cache.get,
        )


class AsyncRegionalTieredCacheWithStreamingResponse:
    def __init__(self, regional_tiered_cache: AsyncRegionalTieredCache) -> None:
        self._regional_tiered_cache = regional_tiered_cache

        self.edit = async_to_streamed_response_wrapper(
            regional_tiered_cache.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            regional_tiered_cache.get,
        )
