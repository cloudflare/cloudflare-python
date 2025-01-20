# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...._base_client import make_request_options
from ....types.shared.asn import ASN
from ....types.intel.asn.subnet_get_response import SubnetGetResponse

__all__ = ["SubnetsResource", "AsyncSubnetsResource"]


class SubnetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubnetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SubnetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubnetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SubnetsResourceWithStreamingResponse(self)

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
    ) -> SubnetGetResponse:
        """
        Get ASN Subnets

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
            f"/accounts/{account_id}/intel/asn/{asn}/subnets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubnetGetResponse,
        )


class AsyncSubnetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubnetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubnetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubnetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSubnetsResourceWithStreamingResponse(self)

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
    ) -> SubnetGetResponse:
        """
        Get ASN Subnets

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
            f"/accounts/{account_id}/intel/asn/{asn}/subnets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubnetGetResponse,
        )


class SubnetsResourceWithRawResponse:
    def __init__(self, subnets: SubnetsResource) -> None:
        self._subnets = subnets

        self.get = to_raw_response_wrapper(
            subnets.get,
        )


class AsyncSubnetsResourceWithRawResponse:
    def __init__(self, subnets: AsyncSubnetsResource) -> None:
        self._subnets = subnets

        self.get = async_to_raw_response_wrapper(
            subnets.get,
        )


class SubnetsResourceWithStreamingResponse:
    def __init__(self, subnets: SubnetsResource) -> None:
        self._subnets = subnets

        self.get = to_streamed_response_wrapper(
            subnets.get,
        )


class AsyncSubnetsResourceWithStreamingResponse:
    def __init__(self, subnets: AsyncSubnetsResource) -> None:
        self._subnets = subnets

        self.get = async_to_streamed_response_wrapper(
            subnets.get,
        )
