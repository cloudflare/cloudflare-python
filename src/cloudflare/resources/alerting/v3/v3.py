# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, Optional, cast

import httpx

from .policies import (
    Policies,
    AsyncPolicies,
    PoliciesWithRawResponse,
    AsyncPoliciesWithRawResponse,
    PoliciesWithStreamingResponse,
    AsyncPoliciesWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .histories import (
    Histories,
    AsyncHistories,
    HistoriesWithRawResponse,
    AsyncHistoriesWithRawResponse,
    HistoriesWithStreamingResponse,
    AsyncHistoriesWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from .destinations import (
    Destinations,
    AsyncDestinations,
    DestinationsWithRawResponse,
    AsyncDestinationsWithRawResponse,
    DestinationsWithStreamingResponse,
    AsyncDestinationsWithStreamingResponse,
)
from ...._base_client import (
    make_request_options,
)
from ....types.alerting import V3ListResponse
from .destinations.destinations import Destinations, AsyncDestinations

__all__ = ["V3", "AsyncV3"]


class V3(SyncAPIResource):
    @cached_property
    def destinations(self) -> Destinations:
        return Destinations(self._client)

    @cached_property
    def histories(self) -> Histories:
        return Histories(self._client)

    @cached_property
    def policies(self) -> Policies:
        return Policies(self._client)

    @cached_property
    def with_raw_response(self) -> V3WithRawResponse:
        return V3WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V3WithStreamingResponse:
        return V3WithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[V3ListResponse]:
        """
        Gets a list of all alert types for which an account is eligible.

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
            Optional[V3ListResponse],
            self._get(
                f"/accounts/{account_id}/alerting/v3/available_alerts",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[V3ListResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncV3(AsyncAPIResource):
    @cached_property
    def destinations(self) -> AsyncDestinations:
        return AsyncDestinations(self._client)

    @cached_property
    def histories(self) -> AsyncHistories:
        return AsyncHistories(self._client)

    @cached_property
    def policies(self) -> AsyncPolicies:
        return AsyncPolicies(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV3WithRawResponse:
        return AsyncV3WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV3WithStreamingResponse:
        return AsyncV3WithStreamingResponse(self)

    async def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[V3ListResponse]:
        """
        Gets a list of all alert types for which an account is eligible.

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
            Optional[V3ListResponse],
            await self._get(
                f"/accounts/{account_id}/alerting/v3/available_alerts",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[V3ListResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class V3WithRawResponse:
    def __init__(self, v3: V3) -> None:
        self._v3 = v3

        self.list = to_raw_response_wrapper(
            v3.list,
        )

    @cached_property
    def destinations(self) -> DestinationsWithRawResponse:
        return DestinationsWithRawResponse(self._v3.destinations)

    @cached_property
    def histories(self) -> HistoriesWithRawResponse:
        return HistoriesWithRawResponse(self._v3.histories)

    @cached_property
    def policies(self) -> PoliciesWithRawResponse:
        return PoliciesWithRawResponse(self._v3.policies)


class AsyncV3WithRawResponse:
    def __init__(self, v3: AsyncV3) -> None:
        self._v3 = v3

        self.list = async_to_raw_response_wrapper(
            v3.list,
        )

    @cached_property
    def destinations(self) -> AsyncDestinationsWithRawResponse:
        return AsyncDestinationsWithRawResponse(self._v3.destinations)

    @cached_property
    def histories(self) -> AsyncHistoriesWithRawResponse:
        return AsyncHistoriesWithRawResponse(self._v3.histories)

    @cached_property
    def policies(self) -> AsyncPoliciesWithRawResponse:
        return AsyncPoliciesWithRawResponse(self._v3.policies)


class V3WithStreamingResponse:
    def __init__(self, v3: V3) -> None:
        self._v3 = v3

        self.list = to_streamed_response_wrapper(
            v3.list,
        )

    @cached_property
    def destinations(self) -> DestinationsWithStreamingResponse:
        return DestinationsWithStreamingResponse(self._v3.destinations)

    @cached_property
    def histories(self) -> HistoriesWithStreamingResponse:
        return HistoriesWithStreamingResponse(self._v3.histories)

    @cached_property
    def policies(self) -> PoliciesWithStreamingResponse:
        return PoliciesWithStreamingResponse(self._v3.policies)


class AsyncV3WithStreamingResponse:
    def __init__(self, v3: AsyncV3) -> None:
        self._v3 = v3

        self.list = async_to_streamed_response_wrapper(
            v3.list,
        )

    @cached_property
    def destinations(self) -> AsyncDestinationsWithStreamingResponse:
        return AsyncDestinationsWithStreamingResponse(self._v3.destinations)

    @cached_property
    def histories(self) -> AsyncHistoriesWithStreamingResponse:
        return AsyncHistoriesWithStreamingResponse(self._v3.histories)

    @cached_property
    def policies(self) -> AsyncPoliciesWithStreamingResponse:
        return AsyncPoliciesWithStreamingResponse(self._v3.policies)
