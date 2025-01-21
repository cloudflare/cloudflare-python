# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
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
from ...types.cache import regional_tiered_cache_edit_params
from ..._base_client import make_request_options
from ...types.cache.regional_tiered_cache_get_response import RegionalTieredCacheGetResponse
from ...types.cache.regional_tiered_cache_edit_response import RegionalTieredCacheEditResponse

__all__ = ["RegionalTieredCacheResource", "AsyncRegionalTieredCacheResource"]


class RegionalTieredCacheResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RegionalTieredCacheResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RegionalTieredCacheResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RegionalTieredCacheResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RegionalTieredCacheResourceWithStreamingResponse(self)

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
    ) -> Optional[RegionalTieredCacheEditResponse]:
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
                post_parser=ResultWrapper[Optional[RegionalTieredCacheEditResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[RegionalTieredCacheEditResponse]], ResultWrapper[RegionalTieredCacheEditResponse]
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
    ) -> Optional[RegionalTieredCacheGetResponse]:
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
                post_parser=ResultWrapper[Optional[RegionalTieredCacheGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RegionalTieredCacheGetResponse]], ResultWrapper[RegionalTieredCacheGetResponse]),
        )


class AsyncRegionalTieredCacheResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRegionalTieredCacheResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRegionalTieredCacheResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRegionalTieredCacheResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncRegionalTieredCacheResourceWithStreamingResponse(self)

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
    ) -> Optional[RegionalTieredCacheEditResponse]:
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
                post_parser=ResultWrapper[Optional[RegionalTieredCacheEditResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[RegionalTieredCacheEditResponse]], ResultWrapper[RegionalTieredCacheEditResponse]
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
    ) -> Optional[RegionalTieredCacheGetResponse]:
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
                post_parser=ResultWrapper[Optional[RegionalTieredCacheGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RegionalTieredCacheGetResponse]], ResultWrapper[RegionalTieredCacheGetResponse]),
        )


class RegionalTieredCacheResourceWithRawResponse:
    def __init__(self, regional_tiered_cache: RegionalTieredCacheResource) -> None:
        self._regional_tiered_cache = regional_tiered_cache

        self.edit = to_raw_response_wrapper(
            regional_tiered_cache.edit,
        )
        self.get = to_raw_response_wrapper(
            regional_tiered_cache.get,
        )


class AsyncRegionalTieredCacheResourceWithRawResponse:
    def __init__(self, regional_tiered_cache: AsyncRegionalTieredCacheResource) -> None:
        self._regional_tiered_cache = regional_tiered_cache

        self.edit = async_to_raw_response_wrapper(
            regional_tiered_cache.edit,
        )
        self.get = async_to_raw_response_wrapper(
            regional_tiered_cache.get,
        )


class RegionalTieredCacheResourceWithStreamingResponse:
    def __init__(self, regional_tiered_cache: RegionalTieredCacheResource) -> None:
        self._regional_tiered_cache = regional_tiered_cache

        self.edit = to_streamed_response_wrapper(
            regional_tiered_cache.edit,
        )
        self.get = to_streamed_response_wrapper(
            regional_tiered_cache.get,
        )


class AsyncRegionalTieredCacheResourceWithStreamingResponse:
    def __init__(self, regional_tiered_cache: AsyncRegionalTieredCacheResource) -> None:
        self._regional_tiered_cache = regional_tiered_cache

        self.edit = async_to_streamed_response_wrapper(
            regional_tiered_cache.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            regional_tiered_cache.get,
        )
