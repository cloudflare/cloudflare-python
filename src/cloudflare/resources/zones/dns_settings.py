# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...types.zones import dns_setting_edit_params
from ..._base_client import (
    make_request_options,
)
from ...types.zones.dns_setting import DNSSetting
from ...types.zones.nameserver_param import NameserverParam

__all__ = ["DNSSettingsResource", "AsyncDNSSettingsResource"]


class DNSSettingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DNSSettingsResourceWithRawResponse:
        return DNSSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DNSSettingsResourceWithStreamingResponse:
        return DNSSettingsResourceWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        foundation_dns: bool | NotGiven = NOT_GIVEN,
        multi_provider: bool | NotGiven = NOT_GIVEN,
        nameservers: NameserverParam | NotGiven = NOT_GIVEN,
        secondary_overrides: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DNSSetting]:
        """
        Update DNS settings for a zone

        Args:
          zone_id: Identifier

          foundation_dns: Whether to enable Foundation DNS Advanced Nameservers on the zone.

          multi_provider: Whether to enable multi-provider DNS, which causes Cloudflare to activate the
              zone even when non-Cloudflare NS records exist, and to respect NS records at the
              zone apex during outbound zone transfers.

          nameservers: Settings determining the nameservers through which the zone should be available.

          secondary_overrides: Allows a Secondary DNS zone to use (proxied) override records and CNAME
              flattening at the zone apex.

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
                    "foundation_dns": foundation_dns,
                    "multi_provider": multi_provider,
                    "nameservers": nameservers,
                    "secondary_overrides": secondary_overrides,
                },
                dns_setting_edit_params.DNSSettingEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DNSSetting]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DNSSetting]], ResultWrapper[DNSSetting]),
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
    ) -> Optional[DNSSetting]:
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
                post_parser=ResultWrapper[Optional[DNSSetting]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DNSSetting]], ResultWrapper[DNSSetting]),
        )


class AsyncDNSSettingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDNSSettingsResourceWithRawResponse:
        return AsyncDNSSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDNSSettingsResourceWithStreamingResponse:
        return AsyncDNSSettingsResourceWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        foundation_dns: bool | NotGiven = NOT_GIVEN,
        multi_provider: bool | NotGiven = NOT_GIVEN,
        nameservers: NameserverParam | NotGiven = NOT_GIVEN,
        secondary_overrides: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DNSSetting]:
        """
        Update DNS settings for a zone

        Args:
          zone_id: Identifier

          foundation_dns: Whether to enable Foundation DNS Advanced Nameservers on the zone.

          multi_provider: Whether to enable multi-provider DNS, which causes Cloudflare to activate the
              zone even when non-Cloudflare NS records exist, and to respect NS records at the
              zone apex during outbound zone transfers.

          nameservers: Settings determining the nameservers through which the zone should be available.

          secondary_overrides: Allows a Secondary DNS zone to use (proxied) override records and CNAME
              flattening at the zone apex.

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
                    "foundation_dns": foundation_dns,
                    "multi_provider": multi_provider,
                    "nameservers": nameservers,
                    "secondary_overrides": secondary_overrides,
                },
                dns_setting_edit_params.DNSSettingEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DNSSetting]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DNSSetting]], ResultWrapper[DNSSetting]),
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
    ) -> Optional[DNSSetting]:
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
                post_parser=ResultWrapper[Optional[DNSSetting]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DNSSetting]], ResultWrapper[DNSSetting]),
        )


class DNSSettingsResourceWithRawResponse:
    def __init__(self, dns_settings: DNSSettingsResource) -> None:
        self._dns_settings = dns_settings

        self.edit = to_raw_response_wrapper(
            dns_settings.edit,
        )
        self.get = to_raw_response_wrapper(
            dns_settings.get,
        )


class AsyncDNSSettingsResourceWithRawResponse:
    def __init__(self, dns_settings: AsyncDNSSettingsResource) -> None:
        self._dns_settings = dns_settings

        self.edit = async_to_raw_response_wrapper(
            dns_settings.edit,
        )
        self.get = async_to_raw_response_wrapper(
            dns_settings.get,
        )


class DNSSettingsResourceWithStreamingResponse:
    def __init__(self, dns_settings: DNSSettingsResource) -> None:
        self._dns_settings = dns_settings

        self.edit = to_streamed_response_wrapper(
            dns_settings.edit,
        )
        self.get = to_streamed_response_wrapper(
            dns_settings.get,
        )


class AsyncDNSSettingsResourceWithStreamingResponse:
    def __init__(self, dns_settings: AsyncDNSSettingsResource) -> None:
        self._dns_settings = dns_settings

        self.edit = async_to_streamed_response_wrapper(
            dns_settings.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            dns_settings.get,
        )
