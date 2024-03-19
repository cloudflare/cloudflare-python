# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

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
from ....types.zones.settings import (
    ZonesAutomaticPlatformOptimization,
    ZonesAutomaticPlatformOptimizationParam,
    automatic_platform_optimization_edit_params,
)

__all__ = ["AutomaticPlatformOptimization", "AsyncAutomaticPlatformOptimization"]


class AutomaticPlatformOptimization(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AutomaticPlatformOptimizationWithRawResponse:
        return AutomaticPlatformOptimizationWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AutomaticPlatformOptimizationWithStreamingResponse:
        return AutomaticPlatformOptimizationWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        value: ZonesAutomaticPlatformOptimizationParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZonesAutomaticPlatformOptimization]:
        """
        [Automatic Platform Optimization for WordPress](https://developers.cloudflare.com/automatic-platform-optimization/)
        serves your WordPress site from Cloudflare's edge network and caches third-party
        fonts.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/automatic_platform_optimization",
            body=maybe_transform(
                {"value": value}, automatic_platform_optimization_edit_params.AutomaticPlatformOptimizationEditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ZonesAutomaticPlatformOptimization]], ResultWrapper[ZonesAutomaticPlatformOptimization]
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
    ) -> Optional[ZonesAutomaticPlatformOptimization]:
        """
        [Automatic Platform Optimization for WordPress](https://developers.cloudflare.com/automatic-platform-optimization/)
        serves your WordPress site from Cloudflare's edge network and caches third-party
        fonts.

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
            f"/zones/{zone_id}/settings/automatic_platform_optimization",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ZonesAutomaticPlatformOptimization]], ResultWrapper[ZonesAutomaticPlatformOptimization]
            ),
        )


class AsyncAutomaticPlatformOptimization(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAutomaticPlatformOptimizationWithRawResponse:
        return AsyncAutomaticPlatformOptimizationWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAutomaticPlatformOptimizationWithStreamingResponse:
        return AsyncAutomaticPlatformOptimizationWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        value: ZonesAutomaticPlatformOptimizationParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZonesAutomaticPlatformOptimization]:
        """
        [Automatic Platform Optimization for WordPress](https://developers.cloudflare.com/automatic-platform-optimization/)
        serves your WordPress site from Cloudflare's edge network and caches third-party
        fonts.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/automatic_platform_optimization",
            body=await async_maybe_transform(
                {"value": value}, automatic_platform_optimization_edit_params.AutomaticPlatformOptimizationEditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ZonesAutomaticPlatformOptimization]], ResultWrapper[ZonesAutomaticPlatformOptimization]
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
    ) -> Optional[ZonesAutomaticPlatformOptimization]:
        """
        [Automatic Platform Optimization for WordPress](https://developers.cloudflare.com/automatic-platform-optimization/)
        serves your WordPress site from Cloudflare's edge network and caches third-party
        fonts.

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
            f"/zones/{zone_id}/settings/automatic_platform_optimization",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ZonesAutomaticPlatformOptimization]], ResultWrapper[ZonesAutomaticPlatformOptimization]
            ),
        )


class AutomaticPlatformOptimizationWithRawResponse:
    def __init__(self, automatic_platform_optimization: AutomaticPlatformOptimization) -> None:
        self._automatic_platform_optimization = automatic_platform_optimization

        self.edit = to_raw_response_wrapper(
            automatic_platform_optimization.edit,
        )
        self.get = to_raw_response_wrapper(
            automatic_platform_optimization.get,
        )


class AsyncAutomaticPlatformOptimizationWithRawResponse:
    def __init__(self, automatic_platform_optimization: AsyncAutomaticPlatformOptimization) -> None:
        self._automatic_platform_optimization = automatic_platform_optimization

        self.edit = async_to_raw_response_wrapper(
            automatic_platform_optimization.edit,
        )
        self.get = async_to_raw_response_wrapper(
            automatic_platform_optimization.get,
        )


class AutomaticPlatformOptimizationWithStreamingResponse:
    def __init__(self, automatic_platform_optimization: AutomaticPlatformOptimization) -> None:
        self._automatic_platform_optimization = automatic_platform_optimization

        self.edit = to_streamed_response_wrapper(
            automatic_platform_optimization.edit,
        )
        self.get = to_streamed_response_wrapper(
            automatic_platform_optimization.get,
        )


class AsyncAutomaticPlatformOptimizationWithStreamingResponse:
    def __init__(self, automatic_platform_optimization: AsyncAutomaticPlatformOptimization) -> None:
        self._automatic_platform_optimization = automatic_platform_optimization

        self.edit = async_to_streamed_response_wrapper(
            automatic_platform_optimization.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            automatic_platform_optimization.get,
        )
