# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
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
    session_get_sessions_params,
    session_get_session_details_params,
    session_get_session_participants_params,
    session_get_session_participant_details_params,
    session_get_participant_data_from_peer_id_params,
)
from ...types.realtime_kit.session_get_sessions_response import SessionGetSessionsResponse
from ...types.realtime_kit.session_get_session_chat_response import SessionGetSessionChatResponse
from ...types.realtime_kit.session_get_session_details_response import SessionGetSessionDetailsResponse
from ...types.realtime_kit.session_get_session_summary_response import SessionGetSessionSummaryResponse
from ...types.realtime_kit.session_get_session_transcripts_response import SessionGetSessionTranscriptsResponse
from ...types.realtime_kit.session_get_session_participants_response import SessionGetSessionParticipantsResponse
from ...types.realtime_kit.session_get_session_participant_details_response import (
    SessionGetSessionParticipantDetailsResponse,
)
from ...types.realtime_kit.session_get_participant_data_from_peer_id_response import (
    SessionGetParticipantDataFromPeerIDResponse,
)

__all__ = ["SessionsResource", "AsyncSessionsResource"]


class SessionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SessionsResourceWithStreamingResponse(self)

    def generate_summary_of_transcripts(
        self,
        session_id: str,
        *,
        account_id: str,
        app_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Trigger Summary generation of Transcripts for the session ID.

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
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/summary",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_participant_data_from_peer_id(
        self,
        peer_id: str,
        *,
        account_id: str,
        app_id: str,
        filters: Literal["device_info", "ip_information", "precall_network_information", "events", "quality_stats"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionGetParticipantDataFromPeerIDResponse:
        """
        Returns details of the given peer ID along with call statistics for the given
        session ID.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          filters: Comma separated list of filters to apply. Note that there must be no spaces
              between the filters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not peer_id:
            raise ValueError(f"Expected a non-empty value for `peer_id` but received {peer_id!r}")
        return self._get(
            f"/accounts/{account_id}/realtime/kit/{app_id}/sessions/peer-report/{peer_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"filters": filters},
                    session_get_participant_data_from_peer_id_params.SessionGetParticipantDataFromPeerIDParams,
                ),
            ),
            cast_to=SessionGetParticipantDataFromPeerIDResponse,
        )

    def get_session_chat(
        self,
        session_id: str,
        *,
        account_id: str,
        app_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionGetSessionChatResponse:
        """
        Returns a URL to download all chat messages of the session ID in CSV format.

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
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/chat",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionGetSessionChatResponse,
        )

    def get_session_details(
        self,
        session_id: str,
        *,
        account_id: str,
        app_id: str,
        include_breakout_rooms: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionGetSessionDetailsResponse:
        """
        Returns data of the given session ID including recording details.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          include_breakout_rooms: List all breakout rooms

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"include_breakout_rooms": include_breakout_rooms},
                    session_get_session_details_params.SessionGetSessionDetailsParams,
                ),
            ),
            cast_to=SessionGetSessionDetailsResponse,
        )

    def get_session_participant_details(
        self,
        participant_id: str,
        *,
        account_id: str,
        app_id: str,
        session_id: str,
        filters: Literal["device_info", "ip_information", "precall_network_information", "events", "quality_stats"]
        | Omit = omit,
        include_peer_events: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionGetSessionParticipantDetailsResponse:
        """
        Returns details of the given participant ID along with call statistics for the
        given session ID.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          filters: Comma separated list of filters to apply. Note that there must be no spaces
              between the filters.

          include_peer_events: if true, response includes all the peer events of participant.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not participant_id:
            raise ValueError(f"Expected a non-empty value for `participant_id` but received {participant_id!r}")
        return self._get(
            f"/accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/participants/{participant_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filters": filters,
                        "include_peer_events": include_peer_events,
                    },
                    session_get_session_participant_details_params.SessionGetSessionParticipantDetailsParams,
                ),
            ),
            cast_to=SessionGetSessionParticipantDetailsResponse,
        )

    def get_session_participants(
        self,
        session_id: str,
        *,
        account_id: str,
        app_id: str,
        include_peer_events: bool | Omit = omit,
        page_no: float | Omit = omit,
        per_page: float | Omit = omit,
        search: str | Omit = omit,
        sort_by: Literal["joinedAt", "duration"] | Omit = omit,
        sort_order: Literal["ASC", "DESC"] | Omit = omit,
        view: Literal["raw", "consolidated"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionGetSessionParticipantsResponse:
        """
        Returns a list of participants for the given session ID.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          include_peer_events: if true, response includes all the peer events of participants.

          page_no: The page number from which you want your page search results to be displayed.

          per_page: Number of results per page

          search: The search query string. You can search using the meeting ID or title.

          view: In breakout room sessions, the view parameter can be set to `raw` for session
              specific duration for participants or `consolidated` to accumulate breakout room
              durations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/participants",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_peer_events": include_peer_events,
                        "page_no": page_no,
                        "per_page": per_page,
                        "search": search,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "view": view,
                    },
                    session_get_session_participants_params.SessionGetSessionParticipantsParams,
                ),
            ),
            cast_to=SessionGetSessionParticipantsResponse,
        )

    def get_session_summary(
        self,
        session_id: str,
        *,
        account_id: str,
        app_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionGetSessionSummaryResponse:
        """
        Returns a Summary URL to download the Summary of Transcripts for the session ID
        as plain text.

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
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/summary",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionGetSessionSummaryResponse,
        )

    def get_session_transcripts(
        self,
        session_id: str,
        *,
        account_id: str,
        app_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionGetSessionTranscriptsResponse:
        """
        Returns a URL to download the transcript for the session ID in CSV format.

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
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/transcript",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionGetSessionTranscriptsResponse,
        )

    def get_sessions(
        self,
        app_id: str,
        *,
        account_id: str,
        associated_id: str | Omit = omit,
        end_time: Union[str, datetime] | Omit = omit,
        page_no: float | Omit = omit,
        participants: str | Omit = omit,
        per_page: float | Omit = omit,
        search: str | Omit = omit,
        sort_by: Literal["minutesConsumed", "createdAt"] | Omit = omit,
        sort_order: Literal["ASC", "DESC"] | Omit = omit,
        start_time: Union[str, datetime] | Omit = omit,
        status: Literal["LIVE", "ENDED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionGetSessionsResponse:
        """
        Returns details of all sessions of an App.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          associated_id: ID of the meeting that sessions should be associated with

          end_time: The end time range for which you want to retrieve the meetings. The time must be
              specified in ISO format.

          page_no: The page number from which you want your page search results to be displayed.

          per_page: Number of results per page

          search: Search string that matches sessions based on meeting title, meeting ID, and
              session ID

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
            f"/accounts/{account_id}/realtime/kit/{app_id}/sessions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "associated_id": associated_id,
                        "end_time": end_time,
                        "page_no": page_no,
                        "participants": participants,
                        "per_page": per_page,
                        "search": search,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "start_time": start_time,
                        "status": status,
                    },
                    session_get_sessions_params.SessionGetSessionsParams,
                ),
            ),
            cast_to=SessionGetSessionsResponse,
        )


class AsyncSessionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSessionsResourceWithStreamingResponse(self)

    async def generate_summary_of_transcripts(
        self,
        session_id: str,
        *,
        account_id: str,
        app_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Trigger Summary generation of Transcripts for the session ID.

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
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/summary",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_participant_data_from_peer_id(
        self,
        peer_id: str,
        *,
        account_id: str,
        app_id: str,
        filters: Literal["device_info", "ip_information", "precall_network_information", "events", "quality_stats"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionGetParticipantDataFromPeerIDResponse:
        """
        Returns details of the given peer ID along with call statistics for the given
        session ID.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          filters: Comma separated list of filters to apply. Note that there must be no spaces
              between the filters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not peer_id:
            raise ValueError(f"Expected a non-empty value for `peer_id` but received {peer_id!r}")
        return await self._get(
            f"/accounts/{account_id}/realtime/kit/{app_id}/sessions/peer-report/{peer_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"filters": filters},
                    session_get_participant_data_from_peer_id_params.SessionGetParticipantDataFromPeerIDParams,
                ),
            ),
            cast_to=SessionGetParticipantDataFromPeerIDResponse,
        )

    async def get_session_chat(
        self,
        session_id: str,
        *,
        account_id: str,
        app_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionGetSessionChatResponse:
        """
        Returns a URL to download all chat messages of the session ID in CSV format.

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
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/chat",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionGetSessionChatResponse,
        )

    async def get_session_details(
        self,
        session_id: str,
        *,
        account_id: str,
        app_id: str,
        include_breakout_rooms: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionGetSessionDetailsResponse:
        """
        Returns data of the given session ID including recording details.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          include_breakout_rooms: List all breakout rooms

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_breakout_rooms": include_breakout_rooms},
                    session_get_session_details_params.SessionGetSessionDetailsParams,
                ),
            ),
            cast_to=SessionGetSessionDetailsResponse,
        )

    async def get_session_participant_details(
        self,
        participant_id: str,
        *,
        account_id: str,
        app_id: str,
        session_id: str,
        filters: Literal["device_info", "ip_information", "precall_network_information", "events", "quality_stats"]
        | Omit = omit,
        include_peer_events: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionGetSessionParticipantDetailsResponse:
        """
        Returns details of the given participant ID along with call statistics for the
        given session ID.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          filters: Comma separated list of filters to apply. Note that there must be no spaces
              between the filters.

          include_peer_events: if true, response includes all the peer events of participant.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not participant_id:
            raise ValueError(f"Expected a non-empty value for `participant_id` but received {participant_id!r}")
        return await self._get(
            f"/accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/participants/{participant_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filters": filters,
                        "include_peer_events": include_peer_events,
                    },
                    session_get_session_participant_details_params.SessionGetSessionParticipantDetailsParams,
                ),
            ),
            cast_to=SessionGetSessionParticipantDetailsResponse,
        )

    async def get_session_participants(
        self,
        session_id: str,
        *,
        account_id: str,
        app_id: str,
        include_peer_events: bool | Omit = omit,
        page_no: float | Omit = omit,
        per_page: float | Omit = omit,
        search: str | Omit = omit,
        sort_by: Literal["joinedAt", "duration"] | Omit = omit,
        sort_order: Literal["ASC", "DESC"] | Omit = omit,
        view: Literal["raw", "consolidated"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionGetSessionParticipantsResponse:
        """
        Returns a list of participants for the given session ID.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          include_peer_events: if true, response includes all the peer events of participants.

          page_no: The page number from which you want your page search results to be displayed.

          per_page: Number of results per page

          search: The search query string. You can search using the meeting ID or title.

          view: In breakout room sessions, the view parameter can be set to `raw` for session
              specific duration for participants or `consolidated` to accumulate breakout room
              durations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/participants",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include_peer_events": include_peer_events,
                        "page_no": page_no,
                        "per_page": per_page,
                        "search": search,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "view": view,
                    },
                    session_get_session_participants_params.SessionGetSessionParticipantsParams,
                ),
            ),
            cast_to=SessionGetSessionParticipantsResponse,
        )

    async def get_session_summary(
        self,
        session_id: str,
        *,
        account_id: str,
        app_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionGetSessionSummaryResponse:
        """
        Returns a Summary URL to download the Summary of Transcripts for the session ID
        as plain text.

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
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/summary",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionGetSessionSummaryResponse,
        )

    async def get_session_transcripts(
        self,
        session_id: str,
        *,
        account_id: str,
        app_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionGetSessionTranscriptsResponse:
        """
        Returns a URL to download the transcript for the session ID in CSV format.

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
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/transcript",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionGetSessionTranscriptsResponse,
        )

    async def get_sessions(
        self,
        app_id: str,
        *,
        account_id: str,
        associated_id: str | Omit = omit,
        end_time: Union[str, datetime] | Omit = omit,
        page_no: float | Omit = omit,
        participants: str | Omit = omit,
        per_page: float | Omit = omit,
        search: str | Omit = omit,
        sort_by: Literal["minutesConsumed", "createdAt"] | Omit = omit,
        sort_order: Literal["ASC", "DESC"] | Omit = omit,
        start_time: Union[str, datetime] | Omit = omit,
        status: Literal["LIVE", "ENDED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionGetSessionsResponse:
        """
        Returns details of all sessions of an App.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          associated_id: ID of the meeting that sessions should be associated with

          end_time: The end time range for which you want to retrieve the meetings. The time must be
              specified in ISO format.

          page_no: The page number from which you want your page search results to be displayed.

          per_page: Number of results per page

          search: Search string that matches sessions based on meeting title, meeting ID, and
              session ID

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
            f"/accounts/{account_id}/realtime/kit/{app_id}/sessions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "associated_id": associated_id,
                        "end_time": end_time,
                        "page_no": page_no,
                        "participants": participants,
                        "per_page": per_page,
                        "search": search,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "start_time": start_time,
                        "status": status,
                    },
                    session_get_sessions_params.SessionGetSessionsParams,
                ),
            ),
            cast_to=SessionGetSessionsResponse,
        )


class SessionsResourceWithRawResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.generate_summary_of_transcripts = to_raw_response_wrapper(
            sessions.generate_summary_of_transcripts,
        )
        self.get_participant_data_from_peer_id = to_raw_response_wrapper(
            sessions.get_participant_data_from_peer_id,
        )
        self.get_session_chat = to_raw_response_wrapper(
            sessions.get_session_chat,
        )
        self.get_session_details = to_raw_response_wrapper(
            sessions.get_session_details,
        )
        self.get_session_participant_details = to_raw_response_wrapper(
            sessions.get_session_participant_details,
        )
        self.get_session_participants = to_raw_response_wrapper(
            sessions.get_session_participants,
        )
        self.get_session_summary = to_raw_response_wrapper(
            sessions.get_session_summary,
        )
        self.get_session_transcripts = to_raw_response_wrapper(
            sessions.get_session_transcripts,
        )
        self.get_sessions = to_raw_response_wrapper(
            sessions.get_sessions,
        )


class AsyncSessionsResourceWithRawResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.generate_summary_of_transcripts = async_to_raw_response_wrapper(
            sessions.generate_summary_of_transcripts,
        )
        self.get_participant_data_from_peer_id = async_to_raw_response_wrapper(
            sessions.get_participant_data_from_peer_id,
        )
        self.get_session_chat = async_to_raw_response_wrapper(
            sessions.get_session_chat,
        )
        self.get_session_details = async_to_raw_response_wrapper(
            sessions.get_session_details,
        )
        self.get_session_participant_details = async_to_raw_response_wrapper(
            sessions.get_session_participant_details,
        )
        self.get_session_participants = async_to_raw_response_wrapper(
            sessions.get_session_participants,
        )
        self.get_session_summary = async_to_raw_response_wrapper(
            sessions.get_session_summary,
        )
        self.get_session_transcripts = async_to_raw_response_wrapper(
            sessions.get_session_transcripts,
        )
        self.get_sessions = async_to_raw_response_wrapper(
            sessions.get_sessions,
        )


class SessionsResourceWithStreamingResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.generate_summary_of_transcripts = to_streamed_response_wrapper(
            sessions.generate_summary_of_transcripts,
        )
        self.get_participant_data_from_peer_id = to_streamed_response_wrapper(
            sessions.get_participant_data_from_peer_id,
        )
        self.get_session_chat = to_streamed_response_wrapper(
            sessions.get_session_chat,
        )
        self.get_session_details = to_streamed_response_wrapper(
            sessions.get_session_details,
        )
        self.get_session_participant_details = to_streamed_response_wrapper(
            sessions.get_session_participant_details,
        )
        self.get_session_participants = to_streamed_response_wrapper(
            sessions.get_session_participants,
        )
        self.get_session_summary = to_streamed_response_wrapper(
            sessions.get_session_summary,
        )
        self.get_session_transcripts = to_streamed_response_wrapper(
            sessions.get_session_transcripts,
        )
        self.get_sessions = to_streamed_response_wrapper(
            sessions.get_sessions,
        )


class AsyncSessionsResourceWithStreamingResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.generate_summary_of_transcripts = async_to_streamed_response_wrapper(
            sessions.generate_summary_of_transcripts,
        )
        self.get_participant_data_from_peer_id = async_to_streamed_response_wrapper(
            sessions.get_participant_data_from_peer_id,
        )
        self.get_session_chat = async_to_streamed_response_wrapper(
            sessions.get_session_chat,
        )
        self.get_session_details = async_to_streamed_response_wrapper(
            sessions.get_session_details,
        )
        self.get_session_participant_details = async_to_streamed_response_wrapper(
            sessions.get_session_participant_details,
        )
        self.get_session_participants = async_to_streamed_response_wrapper(
            sessions.get_session_participants,
        )
        self.get_session_summary = async_to_streamed_response_wrapper(
            sessions.get_session_summary,
        )
        self.get_session_transcripts = async_to_streamed_response_wrapper(
            sessions.get_session_transcripts,
        )
        self.get_sessions = async_to_streamed_response_wrapper(
            sessions.get_sessions,
        )
