# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from ...types import (
    SpeedAPITestsGetResponse,
    SpeedAPIPagesListResponse,
    SpeedAPITestsListResponse,
    SpeedAPITrendsListResponse,
    SpeedAPIScheduleGetResponse,
    SpeedAPITestsCreateResponse,
    SpeedAPITestsDeleteResponse,
    SpeedAPIScheduleDeleteResponse,
    SpeedAPIAvailabilitiesListResponse,
    speed_api_tests_list_params,
    speed_api_trends_list_params,
    speed_api_schedule_get_params,
    speed_api_tests_create_params,
    speed_api_tests_delete_params,
    speed_api_schedule_delete_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from .schedule import (
    Schedule,
    AsyncSchedule,
    ScheduleWithRawResponse,
    AsyncScheduleWithRawResponse,
    ScheduleWithStreamingResponse,
    AsyncScheduleWithStreamingResponse,
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
from ..._base_client import (
    make_request_options,
)

__all__ = ["SpeedAPI", "AsyncSpeedAPI"]


class SpeedAPI(SyncAPIResource):
    @cached_property
    def schedule(self) -> Schedule:
        return Schedule(self._client)

    @cached_property
    def with_raw_response(self) -> SpeedAPIWithRawResponse:
        return SpeedAPIWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SpeedAPIWithStreamingResponse:
        return SpeedAPIWithStreamingResponse(self)

    def availabilities_list(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SpeedAPIAvailabilitiesListResponse]:
        """
        Retrieves quota for all plans, as well as the current zone quota.

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
            f"/zones/{zone_id}/speed_api/availabilities",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[SpeedAPIAvailabilitiesListResponse]], ResultWrapper[SpeedAPIAvailabilitiesListResponse]
            ),
        )

    def pages_list(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SpeedAPIPagesListResponse]:
        """
        Lists all webpages which have been tested.

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
            f"/zones/{zone_id}/speed_api/pages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[SpeedAPIPagesListResponse]], ResultWrapper[SpeedAPIPagesListResponse]),
        )

    def schedule_delete(
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
    ) -> Optional[SpeedAPIScheduleDeleteResponse]:
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
                query=maybe_transform(
                    {"region": region}, speed_api_schedule_delete_params.SpeedAPIScheduleDeleteParams
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[SpeedAPIScheduleDeleteResponse]], ResultWrapper[SpeedAPIScheduleDeleteResponse]),
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
    ) -> Optional[SpeedAPIScheduleGetResponse]:
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
                query=maybe_transform({"region": region}, speed_api_schedule_get_params.SpeedAPIScheduleGetParams),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[SpeedAPIScheduleGetResponse]], ResultWrapper[SpeedAPIScheduleGetResponse]),
        )

    def tests_create(
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
    ) -> Optional[SpeedAPITestsCreateResponse]:
        """
        Starts a test for a specific webpage, in a specific region.

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
            f"/zones/{zone_id}/speed_api/pages/{url}/tests",
            body=maybe_transform({"region": region}, speed_api_tests_create_params.SpeedAPITestsCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[SpeedAPITestsCreateResponse]], ResultWrapper[SpeedAPITestsCreateResponse]),
        )

    def tests_delete(
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
    ) -> Optional[SpeedAPITestsDeleteResponse]:
        """Deletes all tests for a specific webpage from a specific region.

        Deleted tests
        are still counted as part of the quota.

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
            f"/zones/{zone_id}/speed_api/pages/{url}/tests",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"region": region}, speed_api_tests_delete_params.SpeedAPITestsDeleteParams),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[SpeedAPITestsDeleteResponse]], ResultWrapper[SpeedAPITestsDeleteResponse]),
        )

    def tests_get(
        self,
        test_id: str,
        *,
        zone_id: str,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SpeedAPITestsGetResponse]:
        """
        Retrieves the result of a specific test.

        Args:
          zone_id: Identifier

          url: A URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not url:
            raise ValueError(f"Expected a non-empty value for `url` but received {url!r}")
        if not test_id:
            raise ValueError(f"Expected a non-empty value for `test_id` but received {test_id!r}")
        return self._get(
            f"/zones/{zone_id}/speed_api/pages/{url}/tests/{test_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[SpeedAPITestsGetResponse]], ResultWrapper[SpeedAPITestsGetResponse]),
        )

    def tests_list(
        self,
        url: str,
        *,
        zone_id: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
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
    ) -> SpeedAPITestsListResponse:
        """
        Test history (list of tests) for a specific webpage.

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
            f"/zones/{zone_id}/speed_api/pages/{url}/tests",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "region": region,
                    },
                    speed_api_tests_list_params.SpeedAPITestsListParams,
                ),
            ),
            cast_to=SpeedAPITestsListResponse,
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
        tz: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SpeedAPITrendsListResponse]:
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
                        "tz": tz,
                    },
                    speed_api_trends_list_params.SpeedAPITrendsListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[SpeedAPITrendsListResponse]], ResultWrapper[SpeedAPITrendsListResponse]),
        )


class AsyncSpeedAPI(AsyncAPIResource):
    @cached_property
    def schedule(self) -> AsyncSchedule:
        return AsyncSchedule(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSpeedAPIWithRawResponse:
        return AsyncSpeedAPIWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSpeedAPIWithStreamingResponse:
        return AsyncSpeedAPIWithStreamingResponse(self)

    async def availabilities_list(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SpeedAPIAvailabilitiesListResponse]:
        """
        Retrieves quota for all plans, as well as the current zone quota.

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
            f"/zones/{zone_id}/speed_api/availabilities",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[SpeedAPIAvailabilitiesListResponse]], ResultWrapper[SpeedAPIAvailabilitiesListResponse]
            ),
        )

    async def pages_list(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SpeedAPIPagesListResponse]:
        """
        Lists all webpages which have been tested.

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
            f"/zones/{zone_id}/speed_api/pages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[SpeedAPIPagesListResponse]], ResultWrapper[SpeedAPIPagesListResponse]),
        )

    async def schedule_delete(
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
    ) -> Optional[SpeedAPIScheduleDeleteResponse]:
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
                query=maybe_transform(
                    {"region": region}, speed_api_schedule_delete_params.SpeedAPIScheduleDeleteParams
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[SpeedAPIScheduleDeleteResponse]], ResultWrapper[SpeedAPIScheduleDeleteResponse]),
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
    ) -> Optional[SpeedAPIScheduleGetResponse]:
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
                query=maybe_transform({"region": region}, speed_api_schedule_get_params.SpeedAPIScheduleGetParams),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[SpeedAPIScheduleGetResponse]], ResultWrapper[SpeedAPIScheduleGetResponse]),
        )

    async def tests_create(
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
    ) -> Optional[SpeedAPITestsCreateResponse]:
        """
        Starts a test for a specific webpage, in a specific region.

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
            f"/zones/{zone_id}/speed_api/pages/{url}/tests",
            body=maybe_transform({"region": region}, speed_api_tests_create_params.SpeedAPITestsCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[SpeedAPITestsCreateResponse]], ResultWrapper[SpeedAPITestsCreateResponse]),
        )

    async def tests_delete(
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
    ) -> Optional[SpeedAPITestsDeleteResponse]:
        """Deletes all tests for a specific webpage from a specific region.

        Deleted tests
        are still counted as part of the quota.

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
            f"/zones/{zone_id}/speed_api/pages/{url}/tests",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"region": region}, speed_api_tests_delete_params.SpeedAPITestsDeleteParams),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[SpeedAPITestsDeleteResponse]], ResultWrapper[SpeedAPITestsDeleteResponse]),
        )

    async def tests_get(
        self,
        test_id: str,
        *,
        zone_id: str,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SpeedAPITestsGetResponse]:
        """
        Retrieves the result of a specific test.

        Args:
          zone_id: Identifier

          url: A URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not url:
            raise ValueError(f"Expected a non-empty value for `url` but received {url!r}")
        if not test_id:
            raise ValueError(f"Expected a non-empty value for `test_id` but received {test_id!r}")
        return await self._get(
            f"/zones/{zone_id}/speed_api/pages/{url}/tests/{test_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[SpeedAPITestsGetResponse]], ResultWrapper[SpeedAPITestsGetResponse]),
        )

    async def tests_list(
        self,
        url: str,
        *,
        zone_id: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
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
    ) -> SpeedAPITestsListResponse:
        """
        Test history (list of tests) for a specific webpage.

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
            f"/zones/{zone_id}/speed_api/pages/{url}/tests",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "region": region,
                    },
                    speed_api_tests_list_params.SpeedAPITestsListParams,
                ),
            ),
            cast_to=SpeedAPITestsListResponse,
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
        tz: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SpeedAPITrendsListResponse]:
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
                query=maybe_transform(
                    {
                        "device_type": device_type,
                        "metrics": metrics,
                        "region": region,
                        "tz": tz,
                    },
                    speed_api_trends_list_params.SpeedAPITrendsListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[SpeedAPITrendsListResponse]], ResultWrapper[SpeedAPITrendsListResponse]),
        )


class SpeedAPIWithRawResponse:
    def __init__(self, speed_api: SpeedAPI) -> None:
        self._speed_api = speed_api

        self.availabilities_list = to_raw_response_wrapper(
            speed_api.availabilities_list,
        )
        self.pages_list = to_raw_response_wrapper(
            speed_api.pages_list,
        )
        self.schedule_delete = to_raw_response_wrapper(
            speed_api.schedule_delete,
        )
        self.schedule_get = to_raw_response_wrapper(
            speed_api.schedule_get,
        )
        self.tests_create = to_raw_response_wrapper(
            speed_api.tests_create,
        )
        self.tests_delete = to_raw_response_wrapper(
            speed_api.tests_delete,
        )
        self.tests_get = to_raw_response_wrapper(
            speed_api.tests_get,
        )
        self.tests_list = to_raw_response_wrapper(
            speed_api.tests_list,
        )
        self.trends_list = to_raw_response_wrapper(
            speed_api.trends_list,
        )

    @cached_property
    def schedule(self) -> ScheduleWithRawResponse:
        return ScheduleWithRawResponse(self._speed_api.schedule)


class AsyncSpeedAPIWithRawResponse:
    def __init__(self, speed_api: AsyncSpeedAPI) -> None:
        self._speed_api = speed_api

        self.availabilities_list = async_to_raw_response_wrapper(
            speed_api.availabilities_list,
        )
        self.pages_list = async_to_raw_response_wrapper(
            speed_api.pages_list,
        )
        self.schedule_delete = async_to_raw_response_wrapper(
            speed_api.schedule_delete,
        )
        self.schedule_get = async_to_raw_response_wrapper(
            speed_api.schedule_get,
        )
        self.tests_create = async_to_raw_response_wrapper(
            speed_api.tests_create,
        )
        self.tests_delete = async_to_raw_response_wrapper(
            speed_api.tests_delete,
        )
        self.tests_get = async_to_raw_response_wrapper(
            speed_api.tests_get,
        )
        self.tests_list = async_to_raw_response_wrapper(
            speed_api.tests_list,
        )
        self.trends_list = async_to_raw_response_wrapper(
            speed_api.trends_list,
        )

    @cached_property
    def schedule(self) -> AsyncScheduleWithRawResponse:
        return AsyncScheduleWithRawResponse(self._speed_api.schedule)


class SpeedAPIWithStreamingResponse:
    def __init__(self, speed_api: SpeedAPI) -> None:
        self._speed_api = speed_api

        self.availabilities_list = to_streamed_response_wrapper(
            speed_api.availabilities_list,
        )
        self.pages_list = to_streamed_response_wrapper(
            speed_api.pages_list,
        )
        self.schedule_delete = to_streamed_response_wrapper(
            speed_api.schedule_delete,
        )
        self.schedule_get = to_streamed_response_wrapper(
            speed_api.schedule_get,
        )
        self.tests_create = to_streamed_response_wrapper(
            speed_api.tests_create,
        )
        self.tests_delete = to_streamed_response_wrapper(
            speed_api.tests_delete,
        )
        self.tests_get = to_streamed_response_wrapper(
            speed_api.tests_get,
        )
        self.tests_list = to_streamed_response_wrapper(
            speed_api.tests_list,
        )
        self.trends_list = to_streamed_response_wrapper(
            speed_api.trends_list,
        )

    @cached_property
    def schedule(self) -> ScheduleWithStreamingResponse:
        return ScheduleWithStreamingResponse(self._speed_api.schedule)


class AsyncSpeedAPIWithStreamingResponse:
    def __init__(self, speed_api: AsyncSpeedAPI) -> None:
        self._speed_api = speed_api

        self.availabilities_list = async_to_streamed_response_wrapper(
            speed_api.availabilities_list,
        )
        self.pages_list = async_to_streamed_response_wrapper(
            speed_api.pages_list,
        )
        self.schedule_delete = async_to_streamed_response_wrapper(
            speed_api.schedule_delete,
        )
        self.schedule_get = async_to_streamed_response_wrapper(
            speed_api.schedule_get,
        )
        self.tests_create = async_to_streamed_response_wrapper(
            speed_api.tests_create,
        )
        self.tests_delete = async_to_streamed_response_wrapper(
            speed_api.tests_delete,
        )
        self.tests_get = async_to_streamed_response_wrapper(
            speed_api.tests_get,
        )
        self.tests_list = async_to_streamed_response_wrapper(
            speed_api.tests_list,
        )
        self.trends_list = async_to_streamed_response_wrapper(
            speed_api.trends_list,
        )

    @cached_property
    def schedule(self) -> AsyncScheduleWithStreamingResponse:
        return AsyncScheduleWithStreamingResponse(self._speed_api.schedule)
