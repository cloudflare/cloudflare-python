# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from .summary import (
    SummaryResource,
    AsyncSummaryResource,
    SummaryResourceWithRawResponse,
    AsyncSummaryResourceWithRawResponse,
    SummaryResourceWithStreamingResponse,
    AsyncSummaryResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from .behaviours import (
    BehavioursResource,
    AsyncBehavioursResource,
    BehavioursResourceWithRawResponse,
    AsyncBehavioursResourceWithRawResponse,
    BehavioursResourceWithStreamingResponse,
    AsyncBehavioursResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import make_request_options
from .integrations.integrations import (
    IntegrationsResource,
    AsyncIntegrationsResource,
    IntegrationsResourceWithRawResponse,
    AsyncIntegrationsResourceWithRawResponse,
    IntegrationsResourceWithStreamingResponse,
    AsyncIntegrationsResourceWithStreamingResponse,
)
from ....types.zero_trust.risk_scoring_get_response import RiskScoringGetResponse

__all__ = ["RiskScoringResource", "AsyncRiskScoringResource"]


class RiskScoringResource(SyncAPIResource):
    @cached_property
    def behaviours(self) -> BehavioursResource:
        return BehavioursResource(self._client)

    @cached_property
    def summary(self) -> SummaryResource:
        return SummaryResource(self._client)

    @cached_property
    def integrations(self) -> IntegrationsResource:
        return IntegrationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> RiskScoringResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RiskScoringResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RiskScoringResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RiskScoringResourceWithStreamingResponse(self)

    def get(
        self,
        user_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RiskScoringGetResponse]:
        """
        Get risk event/score information for a specific user

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            f"/accounts/{account_id}/zt_risk_scoring/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RiskScoringGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RiskScoringGetResponse]], ResultWrapper[RiskScoringGetResponse]),
        )

    def reset(
        self,
        user_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Clear the risk score for a particular user

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._post(
            f"/accounts/{account_id}/zt_risk_scoring/{user_id}/reset",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )


class AsyncRiskScoringResource(AsyncAPIResource):
    @cached_property
    def behaviours(self) -> AsyncBehavioursResource:
        return AsyncBehavioursResource(self._client)

    @cached_property
    def summary(self) -> AsyncSummaryResource:
        return AsyncSummaryResource(self._client)

    @cached_property
    def integrations(self) -> AsyncIntegrationsResource:
        return AsyncIntegrationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRiskScoringResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRiskScoringResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRiskScoringResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncRiskScoringResourceWithStreamingResponse(self)

    async def get(
        self,
        user_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RiskScoringGetResponse]:
        """
        Get risk event/score information for a specific user

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            f"/accounts/{account_id}/zt_risk_scoring/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RiskScoringGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RiskScoringGetResponse]], ResultWrapper[RiskScoringGetResponse]),
        )

    async def reset(
        self,
        user_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Clear the risk score for a particular user

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._post(
            f"/accounts/{account_id}/zt_risk_scoring/{user_id}/reset",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )


class RiskScoringResourceWithRawResponse:
    def __init__(self, risk_scoring: RiskScoringResource) -> None:
        self._risk_scoring = risk_scoring

        self.get = to_raw_response_wrapper(
            risk_scoring.get,
        )
        self.reset = to_raw_response_wrapper(
            risk_scoring.reset,
        )

    @cached_property
    def behaviours(self) -> BehavioursResourceWithRawResponse:
        return BehavioursResourceWithRawResponse(self._risk_scoring.behaviours)

    @cached_property
    def summary(self) -> SummaryResourceWithRawResponse:
        return SummaryResourceWithRawResponse(self._risk_scoring.summary)

    @cached_property
    def integrations(self) -> IntegrationsResourceWithRawResponse:
        return IntegrationsResourceWithRawResponse(self._risk_scoring.integrations)


class AsyncRiskScoringResourceWithRawResponse:
    def __init__(self, risk_scoring: AsyncRiskScoringResource) -> None:
        self._risk_scoring = risk_scoring

        self.get = async_to_raw_response_wrapper(
            risk_scoring.get,
        )
        self.reset = async_to_raw_response_wrapper(
            risk_scoring.reset,
        )

    @cached_property
    def behaviours(self) -> AsyncBehavioursResourceWithRawResponse:
        return AsyncBehavioursResourceWithRawResponse(self._risk_scoring.behaviours)

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithRawResponse:
        return AsyncSummaryResourceWithRawResponse(self._risk_scoring.summary)

    @cached_property
    def integrations(self) -> AsyncIntegrationsResourceWithRawResponse:
        return AsyncIntegrationsResourceWithRawResponse(self._risk_scoring.integrations)


class RiskScoringResourceWithStreamingResponse:
    def __init__(self, risk_scoring: RiskScoringResource) -> None:
        self._risk_scoring = risk_scoring

        self.get = to_streamed_response_wrapper(
            risk_scoring.get,
        )
        self.reset = to_streamed_response_wrapper(
            risk_scoring.reset,
        )

    @cached_property
    def behaviours(self) -> BehavioursResourceWithStreamingResponse:
        return BehavioursResourceWithStreamingResponse(self._risk_scoring.behaviours)

    @cached_property
    def summary(self) -> SummaryResourceWithStreamingResponse:
        return SummaryResourceWithStreamingResponse(self._risk_scoring.summary)

    @cached_property
    def integrations(self) -> IntegrationsResourceWithStreamingResponse:
        return IntegrationsResourceWithStreamingResponse(self._risk_scoring.integrations)


class AsyncRiskScoringResourceWithStreamingResponse:
    def __init__(self, risk_scoring: AsyncRiskScoringResource) -> None:
        self._risk_scoring = risk_scoring

        self.get = async_to_streamed_response_wrapper(
            risk_scoring.get,
        )
        self.reset = async_to_streamed_response_wrapper(
            risk_scoring.reset,
        )

    @cached_property
    def behaviours(self) -> AsyncBehavioursResourceWithStreamingResponse:
        return AsyncBehavioursResourceWithStreamingResponse(self._risk_scoring.behaviours)

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithStreamingResponse:
        return AsyncSummaryResourceWithStreamingResponse(self._risk_scoring.summary)

    @cached_property
    def integrations(self) -> AsyncIntegrationsResourceWithStreamingResponse:
        return AsyncIntegrationsResourceWithStreamingResponse(self._risk_scoring.integrations)
