# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...types.speed import ScheduleCreateResponse, schedule_create_params
from ..._base_client import (
    make_request_options,
)

__all__ = ["Schedule", "AsyncSchedule"]


class Schedule(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScheduleWithRawResponse:
        return ScheduleWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScheduleWithStreamingResponse:
        return ScheduleWithStreamingResponse(self)

    def create(
        self,
        url: str,
        *,
        zone_id: str,
        region: Literal[
            "asia-east1",
            "asia-northeast1",
            "asia-northeast2",
            "asia-south1",
            "asia-southeast1",
            "australia-southeast1",
            "europe-north1",
            "europe-southwest1",
            "europe-west1",
            "europe-west2",
            "europe-west3",
            "europe-west4",
            "europe-west8",
            "europe-west9",
            "me-west1",
            "southamerica-east1",
            "us-central1",
            "us-east1",
            "us-east4",
            "us-south1",
            "us-west1",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ScheduleCreateResponse]:
        """
        Creates a scheduled test for a page.

        Args:
          zone_id: Identifier

          url: A URL.

          region: A test region.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not url:
            raise ValueError(f"Expected a non-empty value for `url` but received {url!r}")
        return self._post(
            f"/zones/{zone_id}/speed_api/schedule/{url}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"region": region}, schedule_create_params.ScheduleCreateParams),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ScheduleCreateResponse]], ResultWrapper[ScheduleCreateResponse]),
        )


class AsyncSchedule(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScheduleWithRawResponse:
        return AsyncScheduleWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScheduleWithStreamingResponse:
        return AsyncScheduleWithStreamingResponse(self)

    async def create(
        self,
        url: str,
        *,
        zone_id: str,
        region: Literal[
            "asia-east1",
            "asia-northeast1",
            "asia-northeast2",
            "asia-south1",
            "asia-southeast1",
            "australia-southeast1",
            "europe-north1",
            "europe-southwest1",
            "europe-west1",
            "europe-west2",
            "europe-west3",
            "europe-west4",
            "europe-west8",
            "europe-west9",
            "me-west1",
            "southamerica-east1",
            "us-central1",
            "us-east1",
            "us-east4",
            "us-south1",
            "us-west1",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ScheduleCreateResponse]:
        """
        Creates a scheduled test for a page.

        Args:
          zone_id: Identifier

          url: A URL.

          region: A test region.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not url:
            raise ValueError(f"Expected a non-empty value for `url` but received {url!r}")
        return await self._post(
            f"/zones/{zone_id}/speed_api/schedule/{url}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"region": region}, schedule_create_params.ScheduleCreateParams),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ScheduleCreateResponse]], ResultWrapper[ScheduleCreateResponse]),
        )


class ScheduleWithRawResponse:
    def __init__(self, schedule: Schedule) -> None:
        self._schedule = schedule

        self.create = to_raw_response_wrapper(
            schedule.create,
        )


class AsyncScheduleWithRawResponse:
    def __init__(self, schedule: AsyncSchedule) -> None:
        self._schedule = schedule

        self.create = async_to_raw_response_wrapper(
            schedule.create,
        )


class ScheduleWithStreamingResponse:
    def __init__(self, schedule: Schedule) -> None:
        self._schedule = schedule

        self.create = to_streamed_response_wrapper(
            schedule.create,
        )


class AsyncScheduleWithStreamingResponse:
    def __init__(self, schedule: AsyncSchedule) -> None:
        self._schedule = schedule

        self.create = async_to_streamed_response_wrapper(
            schedule.create,
        )
