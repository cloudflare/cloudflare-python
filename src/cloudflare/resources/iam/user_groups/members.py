# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncSinglePage, AsyncSinglePage, SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ...._base_client import AsyncPaginator, make_request_options
from ....types.iam.user_groups import member_list_params, member_create_params, member_update_params
from ....types.iam.user_groups.member_list_response import MemberListResponse
from ....types.iam.user_groups.member_create_response import MemberCreateResponse
from ....types.iam.user_groups.member_delete_response import MemberDeleteResponse
from ....types.iam.user_groups.member_update_response import MemberUpdateResponse

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

    def create(
        self,
        user_group_id: str,
        *,
        account_id: str,
        body: Iterable[member_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MemberCreateResponse]:
        """
        Add members to a User Group.

        Args:
          account_id: Account identifier tag.

          user_group_id: User Group identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not user_group_id:
            raise ValueError(f"Expected a non-empty value for `user_group_id` but received {user_group_id!r}")
        return self._post(
            f"/accounts/{account_id}/iam/user_groups/{user_group_id}/members",
            body=maybe_transform(body, Iterable[member_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MemberCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MemberCreateResponse]], ResultWrapper[MemberCreateResponse]),
        )

    def update(
        self,
        user_group_id: str,
        *,
        account_id: str,
        body: Iterable[member_update_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[MemberUpdateResponse]:
        """
        Replace the set of members attached to a User Group.

        Args:
          account_id: Account identifier tag.

          user_group_id: User Group identifier tag.

          body: Set/Replace members to a user group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not user_group_id:
            raise ValueError(f"Expected a non-empty value for `user_group_id` but received {user_group_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/iam/user_groups/{user_group_id}/members",
            page=SyncSinglePage[MemberUpdateResponse],
            body=maybe_transform(body, Iterable[member_update_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=MemberUpdateResponse,
            method="put",
        )

    def list(
        self,
        user_group_id: str,
        *,
        account_id: str,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[MemberListResponse]:
        """
        List all the members attached to a user group.

        Args:
          account_id: Account identifier tag.

          user_group_id: User Group identifier tag.

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not user_group_id:
            raise ValueError(f"Expected a non-empty value for `user_group_id` but received {user_group_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/iam/user_groups/{user_group_id}/members",
            page=SyncV4PagePaginationArray[MemberListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    member_list_params.MemberListParams,
                ),
            ),
            model=MemberListResponse,
        )

    def delete(
        self,
        member_id: str,
        *,
        account_id: str,
        user_group_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MemberDeleteResponse]:
        """
        Remove a member from User Group

        Args:
          account_id: Account identifier tag.

          user_group_id: User Group identifier tag.

          member_id: The identifier of an existing account Member.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not user_group_id:
            raise ValueError(f"Expected a non-empty value for `user_group_id` but received {user_group_id!r}")
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return self._delete(
            f"/accounts/{account_id}/iam/user_groups/{user_group_id}/members/{member_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MemberDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MemberDeleteResponse]], ResultWrapper[MemberDeleteResponse]),
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

    async def create(
        self,
        user_group_id: str,
        *,
        account_id: str,
        body: Iterable[member_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MemberCreateResponse]:
        """
        Add members to a User Group.

        Args:
          account_id: Account identifier tag.

          user_group_id: User Group identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not user_group_id:
            raise ValueError(f"Expected a non-empty value for `user_group_id` but received {user_group_id!r}")
        return await self._post(
            f"/accounts/{account_id}/iam/user_groups/{user_group_id}/members",
            body=await async_maybe_transform(body, Iterable[member_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MemberCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MemberCreateResponse]], ResultWrapper[MemberCreateResponse]),
        )

    def update(
        self,
        user_group_id: str,
        *,
        account_id: str,
        body: Iterable[member_update_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[MemberUpdateResponse, AsyncSinglePage[MemberUpdateResponse]]:
        """
        Replace the set of members attached to a User Group.

        Args:
          account_id: Account identifier tag.

          user_group_id: User Group identifier tag.

          body: Set/Replace members to a user group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not user_group_id:
            raise ValueError(f"Expected a non-empty value for `user_group_id` but received {user_group_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/iam/user_groups/{user_group_id}/members",
            page=AsyncSinglePage[MemberUpdateResponse],
            body=maybe_transform(body, Iterable[member_update_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=MemberUpdateResponse,
            method="put",
        )

    def list(
        self,
        user_group_id: str,
        *,
        account_id: str,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[MemberListResponse, AsyncV4PagePaginationArray[MemberListResponse]]:
        """
        List all the members attached to a user group.

        Args:
          account_id: Account identifier tag.

          user_group_id: User Group identifier tag.

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not user_group_id:
            raise ValueError(f"Expected a non-empty value for `user_group_id` but received {user_group_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/iam/user_groups/{user_group_id}/members",
            page=AsyncV4PagePaginationArray[MemberListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    member_list_params.MemberListParams,
                ),
            ),
            model=MemberListResponse,
        )

    async def delete(
        self,
        member_id: str,
        *,
        account_id: str,
        user_group_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MemberDeleteResponse]:
        """
        Remove a member from User Group

        Args:
          account_id: Account identifier tag.

          user_group_id: User Group identifier tag.

          member_id: The identifier of an existing account Member.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not user_group_id:
            raise ValueError(f"Expected a non-empty value for `user_group_id` but received {user_group_id!r}")
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/iam/user_groups/{user_group_id}/members/{member_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MemberDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MemberDeleteResponse]], ResultWrapper[MemberDeleteResponse]),
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
