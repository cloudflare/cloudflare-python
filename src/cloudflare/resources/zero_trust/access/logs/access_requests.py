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
from .....types.zero_trust.access.logs import AccessRequestListResponse

__all__ = ["AccessRequests", "AsyncAccessRequests"]


class AccessRequests(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccessRequestsWithRawResponse:
        return AccessRequestsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccessRequestsWithStreamingResponse:
        return AccessRequestsWithStreamingResponse(self)

    def list(
        self,
        identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AccessRequestListResponse]:
        """
        Gets a list of Access authentication audit logs for an account.

        Args:
          identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._get(
            f"/accounts/{identifier}/access/logs/access_requests",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[AccessRequestListResponse]], ResultWrapper[AccessRequestListResponse]),
        )


class AsyncAccessRequests(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccessRequestsWithRawResponse:
        return AsyncAccessRequestsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccessRequestsWithStreamingResponse:
        return AsyncAccessRequestsWithStreamingResponse(self)

    async def list(
        self,
        identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AccessRequestListResponse]:
        """
        Gets a list of Access authentication audit logs for an account.

        Args:
          identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return await self._get(
            f"/accounts/{identifier}/access/logs/access_requests",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[AccessRequestListResponse]], ResultWrapper[AccessRequestListResponse]),
        )


class AccessRequestsWithRawResponse:
    def __init__(self, access_requests: AccessRequests) -> None:
        self._access_requests = access_requests

        self.list = to_raw_response_wrapper(
            access_requests.list,
        )


class AsyncAccessRequestsWithRawResponse:
    def __init__(self, access_requests: AsyncAccessRequests) -> None:
        self._access_requests = access_requests

        self.list = async_to_raw_response_wrapper(
            access_requests.list,
        )


class AccessRequestsWithStreamingResponse:
    def __init__(self, access_requests: AccessRequests) -> None:
        self._access_requests = access_requests

        self.list = to_streamed_response_wrapper(
            access_requests.list,
        )


class AsyncAccessRequestsWithStreamingResponse:
    def __init__(self, access_requests: AsyncAccessRequests) -> None:
        self._access_requests = access_requests

        self.list = async_to_streamed_response_wrapper(
            access_requests.list,
        )
