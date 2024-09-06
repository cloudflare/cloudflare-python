# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._compat import cached_property

from .....types.zero_trust.dex.http_tests.http_details_percentiles import HTTPDetailsPercentiles

from ....._wrappers import ResultWrapper

from ....._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type, List

from ....._base_client import make_request_options

from ....._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from .....types import shared_params
from .....types.zero_trust.dex.http_tests import percentile_get_params
from typing import cast
from typing import cast

__all__ = ["PercentilesResource", "AsyncPercentilesResource"]


class PercentilesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PercentilesResourceWithRawResponse:
        return PercentilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PercentilesResourceWithStreamingResponse:
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

          from_: Start time for aggregate metrics in ISO format

          to: End time for aggregate metrics in ISO format

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
        return AsyncPercentilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPercentilesResourceWithStreamingResponse:
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

          from_: Start time for aggregate metrics in ISO format

          to: End time for aggregate metrics in ISO format

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
