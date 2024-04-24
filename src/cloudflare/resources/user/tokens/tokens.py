# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, Union, Iterable, Optional, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from .value import (
    ValueResource,
    AsyncValueResource,
    ValueResourceWithRawResponse,
    AsyncValueResourceWithRawResponse,
    ValueResourceWithStreamingResponse,
    AsyncValueResourceWithStreamingResponse,
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
from ....types.user import token_list_params, token_create_params, token_update_params
from ...._base_client import (
    AsyncPaginator,
    make_request_options,
)
from .permission_groups import (
    PermissionGroupsResource,
    AsyncPermissionGroupsResource,
    PermissionGroupsResourceWithRawResponse,
    AsyncPermissionGroupsResourceWithRawResponse,
    PermissionGroupsResourceWithStreamingResponse,
    AsyncPermissionGroupsResourceWithStreamingResponse,
)
from ....types.user.policy_param import PolicyParam
from ....types.user.token_get_response import TokenGetResponse
from ....types.user.token_create_response import TokenCreateResponse
from ....types.user.token_delete_response import TokenDeleteResponse
from ....types.user.token_update_response import TokenUpdateResponse
from ....types.user.token_verify_response import TokenVerifyResponse

__all__ = ["TokensResource", "AsyncTokensResource"]


class TokensResource(SyncAPIResource):
    @cached_property
    def permission_groups(self) -> PermissionGroupsResource:
        return PermissionGroupsResource(self._client)

    @cached_property
    def value(self) -> ValueResource:
        return ValueResource(self._client)

    @cached_property
    def with_raw_response(self) -> TokensResourceWithRawResponse:
        return TokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TokensResourceWithStreamingResponse:
        return TokensResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        policies: Iterable[PolicyParam],
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
                post_parser=ResultWrapper[TokenCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[TokenCreateResponse], ResultWrapper[TokenCreateResponse]),
        )

    def update(
        self,
        token_id: object,
        *,
        name: str,
        policies: Iterable[PolicyParam],
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
                    post_parser=ResultWrapper[TokenUpdateResponse]._unwrapper,
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
                post_parser=ResultWrapper[Optional[TokenDeleteResponse]]._unwrapper,
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
                    post_parser=ResultWrapper[TokenGetResponse]._unwrapper,
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
                post_parser=ResultWrapper[TokenVerifyResponse]._unwrapper,
            ),
            cast_to=cast(Type[TokenVerifyResponse], ResultWrapper[TokenVerifyResponse]),
        )


class AsyncTokensResource(AsyncAPIResource):
    @cached_property
    def permission_groups(self) -> AsyncPermissionGroupsResource:
        return AsyncPermissionGroupsResource(self._client)

    @cached_property
    def value(self) -> AsyncValueResource:
        return AsyncValueResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTokensResourceWithRawResponse:
        return AsyncTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTokensResourceWithStreamingResponse:
        return AsyncTokensResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        policies: Iterable[PolicyParam],
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
                post_parser=ResultWrapper[TokenCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[TokenCreateResponse], ResultWrapper[TokenCreateResponse]),
        )

    async def update(
        self,
        token_id: object,
        *,
        name: str,
        policies: Iterable[PolicyParam],
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
                    post_parser=ResultWrapper[TokenUpdateResponse]._unwrapper,
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
                post_parser=ResultWrapper[Optional[TokenDeleteResponse]]._unwrapper,
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
                    post_parser=ResultWrapper[TokenGetResponse]._unwrapper,
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
                post_parser=ResultWrapper[TokenVerifyResponse]._unwrapper,
            ),
            cast_to=cast(Type[TokenVerifyResponse], ResultWrapper[TokenVerifyResponse]),
        )


class TokensResourceWithRawResponse:
    def __init__(self, tokens: TokensResource) -> None:
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
    def permission_groups(self) -> PermissionGroupsResourceWithRawResponse:
        return PermissionGroupsResourceWithRawResponse(self._tokens.permission_groups)

    @cached_property
    def value(self) -> ValueResourceWithRawResponse:
        return ValueResourceWithRawResponse(self._tokens.value)


class AsyncTokensResourceWithRawResponse:
    def __init__(self, tokens: AsyncTokensResource) -> None:
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
    def permission_groups(self) -> AsyncPermissionGroupsResourceWithRawResponse:
        return AsyncPermissionGroupsResourceWithRawResponse(self._tokens.permission_groups)

    @cached_property
    def value(self) -> AsyncValueResourceWithRawResponse:
        return AsyncValueResourceWithRawResponse(self._tokens.value)


class TokensResourceWithStreamingResponse:
    def __init__(self, tokens: TokensResource) -> None:
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
    def permission_groups(self) -> PermissionGroupsResourceWithStreamingResponse:
        return PermissionGroupsResourceWithStreamingResponse(self._tokens.permission_groups)

    @cached_property
    def value(self) -> ValueResourceWithStreamingResponse:
        return ValueResourceWithStreamingResponse(self._tokens.value)


class AsyncTokensResourceWithStreamingResponse:
    def __init__(self, tokens: AsyncTokensResource) -> None:
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
    def permission_groups(self) -> AsyncPermissionGroupsResourceWithStreamingResponse:
        return AsyncPermissionGroupsResourceWithStreamingResponse(self._tokens.permission_groups)

    @cached_property
    def value(self) -> AsyncValueResourceWithStreamingResponse:
        return AsyncValueResourceWithStreamingResponse(self._tokens.value)
