# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.argo import (
    TieredCachingTieredCachingGetTieredCachingSettingResponse,
    TieredCachingTieredCachingPatchTieredCachingSettingResponse,
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
from ...types.argo import tiered_caching_tiered_caching_patch_tiered_caching_setting_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["TieredCaching", "AsyncTieredCaching"]


class TieredCaching(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TieredCachingWithRawResponse:
        return TieredCachingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TieredCachingWithStreamingResponse:
        return TieredCachingWithStreamingResponse(self)

    def tiered_caching_get_tiered_caching_setting(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TieredCachingTieredCachingGetTieredCachingSettingResponse:
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
            TieredCachingTieredCachingGetTieredCachingSettingResponse,
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
                    Any, ResultWrapper[TieredCachingTieredCachingGetTieredCachingSettingResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def tiered_caching_patch_tiered_caching_setting(
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
    ) -> TieredCachingTieredCachingPatchTieredCachingSettingResponse:
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
            TieredCachingTieredCachingPatchTieredCachingSettingResponse,
            self._patch(
                f"/zones/{zone_id}/argo/tiered_caching",
                body=maybe_transform(
                    {"value": value},
                    tiered_caching_tiered_caching_patch_tiered_caching_setting_params.TieredCachingTieredCachingPatchTieredCachingSettingParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[TieredCachingTieredCachingPatchTieredCachingSettingResponse]
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

    async def tiered_caching_get_tiered_caching_setting(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TieredCachingTieredCachingGetTieredCachingSettingResponse:
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
            TieredCachingTieredCachingGetTieredCachingSettingResponse,
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
                    Any, ResultWrapper[TieredCachingTieredCachingGetTieredCachingSettingResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def tiered_caching_patch_tiered_caching_setting(
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
    ) -> TieredCachingTieredCachingPatchTieredCachingSettingResponse:
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
            TieredCachingTieredCachingPatchTieredCachingSettingResponse,
            await self._patch(
                f"/zones/{zone_id}/argo/tiered_caching",
                body=maybe_transform(
                    {"value": value},
                    tiered_caching_tiered_caching_patch_tiered_caching_setting_params.TieredCachingTieredCachingPatchTieredCachingSettingParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[TieredCachingTieredCachingPatchTieredCachingSettingResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class TieredCachingWithRawResponse:
    def __init__(self, tiered_caching: TieredCaching) -> None:
        self._tiered_caching = tiered_caching

        self.tiered_caching_get_tiered_caching_setting = to_raw_response_wrapper(
            tiered_caching.tiered_caching_get_tiered_caching_setting,
        )
        self.tiered_caching_patch_tiered_caching_setting = to_raw_response_wrapper(
            tiered_caching.tiered_caching_patch_tiered_caching_setting,
        )


class AsyncTieredCachingWithRawResponse:
    def __init__(self, tiered_caching: AsyncTieredCaching) -> None:
        self._tiered_caching = tiered_caching

        self.tiered_caching_get_tiered_caching_setting = async_to_raw_response_wrapper(
            tiered_caching.tiered_caching_get_tiered_caching_setting,
        )
        self.tiered_caching_patch_tiered_caching_setting = async_to_raw_response_wrapper(
            tiered_caching.tiered_caching_patch_tiered_caching_setting,
        )


class TieredCachingWithStreamingResponse:
    def __init__(self, tiered_caching: TieredCaching) -> None:
        self._tiered_caching = tiered_caching

        self.tiered_caching_get_tiered_caching_setting = to_streamed_response_wrapper(
            tiered_caching.tiered_caching_get_tiered_caching_setting,
        )
        self.tiered_caching_patch_tiered_caching_setting = to_streamed_response_wrapper(
            tiered_caching.tiered_caching_patch_tiered_caching_setting,
        )


class AsyncTieredCachingWithStreamingResponse:
    def __init__(self, tiered_caching: AsyncTieredCaching) -> None:
        self._tiered_caching = tiered_caching

        self.tiered_caching_get_tiered_caching_setting = async_to_streamed_response_wrapper(
            tiered_caching.tiered_caching_get_tiered_caching_setting,
        )
        self.tiered_caching_patch_tiered_caching_setting = async_to_streamed_response_wrapper(
            tiered_caching.tiered_caching_patch_tiered_caching_setting,
        )
