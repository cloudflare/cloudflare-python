# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...types.speed import ObservatoryAvailabilities
from ..._base_client import (
    make_request_options,
)

__all__ = ["Availabilities", "AsyncAvailabilities"]


class Availabilities(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AvailabilitiesWithRawResponse:
        return AvailabilitiesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AvailabilitiesWithStreamingResponse:
        return AvailabilitiesWithStreamingResponse(self)

    def list(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ObservatoryAvailabilities]:
        """
        Retrieves quota for all plans, as well as the current zone quota.

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
            f"/zones/{zone_id}/speed_api/availabilities",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ObservatoryAvailabilities]], ResultWrapper[ObservatoryAvailabilities]),
        )


class AsyncAvailabilities(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAvailabilitiesWithRawResponse:
        return AsyncAvailabilitiesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAvailabilitiesWithStreamingResponse:
        return AsyncAvailabilitiesWithStreamingResponse(self)

    async def list(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ObservatoryAvailabilities]:
        """
        Retrieves quota for all plans, as well as the current zone quota.

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
            f"/zones/{zone_id}/speed_api/availabilities",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ObservatoryAvailabilities]], ResultWrapper[ObservatoryAvailabilities]),
        )


class AvailabilitiesWithRawResponse:
    def __init__(self, availabilities: Availabilities) -> None:
        self._availabilities = availabilities

        self.list = to_raw_response_wrapper(
            availabilities.list,
        )


class AsyncAvailabilitiesWithRawResponse:
    def __init__(self, availabilities: AsyncAvailabilities) -> None:
        self._availabilities = availabilities

        self.list = async_to_raw_response_wrapper(
            availabilities.list,
        )


class AvailabilitiesWithStreamingResponse:
    def __init__(self, availabilities: Availabilities) -> None:
        self._availabilities = availabilities

        self.list = to_streamed_response_wrapper(
            availabilities.list,
        )


class AsyncAvailabilitiesWithStreamingResponse:
    def __init__(self, availabilities: AsyncAvailabilities) -> None:
        self._availabilities = availabilities

        self.list = async_to_streamed_response_wrapper(
            availabilities.list,
        )
