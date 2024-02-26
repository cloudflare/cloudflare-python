# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ...._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ....types.user.billing import HistoryListResponse, history_list_params

__all__ = ["History", "AsyncHistory"]


class History(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HistoryWithRawResponse:
        return HistoryWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HistoryWithStreamingResponse:
        return HistoryWithStreamingResponse(self)

    def list(
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
    ) -> SyncV4PagePaginationArray[HistoryListResponse]:
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
        return self._get_api_list(
            "/user/billing/history",
            page=SyncV4PagePaginationArray[HistoryListResponse],
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
                    history_list_params.HistoryListParams,
                ),
            ),
            model=HistoryListResponse,
        )


class AsyncHistory(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHistoryWithRawResponse:
        return AsyncHistoryWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHistoryWithStreamingResponse:
        return AsyncHistoryWithStreamingResponse(self)

    def list(
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
    ) -> AsyncPaginator[HistoryListResponse, AsyncV4PagePaginationArray[HistoryListResponse]]:
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
        return self._get_api_list(
            "/user/billing/history",
            page=AsyncV4PagePaginationArray[HistoryListResponse],
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
                    history_list_params.HistoryListParams,
                ),
            ),
            model=HistoryListResponse,
        )


class HistoryWithRawResponse:
    def __init__(self, history: History) -> None:
        self._history = history

        self.list = to_raw_response_wrapper(
            history.list,
        )


class AsyncHistoryWithRawResponse:
    def __init__(self, history: AsyncHistory) -> None:
        self._history = history

        self.list = async_to_raw_response_wrapper(
            history.list,
        )


class HistoryWithStreamingResponse:
    def __init__(self, history: History) -> None:
        self._history = history

        self.list = to_streamed_response_wrapper(
            history.list,
        )


class AsyncHistoryWithStreamingResponse:
    def __init__(self, history: AsyncHistory) -> None:
        self._history = history

        self.list = async_to_streamed_response_wrapper(
            history.list,
        )
