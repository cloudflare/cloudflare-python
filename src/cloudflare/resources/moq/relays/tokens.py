# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, Optional, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import make_request_options
from ....types.moq.relays import token_create_params
from ....types.moq.relays.token_list_response import TokenListResponse
from ....types.moq.relays.token_create_response import TokenCreateResponse
from ....types.moq.relays.token_delete_response import TokenDeleteResponse

__all__ = ["TokensResource", "AsyncTokensResource"]


class TokensResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TokensResourceWithStreamingResponse(self)

    def create(
        self,
        relay_id: str,
        *,
        account_id: str,
        operations: List[Literal["publish", "subscribe"]],
        expires: Union[str, datetime] | Omit = omit,
        label: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[TokenCreateResponse]:
        """Mints a new relay-scoped token and adds it to the relay's accepted-auth
        registry.

        The token value (secret) is shown once in the response. A relay may
        hold up to 10 tokens; creating an 11th is rejected.

        Args:
          account_id: Cloudflare account identifier.

          operations: Non-empty subset of the V1 roles the token is allowed to perform. Signed into
              the token.

          expires: Optional expiry (RFC 3339). Defaults to 1 year from creation; rejected if more
              than 1 year in the future.

          label: Optional, customer-set label.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not relay_id:
            raise ValueError(f"Expected a non-empty value for `relay_id` but received {relay_id!r}")
        return self._post(
            path_template(
                "/accounts/{account_id}/moq/relays/{relay_id}/tokens", account_id=account_id, relay_id=relay_id
            ),
            body=maybe_transform(
                {
                    "operations": operations,
                    "expires": expires,
                    "label": label,
                },
                token_create_params.TokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TokenCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TokenCreateResponse]], ResultWrapper[TokenCreateResponse]),
        )

    def list(
        self,
        relay_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[TokenListResponse]:
        """Returns metadata for every token in the relay's registry.

        Secrets are never
        returned. The dashboard derives an `expired` flag by comparing each token's
        `expires` to the current time.

        Args:
          account_id: Cloudflare account identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not relay_id:
            raise ValueError(f"Expected a non-empty value for `relay_id` but received {relay_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/moq/relays/{relay_id}/tokens", account_id=account_id, relay_id=relay_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TokenListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TokenListResponse]], ResultWrapper[TokenListResponse]),
        )

    def delete(
        self,
        jti: str,
        *,
        account_id: str,
        relay_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenDeleteResponse:
        """Revokes a token by removing it from the relay's registry.

        crique rejects the
        token within the cache TTL. Idempotent — revoking an unknown token succeeds.

        Args:
          account_id: Cloudflare account identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not relay_id:
            raise ValueError(f"Expected a non-empty value for `relay_id` but received {relay_id!r}")
        if not jti:
            raise ValueError(f"Expected a non-empty value for `jti` but received {jti!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/moq/relays/{relay_id}/tokens/{jti}",
                account_id=account_id,
                relay_id=relay_id,
                jti=jti,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenDeleteResponse,
        )


class AsyncTokensResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTokensResourceWithStreamingResponse(self)

    async def create(
        self,
        relay_id: str,
        *,
        account_id: str,
        operations: List[Literal["publish", "subscribe"]],
        expires: Union[str, datetime] | Omit = omit,
        label: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[TokenCreateResponse]:
        """Mints a new relay-scoped token and adds it to the relay's accepted-auth
        registry.

        The token value (secret) is shown once in the response. A relay may
        hold up to 10 tokens; creating an 11th is rejected.

        Args:
          account_id: Cloudflare account identifier.

          operations: Non-empty subset of the V1 roles the token is allowed to perform. Signed into
              the token.

          expires: Optional expiry (RFC 3339). Defaults to 1 year from creation; rejected if more
              than 1 year in the future.

          label: Optional, customer-set label.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not relay_id:
            raise ValueError(f"Expected a non-empty value for `relay_id` but received {relay_id!r}")
        return await self._post(
            path_template(
                "/accounts/{account_id}/moq/relays/{relay_id}/tokens", account_id=account_id, relay_id=relay_id
            ),
            body=await async_maybe_transform(
                {
                    "operations": operations,
                    "expires": expires,
                    "label": label,
                },
                token_create_params.TokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TokenCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TokenCreateResponse]], ResultWrapper[TokenCreateResponse]),
        )

    async def list(
        self,
        relay_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[TokenListResponse]:
        """Returns metadata for every token in the relay's registry.

        Secrets are never
        returned. The dashboard derives an `expired` flag by comparing each token's
        `expires` to the current time.

        Args:
          account_id: Cloudflare account identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not relay_id:
            raise ValueError(f"Expected a non-empty value for `relay_id` but received {relay_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/moq/relays/{relay_id}/tokens", account_id=account_id, relay_id=relay_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TokenListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TokenListResponse]], ResultWrapper[TokenListResponse]),
        )

    async def delete(
        self,
        jti: str,
        *,
        account_id: str,
        relay_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenDeleteResponse:
        """Revokes a token by removing it from the relay's registry.

        crique rejects the
        token within the cache TTL. Idempotent — revoking an unknown token succeeds.

        Args:
          account_id: Cloudflare account identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not relay_id:
            raise ValueError(f"Expected a non-empty value for `relay_id` but received {relay_id!r}")
        if not jti:
            raise ValueError(f"Expected a non-empty value for `jti` but received {jti!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/moq/relays/{relay_id}/tokens/{jti}",
                account_id=account_id,
                relay_id=relay_id,
                jti=jti,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenDeleteResponse,
        )


class TokensResourceWithRawResponse:
    def __init__(self, tokens: TokensResource) -> None:
        self._tokens = tokens

        self.create = to_raw_response_wrapper(
            tokens.create,
        )
        self.list = to_raw_response_wrapper(
            tokens.list,
        )
        self.delete = to_raw_response_wrapper(
            tokens.delete,
        )


class AsyncTokensResourceWithRawResponse:
    def __init__(self, tokens: AsyncTokensResource) -> None:
        self._tokens = tokens

        self.create = async_to_raw_response_wrapper(
            tokens.create,
        )
        self.list = async_to_raw_response_wrapper(
            tokens.list,
        )
        self.delete = async_to_raw_response_wrapper(
            tokens.delete,
        )


class TokensResourceWithStreamingResponse:
    def __init__(self, tokens: TokensResource) -> None:
        self._tokens = tokens

        self.create = to_streamed_response_wrapper(
            tokens.create,
        )
        self.list = to_streamed_response_wrapper(
            tokens.list,
        )
        self.delete = to_streamed_response_wrapper(
            tokens.delete,
        )


class AsyncTokensResourceWithStreamingResponse:
    def __init__(self, tokens: AsyncTokensResource) -> None:
        self._tokens = tokens

        self.create = async_to_streamed_response_wrapper(
            tokens.create,
        )
        self.list = async_to_streamed_response_wrapper(
            tokens.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            tokens.delete,
        )
