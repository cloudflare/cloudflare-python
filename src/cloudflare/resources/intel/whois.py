# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...types.intel import IntelWhois, whois_get_params
from ..._base_client import (
    make_request_options,
)

__all__ = ["Whois", "AsyncWhois"]


class Whois(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WhoisWithRawResponse:
        return WhoisWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WhoisWithStreamingResponse:
        return WhoisWithStreamingResponse(self)

    def get(
        self,
        *,
        account_id: str,
        domain: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IntelWhois:
        """
        Get WHOIS Record

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/intel/whois",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"domain": domain}, whois_get_params.WhoisGetParams),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IntelWhois], ResultWrapper[IntelWhois]),
        )


class AsyncWhois(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWhoisWithRawResponse:
        return AsyncWhoisWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWhoisWithStreamingResponse:
        return AsyncWhoisWithStreamingResponse(self)

    async def get(
        self,
        *,
        account_id: str,
        domain: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IntelWhois:
        """
        Get WHOIS Record

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/intel/whois",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"domain": domain}, whois_get_params.WhoisGetParams),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IntelWhois], ResultWrapper[IntelWhois]),
        )


class WhoisWithRawResponse:
    def __init__(self, whois: Whois) -> None:
        self._whois = whois

        self.get = to_raw_response_wrapper(
            whois.get,
        )


class AsyncWhoisWithRawResponse:
    def __init__(self, whois: AsyncWhois) -> None:
        self._whois = whois

        self.get = async_to_raw_response_wrapper(
            whois.get,
        )


class WhoisWithStreamingResponse:
    def __init__(self, whois: Whois) -> None:
        self._whois = whois

        self.get = to_streamed_response_wrapper(
            whois.get,
        )


class AsyncWhoisWithStreamingResponse:
    def __init__(self, whois: AsyncWhois) -> None:
        self._whois = whois

        self.get = async_to_streamed_response_wrapper(
            whois.get,
        )
