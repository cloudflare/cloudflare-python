# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.access.users import ActiveSessionListResponse, ActiveSessionGetResponse

from typing import Type, Optional

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
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["ActiveSessions", "AsyncActiveSessions"]


class ActiveSessions(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ActiveSessionsWithRawResponse:
        return ActiveSessionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActiveSessionsWithStreamingResponse:
        return ActiveSessionsWithStreamingResponse(self)

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
    ) -> Optional[ActiveSessionListResponse]:
        """
        Get active sessions for a single user.

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
            f"/accounts/{identifier}/access/users/{id}/active_sessions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ActiveSessionListResponse]], ResultWrapper[ActiveSessionListResponse]),
        )

    def get(
        self,
        nonce: str,
        *,
        identifier: str,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActiveSessionGetResponse:
        """
        Get an active session for a single user.

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
        if not nonce:
            raise ValueError(f"Expected a non-empty value for `nonce` but received {nonce!r}")
        return self._get(
            f"/accounts/{identifier}/access/users/{id}/active_sessions/{nonce}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ActiveSessionGetResponse], ResultWrapper[ActiveSessionGetResponse]),
        )


class AsyncActiveSessions(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncActiveSessionsWithRawResponse:
        return AsyncActiveSessionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActiveSessionsWithStreamingResponse:
        return AsyncActiveSessionsWithStreamingResponse(self)

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
    ) -> Optional[ActiveSessionListResponse]:
        """
        Get active sessions for a single user.

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
            f"/accounts/{identifier}/access/users/{id}/active_sessions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ActiveSessionListResponse]], ResultWrapper[ActiveSessionListResponse]),
        )

    async def get(
        self,
        nonce: str,
        *,
        identifier: str,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActiveSessionGetResponse:
        """
        Get an active session for a single user.

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
        if not nonce:
            raise ValueError(f"Expected a non-empty value for `nonce` but received {nonce!r}")
        return await self._get(
            f"/accounts/{identifier}/access/users/{id}/active_sessions/{nonce}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ActiveSessionGetResponse], ResultWrapper[ActiveSessionGetResponse]),
        )


class ActiveSessionsWithRawResponse:
    def __init__(self, active_sessions: ActiveSessions) -> None:
        self._active_sessions = active_sessions

        self.list = to_raw_response_wrapper(
            active_sessions.list,
        )
        self.get = to_raw_response_wrapper(
            active_sessions.get,
        )


class AsyncActiveSessionsWithRawResponse:
    def __init__(self, active_sessions: AsyncActiveSessions) -> None:
        self._active_sessions = active_sessions

        self.list = async_to_raw_response_wrapper(
            active_sessions.list,
        )
        self.get = async_to_raw_response_wrapper(
            active_sessions.get,
        )


class ActiveSessionsWithStreamingResponse:
    def __init__(self, active_sessions: ActiveSessions) -> None:
        self._active_sessions = active_sessions

        self.list = to_streamed_response_wrapper(
            active_sessions.list,
        )
        self.get = to_streamed_response_wrapper(
            active_sessions.get,
        )


class AsyncActiveSessionsWithStreamingResponse:
    def __init__(self, active_sessions: AsyncActiveSessions) -> None:
        self._active_sessions = active_sessions

        self.list = async_to_streamed_response_wrapper(
            active_sessions.list,
        )
        self.get = async_to_streamed_response_wrapper(
            active_sessions.get,
        )
