# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, Optional, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from .tests import (
    TestsResource,
    AsyncTestsResource,
    TestsResourceWithRawResponse,
    AsyncTestsResourceWithRawResponse,
    TestsResourceWithStreamingResponse,
    AsyncTestsResourceWithStreamingResponse,
)
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
from ....pagination import SyncSinglePage, AsyncSinglePage
from ....types.speed import page_trend_params
from ...._base_client import AsyncPaginator, make_request_options
from ....types.speed.trend import Trend
from ....types.speed.page_list_response import PageListResponse

__all__ = ["PagesResource", "AsyncPagesResource"]


class PagesResource(SyncAPIResource):
    @cached_property
    def tests(self) -> TestsResource:
        return TestsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PagesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[PageListResponse]:
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
        return self._get_api_list(
            f"/zones/{zone_id}/speed_api/pages",
            page=SyncSinglePage[PageListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=PageListResponse,
        )

    def trend(
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
                    page_trend_params.PageTrendParams,
                ),
                post_parser=ResultWrapper[Optional[Trend]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Trend]], ResultWrapper[Trend]),
        )


class AsyncPagesResource(AsyncAPIResource):
    @cached_property
    def tests(self) -> AsyncTestsResource:
        return AsyncTestsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPagesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[PageListResponse, AsyncSinglePage[PageListResponse]]:
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
        return self._get_api_list(
            f"/zones/{zone_id}/speed_api/pages",
            page=AsyncSinglePage[PageListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=PageListResponse,
        )

    async def trend(
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
                    page_trend_params.PageTrendParams,
                ),
                post_parser=ResultWrapper[Optional[Trend]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Trend]], ResultWrapper[Trend]),
        )


class PagesResourceWithRawResponse:
    def __init__(self, pages: PagesResource) -> None:
        self._pages = pages

        self.list = to_raw_response_wrapper(
            pages.list,
        )
        self.trend = to_raw_response_wrapper(
            pages.trend,
        )

    @cached_property
    def tests(self) -> TestsResourceWithRawResponse:
        return TestsResourceWithRawResponse(self._pages.tests)


class AsyncPagesResourceWithRawResponse:
    def __init__(self, pages: AsyncPagesResource) -> None:
        self._pages = pages

        self.list = async_to_raw_response_wrapper(
            pages.list,
        )
        self.trend = async_to_raw_response_wrapper(
            pages.trend,
        )

    @cached_property
    def tests(self) -> AsyncTestsResourceWithRawResponse:
        return AsyncTestsResourceWithRawResponse(self._pages.tests)


class PagesResourceWithStreamingResponse:
    def __init__(self, pages: PagesResource) -> None:
        self._pages = pages

        self.list = to_streamed_response_wrapper(
            pages.list,
        )
        self.trend = to_streamed_response_wrapper(
            pages.trend,
        )

    @cached_property
    def tests(self) -> TestsResourceWithStreamingResponse:
        return TestsResourceWithStreamingResponse(self._pages.tests)


class AsyncPagesResourceWithStreamingResponse:
    def __init__(self, pages: AsyncPagesResource) -> None:
        self._pages = pages

        self.list = async_to_streamed_response_wrapper(
            pages.list,
        )
        self.trend = async_to_streamed_response_wrapper(
            pages.trend,
        )

    @cached_property
    def tests(self) -> AsyncTestsResourceWithStreamingResponse:
        return AsyncTestsResourceWithStreamingResponse(self._pages.tests)
