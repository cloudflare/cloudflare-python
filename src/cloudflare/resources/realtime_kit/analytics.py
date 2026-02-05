# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.realtime_kit import analytics_get_org_analytics_params
from ...types.realtime_kit.analytics_get_org_analytics_response import AnalyticsGetOrgAnalyticsResponse

__all__ = ["AnalyticsResource", "AsyncAnalyticsResource"]


class AnalyticsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AnalyticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnalyticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AnalyticsResourceWithStreamingResponse(self)

    def get_org_analytics(
        self,
        app_id: str,
        *,
        account_id: str,
        end_date: str | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsGetOrgAnalyticsResponse:
        """
        Returns day-wise session and recording analytics data of an App for the
        specified time range start_date to end_date. If start_date and end_date are not
        provided, the default time range is set from 30 days ago to the current date.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          end_date: end date in YYYY-MM-DD format

          start_date: start date in YYYY-MM-DD format

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return self._get(
            f"/accounts/{account_id}/realtime/kit/{app_id}/analytics/daywise",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    analytics_get_org_analytics_params.AnalyticsGetOrgAnalyticsParams,
                ),
            ),
            cast_to=AnalyticsGetOrgAnalyticsResponse,
        )


class AsyncAnalyticsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAnalyticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnalyticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAnalyticsResourceWithStreamingResponse(self)

    async def get_org_analytics(
        self,
        app_id: str,
        *,
        account_id: str,
        end_date: str | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsGetOrgAnalyticsResponse:
        """
        Returns day-wise session and recording analytics data of an App for the
        specified time range start_date to end_date. If start_date and end_date are not
        provided, the default time range is set from 30 days ago to the current date.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          end_date: end date in YYYY-MM-DD format

          start_date: start date in YYYY-MM-DD format

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return await self._get(
            f"/accounts/{account_id}/realtime/kit/{app_id}/analytics/daywise",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    analytics_get_org_analytics_params.AnalyticsGetOrgAnalyticsParams,
                ),
            ),
            cast_to=AnalyticsGetOrgAnalyticsResponse,
        )


class AnalyticsResourceWithRawResponse:
    def __init__(self, analytics: AnalyticsResource) -> None:
        self._analytics = analytics

        self.get_org_analytics = to_raw_response_wrapper(
            analytics.get_org_analytics,
        )


class AsyncAnalyticsResourceWithRawResponse:
    def __init__(self, analytics: AsyncAnalyticsResource) -> None:
        self._analytics = analytics

        self.get_org_analytics = async_to_raw_response_wrapper(
            analytics.get_org_analytics,
        )


class AnalyticsResourceWithStreamingResponse:
    def __init__(self, analytics: AnalyticsResource) -> None:
        self._analytics = analytics

        self.get_org_analytics = to_streamed_response_wrapper(
            analytics.get_org_analytics,
        )


class AsyncAnalyticsResourceWithStreamingResponse:
    def __init__(self, analytics: AsyncAnalyticsResource) -> None:
        self._analytics = analytics

        self.get_org_analytics = async_to_streamed_response_wrapper(
            analytics.get_org_analytics,
        )
