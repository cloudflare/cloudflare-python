# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

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
from ...types.logpush import EdgeGetResponse, LogpushInstantLogsJob, edge_create_params

__all__ = ["Edge", "AsyncEdge"]


class Edge(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EdgeWithRawResponse:
        return EdgeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EdgeWithStreamingResponse:
        return EdgeWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        fields: str | NotGiven = NOT_GIVEN,
        filter: str | NotGiven = NOT_GIVEN,
        sample: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[LogpushInstantLogsJob]:
        """
        Creates a new Instant Logs job for a zone.

        Args:
          zone_id: Identifier

          fields: Comma-separated list of fields.

          filter: Filters to drill down into specific events.

          sample:
              The sample parameter is the sample rate of the records set by the client:
              "sample": 1 is 100% of records "sample": 10 is 10% and so on.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/logpush/edge",
            body=maybe_transform(
                {
                    "fields": fields,
                    "filter": filter,
                    "sample": sample,
                },
                edge_create_params.EdgeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[LogpushInstantLogsJob]], ResultWrapper[LogpushInstantLogsJob]),
        )

    def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EdgeGetResponse:
        """
        Lists Instant Logs jobs for a zone.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/logpush/edge",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[EdgeGetResponse], ResultWrapper[EdgeGetResponse]),
        )


class AsyncEdge(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEdgeWithRawResponse:
        return AsyncEdgeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEdgeWithStreamingResponse:
        return AsyncEdgeWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: str,
        fields: str | NotGiven = NOT_GIVEN,
        filter: str | NotGiven = NOT_GIVEN,
        sample: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[LogpushInstantLogsJob]:
        """
        Creates a new Instant Logs job for a zone.

        Args:
          zone_id: Identifier

          fields: Comma-separated list of fields.

          filter: Filters to drill down into specific events.

          sample:
              The sample parameter is the sample rate of the records set by the client:
              "sample": 1 is 100% of records "sample": 10 is 10% and so on.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/logpush/edge",
            body=await async_maybe_transform(
                {
                    "fields": fields,
                    "filter": filter,
                    "sample": sample,
                },
                edge_create_params.EdgeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[LogpushInstantLogsJob]], ResultWrapper[LogpushInstantLogsJob]),
        )

    async def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EdgeGetResponse:
        """
        Lists Instant Logs jobs for a zone.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/logpush/edge",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[EdgeGetResponse], ResultWrapper[EdgeGetResponse]),
        )


class EdgeWithRawResponse:
    def __init__(self, edge: Edge) -> None:
        self._edge = edge

        self.create = to_raw_response_wrapper(
            edge.create,
        )
        self.get = to_raw_response_wrapper(
            edge.get,
        )


class AsyncEdgeWithRawResponse:
    def __init__(self, edge: AsyncEdge) -> None:
        self._edge = edge

        self.create = async_to_raw_response_wrapper(
            edge.create,
        )
        self.get = async_to_raw_response_wrapper(
            edge.get,
        )


class EdgeWithStreamingResponse:
    def __init__(self, edge: Edge) -> None:
        self._edge = edge

        self.create = to_streamed_response_wrapper(
            edge.create,
        )
        self.get = to_streamed_response_wrapper(
            edge.get,
        )


class AsyncEdgeWithStreamingResponse:
    def __init__(self, edge: AsyncEdge) -> None:
        self._edge = edge

        self.create = async_to_streamed_response_wrapper(
            edge.create,
        )
        self.get = async_to_streamed_response_wrapper(
            edge.get,
        )
