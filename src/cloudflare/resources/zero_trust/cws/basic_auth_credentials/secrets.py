# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

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
from .....types.zero_trust.cws.basic_auth_credentials import secret_list_params, secret_create_params
from .....types.zero_trust.cws.basic_auth_credentials.basic_auth_secret import BasicAuthSecret
from .....types.zero_trust.cws.basic_auth_credentials.secret_delete_response import SecretDeleteResponse

__all__ = ["SecretsResource", "AsyncSecretsResource"]


class SecretsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SecretsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SecretsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SecretsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SecretsResourceWithStreamingResponse(self)

    def create(
        self,
        credential_id: str,
        *,
        account_id: str,
        password: str,
        expires_at: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BasicAuthSecret:
        """
        Adds a password secret to the credential.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          credential_id: ID of the parent credential

          password: Password stored only as a one-way hash and never returned. Maximum 72 UTF-8
              bytes.

          expires_at: Optional deactivation deadline (RFC 3339). Omit or null for no expiry.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not credential_id:
            raise ValueError(f"Expected a non-empty value for `credential_id` but received {credential_id!r}")
        return self._post(
            path_template(
                "/accounts/{account_id}/cws/basic-auth-credentials/{credential_id}/secrets",
                account_id=account_id,
                credential_id=credential_id,
            ),
            body=maybe_transform(
                {
                    "password": password,
                    "expires_at": expires_at,
                },
                secret_create_params.SecretCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[BasicAuthSecret]._unwrapper,
            ),
            cast_to=cast(Type[BasicAuthSecret], ResultWrapper[BasicAuthSecret]),
        )

    def list(
        self,
        credential_id: str,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        order: Literal["created_at"] | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[BasicAuthSecret]:
        """
        Returns a paginated list of secrets belonging to the credential.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          credential_id: ID of the parent credential

          cursor: Pagination cursor from previous response

          direction: Sort direction (default: asc)

          order: Field to order results by (default: created_at)

          per_page: Number of items per page (1-100, default 20)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not credential_id:
            raise ValueError(f"Expected a non-empty value for `credential_id` but received {credential_id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/cws/basic-auth-credentials/{credential_id}/secrets",
                account_id=account_id,
                credential_id=credential_id,
            ),
            page=SyncCursorPagination[BasicAuthSecret],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "direction": direction,
                        "order": order,
                        "per_page": per_page,
                    },
                    secret_list_params.SecretListParams,
                ),
            ),
            model=BasicAuthSecret,
        )

    def delete(
        self,
        secret_id: str,
        *,
        account_id: str,
        credential_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecretDeleteResponse:
        """
        Deletes the specified secret from the credential.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          credential_id: ID of the parent credential

          secret_id: ID of the secret to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not credential_id:
            raise ValueError(f"Expected a non-empty value for `credential_id` but received {credential_id!r}")
        if not secret_id:
            raise ValueError(f"Expected a non-empty value for `secret_id` but received {secret_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/cws/basic-auth-credentials/{credential_id}/secrets/{secret_id}",
                account_id=account_id,
                credential_id=credential_id,
                secret_id=secret_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SecretDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[SecretDeleteResponse], ResultWrapper[SecretDeleteResponse]),
        )

    def get(
        self,
        secret_id: str,
        *,
        account_id: str,
        credential_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BasicAuthSecret:
        """
        Returns the specified secret's metadata without exposing its password or hash.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          credential_id: ID of the parent credential

          secret_id: ID of the secret to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not credential_id:
            raise ValueError(f"Expected a non-empty value for `credential_id` but received {credential_id!r}")
        if not secret_id:
            raise ValueError(f"Expected a non-empty value for `secret_id` but received {secret_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/cws/basic-auth-credentials/{credential_id}/secrets/{secret_id}",
                account_id=account_id,
                credential_id=credential_id,
                secret_id=secret_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[BasicAuthSecret]._unwrapper,
            ),
            cast_to=cast(Type[BasicAuthSecret], ResultWrapper[BasicAuthSecret]),
        )


class AsyncSecretsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSecretsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSecretsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSecretsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSecretsResourceWithStreamingResponse(self)

    async def create(
        self,
        credential_id: str,
        *,
        account_id: str,
        password: str,
        expires_at: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BasicAuthSecret:
        """
        Adds a password secret to the credential.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          credential_id: ID of the parent credential

          password: Password stored only as a one-way hash and never returned. Maximum 72 UTF-8
              bytes.

          expires_at: Optional deactivation deadline (RFC 3339). Omit or null for no expiry.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not credential_id:
            raise ValueError(f"Expected a non-empty value for `credential_id` but received {credential_id!r}")
        return await self._post(
            path_template(
                "/accounts/{account_id}/cws/basic-auth-credentials/{credential_id}/secrets",
                account_id=account_id,
                credential_id=credential_id,
            ),
            body=await async_maybe_transform(
                {
                    "password": password,
                    "expires_at": expires_at,
                },
                secret_create_params.SecretCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[BasicAuthSecret]._unwrapper,
            ),
            cast_to=cast(Type[BasicAuthSecret], ResultWrapper[BasicAuthSecret]),
        )

    def list(
        self,
        credential_id: str,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        order: Literal["created_at"] | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[BasicAuthSecret, AsyncCursorPagination[BasicAuthSecret]]:
        """
        Returns a paginated list of secrets belonging to the credential.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          credential_id: ID of the parent credential

          cursor: Pagination cursor from previous response

          direction: Sort direction (default: asc)

          order: Field to order results by (default: created_at)

          per_page: Number of items per page (1-100, default 20)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not credential_id:
            raise ValueError(f"Expected a non-empty value for `credential_id` but received {credential_id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/cws/basic-auth-credentials/{credential_id}/secrets",
                account_id=account_id,
                credential_id=credential_id,
            ),
            page=AsyncCursorPagination[BasicAuthSecret],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "direction": direction,
                        "order": order,
                        "per_page": per_page,
                    },
                    secret_list_params.SecretListParams,
                ),
            ),
            model=BasicAuthSecret,
        )

    async def delete(
        self,
        secret_id: str,
        *,
        account_id: str,
        credential_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecretDeleteResponse:
        """
        Deletes the specified secret from the credential.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          credential_id: ID of the parent credential

          secret_id: ID of the secret to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not credential_id:
            raise ValueError(f"Expected a non-empty value for `credential_id` but received {credential_id!r}")
        if not secret_id:
            raise ValueError(f"Expected a non-empty value for `secret_id` but received {secret_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/cws/basic-auth-credentials/{credential_id}/secrets/{secret_id}",
                account_id=account_id,
                credential_id=credential_id,
                secret_id=secret_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SecretDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[SecretDeleteResponse], ResultWrapper[SecretDeleteResponse]),
        )

    async def get(
        self,
        secret_id: str,
        *,
        account_id: str,
        credential_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BasicAuthSecret:
        """
        Returns the specified secret's metadata without exposing its password or hash.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          credential_id: ID of the parent credential

          secret_id: ID of the secret to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not credential_id:
            raise ValueError(f"Expected a non-empty value for `credential_id` but received {credential_id!r}")
        if not secret_id:
            raise ValueError(f"Expected a non-empty value for `secret_id` but received {secret_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/cws/basic-auth-credentials/{credential_id}/secrets/{secret_id}",
                account_id=account_id,
                credential_id=credential_id,
                secret_id=secret_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[BasicAuthSecret]._unwrapper,
            ),
            cast_to=cast(Type[BasicAuthSecret], ResultWrapper[BasicAuthSecret]),
        )


class SecretsResourceWithRawResponse:
    def __init__(self, secrets: SecretsResource) -> None:
        self._secrets = secrets

        self.create = to_raw_response_wrapper(
            secrets.create,
        )
        self.list = to_raw_response_wrapper(
            secrets.list,
        )
        self.delete = to_raw_response_wrapper(
            secrets.delete,
        )
        self.get = to_raw_response_wrapper(
            secrets.get,
        )


class AsyncSecretsResourceWithRawResponse:
    def __init__(self, secrets: AsyncSecretsResource) -> None:
        self._secrets = secrets

        self.create = async_to_raw_response_wrapper(
            secrets.create,
        )
        self.list = async_to_raw_response_wrapper(
            secrets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            secrets.delete,
        )
        self.get = async_to_raw_response_wrapper(
            secrets.get,
        )


class SecretsResourceWithStreamingResponse:
    def __init__(self, secrets: SecretsResource) -> None:
        self._secrets = secrets

        self.create = to_streamed_response_wrapper(
            secrets.create,
        )
        self.list = to_streamed_response_wrapper(
            secrets.list,
        )
        self.delete = to_streamed_response_wrapper(
            secrets.delete,
        )
        self.get = to_streamed_response_wrapper(
            secrets.get,
        )


class AsyncSecretsResourceWithStreamingResponse:
    def __init__(self, secrets: AsyncSecretsResource) -> None:
        self._secrets = secrets

        self.create = async_to_streamed_response_wrapper(
            secrets.create,
        )
        self.list = async_to_streamed_response_wrapper(
            secrets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            secrets.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            secrets.get,
        )
