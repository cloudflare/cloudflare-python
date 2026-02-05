# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
    recording_get_recordings_params,
    recording_start_recordings_params,
    recording_start_track_recording_params,
    recording_pause_resume_stop_recording_params,
)
from ...types.realtime_kit.recording_get_recordings_response import RecordingGetRecordingsResponse
from ...types.realtime_kit.recording_start_recordings_response import RecordingStartRecordingsResponse
from ...types.realtime_kit.recording_get_one_recording_response import RecordingGetOneRecordingResponse
from ...types.realtime_kit.recording_get_active_recordings_response import RecordingGetActiveRecordingsResponse
from ...types.realtime_kit.recording_pause_resume_stop_recording_response import (
    RecordingPauseResumeStopRecordingResponse,
)

__all__ = ["RecordingsResource", "AsyncRecordingsResource"]


class RecordingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RecordingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RecordingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RecordingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RecordingsResourceWithStreamingResponse(self)

    def get_active_recordings(
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
    ) -> RecordingGetActiveRecordingsResponse:
        """
        Returns the active recording details for the given meeting ID.

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
            f"/accounts/{account_id}/realtime/kit/{app_id}/recordings/active-recording/{meeting_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingGetActiveRecordingsResponse,
        )

    def get_one_recording(
        self,
        recording_id: str,
        *,
        account_id: str,
        app_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordingGetOneRecordingResponse:
        """
        Returns details of a recording for the given recording ID.

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
        if not recording_id:
            raise ValueError(f"Expected a non-empty value for `recording_id` but received {recording_id!r}")
        return self._get(
            f"/accounts/{account_id}/realtime/kit/{app_id}/recordings/{recording_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingGetOneRecordingResponse,
        )

    def get_recordings(
        self,
        app_id: str,
        *,
        account_id: str,
        end_time: Union[str, datetime] | Omit = omit,
        expired: bool | Omit = omit,
        meeting_id: str | Omit = omit,
        page_no: float | Omit = omit,
        per_page: float | Omit = omit,
        search: str | Omit = omit,
        sort_by: Literal["invokedTime"] | Omit = omit,
        sort_order: Literal["ASC", "DESC"] | Omit = omit,
        start_time: Union[str, datetime] | Omit = omit,
        status: List[Literal["INVOKED", "RECORDING", "UPLOADING", "UPLOADED"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordingGetRecordingsResponse:
        """Returns all recordings for an App.

        If the `meeting_id` parameter is passed,
        returns all recordings for the given meeting ID.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          end_time: The end time range for which you want to retrieve the meetings. The time must be
              specified in ISO format.

          expired: If passed, only shows expired/non-expired recordings on RealtimeKit's bucket

          meeting_id: ID of a meeting. Optional. Will limit results to only this meeting if passed.

          page_no: The page number from which you want your page search results to be displayed.

          per_page: Number of results per page

          search: The search query string. You can search using the meeting ID or title.

          start_time: The start time range for which you want to retrieve the meetings. The time must
              be specified in ISO format.

          status: Filter by one or more recording status

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
            f"/accounts/{account_id}/realtime/kit/{app_id}/recordings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_time": end_time,
                        "expired": expired,
                        "meeting_id": meeting_id,
                        "page_no": page_no,
                        "per_page": per_page,
                        "search": search,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "start_time": start_time,
                        "status": status,
                    },
                    recording_get_recordings_params.RecordingGetRecordingsParams,
                ),
            ),
            cast_to=RecordingGetRecordingsResponse,
        )

    def pause_resume_stop_recording(
        self,
        recording_id: str,
        *,
        account_id: str,
        app_id: str,
        action: Literal["stop", "pause", "resume"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordingPauseResumeStopRecordingResponse:
        """
        Pause/Resume/Stop a given recording ID.

        Args:
          account_id: The account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not recording_id:
            raise ValueError(f"Expected a non-empty value for `recording_id` but received {recording_id!r}")
        return self._put(
            f"/accounts/{account_id}/realtime/kit/{app_id}/recordings/{recording_id}",
            body=maybe_transform(
                {"action": action}, recording_pause_resume_stop_recording_params.RecordingPauseResumeStopRecordingParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingPauseResumeStopRecordingResponse,
        )

    def start_recordings(
        self,
        app_id: str,
        *,
        account_id: str,
        allow_multiple_recordings: bool | Omit = omit,
        audio_config: recording_start_recordings_params.AudioConfig | Omit = omit,
        file_name_prefix: str | Omit = omit,
        interactive_config: recording_start_recordings_params.InteractiveConfig | Omit = omit,
        max_seconds: int | Omit = omit,
        meeting_id: str | Omit = omit,
        realtimekit_bucket_config: recording_start_recordings_params.RealtimekitBucketConfig | Omit = omit,
        rtmp_out_config: recording_start_recordings_params.RtmpOutConfig | Omit = omit,
        storage_config: Optional[recording_start_recordings_params.StorageConfig] | Omit = omit,
        url: str | Omit = omit,
        video_config: recording_start_recordings_params.VideoConfig | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordingStartRecordingsResponse:
        """Starts recording a meeting.

        The meeting can be started by an App admin directly,
        or a participant with permissions to start a recording, based on the type of
        authorization used.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          allow_multiple_recordings: By default, a meeting allows only one recording to run at a time. Enabling the
              `allow_multiple_recordings` parameter to true allows you to initiate multiple
              recordings concurrently in the same meeting. This allows you to record separate
              videos of the same meeting with different configurations, such as portrait mode
              or landscape mode.

          audio_config: Object containing configuration regarding the audio that is being recorded.

          file_name_prefix: Update the recording file name.

          interactive_config: Allows you to add timed metadata to your recordings, which are digital markers
              inserted into a video file to provide contextual information at specific points
              in the content range. The ID3 tags containing this information are available to
              clients on the playback timeline in HLS format. The output files are generated
              in a compressed .tar format.

          max_seconds: Specifies the maximum duration for recording in seconds, ranging from a minimum
              of 60 seconds to a maximum of 24 hours.

          meeting_id: ID of the meeting to record.

          url: Pass a custom url to record arbitary screen

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
            f"/accounts/{account_id}/realtime/kit/{app_id}/recordings",
            body=maybe_transform(
                {
                    "allow_multiple_recordings": allow_multiple_recordings,
                    "audio_config": audio_config,
                    "file_name_prefix": file_name_prefix,
                    "interactive_config": interactive_config,
                    "max_seconds": max_seconds,
                    "meeting_id": meeting_id,
                    "realtimekit_bucket_config": realtimekit_bucket_config,
                    "rtmp_out_config": rtmp_out_config,
                    "storage_config": storage_config,
                    "url": url,
                    "video_config": video_config,
                },
                recording_start_recordings_params.RecordingStartRecordingsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingStartRecordingsResponse,
        )

    def start_track_recording(
        self,
        app_id: str,
        *,
        account_id: str,
        layers: Dict[str, recording_start_track_recording_params.Layers],
        meeting_id: str,
        max_seconds: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Starts a track recording in a meeting.

        Track recordings consist of "layers".
        Layers are used to map audio/video tracks in a meeting to output destinations.
        More information about track recordings is available in the
        [Track Recordings Guide Page](https://docs.realtime.cloudflare.com/guides/capabilities/recording/recording-overview).

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          meeting_id: ID of the meeting to record.

          max_seconds: Maximum seconds this recording should be active for (beta)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/accounts/{account_id}/realtime/kit/{app_id}/recordings/track",
            body=maybe_transform(
                {
                    "layers": layers,
                    "meeting_id": meeting_id,
                    "max_seconds": max_seconds,
                },
                recording_start_track_recording_params.RecordingStartTrackRecordingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncRecordingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRecordingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRecordingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRecordingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncRecordingsResourceWithStreamingResponse(self)

    async def get_active_recordings(
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
    ) -> RecordingGetActiveRecordingsResponse:
        """
        Returns the active recording details for the given meeting ID.

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
            f"/accounts/{account_id}/realtime/kit/{app_id}/recordings/active-recording/{meeting_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingGetActiveRecordingsResponse,
        )

    async def get_one_recording(
        self,
        recording_id: str,
        *,
        account_id: str,
        app_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordingGetOneRecordingResponse:
        """
        Returns details of a recording for the given recording ID.

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
        if not recording_id:
            raise ValueError(f"Expected a non-empty value for `recording_id` but received {recording_id!r}")
        return await self._get(
            f"/accounts/{account_id}/realtime/kit/{app_id}/recordings/{recording_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingGetOneRecordingResponse,
        )

    async def get_recordings(
        self,
        app_id: str,
        *,
        account_id: str,
        end_time: Union[str, datetime] | Omit = omit,
        expired: bool | Omit = omit,
        meeting_id: str | Omit = omit,
        page_no: float | Omit = omit,
        per_page: float | Omit = omit,
        search: str | Omit = omit,
        sort_by: Literal["invokedTime"] | Omit = omit,
        sort_order: Literal["ASC", "DESC"] | Omit = omit,
        start_time: Union[str, datetime] | Omit = omit,
        status: List[Literal["INVOKED", "RECORDING", "UPLOADING", "UPLOADED"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordingGetRecordingsResponse:
        """Returns all recordings for an App.

        If the `meeting_id` parameter is passed,
        returns all recordings for the given meeting ID.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          end_time: The end time range for which you want to retrieve the meetings. The time must be
              specified in ISO format.

          expired: If passed, only shows expired/non-expired recordings on RealtimeKit's bucket

          meeting_id: ID of a meeting. Optional. Will limit results to only this meeting if passed.

          page_no: The page number from which you want your page search results to be displayed.

          per_page: Number of results per page

          search: The search query string. You can search using the meeting ID or title.

          start_time: The start time range for which you want to retrieve the meetings. The time must
              be specified in ISO format.

          status: Filter by one or more recording status

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
            f"/accounts/{account_id}/realtime/kit/{app_id}/recordings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_time": end_time,
                        "expired": expired,
                        "meeting_id": meeting_id,
                        "page_no": page_no,
                        "per_page": per_page,
                        "search": search,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "start_time": start_time,
                        "status": status,
                    },
                    recording_get_recordings_params.RecordingGetRecordingsParams,
                ),
            ),
            cast_to=RecordingGetRecordingsResponse,
        )

    async def pause_resume_stop_recording(
        self,
        recording_id: str,
        *,
        account_id: str,
        app_id: str,
        action: Literal["stop", "pause", "resume"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordingPauseResumeStopRecordingResponse:
        """
        Pause/Resume/Stop a given recording ID.

        Args:
          account_id: The account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not recording_id:
            raise ValueError(f"Expected a non-empty value for `recording_id` but received {recording_id!r}")
        return await self._put(
            f"/accounts/{account_id}/realtime/kit/{app_id}/recordings/{recording_id}",
            body=await async_maybe_transform(
                {"action": action}, recording_pause_resume_stop_recording_params.RecordingPauseResumeStopRecordingParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingPauseResumeStopRecordingResponse,
        )

    async def start_recordings(
        self,
        app_id: str,
        *,
        account_id: str,
        allow_multiple_recordings: bool | Omit = omit,
        audio_config: recording_start_recordings_params.AudioConfig | Omit = omit,
        file_name_prefix: str | Omit = omit,
        interactive_config: recording_start_recordings_params.InteractiveConfig | Omit = omit,
        max_seconds: int | Omit = omit,
        meeting_id: str | Omit = omit,
        realtimekit_bucket_config: recording_start_recordings_params.RealtimekitBucketConfig | Omit = omit,
        rtmp_out_config: recording_start_recordings_params.RtmpOutConfig | Omit = omit,
        storage_config: Optional[recording_start_recordings_params.StorageConfig] | Omit = omit,
        url: str | Omit = omit,
        video_config: recording_start_recordings_params.VideoConfig | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordingStartRecordingsResponse:
        """Starts recording a meeting.

        The meeting can be started by an App admin directly,
        or a participant with permissions to start a recording, based on the type of
        authorization used.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          allow_multiple_recordings: By default, a meeting allows only one recording to run at a time. Enabling the
              `allow_multiple_recordings` parameter to true allows you to initiate multiple
              recordings concurrently in the same meeting. This allows you to record separate
              videos of the same meeting with different configurations, such as portrait mode
              or landscape mode.

          audio_config: Object containing configuration regarding the audio that is being recorded.

          file_name_prefix: Update the recording file name.

          interactive_config: Allows you to add timed metadata to your recordings, which are digital markers
              inserted into a video file to provide contextual information at specific points
              in the content range. The ID3 tags containing this information are available to
              clients on the playback timeline in HLS format. The output files are generated
              in a compressed .tar format.

          max_seconds: Specifies the maximum duration for recording in seconds, ranging from a minimum
              of 60 seconds to a maximum of 24 hours.

          meeting_id: ID of the meeting to record.

          url: Pass a custom url to record arbitary screen

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
            f"/accounts/{account_id}/realtime/kit/{app_id}/recordings",
            body=await async_maybe_transform(
                {
                    "allow_multiple_recordings": allow_multiple_recordings,
                    "audio_config": audio_config,
                    "file_name_prefix": file_name_prefix,
                    "interactive_config": interactive_config,
                    "max_seconds": max_seconds,
                    "meeting_id": meeting_id,
                    "realtimekit_bucket_config": realtimekit_bucket_config,
                    "rtmp_out_config": rtmp_out_config,
                    "storage_config": storage_config,
                    "url": url,
                    "video_config": video_config,
                },
                recording_start_recordings_params.RecordingStartRecordingsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingStartRecordingsResponse,
        )

    async def start_track_recording(
        self,
        app_id: str,
        *,
        account_id: str,
        layers: Dict[str, recording_start_track_recording_params.Layers],
        meeting_id: str,
        max_seconds: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Starts a track recording in a meeting.

        Track recordings consist of "layers".
        Layers are used to map audio/video tracks in a meeting to output destinations.
        More information about track recordings is available in the
        [Track Recordings Guide Page](https://docs.realtime.cloudflare.com/guides/capabilities/recording/recording-overview).

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          meeting_id: ID of the meeting to record.

          max_seconds: Maximum seconds this recording should be active for (beta)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/accounts/{account_id}/realtime/kit/{app_id}/recordings/track",
            body=await async_maybe_transform(
                {
                    "layers": layers,
                    "meeting_id": meeting_id,
                    "max_seconds": max_seconds,
                },
                recording_start_track_recording_params.RecordingStartTrackRecordingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class RecordingsResourceWithRawResponse:
    def __init__(self, recordings: RecordingsResource) -> None:
        self._recordings = recordings

        self.get_active_recordings = to_raw_response_wrapper(
            recordings.get_active_recordings,
        )
        self.get_one_recording = to_raw_response_wrapper(
            recordings.get_one_recording,
        )
        self.get_recordings = to_raw_response_wrapper(
            recordings.get_recordings,
        )
        self.pause_resume_stop_recording = to_raw_response_wrapper(
            recordings.pause_resume_stop_recording,
        )
        self.start_recordings = to_raw_response_wrapper(
            recordings.start_recordings,
        )
        self.start_track_recording = to_raw_response_wrapper(
            recordings.start_track_recording,
        )


class AsyncRecordingsResourceWithRawResponse:
    def __init__(self, recordings: AsyncRecordingsResource) -> None:
        self._recordings = recordings

        self.get_active_recordings = async_to_raw_response_wrapper(
            recordings.get_active_recordings,
        )
        self.get_one_recording = async_to_raw_response_wrapper(
            recordings.get_one_recording,
        )
        self.get_recordings = async_to_raw_response_wrapper(
            recordings.get_recordings,
        )
        self.pause_resume_stop_recording = async_to_raw_response_wrapper(
            recordings.pause_resume_stop_recording,
        )
        self.start_recordings = async_to_raw_response_wrapper(
            recordings.start_recordings,
        )
        self.start_track_recording = async_to_raw_response_wrapper(
            recordings.start_track_recording,
        )


class RecordingsResourceWithStreamingResponse:
    def __init__(self, recordings: RecordingsResource) -> None:
        self._recordings = recordings

        self.get_active_recordings = to_streamed_response_wrapper(
            recordings.get_active_recordings,
        )
        self.get_one_recording = to_streamed_response_wrapper(
            recordings.get_one_recording,
        )
        self.get_recordings = to_streamed_response_wrapper(
            recordings.get_recordings,
        )
        self.pause_resume_stop_recording = to_streamed_response_wrapper(
            recordings.pause_resume_stop_recording,
        )
        self.start_recordings = to_streamed_response_wrapper(
            recordings.start_recordings,
        )
        self.start_track_recording = to_streamed_response_wrapper(
            recordings.start_track_recording,
        )


class AsyncRecordingsResourceWithStreamingResponse:
    def __init__(self, recordings: AsyncRecordingsResource) -> None:
        self._recordings = recordings

        self.get_active_recordings = async_to_streamed_response_wrapper(
            recordings.get_active_recordings,
        )
        self.get_one_recording = async_to_streamed_response_wrapper(
            recordings.get_one_recording,
        )
        self.get_recordings = async_to_streamed_response_wrapper(
            recordings.get_recordings,
        )
        self.pause_resume_stop_recording = async_to_streamed_response_wrapper(
            recordings.pause_resume_stop_recording,
        )
        self.start_recordings = async_to_streamed_response_wrapper(
            recordings.start_recordings,
        )
        self.start_track_recording = async_to_streamed_response_wrapper(
            recordings.start_track_recording,
        )
