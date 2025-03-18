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
from ...pagination import SyncSinglePage, AsyncSinglePage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.logpush import edge_create_params
from ...types.logpush.instant_logpush_job import InstantLogpushJob

__all__ = ["EdgeResource", "AsyncEdgeResource"]


class EdgeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EdgeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return EdgeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EdgeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return EdgeResourceWithStreamingResponse(self)

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
    ) -> Optional[InstantLogpushJob]:
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
                post_parser=ResultWrapper[Optional[InstantLogpushJob]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[InstantLogpushJob]], ResultWrapper[InstantLogpushJob]),
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
    ) -> SyncSinglePage[Optional[InstantLogpushJob]]:
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
        return self._get_api_list(
            f"/zones/{zone_id}/logpush/edge",
            page=SyncSinglePage[Optional[InstantLogpushJob]],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=InstantLogpushJob,
        )


class AsyncEdgeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEdgeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEdgeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEdgeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncEdgeResourceWithStreamingResponse(self)

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
    ) -> Optional[InstantLogpushJob]:
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
                post_parser=ResultWrapper[Optional[InstantLogpushJob]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[InstantLogpushJob]], ResultWrapper[InstantLogpushJob]),
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
    ) -> AsyncPaginator[Optional[InstantLogpushJob], AsyncSinglePage[Optional[InstantLogpushJob]]]:
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
        return self._get_api_list(
            f"/zones/{zone_id}/logpush/edge",
            page=AsyncSinglePage[Optional[InstantLogpushJob]],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=InstantLogpushJob,
        )


class EdgeResourceWithRawResponse:
    def __init__(self, edge: EdgeResource) -> None:
        self._edge = edge

        self.create = to_raw_response_wrapper(
            edge.create,
        )
        self.get = to_raw_response_wrapper(
            edge.get,
        )


class AsyncEdgeResourceWithRawResponse:
    def __init__(self, edge: AsyncEdgeResource) -> None:
        self._edge = edge

        self.create = async_to_raw_response_wrapper(
            edge.create,
        )
        self.get = async_to_raw_response_wrapper(
            edge.get,
        )


class EdgeResourceWithStreamingResponse:
    def __init__(self, edge: EdgeResource) -> None:
        self._edge = edge

        self.create = to_streamed_response_wrapper(
            edge.create,
        )
        self.get = to_streamed_response_wrapper(
            edge.get,
        )


class AsyncEdgeResourceWithStreamingResponse:
    def __init__(self, edge: AsyncEdgeResource) -> None:
        self._edge = edge

        self.create = async_to_streamed_response_wrapper(
            edge.create,
        )
        self.get = async_to_streamed_response_wrapper(
            edge.get,
        )
