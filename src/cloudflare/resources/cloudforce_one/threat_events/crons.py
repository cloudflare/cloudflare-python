# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.cloudforce_one.threat_events.cron_edit_response import CronEditResponse
from ....types.cloudforce_one.threat_events.cron_list_response import CronListResponse

__all__ = ["CronsResource", "AsyncCronsResource"]


class CronsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CronsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CronsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CronsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CronsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CronListResponse:
        """
        Reads the last cron update time

        Args:
          account_id: Account ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{account_id}/cloudforce-one/events/cron",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CronListResponse,
        )

    def edit(
        self,
        *,
        account_id: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CronEditResponse:
        """
        Reads the last cron update time

        Args:
          account_id: Account ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/accounts/{account_id}/cloudforce-one/events/cron",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CronEditResponse,
        )


class AsyncCronsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCronsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCronsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCronsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCronsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        account_id: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CronListResponse:
        """
        Reads the last cron update time

        Args:
          account_id: Account ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{account_id}/cloudforce-one/events/cron",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CronListResponse,
        )

    async def edit(
        self,
        *,
        account_id: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CronEditResponse:
        """
        Reads the last cron update time

        Args:
          account_id: Account ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/accounts/{account_id}/cloudforce-one/events/cron",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CronEditResponse,
        )


class CronsResourceWithRawResponse:
    def __init__(self, crons: CronsResource) -> None:
        self._crons = crons

        self.list = to_raw_response_wrapper(
            crons.list,
        )
        self.edit = to_raw_response_wrapper(
            crons.edit,
        )


class AsyncCronsResourceWithRawResponse:
    def __init__(self, crons: AsyncCronsResource) -> None:
        self._crons = crons

        self.list = async_to_raw_response_wrapper(
            crons.list,
        )
        self.edit = async_to_raw_response_wrapper(
            crons.edit,
        )


class CronsResourceWithStreamingResponse:
    def __init__(self, crons: CronsResource) -> None:
        self._crons = crons

        self.list = to_streamed_response_wrapper(
            crons.list,
        )
        self.edit = to_streamed_response_wrapper(
            crons.edit,
        )


class AsyncCronsResourceWithStreamingResponse:
    def __init__(self, crons: AsyncCronsResource) -> None:
        self._crons = crons

        self.list = async_to_streamed_response_wrapper(
            crons.list,
        )
        self.edit = async_to_streamed_response_wrapper(
            crons.edit,
        )
