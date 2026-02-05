# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ....._base_client import AsyncPaginator, make_request_options
from .....types.zero_trust.access.access_user import AccessUser
from .....types.zero_trust.identity_providers.scim import user_list_params

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)

    def list(
        self,
        identity_provider_id: str,
        *,
        account_id: str,
        cf_resource_id: str | Omit = omit,
        email: str | Omit = omit,
        idp_resource_id: str | Omit = omit,
        name: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        username: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[AccessUser]:
        """
        Lists SCIM User resources synced to Cloudflare via the System for Cross-domain
        Identity Management (SCIM).

        Args:
          account_id: Identifier.

          identity_provider_id: UUID.

          cf_resource_id: The unique Cloudflare-generated Id of the SCIM User resource; also known as the
              "Id".

          email: The email address of the SCIM User resource.

          idp_resource_id: The IdP-generated Id of the SCIM User resource; also known as the "external Id".

          name: The name of the SCIM User resource.

          page: Page number of results.

          per_page: Number of results per page.

          username: The username of the SCIM User resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identity_provider_id:
            raise ValueError(
                f"Expected a non-empty value for `identity_provider_id` but received {identity_provider_id!r}"
            )
        return self._get_api_list(
            f"/accounts/{account_id}/access/identity_providers/{identity_provider_id}/scim/users",
            page=SyncV4PagePaginationArray[AccessUser],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cf_resource_id": cf_resource_id,
                        "email": email,
                        "idp_resource_id": idp_resource_id,
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                        "username": username,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            model=AccessUser,
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)

    def list(
        self,
        identity_provider_id: str,
        *,
        account_id: str,
        cf_resource_id: str | Omit = omit,
        email: str | Omit = omit,
        idp_resource_id: str | Omit = omit,
        name: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        username: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AccessUser, AsyncV4PagePaginationArray[AccessUser]]:
        """
        Lists SCIM User resources synced to Cloudflare via the System for Cross-domain
        Identity Management (SCIM).

        Args:
          account_id: Identifier.

          identity_provider_id: UUID.

          cf_resource_id: The unique Cloudflare-generated Id of the SCIM User resource; also known as the
              "Id".

          email: The email address of the SCIM User resource.

          idp_resource_id: The IdP-generated Id of the SCIM User resource; also known as the "external Id".

          name: The name of the SCIM User resource.

          page: Page number of results.

          per_page: Number of results per page.

          username: The username of the SCIM User resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identity_provider_id:
            raise ValueError(
                f"Expected a non-empty value for `identity_provider_id` but received {identity_provider_id!r}"
            )
        return self._get_api_list(
            f"/accounts/{account_id}/access/identity_providers/{identity_provider_id}/scim/users",
            page=AsyncV4PagePaginationArray[AccessUser],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cf_resource_id": cf_resource_id,
                        "email": email,
                        "idp_resource_id": idp_resource_id,
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                        "username": username,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            model=AccessUser,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.list = to_raw_response_wrapper(
            users.list,
        )


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.list = async_to_raw_response_wrapper(
            users.list,
        )


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.list = to_streamed_response_wrapper(
            users.list,
        )


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.list = async_to_streamed_response_wrapper(
            users.list,
        )
