# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.logpush import EdgeUpdateResponse, EdgeGetResponse

from typing import Type, Optional

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
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ...types.logpush import edge_update_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Edges", "AsyncEdges"]


class Edges(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EdgesWithRawResponse:
        return EdgesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EdgesWithStreamingResponse:
        return EdgesWithStreamingResponse(self)

    def update(
        self,
        zone_id: str,
        *,
        fields: str | NotGiven = NOT_GIVEN,
        filter: str | NotGiven = NOT_GIVEN,
        sample: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[EdgeUpdateResponse]:
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
                edge_update_params.EdgeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[EdgeUpdateResponse]], ResultWrapper[EdgeUpdateResponse]),
        )

    def get(
        self,
        zone_id: str,
        *,
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


class AsyncEdges(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEdgesWithRawResponse:
        return AsyncEdgesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEdgesWithStreamingResponse:
        return AsyncEdgesWithStreamingResponse(self)

    async def update(
        self,
        zone_id: str,
        *,
        fields: str | NotGiven = NOT_GIVEN,
        filter: str | NotGiven = NOT_GIVEN,
        sample: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[EdgeUpdateResponse]:
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
            body=maybe_transform(
                {
                    "fields": fields,
                    "filter": filter,
                    "sample": sample,
                },
                edge_update_params.EdgeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[EdgeUpdateResponse]], ResultWrapper[EdgeUpdateResponse]),
        )

    async def get(
        self,
        zone_id: str,
        *,
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


class EdgesWithRawResponse:
    def __init__(self, edges: Edges) -> None:
        self._edges = edges

        self.update = to_raw_response_wrapper(
            edges.update,
        )
        self.get = to_raw_response_wrapper(
            edges.get,
        )


class AsyncEdgesWithRawResponse:
    def __init__(self, edges: AsyncEdges) -> None:
        self._edges = edges

        self.update = async_to_raw_response_wrapper(
            edges.update,
        )
        self.get = async_to_raw_response_wrapper(
            edges.get,
        )


class EdgesWithStreamingResponse:
    def __init__(self, edges: Edges) -> None:
        self._edges = edges

        self.update = to_streamed_response_wrapper(
            edges.update,
        )
        self.get = to_streamed_response_wrapper(
            edges.get,
        )


class AsyncEdgesWithStreamingResponse:
    def __init__(self, edges: AsyncEdges) -> None:
        self._edges = edges

        self.update = async_to_streamed_response_wrapper(
            edges.update,
        )
        self.get = async_to_streamed_response_wrapper(
            edges.get,
        )
