# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, cast
from datetime import date, datetime
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import make_request_options
from ....types.radar.ranking import (
    internet_service_top_params,
    internet_service_categories_params,
    internet_service_timeseries_groups_params,
)
from ....types.radar.ranking.internet_service_top_response import InternetServiceTopResponse
from ....types.radar.ranking.internet_service_categories_response import InternetServiceCategoriesResponse
from ....types.radar.ranking.internet_service_timeseries_groups_response import InternetServiceTimeseriesGroupsResponse

__all__ = ["InternetServicesResource", "AsyncInternetServicesResource"]


class InternetServicesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InternetServicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return InternetServicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InternetServicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return InternetServicesResourceWithStreamingResponse(self)

    def categories(
        self,
        *,
        date: List[Union[str, date]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InternetServiceCategoriesResponse:
        """
        Retrieves the list of Internet services categories.

        Args:
          date: Array of dates to filter the results.

          format: Format in which results will be returned.

          limit: Limits the number of objects returned in the response.

          name: Array of names used to label the series in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/ranking/internet_services/categories",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "format": format,
                        "limit": limit,
                        "name": name,
                    },
                    internet_service_categories_params.InternetServiceCategoriesParams,
                ),
                post_parser=ResultWrapper[InternetServiceCategoriesResponse]._unwrapper,
            ),
            cast_to=cast(Type[InternetServiceCategoriesResponse], ResultWrapper[InternetServiceCategoriesResponse]),
        )

    def timeseries_groups(
        self,
        *,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        service_category: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InternetServiceTimeseriesGroupsResponse:
        """
        Retrieves Internet Services rank update changes over time.

        Args:
          date_end: End of the date range (inclusive).

          date_range: Filters results by the specified date range. For example, use `7d` and
              `7dcontrol` to compare this week with the previous week. Use this parameter or
              set specific start and end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          limit: Limits the number of objects returned in the response.

          name: Array of names used to label the series in the response.

          service_category: Filters results by Internet service category.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/ranking/internet_services/timeseries_groups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "limit": limit,
                        "name": name,
                        "service_category": service_category,
                    },
                    internet_service_timeseries_groups_params.InternetServiceTimeseriesGroupsParams,
                ),
                post_parser=ResultWrapper[InternetServiceTimeseriesGroupsResponse]._unwrapper,
            ),
            cast_to=cast(
                Type[InternetServiceTimeseriesGroupsResponse], ResultWrapper[InternetServiceTimeseriesGroupsResponse]
            ),
        )

    def top(
        self,
        *,
        date: List[Union[str, date]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        service_category: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InternetServiceTopResponse:
        """
        Retrieves top Internet services based on their rank.

        Args:
          date: Array of dates to filter the results.

          format: Format in which results will be returned.

          limit: Limits the number of objects returned in the response.

          name: Array of names used to label the series in the response.

          service_category: Filters results by Internet service category.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/ranking/internet_services/top",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "format": format,
                        "limit": limit,
                        "name": name,
                        "service_category": service_category,
                    },
                    internet_service_top_params.InternetServiceTopParams,
                ),
                post_parser=ResultWrapper[InternetServiceTopResponse]._unwrapper,
            ),
            cast_to=cast(Type[InternetServiceTopResponse], ResultWrapper[InternetServiceTopResponse]),
        )


class AsyncInternetServicesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInternetServicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInternetServicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInternetServicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncInternetServicesResourceWithStreamingResponse(self)

    async def categories(
        self,
        *,
        date: List[Union[str, date]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InternetServiceCategoriesResponse:
        """
        Retrieves the list of Internet services categories.

        Args:
          date: Array of dates to filter the results.

          format: Format in which results will be returned.

          limit: Limits the number of objects returned in the response.

          name: Array of names used to label the series in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/ranking/internet_services/categories",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "format": format,
                        "limit": limit,
                        "name": name,
                    },
                    internet_service_categories_params.InternetServiceCategoriesParams,
                ),
                post_parser=ResultWrapper[InternetServiceCategoriesResponse]._unwrapper,
            ),
            cast_to=cast(Type[InternetServiceCategoriesResponse], ResultWrapper[InternetServiceCategoriesResponse]),
        )

    async def timeseries_groups(
        self,
        *,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        service_category: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InternetServiceTimeseriesGroupsResponse:
        """
        Retrieves Internet Services rank update changes over time.

        Args:
          date_end: End of the date range (inclusive).

          date_range: Filters results by the specified date range. For example, use `7d` and
              `7dcontrol` to compare this week with the previous week. Use this parameter or
              set specific start and end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          limit: Limits the number of objects returned in the response.

          name: Array of names used to label the series in the response.

          service_category: Filters results by Internet service category.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/ranking/internet_services/timeseries_groups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "limit": limit,
                        "name": name,
                        "service_category": service_category,
                    },
                    internet_service_timeseries_groups_params.InternetServiceTimeseriesGroupsParams,
                ),
                post_parser=ResultWrapper[InternetServiceTimeseriesGroupsResponse]._unwrapper,
            ),
            cast_to=cast(
                Type[InternetServiceTimeseriesGroupsResponse], ResultWrapper[InternetServiceTimeseriesGroupsResponse]
            ),
        )

    async def top(
        self,
        *,
        date: List[Union[str, date]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        service_category: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InternetServiceTopResponse:
        """
        Retrieves top Internet services based on their rank.

        Args:
          date: Array of dates to filter the results.

          format: Format in which results will be returned.

          limit: Limits the number of objects returned in the response.

          name: Array of names used to label the series in the response.

          service_category: Filters results by Internet service category.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/ranking/internet_services/top",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "format": format,
                        "limit": limit,
                        "name": name,
                        "service_category": service_category,
                    },
                    internet_service_top_params.InternetServiceTopParams,
                ),
                post_parser=ResultWrapper[InternetServiceTopResponse]._unwrapper,
            ),
            cast_to=cast(Type[InternetServiceTopResponse], ResultWrapper[InternetServiceTopResponse]),
        )


class InternetServicesResourceWithRawResponse:
    def __init__(self, internet_services: InternetServicesResource) -> None:
        self._internet_services = internet_services

        self.categories = to_raw_response_wrapper(
            internet_services.categories,
        )
        self.timeseries_groups = to_raw_response_wrapper(
            internet_services.timeseries_groups,
        )
        self.top = to_raw_response_wrapper(
            internet_services.top,
        )


class AsyncInternetServicesResourceWithRawResponse:
    def __init__(self, internet_services: AsyncInternetServicesResource) -> None:
        self._internet_services = internet_services

        self.categories = async_to_raw_response_wrapper(
            internet_services.categories,
        )
        self.timeseries_groups = async_to_raw_response_wrapper(
            internet_services.timeseries_groups,
        )
        self.top = async_to_raw_response_wrapper(
            internet_services.top,
        )


class InternetServicesResourceWithStreamingResponse:
    def __init__(self, internet_services: InternetServicesResource) -> None:
        self._internet_services = internet_services

        self.categories = to_streamed_response_wrapper(
            internet_services.categories,
        )
        self.timeseries_groups = to_streamed_response_wrapper(
            internet_services.timeseries_groups,
        )
        self.top = to_streamed_response_wrapper(
            internet_services.top,
        )


class AsyncInternetServicesResourceWithStreamingResponse:
    def __init__(self, internet_services: AsyncInternetServicesResource) -> None:
        self._internet_services = internet_services

        self.categories = async_to_streamed_response_wrapper(
            internet_services.categories,
        )
        self.timeseries_groups = async_to_streamed_response_wrapper(
            internet_services.timeseries_groups,
        )
        self.top = async_to_streamed_response_wrapper(
            internet_services.top,
        )
