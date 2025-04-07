# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....pagination import SyncSinglePage, AsyncSinglePage
from ....._base_client import AsyncPaginator, make_request_options
from .....types.workers.observability.telemetry import value_create_params
from .....types.workers.observability.telemetry.value_create_response import ValueCreateResponse

__all__ = ["ValuesResource", "AsyncValuesResource"]


class ValuesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ValuesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ValuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ValuesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ValuesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        datasets: List[str],
        key: str,
        timeframe: value_create_params.Timeframe,
        type: Literal["string", "boolean", "number"],
        filters: Iterable[value_create_params.Filter] | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        needle: value_create_params.Needle | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[ValueCreateResponse]:
        """
        List unique values found in your events

        Args:
          needle: Search for a specific substring in the event.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/workers/observability/telemetry/values",
            page=SyncSinglePage[ValueCreateResponse],
            body=maybe_transform(
                {
                    "datasets": datasets,
                    "key": key,
                    "timeframe": timeframe,
                    "type": type,
                    "filters": filters,
                    "limit": limit,
                    "needle": needle,
                },
                value_create_params.ValueCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=ValueCreateResponse,
            method="post",
        )


class AsyncValuesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncValuesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncValuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncValuesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncValuesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        datasets: List[str],
        key: str,
        timeframe: value_create_params.Timeframe,
        type: Literal["string", "boolean", "number"],
        filters: Iterable[value_create_params.Filter] | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        needle: value_create_params.Needle | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ValueCreateResponse, AsyncSinglePage[ValueCreateResponse]]:
        """
        List unique values found in your events

        Args:
          needle: Search for a specific substring in the event.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/workers/observability/telemetry/values",
            page=AsyncSinglePage[ValueCreateResponse],
            body=maybe_transform(
                {
                    "datasets": datasets,
                    "key": key,
                    "timeframe": timeframe,
                    "type": type,
                    "filters": filters,
                    "limit": limit,
                    "needle": needle,
                },
                value_create_params.ValueCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=ValueCreateResponse,
            method="post",
        )


class ValuesResourceWithRawResponse:
    def __init__(self, values: ValuesResource) -> None:
        self._values = values

        self.create = to_raw_response_wrapper(
            values.create,
        )


class AsyncValuesResourceWithRawResponse:
    def __init__(self, values: AsyncValuesResource) -> None:
        self._values = values

        self.create = async_to_raw_response_wrapper(
            values.create,
        )


class ValuesResourceWithStreamingResponse:
    def __init__(self, values: ValuesResource) -> None:
        self._values = values

        self.create = to_streamed_response_wrapper(
            values.create,
        )


class AsyncValuesResourceWithStreamingResponse:
    def __init__(self, values: AsyncValuesResource) -> None:
        self._values = values

        self.create = async_to_streamed_response_wrapper(
            values.create,
        )
