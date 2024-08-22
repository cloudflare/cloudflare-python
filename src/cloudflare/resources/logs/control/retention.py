# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.logs.control.retention_create_response import RetentionCreateResponse

from ...._wrappers import ResultWrapper

from ...._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type

from ...._base_client import make_request_options

from ....types.logs.control.retention_get_response import RetentionGetResponse

from ...._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from ....types.logs.control import retention_create_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["RetentionResource", "AsyncRetentionResource"]

class RetentionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RetentionResourceWithRawResponse:
        return RetentionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RetentionResourceWithStreamingResponse:
        return RetentionResourceWithStreamingResponse(self)

    def create(self,
    *,
    zone_id: str,
    flag: bool | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[RetentionCreateResponse]:
        """
        Updates log retention flag for Logpull API.

        Args:
          zone_id: Identifier

          flag: The log retention flag for Logpull API.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
          raise ValueError(
            f'Expected a non-empty value for `zone_id` but received {zone_id!r}'
          )
        return self._post(
            f"/zones/{zone_id}/logs/control/retention/flag",
            body=maybe_transform({
                "flag": flag
            }, retention_create_params.RetentionCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[RetentionCreateResponse]]._unwrapper),
            cast_to=cast(Type[Optional[RetentionCreateResponse]], ResultWrapper[RetentionCreateResponse]),
        )

    def get(self,
    *,
    zone_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[RetentionGetResponse]:
        """
        Gets log retention flag for Logpull API.

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
            f"/zones/{zone_id}/logs/control/retention/flag",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[RetentionGetResponse]]._unwrapper),
            cast_to=cast(Type[Optional[RetentionGetResponse]], ResultWrapper[RetentionGetResponse]),
        )

class AsyncRetentionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRetentionResourceWithRawResponse:
        return AsyncRetentionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRetentionResourceWithStreamingResponse:
        return AsyncRetentionResourceWithStreamingResponse(self)

    async def create(self,
    *,
    zone_id: str,
    flag: bool | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[RetentionCreateResponse]:
        """
        Updates log retention flag for Logpull API.

        Args:
          zone_id: Identifier

          flag: The log retention flag for Logpull API.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
          raise ValueError(
            f'Expected a non-empty value for `zone_id` but received {zone_id!r}'
          )
        return await self._post(
            f"/zones/{zone_id}/logs/control/retention/flag",
            body=await async_maybe_transform({
                "flag": flag
            }, retention_create_params.RetentionCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[RetentionCreateResponse]]._unwrapper),
            cast_to=cast(Type[Optional[RetentionCreateResponse]], ResultWrapper[RetentionCreateResponse]),
        )

    async def get(self,
    *,
    zone_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[RetentionGetResponse]:
        """
        Gets log retention flag for Logpull API.

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
            f"/zones/{zone_id}/logs/control/retention/flag",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[RetentionGetResponse]]._unwrapper),
            cast_to=cast(Type[Optional[RetentionGetResponse]], ResultWrapper[RetentionGetResponse]),
        )

class RetentionResourceWithRawResponse:
    def __init__(self, retention: RetentionResource) -> None:
        self._retention = retention

        self.create = to_raw_response_wrapper(
            retention.create,
        )
        self.get = to_raw_response_wrapper(
            retention.get,
        )

class AsyncRetentionResourceWithRawResponse:
    def __init__(self, retention: AsyncRetentionResource) -> None:
        self._retention = retention

        self.create = async_to_raw_response_wrapper(
            retention.create,
        )
        self.get = async_to_raw_response_wrapper(
            retention.get,
        )

class RetentionResourceWithStreamingResponse:
    def __init__(self, retention: RetentionResource) -> None:
        self._retention = retention

        self.create = to_streamed_response_wrapper(
            retention.create,
        )
        self.get = to_streamed_response_wrapper(
            retention.get,
        )

class AsyncRetentionResourceWithStreamingResponse:
    def __init__(self, retention: AsyncRetentionResource) -> None:
        self._retention = retention

        self.create = async_to_streamed_response_wrapper(
            retention.create,
        )
        self.get = async_to_streamed_response_wrapper(
            retention.get,
        )