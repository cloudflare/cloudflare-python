# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.user.invite import Invite

from ...pagination import SyncSinglePage, AsyncSinglePage

from ..._base_client import make_request_options, AsyncPaginator

from ..._wrappers import ResultWrapper

from ..._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type

from typing_extensions import Literal

from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from ...types.user import invite_edit_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["InvitesResource", "AsyncInvitesResource"]

class InvitesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InvitesResourceWithRawResponse:
        return InvitesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InvitesResourceWithStreamingResponse:
        return InvitesResourceWithStreamingResponse(self)

    def list(self,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> SyncSinglePage[Invite]:
        """Lists all invitations associated with my user."""
        return self._get_api_list(
            "/user/invites",
            page = SyncSinglePage[Invite],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            model=Invite,
        )

    def edit(self,
    invite_id: str,
    *,
    status: Literal["accepted", "rejected"],
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> object:
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
          raise ValueError(
            f'Expected a non-empty value for `invite_id` but received {invite_id!r}'
          )
        return self._patch(
            f"/user/invites/{invite_id}",
            body=maybe_transform({
                "status": status
            }, invite_edit_params.InviteEditParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[object]]._unwrapper),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    def get(self,
    invite_id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> object:
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
          raise ValueError(
            f'Expected a non-empty value for `invite_id` but received {invite_id!r}'
          )
        return self._get(
            f"/user/invites/{invite_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[object]]._unwrapper),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

class AsyncInvitesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInvitesResourceWithRawResponse:
        return AsyncInvitesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInvitesResourceWithStreamingResponse:
        return AsyncInvitesResourceWithStreamingResponse(self)

    def list(self,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AsyncPaginator[Invite, AsyncSinglePage[Invite]]:
        """Lists all invitations associated with my user."""
        return self._get_api_list(
            "/user/invites",
            page = AsyncSinglePage[Invite],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            model=Invite,
        )

    async def edit(self,
    invite_id: str,
    *,
    status: Literal["accepted", "rejected"],
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> object:
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
          raise ValueError(
            f'Expected a non-empty value for `invite_id` but received {invite_id!r}'
          )
        return await self._patch(
            f"/user/invites/{invite_id}",
            body=await async_maybe_transform({
                "status": status
            }, invite_edit_params.InviteEditParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[object]]._unwrapper),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    async def get(self,
    invite_id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> object:
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
          raise ValueError(
            f'Expected a non-empty value for `invite_id` but received {invite_id!r}'
          )
        return await self._get(
            f"/user/invites/{invite_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[object]]._unwrapper),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

class InvitesResourceWithRawResponse:
    def __init__(self, invites: InvitesResource) -> None:
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

class AsyncInvitesResourceWithRawResponse:
    def __init__(self, invites: AsyncInvitesResource) -> None:
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

class InvitesResourceWithStreamingResponse:
    def __init__(self, invites: InvitesResource) -> None:
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

class AsyncInvitesResourceWithStreamingResponse:
    def __init__(self, invites: AsyncInvitesResource) -> None:
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