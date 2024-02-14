# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.caches import (
    TieredCacheSmartTopologyEnableDeleteResponse,
    TieredCacheSmartTopologyEnableSmartTieredCacheGetSmartTieredCacheSettingResponse,
    TieredCacheSmartTopologyEnableSmartTieredCachePatchSmartTieredCacheSettingResponse,
)

from typing_extensions import Literal

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
from ...types.caches import (
    tiered_cache_smart_topology_enable_smart_tiered_cache_patch_smart_tiered_cache_setting_params,
)
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["TieredCacheSmartTopologyEnables", "AsyncTieredCacheSmartTopologyEnables"]


class TieredCacheSmartTopologyEnables(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TieredCacheSmartTopologyEnablesWithRawResponse:
        return TieredCacheSmartTopologyEnablesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TieredCacheSmartTopologyEnablesWithStreamingResponse:
        return TieredCacheSmartTopologyEnablesWithStreamingResponse(self)

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
    ) -> TieredCacheSmartTopologyEnableDeleteResponse:
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
            TieredCacheSmartTopologyEnableDeleteResponse,
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
                    Any, ResultWrapper[TieredCacheSmartTopologyEnableDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def smart_tiered_cache_get_smart_tiered_cache_setting(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TieredCacheSmartTopologyEnableSmartTieredCacheGetSmartTieredCacheSettingResponse:
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
            TieredCacheSmartTopologyEnableSmartTieredCacheGetSmartTieredCacheSettingResponse,
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
                    Any, ResultWrapper[TieredCacheSmartTopologyEnableSmartTieredCacheGetSmartTieredCacheSettingResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def smart_tiered_cache_patch_smart_tiered_cache_setting(
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
    ) -> TieredCacheSmartTopologyEnableSmartTieredCachePatchSmartTieredCacheSettingResponse:
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
            TieredCacheSmartTopologyEnableSmartTieredCachePatchSmartTieredCacheSettingResponse,
            self._patch(
                f"/zones/{zone_id}/cache/tiered_cache_smart_topology_enable",
                body=maybe_transform(
                    {"value": value},
                    tiered_cache_smart_topology_enable_smart_tiered_cache_patch_smart_tiered_cache_setting_params.TieredCacheSmartTopologyEnableSmartTieredCachePatchSmartTieredCacheSettingParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any,
                    ResultWrapper[TieredCacheSmartTopologyEnableSmartTieredCachePatchSmartTieredCacheSettingResponse],
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncTieredCacheSmartTopologyEnables(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTieredCacheSmartTopologyEnablesWithRawResponse:
        return AsyncTieredCacheSmartTopologyEnablesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTieredCacheSmartTopologyEnablesWithStreamingResponse:
        return AsyncTieredCacheSmartTopologyEnablesWithStreamingResponse(self)

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
    ) -> TieredCacheSmartTopologyEnableDeleteResponse:
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
            TieredCacheSmartTopologyEnableDeleteResponse,
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
                    Any, ResultWrapper[TieredCacheSmartTopologyEnableDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def smart_tiered_cache_get_smart_tiered_cache_setting(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TieredCacheSmartTopologyEnableSmartTieredCacheGetSmartTieredCacheSettingResponse:
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
            TieredCacheSmartTopologyEnableSmartTieredCacheGetSmartTieredCacheSettingResponse,
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
                    Any, ResultWrapper[TieredCacheSmartTopologyEnableSmartTieredCacheGetSmartTieredCacheSettingResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def smart_tiered_cache_patch_smart_tiered_cache_setting(
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
    ) -> TieredCacheSmartTopologyEnableSmartTieredCachePatchSmartTieredCacheSettingResponse:
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
            TieredCacheSmartTopologyEnableSmartTieredCachePatchSmartTieredCacheSettingResponse,
            await self._patch(
                f"/zones/{zone_id}/cache/tiered_cache_smart_topology_enable",
                body=maybe_transform(
                    {"value": value},
                    tiered_cache_smart_topology_enable_smart_tiered_cache_patch_smart_tiered_cache_setting_params.TieredCacheSmartTopologyEnableSmartTieredCachePatchSmartTieredCacheSettingParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any,
                    ResultWrapper[TieredCacheSmartTopologyEnableSmartTieredCachePatchSmartTieredCacheSettingResponse],
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class TieredCacheSmartTopologyEnablesWithRawResponse:
    def __init__(self, tiered_cache_smart_topology_enables: TieredCacheSmartTopologyEnables) -> None:
        self._tiered_cache_smart_topology_enables = tiered_cache_smart_topology_enables

        self.delete = to_raw_response_wrapper(
            tiered_cache_smart_topology_enables.delete,
        )
        self.smart_tiered_cache_get_smart_tiered_cache_setting = to_raw_response_wrapper(
            tiered_cache_smart_topology_enables.smart_tiered_cache_get_smart_tiered_cache_setting,
        )
        self.smart_tiered_cache_patch_smart_tiered_cache_setting = to_raw_response_wrapper(
            tiered_cache_smart_topology_enables.smart_tiered_cache_patch_smart_tiered_cache_setting,
        )


class AsyncTieredCacheSmartTopologyEnablesWithRawResponse:
    def __init__(self, tiered_cache_smart_topology_enables: AsyncTieredCacheSmartTopologyEnables) -> None:
        self._tiered_cache_smart_topology_enables = tiered_cache_smart_topology_enables

        self.delete = async_to_raw_response_wrapper(
            tiered_cache_smart_topology_enables.delete,
        )
        self.smart_tiered_cache_get_smart_tiered_cache_setting = async_to_raw_response_wrapper(
            tiered_cache_smart_topology_enables.smart_tiered_cache_get_smart_tiered_cache_setting,
        )
        self.smart_tiered_cache_patch_smart_tiered_cache_setting = async_to_raw_response_wrapper(
            tiered_cache_smart_topology_enables.smart_tiered_cache_patch_smart_tiered_cache_setting,
        )


class TieredCacheSmartTopologyEnablesWithStreamingResponse:
    def __init__(self, tiered_cache_smart_topology_enables: TieredCacheSmartTopologyEnables) -> None:
        self._tiered_cache_smart_topology_enables = tiered_cache_smart_topology_enables

        self.delete = to_streamed_response_wrapper(
            tiered_cache_smart_topology_enables.delete,
        )
        self.smart_tiered_cache_get_smart_tiered_cache_setting = to_streamed_response_wrapper(
            tiered_cache_smart_topology_enables.smart_tiered_cache_get_smart_tiered_cache_setting,
        )
        self.smart_tiered_cache_patch_smart_tiered_cache_setting = to_streamed_response_wrapper(
            tiered_cache_smart_topology_enables.smart_tiered_cache_patch_smart_tiered_cache_setting,
        )


class AsyncTieredCacheSmartTopologyEnablesWithStreamingResponse:
    def __init__(self, tiered_cache_smart_topology_enables: AsyncTieredCacheSmartTopologyEnables) -> None:
        self._tiered_cache_smart_topology_enables = tiered_cache_smart_topology_enables

        self.delete = async_to_streamed_response_wrapper(
            tiered_cache_smart_topology_enables.delete,
        )
        self.smart_tiered_cache_get_smart_tiered_cache_setting = async_to_streamed_response_wrapper(
            tiered_cache_smart_topology_enables.smart_tiered_cache_get_smart_tiered_cache_setting,
        )
        self.smart_tiered_cache_patch_smart_tiered_cache_setting = async_to_streamed_response_wrapper(
            tiered_cache_smart_topology_enables.smart_tiered_cache_patch_smart_tiered_cache_setting,
        )
