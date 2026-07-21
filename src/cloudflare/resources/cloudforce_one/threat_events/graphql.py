# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import path_template
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.cloudforce_one.threat_events.graphql_create_response import GraphqlCreateResponse

__all__ = ["GraphqlResource", "AsyncGraphqlResource"]


class GraphqlResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GraphqlResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return GraphqlResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GraphqlResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return GraphqlResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GraphqlCreateResponse:
        """Execute GraphQL aggregations over threat events.

        Supports multi-dimensional
        group-bys, optional date range filtering, and multi-dataset aggregation.

        Args:
          account_id: Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/cloudforce-one/events/graphql", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GraphqlCreateResponse,
        )


class AsyncGraphqlResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGraphqlResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGraphqlResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGraphqlResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncGraphqlResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GraphqlCreateResponse:
        """Execute GraphQL aggregations over threat events.

        Supports multi-dimensional
        group-bys, optional date range filtering, and multi-dataset aggregation.

        Args:
          account_id: Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/cloudforce-one/events/graphql", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GraphqlCreateResponse,
        )


class GraphqlResourceWithRawResponse:
    def __init__(self, graphql: GraphqlResource) -> None:
        self._graphql = graphql

        self.create = to_raw_response_wrapper(
            graphql.create,
        )


class AsyncGraphqlResourceWithRawResponse:
    def __init__(self, graphql: AsyncGraphqlResource) -> None:
        self._graphql = graphql

        self.create = async_to_raw_response_wrapper(
            graphql.create,
        )


class GraphqlResourceWithStreamingResponse:
    def __init__(self, graphql: GraphqlResource) -> None:
        self._graphql = graphql

        self.create = to_streamed_response_wrapper(
            graphql.create,
        )


class AsyncGraphqlResourceWithStreamingResponse:
    def __init__(self, graphql: AsyncGraphqlResource) -> None:
        self._graphql = graphql

        self.create = async_to_streamed_response_wrapper(
            graphql.create,
        )
