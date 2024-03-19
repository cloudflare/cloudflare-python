# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

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
from ...._base_client import (
    make_request_options,
)
from ....types.zones.settings import ZonesIPGeolocation, ip_geolocation_edit_params

__all__ = ["IPGeolocation", "AsyncIPGeolocation"]


class IPGeolocation(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IPGeolocationWithRawResponse:
        return IPGeolocationWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IPGeolocationWithStreamingResponse:
        return IPGeolocationWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZonesIPGeolocation]:
        """
        Enable IP Geolocation to have Cloudflare geolocate visitors to your website and
        pass the country code to you.
        (https://support.cloudflare.com/hc/en-us/articles/200168236).

        Args:
          zone_id: Identifier

          value: Value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/ip_geolocation",
            body=maybe_transform({"value": value}, ip_geolocation_edit_params.IPGeolocationEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesIPGeolocation]], ResultWrapper[ZonesIPGeolocation]),
        )

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
    ) -> Optional[ZonesIPGeolocation]:
        """
        Enable IP Geolocation to have Cloudflare geolocate visitors to your website and
        pass the country code to you.
        (https://support.cloudflare.com/hc/en-us/articles/200168236).

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
            f"/zones/{zone_id}/settings/ip_geolocation",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesIPGeolocation]], ResultWrapper[ZonesIPGeolocation]),
        )


class AsyncIPGeolocation(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIPGeolocationWithRawResponse:
        return AsyncIPGeolocationWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIPGeolocationWithStreamingResponse:
        return AsyncIPGeolocationWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZonesIPGeolocation]:
        """
        Enable IP Geolocation to have Cloudflare geolocate visitors to your website and
        pass the country code to you.
        (https://support.cloudflare.com/hc/en-us/articles/200168236).

        Args:
          zone_id: Identifier

          value: Value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/ip_geolocation",
            body=await async_maybe_transform({"value": value}, ip_geolocation_edit_params.IPGeolocationEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesIPGeolocation]], ResultWrapper[ZonesIPGeolocation]),
        )

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
    ) -> Optional[ZonesIPGeolocation]:
        """
        Enable IP Geolocation to have Cloudflare geolocate visitors to your website and
        pass the country code to you.
        (https://support.cloudflare.com/hc/en-us/articles/200168236).

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
            f"/zones/{zone_id}/settings/ip_geolocation",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesIPGeolocation]], ResultWrapper[ZonesIPGeolocation]),
        )


class IPGeolocationWithRawResponse:
    def __init__(self, ip_geolocation: IPGeolocation) -> None:
        self._ip_geolocation = ip_geolocation

        self.edit = to_raw_response_wrapper(
            ip_geolocation.edit,
        )
        self.get = to_raw_response_wrapper(
            ip_geolocation.get,
        )


class AsyncIPGeolocationWithRawResponse:
    def __init__(self, ip_geolocation: AsyncIPGeolocation) -> None:
        self._ip_geolocation = ip_geolocation

        self.edit = async_to_raw_response_wrapper(
            ip_geolocation.edit,
        )
        self.get = async_to_raw_response_wrapper(
            ip_geolocation.get,
        )


class IPGeolocationWithStreamingResponse:
    def __init__(self, ip_geolocation: IPGeolocation) -> None:
        self._ip_geolocation = ip_geolocation

        self.edit = to_streamed_response_wrapper(
            ip_geolocation.edit,
        )
        self.get = to_streamed_response_wrapper(
            ip_geolocation.get,
        )


class AsyncIPGeolocationWithStreamingResponse:
    def __init__(self, ip_geolocation: AsyncIPGeolocation) -> None:
        self._ip_geolocation = ip_geolocation

        self.edit = async_to_streamed_response_wrapper(
            ip_geolocation.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            ip_geolocation.get,
        )
