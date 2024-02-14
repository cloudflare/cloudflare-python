# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .._compat import cached_property

from ..types import (
    AccountMemberCreateResponse,
    AccountMemberUpdateResponse,
    AccountMemberListResponse,
    AccountMemberDeleteResponse,
    AccountMemberGetResponse,
    account_member_update_params,
)

from typing import Type, List, Iterable, Optional

from typing_extensions import Literal

from .._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from .._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from .._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ..types import shared_params
from ..types import account_member_create_params
from ..types import account_member_update_params
from ..types import account_member_list_params
from .._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["AccountMembers", "AsyncAccountMembers"]


class AccountMembers(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountMembersWithRawResponse:
        return AccountMembersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountMembersWithStreamingResponse:
        return AccountMembersWithStreamingResponse(self)

    def create(
        self,
        account_id: object,
        *,
        email: str,
        roles: List[str],
        status: Literal["accepted", "pending"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountMemberCreateResponse:
        """
        Add a user to the list of members for this account.

        Args:
          email: The contact email address of the user.

          roles: Array of roles associated with this member.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/accounts/{account_id}/members",
            body=maybe_transform(
                {
                    "email": email,
                    "roles": roles,
                    "status": status,
                },
                account_member_create_params.AccountMemberCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AccountMemberCreateResponse], ResultWrapper[AccountMemberCreateResponse]),
        )

    def update(
        self,
        member_id: str,
        *,
        account_id: object,
        roles: Iterable[account_member_update_params.Role],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountMemberUpdateResponse:
        """
        Modify an account member.

        Args:
          member_id: Membership identifier tag.

          roles: Roles assigned to this member.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return self._put(
            f"/accounts/{account_id}/members/{member_id}",
            body=maybe_transform({"roles": roles}, account_member_update_params.AccountMemberUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AccountMemberUpdateResponse], ResultWrapper[AccountMemberUpdateResponse]),
        )

    def list(
        self,
        account_id: object,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        order: Literal["user.first_name", "user.last_name", "user.email", "status"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        status: Literal["accepted", "pending", "rejected"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AccountMemberListResponse]:
        """
        List all members of an account.

        Args:
          direction: Direction to order results.

          order: Field to order results by.

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          status: A member's status in the account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{account_id}/members",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "status": status,
                    },
                    account_member_list_params.AccountMemberListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[AccountMemberListResponse]], ResultWrapper[AccountMemberListResponse]),
        )

    def delete(
        self,
        member_id: str,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AccountMemberDeleteResponse]:
        """
        Remove a member from an account.

        Args:
          member_id: Membership identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return self._delete(
            f"/accounts/{account_id}/members/{member_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[AccountMemberDeleteResponse]], ResultWrapper[AccountMemberDeleteResponse]),
        )

    def get(
        self,
        member_id: str,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountMemberGetResponse:
        """
        Get information about a specific member of an account.

        Args:
          member_id: Membership identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return self._get(
            f"/accounts/{account_id}/members/{member_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AccountMemberGetResponse], ResultWrapper[AccountMemberGetResponse]),
        )


class AsyncAccountMembers(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountMembersWithRawResponse:
        return AsyncAccountMembersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountMembersWithStreamingResponse:
        return AsyncAccountMembersWithStreamingResponse(self)

    async def create(
        self,
        account_id: object,
        *,
        email: str,
        roles: List[str],
        status: Literal["accepted", "pending"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountMemberCreateResponse:
        """
        Add a user to the list of members for this account.

        Args:
          email: The contact email address of the user.

          roles: Array of roles associated with this member.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/accounts/{account_id}/members",
            body=maybe_transform(
                {
                    "email": email,
                    "roles": roles,
                    "status": status,
                },
                account_member_create_params.AccountMemberCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AccountMemberCreateResponse], ResultWrapper[AccountMemberCreateResponse]),
        )

    async def update(
        self,
        member_id: str,
        *,
        account_id: object,
        roles: Iterable[account_member_update_params.Role],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountMemberUpdateResponse:
        """
        Modify an account member.

        Args:
          member_id: Membership identifier tag.

          roles: Roles assigned to this member.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return await self._put(
            f"/accounts/{account_id}/members/{member_id}",
            body=maybe_transform({"roles": roles}, account_member_update_params.AccountMemberUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AccountMemberUpdateResponse], ResultWrapper[AccountMemberUpdateResponse]),
        )

    async def list(
        self,
        account_id: object,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        order: Literal["user.first_name", "user.last_name", "user.email", "status"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        status: Literal["accepted", "pending", "rejected"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AccountMemberListResponse]:
        """
        List all members of an account.

        Args:
          direction: Direction to order results.

          order: Field to order results by.

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          status: A member's status in the account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{account_id}/members",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "status": status,
                    },
                    account_member_list_params.AccountMemberListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[AccountMemberListResponse]], ResultWrapper[AccountMemberListResponse]),
        )

    async def delete(
        self,
        member_id: str,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AccountMemberDeleteResponse]:
        """
        Remove a member from an account.

        Args:
          member_id: Membership identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/members/{member_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[AccountMemberDeleteResponse]], ResultWrapper[AccountMemberDeleteResponse]),
        )

    async def get(
        self,
        member_id: str,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountMemberGetResponse:
        """
        Get information about a specific member of an account.

        Args:
          member_id: Membership identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return await self._get(
            f"/accounts/{account_id}/members/{member_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AccountMemberGetResponse], ResultWrapper[AccountMemberGetResponse]),
        )


class AccountMembersWithRawResponse:
    def __init__(self, account_members: AccountMembers) -> None:
        self._account_members = account_members

        self.create = to_raw_response_wrapper(
            account_members.create,
        )
        self.update = to_raw_response_wrapper(
            account_members.update,
        )
        self.list = to_raw_response_wrapper(
            account_members.list,
        )
        self.delete = to_raw_response_wrapper(
            account_members.delete,
        )
        self.get = to_raw_response_wrapper(
            account_members.get,
        )


class AsyncAccountMembersWithRawResponse:
    def __init__(self, account_members: AsyncAccountMembers) -> None:
        self._account_members = account_members

        self.create = async_to_raw_response_wrapper(
            account_members.create,
        )
        self.update = async_to_raw_response_wrapper(
            account_members.update,
        )
        self.list = async_to_raw_response_wrapper(
            account_members.list,
        )
        self.delete = async_to_raw_response_wrapper(
            account_members.delete,
        )
        self.get = async_to_raw_response_wrapper(
            account_members.get,
        )


class AccountMembersWithStreamingResponse:
    def __init__(self, account_members: AccountMembers) -> None:
        self._account_members = account_members

        self.create = to_streamed_response_wrapper(
            account_members.create,
        )
        self.update = to_streamed_response_wrapper(
            account_members.update,
        )
        self.list = to_streamed_response_wrapper(
            account_members.list,
        )
        self.delete = to_streamed_response_wrapper(
            account_members.delete,
        )
        self.get = to_streamed_response_wrapper(
            account_members.get,
        )


class AsyncAccountMembersWithStreamingResponse:
    def __init__(self, account_members: AsyncAccountMembers) -> None:
        self._account_members = account_members

        self.create = async_to_streamed_response_wrapper(
            account_members.create,
        )
        self.update = async_to_streamed_response_wrapper(
            account_members.update,
        )
        self.list = async_to_streamed_response_wrapper(
            account_members.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            account_members.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            account_members.get,
        )
