# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.ai_gateway.log_list_response import LogListResponse

from ...pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray

from ..._utils import maybe_transform

from ..._base_client import make_request_options, AsyncPaginator

from typing_extensions import Literal

from typing import Union

from datetime import datetime

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
from ...types.ai_gateway import log_list_params

__all__ = ["LogsResource", "AsyncLogsResource"]


class LogsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LogsResourceWithRawResponse:
        return LogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LogsResourceWithStreamingResponse:
        return LogsResourceWithStreamingResponse(self)

    def list(
        self,
        gateway_id: str,
        *,
        account_id: str,
        cached: bool | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc", "ASC", "DESC"] | NotGiven = NOT_GIVEN,
        end_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        max_cost: float | NotGiven = NOT_GIVEN,
        max_duration: float | NotGiven = NOT_GIVEN,
        max_tokens: float | NotGiven = NOT_GIVEN,
        min_cost: float | NotGiven = NOT_GIVEN,
        min_duration: float | NotGiven = NOT_GIVEN,
        min_tokens: float | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        model_type: str | NotGiven = NOT_GIVEN,
        order_by: Literal["created_at", "provider", "model", "model_type", "success", "cached"] | NotGiven = NOT_GIVEN,
        order_by_direction: Literal["asc", "desc", "ASC", "DESC"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        provider: str | NotGiven = NOT_GIVEN,
        request_content_type: str | NotGiven = NOT_GIVEN,
        response_content_type: str | NotGiven = NOT_GIVEN,
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
          gateway_id: gateway id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not gateway_id:
            raise ValueError(f"Expected a non-empty value for `gateway_id` but received {gateway_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs",
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
                        "max_cost": max_cost,
                        "max_duration": max_duration,
                        "max_tokens": max_tokens,
                        "min_cost": min_cost,
                        "min_duration": min_duration,
                        "min_tokens": min_tokens,
                        "model": model,
                        "model_type": model_type,
                        "order_by": order_by,
                        "order_by_direction": order_by_direction,
                        "page": page,
                        "per_page": per_page,
                        "provider": provider,
                        "request_content_type": request_content_type,
                        "response_content_type": response_content_type,
                        "search": search,
                        "start_date": start_date,
                        "success": success,
                    },
                    log_list_params.LogListParams,
                ),
            ),
            model=LogListResponse,
        )


class AsyncLogsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLogsResourceWithRawResponse:
        return AsyncLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLogsResourceWithStreamingResponse:
        return AsyncLogsResourceWithStreamingResponse(self)

    def list(
        self,
        gateway_id: str,
        *,
        account_id: str,
        cached: bool | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc", "ASC", "DESC"] | NotGiven = NOT_GIVEN,
        end_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        max_cost: float | NotGiven = NOT_GIVEN,
        max_duration: float | NotGiven = NOT_GIVEN,
        max_tokens: float | NotGiven = NOT_GIVEN,
        min_cost: float | NotGiven = NOT_GIVEN,
        min_duration: float | NotGiven = NOT_GIVEN,
        min_tokens: float | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        model_type: str | NotGiven = NOT_GIVEN,
        order_by: Literal["created_at", "provider", "model", "model_type", "success", "cached"] | NotGiven = NOT_GIVEN,
        order_by_direction: Literal["asc", "desc", "ASC", "DESC"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        provider: str | NotGiven = NOT_GIVEN,
        request_content_type: str | NotGiven = NOT_GIVEN,
        response_content_type: str | NotGiven = NOT_GIVEN,
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
          gateway_id: gateway id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not gateway_id:
            raise ValueError(f"Expected a non-empty value for `gateway_id` but received {gateway_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs",
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
                        "max_cost": max_cost,
                        "max_duration": max_duration,
                        "max_tokens": max_tokens,
                        "min_cost": min_cost,
                        "min_duration": min_duration,
                        "min_tokens": min_tokens,
                        "model": model,
                        "model_type": model_type,
                        "order_by": order_by,
                        "order_by_direction": order_by_direction,
                        "page": page,
                        "per_page": per_page,
                        "provider": provider,
                        "request_content_type": request_content_type,
                        "response_content_type": response_content_type,
                        "search": search,
                        "start_date": start_date,
                        "success": success,
                    },
                    log_list_params.LogListParams,
                ),
            ),
            model=LogListResponse,
        )


class LogsResourceWithRawResponse:
    def __init__(self, logs: LogsResource) -> None:
        self._logs = logs

        self.list = to_raw_response_wrapper(
            logs.list,
        )


class AsyncLogsResourceWithRawResponse:
    def __init__(self, logs: AsyncLogsResource) -> None:
        self._logs = logs

        self.list = async_to_raw_response_wrapper(
            logs.list,
        )


class LogsResourceWithStreamingResponse:
    def __init__(self, logs: LogsResource) -> None:
        self._logs = logs

        self.list = to_streamed_response_wrapper(
            logs.list,
        )


class AsyncLogsResourceWithStreamingResponse:
    def __init__(self, logs: AsyncLogsResource) -> None:
        self._logs = logs

        self.list = async_to_streamed_response_wrapper(
            logs.list,
        )
