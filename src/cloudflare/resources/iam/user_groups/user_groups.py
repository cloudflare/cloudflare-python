# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast

import httpx

from .members import (
    MembersResource,
    AsyncMembersResource,
    MembersResourceWithRawResponse,
    AsyncMembersResourceWithRawResponse,
    MembersResourceWithStreamingResponse,
    AsyncMembersResourceWithStreamingResponse,
)
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
from ....types.iam import user_group_list_params, user_group_create_params, user_group_update_params
from ....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ...._base_client import AsyncPaginator, make_request_options
from ....types.iam.user_group_get_response import UserGroupGetResponse
from ....types.iam.user_group_list_response import UserGroupListResponse
from ....types.iam.user_group_create_response import UserGroupCreateResponse
from ....types.iam.user_group_delete_response import UserGroupDeleteResponse
from ....types.iam.user_group_update_response import UserGroupUpdateResponse

__all__ = ["UserGroupsResource", "AsyncUserGroupsResource"]


class UserGroupsResource(SyncAPIResource):
    @cached_property
    def members(self) -> MembersResource:
        return MembersResource(self._client)

    @cached_property
    def with_raw_response(self) -> UserGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return UserGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return UserGroupsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        policies: Iterable[user_group_create_params.Policy],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[UserGroupCreateResponse]:
        """
        Create a new user group under the specified account.

        Args:
          account_id: Account identifier tag.

          name: Name of the User group.

          policies: Policies attached to the User group

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/iam/user_groups",
            body=maybe_transform(
                {
                    "name": name,
                    "policies": policies,
                },
                user_group_create_params.UserGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[UserGroupCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[UserGroupCreateResponse]], ResultWrapper[UserGroupCreateResponse]),
        )

    def update(
        self,
        user_group_id: str,
        *,
        account_id: str,
        name: str | NotGiven = NOT_GIVEN,
        policies: Iterable[user_group_update_params.Policy] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[UserGroupUpdateResponse]:
        """
        Modify an existing user group.

        Args:
          account_id: Account identifier tag.

          user_group_id: User Group identifier tag.

          name: Name of the User group.

          policies: Policies attached to the User group

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not user_group_id:
            raise ValueError(f"Expected a non-empty value for `user_group_id` but received {user_group_id!r}")
        return self._put(
            f"/accounts/{account_id}/iam/user_groups/{user_group_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "policies": policies,
                },
                user_group_update_params.UserGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[UserGroupUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[UserGroupUpdateResponse]], ResultWrapper[UserGroupUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        id: str | NotGiven = NOT_GIVEN,
        direction: str | NotGiven = NOT_GIVEN,
        fuzzy_name: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[UserGroupListResponse]:
        """
        List all the user groups for an account.

        Args:
          account_id: Account identifier tag.

          id: ID of the user group to be fetched.

          direction: The sort order of returned user groups by name. Default sort order is ascending.
              To switch to descending, set this parameter to "desc"

          fuzzy_name: A string used for searching for user groups containing that substring.

          name: Name of the user group to be fetched.

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/iam/user_groups",
            page=SyncV4PagePaginationArray[UserGroupListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "direction": direction,
                        "fuzzy_name": fuzzy_name,
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                    },
                    user_group_list_params.UserGroupListParams,
                ),
            ),
            model=UserGroupListResponse,
        )

    def delete(
        self,
        user_group_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[UserGroupDeleteResponse]:
        """
        Remove a user group from an account.

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
        return self._delete(
            f"/accounts/{account_id}/iam/user_groups/{user_group_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[UserGroupDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[UserGroupDeleteResponse]], ResultWrapper[UserGroupDeleteResponse]),
        )

    def get(
        self,
        user_group_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[UserGroupGetResponse]:
        """
        Get information about a specific user group in an account.

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
        return self._get(
            f"/accounts/{account_id}/iam/user_groups/{user_group_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[UserGroupGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[UserGroupGetResponse]], ResultWrapper[UserGroupGetResponse]),
        )


class AsyncUserGroupsResource(AsyncAPIResource):
    @cached_property
    def members(self) -> AsyncMembersResource:
        return AsyncMembersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUserGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUserGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncUserGroupsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        policies: Iterable[user_group_create_params.Policy],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[UserGroupCreateResponse]:
        """
        Create a new user group under the specified account.

        Args:
          account_id: Account identifier tag.

          name: Name of the User group.

          policies: Policies attached to the User group

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/iam/user_groups",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "policies": policies,
                },
                user_group_create_params.UserGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[UserGroupCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[UserGroupCreateResponse]], ResultWrapper[UserGroupCreateResponse]),
        )

    async def update(
        self,
        user_group_id: str,
        *,
        account_id: str,
        name: str | NotGiven = NOT_GIVEN,
        policies: Iterable[user_group_update_params.Policy] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[UserGroupUpdateResponse]:
        """
        Modify an existing user group.

        Args:
          account_id: Account identifier tag.

          user_group_id: User Group identifier tag.

          name: Name of the User group.

          policies: Policies attached to the User group

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not user_group_id:
            raise ValueError(f"Expected a non-empty value for `user_group_id` but received {user_group_id!r}")
        return await self._put(
            f"/accounts/{account_id}/iam/user_groups/{user_group_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "policies": policies,
                },
                user_group_update_params.UserGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[UserGroupUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[UserGroupUpdateResponse]], ResultWrapper[UserGroupUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        id: str | NotGiven = NOT_GIVEN,
        direction: str | NotGiven = NOT_GIVEN,
        fuzzy_name: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[UserGroupListResponse, AsyncV4PagePaginationArray[UserGroupListResponse]]:
        """
        List all the user groups for an account.

        Args:
          account_id: Account identifier tag.

          id: ID of the user group to be fetched.

          direction: The sort order of returned user groups by name. Default sort order is ascending.
              To switch to descending, set this parameter to "desc"

          fuzzy_name: A string used for searching for user groups containing that substring.

          name: Name of the user group to be fetched.

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/iam/user_groups",
            page=AsyncV4PagePaginationArray[UserGroupListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "direction": direction,
                        "fuzzy_name": fuzzy_name,
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                    },
                    user_group_list_params.UserGroupListParams,
                ),
            ),
            model=UserGroupListResponse,
        )

    async def delete(
        self,
        user_group_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[UserGroupDeleteResponse]:
        """
        Remove a user group from an account.

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
        return await self._delete(
            f"/accounts/{account_id}/iam/user_groups/{user_group_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[UserGroupDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[UserGroupDeleteResponse]], ResultWrapper[UserGroupDeleteResponse]),
        )

    async def get(
        self,
        user_group_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[UserGroupGetResponse]:
        """
        Get information about a specific user group in an account.

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
        return await self._get(
            f"/accounts/{account_id}/iam/user_groups/{user_group_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[UserGroupGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[UserGroupGetResponse]], ResultWrapper[UserGroupGetResponse]),
        )


class UserGroupsResourceWithRawResponse:
    def __init__(self, user_groups: UserGroupsResource) -> None:
        self._user_groups = user_groups

        self.create = to_raw_response_wrapper(
            user_groups.create,
        )
        self.update = to_raw_response_wrapper(
            user_groups.update,
        )
        self.list = to_raw_response_wrapper(
            user_groups.list,
        )
        self.delete = to_raw_response_wrapper(
            user_groups.delete,
        )
        self.get = to_raw_response_wrapper(
            user_groups.get,
        )

    @cached_property
    def members(self) -> MembersResourceWithRawResponse:
        return MembersResourceWithRawResponse(self._user_groups.members)


class AsyncUserGroupsResourceWithRawResponse:
    def __init__(self, user_groups: AsyncUserGroupsResource) -> None:
        self._user_groups = user_groups

        self.create = async_to_raw_response_wrapper(
            user_groups.create,
        )
        self.update = async_to_raw_response_wrapper(
            user_groups.update,
        )
        self.list = async_to_raw_response_wrapper(
            user_groups.list,
        )
        self.delete = async_to_raw_response_wrapper(
            user_groups.delete,
        )
        self.get = async_to_raw_response_wrapper(
            user_groups.get,
        )

    @cached_property
    def members(self) -> AsyncMembersResourceWithRawResponse:
        return AsyncMembersResourceWithRawResponse(self._user_groups.members)


class UserGroupsResourceWithStreamingResponse:
    def __init__(self, user_groups: UserGroupsResource) -> None:
        self._user_groups = user_groups

        self.create = to_streamed_response_wrapper(
            user_groups.create,
        )
        self.update = to_streamed_response_wrapper(
            user_groups.update,
        )
        self.list = to_streamed_response_wrapper(
            user_groups.list,
        )
        self.delete = to_streamed_response_wrapper(
            user_groups.delete,
        )
        self.get = to_streamed_response_wrapper(
            user_groups.get,
        )

    @cached_property
    def members(self) -> MembersResourceWithStreamingResponse:
        return MembersResourceWithStreamingResponse(self._user_groups.members)


class AsyncUserGroupsResourceWithStreamingResponse:
    def __init__(self, user_groups: AsyncUserGroupsResource) -> None:
        self._user_groups = user_groups

        self.create = async_to_streamed_response_wrapper(
            user_groups.create,
        )
        self.update = async_to_streamed_response_wrapper(
            user_groups.update,
        )
        self.list = async_to_streamed_response_wrapper(
            user_groups.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            user_groups.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            user_groups.get,
        )

    @cached_property
    def members(self) -> AsyncMembersResourceWithStreamingResponse:
        return AsyncMembersResourceWithStreamingResponse(self._user_groups.members)
