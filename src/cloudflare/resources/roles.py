# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .._compat import cached_property

from ..types import RoleAccountRolesListRolesResponse, RoleGetResponse

from typing import Type, Optional

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
from .._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Roles", "AsyncRoles"]


class Roles(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RolesWithRawResponse:
        return RolesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RolesWithStreamingResponse:
        return RolesWithStreamingResponse(self)

    def account_roles_list_roles(
        self,
        account_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RoleAccountRolesListRolesResponse]:
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
            cast_to=cast(
                Type[Optional[RoleAccountRolesListRolesResponse]], ResultWrapper[RoleAccountRolesListRolesResponse]
            ),
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

    async def account_roles_list_roles(
        self,
        account_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RoleAccountRolesListRolesResponse]:
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
            cast_to=cast(
                Type[Optional[RoleAccountRolesListRolesResponse]], ResultWrapper[RoleAccountRolesListRolesResponse]
            ),
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

        self.account_roles_list_roles = to_raw_response_wrapper(
            roles.account_roles_list_roles,
        )
        self.get = to_raw_response_wrapper(
            roles.get,
        )


class AsyncRolesWithRawResponse:
    def __init__(self, roles: AsyncRoles) -> None:
        self._roles = roles

        self.account_roles_list_roles = async_to_raw_response_wrapper(
            roles.account_roles_list_roles,
        )
        self.get = async_to_raw_response_wrapper(
            roles.get,
        )


class RolesWithStreamingResponse:
    def __init__(self, roles: Roles) -> None:
        self._roles = roles

        self.account_roles_list_roles = to_streamed_response_wrapper(
            roles.account_roles_list_roles,
        )
        self.get = to_streamed_response_wrapper(
            roles.get,
        )


class AsyncRolesWithStreamingResponse:
    def __init__(self, roles: AsyncRoles) -> None:
        self._roles = roles

        self.account_roles_list_roles = async_to_streamed_response_wrapper(
            roles.account_roles_list_roles,
        )
        self.get = async_to_streamed_response_wrapper(
            roles.get,
        )
