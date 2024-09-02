# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .outages import OutagesResource, AsyncOutagesResource

from ...._compat import cached_property

from ....types.radar.annotation_list_response import AnnotationListResponse

from ...._wrappers import ResultWrapper

from ...._utils import maybe_transform, async_maybe_transform

from ...._base_client import make_request_options

from typing import Type, Union

from datetime import datetime

from typing_extensions import Literal

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from ....types.radar import annotation_list_params
from .outages import (
    OutagesResource,
    AsyncOutagesResource,
    OutagesResourceWithRawResponse,
    AsyncOutagesResourceWithRawResponse,
    OutagesResourceWithStreamingResponse,
    AsyncOutagesResourceWithStreamingResponse,
)
from typing import cast
from typing import cast

__all__ = ["AnnotationsResource", "AsyncAnnotationsResource"]


class AnnotationsResource(SyncAPIResource):
    @cached_property
    def outages(self) -> OutagesResource:
        return OutagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AnnotationsResourceWithRawResponse:
        return AnnotationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnnotationsResourceWithStreamingResponse:
        return AnnotationsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        asn: int | NotGiven = NOT_GIVEN,
        date_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        date_range: str | NotGiven = NOT_GIVEN,
        date_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnnotationListResponse:
        """
        Get latest annotations.

        Args:
          asn: Single ASN as integer.

          date_end: End of the date range (inclusive).

          date_range: Shorthand date ranges for the last X days - use when you don't need specific
              start and end dates.

          date_start: Start of the date range (inclusive).

          format: Format results are returned in.

          limit: Limit the number of objects in the response.

          location: Location Alpha2 code.

          offset: Number of objects to skip before grabbing results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/annotations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asn": asn,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "limit": limit,
                        "location": location,
                        "offset": offset,
                    },
                    annotation_list_params.AnnotationListParams,
                ),
                post_parser=ResultWrapper[AnnotationListResponse]._unwrapper,
            ),
            cast_to=cast(Type[AnnotationListResponse], ResultWrapper[AnnotationListResponse]),
        )


class AsyncAnnotationsResource(AsyncAPIResource):
    @cached_property
    def outages(self) -> AsyncOutagesResource:
        return AsyncOutagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAnnotationsResourceWithRawResponse:
        return AsyncAnnotationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnnotationsResourceWithStreamingResponse:
        return AsyncAnnotationsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        asn: int | NotGiven = NOT_GIVEN,
        date_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        date_range: str | NotGiven = NOT_GIVEN,
        date_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnnotationListResponse:
        """
        Get latest annotations.

        Args:
          asn: Single ASN as integer.

          date_end: End of the date range (inclusive).

          date_range: Shorthand date ranges for the last X days - use when you don't need specific
              start and end dates.

          date_start: Start of the date range (inclusive).

          format: Format results are returned in.

          limit: Limit the number of objects in the response.

          location: Location Alpha2 code.

          offset: Number of objects to skip before grabbing results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/annotations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "asn": asn,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "limit": limit,
                        "location": location,
                        "offset": offset,
                    },
                    annotation_list_params.AnnotationListParams,
                ),
                post_parser=ResultWrapper[AnnotationListResponse]._unwrapper,
            ),
            cast_to=cast(Type[AnnotationListResponse], ResultWrapper[AnnotationListResponse]),
        )


class AnnotationsResourceWithRawResponse:
    def __init__(self, annotations: AnnotationsResource) -> None:
        self._annotations = annotations

        self.list = to_raw_response_wrapper(
            annotations.list,
        )

    @cached_property
    def outages(self) -> OutagesResourceWithRawResponse:
        return OutagesResourceWithRawResponse(self._annotations.outages)


class AsyncAnnotationsResourceWithRawResponse:
    def __init__(self, annotations: AsyncAnnotationsResource) -> None:
        self._annotations = annotations

        self.list = async_to_raw_response_wrapper(
            annotations.list,
        )

    @cached_property
    def outages(self) -> AsyncOutagesResourceWithRawResponse:
        return AsyncOutagesResourceWithRawResponse(self._annotations.outages)


class AnnotationsResourceWithStreamingResponse:
    def __init__(self, annotations: AnnotationsResource) -> None:
        self._annotations = annotations

        self.list = to_streamed_response_wrapper(
            annotations.list,
        )

    @cached_property
    def outages(self) -> OutagesResourceWithStreamingResponse:
        return OutagesResourceWithStreamingResponse(self._annotations.outages)


class AsyncAnnotationsResourceWithStreamingResponse:
    def __init__(self, annotations: AsyncAnnotationsResource) -> None:
        self._annotations = annotations

        self.list = async_to_streamed_response_wrapper(
            annotations.list,
        )

    @cached_property
    def outages(self) -> AsyncOutagesResourceWithStreamingResponse:
        return AsyncOutagesResourceWithStreamingResponse(self._annotations.outages)
