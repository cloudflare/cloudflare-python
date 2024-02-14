# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.waiting_rooms.events import DetailWaitingRoomPreviewActiveEventDetailsResponse

from typing import Type

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
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["Details", "AsyncDetails"]


class Details(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DetailsWithRawResponse:
        return DetailsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DetailsWithStreamingResponse:
        return DetailsWithStreamingResponse(self)

    def waiting_room_preview_active_event_details(
        self,
        event_id: object,
        *,
        zone_identifier: str,
        waiting_room_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetailWaitingRoomPreviewActiveEventDetailsResponse:
        """Previews an event's configuration as if it was active.

        Inherited fields from the
        waiting room will be displayed with their current values.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._get(
            f"/zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/events/{event_id}/details",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[DetailWaitingRoomPreviewActiveEventDetailsResponse],
                ResultWrapper[DetailWaitingRoomPreviewActiveEventDetailsResponse],
            ),
        )


class AsyncDetails(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDetailsWithRawResponse:
        return AsyncDetailsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDetailsWithStreamingResponse:
        return AsyncDetailsWithStreamingResponse(self)

    async def waiting_room_preview_active_event_details(
        self,
        event_id: object,
        *,
        zone_identifier: str,
        waiting_room_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetailWaitingRoomPreviewActiveEventDetailsResponse:
        """Previews an event's configuration as if it was active.

        Inherited fields from the
        waiting room will be displayed with their current values.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._get(
            f"/zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/events/{event_id}/details",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[DetailWaitingRoomPreviewActiveEventDetailsResponse],
                ResultWrapper[DetailWaitingRoomPreviewActiveEventDetailsResponse],
            ),
        )


class DetailsWithRawResponse:
    def __init__(self, details: Details) -> None:
        self._details = details

        self.waiting_room_preview_active_event_details = to_raw_response_wrapper(
            details.waiting_room_preview_active_event_details,
        )


class AsyncDetailsWithRawResponse:
    def __init__(self, details: AsyncDetails) -> None:
        self._details = details

        self.waiting_room_preview_active_event_details = async_to_raw_response_wrapper(
            details.waiting_room_preview_active_event_details,
        )


class DetailsWithStreamingResponse:
    def __init__(self, details: Details) -> None:
        self._details = details

        self.waiting_room_preview_active_event_details = to_streamed_response_wrapper(
            details.waiting_room_preview_active_event_details,
        )


class AsyncDetailsWithStreamingResponse:
    def __init__(self, details: AsyncDetails) -> None:
        self._details = details

        self.waiting_room_preview_active_event_details = async_to_streamed_response_wrapper(
            details.waiting_room_preview_active_event_details,
        )
