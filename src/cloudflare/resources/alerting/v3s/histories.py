# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.alerting.v3s import HistoryNotificationHistoryListHistoryResponse

from typing import Type, Optional, Union

from datetime import datetime

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
from ....types.alerting.v3s import history_notification_history_list_history_params
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

    def notification_history_list_history(
        self,
        account_id: str,
        *,
        before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        since: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[HistoryNotificationHistoryListHistoryResponse]:
        """Gets a list of history records for notifications sent to an account.

        The records
        are displayed for last `x` number of days based on the zone plan (free = 30, pro
        = 30, biz = 30, ent = 90).

        Args:
          account_id: The account id

          before: Limit the returned results to history records older than the specified date.
              This must be a timestamp that conforms to RFC3339.

          page: Page number of paginated results.

          per_page: Number of items per page.

          since: Limit the returned results to history records newer than the specified date.
              This must be a timestamp that conforms to RFC3339.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/alerting/v3/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "before": before,
                        "page": page,
                        "per_page": per_page,
                        "since": since,
                    },
                    history_notification_history_list_history_params.HistoryNotificationHistoryListHistoryParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[HistoryNotificationHistoryListHistoryResponse]],
                ResultWrapper[HistoryNotificationHistoryListHistoryResponse],
            ),
        )


class AsyncHistories(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHistoriesWithRawResponse:
        return AsyncHistoriesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHistoriesWithStreamingResponse:
        return AsyncHistoriesWithStreamingResponse(self)

    async def notification_history_list_history(
        self,
        account_id: str,
        *,
        before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        since: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[HistoryNotificationHistoryListHistoryResponse]:
        """Gets a list of history records for notifications sent to an account.

        The records
        are displayed for last `x` number of days based on the zone plan (free = 30, pro
        = 30, biz = 30, ent = 90).

        Args:
          account_id: The account id

          before: Limit the returned results to history records older than the specified date.
              This must be a timestamp that conforms to RFC3339.

          page: Page number of paginated results.

          per_page: Number of items per page.

          since: Limit the returned results to history records newer than the specified date.
              This must be a timestamp that conforms to RFC3339.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/alerting/v3/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "before": before,
                        "page": page,
                        "per_page": per_page,
                        "since": since,
                    },
                    history_notification_history_list_history_params.HistoryNotificationHistoryListHistoryParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[HistoryNotificationHistoryListHistoryResponse]],
                ResultWrapper[HistoryNotificationHistoryListHistoryResponse],
            ),
        )


class HistoriesWithRawResponse:
    def __init__(self, histories: Histories) -> None:
        self._histories = histories

        self.notification_history_list_history = to_raw_response_wrapper(
            histories.notification_history_list_history,
        )


class AsyncHistoriesWithRawResponse:
    def __init__(self, histories: AsyncHistories) -> None:
        self._histories = histories

        self.notification_history_list_history = async_to_raw_response_wrapper(
            histories.notification_history_list_history,
        )


class HistoriesWithStreamingResponse:
    def __init__(self, histories: Histories) -> None:
        self._histories = histories

        self.notification_history_list_history = to_streamed_response_wrapper(
            histories.notification_history_list_history,
        )


class AsyncHistoriesWithStreamingResponse:
    def __init__(self, histories: AsyncHistories) -> None:
        self._histories = histories

        self.notification_history_list_history = async_to_streamed_response_wrapper(
            histories.notification_history_list_history,
        )
