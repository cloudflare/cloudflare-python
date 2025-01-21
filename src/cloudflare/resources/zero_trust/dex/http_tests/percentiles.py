# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Optional, cast

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
from ....._base_client import make_request_options
from .....types.zero_trust.dex.http_tests import percentile_get_params
from .....types.zero_trust.dex.http_tests.http_details_percentiles import HTTPDetailsPercentiles

__all__ = ["PercentilesResource", "AsyncPercentilesResource"]


class PercentilesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PercentilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PercentilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PercentilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PercentilesResourceWithStreamingResponse(self)

    def get(
        self,
        test_id: str,
        *,
        account_id: str,
        from_: str,
        to: str,
        colo: str | NotGiven = NOT_GIVEN,
        device_id: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[HTTPDetailsPercentiles]:
        """
        Get percentiles for an http test for a given time period between 1 hour and 7
        days.

        Args:
          test_id: API Resource UUID tag.

          from_: Start time for the query in ISO (RFC3339 - ISO 8601) format

          to: End time for the query in ISO (RFC3339 - ISO 8601) format

          colo: Optionally filter result stats to a Cloudflare colo. Cannot be used in
              combination with deviceId param.

          device_id: Optionally filter result stats to a specific device(s). Cannot be used in
              combination with colo param.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not test_id:
            raise ValueError(f"Expected a non-empty value for `test_id` but received {test_id!r}")
        return self._get(
            f"/accounts/{account_id}/dex/http-tests/{test_id}/percentiles",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                        "colo": colo,
                        "device_id": device_id,
                    },
                    percentile_get_params.PercentileGetParams,
                ),
                post_parser=ResultWrapper[Optional[HTTPDetailsPercentiles]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[HTTPDetailsPercentiles]], ResultWrapper[HTTPDetailsPercentiles]),
        )


class AsyncPercentilesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPercentilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPercentilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPercentilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPercentilesResourceWithStreamingResponse(self)

    async def get(
        self,
        test_id: str,
        *,
        account_id: str,
        from_: str,
        to: str,
        colo: str | NotGiven = NOT_GIVEN,
        device_id: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[HTTPDetailsPercentiles]:
        """
        Get percentiles for an http test for a given time period between 1 hour and 7
        days.

        Args:
          test_id: API Resource UUID tag.

          from_: Start time for the query in ISO (RFC3339 - ISO 8601) format

          to: End time for the query in ISO (RFC3339 - ISO 8601) format

          colo: Optionally filter result stats to a Cloudflare colo. Cannot be used in
              combination with deviceId param.

          device_id: Optionally filter result stats to a specific device(s). Cannot be used in
              combination with colo param.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not test_id:
            raise ValueError(f"Expected a non-empty value for `test_id` but received {test_id!r}")
        return await self._get(
            f"/accounts/{account_id}/dex/http-tests/{test_id}/percentiles",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                        "colo": colo,
                        "device_id": device_id,
                    },
                    percentile_get_params.PercentileGetParams,
                ),
                post_parser=ResultWrapper[Optional[HTTPDetailsPercentiles]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[HTTPDetailsPercentiles]], ResultWrapper[HTTPDetailsPercentiles]),
        )


class PercentilesResourceWithRawResponse:
    def __init__(self, percentiles: PercentilesResource) -> None:
        self._percentiles = percentiles

        self.get = to_raw_response_wrapper(
            percentiles.get,
        )


class AsyncPercentilesResourceWithRawResponse:
    def __init__(self, percentiles: AsyncPercentilesResource) -> None:
        self._percentiles = percentiles

        self.get = async_to_raw_response_wrapper(
            percentiles.get,
        )


class PercentilesResourceWithStreamingResponse:
    def __init__(self, percentiles: PercentilesResource) -> None:
        self._percentiles = percentiles

        self.get = to_streamed_response_wrapper(
            percentiles.get,
        )


class AsyncPercentilesResourceWithStreamingResponse:
    def __init__(self, percentiles: AsyncPercentilesResource) -> None:
        self._percentiles = percentiles

        self.get = async_to_streamed_response_wrapper(
            percentiles.get,
        )
