# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, cast

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...pagination import SyncSinglePage, AsyncSinglePage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.load_balancers import monitor_group_edit_params, monitor_group_create_params, monitor_group_update_params
from ...types.load_balancers.monitor_group import MonitorGroup

__all__ = ["MonitorGroupsResource", "AsyncMonitorGroupsResource"]


class MonitorGroupsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MonitorGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return MonitorGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MonitorGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return MonitorGroupsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        id: str,
        description: str,
        members: Iterable[monitor_group_create_params.Member],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorGroup:
        """
        Create a new monitor group.

        Args:
          account_id: Identifier.

          id: The ID of the Monitor Group to use for checking the health of origins within
              this pool.

          description: A short description of the monitor group

          members: List of monitors in this group

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/load_balancers/monitor_groups",
            body=maybe_transform(
                {
                    "id": id,
                    "description": description,
                    "members": members,
                },
                monitor_group_create_params.MonitorGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[MonitorGroup]._unwrapper,
            ),
            cast_to=cast(Type[MonitorGroup], ResultWrapper[MonitorGroup]),
        )

    def update(
        self,
        monitor_group_id: str,
        *,
        account_id: str,
        id: str,
        description: str,
        members: Iterable[monitor_group_update_params.Member],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorGroup:
        """
        Modify a configured monitor group.

        Args:
          account_id: Identifier.

          id: The ID of the Monitor Group to use for checking the health of origins within
              this pool.

          description: A short description of the monitor group

          members: List of monitors in this group

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not monitor_group_id:
            raise ValueError(f"Expected a non-empty value for `monitor_group_id` but received {monitor_group_id!r}")
        return self._put(
            f"/accounts/{account_id}/load_balancers/monitor_groups/{monitor_group_id}",
            body=maybe_transform(
                {
                    "id": id,
                    "description": description,
                    "members": members,
                },
                monitor_group_update_params.MonitorGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[MonitorGroup]._unwrapper,
            ),
            cast_to=cast(Type[MonitorGroup], ResultWrapper[MonitorGroup]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[MonitorGroup]:
        """
        List configured monitor groups.

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/load_balancers/monitor_groups",
            page=SyncSinglePage[MonitorGroup],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=MonitorGroup,
        )

    def delete(
        self,
        monitor_group_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorGroup:
        """
        Delete a configured monitor group.

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not monitor_group_id:
            raise ValueError(f"Expected a non-empty value for `monitor_group_id` but received {monitor_group_id!r}")
        return self._delete(
            f"/accounts/{account_id}/load_balancers/monitor_groups/{monitor_group_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[MonitorGroup]._unwrapper,
            ),
            cast_to=cast(Type[MonitorGroup], ResultWrapper[MonitorGroup]),
        )

    def edit(
        self,
        monitor_group_id: str,
        *,
        account_id: str,
        id: str,
        description: str,
        members: Iterable[monitor_group_edit_params.Member],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorGroup:
        """
        Apply changes to an existing monitor group, overwriting the supplied properties.

        Args:
          account_id: Identifier.

          id: The ID of the Monitor Group to use for checking the health of origins within
              this pool.

          description: A short description of the monitor group

          members: List of monitors in this group

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not monitor_group_id:
            raise ValueError(f"Expected a non-empty value for `monitor_group_id` but received {monitor_group_id!r}")
        return self._patch(
            f"/accounts/{account_id}/load_balancers/monitor_groups/{monitor_group_id}",
            body=maybe_transform(
                {
                    "id": id,
                    "description": description,
                    "members": members,
                },
                monitor_group_edit_params.MonitorGroupEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[MonitorGroup]._unwrapper,
            ),
            cast_to=cast(Type[MonitorGroup], ResultWrapper[MonitorGroup]),
        )

    def get(
        self,
        monitor_group_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorGroup:
        """
        Fetch a single configured monitor group.

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not monitor_group_id:
            raise ValueError(f"Expected a non-empty value for `monitor_group_id` but received {monitor_group_id!r}")
        return self._get(
            f"/accounts/{account_id}/load_balancers/monitor_groups/{monitor_group_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[MonitorGroup]._unwrapper,
            ),
            cast_to=cast(Type[MonitorGroup], ResultWrapper[MonitorGroup]),
        )


class AsyncMonitorGroupsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMonitorGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMonitorGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMonitorGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncMonitorGroupsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        id: str,
        description: str,
        members: Iterable[monitor_group_create_params.Member],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorGroup:
        """
        Create a new monitor group.

        Args:
          account_id: Identifier.

          id: The ID of the Monitor Group to use for checking the health of origins within
              this pool.

          description: A short description of the monitor group

          members: List of monitors in this group

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/load_balancers/monitor_groups",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "description": description,
                    "members": members,
                },
                monitor_group_create_params.MonitorGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[MonitorGroup]._unwrapper,
            ),
            cast_to=cast(Type[MonitorGroup], ResultWrapper[MonitorGroup]),
        )

    async def update(
        self,
        monitor_group_id: str,
        *,
        account_id: str,
        id: str,
        description: str,
        members: Iterable[monitor_group_update_params.Member],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorGroup:
        """
        Modify a configured monitor group.

        Args:
          account_id: Identifier.

          id: The ID of the Monitor Group to use for checking the health of origins within
              this pool.

          description: A short description of the monitor group

          members: List of monitors in this group

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not monitor_group_id:
            raise ValueError(f"Expected a non-empty value for `monitor_group_id` but received {monitor_group_id!r}")
        return await self._put(
            f"/accounts/{account_id}/load_balancers/monitor_groups/{monitor_group_id}",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "description": description,
                    "members": members,
                },
                monitor_group_update_params.MonitorGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[MonitorGroup]._unwrapper,
            ),
            cast_to=cast(Type[MonitorGroup], ResultWrapper[MonitorGroup]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[MonitorGroup, AsyncSinglePage[MonitorGroup]]:
        """
        List configured monitor groups.

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/load_balancers/monitor_groups",
            page=AsyncSinglePage[MonitorGroup],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=MonitorGroup,
        )

    async def delete(
        self,
        monitor_group_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorGroup:
        """
        Delete a configured monitor group.

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not monitor_group_id:
            raise ValueError(f"Expected a non-empty value for `monitor_group_id` but received {monitor_group_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/load_balancers/monitor_groups/{monitor_group_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[MonitorGroup]._unwrapper,
            ),
            cast_to=cast(Type[MonitorGroup], ResultWrapper[MonitorGroup]),
        )

    async def edit(
        self,
        monitor_group_id: str,
        *,
        account_id: str,
        id: str,
        description: str,
        members: Iterable[monitor_group_edit_params.Member],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorGroup:
        """
        Apply changes to an existing monitor group, overwriting the supplied properties.

        Args:
          account_id: Identifier.

          id: The ID of the Monitor Group to use for checking the health of origins within
              this pool.

          description: A short description of the monitor group

          members: List of monitors in this group

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not monitor_group_id:
            raise ValueError(f"Expected a non-empty value for `monitor_group_id` but received {monitor_group_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/load_balancers/monitor_groups/{monitor_group_id}",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "description": description,
                    "members": members,
                },
                monitor_group_edit_params.MonitorGroupEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[MonitorGroup]._unwrapper,
            ),
            cast_to=cast(Type[MonitorGroup], ResultWrapper[MonitorGroup]),
        )

    async def get(
        self,
        monitor_group_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorGroup:
        """
        Fetch a single configured monitor group.

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not monitor_group_id:
            raise ValueError(f"Expected a non-empty value for `monitor_group_id` but received {monitor_group_id!r}")
        return await self._get(
            f"/accounts/{account_id}/load_balancers/monitor_groups/{monitor_group_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[MonitorGroup]._unwrapper,
            ),
            cast_to=cast(Type[MonitorGroup], ResultWrapper[MonitorGroup]),
        )


class MonitorGroupsResourceWithRawResponse:
    def __init__(self, monitor_groups: MonitorGroupsResource) -> None:
        self._monitor_groups = monitor_groups

        self.create = to_raw_response_wrapper(
            monitor_groups.create,
        )
        self.update = to_raw_response_wrapper(
            monitor_groups.update,
        )
        self.list = to_raw_response_wrapper(
            monitor_groups.list,
        )
        self.delete = to_raw_response_wrapper(
            monitor_groups.delete,
        )
        self.edit = to_raw_response_wrapper(
            monitor_groups.edit,
        )
        self.get = to_raw_response_wrapper(
            monitor_groups.get,
        )


class AsyncMonitorGroupsResourceWithRawResponse:
    def __init__(self, monitor_groups: AsyncMonitorGroupsResource) -> None:
        self._monitor_groups = monitor_groups

        self.create = async_to_raw_response_wrapper(
            monitor_groups.create,
        )
        self.update = async_to_raw_response_wrapper(
            monitor_groups.update,
        )
        self.list = async_to_raw_response_wrapper(
            monitor_groups.list,
        )
        self.delete = async_to_raw_response_wrapper(
            monitor_groups.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            monitor_groups.edit,
        )
        self.get = async_to_raw_response_wrapper(
            monitor_groups.get,
        )


class MonitorGroupsResourceWithStreamingResponse:
    def __init__(self, monitor_groups: MonitorGroupsResource) -> None:
        self._monitor_groups = monitor_groups

        self.create = to_streamed_response_wrapper(
            monitor_groups.create,
        )
        self.update = to_streamed_response_wrapper(
            monitor_groups.update,
        )
        self.list = to_streamed_response_wrapper(
            monitor_groups.list,
        )
        self.delete = to_streamed_response_wrapper(
            monitor_groups.delete,
        )
        self.edit = to_streamed_response_wrapper(
            monitor_groups.edit,
        )
        self.get = to_streamed_response_wrapper(
            monitor_groups.get,
        )


class AsyncMonitorGroupsResourceWithStreamingResponse:
    def __init__(self, monitor_groups: AsyncMonitorGroupsResource) -> None:
        self._monitor_groups = monitor_groups

        self.create = async_to_streamed_response_wrapper(
            monitor_groups.create,
        )
        self.update = async_to_streamed_response_wrapper(
            monitor_groups.update,
        )
        self.list = async_to_streamed_response_wrapper(
            monitor_groups.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            monitor_groups.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            monitor_groups.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            monitor_groups.get,
        )
