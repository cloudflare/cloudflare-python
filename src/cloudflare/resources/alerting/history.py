# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.alerting.history import History

from ...pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray

from ..._utils import maybe_transform

from ..._base_client import make_request_options, AsyncPaginator

from typing import Union

from datetime import datetime

from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from ...types.alerting import history_list_params

__all__ = ["HistoryResource", "AsyncHistoryResource"]

class HistoryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self)

    def list(self,
    *,
    account_id: str,
    before: Union[str, datetime] | NotGiven = NOT_GIVEN,
    page: float | NotGiven = NOT_GIVEN,
    per_page: float | NotGiven = NOT_GIVEN,
    since: Union[str, datetime] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> SyncV4PagePaginationArray[History]:
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
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._get_api_list(
            f"/accounts/{account_id}/alerting/v3/history",
            page = SyncV4PagePaginationArray[History],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "before": before,
                "page": page,
                "per_page": per_page,
                "since": since,
            }, history_list_params.HistoryListParams)),
            model=History,
        )

class AsyncHistoryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self)

    def list(self,
    *,
    account_id: str,
    before: Union[str, datetime] | NotGiven = NOT_GIVEN,
    page: float | NotGiven = NOT_GIVEN,
    per_page: float | NotGiven = NOT_GIVEN,
    since: Union[str, datetime] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AsyncPaginator[History, AsyncV4PagePaginationArray[History]]:
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
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._get_api_list(
            f"/accounts/{account_id}/alerting/v3/history",
            page = AsyncV4PagePaginationArray[History],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "before": before,
                "page": page,
                "per_page": per_page,
                "since": since,
            }, history_list_params.HistoryListParams)),
            model=History,
        )

class HistoryResourceWithRawResponse:
    def __init__(self, history: HistoryResource) -> None:
        self._history = history

        self.list = to_raw_response_wrapper(
            history.list,
        )

class AsyncHistoryResourceWithRawResponse:
    def __init__(self, history: AsyncHistoryResource) -> None:
        self._history = history

        self.list = async_to_raw_response_wrapper(
            history.list,
        )

class HistoryResourceWithStreamingResponse:
    def __init__(self, history: HistoryResource) -> None:
        self._history = history

        self.list = to_streamed_response_wrapper(
            history.list,
        )

class AsyncHistoryResourceWithStreamingResponse:
    def __init__(self, history: AsyncHistoryResource) -> None:
        self._history = history

        self.list = async_to_streamed_response_wrapper(
            history.list,
        )