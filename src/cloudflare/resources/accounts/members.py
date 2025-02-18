# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Iterable, Optional, cast
from typing_extensions import Literal, overload

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    required_args,
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
from ...pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ..._base_client import AsyncPaginator, make_request_options
from ...types.accounts import member_list_params, member_create_params, member_update_params
from ...types.shared.member import Member
from ...types.shared_params.role import Role
from ...types.accounts.member_delete_response import MemberDeleteResponse

__all__ = ["MembersResource", "AsyncMembersResource"]


class MembersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MembersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return MembersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MembersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return MembersResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        account_id: str,
        email: str,
        roles: List[str],
        status: Literal["accepted", "pending"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Member]:
        """
        Add a user to the list of members for this account.

        Args:
          account_id: Account identifier tag.

          email: The contact email address of the user.

          roles: Array of roles associated with this member.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        account_id: str,
        email: str,
        policies: Iterable[member_create_params.IAMCreateMemberWithPoliciesPolicy],
        status: Literal["accepted", "pending"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Member]:
        """
        Add a user to the list of members for this account.

        Args:
          account_id: Account identifier tag.

          email: The contact email address of the user.

          policies: Array of policies associated with this member.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_id", "email", "roles"], ["account_id", "email", "policies"])
    def create(
        self,
        *,
        account_id: str,
        email: str,
        roles: List[str] | NotGiven = NOT_GIVEN,
        status: Literal["accepted", "pending"] | NotGiven = NOT_GIVEN,
        policies: Iterable[member_create_params.IAMCreateMemberWithPoliciesPolicy] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Member]:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/members",
            body=maybe_transform(
                {
                    "email": email,
                    "roles": roles,
                    "status": status,
                    "policies": policies,
                },
                member_create_params.MemberCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Member]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Member]], ResultWrapper[Member]),
        )

    @overload
    def update(
        self,
        member_id: str,
        *,
        account_id: str,
        roles: Iterable[Role] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Member]:
        """
        Modify an account member.

        Args:
          account_id: Account identifier tag.

          member_id: Membership identifier tag.

          roles: Roles assigned to this member.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        member_id: str,
        *,
        account_id: str,
        policies: Iterable[member_update_params.IAMUpdateMemberWithPoliciesPolicy],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Member]:
        """
        Modify an account member.

        Args:
          account_id: Account identifier tag.

          member_id: Membership identifier tag.

          policies: Array of policies associated with this member.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_id"], ["account_id", "policies"])
    def update(
        self,
        member_id: str,
        *,
        account_id: str,
        roles: Iterable[Role] | NotGiven = NOT_GIVEN,
        policies: Iterable[member_update_params.IAMUpdateMemberWithPoliciesPolicy] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Member]:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return self._put(
            f"/accounts/{account_id}/members/{member_id}",
            body=maybe_transform(
                {
                    "roles": roles,
                    "policies": policies,
                },
                member_update_params.MemberUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Member]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Member]], ResultWrapper[Member]),
        )

    def list(
        self,
        *,
        account_id: str,
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
    ) -> SyncV4PagePaginationArray[Member]:
        """
        List all members of an account.

        Args:
          account_id: Account identifier tag.

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
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/members",
            page=SyncV4PagePaginationArray[Member],
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
                    member_list_params.MemberListParams,
                ),
            ),
            model=Member,
        )

    def delete(
        self,
        member_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MemberDeleteResponse]:
        """
        Remove a member from an account.

        Args:
          account_id: Account identifier tag.

          member_id: Membership identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return self._delete(
            f"/accounts/{account_id}/members/{member_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MemberDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MemberDeleteResponse]], ResultWrapper[MemberDeleteResponse]),
        )

    def get(
        self,
        member_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Member]:
        """
        Get information about a specific member of an account.

        Args:
          account_id: Account identifier tag.

          member_id: Membership identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return self._get(
            f"/accounts/{account_id}/members/{member_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Member]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Member]], ResultWrapper[Member]),
        )


class AsyncMembersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMembersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMembersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMembersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncMembersResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        account_id: str,
        email: str,
        roles: List[str],
        status: Literal["accepted", "pending"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Member]:
        """
        Add a user to the list of members for this account.

        Args:
          account_id: Account identifier tag.

          email: The contact email address of the user.

          roles: Array of roles associated with this member.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        account_id: str,
        email: str,
        policies: Iterable[member_create_params.IAMCreateMemberWithPoliciesPolicy],
        status: Literal["accepted", "pending"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Member]:
        """
        Add a user to the list of members for this account.

        Args:
          account_id: Account identifier tag.

          email: The contact email address of the user.

          policies: Array of policies associated with this member.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_id", "email", "roles"], ["account_id", "email", "policies"])
    async def create(
        self,
        *,
        account_id: str,
        email: str,
        roles: List[str] | NotGiven = NOT_GIVEN,
        status: Literal["accepted", "pending"] | NotGiven = NOT_GIVEN,
        policies: Iterable[member_create_params.IAMCreateMemberWithPoliciesPolicy] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Member]:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/members",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "roles": roles,
                    "status": status,
                    "policies": policies,
                },
                member_create_params.MemberCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Member]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Member]], ResultWrapper[Member]),
        )

    @overload
    async def update(
        self,
        member_id: str,
        *,
        account_id: str,
        roles: Iterable[Role] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Member]:
        """
        Modify an account member.

        Args:
          account_id: Account identifier tag.

          member_id: Membership identifier tag.

          roles: Roles assigned to this member.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        member_id: str,
        *,
        account_id: str,
        policies: Iterable[member_update_params.IAMUpdateMemberWithPoliciesPolicy],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Member]:
        """
        Modify an account member.

        Args:
          account_id: Account identifier tag.

          member_id: Membership identifier tag.

          policies: Array of policies associated with this member.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_id"], ["account_id", "policies"])
    async def update(
        self,
        member_id: str,
        *,
        account_id: str,
        roles: Iterable[Role] | NotGiven = NOT_GIVEN,
        policies: Iterable[member_update_params.IAMUpdateMemberWithPoliciesPolicy] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Member]:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return await self._put(
            f"/accounts/{account_id}/members/{member_id}",
            body=await async_maybe_transform(
                {
                    "roles": roles,
                    "policies": policies,
                },
                member_update_params.MemberUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Member]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Member]], ResultWrapper[Member]),
        )

    def list(
        self,
        *,
        account_id: str,
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
    ) -> AsyncPaginator[Member, AsyncV4PagePaginationArray[Member]]:
        """
        List all members of an account.

        Args:
          account_id: Account identifier tag.

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
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/members",
            page=AsyncV4PagePaginationArray[Member],
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
                    member_list_params.MemberListParams,
                ),
            ),
            model=Member,
        )

    async def delete(
        self,
        member_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MemberDeleteResponse]:
        """
        Remove a member from an account.

        Args:
          account_id: Account identifier tag.

          member_id: Membership identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/members/{member_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MemberDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MemberDeleteResponse]], ResultWrapper[MemberDeleteResponse]),
        )

    async def get(
        self,
        member_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Member]:
        """
        Get information about a specific member of an account.

        Args:
          account_id: Account identifier tag.

          member_id: Membership identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return await self._get(
            f"/accounts/{account_id}/members/{member_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Member]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Member]], ResultWrapper[Member]),
        )


class MembersResourceWithRawResponse:
    def __init__(self, members: MembersResource) -> None:
        self._members = members

        self.create = to_raw_response_wrapper(
            members.create,
        )
        self.update = to_raw_response_wrapper(
            members.update,
        )
        self.list = to_raw_response_wrapper(
            members.list,
        )
        self.delete = to_raw_response_wrapper(
            members.delete,
        )
        self.get = to_raw_response_wrapper(
            members.get,
        )


class AsyncMembersResourceWithRawResponse:
    def __init__(self, members: AsyncMembersResource) -> None:
        self._members = members

        self.create = async_to_raw_response_wrapper(
            members.create,
        )
        self.update = async_to_raw_response_wrapper(
            members.update,
        )
        self.list = async_to_raw_response_wrapper(
            members.list,
        )
        self.delete = async_to_raw_response_wrapper(
            members.delete,
        )
        self.get = async_to_raw_response_wrapper(
            members.get,
        )


class MembersResourceWithStreamingResponse:
    def __init__(self, members: MembersResource) -> None:
        self._members = members

        self.create = to_streamed_response_wrapper(
            members.create,
        )
        self.update = to_streamed_response_wrapper(
            members.update,
        )
        self.list = to_streamed_response_wrapper(
            members.list,
        )
        self.delete = to_streamed_response_wrapper(
            members.delete,
        )
        self.get = to_streamed_response_wrapper(
            members.get,
        )


class AsyncMembersResourceWithStreamingResponse:
    def __init__(self, members: AsyncMembersResource) -> None:
        self._members = members

        self.create = async_to_streamed_response_wrapper(
            members.create,
        )
        self.update = async_to_streamed_response_wrapper(
            members.update,
        )
        self.list = async_to_streamed_response_wrapper(
            members.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            members.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            members.get,
        )
