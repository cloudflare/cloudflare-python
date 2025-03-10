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
from ...._base_client import make_request_options
from ....types.dns.settings import zone_edit_params
from ....types.dns.settings.zone_get_response import ZoneGetResponse
from ....types.dns.settings.zone_edit_response import ZoneEditResponse

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

    def edit(
        self,
        *,
        zone_id: str,
        flatten_all_cnames: bool | NotGiven = NOT_GIVEN,
        foundation_dns: bool | NotGiven = NOT_GIVEN,
        internal_dns: zone_edit_params.InternalDNS | NotGiven = NOT_GIVEN,
        multi_provider: bool | NotGiven = NOT_GIVEN,
        nameservers: zone_edit_params.Nameservers | NotGiven = NOT_GIVEN,
        ns_ttl: float | NotGiven = NOT_GIVEN,
        secondary_overrides: bool | NotGiven = NOT_GIVEN,
        soa: zone_edit_params.SOA | NotGiven = NOT_GIVEN,
        zone_mode: Literal["standard", "cdn_only", "dns_only"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZoneEditResponse]:
        """
        Update DNS settings for a zone

        Args:
          zone_id: Identifier

          flatten_all_cnames: Whether to flatten all CNAME records in the zone. Note that, due to DNS
              limitations, a CNAME record at the zone apex will always be flattened.

          foundation_dns: Whether to enable Foundation DNS Advanced Nameservers on the zone.

          internal_dns: Settings for this internal zone.

          multi_provider: Whether to enable multi-provider DNS, which causes Cloudflare to activate the
              zone even when non-Cloudflare NS records exist, and to respect NS records at the
              zone apex during outbound zone transfers.

          nameservers: Settings determining the nameservers through which the zone should be available.

          ns_ttl: The time to live (TTL) of the zone's nameserver (NS) records.

          secondary_overrides: Allows a Secondary DNS zone to use (proxied) override records and CNAME
              flattening at the zone apex.

          soa: Components of the zone's SOA record.

          zone_mode: Whether the zone mode is a regular or CDN/DNS only zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/dns_settings",
            body=maybe_transform(
                {
                    "flatten_all_cnames": flatten_all_cnames,
                    "foundation_dns": foundation_dns,
                    "internal_dns": internal_dns,
                    "multi_provider": multi_provider,
                    "nameservers": nameservers,
                    "ns_ttl": ns_ttl,
                    "secondary_overrides": secondary_overrides,
                    "soa": soa,
                    "zone_mode": zone_mode,
                },
                zone_edit_params.ZoneEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ZoneEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZoneEditResponse]], ResultWrapper[ZoneEditResponse]),
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
    ) -> Optional[ZoneGetResponse]:
        """
        Show DNS settings for a zone

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
            f"/zones/{zone_id}/dns_settings",
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

    async def edit(
        self,
        *,
        zone_id: str,
        flatten_all_cnames: bool | NotGiven = NOT_GIVEN,
        foundation_dns: bool | NotGiven = NOT_GIVEN,
        internal_dns: zone_edit_params.InternalDNS | NotGiven = NOT_GIVEN,
        multi_provider: bool | NotGiven = NOT_GIVEN,
        nameservers: zone_edit_params.Nameservers | NotGiven = NOT_GIVEN,
        ns_ttl: float | NotGiven = NOT_GIVEN,
        secondary_overrides: bool | NotGiven = NOT_GIVEN,
        soa: zone_edit_params.SOA | NotGiven = NOT_GIVEN,
        zone_mode: Literal["standard", "cdn_only", "dns_only"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZoneEditResponse]:
        """
        Update DNS settings for a zone

        Args:
          zone_id: Identifier

          flatten_all_cnames: Whether to flatten all CNAME records in the zone. Note that, due to DNS
              limitations, a CNAME record at the zone apex will always be flattened.

          foundation_dns: Whether to enable Foundation DNS Advanced Nameservers on the zone.

          internal_dns: Settings for this internal zone.

          multi_provider: Whether to enable multi-provider DNS, which causes Cloudflare to activate the
              zone even when non-Cloudflare NS records exist, and to respect NS records at the
              zone apex during outbound zone transfers.

          nameservers: Settings determining the nameservers through which the zone should be available.

          ns_ttl: The time to live (TTL) of the zone's nameserver (NS) records.

          secondary_overrides: Allows a Secondary DNS zone to use (proxied) override records and CNAME
              flattening at the zone apex.

          soa: Components of the zone's SOA record.

          zone_mode: Whether the zone mode is a regular or CDN/DNS only zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/dns_settings",
            body=await async_maybe_transform(
                {
                    "flatten_all_cnames": flatten_all_cnames,
                    "foundation_dns": foundation_dns,
                    "internal_dns": internal_dns,
                    "multi_provider": multi_provider,
                    "nameservers": nameservers,
                    "ns_ttl": ns_ttl,
                    "secondary_overrides": secondary_overrides,
                    "soa": soa,
                    "zone_mode": zone_mode,
                },
                zone_edit_params.ZoneEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ZoneEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZoneEditResponse]], ResultWrapper[ZoneEditResponse]),
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
    ) -> Optional[ZoneGetResponse]:
        """
        Show DNS settings for a zone

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
            f"/zones/{zone_id}/dns_settings",
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

        self.edit = to_raw_response_wrapper(
            zone.edit,
        )
        self.get = to_raw_response_wrapper(
            zone.get,
        )


class AsyncZoneResourceWithRawResponse:
    def __init__(self, zone: AsyncZoneResource) -> None:
        self._zone = zone

        self.edit = async_to_raw_response_wrapper(
            zone.edit,
        )
        self.get = async_to_raw_response_wrapper(
            zone.get,
        )


class ZoneResourceWithStreamingResponse:
    def __init__(self, zone: ZoneResource) -> None:
        self._zone = zone

        self.edit = to_streamed_response_wrapper(
            zone.edit,
        )
        self.get = to_streamed_response_wrapper(
            zone.get,
        )


class AsyncZoneResourceWithStreamingResponse:
    def __init__(self, zone: AsyncZoneResource) -> None:
        self._zone = zone

        self.edit = async_to_streamed_response_wrapper(
            zone.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            zone.get,
        )
