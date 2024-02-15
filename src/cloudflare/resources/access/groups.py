# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast

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
from ..._base_client import (
    make_request_options,
)
from ...types.access import (
    GroupGetResponse,
    GroupDeleteResponse,
    GroupUpdateResponse,
    GroupAccessGroupsListAccessGroupsResponse,
    GroupAccessGroupsCreateAnAccessGroupResponse,
    group_update_params,
    group_access_groups_create_an_access_group_params,
)

__all__ = ["Groups", "AsyncGroups"]


class Groups(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GroupsWithRawResponse:
        return GroupsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GroupsWithStreamingResponse:
        return GroupsWithStreamingResponse(self)

    def update(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        include: Iterable[group_update_params.Include],
        name: str,
        exclude: Iterable[group_update_params.Exclude] | NotGiven = NOT_GIVEN,
        is_default: bool | NotGiven = NOT_GIVEN,
        require: Iterable[group_update_params.Require] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupUpdateResponse:
        """
        Updates a configured Access group.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          include: Rules evaluated with an OR logical operator. A user needs to meet only one of
              the Include rules.

          name: The name of the Access group.

          exclude: Rules evaluated with a NOT logical operator. To match a policy, a user cannot
              meet any of the Exclude rules.

          is_default: Whether this is the default group

          require: Rules evaluated with an AND logical operator. To match a policy, a user must
              meet all of the Require rules.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._put(
            f"/{account_or_zone}/{account_or_zone_id}/access/groups/{uuid}",
            body=maybe_transform(
                {
                    "include": include,
                    "name": name,
                    "exclude": exclude,
                    "is_default": is_default,
                    "require": require,
                },
                group_update_params.GroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[GroupUpdateResponse], ResultWrapper[GroupUpdateResponse]),
        )

    def delete(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupDeleteResponse:
        """
        Deletes an Access group.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._delete(
            f"/{account_or_zone}/{account_or_zone_id}/access/groups/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[GroupDeleteResponse], ResultWrapper[GroupDeleteResponse]),
        )

    def access_groups_create_an_access_group(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        include: Iterable[group_access_groups_create_an_access_group_params.Include],
        name: str,
        exclude: Iterable[group_access_groups_create_an_access_group_params.Exclude] | NotGiven = NOT_GIVEN,
        is_default: bool | NotGiven = NOT_GIVEN,
        require: Iterable[group_access_groups_create_an_access_group_params.Require] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupAccessGroupsCreateAnAccessGroupResponse:
        """
        Creates a new Access group.

        Args:
          account_or_zone_id: Identifier

          include: Rules evaluated with an OR logical operator. A user needs to meet only one of
              the Include rules.

          name: The name of the Access group.

          exclude: Rules evaluated with a NOT logical operator. To match a policy, a user cannot
              meet any of the Exclude rules.

          is_default: Whether this is the default group

          require: Rules evaluated with an AND logical operator. To match a policy, a user must
              meet all of the Require rules.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return self._post(
            f"/{account_or_zone}/{account_or_zone_id}/access/groups",
            body=maybe_transform(
                {
                    "include": include,
                    "name": name,
                    "exclude": exclude,
                    "is_default": is_default,
                    "require": require,
                },
                group_access_groups_create_an_access_group_params.GroupAccessGroupsCreateAnAccessGroupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[GroupAccessGroupsCreateAnAccessGroupResponse],
                ResultWrapper[GroupAccessGroupsCreateAnAccessGroupResponse],
            ),
        )

    def access_groups_list_access_groups(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[GroupAccessGroupsListAccessGroupsResponse]:
        """
        Lists all Access groups.

        Args:
          account_or_zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return self._get(
            f"/{account_or_zone}/{account_or_zone_id}/access/groups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[GroupAccessGroupsListAccessGroupsResponse]],
                ResultWrapper[GroupAccessGroupsListAccessGroupsResponse],
            ),
        )

    def get(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupGetResponse:
        """
        Fetches a single Access group.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._get(
            f"/{account_or_zone}/{account_or_zone_id}/access/groups/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[GroupGetResponse], ResultWrapper[GroupGetResponse]),
        )


class AsyncGroups(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGroupsWithRawResponse:
        return AsyncGroupsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGroupsWithStreamingResponse:
        return AsyncGroupsWithStreamingResponse(self)

    async def update(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        include: Iterable[group_update_params.Include],
        name: str,
        exclude: Iterable[group_update_params.Exclude] | NotGiven = NOT_GIVEN,
        is_default: bool | NotGiven = NOT_GIVEN,
        require: Iterable[group_update_params.Require] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupUpdateResponse:
        """
        Updates a configured Access group.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          include: Rules evaluated with an OR logical operator. A user needs to meet only one of
              the Include rules.

          name: The name of the Access group.

          exclude: Rules evaluated with a NOT logical operator. To match a policy, a user cannot
              meet any of the Exclude rules.

          is_default: Whether this is the default group

          require: Rules evaluated with an AND logical operator. To match a policy, a user must
              meet all of the Require rules.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._put(
            f"/{account_or_zone}/{account_or_zone_id}/access/groups/{uuid}",
            body=maybe_transform(
                {
                    "include": include,
                    "name": name,
                    "exclude": exclude,
                    "is_default": is_default,
                    "require": require,
                },
                group_update_params.GroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[GroupUpdateResponse], ResultWrapper[GroupUpdateResponse]),
        )

    async def delete(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupDeleteResponse:
        """
        Deletes an Access group.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._delete(
            f"/{account_or_zone}/{account_or_zone_id}/access/groups/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[GroupDeleteResponse], ResultWrapper[GroupDeleteResponse]),
        )

    async def access_groups_create_an_access_group(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        include: Iterable[group_access_groups_create_an_access_group_params.Include],
        name: str,
        exclude: Iterable[group_access_groups_create_an_access_group_params.Exclude] | NotGiven = NOT_GIVEN,
        is_default: bool | NotGiven = NOT_GIVEN,
        require: Iterable[group_access_groups_create_an_access_group_params.Require] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupAccessGroupsCreateAnAccessGroupResponse:
        """
        Creates a new Access group.

        Args:
          account_or_zone_id: Identifier

          include: Rules evaluated with an OR logical operator. A user needs to meet only one of
              the Include rules.

          name: The name of the Access group.

          exclude: Rules evaluated with a NOT logical operator. To match a policy, a user cannot
              meet any of the Exclude rules.

          is_default: Whether this is the default group

          require: Rules evaluated with an AND logical operator. To match a policy, a user must
              meet all of the Require rules.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return await self._post(
            f"/{account_or_zone}/{account_or_zone_id}/access/groups",
            body=maybe_transform(
                {
                    "include": include,
                    "name": name,
                    "exclude": exclude,
                    "is_default": is_default,
                    "require": require,
                },
                group_access_groups_create_an_access_group_params.GroupAccessGroupsCreateAnAccessGroupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[GroupAccessGroupsCreateAnAccessGroupResponse],
                ResultWrapper[GroupAccessGroupsCreateAnAccessGroupResponse],
            ),
        )

    async def access_groups_list_access_groups(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[GroupAccessGroupsListAccessGroupsResponse]:
        """
        Lists all Access groups.

        Args:
          account_or_zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return await self._get(
            f"/{account_or_zone}/{account_or_zone_id}/access/groups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[GroupAccessGroupsListAccessGroupsResponse]],
                ResultWrapper[GroupAccessGroupsListAccessGroupsResponse],
            ),
        )

    async def get(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupGetResponse:
        """
        Fetches a single Access group.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._get(
            f"/{account_or_zone}/{account_or_zone_id}/access/groups/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[GroupGetResponse], ResultWrapper[GroupGetResponse]),
        )


class GroupsWithRawResponse:
    def __init__(self, groups: Groups) -> None:
        self._groups = groups

        self.update = to_raw_response_wrapper(
            groups.update,
        )
        self.delete = to_raw_response_wrapper(
            groups.delete,
        )
        self.access_groups_create_an_access_group = to_raw_response_wrapper(
            groups.access_groups_create_an_access_group,
        )
        self.access_groups_list_access_groups = to_raw_response_wrapper(
            groups.access_groups_list_access_groups,
        )
        self.get = to_raw_response_wrapper(
            groups.get,
        )


class AsyncGroupsWithRawResponse:
    def __init__(self, groups: AsyncGroups) -> None:
        self._groups = groups

        self.update = async_to_raw_response_wrapper(
            groups.update,
        )
        self.delete = async_to_raw_response_wrapper(
            groups.delete,
        )
        self.access_groups_create_an_access_group = async_to_raw_response_wrapper(
            groups.access_groups_create_an_access_group,
        )
        self.access_groups_list_access_groups = async_to_raw_response_wrapper(
            groups.access_groups_list_access_groups,
        )
        self.get = async_to_raw_response_wrapper(
            groups.get,
        )


class GroupsWithStreamingResponse:
    def __init__(self, groups: Groups) -> None:
        self._groups = groups

        self.update = to_streamed_response_wrapper(
            groups.update,
        )
        self.delete = to_streamed_response_wrapper(
            groups.delete,
        )
        self.access_groups_create_an_access_group = to_streamed_response_wrapper(
            groups.access_groups_create_an_access_group,
        )
        self.access_groups_list_access_groups = to_streamed_response_wrapper(
            groups.access_groups_list_access_groups,
        )
        self.get = to_streamed_response_wrapper(
            groups.get,
        )


class AsyncGroupsWithStreamingResponse:
    def __init__(self, groups: AsyncGroups) -> None:
        self._groups = groups

        self.update = async_to_streamed_response_wrapper(
            groups.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            groups.delete,
        )
        self.access_groups_create_an_access_group = async_to_streamed_response_wrapper(
            groups.access_groups_create_an_access_group,
        )
        self.access_groups_list_access_groups = async_to_streamed_response_wrapper(
            groups.access_groups_list_access_groups,
        )
        self.get = async_to_streamed_response_wrapper(
            groups.get,
        )
