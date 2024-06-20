# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from .request import (
    RequestResource,
    AsyncRequestResource,
    RequestResourceWithRawResponse,
    AsyncRequestResourceWithRawResponse,
    RequestResourceWithStreamingResponse,
    AsyncRequestResourceWithStreamingResponse,
)
from .response import (
    ResponseResource,
    AsyncResponseResource,
    ResponseResourceWithRawResponse,
    AsyncResponseResourceWithRawResponse,
    ResponseResourceWithStreamingResponse,
    AsyncResponseResourceWithStreamingResponse,
)
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
from ...._wrappers import ResultWrapper
from ....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ...._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ....types.ai_gateway import log_list_params
from ....types.ai_gateway.log_get_response import LogGetResponse
from ....types.ai_gateway.log_list_response import LogListResponse

__all__ = ["LogsResource", "AsyncLogsResource"]


class LogsResource(SyncAPIResource):
    @cached_property
    def request(self) -> RequestResource:
        return RequestResource(self._client)

    @cached_property
    def response(self) -> ResponseResource:
        return ResponseResource(self._client)

    @cached_property
    def with_raw_response(self) -> LogsResourceWithRawResponse:
        return LogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LogsResourceWithStreamingResponse:
        return LogsResourceWithStreamingResponse(self)

    def list(
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
    ) -> SyncV4PagePaginationArray[LogListResponse]:
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
        return self._get_api_list(
            f"/accounts/{account_id}/ai-gateway/gateways/{id}/logs",
            page=SyncV4PagePaginationArray[LogListResponse],
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
                    log_list_params.LogListParams,
                ),
            ),
            model=LogListResponse,
        )

    def get(
        self,
        log_id: str,
        *,
        account_id: str,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LogGetResponse:
        """
        Get Gateway Log Detail

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
        if not log_id:
            raise ValueError(f"Expected a non-empty value for `log_id` but received {log_id!r}")
        return self._get(
            f"/accounts/{account_id}/ai-gateway/gateways/{id}/logs/{log_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[LogGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[LogGetResponse], ResultWrapper[LogGetResponse]),
        )


class AsyncLogsResource(AsyncAPIResource):
    @cached_property
    def request(self) -> AsyncRequestResource:
        return AsyncRequestResource(self._client)

    @cached_property
    def response(self) -> AsyncResponseResource:
        return AsyncResponseResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLogsResourceWithRawResponse:
        return AsyncLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLogsResourceWithStreamingResponse:
        return AsyncLogsResourceWithStreamingResponse(self)

    def list(
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
    ) -> AsyncPaginator[LogListResponse, AsyncV4PagePaginationArray[LogListResponse]]:
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
        return self._get_api_list(
            f"/accounts/{account_id}/ai-gateway/gateways/{id}/logs",
            page=AsyncV4PagePaginationArray[LogListResponse],
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
                    log_list_params.LogListParams,
                ),
            ),
            model=LogListResponse,
        )

    async def get(
        self,
        log_id: str,
        *,
        account_id: str,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LogGetResponse:
        """
        Get Gateway Log Detail

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
        if not log_id:
            raise ValueError(f"Expected a non-empty value for `log_id` but received {log_id!r}")
        return await self._get(
            f"/accounts/{account_id}/ai-gateway/gateways/{id}/logs/{log_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[LogGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[LogGetResponse], ResultWrapper[LogGetResponse]),
        )


class LogsResourceWithRawResponse:
    def __init__(self, logs: LogsResource) -> None:
        self._logs = logs

        self.list = to_raw_response_wrapper(
            logs.list,
        )
        self.get = to_raw_response_wrapper(
            logs.get,
        )

    @cached_property
    def request(self) -> RequestResourceWithRawResponse:
        return RequestResourceWithRawResponse(self._logs.request)

    @cached_property
    def response(self) -> ResponseResourceWithRawResponse:
        return ResponseResourceWithRawResponse(self._logs.response)


class AsyncLogsResourceWithRawResponse:
    def __init__(self, logs: AsyncLogsResource) -> None:
        self._logs = logs

        self.list = async_to_raw_response_wrapper(
            logs.list,
        )
        self.get = async_to_raw_response_wrapper(
            logs.get,
        )

    @cached_property
    def request(self) -> AsyncRequestResourceWithRawResponse:
        return AsyncRequestResourceWithRawResponse(self._logs.request)

    @cached_property
    def response(self) -> AsyncResponseResourceWithRawResponse:
        return AsyncResponseResourceWithRawResponse(self._logs.response)


class LogsResourceWithStreamingResponse:
    def __init__(self, logs: LogsResource) -> None:
        self._logs = logs

        self.list = to_streamed_response_wrapper(
            logs.list,
        )
        self.get = to_streamed_response_wrapper(
            logs.get,
        )

    @cached_property
    def request(self) -> RequestResourceWithStreamingResponse:
        return RequestResourceWithStreamingResponse(self._logs.request)

    @cached_property
    def response(self) -> ResponseResourceWithStreamingResponse:
        return ResponseResourceWithStreamingResponse(self._logs.response)


class AsyncLogsResourceWithStreamingResponse:
    def __init__(self, logs: AsyncLogsResource) -> None:
        self._logs = logs

        self.list = async_to_streamed_response_wrapper(
            logs.list,
        )
        self.get = async_to_streamed_response_wrapper(
            logs.get,
        )

    @cached_property
    def request(self) -> AsyncRequestResourceWithStreamingResponse:
        return AsyncRequestResourceWithStreamingResponse(self._logs.request)

    @cached_property
    def response(self) -> AsyncResponseResourceWithStreamingResponse:
        return AsyncResponseResourceWithStreamingResponse(self._logs.response)
