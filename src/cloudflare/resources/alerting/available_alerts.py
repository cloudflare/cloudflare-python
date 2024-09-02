# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.alerting.available_alert_list_response import AvailableAlertListResponse

from ..._wrappers import ResultWrapper

from typing import Optional, Type

from ..._base_client import make_request_options

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from typing import cast
from typing import cast

__all__ = ["AvailableAlertsResource", "AsyncAvailableAlertsResource"]


class AvailableAlertsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AvailableAlertsResourceWithRawResponse:
        return AvailableAlertsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AvailableAlertsResourceWithStreamingResponse:
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
        return AsyncAvailableAlertsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAvailableAlertsResourceWithStreamingResponse:
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
