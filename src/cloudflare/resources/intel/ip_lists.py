# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.intel.ip_list_get_response import IPListGetResponse

from ..._wrappers import ResultWrapper

from typing import Optional, Type

from ..._base_client import make_request_options

from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from typing import cast
from typing import cast

__all__ = ["IPListsResource", "AsyncIPListsResource"]

class IPListsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IPListsResourceWithRawResponse:
        return IPListsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IPListsResourceWithStreamingResponse:
        return IPListsResourceWithStreamingResponse(self)

    def get(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[IPListGetResponse]:
        """
        Get IP Lists

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._get(
            f"/accounts/{account_id}/intel/ip-list",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[IPListGetResponse]]._unwrapper),
            cast_to=cast(Type[Optional[IPListGetResponse]], ResultWrapper[IPListGetResponse]),
        )

class AsyncIPListsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIPListsResourceWithRawResponse:
        return AsyncIPListsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIPListsResourceWithStreamingResponse:
        return AsyncIPListsResourceWithStreamingResponse(self)

    async def get(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[IPListGetResponse]:
        """
        Get IP Lists

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return await self._get(
            f"/accounts/{account_id}/intel/ip-list",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[IPListGetResponse]]._unwrapper),
            cast_to=cast(Type[Optional[IPListGetResponse]], ResultWrapper[IPListGetResponse]),
        )

class IPListsResourceWithRawResponse:
    def __init__(self, ip_lists: IPListsResource) -> None:
        self._ip_lists = ip_lists

        self.get = to_raw_response_wrapper(
            ip_lists.get,
        )

class AsyncIPListsResourceWithRawResponse:
    def __init__(self, ip_lists: AsyncIPListsResource) -> None:
        self._ip_lists = ip_lists

        self.get = async_to_raw_response_wrapper(
            ip_lists.get,
        )

class IPListsResourceWithStreamingResponse:
    def __init__(self, ip_lists: IPListsResource) -> None:
        self._ip_lists = ip_lists

        self.get = to_streamed_response_wrapper(
            ip_lists.get,
        )

class AsyncIPListsResourceWithStreamingResponse:
    def __init__(self, ip_lists: AsyncIPListsResource) -> None:
        self._ip_lists = ip_lists

        self.get = async_to_streamed_response_wrapper(
            ip_lists.get,
        )