# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

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
from ....._base_client import (
    make_request_options,
)
from .....types.zero_trust.access.users import AccessIdentity

__all__ = ["LastSeenIdentity", "AsyncLastSeenIdentity"]


class LastSeenIdentity(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LastSeenIdentityWithRawResponse:
        return LastSeenIdentityWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LastSeenIdentityWithStreamingResponse:
        return LastSeenIdentityWithStreamingResponse(self)

    def get(
        self,
        id: str,
        *,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessIdentity:
        """
        Get last seen identity for a single user.

        Args:
          identifier: Identifier

          id: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/accounts/{identifier}/access/users/{id}/last_seen_identity",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AccessIdentity], ResultWrapper[AccessIdentity]),
        )


class AsyncLastSeenIdentity(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLastSeenIdentityWithRawResponse:
        return AsyncLastSeenIdentityWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLastSeenIdentityWithStreamingResponse:
        return AsyncLastSeenIdentityWithStreamingResponse(self)

    async def get(
        self,
        id: str,
        *,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessIdentity:
        """
        Get last seen identity for a single user.

        Args:
          identifier: Identifier

          id: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/accounts/{identifier}/access/users/{id}/last_seen_identity",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AccessIdentity], ResultWrapper[AccessIdentity]),
        )


class LastSeenIdentityWithRawResponse:
    def __init__(self, last_seen_identity: LastSeenIdentity) -> None:
        self._last_seen_identity = last_seen_identity

        self.get = to_raw_response_wrapper(
            last_seen_identity.get,
        )


class AsyncLastSeenIdentityWithRawResponse:
    def __init__(self, last_seen_identity: AsyncLastSeenIdentity) -> None:
        self._last_seen_identity = last_seen_identity

        self.get = async_to_raw_response_wrapper(
            last_seen_identity.get,
        )


class LastSeenIdentityWithStreamingResponse:
    def __init__(self, last_seen_identity: LastSeenIdentity) -> None:
        self._last_seen_identity = last_seen_identity

        self.get = to_streamed_response_wrapper(
            last_seen_identity.get,
        )


class AsyncLastSeenIdentityWithStreamingResponse:
    def __init__(self, last_seen_identity: AsyncLastSeenIdentity) -> None:
        self._last_seen_identity = last_seen_identity

        self.get = async_to_streamed_response_wrapper(
            last_seen_identity.get,
        )
