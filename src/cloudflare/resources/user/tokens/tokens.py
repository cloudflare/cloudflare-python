# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, Union, Iterable, Optional, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from .value import (
    Value,
    AsyncValue,
    ValueWithRawResponse,
    AsyncValueWithRawResponse,
    ValueWithStreamingResponse,
    AsyncValueWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ....types.user import (
    TokenGetResponse,
    TokenCreateResponse,
    TokenDeleteResponse,
    TokenUpdateResponse,
    TokenVerifyResponse,
    token_list_params,
    token_create_params,
    token_update_params,
)
from ...._base_client import (
    AsyncPaginator,
    make_request_options,
)
from .permission_groups import (
    PermissionGroups,
    AsyncPermissionGroups,
    PermissionGroupsWithRawResponse,
    AsyncPermissionGroupsWithRawResponse,
    PermissionGroupsWithStreamingResponse,
    AsyncPermissionGroupsWithStreamingResponse,
)

__all__ = ["Tokens", "AsyncTokens"]


class Tokens(SyncAPIResource):
    @cached_property
    def permission_groups(self) -> PermissionGroups:
        return PermissionGroups(self._client)

    @cached_property
    def value(self) -> Value:
        return Value(self._client)

    @cached_property
    def with_raw_response(self) -> TokensWithRawResponse:
        return TokensWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TokensWithStreamingResponse:
        return TokensWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        policies: Iterable[token_create_params.Policy],
        condition: token_create_params.Condition | NotGiven = NOT_GIVEN,
        expires_on: Union[str, datetime] | NotGiven = NOT_GIVEN,
        not_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokenCreateResponse:
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
                token_create_params.TokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TokenCreateResponse], ResultWrapper[TokenCreateResponse]),
        )

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

    def list(
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
    ) -> SyncV4PagePaginationArray[object]:
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
        return self._get_api_list(
            "/user/tokens",
            page=SyncV4PagePaginationArray[object],
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
                    token_list_params.TokenListParams,
                ),
            ),
            model=object,
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

    def verify(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokenVerifyResponse:
        """Test whether a token works."""
        return self._get(
            "/user/tokens/verify",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TokenVerifyResponse], ResultWrapper[TokenVerifyResponse]),
        )


class AsyncTokens(AsyncAPIResource):
    @cached_property
    def permission_groups(self) -> AsyncPermissionGroups:
        return AsyncPermissionGroups(self._client)

    @cached_property
    def value(self) -> AsyncValue:
        return AsyncValue(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTokensWithRawResponse:
        return AsyncTokensWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTokensWithStreamingResponse:
        return AsyncTokensWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        policies: Iterable[token_create_params.Policy],
        condition: token_create_params.Condition | NotGiven = NOT_GIVEN,
        expires_on: Union[str, datetime] | NotGiven = NOT_GIVEN,
        not_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokenCreateResponse:
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
            body=await async_maybe_transform(
                {
                    "name": name,
                    "policies": policies,
                    "condition": condition,
                    "expires_on": expires_on,
                    "not_before": not_before,
                },
                token_create_params.TokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TokenCreateResponse], ResultWrapper[TokenCreateResponse]),
        )

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
                body=await async_maybe_transform(
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

    def list(
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
    ) -> AsyncPaginator[object, AsyncV4PagePaginationArray[object]]:
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
        return self._get_api_list(
            "/user/tokens",
            page=AsyncV4PagePaginationArray[object],
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
                    token_list_params.TokenListParams,
                ),
            ),
            model=object,
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

    async def verify(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokenVerifyResponse:
        """Test whether a token works."""
        return await self._get(
            "/user/tokens/verify",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TokenVerifyResponse], ResultWrapper[TokenVerifyResponse]),
        )


class TokensWithRawResponse:
    def __init__(self, tokens: Tokens) -> None:
        self._tokens = tokens

        self.create = to_raw_response_wrapper(
            tokens.create,
        )
        self.update = to_raw_response_wrapper(
            tokens.update,
        )
        self.list = to_raw_response_wrapper(
            tokens.list,
        )
        self.delete = to_raw_response_wrapper(
            tokens.delete,
        )
        self.get = to_raw_response_wrapper(
            tokens.get,
        )
        self.verify = to_raw_response_wrapper(
            tokens.verify,
        )

    @cached_property
    def permission_groups(self) -> PermissionGroupsWithRawResponse:
        return PermissionGroupsWithRawResponse(self._tokens.permission_groups)

    @cached_property
    def value(self) -> ValueWithRawResponse:
        return ValueWithRawResponse(self._tokens.value)


class AsyncTokensWithRawResponse:
    def __init__(self, tokens: AsyncTokens) -> None:
        self._tokens = tokens

        self.create = async_to_raw_response_wrapper(
            tokens.create,
        )
        self.update = async_to_raw_response_wrapper(
            tokens.update,
        )
        self.list = async_to_raw_response_wrapper(
            tokens.list,
        )
        self.delete = async_to_raw_response_wrapper(
            tokens.delete,
        )
        self.get = async_to_raw_response_wrapper(
            tokens.get,
        )
        self.verify = async_to_raw_response_wrapper(
            tokens.verify,
        )

    @cached_property
    def permission_groups(self) -> AsyncPermissionGroupsWithRawResponse:
        return AsyncPermissionGroupsWithRawResponse(self._tokens.permission_groups)

    @cached_property
    def value(self) -> AsyncValueWithRawResponse:
        return AsyncValueWithRawResponse(self._tokens.value)


class TokensWithStreamingResponse:
    def __init__(self, tokens: Tokens) -> None:
        self._tokens = tokens

        self.create = to_streamed_response_wrapper(
            tokens.create,
        )
        self.update = to_streamed_response_wrapper(
            tokens.update,
        )
        self.list = to_streamed_response_wrapper(
            tokens.list,
        )
        self.delete = to_streamed_response_wrapper(
            tokens.delete,
        )
        self.get = to_streamed_response_wrapper(
            tokens.get,
        )
        self.verify = to_streamed_response_wrapper(
            tokens.verify,
        )

    @cached_property
    def permission_groups(self) -> PermissionGroupsWithStreamingResponse:
        return PermissionGroupsWithStreamingResponse(self._tokens.permission_groups)

    @cached_property
    def value(self) -> ValueWithStreamingResponse:
        return ValueWithStreamingResponse(self._tokens.value)


class AsyncTokensWithStreamingResponse:
    def __init__(self, tokens: AsyncTokens) -> None:
        self._tokens = tokens

        self.create = async_to_streamed_response_wrapper(
            tokens.create,
        )
        self.update = async_to_streamed_response_wrapper(
            tokens.update,
        )
        self.list = async_to_streamed_response_wrapper(
            tokens.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            tokens.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            tokens.get,
        )
        self.verify = async_to_streamed_response_wrapper(
            tokens.verify,
        )

    @cached_property
    def permission_groups(self) -> AsyncPermissionGroupsWithStreamingResponse:
        return AsyncPermissionGroupsWithStreamingResponse(self._tokens.permission_groups)

    @cached_property
    def value(self) -> AsyncValueWithStreamingResponse:
        return AsyncValueWithStreamingResponse(self._tokens.value)
