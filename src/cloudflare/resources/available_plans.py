# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .._compat import cached_property

from ..types import AvailablePlanListResponse, AvailablePlanGetResponse

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
from typing import cast
from typing import cast

__all__ = ["AvailablePlans", "AsyncAvailablePlans"]


class AvailablePlans(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AvailablePlansWithRawResponse:
        return AvailablePlansWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AvailablePlansWithStreamingResponse:
        return AvailablePlansWithStreamingResponse(self)

    def list(
        self,
        zone_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AvailablePlanListResponse]:
        """
        Lists available plans the zone can subscribe to.

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
            f"/zones/{zone_identifier}/available_plans",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[AvailablePlanListResponse]], ResultWrapper[AvailablePlanListResponse]),
        )

    def get(
        self,
        plan_identifier: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AvailablePlanGetResponse:
        """
        Details of the available plan that the zone can subscribe to.

        Args:
          zone_identifier: Identifier

          plan_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not plan_identifier:
            raise ValueError(f"Expected a non-empty value for `plan_identifier` but received {plan_identifier!r}")
        return self._get(
            f"/zones/{zone_identifier}/available_plans/{plan_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AvailablePlanGetResponse], ResultWrapper[AvailablePlanGetResponse]),
        )


class AsyncAvailablePlans(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAvailablePlansWithRawResponse:
        return AsyncAvailablePlansWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAvailablePlansWithStreamingResponse:
        return AsyncAvailablePlansWithStreamingResponse(self)

    async def list(
        self,
        zone_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AvailablePlanListResponse]:
        """
        Lists available plans the zone can subscribe to.

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
            f"/zones/{zone_identifier}/available_plans",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[AvailablePlanListResponse]], ResultWrapper[AvailablePlanListResponse]),
        )

    async def get(
        self,
        plan_identifier: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AvailablePlanGetResponse:
        """
        Details of the available plan that the zone can subscribe to.

        Args:
          zone_identifier: Identifier

          plan_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not plan_identifier:
            raise ValueError(f"Expected a non-empty value for `plan_identifier` but received {plan_identifier!r}")
        return await self._get(
            f"/zones/{zone_identifier}/available_plans/{plan_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AvailablePlanGetResponse], ResultWrapper[AvailablePlanGetResponse]),
        )


class AvailablePlansWithRawResponse:
    def __init__(self, available_plans: AvailablePlans) -> None:
        self._available_plans = available_plans

        self.list = to_raw_response_wrapper(
            available_plans.list,
        )
        self.get = to_raw_response_wrapper(
            available_plans.get,
        )


class AsyncAvailablePlansWithRawResponse:
    def __init__(self, available_plans: AsyncAvailablePlans) -> None:
        self._available_plans = available_plans

        self.list = async_to_raw_response_wrapper(
            available_plans.list,
        )
        self.get = async_to_raw_response_wrapper(
            available_plans.get,
        )


class AvailablePlansWithStreamingResponse:
    def __init__(self, available_plans: AvailablePlans) -> None:
        self._available_plans = available_plans

        self.list = to_streamed_response_wrapper(
            available_plans.list,
        )
        self.get = to_streamed_response_wrapper(
            available_plans.get,
        )


class AsyncAvailablePlansWithStreamingResponse:
    def __init__(self, available_plans: AsyncAvailablePlans) -> None:
        self._available_plans = available_plans

        self.list = async_to_streamed_response_wrapper(
            available_plans.list,
        )
        self.get = async_to_streamed_response_wrapper(
            available_plans.get,
        )
