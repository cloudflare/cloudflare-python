# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast
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
    SmartTieredCacheGetResponse,
    SmartTieredCacheEditResponse,
    SmartTieredCacheDeleteResponse,
    smart_tiered_cache_edit_params,
)
from ..._base_client import (
    make_request_options,
)

__all__ = ["SmartTieredCache", "AsyncSmartTieredCache"]


class SmartTieredCache(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SmartTieredCacheWithRawResponse:
        return SmartTieredCacheWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SmartTieredCacheWithStreamingResponse:
        return SmartTieredCacheWithStreamingResponse(self)

    def delete(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SmartTieredCacheDeleteResponse:
        """
        Remvoves enablement of Smart Tiered Cache

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            SmartTieredCacheDeleteResponse,
            self._delete(
                f"/zones/{zone_id}/cache/tiered_cache_smart_topology_enable",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SmartTieredCacheDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> SmartTieredCacheEditResponse:
        """
        Updates enablement of Tiered Cache

        Args:
          zone_id: Identifier

          value: Enables Tiered Cache.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            SmartTieredCacheEditResponse,
            self._patch(
                f"/zones/{zone_id}/cache/tiered_cache_smart_topology_enable",
                body=maybe_transform({"value": value}, smart_tiered_cache_edit_params.SmartTieredCacheEditParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SmartTieredCacheEditResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> SmartTieredCacheGetResponse:
        """
        Get Smart Tiered Cache setting

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            SmartTieredCacheGetResponse,
            self._get(
                f"/zones/{zone_id}/cache/tiered_cache_smart_topology_enable",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SmartTieredCacheGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncSmartTieredCache(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSmartTieredCacheWithRawResponse:
        return AsyncSmartTieredCacheWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSmartTieredCacheWithStreamingResponse:
        return AsyncSmartTieredCacheWithStreamingResponse(self)

    async def delete(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SmartTieredCacheDeleteResponse:
        """
        Remvoves enablement of Smart Tiered Cache

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            SmartTieredCacheDeleteResponse,
            await self._delete(
                f"/zones/{zone_id}/cache/tiered_cache_smart_topology_enable",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SmartTieredCacheDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> SmartTieredCacheEditResponse:
        """
        Updates enablement of Tiered Cache

        Args:
          zone_id: Identifier

          value: Enables Tiered Cache.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            SmartTieredCacheEditResponse,
            await self._patch(
                f"/zones/{zone_id}/cache/tiered_cache_smart_topology_enable",
                body=await async_maybe_transform(
                    {"value": value}, smart_tiered_cache_edit_params.SmartTieredCacheEditParams
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SmartTieredCacheEditResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> SmartTieredCacheGetResponse:
        """
        Get Smart Tiered Cache setting

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            SmartTieredCacheGetResponse,
            await self._get(
                f"/zones/{zone_id}/cache/tiered_cache_smart_topology_enable",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SmartTieredCacheGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class SmartTieredCacheWithRawResponse:
    def __init__(self, smart_tiered_cache: SmartTieredCache) -> None:
        self._smart_tiered_cache = smart_tiered_cache

        self.delete = to_raw_response_wrapper(
            smart_tiered_cache.delete,
        )
        self.edit = to_raw_response_wrapper(
            smart_tiered_cache.edit,
        )
        self.get = to_raw_response_wrapper(
            smart_tiered_cache.get,
        )


class AsyncSmartTieredCacheWithRawResponse:
    def __init__(self, smart_tiered_cache: AsyncSmartTieredCache) -> None:
        self._smart_tiered_cache = smart_tiered_cache

        self.delete = async_to_raw_response_wrapper(
            smart_tiered_cache.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            smart_tiered_cache.edit,
        )
        self.get = async_to_raw_response_wrapper(
            smart_tiered_cache.get,
        )


class SmartTieredCacheWithStreamingResponse:
    def __init__(self, smart_tiered_cache: SmartTieredCache) -> None:
        self._smart_tiered_cache = smart_tiered_cache

        self.delete = to_streamed_response_wrapper(
            smart_tiered_cache.delete,
        )
        self.edit = to_streamed_response_wrapper(
            smart_tiered_cache.edit,
        )
        self.get = to_streamed_response_wrapper(
            smart_tiered_cache.get,
        )


class AsyncSmartTieredCacheWithStreamingResponse:
    def __init__(self, smart_tiered_cache: AsyncSmartTieredCache) -> None:
        self._smart_tiered_cache = smart_tiered_cache

        self.delete = async_to_streamed_response_wrapper(
            smart_tiered_cache.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            smart_tiered_cache.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            smart_tiered_cache.get,
        )
