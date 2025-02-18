# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ....types.email_security.investigate.raw_get_response import RawGetResponse

__all__ = ["RawResource", "AsyncRawResource"]


class RawResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RawResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RawResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RawResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RawResourceWithStreamingResponse(self)

    def get(
        self,
        postfix_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RawGetResponse:
        """
        Returns the raw eml of any non-benign message.

        Args:
          account_id: Account Identifier

          postfix_id: The identifier of the message.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not postfix_id:
            raise ValueError(f"Expected a non-empty value for `postfix_id` but received {postfix_id!r}")
        return self._get(
            f"/accounts/{account_id}/email-security/investigate/{postfix_id}/raw",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RawGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[RawGetResponse], ResultWrapper[RawGetResponse]),
        )


class AsyncRawResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRawResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRawResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRawResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncRawResourceWithStreamingResponse(self)

    async def get(
        self,
        postfix_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RawGetResponse:
        """
        Returns the raw eml of any non-benign message.

        Args:
          account_id: Account Identifier

          postfix_id: The identifier of the message.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not postfix_id:
            raise ValueError(f"Expected a non-empty value for `postfix_id` but received {postfix_id!r}")
        return await self._get(
            f"/accounts/{account_id}/email-security/investigate/{postfix_id}/raw",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RawGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[RawGetResponse], ResultWrapper[RawGetResponse]),
        )


class RawResourceWithRawResponse:
    def __init__(self, raw: RawResource) -> None:
        self._raw = raw

        self.get = to_raw_response_wrapper(
            raw.get,
        )


class AsyncRawResourceWithRawResponse:
    def __init__(self, raw: AsyncRawResource) -> None:
        self._raw = raw

        self.get = async_to_raw_response_wrapper(
            raw.get,
        )


class RawResourceWithStreamingResponse:
    def __init__(self, raw: RawResource) -> None:
        self._raw = raw

        self.get = to_streamed_response_wrapper(
            raw.get,
        )


class AsyncRawResourceWithStreamingResponse:
    def __init__(self, raw: AsyncRawResource) -> None:
        self._raw = raw

        self.get = async_to_streamed_response_wrapper(
            raw.get,
        )
