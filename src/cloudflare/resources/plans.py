# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._compat import cached_property

from ..types.plans.available_rate_plan import AvailableRatePlan

from ..pagination import SyncSinglePage, AsyncSinglePage

from .._base_client import make_request_options, AsyncPaginator

from .._wrappers import ResultWrapper

from typing import Type

from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from .._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from .._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from .._resource import SyncAPIResource, AsyncAPIResource
from ..types import shared_params
from typing import cast
from typing import cast

__all__ = ["PlansResource", "AsyncPlansResource"]

class PlansResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PlansResourceWithRawResponse:
        return PlansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PlansResourceWithStreamingResponse:
        return PlansResourceWithStreamingResponse(self)

    def list(self,
    *,
    zone_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> SyncSinglePage[AvailableRatePlan]:
        """
        Lists available plans the zone can subscribe to.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
          raise ValueError(
            f'Expected a non-empty value for `zone_id` but received {zone_id!r}'
          )
        return self._get_api_list(
            f"/zones/{zone_id}/available_plans",
            page = SyncSinglePage[AvailableRatePlan],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            model=AvailableRatePlan,
        )

    def get(self,
    plan_identifier: str,
    *,
    zone_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AvailableRatePlan:
        """
        Details of the available plan that the zone can subscribe to.

        Args:
          zone_id: Identifier

          plan_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
          raise ValueError(
            f'Expected a non-empty value for `zone_id` but received {zone_id!r}'
          )
        if not plan_identifier:
          raise ValueError(
            f'Expected a non-empty value for `plan_identifier` but received {plan_identifier!r}'
          )
        return self._get(
            f"/zones/{zone_id}/available_plans/{plan_identifier}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[AvailableRatePlan]._unwrapper),
            cast_to=cast(Type[AvailableRatePlan], ResultWrapper[AvailableRatePlan]),
        )

class AsyncPlansResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPlansResourceWithRawResponse:
        return AsyncPlansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPlansResourceWithStreamingResponse:
        return AsyncPlansResourceWithStreamingResponse(self)

    def list(self,
    *,
    zone_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AsyncPaginator[AvailableRatePlan, AsyncSinglePage[AvailableRatePlan]]:
        """
        Lists available plans the zone can subscribe to.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
          raise ValueError(
            f'Expected a non-empty value for `zone_id` but received {zone_id!r}'
          )
        return self._get_api_list(
            f"/zones/{zone_id}/available_plans",
            page = AsyncSinglePage[AvailableRatePlan],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            model=AvailableRatePlan,
        )

    async def get(self,
    plan_identifier: str,
    *,
    zone_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AvailableRatePlan:
        """
        Details of the available plan that the zone can subscribe to.

        Args:
          zone_id: Identifier

          plan_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
          raise ValueError(
            f'Expected a non-empty value for `zone_id` but received {zone_id!r}'
          )
        if not plan_identifier:
          raise ValueError(
            f'Expected a non-empty value for `plan_identifier` but received {plan_identifier!r}'
          )
        return await self._get(
            f"/zones/{zone_id}/available_plans/{plan_identifier}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[AvailableRatePlan]._unwrapper),
            cast_to=cast(Type[AvailableRatePlan], ResultWrapper[AvailableRatePlan]),
        )

class PlansResourceWithRawResponse:
    def __init__(self, plans: PlansResource) -> None:
        self._plans = plans

        self.list = to_raw_response_wrapper(
            plans.list,
        )
        self.get = to_raw_response_wrapper(
            plans.get,
        )

class AsyncPlansResourceWithRawResponse:
    def __init__(self, plans: AsyncPlansResource) -> None:
        self._plans = plans

        self.list = async_to_raw_response_wrapper(
            plans.list,
        )
        self.get = async_to_raw_response_wrapper(
            plans.get,
        )

class PlansResourceWithStreamingResponse:
    def __init__(self, plans: PlansResource) -> None:
        self._plans = plans

        self.list = to_streamed_response_wrapper(
            plans.list,
        )
        self.get = to_streamed_response_wrapper(
            plans.get,
        )

class AsyncPlansResourceWithStreamingResponse:
    def __init__(self, plans: AsyncPlansResource) -> None:
        self._plans = plans

        self.list = async_to_streamed_response_wrapper(
            plans.list,
        )
        self.get = async_to_streamed_response_wrapper(
            plans.get,
        )