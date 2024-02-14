# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .._compat import cached_property

from ..types import AvailableRatePlanZoneRatePlanListAvailableRatePlansResponse

from typing import Type, Optional

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
from .._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ..types import shared_params
from .._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["AvailableRatePlans", "AsyncAvailableRatePlans"]


class AvailableRatePlans(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AvailableRatePlansWithRawResponse:
        return AvailableRatePlansWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AvailableRatePlansWithStreamingResponse:
        return AvailableRatePlansWithStreamingResponse(self)

    def zone_rate_plan_list_available_rate_plans(
        self,
        zone_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AvailableRatePlanZoneRatePlanListAvailableRatePlansResponse]:
        """
        Lists all rate plans the zone can subscribe to.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._get(
            f"/zones/{zone_identifier}/available_rate_plans",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[AvailableRatePlanZoneRatePlanListAvailableRatePlansResponse]],
                ResultWrapper[AvailableRatePlanZoneRatePlanListAvailableRatePlansResponse],
            ),
        )


class AsyncAvailableRatePlans(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAvailableRatePlansWithRawResponse:
        return AsyncAvailableRatePlansWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAvailableRatePlansWithStreamingResponse:
        return AsyncAvailableRatePlansWithStreamingResponse(self)

    async def zone_rate_plan_list_available_rate_plans(
        self,
        zone_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AvailableRatePlanZoneRatePlanListAvailableRatePlansResponse]:
        """
        Lists all rate plans the zone can subscribe to.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._get(
            f"/zones/{zone_identifier}/available_rate_plans",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[AvailableRatePlanZoneRatePlanListAvailableRatePlansResponse]],
                ResultWrapper[AvailableRatePlanZoneRatePlanListAvailableRatePlansResponse],
            ),
        )


class AvailableRatePlansWithRawResponse:
    def __init__(self, available_rate_plans: AvailableRatePlans) -> None:
        self._available_rate_plans = available_rate_plans

        self.zone_rate_plan_list_available_rate_plans = to_raw_response_wrapper(
            available_rate_plans.zone_rate_plan_list_available_rate_plans,
        )


class AsyncAvailableRatePlansWithRawResponse:
    def __init__(self, available_rate_plans: AsyncAvailableRatePlans) -> None:
        self._available_rate_plans = available_rate_plans

        self.zone_rate_plan_list_available_rate_plans = async_to_raw_response_wrapper(
            available_rate_plans.zone_rate_plan_list_available_rate_plans,
        )


class AvailableRatePlansWithStreamingResponse:
    def __init__(self, available_rate_plans: AvailableRatePlans) -> None:
        self._available_rate_plans = available_rate_plans

        self.zone_rate_plan_list_available_rate_plans = to_streamed_response_wrapper(
            available_rate_plans.zone_rate_plan_list_available_rate_plans,
        )


class AsyncAvailableRatePlansWithStreamingResponse:
    def __init__(self, available_rate_plans: AsyncAvailableRatePlans) -> None:
        self._available_rate_plans = available_rate_plans

        self.zone_rate_plan_list_available_rate_plans = async_to_streamed_response_wrapper(
            available_rate_plans.zone_rate_plan_list_available_rate_plans,
        )
