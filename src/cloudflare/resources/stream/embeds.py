# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

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
from ..._wrappers import ResultWrapper

__all__ = ["Embeds", "AsyncEmbeds"]


class Embeds(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmbedsWithRawResponse:
        return EmbedsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmbedsWithStreamingResponse:
        return EmbedsWithStreamingResponse(self)

    def list(
        self,
        identifier: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Fetches an HTML code snippet to embed a video in a web page delivered through
        Cloudflare. On success, returns an HTML fragment for use on web pages to display
        a video. On failure, returns a JSON response body.

        Args:
          account_id: The account identifier tag.

          identifier: A Cloudflare-generated unique identifier for a media item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._get(
            f"/accounts/{account_id}/stream/{identifier}/embed",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncEmbeds(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmbedsWithRawResponse:
        return AsyncEmbedsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmbedsWithStreamingResponse:
        return AsyncEmbedsWithStreamingResponse(self)

    async def list(
        self,
        identifier: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Fetches an HTML code snippet to embed a video in a web page delivered through
        Cloudflare. On success, returns an HTML fragment for use on web pages to display
        a video. On failure, returns a JSON response body.

        Args:
          account_id: The account identifier tag.

          identifier: A Cloudflare-generated unique identifier for a media item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return await self._get(
            f"/accounts/{account_id}/stream/{identifier}/embed",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class EmbedsWithRawResponse:
    def __init__(self, embeds: Embeds) -> None:
        self._embeds = embeds

        self.list = to_raw_response_wrapper(
            embeds.list,
        )


class AsyncEmbedsWithRawResponse:
    def __init__(self, embeds: AsyncEmbeds) -> None:
        self._embeds = embeds

        self.list = async_to_raw_response_wrapper(
            embeds.list,
        )


class EmbedsWithStreamingResponse:
    def __init__(self, embeds: Embeds) -> None:
        self._embeds = embeds

        self.list = to_streamed_response_wrapper(
            embeds.list,
        )


class AsyncEmbedsWithStreamingResponse:
    def __init__(self, embeds: AsyncEmbeds) -> None:
        self._embeds = embeds

        self.list = async_to_streamed_response_wrapper(
            embeds.list,
        )
