# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from .secrets import (
    SecretsResource,
    AsyncSecretsResource,
    SecretsResourceWithRawResponse,
    AsyncSecretsResourceWithRawResponse,
    SecretsResourceWithStreamingResponse,
    AsyncSecretsResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from .....pagination import SyncCursorPagination, AsyncCursorPagination
from ....._base_client import AsyncPaginator, make_request_options
from .....types.zero_trust.cws import basic_auth_credential_list_params, basic_auth_credential_create_params
from .....types.zero_trust.cws.basic_auth_credential import BasicAuthCredential
from .....types.zero_trust.cws.basic_auth_credential_delete_response import BasicAuthCredentialDeleteResponse

__all__ = ["BasicAuthCredentialsResource", "AsyncBasicAuthCredentialsResource"]


class BasicAuthCredentialsResource(SyncAPIResource):
    @cached_property
    def secrets(self) -> SecretsResource:
        return SecretsResource(self._client)

    @cached_property
    def with_raw_response(self) -> BasicAuthCredentialsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return BasicAuthCredentialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BasicAuthCredentialsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return BasicAuthCredentialsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        username: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BasicAuthCredential:
        """
        Creates a basic-auth credential with the specified username.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          username: Login presented by the client. Printable ASCII only, excluding space and colon.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/cws/basic-auth-credentials", account_id=account_id),
            body=maybe_transform(
                {"username": username}, basic_auth_credential_create_params.BasicAuthCredentialCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[BasicAuthCredential]._unwrapper,
            ),
            cast_to=cast(Type[BasicAuthCredential], ResultWrapper[BasicAuthCredential]),
        )

    def list(
        self,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        deployment_id: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        order: Literal["username", "created_at", "updated_at"] | Omit = omit,
        per_page: int | Omit = omit,
        username: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[BasicAuthCredential]:
        """
        Returns a paginated list of basic-auth credentials in the account.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          cursor: Pagination cursor from previous response

          deployment_id: Filter to credentials attached to this deployment

          direction: Sort direction (default: asc)

          order: Field to order results by (default: created_at)

          per_page: Number of items per page (1-100, default 20)

          username: Filter by username (case-insensitive substring match)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/cws/basic-auth-credentials", account_id=account_id),
            page=SyncCursorPagination[BasicAuthCredential],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "deployment_id": deployment_id,
                        "direction": direction,
                        "order": order,
                        "per_page": per_page,
                        "username": username,
                    },
                    basic_auth_credential_list_params.BasicAuthCredentialListParams,
                ),
            ),
            model=BasicAuthCredential,
        )

    def delete(
        self,
        credential_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BasicAuthCredentialDeleteResponse:
        """
        Deletes the credential and its secrets if it is not attached to a deployment.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          credential_id: ID of the credential to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not credential_id:
            raise ValueError(f"Expected a non-empty value for `credential_id` but received {credential_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/cws/basic-auth-credentials/{credential_id}",
                account_id=account_id,
                credential_id=credential_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[BasicAuthCredentialDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[BasicAuthCredentialDeleteResponse], ResultWrapper[BasicAuthCredentialDeleteResponse]),
        )

    def get(
        self,
        credential_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BasicAuthCredential:
        """
        Returns the basic-auth credential with the specified ID.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          credential_id: ID of the credential to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not credential_id:
            raise ValueError(f"Expected a non-empty value for `credential_id` but received {credential_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/cws/basic-auth-credentials/{credential_id}",
                account_id=account_id,
                credential_id=credential_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[BasicAuthCredential]._unwrapper,
            ),
            cast_to=cast(Type[BasicAuthCredential], ResultWrapper[BasicAuthCredential]),
        )


class AsyncBasicAuthCredentialsResource(AsyncAPIResource):
    @cached_property
    def secrets(self) -> AsyncSecretsResource:
        return AsyncSecretsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBasicAuthCredentialsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBasicAuthCredentialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBasicAuthCredentialsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncBasicAuthCredentialsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        username: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BasicAuthCredential:
        """
        Creates a basic-auth credential with the specified username.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          username: Login presented by the client. Printable ASCII only, excluding space and colon.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/cws/basic-auth-credentials", account_id=account_id),
            body=await async_maybe_transform(
                {"username": username}, basic_auth_credential_create_params.BasicAuthCredentialCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[BasicAuthCredential]._unwrapper,
            ),
            cast_to=cast(Type[BasicAuthCredential], ResultWrapper[BasicAuthCredential]),
        )

    def list(
        self,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        deployment_id: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        order: Literal["username", "created_at", "updated_at"] | Omit = omit,
        per_page: int | Omit = omit,
        username: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[BasicAuthCredential, AsyncCursorPagination[BasicAuthCredential]]:
        """
        Returns a paginated list of basic-auth credentials in the account.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          cursor: Pagination cursor from previous response

          deployment_id: Filter to credentials attached to this deployment

          direction: Sort direction (default: asc)

          order: Field to order results by (default: created_at)

          per_page: Number of items per page (1-100, default 20)

          username: Filter by username (case-insensitive substring match)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/cws/basic-auth-credentials", account_id=account_id),
            page=AsyncCursorPagination[BasicAuthCredential],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "deployment_id": deployment_id,
                        "direction": direction,
                        "order": order,
                        "per_page": per_page,
                        "username": username,
                    },
                    basic_auth_credential_list_params.BasicAuthCredentialListParams,
                ),
            ),
            model=BasicAuthCredential,
        )

    async def delete(
        self,
        credential_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BasicAuthCredentialDeleteResponse:
        """
        Deletes the credential and its secrets if it is not attached to a deployment.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          credential_id: ID of the credential to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not credential_id:
            raise ValueError(f"Expected a non-empty value for `credential_id` but received {credential_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/cws/basic-auth-credentials/{credential_id}",
                account_id=account_id,
                credential_id=credential_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[BasicAuthCredentialDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[BasicAuthCredentialDeleteResponse], ResultWrapper[BasicAuthCredentialDeleteResponse]),
        )

    async def get(
        self,
        credential_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BasicAuthCredential:
        """
        Returns the basic-auth credential with the specified ID.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          credential_id: ID of the credential to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not credential_id:
            raise ValueError(f"Expected a non-empty value for `credential_id` but received {credential_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/cws/basic-auth-credentials/{credential_id}",
                account_id=account_id,
                credential_id=credential_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[BasicAuthCredential]._unwrapper,
            ),
            cast_to=cast(Type[BasicAuthCredential], ResultWrapper[BasicAuthCredential]),
        )


class BasicAuthCredentialsResourceWithRawResponse:
    def __init__(self, basic_auth_credentials: BasicAuthCredentialsResource) -> None:
        self._basic_auth_credentials = basic_auth_credentials

        self.create = to_raw_response_wrapper(
            basic_auth_credentials.create,
        )
        self.list = to_raw_response_wrapper(
            basic_auth_credentials.list,
        )
        self.delete = to_raw_response_wrapper(
            basic_auth_credentials.delete,
        )
        self.get = to_raw_response_wrapper(
            basic_auth_credentials.get,
        )

    @cached_property
    def secrets(self) -> SecretsResourceWithRawResponse:
        return SecretsResourceWithRawResponse(self._basic_auth_credentials.secrets)


class AsyncBasicAuthCredentialsResourceWithRawResponse:
    def __init__(self, basic_auth_credentials: AsyncBasicAuthCredentialsResource) -> None:
        self._basic_auth_credentials = basic_auth_credentials

        self.create = async_to_raw_response_wrapper(
            basic_auth_credentials.create,
        )
        self.list = async_to_raw_response_wrapper(
            basic_auth_credentials.list,
        )
        self.delete = async_to_raw_response_wrapper(
            basic_auth_credentials.delete,
        )
        self.get = async_to_raw_response_wrapper(
            basic_auth_credentials.get,
        )

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithRawResponse:
        return AsyncSecretsResourceWithRawResponse(self._basic_auth_credentials.secrets)


class BasicAuthCredentialsResourceWithStreamingResponse:
    def __init__(self, basic_auth_credentials: BasicAuthCredentialsResource) -> None:
        self._basic_auth_credentials = basic_auth_credentials

        self.create = to_streamed_response_wrapper(
            basic_auth_credentials.create,
        )
        self.list = to_streamed_response_wrapper(
            basic_auth_credentials.list,
        )
        self.delete = to_streamed_response_wrapper(
            basic_auth_credentials.delete,
        )
        self.get = to_streamed_response_wrapper(
            basic_auth_credentials.get,
        )

    @cached_property
    def secrets(self) -> SecretsResourceWithStreamingResponse:
        return SecretsResourceWithStreamingResponse(self._basic_auth_credentials.secrets)


class AsyncBasicAuthCredentialsResourceWithStreamingResponse:
    def __init__(self, basic_auth_credentials: AsyncBasicAuthCredentialsResource) -> None:
        self._basic_auth_credentials = basic_auth_credentials

        self.create = async_to_streamed_response_wrapper(
            basic_auth_credentials.create,
        )
        self.list = async_to_streamed_response_wrapper(
            basic_auth_credentials.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            basic_auth_credentials.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            basic_auth_credentials.get,
        )

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithStreamingResponse:
        return AsyncSecretsResourceWithStreamingResponse(self._basic_auth_credentials.secrets)
