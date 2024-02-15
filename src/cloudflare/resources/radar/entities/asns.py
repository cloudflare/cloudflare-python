# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
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
from ....types.radar.entities import AsnRelResponse, asn_rel_params

__all__ = ["Asns", "AsyncAsns"]


class Asns(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsnsWithRawResponse:
        return AsnsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsnsWithStreamingResponse:
        return AsnsWithStreamingResponse(self)

    def rel(
        self,
        asn: int,
        *,
        asn2: int | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsnRelResponse:
        """
        Get AS-level relationship for given networks.

        Args:
          asn: Get all ASNs with provider-customer or peering relationships with the given ASN

          asn2: Get the AS relationship of ASN2 with respect to the given ASN

          format: Format results are returned in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/radar/entities/asns/{asn}/rel",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asn2": asn2,
                        "format": format,
                    },
                    asn_rel_params.AsnRelParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AsnRelResponse], ResultWrapper[AsnRelResponse]),
        )


class AsyncAsns(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAsnsWithRawResponse:
        return AsyncAsnsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAsnsWithStreamingResponse:
        return AsyncAsnsWithStreamingResponse(self)

    async def rel(
        self,
        asn: int,
        *,
        asn2: int | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsnRelResponse:
        """
        Get AS-level relationship for given networks.

        Args:
          asn: Get all ASNs with provider-customer or peering relationships with the given ASN

          asn2: Get the AS relationship of ASN2 with respect to the given ASN

          format: Format results are returned in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/radar/entities/asns/{asn}/rel",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asn2": asn2,
                        "format": format,
                    },
                    asn_rel_params.AsnRelParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AsnRelResponse], ResultWrapper[AsnRelResponse]),
        )


class AsnsWithRawResponse:
    def __init__(self, asns: Asns) -> None:
        self._asns = asns

        self.rel = to_raw_response_wrapper(
            asns.rel,
        )


class AsyncAsnsWithRawResponse:
    def __init__(self, asns: AsyncAsns) -> None:
        self._asns = asns

        self.rel = async_to_raw_response_wrapper(
            asns.rel,
        )


class AsnsWithStreamingResponse:
    def __init__(self, asns: Asns) -> None:
        self._asns = asns

        self.rel = to_streamed_response_wrapper(
            asns.rel,
        )


class AsyncAsnsWithStreamingResponse:
    def __init__(self, asns: AsyncAsns) -> None:
        self._asns = asns

        self.rel = async_to_streamed_response_wrapper(
            asns.rel,
        )
