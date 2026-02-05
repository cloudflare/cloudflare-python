# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.realtime_kit import active_session_create_poll_params, active_session_kick_participants_params
from ...types.realtime_kit.active_session_create_poll_response import ActiveSessionCreatePollResponse
from ...types.realtime_kit.active_session_kick_participants_response import ActiveSessionKickParticipantsResponse
from ...types.realtime_kit.active_session_get_active_session_response import ActiveSessionGetActiveSessionResponse
from ...types.realtime_kit.active_session_kick_all_participants_response import ActiveSessionKickAllParticipantsResponse

__all__ = ["ActiveSessionResource", "AsyncActiveSessionResource"]


class ActiveSessionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ActiveSessionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ActiveSessionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActiveSessionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ActiveSessionResourceWithStreamingResponse(self)

    def create_poll(
        self,
        meeting_id: str,
        *,
        account_id: str,
        app_id: str,
        options: SequenceNotStr[str],
        question: str,
        anonymous: bool | Omit = omit,
        hide_votes: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActiveSessionCreatePollResponse:
        """
        Creates a new poll in an active session for the given meeting ID.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          options: Different options for the question

          question: Question of the poll

          anonymous: if voters on a poll are anonymous

          hide_votes: if votes on an option are visible before a person votes

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
            f"/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-session/poll",
            body=maybe_transform(
                {
                    "options": options,
                    "question": question,
                    "anonymous": anonymous,
                    "hide_votes": hide_votes,
                },
                active_session_create_poll_params.ActiveSessionCreatePollParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActiveSessionCreatePollResponse,
        )

    def get_active_session(
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
    ) -> ActiveSessionGetActiveSessionResponse:
        """
        Returns details of an ongoing active session for the given meeting ID.

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
            f"/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-session",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActiveSessionGetActiveSessionResponse,
        )

    def kick_all_participants(
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
    ) -> ActiveSessionKickAllParticipantsResponse:
        """
        Kicks all participants from an active session for the given meeting ID.

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
            f"/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-session/kick-all",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActiveSessionKickAllParticipantsResponse,
        )

    def kick_participants(
        self,
        meeting_id: str,
        *,
        account_id: str,
        app_id: str,
        custom_participant_ids: SequenceNotStr[str],
        participant_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActiveSessionKickParticipantsResponse:
        """
        Kicks one or more participants from an active session using user ID or custom
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
        return self._post(
            f"/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-session/kick",
            body=maybe_transform(
                {
                    "custom_participant_ids": custom_participant_ids,
                    "participant_ids": participant_ids,
                },
                active_session_kick_participants_params.ActiveSessionKickParticipantsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActiveSessionKickParticipantsResponse,
        )


class AsyncActiveSessionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncActiveSessionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncActiveSessionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActiveSessionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncActiveSessionResourceWithStreamingResponse(self)

    async def create_poll(
        self,
        meeting_id: str,
        *,
        account_id: str,
        app_id: str,
        options: SequenceNotStr[str],
        question: str,
        anonymous: bool | Omit = omit,
        hide_votes: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActiveSessionCreatePollResponse:
        """
        Creates a new poll in an active session for the given meeting ID.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          options: Different options for the question

          question: Question of the poll

          anonymous: if voters on a poll are anonymous

          hide_votes: if votes on an option are visible before a person votes

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
            f"/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-session/poll",
            body=await async_maybe_transform(
                {
                    "options": options,
                    "question": question,
                    "anonymous": anonymous,
                    "hide_votes": hide_votes,
                },
                active_session_create_poll_params.ActiveSessionCreatePollParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActiveSessionCreatePollResponse,
        )

    async def get_active_session(
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
    ) -> ActiveSessionGetActiveSessionResponse:
        """
        Returns details of an ongoing active session for the given meeting ID.

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
            f"/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-session",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActiveSessionGetActiveSessionResponse,
        )

    async def kick_all_participants(
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
    ) -> ActiveSessionKickAllParticipantsResponse:
        """
        Kicks all participants from an active session for the given meeting ID.

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
            f"/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-session/kick-all",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActiveSessionKickAllParticipantsResponse,
        )

    async def kick_participants(
        self,
        meeting_id: str,
        *,
        account_id: str,
        app_id: str,
        custom_participant_ids: SequenceNotStr[str],
        participant_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActiveSessionKickParticipantsResponse:
        """
        Kicks one or more participants from an active session using user ID or custom
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
        return await self._post(
            f"/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-session/kick",
            body=await async_maybe_transform(
                {
                    "custom_participant_ids": custom_participant_ids,
                    "participant_ids": participant_ids,
                },
                active_session_kick_participants_params.ActiveSessionKickParticipantsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActiveSessionKickParticipantsResponse,
        )


class ActiveSessionResourceWithRawResponse:
    def __init__(self, active_session: ActiveSessionResource) -> None:
        self._active_session = active_session

        self.create_poll = to_raw_response_wrapper(
            active_session.create_poll,
        )
        self.get_active_session = to_raw_response_wrapper(
            active_session.get_active_session,
        )
        self.kick_all_participants = to_raw_response_wrapper(
            active_session.kick_all_participants,
        )
        self.kick_participants = to_raw_response_wrapper(
            active_session.kick_participants,
        )


class AsyncActiveSessionResourceWithRawResponse:
    def __init__(self, active_session: AsyncActiveSessionResource) -> None:
        self._active_session = active_session

        self.create_poll = async_to_raw_response_wrapper(
            active_session.create_poll,
        )
        self.get_active_session = async_to_raw_response_wrapper(
            active_session.get_active_session,
        )
        self.kick_all_participants = async_to_raw_response_wrapper(
            active_session.kick_all_participants,
        )
        self.kick_participants = async_to_raw_response_wrapper(
            active_session.kick_participants,
        )


class ActiveSessionResourceWithStreamingResponse:
    def __init__(self, active_session: ActiveSessionResource) -> None:
        self._active_session = active_session

        self.create_poll = to_streamed_response_wrapper(
            active_session.create_poll,
        )
        self.get_active_session = to_streamed_response_wrapper(
            active_session.get_active_session,
        )
        self.kick_all_participants = to_streamed_response_wrapper(
            active_session.kick_all_participants,
        )
        self.kick_participants = to_streamed_response_wrapper(
            active_session.kick_participants,
        )


class AsyncActiveSessionResourceWithStreamingResponse:
    def __init__(self, active_session: AsyncActiveSessionResource) -> None:
        self._active_session = active_session

        self.create_poll = async_to_streamed_response_wrapper(
            active_session.create_poll,
        )
        self.get_active_session = async_to_streamed_response_wrapper(
            active_session.get_active_session,
        )
        self.kick_all_participants = async_to_streamed_response_wrapper(
            active_session.kick_all_participants,
        )
        self.kick_participants = async_to_streamed_response_wrapper(
            active_session.kick_participants,
        )
