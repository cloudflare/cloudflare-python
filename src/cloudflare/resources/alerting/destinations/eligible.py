# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import (
    make_request_options,
)
from ....types.alerting.destinations.eligible_get_response import EligibleGetResponse

__all__ = ["EligibleResource", "AsyncEligibleResource"]


class EligibleResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EligibleResourceWithRawResponse:
        return EligibleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EligibleResourceWithStreamingResponse:
        return EligibleResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[EligibleGetResponse]:
        """
        Get a list of all delivery mechanism types for which an account is eligible.

        Args:
          account_id: The account id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            Optional[EligibleGetResponse],
            self._get(
                f"/accounts/{account_id}/alerting/v3/destinations/eligible",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[EligibleGetResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[EligibleGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncEligibleResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEligibleResourceWithRawResponse:
        return AsyncEligibleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEligibleResourceWithStreamingResponse:
        return AsyncEligibleResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[EligibleGetResponse]:
        """
        Get a list of all delivery mechanism types for which an account is eligible.

        Args:
          account_id: The account id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            Optional[EligibleGetResponse],
            await self._get(
                f"/accounts/{account_id}/alerting/v3/destinations/eligible",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[EligibleGetResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[EligibleGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class EligibleResourceWithRawResponse:
    def __init__(self, eligible: EligibleResource) -> None:
        self._eligible = eligible

        self.get = to_raw_response_wrapper(
            eligible.get,
        )


class AsyncEligibleResourceWithRawResponse:
    def __init__(self, eligible: AsyncEligibleResource) -> None:
        self._eligible = eligible

        self.get = async_to_raw_response_wrapper(
            eligible.get,
        )


class EligibleResourceWithStreamingResponse:
    def __init__(self, eligible: EligibleResource) -> None:
        self._eligible = eligible

        self.get = to_streamed_response_wrapper(
            eligible.get,
        )


class AsyncEligibleResourceWithStreamingResponse:
    def __init__(self, eligible: AsyncEligibleResource) -> None:
        self._eligible = eligible

        self.get = async_to_streamed_response_wrapper(
            eligible.get,
        )
