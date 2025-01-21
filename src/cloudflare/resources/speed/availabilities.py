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
from ..._base_client import make_request_options
from ...types.speed.availability import Availability

__all__ = ["AvailabilitiesResource", "AsyncAvailabilitiesResource"]


class AvailabilitiesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AvailabilitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AvailabilitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AvailabilitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AvailabilitiesResourceWithStreamingResponse(self)

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
    ) -> Optional[Availability]:
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
                post_parser=ResultWrapper[Optional[Availability]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Availability]], ResultWrapper[Availability]),
        )


class AsyncAvailabilitiesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAvailabilitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAvailabilitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAvailabilitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAvailabilitiesResourceWithStreamingResponse(self)

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
    ) -> Optional[Availability]:
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
                post_parser=ResultWrapper[Optional[Availability]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Availability]], ResultWrapper[Availability]),
        )


class AvailabilitiesResourceWithRawResponse:
    def __init__(self, availabilities: AvailabilitiesResource) -> None:
        self._availabilities = availabilities

        self.list = to_raw_response_wrapper(
            availabilities.list,
        )


class AsyncAvailabilitiesResourceWithRawResponse:
    def __init__(self, availabilities: AsyncAvailabilitiesResource) -> None:
        self._availabilities = availabilities

        self.list = async_to_raw_response_wrapper(
            availabilities.list,
        )


class AvailabilitiesResourceWithStreamingResponse:
    def __init__(self, availabilities: AvailabilitiesResource) -> None:
        self._availabilities = availabilities

        self.list = to_streamed_response_wrapper(
            availabilities.list,
        )


class AsyncAvailabilitiesResourceWithStreamingResponse:
    def __init__(self, availabilities: AsyncAvailabilitiesResource) -> None:
        self._availabilities = availabilities

        self.list = async_to_streamed_response_wrapper(
            availabilities.list,
        )
