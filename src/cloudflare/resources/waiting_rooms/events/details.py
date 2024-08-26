# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.waiting_rooms.events.detail_get_response import DetailGetResponse

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

__all__ = ["DetailsResource", "AsyncDetailsResource"]

class DetailsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DetailsResourceWithRawResponse:
        return DetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DetailsResourceWithStreamingResponse:
        return DetailsResourceWithStreamingResponse(self)

    def get(self,
    event_id: str,
    *,
    zone_id: str,
    waiting_room_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> DetailGetResponse:
        """Previews an event's configuration as if it was active.

        Inherited fields from the
        waiting room will be displayed with their current values.

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
        if not waiting_room_id:
          raise ValueError(
            f'Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}'
          )
        if not event_id:
          raise ValueError(
            f'Expected a non-empty value for `event_id` but received {event_id!r}'
          )
        return self._get(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}/events/{event_id}/details",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[DetailGetResponse]._unwrapper),
            cast_to=cast(Type[DetailGetResponse], ResultWrapper[DetailGetResponse]),
        )

class AsyncDetailsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDetailsResourceWithRawResponse:
        return AsyncDetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDetailsResourceWithStreamingResponse:
        return AsyncDetailsResourceWithStreamingResponse(self)

    async def get(self,
    event_id: str,
    *,
    zone_id: str,
    waiting_room_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> DetailGetResponse:
        """Previews an event's configuration as if it was active.

        Inherited fields from the
        waiting room will be displayed with their current values.

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
        if not waiting_room_id:
          raise ValueError(
            f'Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}'
          )
        if not event_id:
          raise ValueError(
            f'Expected a non-empty value for `event_id` but received {event_id!r}'
          )
        return await self._get(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}/events/{event_id}/details",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[DetailGetResponse]._unwrapper),
            cast_to=cast(Type[DetailGetResponse], ResultWrapper[DetailGetResponse]),
        )

class DetailsResourceWithRawResponse:
    def __init__(self, details: DetailsResource) -> None:
        self._details = details

        self.get = to_raw_response_wrapper(
            details.get,
        )

class AsyncDetailsResourceWithRawResponse:
    def __init__(self, details: AsyncDetailsResource) -> None:
        self._details = details

        self.get = async_to_raw_response_wrapper(
            details.get,
        )

class DetailsResourceWithStreamingResponse:
    def __init__(self, details: DetailsResource) -> None:
        self._details = details

        self.get = to_streamed_response_wrapper(
            details.get,
        )

class AsyncDetailsResourceWithStreamingResponse:
    def __init__(self, details: AsyncDetailsResource) -> None:
        self._details = details

        self.get = async_to_streamed_response_wrapper(
            details.get,
        )