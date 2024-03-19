# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import (
    make_request_options,
)
from ...types.dcv_delegation import TLSCertificatesAndHostnamesUUIDObject

__all__ = ["UUID", "AsyncUUID"]


class UUID(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UUIDWithRawResponse:
        return UUIDWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UUIDWithStreamingResponse:
        return UUIDWithStreamingResponse(self)

    def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TLSCertificatesAndHostnamesUUIDObject:
        """
        Retrieve the account and zone specific unique identifier used as part of the
        CNAME target for DCV Delegation.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/dcv_delegation/uuid",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[TLSCertificatesAndHostnamesUUIDObject], ResultWrapper[TLSCertificatesAndHostnamesUUIDObject]
            ),
        )


class AsyncUUID(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUUIDWithRawResponse:
        return AsyncUUIDWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUUIDWithStreamingResponse:
        return AsyncUUIDWithStreamingResponse(self)

    async def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TLSCertificatesAndHostnamesUUIDObject:
        """
        Retrieve the account and zone specific unique identifier used as part of the
        CNAME target for DCV Delegation.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/dcv_delegation/uuid",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[TLSCertificatesAndHostnamesUUIDObject], ResultWrapper[TLSCertificatesAndHostnamesUUIDObject]
            ),
        )


class UUIDWithRawResponse:
    def __init__(self, uuid: UUID) -> None:
        self._uuid = uuid

        self.get = to_raw_response_wrapper(
            uuid.get,
        )


class AsyncUUIDWithRawResponse:
    def __init__(self, uuid: AsyncUUID) -> None:
        self._uuid = uuid

        self.get = async_to_raw_response_wrapper(
            uuid.get,
        )


class UUIDWithStreamingResponse:
    def __init__(self, uuid: UUID) -> None:
        self._uuid = uuid

        self.get = to_streamed_response_wrapper(
            uuid.get,
        )


class AsyncUUIDWithStreamingResponse:
    def __init__(self, uuid: AsyncUUID) -> None:
        self._uuid = uuid

        self.get = async_to_streamed_response_wrapper(
            uuid.get,
        )
