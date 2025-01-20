# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from .subnets import (
    SubnetsResource,
    AsyncSubnetsResource,
    SubnetsResourceWithRawResponse,
    AsyncSubnetsResourceWithRawResponse,
    SubnetsResourceWithStreamingResponse,
    AsyncSubnetsResourceWithStreamingResponse,
)
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
from ....types.shared.asn import ASN

__all__ = ["ASNResource", "AsyncASNResource"]


class ASNResource(SyncAPIResource):
    @cached_property
    def subnets(self) -> SubnetsResource:
        return SubnetsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ASNResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ASNResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ASNResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ASNResourceWithStreamingResponse(self)

    def get(
        self,
        asn: ASN,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ASN]:
        """
        Gets an overview of the Autonomous System Number (ASN) and a list of subnets for
        it.

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
            f"/accounts/{account_id}/intel/asn/{asn}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ASN]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ASN]], ResultWrapper[int]),
        )


class AsyncASNResource(AsyncAPIResource):
    @cached_property
    def subnets(self) -> AsyncSubnetsResource:
        return AsyncSubnetsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncASNResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncASNResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncASNResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncASNResourceWithStreamingResponse(self)

    async def get(
        self,
        asn: ASN,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ASN]:
        """
        Gets an overview of the Autonomous System Number (ASN) and a list of subnets for
        it.

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
            f"/accounts/{account_id}/intel/asn/{asn}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ASN]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ASN]], ResultWrapper[int]),
        )


class ASNResourceWithRawResponse:
    def __init__(self, asn: ASNResource) -> None:
        self._asn = asn

        self.get = to_raw_response_wrapper(
            asn.get,
        )

    @cached_property
    def subnets(self) -> SubnetsResourceWithRawResponse:
        return SubnetsResourceWithRawResponse(self._asn.subnets)


class AsyncASNResourceWithRawResponse:
    def __init__(self, asn: AsyncASNResource) -> None:
        self._asn = asn

        self.get = async_to_raw_response_wrapper(
            asn.get,
        )

    @cached_property
    def subnets(self) -> AsyncSubnetsResourceWithRawResponse:
        return AsyncSubnetsResourceWithRawResponse(self._asn.subnets)


class ASNResourceWithStreamingResponse:
    def __init__(self, asn: ASNResource) -> None:
        self._asn = asn

        self.get = to_streamed_response_wrapper(
            asn.get,
        )

    @cached_property
    def subnets(self) -> SubnetsResourceWithStreamingResponse:
        return SubnetsResourceWithStreamingResponse(self._asn.subnets)


class AsyncASNResourceWithStreamingResponse:
    def __init__(self, asn: AsyncASNResource) -> None:
        self._asn = asn

        self.get = async_to_streamed_response_wrapper(
            asn.get,
        )

    @cached_property
    def subnets(self) -> AsyncSubnetsResourceWithStreamingResponse:
        return AsyncSubnetsResourceWithStreamingResponse(self._asn.subnets)
