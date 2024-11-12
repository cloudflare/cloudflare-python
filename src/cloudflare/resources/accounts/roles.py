# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

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
from ...pagination import SyncSinglePage, AsyncSinglePage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.accounts.role_get_response import RoleGetResponse
from ...types.accounts.role_list_response import RoleListResponse

__all__ = ["RolesResource", "AsyncRolesResource"]


class RolesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RolesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RolesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RolesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RolesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[RoleListResponse]:
        """
        Get all available roles for an account.

        Args:
          account_id: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/roles",
            page=SyncSinglePage[RoleListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=RoleListResponse,
        )

    def get(
        self,
        role_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RoleGetResponse]:
        """
        Get information about a specific role for an account.

        Args:
          account_id: Account identifier tag.

          role_id: Role identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not role_id:
            raise ValueError(f"Expected a non-empty value for `role_id` but received {role_id!r}")
        return self._get(
            f"/accounts/{account_id}/roles/{role_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RoleGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RoleGetResponse]], ResultWrapper[RoleGetResponse]),
        )


class AsyncRolesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRolesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRolesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRolesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncRolesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[RoleListResponse, AsyncSinglePage[RoleListResponse]]:
        """
        Get all available roles for an account.

        Args:
          account_id: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/roles",
            page=AsyncSinglePage[RoleListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=RoleListResponse,
        )

    async def get(
        self,
        role_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RoleGetResponse]:
        """
        Get information about a specific role for an account.

        Args:
          account_id: Account identifier tag.

          role_id: Role identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not role_id:
            raise ValueError(f"Expected a non-empty value for `role_id` but received {role_id!r}")
        return await self._get(
            f"/accounts/{account_id}/roles/{role_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RoleGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RoleGetResponse]], ResultWrapper[RoleGetResponse]),
        )


class RolesResourceWithRawResponse:
    def __init__(self, roles: RolesResource) -> None:
        self._roles = roles

        self.list = to_raw_response_wrapper(
            roles.list,
        )
        self.get = to_raw_response_wrapper(
            roles.get,
        )


class AsyncRolesResourceWithRawResponse:
    def __init__(self, roles: AsyncRolesResource) -> None:
        self._roles = roles

        self.list = async_to_raw_response_wrapper(
            roles.list,
        )
        self.get = async_to_raw_response_wrapper(
            roles.get,
        )


class RolesResourceWithStreamingResponse:
    def __init__(self, roles: RolesResource) -> None:
        self._roles = roles

        self.list = to_streamed_response_wrapper(
            roles.list,
        )
        self.get = to_streamed_response_wrapper(
            roles.get,
        )


class AsyncRolesResourceWithStreamingResponse:
    def __init__(self, roles: AsyncRolesResource) -> None:
        self._roles = roles

        self.list = async_to_streamed_response_wrapper(
            roles.list,
        )
        self.get = async_to_streamed_response_wrapper(
            roles.get,
        )
