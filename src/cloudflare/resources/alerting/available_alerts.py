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
from ...types.alerting.available_alert_list_response import AvailableAlertListResponse

__all__ = ["AvailableAlertsResource", "AsyncAvailableAlertsResource"]


class AvailableAlertsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AvailableAlertsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AvailableAlertsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AvailableAlertsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AvailableAlertsResourceWithStreamingResponse(self)

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
    ) -> Optional[AvailableAlertListResponse]:
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
        return self._get(
            f"/accounts/{account_id}/alerting/v3/available_alerts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AvailableAlertListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AvailableAlertListResponse]], ResultWrapper[AvailableAlertListResponse]),
        )


class AsyncAvailableAlertsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAvailableAlertsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAvailableAlertsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAvailableAlertsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAvailableAlertsResourceWithStreamingResponse(self)

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
    ) -> Optional[AvailableAlertListResponse]:
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
        return await self._get(
            f"/accounts/{account_id}/alerting/v3/available_alerts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AvailableAlertListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AvailableAlertListResponse]], ResultWrapper[AvailableAlertListResponse]),
        )


class AvailableAlertsResourceWithRawResponse:
    def __init__(self, available_alerts: AvailableAlertsResource) -> None:
        self._available_alerts = available_alerts

        self.list = to_raw_response_wrapper(
            available_alerts.list,
        )


class AsyncAvailableAlertsResourceWithRawResponse:
    def __init__(self, available_alerts: AsyncAvailableAlertsResource) -> None:
        self._available_alerts = available_alerts

        self.list = async_to_raw_response_wrapper(
            available_alerts.list,
        )


class AvailableAlertsResourceWithStreamingResponse:
    def __init__(self, available_alerts: AvailableAlertsResource) -> None:
        self._available_alerts = available_alerts

        self.list = to_streamed_response_wrapper(
            available_alerts.list,
        )


class AsyncAvailableAlertsResourceWithStreamingResponse:
    def __init__(self, available_alerts: AsyncAvailableAlertsResource) -> None:
        self._available_alerts = available_alerts

        self.list = async_to_streamed_response_wrapper(
            available_alerts.list,
        )
