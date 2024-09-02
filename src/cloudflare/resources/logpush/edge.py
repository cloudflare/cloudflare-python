# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.logpush.instant_logpush_job import InstantLogpushJob

from ..._wrappers import ResultWrapper

from ..._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type

from ..._base_client import make_request_options

from ...types.logpush.edge_get_response import EdgeGetResponse

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
from ...types.logpush import edge_create_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["EdgeResource", "AsyncEdgeResource"]


class EdgeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EdgeResourceWithRawResponse:
        return EdgeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EdgeResourceWithStreamingResponse:
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
    ) -> Optional[EdgeGetResponse]:
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
                post_parser=ResultWrapper[Optional[EdgeGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[EdgeGetResponse]], ResultWrapper[EdgeGetResponse]),
        )


class AsyncEdgeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEdgeResourceWithRawResponse:
        return AsyncEdgeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEdgeResourceWithStreamingResponse:
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
    ) -> Optional[EdgeGetResponse]:
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
                post_parser=ResultWrapper[Optional[EdgeGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[EdgeGetResponse]], ResultWrapper[EdgeGetResponse]),
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
