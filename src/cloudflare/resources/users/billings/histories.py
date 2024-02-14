# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.users.billings import HistoryUserBillingHistoryBillingHistoryDetailsResponse

from typing import Type, Optional

from typing_extensions import Literal

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
from ....types.users.billings import history_user_billing_history_billing_history_details_params
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["Histories", "AsyncHistories"]


class Histories(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HistoriesWithRawResponse:
        return HistoriesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HistoriesWithStreamingResponse:
        return HistoriesWithStreamingResponse(self)

    def user_billing_history_billing_history_details(
        self,
        *,
        order: Literal["type", "occured_at", "action"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[HistoryUserBillingHistoryBillingHistoryDetailsResponse]:
        """
        Accesses your billing history object.

        Args:
          order: Field to order billing history by.

          page: Page number of paginated results.

          per_page: Number of items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/user/billing/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    history_user_billing_history_billing_history_details_params.HistoryUserBillingHistoryBillingHistoryDetailsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[HistoryUserBillingHistoryBillingHistoryDetailsResponse]],
                ResultWrapper[HistoryUserBillingHistoryBillingHistoryDetailsResponse],
            ),
        )


class AsyncHistories(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHistoriesWithRawResponse:
        return AsyncHistoriesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHistoriesWithStreamingResponse:
        return AsyncHistoriesWithStreamingResponse(self)

    async def user_billing_history_billing_history_details(
        self,
        *,
        order: Literal["type", "occured_at", "action"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[HistoryUserBillingHistoryBillingHistoryDetailsResponse]:
        """
        Accesses your billing history object.

        Args:
          order: Field to order billing history by.

          page: Page number of paginated results.

          per_page: Number of items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/user/billing/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    history_user_billing_history_billing_history_details_params.HistoryUserBillingHistoryBillingHistoryDetailsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[HistoryUserBillingHistoryBillingHistoryDetailsResponse]],
                ResultWrapper[HistoryUserBillingHistoryBillingHistoryDetailsResponse],
            ),
        )


class HistoriesWithRawResponse:
    def __init__(self, histories: Histories) -> None:
        self._histories = histories

        self.user_billing_history_billing_history_details = to_raw_response_wrapper(
            histories.user_billing_history_billing_history_details,
        )


class AsyncHistoriesWithRawResponse:
    def __init__(self, histories: AsyncHistories) -> None:
        self._histories = histories

        self.user_billing_history_billing_history_details = async_to_raw_response_wrapper(
            histories.user_billing_history_billing_history_details,
        )


class HistoriesWithStreamingResponse:
    def __init__(self, histories: Histories) -> None:
        self._histories = histories

        self.user_billing_history_billing_history_details = to_streamed_response_wrapper(
            histories.user_billing_history_billing_history_details,
        )


class AsyncHistoriesWithStreamingResponse:
    def __init__(self, histories: AsyncHistories) -> None:
        self._histories = histories

        self.user_billing_history_billing_history_details = async_to_streamed_response_wrapper(
            histories.user_billing_history_billing_history_details,
        )
