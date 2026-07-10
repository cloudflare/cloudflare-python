# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import path_template
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
from ....types.dns.usage.account_get_response import AccountGetResponse

__all__ = ["AccountResource", "AsyncAccountResource"]


class AccountResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AccountResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AccountResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[AccountGetResponse]:
        """Get the current DNS record usage and quota for an account.

        May include internal
        DNS usage and quota.

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/dns_records/usage", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AccountGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AccountGetResponse]], ResultWrapper[AccountGetResponse]),
        )


class AsyncAccountResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAccountResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[AccountGetResponse]:
        """Get the current DNS record usage and quota for an account.

        May include internal
        DNS usage and quota.

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/dns_records/usage", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AccountGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AccountGetResponse]], ResultWrapper[AccountGetResponse]),
        )


class AccountResourceWithRawResponse:
    def __init__(self, account: AccountResource) -> None:
        self._account = account

        self.get = to_raw_response_wrapper(
            account.get,
        )


class AsyncAccountResourceWithRawResponse:
    def __init__(self, account: AsyncAccountResource) -> None:
        self._account = account

        self.get = async_to_raw_response_wrapper(
            account.get,
        )


class AccountResourceWithStreamingResponse:
    def __init__(self, account: AccountResource) -> None:
        self._account = account

        self.get = to_streamed_response_wrapper(
            account.get,
        )


class AsyncAccountResourceWithStreamingResponse:
    def __init__(self, account: AsyncAccountResource) -> None:
        self._account = account

        self.get = async_to_streamed_response_wrapper(
            account.get,
        )
