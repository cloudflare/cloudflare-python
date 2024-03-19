# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, Optional, cast
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...types.user import InviteGetResponse, InviteEditResponse, InviteListResponse, invite_edit_params
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

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[InviteListResponse]:
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
            cast_to=cast(Type[Optional[InviteListResponse]], ResultWrapper[InviteListResponse]),
        )

    def edit(
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
    ) -> InviteEditResponse:
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
            InviteEditResponse,
            self._patch(
                f"/user/invites/{invite_id}",
                body=maybe_transform({"status": status}, invite_edit_params.InviteEditParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[InviteEditResponse]
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


class AsyncInvites(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInvitesWithRawResponse:
        return AsyncInvitesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInvitesWithStreamingResponse:
        return AsyncInvitesWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[InviteListResponse]:
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
            cast_to=cast(Type[Optional[InviteListResponse]], ResultWrapper[InviteListResponse]),
        )

    async def edit(
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
    ) -> InviteEditResponse:
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
            InviteEditResponse,
            await self._patch(
                f"/user/invites/{invite_id}",
                body=await async_maybe_transform({"status": status}, invite_edit_params.InviteEditParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[InviteEditResponse]
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


class InvitesWithRawResponse:
    def __init__(self, invites: Invites) -> None:
        self._invites = invites

        self.list = to_raw_response_wrapper(
            invites.list,
        )
        self.edit = to_raw_response_wrapper(
            invites.edit,
        )
        self.get = to_raw_response_wrapper(
            invites.get,
        )


class AsyncInvitesWithRawResponse:
    def __init__(self, invites: AsyncInvites) -> None:
        self._invites = invites

        self.list = async_to_raw_response_wrapper(
            invites.list,
        )
        self.edit = async_to_raw_response_wrapper(
            invites.edit,
        )
        self.get = async_to_raw_response_wrapper(
            invites.get,
        )


class InvitesWithStreamingResponse:
    def __init__(self, invites: Invites) -> None:
        self._invites = invites

        self.list = to_streamed_response_wrapper(
            invites.list,
        )
        self.edit = to_streamed_response_wrapper(
            invites.edit,
        )
        self.get = to_streamed_response_wrapper(
            invites.get,
        )


class AsyncInvitesWithStreamingResponse:
    def __init__(self, invites: AsyncInvites) -> None:
        self._invites = invites

        self.list = async_to_streamed_response_wrapper(
            invites.list,
        )
        self.edit = async_to_streamed_response_wrapper(
            invites.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            invites.get,
        )
