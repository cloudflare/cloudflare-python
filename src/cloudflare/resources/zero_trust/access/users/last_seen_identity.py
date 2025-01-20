# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from .....types.zero_trust.access.users.identity import Identity

__all__ = ["LastSeenIdentityResource", "AsyncLastSeenIdentityResource"]


class LastSeenIdentityResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LastSeenIdentityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return LastSeenIdentityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LastSeenIdentityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return LastSeenIdentityResourceWithStreamingResponse(self)

    def get(
        self,
        user_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Identity]:
        """
        Get last seen identity for a single user.

        Args:
          account_id: Identifier

          user_id: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            f"/accounts/{account_id}/access/users/{user_id}/last_seen_identity",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Identity]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Identity]], ResultWrapper[Identity]),
        )


class AsyncLastSeenIdentityResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLastSeenIdentityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLastSeenIdentityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLastSeenIdentityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncLastSeenIdentityResourceWithStreamingResponse(self)

    async def get(
        self,
        user_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Identity]:
        """
        Get last seen identity for a single user.

        Args:
          account_id: Identifier

          user_id: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            f"/accounts/{account_id}/access/users/{user_id}/last_seen_identity",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Identity]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Identity]], ResultWrapper[Identity]),
        )


class LastSeenIdentityResourceWithRawResponse:
    def __init__(self, last_seen_identity: LastSeenIdentityResource) -> None:
        self._last_seen_identity = last_seen_identity

        self.get = to_raw_response_wrapper(
            last_seen_identity.get,
        )


class AsyncLastSeenIdentityResourceWithRawResponse:
    def __init__(self, last_seen_identity: AsyncLastSeenIdentityResource) -> None:
        self._last_seen_identity = last_seen_identity

        self.get = async_to_raw_response_wrapper(
            last_seen_identity.get,
        )


class LastSeenIdentityResourceWithStreamingResponse:
    def __init__(self, last_seen_identity: LastSeenIdentityResource) -> None:
        self._last_seen_identity = last_seen_identity

        self.get = to_streamed_response_wrapper(
            last_seen_identity.get,
        )


class AsyncLastSeenIdentityResourceWithStreamingResponse:
    def __init__(self, last_seen_identity: AsyncLastSeenIdentityResource) -> None:
        self._last_seen_identity = last_seen_identity

        self.get = async_to_streamed_response_wrapper(
            last_seen_identity.get,
        )
