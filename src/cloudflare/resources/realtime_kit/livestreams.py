# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

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
from ...types.realtime_kit import (
    livestream_get_org_analytics_params,
    livestream_get_all_livestreams_params,
    livestream_create_independent_livestream_params,
    livestream_start_livestreaming_a_meeting_params,
    livestream_get_livestream_analytics_complete_params,
    livestream_get_livestream_session_for_livestream_id_params,
)
from ...types.realtime_kit.livestream_get_org_analytics_response import LivestreamGetOrgAnalyticsResponse
from ...types.realtime_kit.livestream_get_all_livestreams_response import LivestreamGetAllLivestreamsResponse
from ...types.realtime_kit.livestream_stop_livestreaming_a_meeting_response import (
    LivestreamStopLivestreamingAMeetingResponse,
)
from ...types.realtime_kit.livestream_create_independent_livestream_response import (
    LivestreamCreateIndependentLivestreamResponse,
)
from ...types.realtime_kit.livestream_start_livestreaming_a_meeting_response import (
    LivestreamStartLivestreamingAMeetingResponse,
)
from ...types.realtime_kit.livestream_get_meeting_active_livestreams_response import (
    LivestreamGetMeetingActiveLivestreamsResponse,
)
from ...types.realtime_kit.livestream_get_livestream_analytics_complete_response import (
    LivestreamGetLivestreamAnalyticsCompleteResponse,
)
from ...types.realtime_kit.livestream_get_active_livestreams_for_livestream_id_response import (
    LivestreamGetActiveLivestreamsForLivestreamIDResponse,
)
from ...types.realtime_kit.livestream_get_livestream_session_for_livestream_id_response import (
    LivestreamGetLivestreamSessionForLivestreamIDResponse,
)
from ...types.realtime_kit.livestream_get_livestream_session_details_for_session_id_response import (
    LivestreamGetLivestreamSessionDetailsForSessionIDResponse,
)

__all__ = ["LivestreamsResource", "AsyncLivestreamsResource"]


class LivestreamsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LivestreamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return LivestreamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LivestreamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return LivestreamsResourceWithStreamingResponse(self)

    def create_independent_livestream(
        self,
        app_id: str,
        *,
        account_id: str,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LivestreamCreateIndependentLivestreamResponse:
        """
        Creates a livestream for the given App ID and returns ingest server, stream key,
        and playback URL. You can pass custom input to the ingest server and stream key,
        and freely distribute the content using the playback URL on any player that
        supports HLS/LHLS.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          name: Name of the livestream

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return self._post(
            f"/accounts/{account_id}/realtime/kit/{app_id}/livestreams",
            body=maybe_transform(
                {"name": name},
                livestream_create_independent_livestream_params.LivestreamCreateIndependentLivestreamParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LivestreamCreateIndependentLivestreamResponse,
        )

    def get_active_livestreams_for_livestream_id(
        self,
        livestream_id: str,
        *,
        account_id: str,
        app_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LivestreamGetActiveLivestreamsForLivestreamIDResponse:
        """Returns details of all active livestreams for the given livestream ID.

        Retreive
        the livestream ID using the `Start livestreaming a meeting` API.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not livestream_id:
            raise ValueError(f"Expected a non-empty value for `livestream_id` but received {livestream_id!r}")
        return self._get(
            f"/accounts/{account_id}/realtime/kit/{app_id}/livestreams/{livestream_id}/active-livestream-session",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LivestreamGetActiveLivestreamsForLivestreamIDResponse,
        )

    def get_all_livestreams(
        self,
        app_id: str,
        *,
        account_id: str,
        end_time: Union[str, datetime] | Omit = omit,
        exclude_meetings: bool | Omit = omit,
        page_no: int | Omit = omit,
        per_page: int | Omit = omit,
        sort_order: Literal["ASC", "DSC"] | Omit = omit,
        start_time: Union[str, datetime] | Omit = omit,
        status: Literal["LIVE", "IDLE", "ERRORED", "INVOKED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LivestreamGetAllLivestreamsResponse:
        """Returns details of livestreams associated with the given App ID.

        It includes
        livestreams created by your App and RealtimeKit meetings that are livestreamed
        by your App. If you only want details of livestreams created by your App and not
        RealtimeKit meetings, you can use the `exclude_meetings` query parameter.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          end_time: Specify the end time range in ISO format to access the live stream.

          exclude_meetings: Exclude the RealtimeKit meetings that are livestreamed.

          page_no: The page number from which you want your page search results to be displayed.

          per_page: Number of results per page.

          sort_order: Specifies the sorting order for the results.

          start_time: Specify the start time range in ISO format to access the live stream.

          status: Specifies the status of the operation.

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
            f"/accounts/{account_id}/realtime/kit/{app_id}/livestreams",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_time": end_time,
                        "exclude_meetings": exclude_meetings,
                        "page_no": page_no,
                        "per_page": per_page,
                        "sort_order": sort_order,
                        "start_time": start_time,
                        "status": status,
                    },
                    livestream_get_all_livestreams_params.LivestreamGetAllLivestreamsParams,
                ),
            ),
            cast_to=LivestreamGetAllLivestreamsResponse,
        )

    def get_livestream_analytics_complete(
        self,
        app_id: str,
        *,
        account_id: str,
        end_time: Union[str, datetime] | Omit = omit,
        start_time: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LivestreamGetLivestreamAnalyticsCompleteResponse:
        """
        Returns livestream analytics for the specified time range.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          end_time: Specify the end time range in ISO format to access the livestream analytics.

          start_time: Specify the start time range in ISO format to access the livestream analytics.

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
            f"/accounts/{account_id}/realtime/kit/{app_id}/analytics/livestreams/overall",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_time": end_time,
                        "start_time": start_time,
                    },
                    livestream_get_livestream_analytics_complete_params.LivestreamGetLivestreamAnalyticsCompleteParams,
                ),
            ),
            cast_to=LivestreamGetLivestreamAnalyticsCompleteResponse,
        )

    def get_livestream_session_details_for_session_id(
        self,
        livestream_session_id: str,
        *,
        account_id: str,
        app_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LivestreamGetLivestreamSessionDetailsForSessionIDResponse:
        """Returns livestream session details for the given livestream session ID.

        Retrieve
        the `livestream_session_id`using the
        `Fetch livestream session details using a session ID` API.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not livestream_session_id:
            raise ValueError(
                f"Expected a non-empty value for `livestream_session_id` but received {livestream_session_id!r}"
            )
        return self._get(
            f"/accounts/{account_id}/realtime/kit/{app_id}/livestreams/sessions/{livestream_session_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LivestreamGetLivestreamSessionDetailsForSessionIDResponse,
        )

    def get_livestream_session_for_livestream_id(
        self,
        livestream_id: str,
        *,
        account_id: str,
        app_id: str,
        page_no: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LivestreamGetLivestreamSessionForLivestreamIDResponse:
        """
        Returns details of a livestream with sessions for the given livestream ID.
        Retreive the livestream ID using the `Start livestreaming a meeting` API.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          page_no: The page number from which you want your page search results to be displayed.

          per_page: Number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not livestream_id:
            raise ValueError(f"Expected a non-empty value for `livestream_id` but received {livestream_id!r}")
        return self._get(
            f"/accounts/{account_id}/realtime/kit/{app_id}/livestreams/{livestream_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_no": page_no,
                        "per_page": per_page,
                    },
                    livestream_get_livestream_session_for_livestream_id_params.LivestreamGetLivestreamSessionForLivestreamIDParams,
                ),
            ),
            cast_to=LivestreamGetLivestreamSessionForLivestreamIDResponse,
        )

    def get_meeting_active_livestreams(
        self,
        meeting_id: str,
        *,
        account_id: str,
        app_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LivestreamGetMeetingActiveLivestreamsResponse:
        """
        Returns details of all active livestreams for the given meeting ID.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not meeting_id:
            raise ValueError(f"Expected a non-empty value for `meeting_id` but received {meeting_id!r}")
        return self._get(
            f"/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-livestream",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LivestreamGetMeetingActiveLivestreamsResponse,
        )

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
    ) -> LivestreamGetOrgAnalyticsResponse:
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
                    livestream_get_org_analytics_params.LivestreamGetOrgAnalyticsParams,
                ),
            ),
            cast_to=LivestreamGetOrgAnalyticsResponse,
        )

    def start_livestreaming_a_meeting(
        self,
        meeting_id: str,
        *,
        account_id: str,
        app_id: str,
        name: Optional[str] | Omit = omit,
        video_config: livestream_start_livestreaming_a_meeting_params.VideoConfig | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LivestreamStartLivestreamingAMeetingResponse:
        """Starts livestream of a meeting associated with the given meeting ID.

        Retreive
        the meeting ID using the `Create a meeting` API.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not meeting_id:
            raise ValueError(f"Expected a non-empty value for `meeting_id` but received {meeting_id!r}")
        return self._post(
            f"/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/livestreams",
            body=maybe_transform(
                {
                    "name": name,
                    "video_config": video_config,
                },
                livestream_start_livestreaming_a_meeting_params.LivestreamStartLivestreamingAMeetingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LivestreamStartLivestreamingAMeetingResponse,
        )

    def stop_livestreaming_a_meeting(
        self,
        meeting_id: str,
        *,
        account_id: str,
        app_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LivestreamStopLivestreamingAMeetingResponse:
        """
        Stops the active livestream of a meeting associated with the given meeting ID.
        Retreive the meeting ID using the `Create a meeting` API.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not meeting_id:
            raise ValueError(f"Expected a non-empty value for `meeting_id` but received {meeting_id!r}")
        return self._post(
            f"/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-livestream/stop",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LivestreamStopLivestreamingAMeetingResponse,
        )


class AsyncLivestreamsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLivestreamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLivestreamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLivestreamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncLivestreamsResourceWithStreamingResponse(self)

    async def create_independent_livestream(
        self,
        app_id: str,
        *,
        account_id: str,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LivestreamCreateIndependentLivestreamResponse:
        """
        Creates a livestream for the given App ID and returns ingest server, stream key,
        and playback URL. You can pass custom input to the ingest server and stream key,
        and freely distribute the content using the playback URL on any player that
        supports HLS/LHLS.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          name: Name of the livestream

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return await self._post(
            f"/accounts/{account_id}/realtime/kit/{app_id}/livestreams",
            body=await async_maybe_transform(
                {"name": name},
                livestream_create_independent_livestream_params.LivestreamCreateIndependentLivestreamParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LivestreamCreateIndependentLivestreamResponse,
        )

    async def get_active_livestreams_for_livestream_id(
        self,
        livestream_id: str,
        *,
        account_id: str,
        app_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LivestreamGetActiveLivestreamsForLivestreamIDResponse:
        """Returns details of all active livestreams for the given livestream ID.

        Retreive
        the livestream ID using the `Start livestreaming a meeting` API.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not livestream_id:
            raise ValueError(f"Expected a non-empty value for `livestream_id` but received {livestream_id!r}")
        return await self._get(
            f"/accounts/{account_id}/realtime/kit/{app_id}/livestreams/{livestream_id}/active-livestream-session",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LivestreamGetActiveLivestreamsForLivestreamIDResponse,
        )

    async def get_all_livestreams(
        self,
        app_id: str,
        *,
        account_id: str,
        end_time: Union[str, datetime] | Omit = omit,
        exclude_meetings: bool | Omit = omit,
        page_no: int | Omit = omit,
        per_page: int | Omit = omit,
        sort_order: Literal["ASC", "DSC"] | Omit = omit,
        start_time: Union[str, datetime] | Omit = omit,
        status: Literal["LIVE", "IDLE", "ERRORED", "INVOKED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LivestreamGetAllLivestreamsResponse:
        """Returns details of livestreams associated with the given App ID.

        It includes
        livestreams created by your App and RealtimeKit meetings that are livestreamed
        by your App. If you only want details of livestreams created by your App and not
        RealtimeKit meetings, you can use the `exclude_meetings` query parameter.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          end_time: Specify the end time range in ISO format to access the live stream.

          exclude_meetings: Exclude the RealtimeKit meetings that are livestreamed.

          page_no: The page number from which you want your page search results to be displayed.

          per_page: Number of results per page.

          sort_order: Specifies the sorting order for the results.

          start_time: Specify the start time range in ISO format to access the live stream.

          status: Specifies the status of the operation.

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
            f"/accounts/{account_id}/realtime/kit/{app_id}/livestreams",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_time": end_time,
                        "exclude_meetings": exclude_meetings,
                        "page_no": page_no,
                        "per_page": per_page,
                        "sort_order": sort_order,
                        "start_time": start_time,
                        "status": status,
                    },
                    livestream_get_all_livestreams_params.LivestreamGetAllLivestreamsParams,
                ),
            ),
            cast_to=LivestreamGetAllLivestreamsResponse,
        )

    async def get_livestream_analytics_complete(
        self,
        app_id: str,
        *,
        account_id: str,
        end_time: Union[str, datetime] | Omit = omit,
        start_time: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LivestreamGetLivestreamAnalyticsCompleteResponse:
        """
        Returns livestream analytics for the specified time range.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          end_time: Specify the end time range in ISO format to access the livestream analytics.

          start_time: Specify the start time range in ISO format to access the livestream analytics.

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
            f"/accounts/{account_id}/realtime/kit/{app_id}/analytics/livestreams/overall",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_time": end_time,
                        "start_time": start_time,
                    },
                    livestream_get_livestream_analytics_complete_params.LivestreamGetLivestreamAnalyticsCompleteParams,
                ),
            ),
            cast_to=LivestreamGetLivestreamAnalyticsCompleteResponse,
        )

    async def get_livestream_session_details_for_session_id(
        self,
        livestream_session_id: str,
        *,
        account_id: str,
        app_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LivestreamGetLivestreamSessionDetailsForSessionIDResponse:
        """Returns livestream session details for the given livestream session ID.

        Retrieve
        the `livestream_session_id`using the
        `Fetch livestream session details using a session ID` API.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not livestream_session_id:
            raise ValueError(
                f"Expected a non-empty value for `livestream_session_id` but received {livestream_session_id!r}"
            )
        return await self._get(
            f"/accounts/{account_id}/realtime/kit/{app_id}/livestreams/sessions/{livestream_session_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LivestreamGetLivestreamSessionDetailsForSessionIDResponse,
        )

    async def get_livestream_session_for_livestream_id(
        self,
        livestream_id: str,
        *,
        account_id: str,
        app_id: str,
        page_no: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LivestreamGetLivestreamSessionForLivestreamIDResponse:
        """
        Returns details of a livestream with sessions for the given livestream ID.
        Retreive the livestream ID using the `Start livestreaming a meeting` API.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          page_no: The page number from which you want your page search results to be displayed.

          per_page: Number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not livestream_id:
            raise ValueError(f"Expected a non-empty value for `livestream_id` but received {livestream_id!r}")
        return await self._get(
            f"/accounts/{account_id}/realtime/kit/{app_id}/livestreams/{livestream_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page_no": page_no,
                        "per_page": per_page,
                    },
                    livestream_get_livestream_session_for_livestream_id_params.LivestreamGetLivestreamSessionForLivestreamIDParams,
                ),
            ),
            cast_to=LivestreamGetLivestreamSessionForLivestreamIDResponse,
        )

    async def get_meeting_active_livestreams(
        self,
        meeting_id: str,
        *,
        account_id: str,
        app_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LivestreamGetMeetingActiveLivestreamsResponse:
        """
        Returns details of all active livestreams for the given meeting ID.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not meeting_id:
            raise ValueError(f"Expected a non-empty value for `meeting_id` but received {meeting_id!r}")
        return await self._get(
            f"/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-livestream",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LivestreamGetMeetingActiveLivestreamsResponse,
        )

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
    ) -> LivestreamGetOrgAnalyticsResponse:
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
                    livestream_get_org_analytics_params.LivestreamGetOrgAnalyticsParams,
                ),
            ),
            cast_to=LivestreamGetOrgAnalyticsResponse,
        )

    async def start_livestreaming_a_meeting(
        self,
        meeting_id: str,
        *,
        account_id: str,
        app_id: str,
        name: Optional[str] | Omit = omit,
        video_config: livestream_start_livestreaming_a_meeting_params.VideoConfig | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LivestreamStartLivestreamingAMeetingResponse:
        """Starts livestream of a meeting associated with the given meeting ID.

        Retreive
        the meeting ID using the `Create a meeting` API.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not meeting_id:
            raise ValueError(f"Expected a non-empty value for `meeting_id` but received {meeting_id!r}")
        return await self._post(
            f"/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/livestreams",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "video_config": video_config,
                },
                livestream_start_livestreaming_a_meeting_params.LivestreamStartLivestreamingAMeetingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LivestreamStartLivestreamingAMeetingResponse,
        )

    async def stop_livestreaming_a_meeting(
        self,
        meeting_id: str,
        *,
        account_id: str,
        app_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LivestreamStopLivestreamingAMeetingResponse:
        """
        Stops the active livestream of a meeting associated with the given meeting ID.
        Retreive the meeting ID using the `Create a meeting` API.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not meeting_id:
            raise ValueError(f"Expected a non-empty value for `meeting_id` but received {meeting_id!r}")
        return await self._post(
            f"/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-livestream/stop",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LivestreamStopLivestreamingAMeetingResponse,
        )


class LivestreamsResourceWithRawResponse:
    def __init__(self, livestreams: LivestreamsResource) -> None:
        self._livestreams = livestreams

        self.create_independent_livestream = to_raw_response_wrapper(
            livestreams.create_independent_livestream,
        )
        self.get_active_livestreams_for_livestream_id = to_raw_response_wrapper(
            livestreams.get_active_livestreams_for_livestream_id,
        )
        self.get_all_livestreams = to_raw_response_wrapper(
            livestreams.get_all_livestreams,
        )
        self.get_livestream_analytics_complete = to_raw_response_wrapper(
            livestreams.get_livestream_analytics_complete,
        )
        self.get_livestream_session_details_for_session_id = to_raw_response_wrapper(
            livestreams.get_livestream_session_details_for_session_id,
        )
        self.get_livestream_session_for_livestream_id = to_raw_response_wrapper(
            livestreams.get_livestream_session_for_livestream_id,
        )
        self.get_meeting_active_livestreams = to_raw_response_wrapper(
            livestreams.get_meeting_active_livestreams,
        )
        self.get_org_analytics = to_raw_response_wrapper(
            livestreams.get_org_analytics,
        )
        self.start_livestreaming_a_meeting = to_raw_response_wrapper(
            livestreams.start_livestreaming_a_meeting,
        )
        self.stop_livestreaming_a_meeting = to_raw_response_wrapper(
            livestreams.stop_livestreaming_a_meeting,
        )


class AsyncLivestreamsResourceWithRawResponse:
    def __init__(self, livestreams: AsyncLivestreamsResource) -> None:
        self._livestreams = livestreams

        self.create_independent_livestream = async_to_raw_response_wrapper(
            livestreams.create_independent_livestream,
        )
        self.get_active_livestreams_for_livestream_id = async_to_raw_response_wrapper(
            livestreams.get_active_livestreams_for_livestream_id,
        )
        self.get_all_livestreams = async_to_raw_response_wrapper(
            livestreams.get_all_livestreams,
        )
        self.get_livestream_analytics_complete = async_to_raw_response_wrapper(
            livestreams.get_livestream_analytics_complete,
        )
        self.get_livestream_session_details_for_session_id = async_to_raw_response_wrapper(
            livestreams.get_livestream_session_details_for_session_id,
        )
        self.get_livestream_session_for_livestream_id = async_to_raw_response_wrapper(
            livestreams.get_livestream_session_for_livestream_id,
        )
        self.get_meeting_active_livestreams = async_to_raw_response_wrapper(
            livestreams.get_meeting_active_livestreams,
        )
        self.get_org_analytics = async_to_raw_response_wrapper(
            livestreams.get_org_analytics,
        )
        self.start_livestreaming_a_meeting = async_to_raw_response_wrapper(
            livestreams.start_livestreaming_a_meeting,
        )
        self.stop_livestreaming_a_meeting = async_to_raw_response_wrapper(
            livestreams.stop_livestreaming_a_meeting,
        )


class LivestreamsResourceWithStreamingResponse:
    def __init__(self, livestreams: LivestreamsResource) -> None:
        self._livestreams = livestreams

        self.create_independent_livestream = to_streamed_response_wrapper(
            livestreams.create_independent_livestream,
        )
        self.get_active_livestreams_for_livestream_id = to_streamed_response_wrapper(
            livestreams.get_active_livestreams_for_livestream_id,
        )
        self.get_all_livestreams = to_streamed_response_wrapper(
            livestreams.get_all_livestreams,
        )
        self.get_livestream_analytics_complete = to_streamed_response_wrapper(
            livestreams.get_livestream_analytics_complete,
        )
        self.get_livestream_session_details_for_session_id = to_streamed_response_wrapper(
            livestreams.get_livestream_session_details_for_session_id,
        )
        self.get_livestream_session_for_livestream_id = to_streamed_response_wrapper(
            livestreams.get_livestream_session_for_livestream_id,
        )
        self.get_meeting_active_livestreams = to_streamed_response_wrapper(
            livestreams.get_meeting_active_livestreams,
        )
        self.get_org_analytics = to_streamed_response_wrapper(
            livestreams.get_org_analytics,
        )
        self.start_livestreaming_a_meeting = to_streamed_response_wrapper(
            livestreams.start_livestreaming_a_meeting,
        )
        self.stop_livestreaming_a_meeting = to_streamed_response_wrapper(
            livestreams.stop_livestreaming_a_meeting,
        )


class AsyncLivestreamsResourceWithStreamingResponse:
    def __init__(self, livestreams: AsyncLivestreamsResource) -> None:
        self._livestreams = livestreams

        self.create_independent_livestream = async_to_streamed_response_wrapper(
            livestreams.create_independent_livestream,
        )
        self.get_active_livestreams_for_livestream_id = async_to_streamed_response_wrapper(
            livestreams.get_active_livestreams_for_livestream_id,
        )
        self.get_all_livestreams = async_to_streamed_response_wrapper(
            livestreams.get_all_livestreams,
        )
        self.get_livestream_analytics_complete = async_to_streamed_response_wrapper(
            livestreams.get_livestream_analytics_complete,
        )
        self.get_livestream_session_details_for_session_id = async_to_streamed_response_wrapper(
            livestreams.get_livestream_session_details_for_session_id,
        )
        self.get_livestream_session_for_livestream_id = async_to_streamed_response_wrapper(
            livestreams.get_livestream_session_for_livestream_id,
        )
        self.get_meeting_active_livestreams = async_to_streamed_response_wrapper(
            livestreams.get_meeting_active_livestreams,
        )
        self.get_org_analytics = async_to_streamed_response_wrapper(
            livestreams.get_org_analytics,
        )
        self.start_livestreaming_a_meeting = async_to_streamed_response_wrapper(
            livestreams.start_livestreaming_a_meeting,
        )
        self.stop_livestreaming_a_meeting = async_to_streamed_response_wrapper(
            livestreams.stop_livestreaming_a_meeting,
        )
