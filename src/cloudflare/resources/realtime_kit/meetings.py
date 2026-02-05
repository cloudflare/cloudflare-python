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
    meeting_get_params,
    meeting_create_params,
    meeting_add_participant_params,
    meeting_edit_participant_params,
    meeting_get_meeting_by_id_params,
    meeting_update_meeting_by_id_params,
    meeting_replace_meeting_by_id_params,
    meeting_get_meeting_participants_params,
)
from ...types.realtime_kit.meeting_get_response import MeetingGetResponse
from ...types.realtime_kit.meeting_create_response import MeetingCreateResponse
from ...types.realtime_kit.meeting_add_participant_response import MeetingAddParticipantResponse
from ...types.realtime_kit.meeting_edit_participant_response import MeetingEditParticipantResponse
from ...types.realtime_kit.meeting_get_meeting_by_id_response import MeetingGetMeetingByIDResponse
from ...types.realtime_kit.meeting_update_meeting_by_id_response import MeetingUpdateMeetingByIDResponse
from ...types.realtime_kit.meeting_replace_meeting_by_id_response import MeetingReplaceMeetingByIDResponse
from ...types.realtime_kit.meeting_get_meeting_participant_response import MeetingGetMeetingParticipantResponse
from ...types.realtime_kit.meeting_get_meeting_participants_response import MeetingGetMeetingParticipantsResponse
from ...types.realtime_kit.meeting_refresh_participant_token_response import MeetingRefreshParticipantTokenResponse
from ...types.realtime_kit.meeting_delete_meeting_participant_response import MeetingDeleteMeetingParticipantResponse

__all__ = ["MeetingsResource", "AsyncMeetingsResource"]


class MeetingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MeetingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return MeetingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MeetingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return MeetingsResourceWithStreamingResponse(self)

    def create(
        self,
        app_id: str,
        *,
        account_id: str,
        ai_config: meeting_create_params.AIConfig | Omit = omit,
        live_stream_on_start: Optional[bool] | Omit = omit,
        persist_chat: bool | Omit = omit,
        record_on_start: Optional[bool] | Omit = omit,
        recording_config: meeting_create_params.RecordingConfig | Omit = omit,
        session_keep_alive_time_in_secs: float | Omit = omit,
        summarize_on_end: bool | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingCreateResponse:
        """
        Create a meeting for the given App ID.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          ai_config: The AI Config allows you to customize the behavior of meeting transcriptions and
              summaries

          live_stream_on_start: Specifies if the meeting should start getting livestreamed on start.

          persist_chat: If a meeting is set to persist_chat, meeting chat would remain for a week within
              the meeting space.

          record_on_start: Specifies if the meeting should start getting recorded as soon as someone joins
              the meeting.

          recording_config: Recording Configurations to be used for this meeting. This level of configs
              takes higher preference over App level configs on the RealtimeKit developer
              portal.

          session_keep_alive_time_in_secs: Time in seconds, for which a session remains active, after the last participant
              has left the meeting.

          summarize_on_end: Automatically generate summary of meetings using transcripts. Requires
              Transcriptions to be enabled, and can be retrieved via Webhooks or summary API.

          title: Title of the meeting

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
            f"/accounts/{account_id}/realtime/kit/{app_id}/meetings",
            body=maybe_transform(
                {
                    "ai_config": ai_config,
                    "live_stream_on_start": live_stream_on_start,
                    "persist_chat": persist_chat,
                    "record_on_start": record_on_start,
                    "recording_config": recording_config,
                    "session_keep_alive_time_in_secs": session_keep_alive_time_in_secs,
                    "summarize_on_end": summarize_on_end,
                    "title": title,
                },
                meeting_create_params.MeetingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeetingCreateResponse,
        )

    def add_participant(
        self,
        meeting_id: str,
        *,
        account_id: str,
        app_id: str,
        custom_participant_id: str,
        preset_name: str,
        name: Optional[str] | Omit = omit,
        picture: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingAddParticipantResponse:
        """
        Adds a participant to the given meeting ID.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          custom_participant_id: A unique participant ID. You must specify a unique ID for the participant, for
              example, UUID, email address, and so on.

          preset_name: Name of the preset to apply to this participant.

          name: (Optional) Name of the participant.

          picture: (Optional) A URL to a picture to be used for the participant.

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
            f"/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants",
            body=maybe_transform(
                {
                    "custom_participant_id": custom_participant_id,
                    "preset_name": preset_name,
                    "name": name,
                    "picture": picture,
                },
                meeting_add_participant_params.MeetingAddParticipantParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeetingAddParticipantResponse,
        )

    def delete_meeting_participant(
        self,
        participant_id: str,
        *,
        account_id: str,
        app_id: str,
        meeting_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingDeleteMeetingParticipantResponse:
        """
        Deletes a participant for the given meeting and participant ID.

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
        if not participant_id:
            raise ValueError(f"Expected a non-empty value for `participant_id` but received {participant_id!r}")
        return self._delete(
            f"/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants/{participant_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeetingDeleteMeetingParticipantResponse,
        )

    def edit_participant(
        self,
        participant_id: str,
        *,
        account_id: str,
        app_id: str,
        meeting_id: str,
        name: Optional[str] | Omit = omit,
        picture: Optional[str] | Omit = omit,
        preset_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingEditParticipantResponse:
        """
        Updates a participant's details for the given meeting and participant ID.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          name: (Optional) Name of the participant.

          picture: (Optional) A URL to a picture to be used for the participant.

          preset_name: (Optional) Name of the preset to apply to this participant.

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
        if not participant_id:
            raise ValueError(f"Expected a non-empty value for `participant_id` but received {participant_id!r}")
        return self._patch(
            f"/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants/{participant_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "picture": picture,
                    "preset_name": preset_name,
                },
                meeting_edit_participant_params.MeetingEditParticipantParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeetingEditParticipantResponse,
        )

    def get(
        self,
        app_id: str,
        *,
        account_id: str,
        end_time: Union[str, datetime] | Omit = omit,
        page_no: float | Omit = omit,
        per_page: float | Omit = omit,
        search: str | Omit = omit,
        start_time: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingGetResponse:
        """
        Returns all meetings for the given App ID.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          end_time: The end time range for which you want to retrieve the meetings. The time must be
              specified in ISO format.

          page_no: The page number from which you want your page search results to be displayed.

          per_page: Number of results per page

          search: The search query string. You can search using the meeting ID or title.

          start_time: The start time range for which you want to retrieve the meetings. The time must
              be specified in ISO format.

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
            f"/accounts/{account_id}/realtime/kit/{app_id}/meetings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_time": end_time,
                        "page_no": page_no,
                        "per_page": per_page,
                        "search": search,
                        "start_time": start_time,
                    },
                    meeting_get_params.MeetingGetParams,
                ),
            ),
            cast_to=MeetingGetResponse,
        )

    def get_meeting_by_id(
        self,
        meeting_id: str,
        *,
        account_id: str,
        app_id: str,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingGetMeetingByIDResponse:
        """
        Returns a meeting details in an App for the given meeting ID.

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
            f"/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"name": name}, meeting_get_meeting_by_id_params.MeetingGetMeetingByIDParams),
            ),
            cast_to=MeetingGetMeetingByIDResponse,
        )

    def get_meeting_participant(
        self,
        participant_id: str,
        *,
        account_id: str,
        app_id: str,
        meeting_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingGetMeetingParticipantResponse:
        """
        Returns a participant details for the given meeting and participant ID.

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
        if not participant_id:
            raise ValueError(f"Expected a non-empty value for `participant_id` but received {participant_id!r}")
        return self._get(
            f"/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants/{participant_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeetingGetMeetingParticipantResponse,
        )

    def get_meeting_participants(
        self,
        meeting_id: str,
        *,
        account_id: str,
        app_id: str,
        page_no: float | Omit = omit,
        per_page: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingGetMeetingParticipantsResponse:
        """
        Returns all participants detail for the given meeting ID.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          page_no: The page number from which you want your page search results to be displayed.

          per_page: Number of results per page

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
            f"/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants",
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
                    meeting_get_meeting_participants_params.MeetingGetMeetingParticipantsParams,
                ),
            ),
            cast_to=MeetingGetMeetingParticipantsResponse,
        )

    def refresh_participant_token(
        self,
        participant_id: str,
        *,
        account_id: str,
        app_id: str,
        meeting_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingRefreshParticipantTokenResponse:
        """
        Regenerates participant's authentication token for the given meeting and
        participant ID.

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
        if not participant_id:
            raise ValueError(f"Expected a non-empty value for `participant_id` but received {participant_id!r}")
        return self._post(
            f"/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants/{participant_id}/token",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeetingRefreshParticipantTokenResponse,
        )

    def replace_meeting_by_id(
        self,
        meeting_id: str,
        *,
        account_id: str,
        app_id: str,
        ai_config: meeting_replace_meeting_by_id_params.AIConfig | Omit = omit,
        live_stream_on_start: Optional[bool] | Omit = omit,
        persist_chat: bool | Omit = omit,
        record_on_start: Optional[bool] | Omit = omit,
        recording_config: meeting_replace_meeting_by_id_params.RecordingConfig | Omit = omit,
        session_keep_alive_time_in_secs: float | Omit = omit,
        summarize_on_end: bool | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingReplaceMeetingByIDResponse:
        """
        Replaces all the details for the given meeting ID.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          ai_config: The AI Config allows you to customize the behavior of meeting transcriptions and
              summaries

          live_stream_on_start: Specifies if the meeting should start getting livestreamed on start.

          persist_chat: If a meeting is set to persist_chat, meeting chat would remain for a week within
              the meeting space.

          record_on_start: Specifies if the meeting should start getting recorded as soon as someone joins
              the meeting.

          recording_config: Recording Configurations to be used for this meeting. This level of configs
              takes higher preference over App level configs on the RealtimeKit developer
              portal.

          session_keep_alive_time_in_secs: Time in seconds, for which a session remains active, after the last participant
              has left the meeting.

          summarize_on_end: Automatically generate summary of meetings using transcripts. Requires
              Transcriptions to be enabled, and can be retrieved via Webhooks or summary API.

          title: Title of the meeting

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
        return self._put(
            f"/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}",
            body=maybe_transform(
                {
                    "ai_config": ai_config,
                    "live_stream_on_start": live_stream_on_start,
                    "persist_chat": persist_chat,
                    "record_on_start": record_on_start,
                    "recording_config": recording_config,
                    "session_keep_alive_time_in_secs": session_keep_alive_time_in_secs,
                    "summarize_on_end": summarize_on_end,
                    "title": title,
                },
                meeting_replace_meeting_by_id_params.MeetingReplaceMeetingByIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeetingReplaceMeetingByIDResponse,
        )

    def update_meeting_by_id(
        self,
        meeting_id: str,
        *,
        account_id: str,
        app_id: str,
        ai_config: meeting_update_meeting_by_id_params.AIConfig | Omit = omit,
        live_stream_on_start: bool | Omit = omit,
        persist_chat: bool | Omit = omit,
        record_on_start: bool | Omit = omit,
        session_keep_alive_time_in_secs: float | Omit = omit,
        status: Literal["ACTIVE", "INACTIVE"] | Omit = omit,
        summarize_on_end: bool | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingUpdateMeetingByIDResponse:
        """
        Updates a meeting in an App for the given meeting ID.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          ai_config: The AI Config allows you to customize the behavior of meeting transcriptions and
              summaries

          live_stream_on_start: Specifies if the meeting should start getting livestreamed on start.

          persist_chat: If a meeting is updated to persist_chat, meeting chat would remain for a week
              within the meeting space.

          record_on_start: Specifies if the meeting should start getting recorded as soon as someone joins
              the meeting.

          session_keep_alive_time_in_secs: Time in seconds, for which a session remains active, after the last participant
              has left the meeting.

          status: Whether the meeting is `ACTIVE` or `INACTIVE`. Users will not be able to join an
              `INACTIVE` meeting.

          summarize_on_end: Automatically generate summary of meetings using transcripts. Requires
              Transcriptions to be enabled, and can be retrieved via Webhooks or summary API.

          title: Title of the meeting

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
        return self._patch(
            f"/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}",
            body=maybe_transform(
                {
                    "ai_config": ai_config,
                    "live_stream_on_start": live_stream_on_start,
                    "persist_chat": persist_chat,
                    "record_on_start": record_on_start,
                    "session_keep_alive_time_in_secs": session_keep_alive_time_in_secs,
                    "status": status,
                    "summarize_on_end": summarize_on_end,
                    "title": title,
                },
                meeting_update_meeting_by_id_params.MeetingUpdateMeetingByIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeetingUpdateMeetingByIDResponse,
        )


class AsyncMeetingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMeetingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMeetingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMeetingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncMeetingsResourceWithStreamingResponse(self)

    async def create(
        self,
        app_id: str,
        *,
        account_id: str,
        ai_config: meeting_create_params.AIConfig | Omit = omit,
        live_stream_on_start: Optional[bool] | Omit = omit,
        persist_chat: bool | Omit = omit,
        record_on_start: Optional[bool] | Omit = omit,
        recording_config: meeting_create_params.RecordingConfig | Omit = omit,
        session_keep_alive_time_in_secs: float | Omit = omit,
        summarize_on_end: bool | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingCreateResponse:
        """
        Create a meeting for the given App ID.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          ai_config: The AI Config allows you to customize the behavior of meeting transcriptions and
              summaries

          live_stream_on_start: Specifies if the meeting should start getting livestreamed on start.

          persist_chat: If a meeting is set to persist_chat, meeting chat would remain for a week within
              the meeting space.

          record_on_start: Specifies if the meeting should start getting recorded as soon as someone joins
              the meeting.

          recording_config: Recording Configurations to be used for this meeting. This level of configs
              takes higher preference over App level configs on the RealtimeKit developer
              portal.

          session_keep_alive_time_in_secs: Time in seconds, for which a session remains active, after the last participant
              has left the meeting.

          summarize_on_end: Automatically generate summary of meetings using transcripts. Requires
              Transcriptions to be enabled, and can be retrieved via Webhooks or summary API.

          title: Title of the meeting

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
            f"/accounts/{account_id}/realtime/kit/{app_id}/meetings",
            body=await async_maybe_transform(
                {
                    "ai_config": ai_config,
                    "live_stream_on_start": live_stream_on_start,
                    "persist_chat": persist_chat,
                    "record_on_start": record_on_start,
                    "recording_config": recording_config,
                    "session_keep_alive_time_in_secs": session_keep_alive_time_in_secs,
                    "summarize_on_end": summarize_on_end,
                    "title": title,
                },
                meeting_create_params.MeetingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeetingCreateResponse,
        )

    async def add_participant(
        self,
        meeting_id: str,
        *,
        account_id: str,
        app_id: str,
        custom_participant_id: str,
        preset_name: str,
        name: Optional[str] | Omit = omit,
        picture: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingAddParticipantResponse:
        """
        Adds a participant to the given meeting ID.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          custom_participant_id: A unique participant ID. You must specify a unique ID for the participant, for
              example, UUID, email address, and so on.

          preset_name: Name of the preset to apply to this participant.

          name: (Optional) Name of the participant.

          picture: (Optional) A URL to a picture to be used for the participant.

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
            f"/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants",
            body=await async_maybe_transform(
                {
                    "custom_participant_id": custom_participant_id,
                    "preset_name": preset_name,
                    "name": name,
                    "picture": picture,
                },
                meeting_add_participant_params.MeetingAddParticipantParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeetingAddParticipantResponse,
        )

    async def delete_meeting_participant(
        self,
        participant_id: str,
        *,
        account_id: str,
        app_id: str,
        meeting_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingDeleteMeetingParticipantResponse:
        """
        Deletes a participant for the given meeting and participant ID.

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
        if not participant_id:
            raise ValueError(f"Expected a non-empty value for `participant_id` but received {participant_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants/{participant_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeetingDeleteMeetingParticipantResponse,
        )

    async def edit_participant(
        self,
        participant_id: str,
        *,
        account_id: str,
        app_id: str,
        meeting_id: str,
        name: Optional[str] | Omit = omit,
        picture: Optional[str] | Omit = omit,
        preset_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingEditParticipantResponse:
        """
        Updates a participant's details for the given meeting and participant ID.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          name: (Optional) Name of the participant.

          picture: (Optional) A URL to a picture to be used for the participant.

          preset_name: (Optional) Name of the preset to apply to this participant.

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
        if not participant_id:
            raise ValueError(f"Expected a non-empty value for `participant_id` but received {participant_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants/{participant_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "picture": picture,
                    "preset_name": preset_name,
                },
                meeting_edit_participant_params.MeetingEditParticipantParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeetingEditParticipantResponse,
        )

    async def get(
        self,
        app_id: str,
        *,
        account_id: str,
        end_time: Union[str, datetime] | Omit = omit,
        page_no: float | Omit = omit,
        per_page: float | Omit = omit,
        search: str | Omit = omit,
        start_time: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingGetResponse:
        """
        Returns all meetings for the given App ID.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          end_time: The end time range for which you want to retrieve the meetings. The time must be
              specified in ISO format.

          page_no: The page number from which you want your page search results to be displayed.

          per_page: Number of results per page

          search: The search query string. You can search using the meeting ID or title.

          start_time: The start time range for which you want to retrieve the meetings. The time must
              be specified in ISO format.

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
            f"/accounts/{account_id}/realtime/kit/{app_id}/meetings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_time": end_time,
                        "page_no": page_no,
                        "per_page": per_page,
                        "search": search,
                        "start_time": start_time,
                    },
                    meeting_get_params.MeetingGetParams,
                ),
            ),
            cast_to=MeetingGetResponse,
        )

    async def get_meeting_by_id(
        self,
        meeting_id: str,
        *,
        account_id: str,
        app_id: str,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingGetMeetingByIDResponse:
        """
        Returns a meeting details in an App for the given meeting ID.

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
            f"/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"name": name}, meeting_get_meeting_by_id_params.MeetingGetMeetingByIDParams
                ),
            ),
            cast_to=MeetingGetMeetingByIDResponse,
        )

    async def get_meeting_participant(
        self,
        participant_id: str,
        *,
        account_id: str,
        app_id: str,
        meeting_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingGetMeetingParticipantResponse:
        """
        Returns a participant details for the given meeting and participant ID.

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
        if not participant_id:
            raise ValueError(f"Expected a non-empty value for `participant_id` but received {participant_id!r}")
        return await self._get(
            f"/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants/{participant_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeetingGetMeetingParticipantResponse,
        )

    async def get_meeting_participants(
        self,
        meeting_id: str,
        *,
        account_id: str,
        app_id: str,
        page_no: float | Omit = omit,
        per_page: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingGetMeetingParticipantsResponse:
        """
        Returns all participants detail for the given meeting ID.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          page_no: The page number from which you want your page search results to be displayed.

          per_page: Number of results per page

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
            f"/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants",
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
                    meeting_get_meeting_participants_params.MeetingGetMeetingParticipantsParams,
                ),
            ),
            cast_to=MeetingGetMeetingParticipantsResponse,
        )

    async def refresh_participant_token(
        self,
        participant_id: str,
        *,
        account_id: str,
        app_id: str,
        meeting_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingRefreshParticipantTokenResponse:
        """
        Regenerates participant's authentication token for the given meeting and
        participant ID.

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
        if not participant_id:
            raise ValueError(f"Expected a non-empty value for `participant_id` but received {participant_id!r}")
        return await self._post(
            f"/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants/{participant_id}/token",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeetingRefreshParticipantTokenResponse,
        )

    async def replace_meeting_by_id(
        self,
        meeting_id: str,
        *,
        account_id: str,
        app_id: str,
        ai_config: meeting_replace_meeting_by_id_params.AIConfig | Omit = omit,
        live_stream_on_start: Optional[bool] | Omit = omit,
        persist_chat: bool | Omit = omit,
        record_on_start: Optional[bool] | Omit = omit,
        recording_config: meeting_replace_meeting_by_id_params.RecordingConfig | Omit = omit,
        session_keep_alive_time_in_secs: float | Omit = omit,
        summarize_on_end: bool | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingReplaceMeetingByIDResponse:
        """
        Replaces all the details for the given meeting ID.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          ai_config: The AI Config allows you to customize the behavior of meeting transcriptions and
              summaries

          live_stream_on_start: Specifies if the meeting should start getting livestreamed on start.

          persist_chat: If a meeting is set to persist_chat, meeting chat would remain for a week within
              the meeting space.

          record_on_start: Specifies if the meeting should start getting recorded as soon as someone joins
              the meeting.

          recording_config: Recording Configurations to be used for this meeting. This level of configs
              takes higher preference over App level configs on the RealtimeKit developer
              portal.

          session_keep_alive_time_in_secs: Time in seconds, for which a session remains active, after the last participant
              has left the meeting.

          summarize_on_end: Automatically generate summary of meetings using transcripts. Requires
              Transcriptions to be enabled, and can be retrieved via Webhooks or summary API.

          title: Title of the meeting

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
        return await self._put(
            f"/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}",
            body=await async_maybe_transform(
                {
                    "ai_config": ai_config,
                    "live_stream_on_start": live_stream_on_start,
                    "persist_chat": persist_chat,
                    "record_on_start": record_on_start,
                    "recording_config": recording_config,
                    "session_keep_alive_time_in_secs": session_keep_alive_time_in_secs,
                    "summarize_on_end": summarize_on_end,
                    "title": title,
                },
                meeting_replace_meeting_by_id_params.MeetingReplaceMeetingByIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeetingReplaceMeetingByIDResponse,
        )

    async def update_meeting_by_id(
        self,
        meeting_id: str,
        *,
        account_id: str,
        app_id: str,
        ai_config: meeting_update_meeting_by_id_params.AIConfig | Omit = omit,
        live_stream_on_start: bool | Omit = omit,
        persist_chat: bool | Omit = omit,
        record_on_start: bool | Omit = omit,
        session_keep_alive_time_in_secs: float | Omit = omit,
        status: Literal["ACTIVE", "INACTIVE"] | Omit = omit,
        summarize_on_end: bool | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingUpdateMeetingByIDResponse:
        """
        Updates a meeting in an App for the given meeting ID.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          ai_config: The AI Config allows you to customize the behavior of meeting transcriptions and
              summaries

          live_stream_on_start: Specifies if the meeting should start getting livestreamed on start.

          persist_chat: If a meeting is updated to persist_chat, meeting chat would remain for a week
              within the meeting space.

          record_on_start: Specifies if the meeting should start getting recorded as soon as someone joins
              the meeting.

          session_keep_alive_time_in_secs: Time in seconds, for which a session remains active, after the last participant
              has left the meeting.

          status: Whether the meeting is `ACTIVE` or `INACTIVE`. Users will not be able to join an
              `INACTIVE` meeting.

          summarize_on_end: Automatically generate summary of meetings using transcripts. Requires
              Transcriptions to be enabled, and can be retrieved via Webhooks or summary API.

          title: Title of the meeting

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
        return await self._patch(
            f"/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}",
            body=await async_maybe_transform(
                {
                    "ai_config": ai_config,
                    "live_stream_on_start": live_stream_on_start,
                    "persist_chat": persist_chat,
                    "record_on_start": record_on_start,
                    "session_keep_alive_time_in_secs": session_keep_alive_time_in_secs,
                    "status": status,
                    "summarize_on_end": summarize_on_end,
                    "title": title,
                },
                meeting_update_meeting_by_id_params.MeetingUpdateMeetingByIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeetingUpdateMeetingByIDResponse,
        )


class MeetingsResourceWithRawResponse:
    def __init__(self, meetings: MeetingsResource) -> None:
        self._meetings = meetings

        self.create = to_raw_response_wrapper(
            meetings.create,
        )
        self.add_participant = to_raw_response_wrapper(
            meetings.add_participant,
        )
        self.delete_meeting_participant = to_raw_response_wrapper(
            meetings.delete_meeting_participant,
        )
        self.edit_participant = to_raw_response_wrapper(
            meetings.edit_participant,
        )
        self.get = to_raw_response_wrapper(
            meetings.get,
        )
        self.get_meeting_by_id = to_raw_response_wrapper(
            meetings.get_meeting_by_id,
        )
        self.get_meeting_participant = to_raw_response_wrapper(
            meetings.get_meeting_participant,
        )
        self.get_meeting_participants = to_raw_response_wrapper(
            meetings.get_meeting_participants,
        )
        self.refresh_participant_token = to_raw_response_wrapper(
            meetings.refresh_participant_token,
        )
        self.replace_meeting_by_id = to_raw_response_wrapper(
            meetings.replace_meeting_by_id,
        )
        self.update_meeting_by_id = to_raw_response_wrapper(
            meetings.update_meeting_by_id,
        )


class AsyncMeetingsResourceWithRawResponse:
    def __init__(self, meetings: AsyncMeetingsResource) -> None:
        self._meetings = meetings

        self.create = async_to_raw_response_wrapper(
            meetings.create,
        )
        self.add_participant = async_to_raw_response_wrapper(
            meetings.add_participant,
        )
        self.delete_meeting_participant = async_to_raw_response_wrapper(
            meetings.delete_meeting_participant,
        )
        self.edit_participant = async_to_raw_response_wrapper(
            meetings.edit_participant,
        )
        self.get = async_to_raw_response_wrapper(
            meetings.get,
        )
        self.get_meeting_by_id = async_to_raw_response_wrapper(
            meetings.get_meeting_by_id,
        )
        self.get_meeting_participant = async_to_raw_response_wrapper(
            meetings.get_meeting_participant,
        )
        self.get_meeting_participants = async_to_raw_response_wrapper(
            meetings.get_meeting_participants,
        )
        self.refresh_participant_token = async_to_raw_response_wrapper(
            meetings.refresh_participant_token,
        )
        self.replace_meeting_by_id = async_to_raw_response_wrapper(
            meetings.replace_meeting_by_id,
        )
        self.update_meeting_by_id = async_to_raw_response_wrapper(
            meetings.update_meeting_by_id,
        )


class MeetingsResourceWithStreamingResponse:
    def __init__(self, meetings: MeetingsResource) -> None:
        self._meetings = meetings

        self.create = to_streamed_response_wrapper(
            meetings.create,
        )
        self.add_participant = to_streamed_response_wrapper(
            meetings.add_participant,
        )
        self.delete_meeting_participant = to_streamed_response_wrapper(
            meetings.delete_meeting_participant,
        )
        self.edit_participant = to_streamed_response_wrapper(
            meetings.edit_participant,
        )
        self.get = to_streamed_response_wrapper(
            meetings.get,
        )
        self.get_meeting_by_id = to_streamed_response_wrapper(
            meetings.get_meeting_by_id,
        )
        self.get_meeting_participant = to_streamed_response_wrapper(
            meetings.get_meeting_participant,
        )
        self.get_meeting_participants = to_streamed_response_wrapper(
            meetings.get_meeting_participants,
        )
        self.refresh_participant_token = to_streamed_response_wrapper(
            meetings.refresh_participant_token,
        )
        self.replace_meeting_by_id = to_streamed_response_wrapper(
            meetings.replace_meeting_by_id,
        )
        self.update_meeting_by_id = to_streamed_response_wrapper(
            meetings.update_meeting_by_id,
        )


class AsyncMeetingsResourceWithStreamingResponse:
    def __init__(self, meetings: AsyncMeetingsResource) -> None:
        self._meetings = meetings

        self.create = async_to_streamed_response_wrapper(
            meetings.create,
        )
        self.add_participant = async_to_streamed_response_wrapper(
            meetings.add_participant,
        )
        self.delete_meeting_participant = async_to_streamed_response_wrapper(
            meetings.delete_meeting_participant,
        )
        self.edit_participant = async_to_streamed_response_wrapper(
            meetings.edit_participant,
        )
        self.get = async_to_streamed_response_wrapper(
            meetings.get,
        )
        self.get_meeting_by_id = async_to_streamed_response_wrapper(
            meetings.get_meeting_by_id,
        )
        self.get_meeting_participant = async_to_streamed_response_wrapper(
            meetings.get_meeting_participant,
        )
        self.get_meeting_participants = async_to_streamed_response_wrapper(
            meetings.get_meeting_participants,
        )
        self.refresh_participant_token = async_to_streamed_response_wrapper(
            meetings.refresh_participant_token,
        )
        self.replace_meeting_by_id = async_to_streamed_response_wrapper(
            meetings.replace_meeting_by_id,
        )
        self.update_meeting_by_id = async_to_streamed_response_wrapper(
            meetings.update_meeting_by_id,
        )
