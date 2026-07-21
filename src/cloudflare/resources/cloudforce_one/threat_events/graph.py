# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ...._base_client import make_request_options
from ....types.cloudforce_one.threat_events import graph_list_params
from ....types.cloudforce_one.threat_events.graph_list_response import GraphListResponse

__all__ = ["GraphResource", "AsyncGraphResource"]


class GraphResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GraphResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return GraphResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GraphResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return GraphResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        dataset_ids: SequenceNotStr[str] | Omit = omit,
        direction: str | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        hydration: str | Omit = omit,
        limit: float | Omit = omit,
        max_nodes: float | Omit = omit,
        relationship_types: SequenceNotStr[str] | Omit = omit,
        seeds: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GraphListResponse:
        """
        Expands the single-level relationship neighborhood of one or more seed nodes
        (event, indicator, or tag) from R2 Data Catalog. Seeds use compact id format
        (type:uuid), e.g. "event:550e8400-...". Multi-seed requests merge and
        deduplicate results server-side. Hydrates neighbor entities with summary data
        from Durable Objects. Supports filtering by relationship type and dataset scope.

        Args:
          account_id: Account ID.

          cursor: Opaque pagination token. Only valid when seeds has exactly 1 entry; 400
              otherwise.

          dataset_ids: Comma-separated dataset UUIDs to restrict neighbor scope. Intersected with ACL
              grants.

          direction: Edge direction relative to each seed: out (seed→neighbors), in (neighbors→seed),
              both (default).

          expand: Comma-separated list of response sections to expand (hydrate). Allowed: `nodes`.
              Omitting `expand` returns identifier-only nodes.

          hydration: Hydration strategy for neighbor nodes when expand=nodes is set. r2_join
              (default): use R2 JOIN query + DO fallback. do_only: use plain R2 query +
              hydrate all neighbors via Durable Objects.

          limit: Max neighbors per seed (default: 100, max: 1000). Values above 1000 return 400.

          max_nodes: Total accumulated node cap across all seeds (default: 500, max: 1000). Values
              above 1000 return 400.

          relationship_types: Comma-separated relationship types to filter by. Allowed: tagged_with,
              appears_in, related_to, caused_by, attributed_to.

          seeds:
              Comma-separated compact seed ids (type:uuid). Example:
              seeds=event:550e8400-...,indicator:661fa920-... Provide 1–50 entries; omitting
              seeds returns 400.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/cloudforce-one/events/graph", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "dataset_ids": dataset_ids,
                        "direction": direction,
                        "expand": expand,
                        "hydration": hydration,
                        "limit": limit,
                        "max_nodes": max_nodes,
                        "relationship_types": relationship_types,
                        "seeds": seeds,
                    },
                    graph_list_params.GraphListParams,
                ),
                post_parser=ResultWrapper[GraphListResponse]._unwrapper,
            ),
            cast_to=cast(Type[GraphListResponse], ResultWrapper[GraphListResponse]),
        )


class AsyncGraphResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGraphResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGraphResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGraphResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncGraphResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        dataset_ids: SequenceNotStr[str] | Omit = omit,
        direction: str | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        hydration: str | Omit = omit,
        limit: float | Omit = omit,
        max_nodes: float | Omit = omit,
        relationship_types: SequenceNotStr[str] | Omit = omit,
        seeds: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GraphListResponse:
        """
        Expands the single-level relationship neighborhood of one or more seed nodes
        (event, indicator, or tag) from R2 Data Catalog. Seeds use compact id format
        (type:uuid), e.g. "event:550e8400-...". Multi-seed requests merge and
        deduplicate results server-side. Hydrates neighbor entities with summary data
        from Durable Objects. Supports filtering by relationship type and dataset scope.

        Args:
          account_id: Account ID.

          cursor: Opaque pagination token. Only valid when seeds has exactly 1 entry; 400
              otherwise.

          dataset_ids: Comma-separated dataset UUIDs to restrict neighbor scope. Intersected with ACL
              grants.

          direction: Edge direction relative to each seed: out (seed→neighbors), in (neighbors→seed),
              both (default).

          expand: Comma-separated list of response sections to expand (hydrate). Allowed: `nodes`.
              Omitting `expand` returns identifier-only nodes.

          hydration: Hydration strategy for neighbor nodes when expand=nodes is set. r2_join
              (default): use R2 JOIN query + DO fallback. do_only: use plain R2 query +
              hydrate all neighbors via Durable Objects.

          limit: Max neighbors per seed (default: 100, max: 1000). Values above 1000 return 400.

          max_nodes: Total accumulated node cap across all seeds (default: 500, max: 1000). Values
              above 1000 return 400.

          relationship_types: Comma-separated relationship types to filter by. Allowed: tagged_with,
              appears_in, related_to, caused_by, attributed_to.

          seeds:
              Comma-separated compact seed ids (type:uuid). Example:
              seeds=event:550e8400-...,indicator:661fa920-... Provide 1–50 entries; omitting
              seeds returns 400.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/cloudforce-one/events/graph", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "dataset_ids": dataset_ids,
                        "direction": direction,
                        "expand": expand,
                        "hydration": hydration,
                        "limit": limit,
                        "max_nodes": max_nodes,
                        "relationship_types": relationship_types,
                        "seeds": seeds,
                    },
                    graph_list_params.GraphListParams,
                ),
                post_parser=ResultWrapper[GraphListResponse]._unwrapper,
            ),
            cast_to=cast(Type[GraphListResponse], ResultWrapper[GraphListResponse]),
        )


class GraphResourceWithRawResponse:
    def __init__(self, graph: GraphResource) -> None:
        self._graph = graph

        self.list = to_raw_response_wrapper(
            graph.list,
        )


class AsyncGraphResourceWithRawResponse:
    def __init__(self, graph: AsyncGraphResource) -> None:
        self._graph = graph

        self.list = async_to_raw_response_wrapper(
            graph.list,
        )


class GraphResourceWithStreamingResponse:
    def __init__(self, graph: GraphResource) -> None:
        self._graph = graph

        self.list = to_streamed_response_wrapper(
            graph.list,
        )


class AsyncGraphResourceWithStreamingResponse:
    def __init__(self, graph: AsyncGraphResource) -> None:
        self._graph = graph

        self.list = async_to_streamed_response_wrapper(
            graph.list,
        )
