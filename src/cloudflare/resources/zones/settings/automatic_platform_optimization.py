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
from ....types.zones.settings import AutomaticPlatformOptimization, automatic_platform_optimization_edit_params
from ....types.zones.settings.automatic_platform_optimization import AutomaticPlatformOptimization
from ....types.zones.settings.automatic_platform_optimization_param import AutomaticPlatformOptimizationParam

__all__ = ["AutomaticPlatformOptimizationResource", "AsyncAutomaticPlatformOptimizationResource"]


class AutomaticPlatformOptimizationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AutomaticPlatformOptimizationResourceWithRawResponse:
        return AutomaticPlatformOptimizationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AutomaticPlatformOptimizationResourceWithStreamingResponse:
        return AutomaticPlatformOptimizationResourceWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        value: AutomaticPlatformOptimizationParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AutomaticPlatformOptimization]:
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
                post_parser=ResultWrapper[Optional[AutomaticPlatformOptimization]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AutomaticPlatformOptimization]], ResultWrapper[AutomaticPlatformOptimization]),
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
    ) -> Optional[AutomaticPlatformOptimization]:
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
                post_parser=ResultWrapper[Optional[AutomaticPlatformOptimization]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AutomaticPlatformOptimization]], ResultWrapper[AutomaticPlatformOptimization]),
        )


class AsyncAutomaticPlatformOptimizationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAutomaticPlatformOptimizationResourceWithRawResponse:
        return AsyncAutomaticPlatformOptimizationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAutomaticPlatformOptimizationResourceWithStreamingResponse:
        return AsyncAutomaticPlatformOptimizationResourceWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        value: AutomaticPlatformOptimizationParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AutomaticPlatformOptimization]:
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
                post_parser=ResultWrapper[Optional[AutomaticPlatformOptimization]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AutomaticPlatformOptimization]], ResultWrapper[AutomaticPlatformOptimization]),
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
    ) -> Optional[AutomaticPlatformOptimization]:
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
                post_parser=ResultWrapper[Optional[AutomaticPlatformOptimization]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AutomaticPlatformOptimization]], ResultWrapper[AutomaticPlatformOptimization]),
        )


class AutomaticPlatformOptimizationResourceWithRawResponse:
    def __init__(self, automatic_platform_optimization: AutomaticPlatformOptimizationResource) -> None:
        self._automatic_platform_optimization = automatic_platform_optimization

        self.edit = to_raw_response_wrapper(
            automatic_platform_optimization.edit,
        )
        self.get = to_raw_response_wrapper(
            automatic_platform_optimization.get,
        )


class AsyncAutomaticPlatformOptimizationResourceWithRawResponse:
    def __init__(self, automatic_platform_optimization: AsyncAutomaticPlatformOptimizationResource) -> None:
        self._automatic_platform_optimization = automatic_platform_optimization

        self.edit = async_to_raw_response_wrapper(
            automatic_platform_optimization.edit,
        )
        self.get = async_to_raw_response_wrapper(
            automatic_platform_optimization.get,
        )


class AutomaticPlatformOptimizationResourceWithStreamingResponse:
    def __init__(self, automatic_platform_optimization: AutomaticPlatformOptimizationResource) -> None:
        self._automatic_platform_optimization = automatic_platform_optimization

        self.edit = to_streamed_response_wrapper(
            automatic_platform_optimization.edit,
        )
        self.get = to_streamed_response_wrapper(
            automatic_platform_optimization.get,
        )


class AsyncAutomaticPlatformOptimizationResourceWithStreamingResponse:
    def __init__(self, automatic_platform_optimization: AsyncAutomaticPlatformOptimizationResource) -> None:
        self._automatic_platform_optimization = automatic_platform_optimization

        self.edit = async_to_streamed_response_wrapper(
            automatic_platform_optimization.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            automatic_platform_optimization.get,
        )
