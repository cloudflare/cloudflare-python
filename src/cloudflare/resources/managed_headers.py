# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._compat import cached_property

from ..types.managed_headers.managed_header_list_response import ManagedHeaderListResponse

from .._base_client import make_request_options

from ..types.managed_headers.managed_header_edit_response import ManagedHeaderEditResponse

from .._utils import maybe_transform, async_maybe_transform

from typing import Iterable

from ..types.managed_headers.request_model_param import RequestModelParam

from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from .._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from .._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from .._resource import SyncAPIResource, AsyncAPIResource
from ..types import shared_params
from ..types.managed_headers import managed_header_edit_params

__all__ = ["ManagedHeadersResource", "AsyncManagedHeadersResource"]

class ManagedHeadersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ManagedHeadersResourceWithRawResponse:
        return ManagedHeadersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ManagedHeadersResourceWithStreamingResponse:
        return ManagedHeadersResourceWithStreamingResponse(self)

    def list(self,
    *,
    zone_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> ManagedHeaderListResponse:
        """
        Fetches a list of all Managed Transforms.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
          raise ValueError(
            f'Expected a non-empty value for `zone_id` but received {zone_id!r}'
          )
        return self._get(
            f"/zones/{zone_id}/managed_headers",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ManagedHeaderListResponse,
        )

    def edit(self,
    *,
    zone_id: str,
    managed_request_headers: Iterable[RequestModelParam],
    managed_response_headers: Iterable[RequestModelParam],
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> ManagedHeaderEditResponse:
        """
        Updates the status of one or more Managed Transforms.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
          raise ValueError(
            f'Expected a non-empty value for `zone_id` but received {zone_id!r}'
          )
        return self._patch(
            f"/zones/{zone_id}/managed_headers",
            body=maybe_transform({
                "managed_request_headers": managed_request_headers,
                "managed_response_headers": managed_response_headers,
            }, managed_header_edit_params.ManagedHeaderEditParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ManagedHeaderEditResponse,
        )

class AsyncManagedHeadersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncManagedHeadersResourceWithRawResponse:
        return AsyncManagedHeadersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncManagedHeadersResourceWithStreamingResponse:
        return AsyncManagedHeadersResourceWithStreamingResponse(self)

    async def list(self,
    *,
    zone_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> ManagedHeaderListResponse:
        """
        Fetches a list of all Managed Transforms.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
          raise ValueError(
            f'Expected a non-empty value for `zone_id` but received {zone_id!r}'
          )
        return await self._get(
            f"/zones/{zone_id}/managed_headers",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ManagedHeaderListResponse,
        )

    async def edit(self,
    *,
    zone_id: str,
    managed_request_headers: Iterable[RequestModelParam],
    managed_response_headers: Iterable[RequestModelParam],
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> ManagedHeaderEditResponse:
        """
        Updates the status of one or more Managed Transforms.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
          raise ValueError(
            f'Expected a non-empty value for `zone_id` but received {zone_id!r}'
          )
        return await self._patch(
            f"/zones/{zone_id}/managed_headers",
            body=await async_maybe_transform({
                "managed_request_headers": managed_request_headers,
                "managed_response_headers": managed_response_headers,
            }, managed_header_edit_params.ManagedHeaderEditParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ManagedHeaderEditResponse,
        )

class ManagedHeadersResourceWithRawResponse:
    def __init__(self, managed_headers: ManagedHeadersResource) -> None:
        self._managed_headers = managed_headers

        self.list = to_raw_response_wrapper(
            managed_headers.list,
        )
        self.edit = to_raw_response_wrapper(
            managed_headers.edit,
        )

class AsyncManagedHeadersResourceWithRawResponse:
    def __init__(self, managed_headers: AsyncManagedHeadersResource) -> None:
        self._managed_headers = managed_headers

        self.list = async_to_raw_response_wrapper(
            managed_headers.list,
        )
        self.edit = async_to_raw_response_wrapper(
            managed_headers.edit,
        )

class ManagedHeadersResourceWithStreamingResponse:
    def __init__(self, managed_headers: ManagedHeadersResource) -> None:
        self._managed_headers = managed_headers

        self.list = to_streamed_response_wrapper(
            managed_headers.list,
        )
        self.edit = to_streamed_response_wrapper(
            managed_headers.edit,
        )

class AsyncManagedHeadersResourceWithStreamingResponse:
    def __init__(self, managed_headers: AsyncManagedHeadersResource) -> None:
        self._managed_headers = managed_headers

        self.list = async_to_streamed_response_wrapper(
            managed_headers.list,
        )
        self.edit = async_to_streamed_response_wrapper(
            managed_headers.edit,
        )