# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, Optional, cast

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from .....types.alerting.v3s.destinations import (
    EligibleNotificationMechanismEligibilityGetDeliveryMechanismEligibilityResponse,
)

__all__ = ["Eligibles", "AsyncEligibles"]


class Eligibles(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EligiblesWithRawResponse:
        return EligiblesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EligiblesWithStreamingResponse:
        return EligiblesWithStreamingResponse(self)

    def notification_mechanism_eligibility_get_delivery_mechanism_eligibility(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[EligibleNotificationMechanismEligibilityGetDeliveryMechanismEligibilityResponse]:
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
            Optional[EligibleNotificationMechanismEligibilityGetDeliveryMechanismEligibilityResponse],
            self._get(
                f"/accounts/{account_id}/alerting/v3/destinations/eligible",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[EligibleNotificationMechanismEligibilityGetDeliveryMechanismEligibilityResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncEligibles(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEligiblesWithRawResponse:
        return AsyncEligiblesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEligiblesWithStreamingResponse:
        return AsyncEligiblesWithStreamingResponse(self)

    async def notification_mechanism_eligibility_get_delivery_mechanism_eligibility(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[EligibleNotificationMechanismEligibilityGetDeliveryMechanismEligibilityResponse]:
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
            Optional[EligibleNotificationMechanismEligibilityGetDeliveryMechanismEligibilityResponse],
            await self._get(
                f"/accounts/{account_id}/alerting/v3/destinations/eligible",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[EligibleNotificationMechanismEligibilityGetDeliveryMechanismEligibilityResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class EligiblesWithRawResponse:
    def __init__(self, eligibles: Eligibles) -> None:
        self._eligibles = eligibles

        self.notification_mechanism_eligibility_get_delivery_mechanism_eligibility = to_raw_response_wrapper(
            eligibles.notification_mechanism_eligibility_get_delivery_mechanism_eligibility,
        )


class AsyncEligiblesWithRawResponse:
    def __init__(self, eligibles: AsyncEligibles) -> None:
        self._eligibles = eligibles

        self.notification_mechanism_eligibility_get_delivery_mechanism_eligibility = async_to_raw_response_wrapper(
            eligibles.notification_mechanism_eligibility_get_delivery_mechanism_eligibility,
        )


class EligiblesWithStreamingResponse:
    def __init__(self, eligibles: Eligibles) -> None:
        self._eligibles = eligibles

        self.notification_mechanism_eligibility_get_delivery_mechanism_eligibility = to_streamed_response_wrapper(
            eligibles.notification_mechanism_eligibility_get_delivery_mechanism_eligibility,
        )


class AsyncEligiblesWithStreamingResponse:
    def __init__(self, eligibles: AsyncEligibles) -> None:
        self._eligibles = eligibles

        self.notification_mechanism_eligibility_get_delivery_mechanism_eligibility = async_to_streamed_response_wrapper(
            eligibles.notification_mechanism_eligibility_get_delivery_mechanism_eligibility,
        )
