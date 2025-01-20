# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

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
from ....types.dns.zone_transfers import force_axfr_create_params
from ....types.dns.zone_transfers.force_axfr import ForceAXFR

__all__ = ["ForceAXFRResource", "AsyncForceAXFRResource"]


class ForceAXFRResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ForceAXFRResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ForceAXFRResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ForceAXFRResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ForceAXFRResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Sends AXFR zone transfer request to primary nameserver(s).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/secondary_dns/force_axfr",
            body=maybe_transform(body, force_axfr_create_params.ForceAXFRCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ForceAXFR]]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )


class AsyncForceAXFRResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncForceAXFRResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncForceAXFRResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncForceAXFRResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncForceAXFRResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Sends AXFR zone transfer request to primary nameserver(s).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/secondary_dns/force_axfr",
            body=await async_maybe_transform(body, force_axfr_create_params.ForceAXFRCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ForceAXFR]]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )


class ForceAXFRResourceWithRawResponse:
    def __init__(self, force_axfr: ForceAXFRResource) -> None:
        self._force_axfr = force_axfr

        self.create = to_raw_response_wrapper(
            force_axfr.create,
        )


class AsyncForceAXFRResourceWithRawResponse:
    def __init__(self, force_axfr: AsyncForceAXFRResource) -> None:
        self._force_axfr = force_axfr

        self.create = async_to_raw_response_wrapper(
            force_axfr.create,
        )


class ForceAXFRResourceWithStreamingResponse:
    def __init__(self, force_axfr: ForceAXFRResource) -> None:
        self._force_axfr = force_axfr

        self.create = to_streamed_response_wrapper(
            force_axfr.create,
        )


class AsyncForceAXFRResourceWithStreamingResponse:
    def __init__(self, force_axfr: AsyncForceAXFRResource) -> None:
        self._force_axfr = force_axfr

        self.create = async_to_streamed_response_wrapper(
            force_axfr.create,
        )
