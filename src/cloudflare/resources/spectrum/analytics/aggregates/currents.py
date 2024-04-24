# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from ....._base_client import (
    make_request_options,
)
from .....types.spectrum.analytics.aggregates import current_get_params
from .....types.spectrum.analytics.aggregates.current_get_response import CurrentGetResponse

__all__ = ["CurrentsResource", "AsyncCurrentsResource"]


class CurrentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CurrentsResourceWithRawResponse:
        return CurrentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CurrentsResourceWithStreamingResponse:
        return CurrentsResourceWithStreamingResponse(self)

    def get(
        self,
        zone: str,
        *,
        app_id_param: str | NotGiven = NOT_GIVEN,
        app_id: str | NotGiven = NOT_GIVEN,
        colo_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CurrentGetResponse:
        """
        Retrieves analytics aggregated from the last minute of usage on Spectrum
        applications underneath a given zone.

        Args:
          zone: Identifier

          app_id_param: Comma-delimited list of Spectrum Application Id(s). If provided, the response
              will be limited to Spectrum Application Id(s) that match.

          app_id: Comma-delimited list of Spectrum Application Id(s). If provided, the response
              will be limited to Spectrum Application Id(s) that match.

          colo_name: Co-location identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone:
            raise ValueError(f"Expected a non-empty value for `zone` but received {zone!r}")
        return self._get(
            f"/zones/{zone}/spectrum/analytics/aggregate/current",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "app_id_param": app_id_param,
                        "app_id": app_id,
                        "colo_name": colo_name,
                    },
                    current_get_params.CurrentGetParams,
                ),
                post_parser=ResultWrapper[CurrentGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[CurrentGetResponse], ResultWrapper[CurrentGetResponse]),
        )


class AsyncCurrentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCurrentsResourceWithRawResponse:
        return AsyncCurrentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCurrentsResourceWithStreamingResponse:
        return AsyncCurrentsResourceWithStreamingResponse(self)

    async def get(
        self,
        zone: str,
        *,
        app_id_param: str | NotGiven = NOT_GIVEN,
        app_id: str | NotGiven = NOT_GIVEN,
        colo_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CurrentGetResponse:
        """
        Retrieves analytics aggregated from the last minute of usage on Spectrum
        applications underneath a given zone.

        Args:
          zone: Identifier

          app_id_param: Comma-delimited list of Spectrum Application Id(s). If provided, the response
              will be limited to Spectrum Application Id(s) that match.

          app_id: Comma-delimited list of Spectrum Application Id(s). If provided, the response
              will be limited to Spectrum Application Id(s) that match.

          colo_name: Co-location identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone:
            raise ValueError(f"Expected a non-empty value for `zone` but received {zone!r}")
        return await self._get(
            f"/zones/{zone}/spectrum/analytics/aggregate/current",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "app_id_param": app_id_param,
                        "app_id": app_id,
                        "colo_name": colo_name,
                    },
                    current_get_params.CurrentGetParams,
                ),
                post_parser=ResultWrapper[CurrentGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[CurrentGetResponse], ResultWrapper[CurrentGetResponse]),
        )


class CurrentsResourceWithRawResponse:
    def __init__(self, currents: CurrentsResource) -> None:
        self._currents = currents

        self.get = to_raw_response_wrapper(
            currents.get,
        )


class AsyncCurrentsResourceWithRawResponse:
    def __init__(self, currents: AsyncCurrentsResource) -> None:
        self._currents = currents

        self.get = async_to_raw_response_wrapper(
            currents.get,
        )


class CurrentsResourceWithStreamingResponse:
    def __init__(self, currents: CurrentsResource) -> None:
        self._currents = currents

        self.get = to_streamed_response_wrapper(
            currents.get,
        )


class AsyncCurrentsResourceWithStreamingResponse:
    def __init__(self, currents: AsyncCurrentsResource) -> None:
        self._currents = currents

        self.get = async_to_streamed_response_wrapper(
            currents.get,
        )
