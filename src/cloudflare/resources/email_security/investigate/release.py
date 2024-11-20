# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, cast

import httpx

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
from ...._base_client import make_request_options
from ....types.email_security.investigate.release_bulk_response import ReleaseBulkResponse

__all__ = ["ReleaseResource", "AsyncReleaseResource"]


class ReleaseResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReleaseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ReleaseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReleaseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ReleaseResourceWithStreamingResponse(self)

    def bulk(
        self,
        *,
        account_id: str,
        body: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReleaseBulkResponse:
        """
        Release messages from quarantine

        Args:
          account_id: Account Identifier

          body: A list of messages identfied by their `postfix_id`s that should be released.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/email-security/investigate/release",
            body=maybe_transform(body, List[str]),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ReleaseBulkResponse]._unwrapper,
            ),
            cast_to=cast(Type[ReleaseBulkResponse], ResultWrapper[ReleaseBulkResponse]),
        )


class AsyncReleaseResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReleaseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReleaseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReleaseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncReleaseResourceWithStreamingResponse(self)

    async def bulk(
        self,
        *,
        account_id: str,
        body: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReleaseBulkResponse:
        """
        Release messages from quarantine

        Args:
          account_id: Account Identifier

          body: A list of messages identfied by their `postfix_id`s that should be released.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/email-security/investigate/release",
            body=await async_maybe_transform(body, List[str]),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ReleaseBulkResponse]._unwrapper,
            ),
            cast_to=cast(Type[ReleaseBulkResponse], ResultWrapper[ReleaseBulkResponse]),
        )


class ReleaseResourceWithRawResponse:
    def __init__(self, release: ReleaseResource) -> None:
        self._release = release

        self.bulk = to_raw_response_wrapper(
            release.bulk,
        )


class AsyncReleaseResourceWithRawResponse:
    def __init__(self, release: AsyncReleaseResource) -> None:
        self._release = release

        self.bulk = async_to_raw_response_wrapper(
            release.bulk,
        )


class ReleaseResourceWithStreamingResponse:
    def __init__(self, release: ReleaseResource) -> None:
        self._release = release

        self.bulk = to_streamed_response_wrapper(
            release.bulk,
        )


class AsyncReleaseResourceWithStreamingResponse:
    def __init__(self, release: AsyncReleaseResource) -> None:
        self._release = release

        self.bulk = async_to_streamed_response_wrapper(
            release.bulk,
        )
