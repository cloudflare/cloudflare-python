# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ..._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    to_custom_raw_response_wrapper,
    async_to_custom_raw_response_wrapper,
    to_custom_streamed_response_wrapper,
    StreamedBinaryAPIResponse,
    async_to_custom_streamed_response_wrapper,
    AsyncStreamedBinaryAPIResponse,
)

from ..._base_client import make_request_options

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params

__all__ = ["ContentResource", "AsyncContentResource"]


class ContentResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContentResourceWithRawResponse:
        return ContentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContentResourceWithStreamingResponse:
        return ContentResourceWithStreamingResponse(self)

    def get(
        self,
        snippet_name: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """
        Snippet Content

        Args:
          zone_id: Identifier

          snippet_name: Snippet identifying name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not snippet_name:
            raise ValueError(f"Expected a non-empty value for `snippet_name` but received {snippet_name!r}")
        extra_headers = {"Accept": "multipart/form-data", **(extra_headers or {})}
        return self._get(
            f"/zones/{zone_id}/snippets/{snippet_name}/content",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncContentResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContentResourceWithRawResponse:
        return AsyncContentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContentResourceWithStreamingResponse:
        return AsyncContentResourceWithStreamingResponse(self)

    async def get(
        self,
        snippet_name: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """
        Snippet Content

        Args:
          zone_id: Identifier

          snippet_name: Snippet identifying name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not snippet_name:
            raise ValueError(f"Expected a non-empty value for `snippet_name` but received {snippet_name!r}")
        extra_headers = {"Accept": "multipart/form-data", **(extra_headers or {})}
        return await self._get(
            f"/zones/{zone_id}/snippets/{snippet_name}/content",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class ContentResourceWithRawResponse:
    def __init__(self, content: ContentResource) -> None:
        self._content = content

        self.get = to_custom_raw_response_wrapper(
            content.get,
            BinaryAPIResponse,
        )


class AsyncContentResourceWithRawResponse:
    def __init__(self, content: AsyncContentResource) -> None:
        self._content = content

        self.get = async_to_custom_raw_response_wrapper(
            content.get,
            AsyncBinaryAPIResponse,
        )


class ContentResourceWithStreamingResponse:
    def __init__(self, content: ContentResource) -> None:
        self._content = content

        self.get = to_custom_streamed_response_wrapper(
            content.get,
            StreamedBinaryAPIResponse,
        )


class AsyncContentResourceWithStreamingResponse:
    def __init__(self, content: AsyncContentResource) -> None:
        self._content = content

        self.get = async_to_custom_streamed_response_wrapper(
            content.get,
            AsyncStreamedBinaryAPIResponse,
        )
