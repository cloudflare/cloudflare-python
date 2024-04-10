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
from ...types.argo import TieredCachingGetResponse, TieredCachingEditResponse, tiered_caching_edit_params
from ..._base_client import (
    make_request_options,
)

__all__ = ["TieredCaching", "AsyncTieredCaching"]


class TieredCaching(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TieredCachingWithRawResponse:
        return TieredCachingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TieredCachingWithStreamingResponse:
        return TieredCachingWithStreamingResponse(self)

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
    ) -> TieredCachingEditResponse:
        """
        Updates enablement of Tiered Caching

        Args:
          zone_id: Identifier

          value: Enables Tiered Caching.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            TieredCachingEditResponse,
            self._patch(
                f"/zones/{zone_id}/argo/tiered_caching",
                body=maybe_transform({"value": value}, tiered_caching_edit_params.TieredCachingEditParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[TieredCachingEditResponse]
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
    ) -> TieredCachingGetResponse:
        """
        Get Tiered Caching setting

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
            TieredCachingGetResponse,
            self._get(
                f"/zones/{zone_id}/argo/tiered_caching",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[TieredCachingGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncTieredCaching(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTieredCachingWithRawResponse:
        return AsyncTieredCachingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTieredCachingWithStreamingResponse:
        return AsyncTieredCachingWithStreamingResponse(self)

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
    ) -> TieredCachingEditResponse:
        """
        Updates enablement of Tiered Caching

        Args:
          zone_id: Identifier

          value: Enables Tiered Caching.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            TieredCachingEditResponse,
            await self._patch(
                f"/zones/{zone_id}/argo/tiered_caching",
                body=await async_maybe_transform({"value": value}, tiered_caching_edit_params.TieredCachingEditParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[TieredCachingEditResponse]
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
    ) -> TieredCachingGetResponse:
        """
        Get Tiered Caching setting

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
            TieredCachingGetResponse,
            await self._get(
                f"/zones/{zone_id}/argo/tiered_caching",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[TieredCachingGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class TieredCachingWithRawResponse:
    def __init__(self, tiered_caching: TieredCaching) -> None:
        self._tiered_caching = tiered_caching

        self.edit = to_raw_response_wrapper(
            tiered_caching.edit,
        )
        self.get = to_raw_response_wrapper(
            tiered_caching.get,
        )


class AsyncTieredCachingWithRawResponse:
    def __init__(self, tiered_caching: AsyncTieredCaching) -> None:
        self._tiered_caching = tiered_caching

        self.edit = async_to_raw_response_wrapper(
            tiered_caching.edit,
        )
        self.get = async_to_raw_response_wrapper(
            tiered_caching.get,
        )


class TieredCachingWithStreamingResponse:
    def __init__(self, tiered_caching: TieredCaching) -> None:
        self._tiered_caching = tiered_caching

        self.edit = to_streamed_response_wrapper(
            tiered_caching.edit,
        )
        self.get = to_streamed_response_wrapper(
            tiered_caching.get,
        )


class AsyncTieredCachingWithStreamingResponse:
    def __init__(self, tiered_caching: AsyncTieredCaching) -> None:
        self._tiered_caching = tiered_caching

        self.edit = async_to_streamed_response_wrapper(
            tiered_caching.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            tiered_caching.get,
        )
