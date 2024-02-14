# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .permission_groups import PermissionGroups, AsyncPermissionGroups

from ...._compat import cached_property

from .verifies import Verifies, AsyncVerifies

from .values import Values, AsyncValues

from ....types.users import (
    TokenUpdateResponse,
    TokenDeleteResponse,
    TokenGetResponse,
    TokenUserAPITokensCreateTokenResponse,
    TokenUserAPITokensListTokensResponse,
    token_update_params,
    token_user_api_tokens_create_token_params,
)

from typing import Iterable, Union, Type, Optional

from typing_extensions import Literal

from datetime import datetime

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from ....types.users import token_update_params
from ....types.users import token_user_api_tokens_create_token_params
from ....types.users import token_user_api_tokens_list_tokens_params
from .permission_groups import (
    PermissionGroups,
    AsyncPermissionGroups,
    PermissionGroupsWithRawResponse,
    AsyncPermissionGroupsWithRawResponse,
    PermissionGroupsWithStreamingResponse,
    AsyncPermissionGroupsWithStreamingResponse,
)
from .verifies import (
    Verifies,
    AsyncVerifies,
    VerifiesWithRawResponse,
    AsyncVerifiesWithRawResponse,
    VerifiesWithStreamingResponse,
    AsyncVerifiesWithStreamingResponse,
)
from .values import (
    Values,
    AsyncValues,
    ValuesWithRawResponse,
    AsyncValuesWithRawResponse,
    ValuesWithStreamingResponse,
    AsyncValuesWithStreamingResponse,
)
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Tokens", "AsyncTokens"]


class Tokens(SyncAPIResource):
    @cached_property
    def permission_groups(self) -> PermissionGroups:
        return PermissionGroups(self._client)

    @cached_property
    def verifies(self) -> Verifies:
        return Verifies(self._client)

    @cached_property
    def values(self) -> Values:
        return Values(self._client)

    @cached_property
    def with_raw_response(self) -> TokensWithRawResponse:
        return TokensWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TokensWithStreamingResponse:
        return TokensWithStreamingResponse(self)

    def update(
        self,
        token_id: object,
        *,
        name: str,
        policies: Iterable[token_update_params.Policy],
        status: Literal["active", "disabled", "expired"],
        condition: token_update_params.Condition | NotGiven = NOT_GIVEN,
        expires_on: Union[str, datetime] | NotGiven = NOT_GIVEN,
        not_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokenUpdateResponse:
        """
        Update an existing token.

        Args:
          name: Token name.

          policies: List of access policies assigned to the token.

          status: Status of the token.

          expires_on: The expiration time on or after which the JWT MUST NOT be accepted for
              processing.

          not_before: The time before which the token MUST NOT be accepted for processing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            TokenUpdateResponse,
            self._put(
                f"/user/tokens/{token_id}",
                body=maybe_transform(
                    {
                        "name": name,
                        "policies": policies,
                        "status": status,
                        "condition": condition,
                        "expires_on": expires_on,
                        "not_before": not_before,
                    },
                    token_update_params.TokenUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[TokenUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def delete(
        self,
        token_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TokenDeleteResponse]:
        """
        Destroy a token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            f"/user/tokens/{token_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[TokenDeleteResponse]], ResultWrapper[TokenDeleteResponse]),
        )

    def get(
        self,
        token_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokenGetResponse:
        """
        Get information about a specific token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            TokenGetResponse,
            self._get(
                f"/user/tokens/{token_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[TokenGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def user_api_tokens_create_token(
        self,
        *,
        name: str,
        policies: Iterable[token_user_api_tokens_create_token_params.Policy],
        condition: token_user_api_tokens_create_token_params.Condition | NotGiven = NOT_GIVEN,
        expires_on: Union[str, datetime] | NotGiven = NOT_GIVEN,
        not_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokenUserAPITokensCreateTokenResponse:
        """
        Create a new access token.

        Args:
          name: Token name.

          policies: List of access policies assigned to the token.

          expires_on: The expiration time on or after which the JWT MUST NOT be accepted for
              processing.

          not_before: The time before which the token MUST NOT be accepted for processing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/user/tokens",
            body=maybe_transform(
                {
                    "name": name,
                    "policies": policies,
                    "condition": condition,
                    "expires_on": expires_on,
                    "not_before": not_before,
                },
                token_user_api_tokens_create_token_params.TokenUserAPITokensCreateTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[TokenUserAPITokensCreateTokenResponse], ResultWrapper[TokenUserAPITokensCreateTokenResponse]
            ),
        )

    def user_api_tokens_list_tokens(
        self,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TokenUserAPITokensListTokensResponse]:
        """
        List all access tokens you created.

        Args:
          direction: Direction to order results.

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/user/tokens",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "page": page,
                        "per_page": per_page,
                    },
                    token_user_api_tokens_list_tokens_params.TokenUserAPITokensListTokensParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[TokenUserAPITokensListTokensResponse]],
                ResultWrapper[TokenUserAPITokensListTokensResponse],
            ),
        )


class AsyncTokens(AsyncAPIResource):
    @cached_property
    def permission_groups(self) -> AsyncPermissionGroups:
        return AsyncPermissionGroups(self._client)

    @cached_property
    def verifies(self) -> AsyncVerifies:
        return AsyncVerifies(self._client)

    @cached_property
    def values(self) -> AsyncValues:
        return AsyncValues(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTokensWithRawResponse:
        return AsyncTokensWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTokensWithStreamingResponse:
        return AsyncTokensWithStreamingResponse(self)

    async def update(
        self,
        token_id: object,
        *,
        name: str,
        policies: Iterable[token_update_params.Policy],
        status: Literal["active", "disabled", "expired"],
        condition: token_update_params.Condition | NotGiven = NOT_GIVEN,
        expires_on: Union[str, datetime] | NotGiven = NOT_GIVEN,
        not_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokenUpdateResponse:
        """
        Update an existing token.

        Args:
          name: Token name.

          policies: List of access policies assigned to the token.

          status: Status of the token.

          expires_on: The expiration time on or after which the JWT MUST NOT be accepted for
              processing.

          not_before: The time before which the token MUST NOT be accepted for processing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            TokenUpdateResponse,
            await self._put(
                f"/user/tokens/{token_id}",
                body=maybe_transform(
                    {
                        "name": name,
                        "policies": policies,
                        "status": status,
                        "condition": condition,
                        "expires_on": expires_on,
                        "not_before": not_before,
                    },
                    token_update_params.TokenUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[TokenUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def delete(
        self,
        token_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TokenDeleteResponse]:
        """
        Destroy a token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            f"/user/tokens/{token_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[TokenDeleteResponse]], ResultWrapper[TokenDeleteResponse]),
        )

    async def get(
        self,
        token_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokenGetResponse:
        """
        Get information about a specific token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            TokenGetResponse,
            await self._get(
                f"/user/tokens/{token_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[TokenGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def user_api_tokens_create_token(
        self,
        *,
        name: str,
        policies: Iterable[token_user_api_tokens_create_token_params.Policy],
        condition: token_user_api_tokens_create_token_params.Condition | NotGiven = NOT_GIVEN,
        expires_on: Union[str, datetime] | NotGiven = NOT_GIVEN,
        not_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokenUserAPITokensCreateTokenResponse:
        """
        Create a new access token.

        Args:
          name: Token name.

          policies: List of access policies assigned to the token.

          expires_on: The expiration time on or after which the JWT MUST NOT be accepted for
              processing.

          not_before: The time before which the token MUST NOT be accepted for processing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/user/tokens",
            body=maybe_transform(
                {
                    "name": name,
                    "policies": policies,
                    "condition": condition,
                    "expires_on": expires_on,
                    "not_before": not_before,
                },
                token_user_api_tokens_create_token_params.TokenUserAPITokensCreateTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[TokenUserAPITokensCreateTokenResponse], ResultWrapper[TokenUserAPITokensCreateTokenResponse]
            ),
        )

    async def user_api_tokens_list_tokens(
        self,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TokenUserAPITokensListTokensResponse]:
        """
        List all access tokens you created.

        Args:
          direction: Direction to order results.

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/user/tokens",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "page": page,
                        "per_page": per_page,
                    },
                    token_user_api_tokens_list_tokens_params.TokenUserAPITokensListTokensParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[TokenUserAPITokensListTokensResponse]],
                ResultWrapper[TokenUserAPITokensListTokensResponse],
            ),
        )


class TokensWithRawResponse:
    def __init__(self, tokens: Tokens) -> None:
        self._tokens = tokens

        self.update = to_raw_response_wrapper(
            tokens.update,
        )
        self.delete = to_raw_response_wrapper(
            tokens.delete,
        )
        self.get = to_raw_response_wrapper(
            tokens.get,
        )
        self.user_api_tokens_create_token = to_raw_response_wrapper(
            tokens.user_api_tokens_create_token,
        )
        self.user_api_tokens_list_tokens = to_raw_response_wrapper(
            tokens.user_api_tokens_list_tokens,
        )

    @cached_property
    def permission_groups(self) -> PermissionGroupsWithRawResponse:
        return PermissionGroupsWithRawResponse(self._tokens.permission_groups)

    @cached_property
    def verifies(self) -> VerifiesWithRawResponse:
        return VerifiesWithRawResponse(self._tokens.verifies)

    @cached_property
    def values(self) -> ValuesWithRawResponse:
        return ValuesWithRawResponse(self._tokens.values)


class AsyncTokensWithRawResponse:
    def __init__(self, tokens: AsyncTokens) -> None:
        self._tokens = tokens

        self.update = async_to_raw_response_wrapper(
            tokens.update,
        )
        self.delete = async_to_raw_response_wrapper(
            tokens.delete,
        )
        self.get = async_to_raw_response_wrapper(
            tokens.get,
        )
        self.user_api_tokens_create_token = async_to_raw_response_wrapper(
            tokens.user_api_tokens_create_token,
        )
        self.user_api_tokens_list_tokens = async_to_raw_response_wrapper(
            tokens.user_api_tokens_list_tokens,
        )

    @cached_property
    def permission_groups(self) -> AsyncPermissionGroupsWithRawResponse:
        return AsyncPermissionGroupsWithRawResponse(self._tokens.permission_groups)

    @cached_property
    def verifies(self) -> AsyncVerifiesWithRawResponse:
        return AsyncVerifiesWithRawResponse(self._tokens.verifies)

    @cached_property
    def values(self) -> AsyncValuesWithRawResponse:
        return AsyncValuesWithRawResponse(self._tokens.values)


class TokensWithStreamingResponse:
    def __init__(self, tokens: Tokens) -> None:
        self._tokens = tokens

        self.update = to_streamed_response_wrapper(
            tokens.update,
        )
        self.delete = to_streamed_response_wrapper(
            tokens.delete,
        )
        self.get = to_streamed_response_wrapper(
            tokens.get,
        )
        self.user_api_tokens_create_token = to_streamed_response_wrapper(
            tokens.user_api_tokens_create_token,
        )
        self.user_api_tokens_list_tokens = to_streamed_response_wrapper(
            tokens.user_api_tokens_list_tokens,
        )

    @cached_property
    def permission_groups(self) -> PermissionGroupsWithStreamingResponse:
        return PermissionGroupsWithStreamingResponse(self._tokens.permission_groups)

    @cached_property
    def verifies(self) -> VerifiesWithStreamingResponse:
        return VerifiesWithStreamingResponse(self._tokens.verifies)

    @cached_property
    def values(self) -> ValuesWithStreamingResponse:
        return ValuesWithStreamingResponse(self._tokens.values)


class AsyncTokensWithStreamingResponse:
    def __init__(self, tokens: AsyncTokens) -> None:
        self._tokens = tokens

        self.update = async_to_streamed_response_wrapper(
            tokens.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            tokens.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            tokens.get,
        )
        self.user_api_tokens_create_token = async_to_streamed_response_wrapper(
            tokens.user_api_tokens_create_token,
        )
        self.user_api_tokens_list_tokens = async_to_streamed_response_wrapper(
            tokens.user_api_tokens_list_tokens,
        )

    @cached_property
    def permission_groups(self) -> AsyncPermissionGroupsWithStreamingResponse:
        return AsyncPermissionGroupsWithStreamingResponse(self._tokens.permission_groups)

    @cached_property
    def verifies(self) -> AsyncVerifiesWithStreamingResponse:
        return AsyncVerifiesWithStreamingResponse(self._tokens.verifies)

    @cached_property
    def values(self) -> AsyncValuesWithStreamingResponse:
        return AsyncValuesWithStreamingResponse(self._tokens.values)
