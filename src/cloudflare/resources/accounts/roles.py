# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ...types.accounts import RoleGetResponse, RoleListResponse

__all__ = ["Roles", "AsyncRoles"]


class Roles(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RolesWithRawResponse:
        return RolesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RolesWithStreamingResponse:
        return RolesWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RoleListResponse]:
        """
        Get all available roles for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{account_id}/roles",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[RoleListResponse]], ResultWrapper[RoleListResponse]),
        )

    def get(
        self,
        role_id: object,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RoleGetResponse:
        """
        Get information about a specific role for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            RoleGetResponse,
            self._get(
                f"/accounts/{account_id}/roles/{role_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RoleGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncRoles(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRolesWithRawResponse:
        return AsyncRolesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRolesWithStreamingResponse:
        return AsyncRolesWithStreamingResponse(self)

    async def list(
        self,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RoleListResponse]:
        """
        Get all available roles for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{account_id}/roles",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[RoleListResponse]], ResultWrapper[RoleListResponse]),
        )

    async def get(
        self,
        role_id: object,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RoleGetResponse:
        """
        Get information about a specific role for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            RoleGetResponse,
            await self._get(
                f"/accounts/{account_id}/roles/{role_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RoleGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class RolesWithRawResponse:
    def __init__(self, roles: Roles) -> None:
        self._roles = roles

        self.list = to_raw_response_wrapper(
            roles.list,
        )
        self.get = to_raw_response_wrapper(
            roles.get,
        )


class AsyncRolesWithRawResponse:
    def __init__(self, roles: AsyncRoles) -> None:
        self._roles = roles

        self.list = async_to_raw_response_wrapper(
            roles.list,
        )
        self.get = async_to_raw_response_wrapper(
            roles.get,
        )


class RolesWithStreamingResponse:
    def __init__(self, roles: Roles) -> None:
        self._roles = roles

        self.list = to_streamed_response_wrapper(
            roles.list,
        )
        self.get = to_streamed_response_wrapper(
            roles.get,
        )


class AsyncRolesWithStreamingResponse:
    def __init__(self, roles: AsyncRoles) -> None:
        self._roles = roles

        self.list = async_to_streamed_response_wrapper(
            roles.list,
        )
        self.get = async_to_streamed_response_wrapper(
            roles.get,
        )
