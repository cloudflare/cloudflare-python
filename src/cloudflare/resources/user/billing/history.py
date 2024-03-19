# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
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
from ....types.user.billing import HistoryGetResponse, history_get_params

__all__ = ["History", "AsyncHistory"]


class History(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HistoryWithRawResponse:
        return HistoryWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HistoryWithStreamingResponse:
        return HistoryWithStreamingResponse(self)

    def get(
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
    ) -> Optional[HistoryGetResponse]:
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
                    history_get_params.HistoryGetParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[HistoryGetResponse]], ResultWrapper[HistoryGetResponse]),
        )


class AsyncHistory(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHistoryWithRawResponse:
        return AsyncHistoryWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHistoryWithStreamingResponse:
        return AsyncHistoryWithStreamingResponse(self)

    async def get(
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
    ) -> Optional[HistoryGetResponse]:
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
                query=await async_maybe_transform(
                    {
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    history_get_params.HistoryGetParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[HistoryGetResponse]], ResultWrapper[HistoryGetResponse]),
        )


class HistoryWithRawResponse:
    def __init__(self, history: History) -> None:
        self._history = history

        self.get = to_raw_response_wrapper(
            history.get,
        )


class AsyncHistoryWithRawResponse:
    def __init__(self, history: AsyncHistory) -> None:
        self._history = history

        self.get = async_to_raw_response_wrapper(
            history.get,
        )


class HistoryWithStreamingResponse:
    def __init__(self, history: History) -> None:
        self._history = history

        self.get = to_streamed_response_wrapper(
            history.get,
        )


class AsyncHistoryWithStreamingResponse:
    def __init__(self, history: AsyncHistory) -> None:
        self._history = history

        self.get = async_to_streamed_response_wrapper(
            history.get,
        )
