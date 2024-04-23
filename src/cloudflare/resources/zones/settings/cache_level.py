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
from ....types.zones.settings import cache_level_edit_params
from ....types.zones.settings.cache_level import CacheLevel

__all__ = ["CacheLevelResource", "AsyncCacheLevelResource"]


class CacheLevelResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CacheLevelResourceWithRawResponse:
        return CacheLevelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CacheLevelResourceWithStreamingResponse:
        return CacheLevelResourceWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        value: Literal["aggressive", "basic", "simplified"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CacheLevel]:
        """Cache Level functions based off the setting level.

        The basic setting will cache
        most static resources (i.e., css, images, and JavaScript). The simplified
        setting will ignore the query string when delivering a cached resource. The
        aggressive setting will cache all static resources, including ones with a query
        string. (https://support.cloudflare.com/hc/en-us/articles/200168256).

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
            f"/zones/{zone_id}/settings/cache_level",
            body=maybe_transform({"value": value}, cache_level_edit_params.CacheLevelEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CacheLevel]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CacheLevel]], ResultWrapper[CacheLevel]),
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
    ) -> Optional[CacheLevel]:
        """Cache Level functions based off the setting level.

        The basic setting will cache
        most static resources (i.e., css, images, and JavaScript). The simplified
        setting will ignore the query string when delivering a cached resource. The
        aggressive setting will cache all static resources, including ones with a query
        string. (https://support.cloudflare.com/hc/en-us/articles/200168256).

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
            f"/zones/{zone_id}/settings/cache_level",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CacheLevel]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CacheLevel]], ResultWrapper[CacheLevel]),
        )


class AsyncCacheLevelResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCacheLevelResourceWithRawResponse:
        return AsyncCacheLevelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCacheLevelResourceWithStreamingResponse:
        return AsyncCacheLevelResourceWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        value: Literal["aggressive", "basic", "simplified"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CacheLevel]:
        """Cache Level functions based off the setting level.

        The basic setting will cache
        most static resources (i.e., css, images, and JavaScript). The simplified
        setting will ignore the query string when delivering a cached resource. The
        aggressive setting will cache all static resources, including ones with a query
        string. (https://support.cloudflare.com/hc/en-us/articles/200168256).

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
            f"/zones/{zone_id}/settings/cache_level",
            body=await async_maybe_transform({"value": value}, cache_level_edit_params.CacheLevelEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CacheLevel]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CacheLevel]], ResultWrapper[CacheLevel]),
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
    ) -> Optional[CacheLevel]:
        """Cache Level functions based off the setting level.

        The basic setting will cache
        most static resources (i.e., css, images, and JavaScript). The simplified
        setting will ignore the query string when delivering a cached resource. The
        aggressive setting will cache all static resources, including ones with a query
        string. (https://support.cloudflare.com/hc/en-us/articles/200168256).

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
            f"/zones/{zone_id}/settings/cache_level",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CacheLevel]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CacheLevel]], ResultWrapper[CacheLevel]),
        )


class CacheLevelResourceWithRawResponse:
    def __init__(self, cache_level: CacheLevelResource) -> None:
        self._cache_level = cache_level

        self.edit = to_raw_response_wrapper(
            cache_level.edit,
        )
        self.get = to_raw_response_wrapper(
            cache_level.get,
        )


class AsyncCacheLevelResourceWithRawResponse:
    def __init__(self, cache_level: AsyncCacheLevelResource) -> None:
        self._cache_level = cache_level

        self.edit = async_to_raw_response_wrapper(
            cache_level.edit,
        )
        self.get = async_to_raw_response_wrapper(
            cache_level.get,
        )


class CacheLevelResourceWithStreamingResponse:
    def __init__(self, cache_level: CacheLevelResource) -> None:
        self._cache_level = cache_level

        self.edit = to_streamed_response_wrapper(
            cache_level.edit,
        )
        self.get = to_streamed_response_wrapper(
            cache_level.get,
        )


class AsyncCacheLevelResourceWithStreamingResponse:
    def __init__(self, cache_level: AsyncCacheLevelResource) -> None:
        self._cache_level = cache_level

        self.edit = async_to_streamed_response_wrapper(
            cache_level.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            cache_level.get,
        )
