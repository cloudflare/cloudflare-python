# File generated from our OpenAPI spec by Stainless.

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
    SmartTieredCachedGetResponse,
    SmartTieredCachedEditResponse,
    SmartTieredCachedDeleteResponse,
    smart_tiered_cached_edit_params,
)
from ..._base_client import (
    make_request_options,
)

__all__ = ["SmartTieredCached", "AsyncSmartTieredCached"]


class SmartTieredCached(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SmartTieredCachedWithRawResponse:
        return SmartTieredCachedWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SmartTieredCachedWithStreamingResponse:
        return SmartTieredCachedWithStreamingResponse(self)

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
    ) -> SmartTieredCachedDeleteResponse:
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
            SmartTieredCachedDeleteResponse,
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
                    Any, ResultWrapper[SmartTieredCachedDeleteResponse]
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
    ) -> SmartTieredCachedEditResponse:
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
            SmartTieredCachedEditResponse,
            self._patch(
                f"/zones/{zone_id}/cache/tiered_cache_smart_topology_enable",
                body=maybe_transform({"value": value}, smart_tiered_cached_edit_params.SmartTieredCachedEditParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SmartTieredCachedEditResponse]
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
    ) -> SmartTieredCachedGetResponse:
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
            SmartTieredCachedGetResponse,
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
                    Any, ResultWrapper[SmartTieredCachedGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncSmartTieredCached(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSmartTieredCachedWithRawResponse:
        return AsyncSmartTieredCachedWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSmartTieredCachedWithStreamingResponse:
        return AsyncSmartTieredCachedWithStreamingResponse(self)

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
    ) -> SmartTieredCachedDeleteResponse:
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
            SmartTieredCachedDeleteResponse,
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
                    Any, ResultWrapper[SmartTieredCachedDeleteResponse]
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
    ) -> SmartTieredCachedEditResponse:
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
            SmartTieredCachedEditResponse,
            await self._patch(
                f"/zones/{zone_id}/cache/tiered_cache_smart_topology_enable",
                body=await async_maybe_transform(
                    {"value": value}, smart_tiered_cached_edit_params.SmartTieredCachedEditParams
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SmartTieredCachedEditResponse]
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
    ) -> SmartTieredCachedGetResponse:
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
            SmartTieredCachedGetResponse,
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
                    Any, ResultWrapper[SmartTieredCachedGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class SmartTieredCachedWithRawResponse:
    def __init__(self, smart_tiered_cached: SmartTieredCached) -> None:
        self._smart_tiered_cached = smart_tiered_cached

        self.delete = to_raw_response_wrapper(
            smart_tiered_cached.delete,
        )
        self.edit = to_raw_response_wrapper(
            smart_tiered_cached.edit,
        )
        self.get = to_raw_response_wrapper(
            smart_tiered_cached.get,
        )


class AsyncSmartTieredCachedWithRawResponse:
    def __init__(self, smart_tiered_cached: AsyncSmartTieredCached) -> None:
        self._smart_tiered_cached = smart_tiered_cached

        self.delete = async_to_raw_response_wrapper(
            smart_tiered_cached.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            smart_tiered_cached.edit,
        )
        self.get = async_to_raw_response_wrapper(
            smart_tiered_cached.get,
        )


class SmartTieredCachedWithStreamingResponse:
    def __init__(self, smart_tiered_cached: SmartTieredCached) -> None:
        self._smart_tiered_cached = smart_tiered_cached

        self.delete = to_streamed_response_wrapper(
            smart_tiered_cached.delete,
        )
        self.edit = to_streamed_response_wrapper(
            smart_tiered_cached.edit,
        )
        self.get = to_streamed_response_wrapper(
            smart_tiered_cached.get,
        )


class AsyncSmartTieredCachedWithStreamingResponse:
    def __init__(self, smart_tiered_cached: AsyncSmartTieredCached) -> None:
        self._smart_tiered_cached = smart_tiered_cached

        self.delete = async_to_streamed_response_wrapper(
            smart_tiered_cached.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            smart_tiered_cached.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            smart_tiered_cached.get,
        )
