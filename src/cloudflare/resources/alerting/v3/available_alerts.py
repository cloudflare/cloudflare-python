# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.alerting.v3 import AvailableAlertListResponse

from typing import Optional

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["AvailableAlerts", "AsyncAvailableAlerts"]


class AvailableAlerts(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AvailableAlertsWithRawResponse:
        return AvailableAlertsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AvailableAlertsWithStreamingResponse:
        return AvailableAlertsWithStreamingResponse(self)

    def list(
        self,
        account_id: str,
        *,
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
        return cast(
            Optional[AvailableAlertListResponse],
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
                    Any, ResultWrapper[AvailableAlertListResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncAvailableAlerts(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAvailableAlertsWithRawResponse:
        return AsyncAvailableAlertsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAvailableAlertsWithStreamingResponse:
        return AsyncAvailableAlertsWithStreamingResponse(self)

    async def list(
        self,
        account_id: str,
        *,
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
        return cast(
            Optional[AvailableAlertListResponse],
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
                    Any, ResultWrapper[AvailableAlertListResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AvailableAlertsWithRawResponse:
    def __init__(self, available_alerts: AvailableAlerts) -> None:
        self._available_alerts = available_alerts

        self.list = to_raw_response_wrapper(
            available_alerts.list,
        )


class AsyncAvailableAlertsWithRawResponse:
    def __init__(self, available_alerts: AsyncAvailableAlerts) -> None:
        self._available_alerts = available_alerts

        self.list = async_to_raw_response_wrapper(
            available_alerts.list,
        )


class AvailableAlertsWithStreamingResponse:
    def __init__(self, available_alerts: AvailableAlerts) -> None:
        self._available_alerts = available_alerts

        self.list = to_streamed_response_wrapper(
            available_alerts.list,
        )


class AsyncAvailableAlertsWithStreamingResponse:
    def __init__(self, available_alerts: AsyncAvailableAlerts) -> None:
        self._available_alerts = available_alerts

        self.list = async_to_streamed_response_wrapper(
            available_alerts.list,
        )
