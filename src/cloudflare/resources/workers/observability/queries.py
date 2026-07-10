# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.workers.observability import query_list_params, query_create_params
from ....types.workers.observability.query_list_response import QueryListResponse
from ....types.workers.observability.query_create_response import QueryCreateResponse

__all__ = ["QueriesResource", "AsyncQueriesResource"]


class QueriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QueriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return QueriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QueriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return QueriesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        description: Optional[str],
        name: str,
        parameters: query_create_params.Parameters,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueryCreateResponse:
        """
        Persist query for later use.

        Args:
          name: Query name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/workers/observability/queries", account_id=account_id),
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "parameters": parameters,
                },
                query_create_params.QueryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[QueryCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[QueryCreateResponse], ResultWrapper[QueryCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["created", "updated"] | Omit = omit,
        page: float | Omit = omit,
        per_page: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[QueryListResponse]:
        """
        List saved queries.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/workers/observability/queries", account_id=account_id),
            page=SyncSinglePage[QueryListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "order": order,
                        "order_by": order_by,
                        "page": page,
                        "per_page": per_page,
                    },
                    query_list_params.QueryListParams,
                ),
            ),
            model=QueryListResponse,
        )


class AsyncQueriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQueriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQueriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQueriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncQueriesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        description: Optional[str],
        name: str,
        parameters: query_create_params.Parameters,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueryCreateResponse:
        """
        Persist query for later use.

        Args:
          name: Query name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/workers/observability/queries", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "parameters": parameters,
                },
                query_create_params.QueryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[QueryCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[QueryCreateResponse], ResultWrapper[QueryCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["created", "updated"] | Omit = omit,
        page: float | Omit = omit,
        per_page: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[QueryListResponse, AsyncSinglePage[QueryListResponse]]:
        """
        List saved queries.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/workers/observability/queries", account_id=account_id),
            page=AsyncSinglePage[QueryListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "order": order,
                        "order_by": order_by,
                        "page": page,
                        "per_page": per_page,
                    },
                    query_list_params.QueryListParams,
                ),
            ),
            model=QueryListResponse,
        )


class QueriesResourceWithRawResponse:
    def __init__(self, queries: QueriesResource) -> None:
        self._queries = queries

        self.create = to_raw_response_wrapper(
            queries.create,
        )
        self.list = to_raw_response_wrapper(
            queries.list,
        )


class AsyncQueriesResourceWithRawResponse:
    def __init__(self, queries: AsyncQueriesResource) -> None:
        self._queries = queries

        self.create = async_to_raw_response_wrapper(
            queries.create,
        )
        self.list = async_to_raw_response_wrapper(
            queries.list,
        )


class QueriesResourceWithStreamingResponse:
    def __init__(self, queries: QueriesResource) -> None:
        self._queries = queries

        self.create = to_streamed_response_wrapper(
            queries.create,
        )
        self.list = to_streamed_response_wrapper(
            queries.list,
        )


class AsyncQueriesResourceWithStreamingResponse:
    def __init__(self, queries: AsyncQueriesResource) -> None:
        self._queries = queries

        self.create = async_to_streamed_response_wrapper(
            queries.create,
        )
        self.list = async_to_streamed_response_wrapper(
            queries.list,
        )
