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
from ...types.cache import smart_tiered_cache_edit_params
from ..._base_client import make_request_options
from ...types.cache.smart_tiered_cache_get_response import SmartTieredCacheGetResponse
from ...types.cache.smart_tiered_cache_edit_response import SmartTieredCacheEditResponse
from ...types.cache.smart_tiered_cache_delete_response import SmartTieredCacheDeleteResponse

__all__ = ["SmartTieredCacheResource", "AsyncSmartTieredCacheResource"]


class SmartTieredCacheResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SmartTieredCacheResourceWithRawResponse:
        return SmartTieredCacheResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SmartTieredCacheResourceWithStreamingResponse:
        return SmartTieredCacheResourceWithStreamingResponse(self)

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
        return self._delete(
            f"/zones/{zone_id}/cache/tiered_cache_smart_topology_enable",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SmartTieredCacheDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[SmartTieredCacheDeleteResponse], ResultWrapper[SmartTieredCacheDeleteResponse]),
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

          value: Enable or disable the Smart Tiered Cache

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/cache/tiered_cache_smart_topology_enable",
            body=maybe_transform({"value": value}, smart_tiered_cache_edit_params.SmartTieredCacheEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SmartTieredCacheEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[SmartTieredCacheEditResponse], ResultWrapper[SmartTieredCacheEditResponse]),
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
        return self._get(
            f"/zones/{zone_id}/cache/tiered_cache_smart_topology_enable",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SmartTieredCacheGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[SmartTieredCacheGetResponse], ResultWrapper[SmartTieredCacheGetResponse]),
        )


class AsyncSmartTieredCacheResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSmartTieredCacheResourceWithRawResponse:
        return AsyncSmartTieredCacheResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSmartTieredCacheResourceWithStreamingResponse:
        return AsyncSmartTieredCacheResourceWithStreamingResponse(self)

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
        return await self._delete(
            f"/zones/{zone_id}/cache/tiered_cache_smart_topology_enable",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SmartTieredCacheDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[SmartTieredCacheDeleteResponse], ResultWrapper[SmartTieredCacheDeleteResponse]),
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

          value: Enable or disable the Smart Tiered Cache

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/cache/tiered_cache_smart_topology_enable",
            body=await async_maybe_transform(
                {"value": value}, smart_tiered_cache_edit_params.SmartTieredCacheEditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SmartTieredCacheEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[SmartTieredCacheEditResponse], ResultWrapper[SmartTieredCacheEditResponse]),
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
        return await self._get(
            f"/zones/{zone_id}/cache/tiered_cache_smart_topology_enable",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SmartTieredCacheGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[SmartTieredCacheGetResponse], ResultWrapper[SmartTieredCacheGetResponse]),
        )


class SmartTieredCacheResourceWithRawResponse:
    def __init__(self, smart_tiered_cache: SmartTieredCacheResource) -> None:
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


class AsyncSmartTieredCacheResourceWithRawResponse:
    def __init__(self, smart_tiered_cache: AsyncSmartTieredCacheResource) -> None:
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


class SmartTieredCacheResourceWithStreamingResponse:
    def __init__(self, smart_tiered_cache: SmartTieredCacheResource) -> None:
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


class AsyncSmartTieredCacheResourceWithStreamingResponse:
    def __init__(self, smart_tiered_cache: AsyncSmartTieredCacheResource) -> None:
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
