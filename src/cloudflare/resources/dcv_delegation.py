# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._wrappers import ResultWrapper
from .._base_client import make_request_options
from ..types.dcv_delegation.dcv_delegation_uuid import DCVDelegationUUID

__all__ = ["DCVDelegationResource", "AsyncDCVDelegationResource"]


class DCVDelegationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DCVDelegationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DCVDelegationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DCVDelegationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DCVDelegationResourceWithStreamingResponse(self)

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
    ) -> Optional[DCVDelegationUUID]:
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
                post_parser=ResultWrapper[Optional[DCVDelegationUUID]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DCVDelegationUUID]], ResultWrapper[DCVDelegationUUID]),
        )


class AsyncDCVDelegationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDCVDelegationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDCVDelegationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDCVDelegationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDCVDelegationResourceWithStreamingResponse(self)

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
    ) -> Optional[DCVDelegationUUID]:
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
                post_parser=ResultWrapper[Optional[DCVDelegationUUID]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DCVDelegationUUID]], ResultWrapper[DCVDelegationUUID]),
        )


class DCVDelegationResourceWithRawResponse:
    def __init__(self, dcv_delegation: DCVDelegationResource) -> None:
        self._dcv_delegation = dcv_delegation

        self.get = to_raw_response_wrapper(
            dcv_delegation.get,
        )


class AsyncDCVDelegationResourceWithRawResponse:
    def __init__(self, dcv_delegation: AsyncDCVDelegationResource) -> None:
        self._dcv_delegation = dcv_delegation

        self.get = async_to_raw_response_wrapper(
            dcv_delegation.get,
        )


class DCVDelegationResourceWithStreamingResponse:
    def __init__(self, dcv_delegation: DCVDelegationResource) -> None:
        self._dcv_delegation = dcv_delegation

        self.get = to_streamed_response_wrapper(
            dcv_delegation.get,
        )


class AsyncDCVDelegationResourceWithStreamingResponse:
    def __init__(self, dcv_delegation: AsyncDCVDelegationResource) -> None:
        self._dcv_delegation = dcv_delegation

        self.get = async_to_streamed_response_wrapper(
            dcv_delegation.get,
        )
