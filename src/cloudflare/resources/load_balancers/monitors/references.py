# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.load_balancers.monitors.reference_get_response import ReferenceGetResponse

from ...._wrappers import ResultWrapper

from ...._base_client import make_request_options

from typing import Type

from ...._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from typing import cast
from typing import cast

__all__ = ["ReferencesResource", "AsyncReferencesResource"]

class ReferencesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReferencesResourceWithRawResponse:
        return ReferencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReferencesResourceWithStreamingResponse:
        return ReferencesResourceWithStreamingResponse(self)

    def get(self,
    monitor_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> ReferenceGetResponse:
        """
        Get the list of resources that reference the provided monitor.

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
        if not monitor_id:
          raise ValueError(
            f'Expected a non-empty value for `monitor_id` but received {monitor_id!r}'
          )
        return self._get(
            f"/accounts/{account_id}/load_balancers/monitors/{monitor_id}/references",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[ReferenceGetResponse]._unwrapper),
            cast_to=cast(Type[ReferenceGetResponse], ResultWrapper[ReferenceGetResponse]),
        )

class AsyncReferencesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReferencesResourceWithRawResponse:
        return AsyncReferencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReferencesResourceWithStreamingResponse:
        return AsyncReferencesResourceWithStreamingResponse(self)

    async def get(self,
    monitor_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> ReferenceGetResponse:
        """
        Get the list of resources that reference the provided monitor.

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
        if not monitor_id:
          raise ValueError(
            f'Expected a non-empty value for `monitor_id` but received {monitor_id!r}'
          )
        return await self._get(
            f"/accounts/{account_id}/load_balancers/monitors/{monitor_id}/references",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[ReferenceGetResponse]._unwrapper),
            cast_to=cast(Type[ReferenceGetResponse], ResultWrapper[ReferenceGetResponse]),
        )

class ReferencesResourceWithRawResponse:
    def __init__(self, references: ReferencesResource) -> None:
        self._references = references

        self.get = to_raw_response_wrapper(
            references.get,
        )

class AsyncReferencesResourceWithRawResponse:
    def __init__(self, references: AsyncReferencesResource) -> None:
        self._references = references

        self.get = async_to_raw_response_wrapper(
            references.get,
        )

class ReferencesResourceWithStreamingResponse:
    def __init__(self, references: ReferencesResource) -> None:
        self._references = references

        self.get = to_streamed_response_wrapper(
            references.get,
        )

class AsyncReferencesResourceWithStreamingResponse:
    def __init__(self, references: AsyncReferencesResource) -> None:
        self._references = references

        self.get = async_to_streamed_response_wrapper(
            references.get,
        )