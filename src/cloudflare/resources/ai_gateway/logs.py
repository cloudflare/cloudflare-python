# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import (
    make_request_options,
)
from ...types.ai_gateway import log_get_params
from ...types.ai_gateway.log_get_response import LogGetResponse

__all__ = ["LogsResource", "AsyncLogsResource"]


class LogsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LogsResourceWithRawResponse:
        return LogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LogsResourceWithStreamingResponse:
        return LogsResourceWithStreamingResponse(self)

    def get(
        self,
        id: str,
        *,
        account_id: str,
        cached: bool | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        end_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        order_by: Literal["created_at", "provider"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        start_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        success: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LogGetResponse:
        """
        List Gateway Logs

        Args:
          id: gateway id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/accounts/{account_id}/ai-gateway/gateways/{id}/logs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cached": cached,
                        "direction": direction,
                        "end_date": end_date,
                        "order_by": order_by,
                        "page": page,
                        "per_page": per_page,
                        "search": search,
                        "start_date": start_date,
                        "success": success,
                    },
                    log_get_params.LogGetParams,
                ),
                post_parser=ResultWrapper[LogGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[LogGetResponse], ResultWrapper[LogGetResponse]),
        )


class AsyncLogsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLogsResourceWithRawResponse:
        return AsyncLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLogsResourceWithStreamingResponse:
        return AsyncLogsResourceWithStreamingResponse(self)

    async def get(
        self,
        id: str,
        *,
        account_id: str,
        cached: bool | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        end_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        order_by: Literal["created_at", "provider"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        start_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        success: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LogGetResponse:
        """
        List Gateway Logs

        Args:
          id: gateway id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/accounts/{account_id}/ai-gateway/gateways/{id}/logs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cached": cached,
                        "direction": direction,
                        "end_date": end_date,
                        "order_by": order_by,
                        "page": page,
                        "per_page": per_page,
                        "search": search,
                        "start_date": start_date,
                        "success": success,
                    },
                    log_get_params.LogGetParams,
                ),
                post_parser=ResultWrapper[LogGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[LogGetResponse], ResultWrapper[LogGetResponse]),
        )


class LogsResourceWithRawResponse:
    def __init__(self, logs: LogsResource) -> None:
        self._logs = logs

        self.get = to_raw_response_wrapper(
            logs.get,
        )


class AsyncLogsResourceWithRawResponse:
    def __init__(self, logs: AsyncLogsResource) -> None:
        self._logs = logs

        self.get = async_to_raw_response_wrapper(
            logs.get,
        )


class LogsResourceWithStreamingResponse:
    def __init__(self, logs: LogsResource) -> None:
        self._logs = logs

        self.get = to_streamed_response_wrapper(
            logs.get,
        )


class AsyncLogsResourceWithStreamingResponse:
    def __init__(self, logs: AsyncLogsResource) -> None:
        self._logs = logs

        self.get = async_to_streamed_response_wrapper(
            logs.get,
        )
