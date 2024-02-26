# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, cast
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
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
    TieredCacheSmartTopologyGetResponse,
    TieredCacheSmartTopologyEditResponse,
    TieredCacheSmartTopologyDeleteResponse,
    tiered_cache_smart_topology_edit_params,
)
from ..._base_client import (
    make_request_options,
)

__all__ = ["TieredCacheSmartTopology", "AsyncTieredCacheSmartTopology"]


class TieredCacheSmartTopology(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TieredCacheSmartTopologyWithRawResponse:
        return TieredCacheSmartTopologyWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TieredCacheSmartTopologyWithStreamingResponse:
        return TieredCacheSmartTopologyWithStreamingResponse(self)

    def delete(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TieredCacheSmartTopologyDeleteResponse:
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
            TieredCacheSmartTopologyDeleteResponse,
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
                    Any, ResultWrapper[TieredCacheSmartTopologyDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def edit(
        self,
        zone_id: str,
        *,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TieredCacheSmartTopologyEditResponse:
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
            TieredCacheSmartTopologyEditResponse,
            self._patch(
                f"/zones/{zone_id}/cache/tiered_cache_smart_topology_enable",
                body=maybe_transform(
                    {"value": value}, tiered_cache_smart_topology_edit_params.TieredCacheSmartTopologyEditParams
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[TieredCacheSmartTopologyEditResponse]
                ),  # Union types cannot be passed in as arguments in the type system
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
    ) -> TieredCacheSmartTopologyGetResponse:
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
            TieredCacheSmartTopologyGetResponse,
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
                    Any, ResultWrapper[TieredCacheSmartTopologyGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncTieredCacheSmartTopology(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTieredCacheSmartTopologyWithRawResponse:
        return AsyncTieredCacheSmartTopologyWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTieredCacheSmartTopologyWithStreamingResponse:
        return AsyncTieredCacheSmartTopologyWithStreamingResponse(self)

    async def delete(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TieredCacheSmartTopologyDeleteResponse:
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
            TieredCacheSmartTopologyDeleteResponse,
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
                    Any, ResultWrapper[TieredCacheSmartTopologyDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def edit(
        self,
        zone_id: str,
        *,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TieredCacheSmartTopologyEditResponse:
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
            TieredCacheSmartTopologyEditResponse,
            await self._patch(
                f"/zones/{zone_id}/cache/tiered_cache_smart_topology_enable",
                body=maybe_transform(
                    {"value": value}, tiered_cache_smart_topology_edit_params.TieredCacheSmartTopologyEditParams
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[TieredCacheSmartTopologyEditResponse]
                ),  # Union types cannot be passed in as arguments in the type system
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
    ) -> TieredCacheSmartTopologyGetResponse:
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
            TieredCacheSmartTopologyGetResponse,
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
                    Any, ResultWrapper[TieredCacheSmartTopologyGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class TieredCacheSmartTopologyWithRawResponse:
    def __init__(self, tiered_cache_smart_topology: TieredCacheSmartTopology) -> None:
        self._tiered_cache_smart_topology = tiered_cache_smart_topology

        self.delete = to_raw_response_wrapper(
            tiered_cache_smart_topology.delete,
        )
        self.edit = to_raw_response_wrapper(
            tiered_cache_smart_topology.edit,
        )
        self.get = to_raw_response_wrapper(
            tiered_cache_smart_topology.get,
        )


class AsyncTieredCacheSmartTopologyWithRawResponse:
    def __init__(self, tiered_cache_smart_topology: AsyncTieredCacheSmartTopology) -> None:
        self._tiered_cache_smart_topology = tiered_cache_smart_topology

        self.delete = async_to_raw_response_wrapper(
            tiered_cache_smart_topology.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            tiered_cache_smart_topology.edit,
        )
        self.get = async_to_raw_response_wrapper(
            tiered_cache_smart_topology.get,
        )


class TieredCacheSmartTopologyWithStreamingResponse:
    def __init__(self, tiered_cache_smart_topology: TieredCacheSmartTopology) -> None:
        self._tiered_cache_smart_topology = tiered_cache_smart_topology

        self.delete = to_streamed_response_wrapper(
            tiered_cache_smart_topology.delete,
        )
        self.edit = to_streamed_response_wrapper(
            tiered_cache_smart_topology.edit,
        )
        self.get = to_streamed_response_wrapper(
            tiered_cache_smart_topology.get,
        )


class AsyncTieredCacheSmartTopologyWithStreamingResponse:
    def __init__(self, tiered_cache_smart_topology: AsyncTieredCacheSmartTopology) -> None:
        self._tiered_cache_smart_topology = tiered_cache_smart_topology

        self.delete = async_to_streamed_response_wrapper(
            tiered_cache_smart_topology.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            tiered_cache_smart_topology.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            tiered_cache_smart_topology.get,
        )
