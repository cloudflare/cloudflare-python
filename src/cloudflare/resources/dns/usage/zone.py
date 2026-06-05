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
from ....types.dns.usage.zone_get_response import ZoneGetResponse

__all__ = ["ZoneResource", "AsyncZoneResource"]


class ZoneResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ZoneResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ZoneResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ZoneResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ZoneResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ZoneGetResponse]:
        """
        Get the current DNS record usage for a zone, including the number of records and
        the quota limit.

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            path_template("/zones/{zone_id}/dns_records/usage", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ZoneGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZoneGetResponse]], ResultWrapper[ZoneGetResponse]),
        )


class AsyncZoneResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncZoneResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncZoneResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncZoneResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncZoneResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ZoneGetResponse]:
        """
        Get the current DNS record usage for a zone, including the number of records and
        the quota limit.

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            path_template("/zones/{zone_id}/dns_records/usage", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ZoneGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZoneGetResponse]], ResultWrapper[ZoneGetResponse]),
        )


class ZoneResourceWithRawResponse:
    def __init__(self, zone: ZoneResource) -> None:
        self._zone = zone

        self.get = to_raw_response_wrapper(
            zone.get,
        )


class AsyncZoneResourceWithRawResponse:
    def __init__(self, zone: AsyncZoneResource) -> None:
        self._zone = zone

        self.get = async_to_raw_response_wrapper(
            zone.get,
        )


class ZoneResourceWithStreamingResponse:
    def __init__(self, zone: ZoneResource) -> None:
        self._zone = zone

        self.get = to_streamed_response_wrapper(
            zone.get,
        )


class AsyncZoneResourceWithStreamingResponse:
    def __init__(self, zone: AsyncZoneResource) -> None:
        self._zone = zone

        self.get = async_to_streamed_response_wrapper(
            zone.get,
        )
