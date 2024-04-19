# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, cast
from typing_extensions import Literal

import httpx

from .summary import (
    Summary,
    AsyncSummary,
    SummaryWithRawResponse,
    AsyncSummaryWithRawResponse,
    SummaryWithStreamingResponse,
    AsyncSummaryWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from .behaviours import (
    Behaviours,
    AsyncBehaviours,
    BehavioursWithRawResponse,
    AsyncBehavioursWithRawResponse,
    BehavioursWithStreamingResponse,
    AsyncBehavioursWithStreamingResponse,
)
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
from ....types.zero_trust import RiskScoringGetResponse, RiskScoringResetResponse, risk_scoring_get_params

__all__ = ["RiskScoring", "AsyncRiskScoring"]


class RiskScoring(SyncAPIResource):
    @cached_property
    def behaviours(self) -> Behaviours:
        return Behaviours(self._client)

    @cached_property
    def summary(self) -> Summary:
        return Summary(self._client)

    @cached_property
    def with_raw_response(self) -> RiskScoringWithRawResponse:
        return RiskScoringWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RiskScoringWithStreamingResponse:
        return RiskScoringWithStreamingResponse(self)

    def get(
        self,
        user_id: str,
        *,
        account_identifier: str,
        direction: Literal["desc", "asc"] | NotGiven = NOT_GIVEN,
        order_by: Literal["timestamp", "risk_level"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RiskScoringGetResponse:
        """
        Get risk event/score information for a specific user

        Args:
          account_identifier: Identifier

          user_id: The ID for a user

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            f"/accounts/{account_identifier}/zt_risk_scoring/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "order_by": order_by,
                        "page": page,
                        "per_page": per_page,
                    },
                    risk_scoring_get_params.RiskScoringGetParams,
                ),
                post_parser=ResultWrapper[RiskScoringGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[RiskScoringGetResponse], ResultWrapper[RiskScoringGetResponse]),
        )

    def reset(
        self,
        user_id: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RiskScoringResetResponse:
        """
        Clear the risk score for a particular user

        Args:
          account_identifier: Identifier

          user_id: The ID for a user

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return cast(
            RiskScoringResetResponse,
            self._post(
                f"/accounts/{account_identifier}/zt_risk_scoring/{user_id}/reset",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[RiskScoringResetResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RiskScoringResetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncRiskScoring(AsyncAPIResource):
    @cached_property
    def behaviours(self) -> AsyncBehaviours:
        return AsyncBehaviours(self._client)

    @cached_property
    def summary(self) -> AsyncSummary:
        return AsyncSummary(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRiskScoringWithRawResponse:
        return AsyncRiskScoringWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRiskScoringWithStreamingResponse:
        return AsyncRiskScoringWithStreamingResponse(self)

    async def get(
        self,
        user_id: str,
        *,
        account_identifier: str,
        direction: Literal["desc", "asc"] | NotGiven = NOT_GIVEN,
        order_by: Literal["timestamp", "risk_level"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RiskScoringGetResponse:
        """
        Get risk event/score information for a specific user

        Args:
          account_identifier: Identifier

          user_id: The ID for a user

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            f"/accounts/{account_identifier}/zt_risk_scoring/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "direction": direction,
                        "order_by": order_by,
                        "page": page,
                        "per_page": per_page,
                    },
                    risk_scoring_get_params.RiskScoringGetParams,
                ),
                post_parser=ResultWrapper[RiskScoringGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[RiskScoringGetResponse], ResultWrapper[RiskScoringGetResponse]),
        )

    async def reset(
        self,
        user_id: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RiskScoringResetResponse:
        """
        Clear the risk score for a particular user

        Args:
          account_identifier: Identifier

          user_id: The ID for a user

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return cast(
            RiskScoringResetResponse,
            await self._post(
                f"/accounts/{account_identifier}/zt_risk_scoring/{user_id}/reset",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[RiskScoringResetResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RiskScoringResetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class RiskScoringWithRawResponse:
    def __init__(self, risk_scoring: RiskScoring) -> None:
        self._risk_scoring = risk_scoring

        self.get = to_raw_response_wrapper(
            risk_scoring.get,
        )
        self.reset = to_raw_response_wrapper(
            risk_scoring.reset,
        )

    @cached_property
    def behaviours(self) -> BehavioursWithRawResponse:
        return BehavioursWithRawResponse(self._risk_scoring.behaviours)

    @cached_property
    def summary(self) -> SummaryWithRawResponse:
        return SummaryWithRawResponse(self._risk_scoring.summary)


class AsyncRiskScoringWithRawResponse:
    def __init__(self, risk_scoring: AsyncRiskScoring) -> None:
        self._risk_scoring = risk_scoring

        self.get = async_to_raw_response_wrapper(
            risk_scoring.get,
        )
        self.reset = async_to_raw_response_wrapper(
            risk_scoring.reset,
        )

    @cached_property
    def behaviours(self) -> AsyncBehavioursWithRawResponse:
        return AsyncBehavioursWithRawResponse(self._risk_scoring.behaviours)

    @cached_property
    def summary(self) -> AsyncSummaryWithRawResponse:
        return AsyncSummaryWithRawResponse(self._risk_scoring.summary)


class RiskScoringWithStreamingResponse:
    def __init__(self, risk_scoring: RiskScoring) -> None:
        self._risk_scoring = risk_scoring

        self.get = to_streamed_response_wrapper(
            risk_scoring.get,
        )
        self.reset = to_streamed_response_wrapper(
            risk_scoring.reset,
        )

    @cached_property
    def behaviours(self) -> BehavioursWithStreamingResponse:
        return BehavioursWithStreamingResponse(self._risk_scoring.behaviours)

    @cached_property
    def summary(self) -> SummaryWithStreamingResponse:
        return SummaryWithStreamingResponse(self._risk_scoring.summary)


class AsyncRiskScoringWithStreamingResponse:
    def __init__(self, risk_scoring: AsyncRiskScoring) -> None:
        self._risk_scoring = risk_scoring

        self.get = async_to_streamed_response_wrapper(
            risk_scoring.get,
        )
        self.reset = async_to_streamed_response_wrapper(
            risk_scoring.reset,
        )

    @cached_property
    def behaviours(self) -> AsyncBehavioursWithStreamingResponse:
        return AsyncBehavioursWithStreamingResponse(self._risk_scoring.behaviours)

    @cached_property
    def summary(self) -> AsyncSummaryWithStreamingResponse:
        return AsyncSummaryWithStreamingResponse(self._risk_scoring.summary)
