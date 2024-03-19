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
from ....._base_client import (
    make_request_options,
)
from .....types.zero_trust.access.users import FailedLoginListResponse

__all__ = ["FailedLogins", "AsyncFailedLogins"]


class FailedLogins(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FailedLoginsWithRawResponse:
        return FailedLoginsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FailedLoginsWithStreamingResponse:
        return FailedLoginsWithStreamingResponse(self)

    def list(
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
    ) -> Optional[FailedLoginListResponse]:
        """
        Get all failed login attempts for a single user.

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
            f"/accounts/{identifier}/access/users/{id}/failed_logins",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[FailedLoginListResponse]], ResultWrapper[FailedLoginListResponse]),
        )


class AsyncFailedLogins(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFailedLoginsWithRawResponse:
        return AsyncFailedLoginsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFailedLoginsWithStreamingResponse:
        return AsyncFailedLoginsWithStreamingResponse(self)

    async def list(
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
    ) -> Optional[FailedLoginListResponse]:
        """
        Get all failed login attempts for a single user.

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
            f"/accounts/{identifier}/access/users/{id}/failed_logins",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[FailedLoginListResponse]], ResultWrapper[FailedLoginListResponse]),
        )


class FailedLoginsWithRawResponse:
    def __init__(self, failed_logins: FailedLogins) -> None:
        self._failed_logins = failed_logins

        self.list = to_raw_response_wrapper(
            failed_logins.list,
        )


class AsyncFailedLoginsWithRawResponse:
    def __init__(self, failed_logins: AsyncFailedLogins) -> None:
        self._failed_logins = failed_logins

        self.list = async_to_raw_response_wrapper(
            failed_logins.list,
        )


class FailedLoginsWithStreamingResponse:
    def __init__(self, failed_logins: FailedLogins) -> None:
        self._failed_logins = failed_logins

        self.list = to_streamed_response_wrapper(
            failed_logins.list,
        )


class AsyncFailedLoginsWithStreamingResponse:
    def __init__(self, failed_logins: AsyncFailedLogins) -> None:
        self._failed_logins = failed_logins

        self.list = async_to_streamed_response_wrapper(
            failed_logins.list,
        )
