# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, Type, Optional, cast
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...types.users import (
    InviteGetResponse,
    InviteUpdateResponse,
    InviteUserSInvitesListInvitationsResponse,
    invite_update_params,
)
from ..._base_client import (
    make_request_options,
)

__all__ = ["Invites", "AsyncInvites"]


class Invites(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InvitesWithRawResponse:
        return InvitesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InvitesWithStreamingResponse:
        return InvitesWithStreamingResponse(self)

    def update(
        self,
        invite_id: str,
        *,
        status: Literal["accepted", "rejected"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InviteUpdateResponse:
        """
        Responds to an invitation.

        Args:
          invite_id: Invite identifier tag.

          status: Status of your response to the invitation (rejected or accepted).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invite_id:
            raise ValueError(f"Expected a non-empty value for `invite_id` but received {invite_id!r}")
        return cast(
            InviteUpdateResponse,
            self._patch(
                f"/user/invites/{invite_id}",
                body=maybe_transform({"status": status}, invite_update_params.InviteUpdateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[InviteUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get(
        self,
        invite_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InviteGetResponse:
        """
        Gets the details of an invitation.

        Args:
          invite_id: Invite identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invite_id:
            raise ValueError(f"Expected a non-empty value for `invite_id` but received {invite_id!r}")
        return cast(
            InviteGetResponse,
            self._get(
                f"/user/invites/{invite_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[InviteGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def user_s_invites_list_invitations(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[InviteUserSInvitesListInvitationsResponse]:
        """Lists all invitations associated with my user."""
        return self._get(
            "/user/invites",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[InviteUserSInvitesListInvitationsResponse]],
                ResultWrapper[InviteUserSInvitesListInvitationsResponse],
            ),
        )


class AsyncInvites(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInvitesWithRawResponse:
        return AsyncInvitesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInvitesWithStreamingResponse:
        return AsyncInvitesWithStreamingResponse(self)

    async def update(
        self,
        invite_id: str,
        *,
        status: Literal["accepted", "rejected"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InviteUpdateResponse:
        """
        Responds to an invitation.

        Args:
          invite_id: Invite identifier tag.

          status: Status of your response to the invitation (rejected or accepted).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invite_id:
            raise ValueError(f"Expected a non-empty value for `invite_id` but received {invite_id!r}")
        return cast(
            InviteUpdateResponse,
            await self._patch(
                f"/user/invites/{invite_id}",
                body=maybe_transform({"status": status}, invite_update_params.InviteUpdateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[InviteUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get(
        self,
        invite_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InviteGetResponse:
        """
        Gets the details of an invitation.

        Args:
          invite_id: Invite identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invite_id:
            raise ValueError(f"Expected a non-empty value for `invite_id` but received {invite_id!r}")
        return cast(
            InviteGetResponse,
            await self._get(
                f"/user/invites/{invite_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[InviteGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def user_s_invites_list_invitations(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[InviteUserSInvitesListInvitationsResponse]:
        """Lists all invitations associated with my user."""
        return await self._get(
            "/user/invites",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[InviteUserSInvitesListInvitationsResponse]],
                ResultWrapper[InviteUserSInvitesListInvitationsResponse],
            ),
        )


class InvitesWithRawResponse:
    def __init__(self, invites: Invites) -> None:
        self._invites = invites

        self.update = to_raw_response_wrapper(
            invites.update,
        )
        self.get = to_raw_response_wrapper(
            invites.get,
        )
        self.user_s_invites_list_invitations = to_raw_response_wrapper(
            invites.user_s_invites_list_invitations,
        )


class AsyncInvitesWithRawResponse:
    def __init__(self, invites: AsyncInvites) -> None:
        self._invites = invites

        self.update = async_to_raw_response_wrapper(
            invites.update,
        )
        self.get = async_to_raw_response_wrapper(
            invites.get,
        )
        self.user_s_invites_list_invitations = async_to_raw_response_wrapper(
            invites.user_s_invites_list_invitations,
        )


class InvitesWithStreamingResponse:
    def __init__(self, invites: Invites) -> None:
        self._invites = invites

        self.update = to_streamed_response_wrapper(
            invites.update,
        )
        self.get = to_streamed_response_wrapper(
            invites.get,
        )
        self.user_s_invites_list_invitations = to_streamed_response_wrapper(
            invites.user_s_invites_list_invitations,
        )


class AsyncInvitesWithStreamingResponse:
    def __init__(self, invites: AsyncInvites) -> None:
        self._invites = invites

        self.update = async_to_streamed_response_wrapper(
            invites.update,
        )
        self.get = async_to_streamed_response_wrapper(
            invites.get,
        )
        self.user_s_invites_list_invitations = async_to_streamed_response_wrapper(
            invites.user_s_invites_list_invitations,
        )
