# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, cast

import httpx

from .dns import (
    DNS,
    AsyncDNS,
    DNSWithRawResponse,
    AsyncDNSWithRawResponse,
    DNSWithStreamingResponse,
    AsyncDNSWithStreamingResponse,
)
from .rules import (
    Rules,
    AsyncRules,
    RulesWithRawResponse,
    AsyncRulesWithRawResponse,
    RulesWithStreamingResponse,
    AsyncRulesWithStreamingResponse,
)
from .enables import (
    Enables,
    AsyncEnables,
    EnablesWithRawResponse,
    AsyncEnablesWithRawResponse,
    EnablesWithStreamingResponse,
    AsyncEnablesWithStreamingResponse,
)
from .disables import (
    Disables,
    AsyncDisables,
    DisablesWithRawResponse,
    AsyncDisablesWithRawResponse,
    DisablesWithStreamingResponse,
    AsyncDisablesWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .addresses import (
    Addresses,
    AsyncAddresses,
    AddressesWithRawResponse,
    AsyncAddressesWithRawResponse,
    AddressesWithStreamingResponse,
    AsyncAddressesWithStreamingResponse,
)
from ...._compat import cached_property
from .rules.rules import Rules, AsyncRules
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
from ....types.emails import RoutingEmailRoutingSettingsGetEmailRoutingSettingsResponse

__all__ = ["Routings", "AsyncRoutings"]


class Routings(SyncAPIResource):
    @cached_property
    def disables(self) -> Disables:
        return Disables(self._client)

    @cached_property
    def dns(self) -> DNS:
        return DNS(self._client)

    @cached_property
    def enables(self) -> Enables:
        return Enables(self._client)

    @cached_property
    def rules(self) -> Rules:
        return Rules(self._client)

    @cached_property
    def addresses(self) -> Addresses:
        return Addresses(self._client)

    @cached_property
    def with_raw_response(self) -> RoutingsWithRawResponse:
        return RoutingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoutingsWithStreamingResponse:
        return RoutingsWithStreamingResponse(self)

    def email_routing_settings_get_email_routing_settings(
        self,
        zone_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RoutingEmailRoutingSettingsGetEmailRoutingSettingsResponse:
        """
        Get information about the settings for your Email Routing zone.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._get(
            f"/zones/{zone_identifier}/email/routing",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[RoutingEmailRoutingSettingsGetEmailRoutingSettingsResponse],
                ResultWrapper[RoutingEmailRoutingSettingsGetEmailRoutingSettingsResponse],
            ),
        )


class AsyncRoutings(AsyncAPIResource):
    @cached_property
    def disables(self) -> AsyncDisables:
        return AsyncDisables(self._client)

    @cached_property
    def dns(self) -> AsyncDNS:
        return AsyncDNS(self._client)

    @cached_property
    def enables(self) -> AsyncEnables:
        return AsyncEnables(self._client)

    @cached_property
    def rules(self) -> AsyncRules:
        return AsyncRules(self._client)

    @cached_property
    def addresses(self) -> AsyncAddresses:
        return AsyncAddresses(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRoutingsWithRawResponse:
        return AsyncRoutingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoutingsWithStreamingResponse:
        return AsyncRoutingsWithStreamingResponse(self)

    async def email_routing_settings_get_email_routing_settings(
        self,
        zone_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RoutingEmailRoutingSettingsGetEmailRoutingSettingsResponse:
        """
        Get information about the settings for your Email Routing zone.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._get(
            f"/zones/{zone_identifier}/email/routing",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[RoutingEmailRoutingSettingsGetEmailRoutingSettingsResponse],
                ResultWrapper[RoutingEmailRoutingSettingsGetEmailRoutingSettingsResponse],
            ),
        )


class RoutingsWithRawResponse:
    def __init__(self, routings: Routings) -> None:
        self._routings = routings

        self.email_routing_settings_get_email_routing_settings = to_raw_response_wrapper(
            routings.email_routing_settings_get_email_routing_settings,
        )

    @cached_property
    def disables(self) -> DisablesWithRawResponse:
        return DisablesWithRawResponse(self._routings.disables)

    @cached_property
    def dns(self) -> DNSWithRawResponse:
        return DNSWithRawResponse(self._routings.dns)

    @cached_property
    def enables(self) -> EnablesWithRawResponse:
        return EnablesWithRawResponse(self._routings.enables)

    @cached_property
    def rules(self) -> RulesWithRawResponse:
        return RulesWithRawResponse(self._routings.rules)

    @cached_property
    def addresses(self) -> AddressesWithRawResponse:
        return AddressesWithRawResponse(self._routings.addresses)


class AsyncRoutingsWithRawResponse:
    def __init__(self, routings: AsyncRoutings) -> None:
        self._routings = routings

        self.email_routing_settings_get_email_routing_settings = async_to_raw_response_wrapper(
            routings.email_routing_settings_get_email_routing_settings,
        )

    @cached_property
    def disables(self) -> AsyncDisablesWithRawResponse:
        return AsyncDisablesWithRawResponse(self._routings.disables)

    @cached_property
    def dns(self) -> AsyncDNSWithRawResponse:
        return AsyncDNSWithRawResponse(self._routings.dns)

    @cached_property
    def enables(self) -> AsyncEnablesWithRawResponse:
        return AsyncEnablesWithRawResponse(self._routings.enables)

    @cached_property
    def rules(self) -> AsyncRulesWithRawResponse:
        return AsyncRulesWithRawResponse(self._routings.rules)

    @cached_property
    def addresses(self) -> AsyncAddressesWithRawResponse:
        return AsyncAddressesWithRawResponse(self._routings.addresses)


class RoutingsWithStreamingResponse:
    def __init__(self, routings: Routings) -> None:
        self._routings = routings

        self.email_routing_settings_get_email_routing_settings = to_streamed_response_wrapper(
            routings.email_routing_settings_get_email_routing_settings,
        )

    @cached_property
    def disables(self) -> DisablesWithStreamingResponse:
        return DisablesWithStreamingResponse(self._routings.disables)

    @cached_property
    def dns(self) -> DNSWithStreamingResponse:
        return DNSWithStreamingResponse(self._routings.dns)

    @cached_property
    def enables(self) -> EnablesWithStreamingResponse:
        return EnablesWithStreamingResponse(self._routings.enables)

    @cached_property
    def rules(self) -> RulesWithStreamingResponse:
        return RulesWithStreamingResponse(self._routings.rules)

    @cached_property
    def addresses(self) -> AddressesWithStreamingResponse:
        return AddressesWithStreamingResponse(self._routings.addresses)


class AsyncRoutingsWithStreamingResponse:
    def __init__(self, routings: AsyncRoutings) -> None:
        self._routings = routings

        self.email_routing_settings_get_email_routing_settings = async_to_streamed_response_wrapper(
            routings.email_routing_settings_get_email_routing_settings,
        )

    @cached_property
    def disables(self) -> AsyncDisablesWithStreamingResponse:
        return AsyncDisablesWithStreamingResponse(self._routings.disables)

    @cached_property
    def dns(self) -> AsyncDNSWithStreamingResponse:
        return AsyncDNSWithStreamingResponse(self._routings.dns)

    @cached_property
    def enables(self) -> AsyncEnablesWithStreamingResponse:
        return AsyncEnablesWithStreamingResponse(self._routings.enables)

    @cached_property
    def rules(self) -> AsyncRulesWithStreamingResponse:
        return AsyncRulesWithStreamingResponse(self._routings.rules)

    @cached_property
    def addresses(self) -> AsyncAddressesWithStreamingResponse:
        return AsyncAddressesWithStreamingResponse(self._routings.addresses)
