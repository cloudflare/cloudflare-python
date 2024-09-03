# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.argo.tiered_caching_edit_response import TieredCachingEditResponse

from ..._wrappers import ResultWrapper

from ..._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type

from ..._base_client import make_request_options

from typing_extensions import Literal

from ...types.argo.tiered_caching_get_response import TieredCachingGetResponse

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
from ...types import shared_params
from ...types.argo import tiered_caching_edit_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["TieredCachingResource", "AsyncTieredCachingResource"]


class TieredCachingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TieredCachingResourceWithRawResponse:
        return TieredCachingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TieredCachingResourceWithStreamingResponse:
        return TieredCachingResourceWithStreamingResponse(self)

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
    ) -> Optional[TieredCachingEditResponse]:
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
        return self._patch(
            f"/zones/{zone_id}/argo/tiered_caching",
            body=maybe_transform({"value": value}, tiered_caching_edit_params.TieredCachingEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TieredCachingEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TieredCachingEditResponse]], ResultWrapper[TieredCachingEditResponse]),
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
    ) -> Optional[TieredCachingGetResponse]:
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
        return self._get(
            f"/zones/{zone_id}/argo/tiered_caching",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TieredCachingGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TieredCachingGetResponse]], ResultWrapper[TieredCachingGetResponse]),
        )


class AsyncTieredCachingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTieredCachingResourceWithRawResponse:
        return AsyncTieredCachingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTieredCachingResourceWithStreamingResponse:
        return AsyncTieredCachingResourceWithStreamingResponse(self)

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
    ) -> Optional[TieredCachingEditResponse]:
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
        return await self._patch(
            f"/zones/{zone_id}/argo/tiered_caching",
            body=await async_maybe_transform({"value": value}, tiered_caching_edit_params.TieredCachingEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TieredCachingEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TieredCachingEditResponse]], ResultWrapper[TieredCachingEditResponse]),
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
    ) -> Optional[TieredCachingGetResponse]:
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
        return await self._get(
            f"/zones/{zone_id}/argo/tiered_caching",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TieredCachingGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TieredCachingGetResponse]], ResultWrapper[TieredCachingGetResponse]),
        )


class TieredCachingResourceWithRawResponse:
    def __init__(self, tiered_caching: TieredCachingResource) -> None:
        self._tiered_caching = tiered_caching

        self.edit = to_raw_response_wrapper(
            tiered_caching.edit,
        )
        self.get = to_raw_response_wrapper(
            tiered_caching.get,
        )


class AsyncTieredCachingResourceWithRawResponse:
    def __init__(self, tiered_caching: AsyncTieredCachingResource) -> None:
        self._tiered_caching = tiered_caching

        self.edit = async_to_raw_response_wrapper(
            tiered_caching.edit,
        )
        self.get = async_to_raw_response_wrapper(
            tiered_caching.get,
        )


class TieredCachingResourceWithStreamingResponse:
    def __init__(self, tiered_caching: TieredCachingResource) -> None:
        self._tiered_caching = tiered_caching

        self.edit = to_streamed_response_wrapper(
            tiered_caching.edit,
        )
        self.get = to_streamed_response_wrapper(
            tiered_caching.get,
        )


class AsyncTieredCachingResourceWithStreamingResponse:
    def __init__(self, tiered_caching: AsyncTieredCachingResource) -> None:
        self._tiered_caching = tiered_caching

        self.edit = async_to_streamed_response_wrapper(
            tiered_caching.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            tiered_caching.get,
        )
