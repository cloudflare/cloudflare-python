# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._compat import cached_property

from ..types.rate_plans.rate_plan_get_response import RatePlanGetResponse

from .._wrappers import ResultWrapper

from typing import Optional, Type

from .._base_client import make_request_options

from .._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from .._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from .._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from .._resource import SyncAPIResource, AsyncAPIResource
from ..types import shared_params
from typing import cast
from typing import cast

__all__ = ["RatePlansResource", "AsyncRatePlansResource"]


class RatePlansResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RatePlansResourceWithRawResponse:
        return RatePlansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RatePlansResourceWithStreamingResponse:
        return RatePlansResourceWithStreamingResponse(self)

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
    ) -> Optional[RatePlanGetResponse]:
        """
        Lists all rate plans the zone can subscribe to.

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
            f"/zones/{zone_id}/available_rate_plans",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RatePlanGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RatePlanGetResponse]], ResultWrapper[RatePlanGetResponse]),
        )


class AsyncRatePlansResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRatePlansResourceWithRawResponse:
        return AsyncRatePlansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRatePlansResourceWithStreamingResponse:
        return AsyncRatePlansResourceWithStreamingResponse(self)

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
    ) -> Optional[RatePlanGetResponse]:
        """
        Lists all rate plans the zone can subscribe to.

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
            f"/zones/{zone_id}/available_rate_plans",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RatePlanGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RatePlanGetResponse]], ResultWrapper[RatePlanGetResponse]),
        )


class RatePlansResourceWithRawResponse:
    def __init__(self, rate_plans: RatePlansResource) -> None:
        self._rate_plans = rate_plans

        self.get = to_raw_response_wrapper(
            rate_plans.get,
        )


class AsyncRatePlansResourceWithRawResponse:
    def __init__(self, rate_plans: AsyncRatePlansResource) -> None:
        self._rate_plans = rate_plans

        self.get = async_to_raw_response_wrapper(
            rate_plans.get,
        )


class RatePlansResourceWithStreamingResponse:
    def __init__(self, rate_plans: RatePlansResource) -> None:
        self._rate_plans = rate_plans

        self.get = to_streamed_response_wrapper(
            rate_plans.get,
        )


class AsyncRatePlansResourceWithStreamingResponse:
    def __init__(self, rate_plans: AsyncRatePlansResource) -> None:
        self._rate_plans = rate_plans

        self.get = async_to_streamed_response_wrapper(
            rate_plans.get,
        )
