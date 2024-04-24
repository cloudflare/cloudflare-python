# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, Optional, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from .pages import (
    PagesResource,
    AsyncPagesResource,
    PagesResourceWithRawResponse,
    AsyncPagesResourceWithRawResponse,
    PagesResourceWithStreamingResponse,
    AsyncPagesResourceWithStreamingResponse,
)
from .tests import (
    TestsResource,
    AsyncTestsResource,
    TestsResourceWithRawResponse,
    AsyncTestsResourceWithRawResponse,
    TestsResourceWithStreamingResponse,
    AsyncTestsResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .schedule import (
    ScheduleResource,
    AsyncScheduleResource,
    ScheduleResourceWithRawResponse,
    AsyncScheduleResourceWithRawResponse,
    ScheduleResourceWithStreamingResponse,
    AsyncScheduleResourceWithStreamingResponse,
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
from ...types.speed import speed_delete_params, speed_trends_list_params, speed_schedule_get_params
from ..._base_client import (
    make_request_options,
)
from .availabilities import (
    AvailabilitiesResource,
    AsyncAvailabilitiesResource,
    AvailabilitiesResourceWithRawResponse,
    AsyncAvailabilitiesResourceWithRawResponse,
    AvailabilitiesResourceWithStreamingResponse,
    AsyncAvailabilitiesResourceWithStreamingResponse,
)
from ...types.speed.trend import Trend
from ...types.speed.schedule import Schedule
from ...types.speed.speed_delete_response import SpeedDeleteResponse

__all__ = ["SpeedResource", "AsyncSpeedResource"]


class SpeedResource(SyncAPIResource):
    @cached_property
    def tests(self) -> TestsResource:
        return TestsResource(self._client)

    @cached_property
    def schedule(self) -> ScheduleResource:
        return ScheduleResource(self._client)

    @cached_property
    def availabilities(self) -> AvailabilitiesResource:
        return AvailabilitiesResource(self._client)

    @cached_property
    def pages(self) -> PagesResource:
        return PagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> SpeedResourceWithRawResponse:
        return SpeedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SpeedResourceWithStreamingResponse:
        return SpeedResourceWithStreamingResponse(self)

    def delete(
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
    ) -> Optional[SpeedDeleteResponse]:
        """
        Deletes a scheduled test for a page.

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
        return self._delete(
            f"/zones/{zone_id}/speed_api/schedule/{url}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"region": region}, speed_delete_params.SpeedDeleteParams),
                post_parser=ResultWrapper[Optional[SpeedDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SpeedDeleteResponse]], ResultWrapper[SpeedDeleteResponse]),
        )

    def schedule_get(
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
    ) -> Optional[Schedule]:
        """
        Retrieves the test schedule for a page in a specific region.

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
        return self._get(
            f"/zones/{zone_id}/speed_api/schedule/{url}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"region": region}, speed_schedule_get_params.SpeedScheduleGetParams),
                post_parser=ResultWrapper[Optional[Schedule]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Schedule]], ResultWrapper[Schedule]),
        )

    def trends_list(
        self,
        url: str,
        *,
        zone_id: str,
        device_type: Literal["DESKTOP", "MOBILE"],
        metrics: str,
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
        ],
        start: Union[str, datetime],
        tz: str,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Trend]:
        """
        Lists the core web vital metrics trend over time for a specific page.

        Args:
          zone_id: Identifier

          url: A URL.

          device_type: The type of device.

          metrics: A comma-separated list of metrics to include in the results.

          region: A test region.

          tz: The timezone of the start and end timestamps.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not url:
            raise ValueError(f"Expected a non-empty value for `url` but received {url!r}")
        return self._get(
            f"/zones/{zone_id}/speed_api/pages/{url}/trend",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "device_type": device_type,
                        "metrics": metrics,
                        "region": region,
                        "start": start,
                        "tz": tz,
                        "end": end,
                    },
                    speed_trends_list_params.SpeedTrendsListParams,
                ),
                post_parser=ResultWrapper[Optional[Trend]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Trend]], ResultWrapper[Trend]),
        )


class AsyncSpeedResource(AsyncAPIResource):
    @cached_property
    def tests(self) -> AsyncTestsResource:
        return AsyncTestsResource(self._client)

    @cached_property
    def schedule(self) -> AsyncScheduleResource:
        return AsyncScheduleResource(self._client)

    @cached_property
    def availabilities(self) -> AsyncAvailabilitiesResource:
        return AsyncAvailabilitiesResource(self._client)

    @cached_property
    def pages(self) -> AsyncPagesResource:
        return AsyncPagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSpeedResourceWithRawResponse:
        return AsyncSpeedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSpeedResourceWithStreamingResponse:
        return AsyncSpeedResourceWithStreamingResponse(self)

    async def delete(
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
    ) -> Optional[SpeedDeleteResponse]:
        """
        Deletes a scheduled test for a page.

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
        return await self._delete(
            f"/zones/{zone_id}/speed_api/schedule/{url}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"region": region}, speed_delete_params.SpeedDeleteParams),
                post_parser=ResultWrapper[Optional[SpeedDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SpeedDeleteResponse]], ResultWrapper[SpeedDeleteResponse]),
        )

    async def schedule_get(
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
    ) -> Optional[Schedule]:
        """
        Retrieves the test schedule for a page in a specific region.

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
        return await self._get(
            f"/zones/{zone_id}/speed_api/schedule/{url}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"region": region}, speed_schedule_get_params.SpeedScheduleGetParams),
                post_parser=ResultWrapper[Optional[Schedule]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Schedule]], ResultWrapper[Schedule]),
        )

    async def trends_list(
        self,
        url: str,
        *,
        zone_id: str,
        device_type: Literal["DESKTOP", "MOBILE"],
        metrics: str,
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
        ],
        start: Union[str, datetime],
        tz: str,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Trend]:
        """
        Lists the core web vital metrics trend over time for a specific page.

        Args:
          zone_id: Identifier

          url: A URL.

          device_type: The type of device.

          metrics: A comma-separated list of metrics to include in the results.

          region: A test region.

          tz: The timezone of the start and end timestamps.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not url:
            raise ValueError(f"Expected a non-empty value for `url` but received {url!r}")
        return await self._get(
            f"/zones/{zone_id}/speed_api/pages/{url}/trend",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "device_type": device_type,
                        "metrics": metrics,
                        "region": region,
                        "start": start,
                        "tz": tz,
                        "end": end,
                    },
                    speed_trends_list_params.SpeedTrendsListParams,
                ),
                post_parser=ResultWrapper[Optional[Trend]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Trend]], ResultWrapper[Trend]),
        )


class SpeedResourceWithRawResponse:
    def __init__(self, speed: SpeedResource) -> None:
        self._speed = speed

        self.delete = to_raw_response_wrapper(
            speed.delete,
        )
        self.schedule_get = to_raw_response_wrapper(
            speed.schedule_get,
        )
        self.trends_list = to_raw_response_wrapper(
            speed.trends_list,
        )

    @cached_property
    def tests(self) -> TestsResourceWithRawResponse:
        return TestsResourceWithRawResponse(self._speed.tests)

    @cached_property
    def schedule(self) -> ScheduleResourceWithRawResponse:
        return ScheduleResourceWithRawResponse(self._speed.schedule)

    @cached_property
    def availabilities(self) -> AvailabilitiesResourceWithRawResponse:
        return AvailabilitiesResourceWithRawResponse(self._speed.availabilities)

    @cached_property
    def pages(self) -> PagesResourceWithRawResponse:
        return PagesResourceWithRawResponse(self._speed.pages)


class AsyncSpeedResourceWithRawResponse:
    def __init__(self, speed: AsyncSpeedResource) -> None:
        self._speed = speed

        self.delete = async_to_raw_response_wrapper(
            speed.delete,
        )
        self.schedule_get = async_to_raw_response_wrapper(
            speed.schedule_get,
        )
        self.trends_list = async_to_raw_response_wrapper(
            speed.trends_list,
        )

    @cached_property
    def tests(self) -> AsyncTestsResourceWithRawResponse:
        return AsyncTestsResourceWithRawResponse(self._speed.tests)

    @cached_property
    def schedule(self) -> AsyncScheduleResourceWithRawResponse:
        return AsyncScheduleResourceWithRawResponse(self._speed.schedule)

    @cached_property
    def availabilities(self) -> AsyncAvailabilitiesResourceWithRawResponse:
        return AsyncAvailabilitiesResourceWithRawResponse(self._speed.availabilities)

    @cached_property
    def pages(self) -> AsyncPagesResourceWithRawResponse:
        return AsyncPagesResourceWithRawResponse(self._speed.pages)


class SpeedResourceWithStreamingResponse:
    def __init__(self, speed: SpeedResource) -> None:
        self._speed = speed

        self.delete = to_streamed_response_wrapper(
            speed.delete,
        )
        self.schedule_get = to_streamed_response_wrapper(
            speed.schedule_get,
        )
        self.trends_list = to_streamed_response_wrapper(
            speed.trends_list,
        )

    @cached_property
    def tests(self) -> TestsResourceWithStreamingResponse:
        return TestsResourceWithStreamingResponse(self._speed.tests)

    @cached_property
    def schedule(self) -> ScheduleResourceWithStreamingResponse:
        return ScheduleResourceWithStreamingResponse(self._speed.schedule)

    @cached_property
    def availabilities(self) -> AvailabilitiesResourceWithStreamingResponse:
        return AvailabilitiesResourceWithStreamingResponse(self._speed.availabilities)

    @cached_property
    def pages(self) -> PagesResourceWithStreamingResponse:
        return PagesResourceWithStreamingResponse(self._speed.pages)


class AsyncSpeedResourceWithStreamingResponse:
    def __init__(self, speed: AsyncSpeedResource) -> None:
        self._speed = speed

        self.delete = async_to_streamed_response_wrapper(
            speed.delete,
        )
        self.schedule_get = async_to_streamed_response_wrapper(
            speed.schedule_get,
        )
        self.trends_list = async_to_streamed_response_wrapper(
            speed.trends_list,
        )

    @cached_property
    def tests(self) -> AsyncTestsResourceWithStreamingResponse:
        return AsyncTestsResourceWithStreamingResponse(self._speed.tests)

    @cached_property
    def schedule(self) -> AsyncScheduleResourceWithStreamingResponse:
        return AsyncScheduleResourceWithStreamingResponse(self._speed.schedule)

    @cached_property
    def availabilities(self) -> AsyncAvailabilitiesResourceWithStreamingResponse:
        return AsyncAvailabilitiesResourceWithStreamingResponse(self._speed.availabilities)

    @cached_property
    def pages(self) -> AsyncPagesResourceWithStreamingResponse:
        return AsyncPagesResourceWithStreamingResponse(self._speed.pages)
