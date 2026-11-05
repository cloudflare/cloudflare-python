# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ....._types import Body, Query, Headers, NotGiven, not_given
from ....._utils import path_template
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from ....._base_client import make_request_options

__all__ = ["PasskeysResource", "AsyncPasskeysResource"]


class PasskeysResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PasskeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PasskeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PasskeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PasskeysResourceWithStreamingResponse(self)

    def delete(
        self,
        authenticator_id: str,
        *,
        account_id: str,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Alias of the authenticator deletion endpoint for passkey management.

        The
        identifier is the passkey's authenticator ID from the last-seen identity
        response. Successful deletion revokes the enrollment and returns a null result.

        Args:
          account_id: Identifier.

          user_id: UUID.

          authenticator_id: The unique identifier for the MFA device.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not authenticator_id:
            raise ValueError(f"Expected a non-empty value for `authenticator_id` but received {authenticator_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/access/users/{user_id}/passkeys/{authenticator_id}",
                account_id=account_id,
                user_id=user_id,
                authenticator_id=authenticator_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )


class AsyncPasskeysResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPasskeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPasskeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPasskeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPasskeysResourceWithStreamingResponse(self)

    async def delete(
        self,
        authenticator_id: str,
        *,
        account_id: str,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Alias of the authenticator deletion endpoint for passkey management.

        The
        identifier is the passkey's authenticator ID from the last-seen identity
        response. Successful deletion revokes the enrollment and returns a null result.

        Args:
          account_id: Identifier.

          user_id: UUID.

          authenticator_id: The unique identifier for the MFA device.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not authenticator_id:
            raise ValueError(f"Expected a non-empty value for `authenticator_id` but received {authenticator_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/access/users/{user_id}/passkeys/{authenticator_id}",
                account_id=account_id,
                user_id=user_id,
                authenticator_id=authenticator_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )


class PasskeysResourceWithRawResponse:
    def __init__(self, passkeys: PasskeysResource) -> None:
        self._passkeys = passkeys

        self.delete = to_raw_response_wrapper(
            passkeys.delete,
        )


class AsyncPasskeysResourceWithRawResponse:
    def __init__(self, passkeys: AsyncPasskeysResource) -> None:
        self._passkeys = passkeys

        self.delete = async_to_raw_response_wrapper(
            passkeys.delete,
        )


class PasskeysResourceWithStreamingResponse:
    def __init__(self, passkeys: PasskeysResource) -> None:
        self._passkeys = passkeys

        self.delete = to_streamed_response_wrapper(
            passkeys.delete,
        )


class AsyncPasskeysResourceWithStreamingResponse:
    def __init__(self, passkeys: AsyncPasskeysResource) -> None:
        self._passkeys = passkeys

        self.delete = async_to_streamed_response_wrapper(
            passkeys.delete,
        )
