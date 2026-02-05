# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Type, Union, Iterable, Optional, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ..._base_client import AsyncPaginator, make_request_options
from ...types.ai_gateway import log_edit_params, log_list_params, log_delete_params
from ...types.ai_gateway.log_get_response import LogGetResponse
from ...types.ai_gateway.log_list_response import LogListResponse
from ...types.ai_gateway.log_delete_response import LogDeleteResponse

__all__ = ["LogsResource", "AsyncLogsResource"]


class LogsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return LogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return LogsResourceWithStreamingResponse(self)

    def list(
        self,
        gateway_id: str,
        *,
        account_id: str,
        cached: bool | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        end_date: Union[str, datetime] | Omit = omit,
        feedback: Literal[0, 1] | Omit = omit,
        filters: Iterable[log_list_params.Filter] | Omit = omit,
        max_cost: float | Omit = omit,
        max_duration: float | Omit = omit,
        max_tokens_in: float | Omit = omit,
        max_tokens_out: float | Omit = omit,
        max_total_tokens: float | Omit = omit,
        meta_info: bool | Omit = omit,
        min_cost: float | Omit = omit,
        min_duration: float | Omit = omit,
        min_tokens_in: float | Omit = omit,
        min_tokens_out: float | Omit = omit,
        min_total_tokens: float | Omit = omit,
        model: str | Omit = omit,
        model_type: str | Omit = omit,
        order_by: Literal["created_at", "provider", "model", "model_type", "success", "cached"] | Omit = omit,
        order_by_direction: Literal["asc", "desc"] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        provider: str | Omit = omit,
        request_content_type: str | Omit = omit,
        response_content_type: str | Omit = omit,
        search: str | Omit = omit,
        start_date: Union[str, datetime] | Omit = omit,
        success: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
                        "feedback": feedback,
                        "filters": filters,
                        "max_cost": max_cost,
                        "max_duration": max_duration,
                        "max_tokens_in": max_tokens_in,
                        "max_tokens_out": max_tokens_out,
                        "max_total_tokens": max_total_tokens,
                        "meta_info": meta_info,
                        "min_cost": min_cost,
                        "min_duration": min_duration,
                        "min_tokens_in": min_tokens_in,
                        "min_tokens_out": min_tokens_out,
                        "min_total_tokens": min_total_tokens,
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

    def delete(
        self,
        gateway_id: str,
        *,
        account_id: str,
        filters: Iterable[log_delete_params.Filter] | Omit = omit,
        limit: int | Omit = omit,
        order_by: Literal[
            "created_at",
            "provider",
            "model",
            "model_type",
            "success",
            "cached",
            "cost",
            "tokens_in",
            "tokens_out",
            "duration",
            "feedback",
        ]
        | Omit = omit,
        order_by_direction: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogDeleteResponse:
        """
        Delete Gateway Logs

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
        return self._delete(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filters": filters,
                        "limit": limit,
                        "order_by": order_by,
                        "order_by_direction": order_by_direction,
                    },
                    log_delete_params.LogDeleteParams,
                ),
            ),
            cast_to=LogDeleteResponse,
        )

    def edit(
        self,
        id: str,
        *,
        account_id: str,
        gateway_id: str,
        feedback: Optional[float] | Omit = omit,
        metadata: Optional[Dict[str, Union[str, float, bool]]] | Omit = omit,
        score: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Patch Gateway Log

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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs/{id}",
            body=maybe_transform(
                {
                    "feedback": feedback,
                    "metadata": metadata,
                    "score": score,
                },
                log_edit_params.LogEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[object]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    def get(
        self,
        id: str,
        *,
        account_id: str,
        gateway_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogGetResponse:
        """
        Get Gateway Log Detail

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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[LogGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[LogGetResponse], ResultWrapper[LogGetResponse]),
        )

    def request(
        self,
        id: str,
        *,
        account_id: str,
        gateway_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get Gateway Log Request

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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs/{id}/request",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def response(
        self,
        id: str,
        *,
        account_id: str,
        gateway_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get Gateway Log Response

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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs/{id}/response",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncLogsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncLogsResourceWithStreamingResponse(self)

    def list(
        self,
        gateway_id: str,
        *,
        account_id: str,
        cached: bool | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        end_date: Union[str, datetime] | Omit = omit,
        feedback: Literal[0, 1] | Omit = omit,
        filters: Iterable[log_list_params.Filter] | Omit = omit,
        max_cost: float | Omit = omit,
        max_duration: float | Omit = omit,
        max_tokens_in: float | Omit = omit,
        max_tokens_out: float | Omit = omit,
        max_total_tokens: float | Omit = omit,
        meta_info: bool | Omit = omit,
        min_cost: float | Omit = omit,
        min_duration: float | Omit = omit,
        min_tokens_in: float | Omit = omit,
        min_tokens_out: float | Omit = omit,
        min_total_tokens: float | Omit = omit,
        model: str | Omit = omit,
        model_type: str | Omit = omit,
        order_by: Literal["created_at", "provider", "model", "model_type", "success", "cached"] | Omit = omit,
        order_by_direction: Literal["asc", "desc"] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        provider: str | Omit = omit,
        request_content_type: str | Omit = omit,
        response_content_type: str | Omit = omit,
        search: str | Omit = omit,
        start_date: Union[str, datetime] | Omit = omit,
        success: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
                        "feedback": feedback,
                        "filters": filters,
                        "max_cost": max_cost,
                        "max_duration": max_duration,
                        "max_tokens_in": max_tokens_in,
                        "max_tokens_out": max_tokens_out,
                        "max_total_tokens": max_total_tokens,
                        "meta_info": meta_info,
                        "min_cost": min_cost,
                        "min_duration": min_duration,
                        "min_tokens_in": min_tokens_in,
                        "min_tokens_out": min_tokens_out,
                        "min_total_tokens": min_total_tokens,
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

    async def delete(
        self,
        gateway_id: str,
        *,
        account_id: str,
        filters: Iterable[log_delete_params.Filter] | Omit = omit,
        limit: int | Omit = omit,
        order_by: Literal[
            "created_at",
            "provider",
            "model",
            "model_type",
            "success",
            "cached",
            "cost",
            "tokens_in",
            "tokens_out",
            "duration",
            "feedback",
        ]
        | Omit = omit,
        order_by_direction: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogDeleteResponse:
        """
        Delete Gateway Logs

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
        return await self._delete(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filters": filters,
                        "limit": limit,
                        "order_by": order_by,
                        "order_by_direction": order_by_direction,
                    },
                    log_delete_params.LogDeleteParams,
                ),
            ),
            cast_to=LogDeleteResponse,
        )

    async def edit(
        self,
        id: str,
        *,
        account_id: str,
        gateway_id: str,
        feedback: Optional[float] | Omit = omit,
        metadata: Optional[Dict[str, Union[str, float, bool]]] | Omit = omit,
        score: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Patch Gateway Log

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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs/{id}",
            body=await async_maybe_transform(
                {
                    "feedback": feedback,
                    "metadata": metadata,
                    "score": score,
                },
                log_edit_params.LogEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[object]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    async def get(
        self,
        id: str,
        *,
        account_id: str,
        gateway_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogGetResponse:
        """
        Get Gateway Log Detail

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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[LogGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[LogGetResponse], ResultWrapper[LogGetResponse]),
        )

    async def request(
        self,
        id: str,
        *,
        account_id: str,
        gateway_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get Gateway Log Request

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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs/{id}/request",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def response(
        self,
        id: str,
        *,
        account_id: str,
        gateway_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get Gateway Log Response

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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs/{id}/response",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class LogsResourceWithRawResponse:
    def __init__(self, logs: LogsResource) -> None:
        self._logs = logs

        self.list = to_raw_response_wrapper(
            logs.list,
        )
        self.delete = to_raw_response_wrapper(
            logs.delete,
        )
        self.edit = to_raw_response_wrapper(
            logs.edit,
        )
        self.get = to_raw_response_wrapper(
            logs.get,
        )
        self.request = to_raw_response_wrapper(
            logs.request,
        )
        self.response = to_raw_response_wrapper(
            logs.response,
        )


class AsyncLogsResourceWithRawResponse:
    def __init__(self, logs: AsyncLogsResource) -> None:
        self._logs = logs

        self.list = async_to_raw_response_wrapper(
            logs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            logs.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            logs.edit,
        )
        self.get = async_to_raw_response_wrapper(
            logs.get,
        )
        self.request = async_to_raw_response_wrapper(
            logs.request,
        )
        self.response = async_to_raw_response_wrapper(
            logs.response,
        )


class LogsResourceWithStreamingResponse:
    def __init__(self, logs: LogsResource) -> None:
        self._logs = logs

        self.list = to_streamed_response_wrapper(
            logs.list,
        )
        self.delete = to_streamed_response_wrapper(
            logs.delete,
        )
        self.edit = to_streamed_response_wrapper(
            logs.edit,
        )
        self.get = to_streamed_response_wrapper(
            logs.get,
        )
        self.request = to_streamed_response_wrapper(
            logs.request,
        )
        self.response = to_streamed_response_wrapper(
            logs.response,
        )


class AsyncLogsResourceWithStreamingResponse:
    def __init__(self, logs: AsyncLogsResource) -> None:
        self._logs = logs

        self.list = async_to_streamed_response_wrapper(
            logs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            logs.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            logs.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            logs.get,
        )
        self.request = async_to_streamed_response_wrapper(
            logs.request,
        )
        self.response = async_to_streamed_response_wrapper(
            logs.response,
        )
