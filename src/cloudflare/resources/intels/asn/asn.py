# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, cast

import httpx

from .subnets import (
    Subnets,
    AsyncSubnets,
    SubnetsWithRawResponse,
    AsyncSubnetsWithRawResponse,
    SubnetsWithStreamingResponse,
    AsyncSubnetsWithStreamingResponse,
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
from ...._base_client import (
    make_request_options,
)
from ....types.intels import AsnGetResponse

__all__ = ["Asn", "AsyncAsn"]


class Asn(SyncAPIResource):
    @cached_property
    def subnets(self) -> Subnets:
        return Subnets(self._client)

    @cached_property
    def with_raw_response(self) -> AsnWithRawResponse:
        return AsnWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsnWithStreamingResponse:
        return AsnWithStreamingResponse(self)

    def get(
        self,
        asn: int,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsnGetResponse:
        """
        Get ASN Overview

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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AsnGetResponse], ResultWrapper[AsnGetResponse]),
        )


class AsyncAsn(AsyncAPIResource):
    @cached_property
    def subnets(self) -> AsyncSubnets:
        return AsyncSubnets(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAsnWithRawResponse:
        return AsyncAsnWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAsnWithStreamingResponse:
        return AsyncAsnWithStreamingResponse(self)

    async def get(
        self,
        asn: int,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsnGetResponse:
        """
        Get ASN Overview

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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AsnGetResponse], ResultWrapper[AsnGetResponse]),
        )


class AsnWithRawResponse:
    def __init__(self, asn: Asn) -> None:
        self._asn = asn

        self.get = to_raw_response_wrapper(
            asn.get,
        )

    @cached_property
    def subnets(self) -> SubnetsWithRawResponse:
        return SubnetsWithRawResponse(self._asn.subnets)


class AsyncAsnWithRawResponse:
    def __init__(self, asn: AsyncAsn) -> None:
        self._asn = asn

        self.get = async_to_raw_response_wrapper(
            asn.get,
        )

    @cached_property
    def subnets(self) -> AsyncSubnetsWithRawResponse:
        return AsyncSubnetsWithRawResponse(self._asn.subnets)


class AsnWithStreamingResponse:
    def __init__(self, asn: Asn) -> None:
        self._asn = asn

        self.get = to_streamed_response_wrapper(
            asn.get,
        )

    @cached_property
    def subnets(self) -> SubnetsWithStreamingResponse:
        return SubnetsWithStreamingResponse(self._asn.subnets)


class AsyncAsnWithStreamingResponse:
    def __init__(self, asn: AsyncAsn) -> None:
        self._asn = asn

        self.get = async_to_streamed_response_wrapper(
            asn.get,
        )

    @cached_property
    def subnets(self) -> AsyncSubnetsWithStreamingResponse:
        return AsyncSubnetsWithStreamingResponse(self._asn.subnets)
