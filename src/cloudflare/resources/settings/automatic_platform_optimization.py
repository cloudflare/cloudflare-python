# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.settings import (
    AutomaticPlatformOptimizationUpdateResponse,
    AutomaticPlatformOptimizationGetResponse,
    automatic_platform_optimization_update_params,
)

from typing import Type, Optional

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ...types.settings import automatic_platform_optimization_update_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["AutomaticPlatformOptimization", "AsyncAutomaticPlatformOptimization"]


class AutomaticPlatformOptimization(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AutomaticPlatformOptimizationWithRawResponse:
        return AutomaticPlatformOptimizationWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AutomaticPlatformOptimizationWithStreamingResponse:
        return AutomaticPlatformOptimizationWithStreamingResponse(self)

    def update(
        self,
        zone_id: str,
        *,
        value: automatic_platform_optimization_update_params.Value,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AutomaticPlatformOptimizationUpdateResponse]:
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
                {"value": value},
                automatic_platform_optimization_update_params.AutomaticPlatformOptimizationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[AutomaticPlatformOptimizationUpdateResponse]],
                ResultWrapper[AutomaticPlatformOptimizationUpdateResponse],
            ),
        )

    def get(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AutomaticPlatformOptimizationGetResponse]:
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
                Type[Optional[AutomaticPlatformOptimizationGetResponse]],
                ResultWrapper[AutomaticPlatformOptimizationGetResponse],
            ),
        )


class AsyncAutomaticPlatformOptimization(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAutomaticPlatformOptimizationWithRawResponse:
        return AsyncAutomaticPlatformOptimizationWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAutomaticPlatformOptimizationWithStreamingResponse:
        return AsyncAutomaticPlatformOptimizationWithStreamingResponse(self)

    async def update(
        self,
        zone_id: str,
        *,
        value: automatic_platform_optimization_update_params.Value,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AutomaticPlatformOptimizationUpdateResponse]:
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
            body=maybe_transform(
                {"value": value},
                automatic_platform_optimization_update_params.AutomaticPlatformOptimizationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[AutomaticPlatformOptimizationUpdateResponse]],
                ResultWrapper[AutomaticPlatformOptimizationUpdateResponse],
            ),
        )

    async def get(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AutomaticPlatformOptimizationGetResponse]:
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
                Type[Optional[AutomaticPlatformOptimizationGetResponse]],
                ResultWrapper[AutomaticPlatformOptimizationGetResponse],
            ),
        )


class AutomaticPlatformOptimizationWithRawResponse:
    def __init__(self, automatic_platform_optimization: AutomaticPlatformOptimization) -> None:
        self._automatic_platform_optimization = automatic_platform_optimization

        self.update = to_raw_response_wrapper(
            automatic_platform_optimization.update,
        )
        self.get = to_raw_response_wrapper(
            automatic_platform_optimization.get,
        )


class AsyncAutomaticPlatformOptimizationWithRawResponse:
    def __init__(self, automatic_platform_optimization: AsyncAutomaticPlatformOptimization) -> None:
        self._automatic_platform_optimization = automatic_platform_optimization

        self.update = async_to_raw_response_wrapper(
            automatic_platform_optimization.update,
        )
        self.get = async_to_raw_response_wrapper(
            automatic_platform_optimization.get,
        )


class AutomaticPlatformOptimizationWithStreamingResponse:
    def __init__(self, automatic_platform_optimization: AutomaticPlatformOptimization) -> None:
        self._automatic_platform_optimization = automatic_platform_optimization

        self.update = to_streamed_response_wrapper(
            automatic_platform_optimization.update,
        )
        self.get = to_streamed_response_wrapper(
            automatic_platform_optimization.get,
        )


class AsyncAutomaticPlatformOptimizationWithStreamingResponse:
    def __init__(self, automatic_platform_optimization: AsyncAutomaticPlatformOptimization) -> None:
        self._automatic_platform_optimization = automatic_platform_optimization

        self.update = async_to_streamed_response_wrapper(
            automatic_platform_optimization.update,
        )
        self.get = async_to_streamed_response_wrapper(
            automatic_platform_optimization.get,
        )
