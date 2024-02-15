# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.dcv_delegation import UuidGetResponse

from typing import Type

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
from typing import cast
from typing import cast

__all__ = ["Uuid", "AsyncUuid"]


class Uuid(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UuidWithRawResponse:
        return UuidWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UuidWithStreamingResponse:
        return UuidWithStreamingResponse(self)

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
    ) -> UuidGetResponse:
        """
        Retrieve the account and zone specific unique identifier used as part of the
        CNAME target for DCV Delegation.

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
            f"/zones/{zone_id}/dcv_delegation/uuid",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[UuidGetResponse], ResultWrapper[UuidGetResponse]),
        )


class AsyncUuid(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUuidWithRawResponse:
        return AsyncUuidWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUuidWithStreamingResponse:
        return AsyncUuidWithStreamingResponse(self)

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
    ) -> UuidGetResponse:
        """
        Retrieve the account and zone specific unique identifier used as part of the
        CNAME target for DCV Delegation.

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
            f"/zones/{zone_id}/dcv_delegation/uuid",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[UuidGetResponse], ResultWrapper[UuidGetResponse]),
        )


class UuidWithRawResponse:
    def __init__(self, uuid: Uuid) -> None:
        self._uuid = uuid

        self.get = to_raw_response_wrapper(
            uuid.get,
        )


class AsyncUuidWithRawResponse:
    def __init__(self, uuid: AsyncUuid) -> None:
        self._uuid = uuid

        self.get = async_to_raw_response_wrapper(
            uuid.get,
        )


class UuidWithStreamingResponse:
    def __init__(self, uuid: Uuid) -> None:
        self._uuid = uuid

        self.get = to_streamed_response_wrapper(
            uuid.get,
        )


class AsyncUuidWithStreamingResponse:
    def __init__(self, uuid: AsyncUuid) -> None:
        self._uuid = uuid

        self.get = async_to_streamed_response_wrapper(
            uuid.get,
        )
