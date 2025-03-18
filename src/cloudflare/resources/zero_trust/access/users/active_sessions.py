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
from .....pagination import SyncSinglePage, AsyncSinglePage
from ....._base_client import AsyncPaginator, make_request_options
from .....types.zero_trust.access.users.active_session_get_response import ActiveSessionGetResponse
from .....types.zero_trust.access.users.active_session_list_response import ActiveSessionListResponse

__all__ = ["ActiveSessionsResource", "AsyncActiveSessionsResource"]


class ActiveSessionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ActiveSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ActiveSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActiveSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ActiveSessionsResourceWithStreamingResponse(self)

    def list(
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
    ) -> SyncSinglePage[ActiveSessionListResponse]:
        """
        Get active sessions for a single user.

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
        return self._get_api_list(
            f"/accounts/{account_id}/access/users/{user_id}/active_sessions",
            page=SyncSinglePage[ActiveSessionListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=ActiveSessionListResponse,
        )

    def get(
        self,
        nonce: str,
        *,
        account_id: str,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ActiveSessionGetResponse]:
        """
        Get an active session for a single user.

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
        if not nonce:
            raise ValueError(f"Expected a non-empty value for `nonce` but received {nonce!r}")
        return self._get(
            f"/accounts/{account_id}/access/users/{user_id}/active_sessions/{nonce}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ActiveSessionGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ActiveSessionGetResponse]], ResultWrapper[ActiveSessionGetResponse]),
        )


class AsyncActiveSessionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncActiveSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncActiveSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActiveSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncActiveSessionsResourceWithStreamingResponse(self)

    def list(
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
    ) -> AsyncPaginator[ActiveSessionListResponse, AsyncSinglePage[ActiveSessionListResponse]]:
        """
        Get active sessions for a single user.

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
        return self._get_api_list(
            f"/accounts/{account_id}/access/users/{user_id}/active_sessions",
            page=AsyncSinglePage[ActiveSessionListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=ActiveSessionListResponse,
        )

    async def get(
        self,
        nonce: str,
        *,
        account_id: str,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ActiveSessionGetResponse]:
        """
        Get an active session for a single user.

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
        if not nonce:
            raise ValueError(f"Expected a non-empty value for `nonce` but received {nonce!r}")
        return await self._get(
            f"/accounts/{account_id}/access/users/{user_id}/active_sessions/{nonce}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ActiveSessionGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ActiveSessionGetResponse]], ResultWrapper[ActiveSessionGetResponse]),
        )


class ActiveSessionsResourceWithRawResponse:
    def __init__(self, active_sessions: ActiveSessionsResource) -> None:
        self._active_sessions = active_sessions

        self.list = to_raw_response_wrapper(
            active_sessions.list,
        )
        self.get = to_raw_response_wrapper(
            active_sessions.get,
        )


class AsyncActiveSessionsResourceWithRawResponse:
    def __init__(self, active_sessions: AsyncActiveSessionsResource) -> None:
        self._active_sessions = active_sessions

        self.list = async_to_raw_response_wrapper(
            active_sessions.list,
        )
        self.get = async_to_raw_response_wrapper(
            active_sessions.get,
        )


class ActiveSessionsResourceWithStreamingResponse:
    def __init__(self, active_sessions: ActiveSessionsResource) -> None:
        self._active_sessions = active_sessions

        self.list = to_streamed_response_wrapper(
            active_sessions.list,
        )
        self.get = to_streamed_response_wrapper(
            active_sessions.get,
        )


class AsyncActiveSessionsResourceWithStreamingResponse:
    def __init__(self, active_sessions: AsyncActiveSessionsResource) -> None:
        self._active_sessions = active_sessions

        self.list = async_to_streamed_response_wrapper(
            active_sessions.list,
        )
        self.get = async_to_streamed_response_wrapper(
            active_sessions.get,
        )
