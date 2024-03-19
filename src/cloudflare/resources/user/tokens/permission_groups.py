# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import (
    make_request_options,
)
from ....types.user.tokens import PermissionGroupListResponse

__all__ = ["PermissionGroups", "AsyncPermissionGroups"]


class PermissionGroups(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PermissionGroupsWithRawResponse:
        return PermissionGroupsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PermissionGroupsWithStreamingResponse:
        return PermissionGroupsWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PermissionGroupListResponse]:
        """Find all available permission groups."""
        return self._get(
            "/user/tokens/permission_groups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[PermissionGroupListResponse]], ResultWrapper[PermissionGroupListResponse]),
        )


class AsyncPermissionGroups(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPermissionGroupsWithRawResponse:
        return AsyncPermissionGroupsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPermissionGroupsWithStreamingResponse:
        return AsyncPermissionGroupsWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PermissionGroupListResponse]:
        """Find all available permission groups."""
        return await self._get(
            "/user/tokens/permission_groups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[PermissionGroupListResponse]], ResultWrapper[PermissionGroupListResponse]),
        )


class PermissionGroupsWithRawResponse:
    def __init__(self, permission_groups: PermissionGroups) -> None:
        self._permission_groups = permission_groups

        self.list = to_raw_response_wrapper(
            permission_groups.list,
        )


class AsyncPermissionGroupsWithRawResponse:
    def __init__(self, permission_groups: AsyncPermissionGroups) -> None:
        self._permission_groups = permission_groups

        self.list = async_to_raw_response_wrapper(
            permission_groups.list,
        )


class PermissionGroupsWithStreamingResponse:
    def __init__(self, permission_groups: PermissionGroups) -> None:
        self._permission_groups = permission_groups

        self.list = to_streamed_response_wrapper(
            permission_groups.list,
        )


class AsyncPermissionGroupsWithStreamingResponse:
    def __init__(self, permission_groups: AsyncPermissionGroups) -> None:
        self._permission_groups = permission_groups

        self.list = async_to_streamed_response_wrapper(
            permission_groups.list,
        )
