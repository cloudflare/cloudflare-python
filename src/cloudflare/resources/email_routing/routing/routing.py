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
from ....types.email_routing import RoutingGetResponse, RoutingEnableResponse, RoutingDisableResponse

__all__ = ["Routing", "AsyncRouting"]


class Routing(SyncAPIResource):
    @cached_property
    def dns(self) -> DNS:
        return DNS(self._client)

    @cached_property
    def rules(self) -> Rules:
        return Rules(self._client)

    @cached_property
    def addresses(self) -> Addresses:
        return Addresses(self._client)

    @cached_property
    def with_raw_response(self) -> RoutingWithRawResponse:
        return RoutingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoutingWithStreamingResponse:
        return RoutingWithStreamingResponse(self)

    def disable(
        self,
        zone_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RoutingDisableResponse:
        """Disable your Email Routing zone.

        Also removes additional MX records previously
        required for Email Routing to work.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._post(
            f"/zones/{zone_identifier}/email/routing/disable",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RoutingDisableResponse], ResultWrapper[RoutingDisableResponse]),
        )

    def enable(
        self,
        zone_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RoutingEnableResponse:
        """Enable you Email Routing zone.

        Add and lock the necessary MX and SPF records.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._post(
            f"/zones/{zone_identifier}/email/routing/enable",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RoutingEnableResponse], ResultWrapper[RoutingEnableResponse]),
        )

    def get(
        self,
        zone_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RoutingGetResponse:
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
            cast_to=cast(Type[RoutingGetResponse], ResultWrapper[RoutingGetResponse]),
        )


class AsyncRouting(AsyncAPIResource):
    @cached_property
    def dns(self) -> AsyncDNS:
        return AsyncDNS(self._client)

    @cached_property
    def rules(self) -> AsyncRules:
        return AsyncRules(self._client)

    @cached_property
    def addresses(self) -> AsyncAddresses:
        return AsyncAddresses(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRoutingWithRawResponse:
        return AsyncRoutingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoutingWithStreamingResponse:
        return AsyncRoutingWithStreamingResponse(self)

    async def disable(
        self,
        zone_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RoutingDisableResponse:
        """Disable your Email Routing zone.

        Also removes additional MX records previously
        required for Email Routing to work.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._post(
            f"/zones/{zone_identifier}/email/routing/disable",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RoutingDisableResponse], ResultWrapper[RoutingDisableResponse]),
        )

    async def enable(
        self,
        zone_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RoutingEnableResponse:
        """Enable you Email Routing zone.

        Add and lock the necessary MX and SPF records.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._post(
            f"/zones/{zone_identifier}/email/routing/enable",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RoutingEnableResponse], ResultWrapper[RoutingEnableResponse]),
        )

    async def get(
        self,
        zone_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RoutingGetResponse:
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
            cast_to=cast(Type[RoutingGetResponse], ResultWrapper[RoutingGetResponse]),
        )


class RoutingWithRawResponse:
    def __init__(self, routing: Routing) -> None:
        self._routing = routing

        self.disable = to_raw_response_wrapper(
            routing.disable,
        )
        self.enable = to_raw_response_wrapper(
            routing.enable,
        )
        self.get = to_raw_response_wrapper(
            routing.get,
        )

    @cached_property
    def dns(self) -> DNSWithRawResponse:
        return DNSWithRawResponse(self._routing.dns)

    @cached_property
    def rules(self) -> RulesWithRawResponse:
        return RulesWithRawResponse(self._routing.rules)

    @cached_property
    def addresses(self) -> AddressesWithRawResponse:
        return AddressesWithRawResponse(self._routing.addresses)


class AsyncRoutingWithRawResponse:
    def __init__(self, routing: AsyncRouting) -> None:
        self._routing = routing

        self.disable = async_to_raw_response_wrapper(
            routing.disable,
        )
        self.enable = async_to_raw_response_wrapper(
            routing.enable,
        )
        self.get = async_to_raw_response_wrapper(
            routing.get,
        )

    @cached_property
    def dns(self) -> AsyncDNSWithRawResponse:
        return AsyncDNSWithRawResponse(self._routing.dns)

    @cached_property
    def rules(self) -> AsyncRulesWithRawResponse:
        return AsyncRulesWithRawResponse(self._routing.rules)

    @cached_property
    def addresses(self) -> AsyncAddressesWithRawResponse:
        return AsyncAddressesWithRawResponse(self._routing.addresses)


class RoutingWithStreamingResponse:
    def __init__(self, routing: Routing) -> None:
        self._routing = routing

        self.disable = to_streamed_response_wrapper(
            routing.disable,
        )
        self.enable = to_streamed_response_wrapper(
            routing.enable,
        )
        self.get = to_streamed_response_wrapper(
            routing.get,
        )

    @cached_property
    def dns(self) -> DNSWithStreamingResponse:
        return DNSWithStreamingResponse(self._routing.dns)

    @cached_property
    def rules(self) -> RulesWithStreamingResponse:
        return RulesWithStreamingResponse(self._routing.rules)

    @cached_property
    def addresses(self) -> AddressesWithStreamingResponse:
        return AddressesWithStreamingResponse(self._routing.addresses)


class AsyncRoutingWithStreamingResponse:
    def __init__(self, routing: AsyncRouting) -> None:
        self._routing = routing

        self.disable = async_to_streamed_response_wrapper(
            routing.disable,
        )
        self.enable = async_to_streamed_response_wrapper(
            routing.enable,
        )
        self.get = async_to_streamed_response_wrapper(
            routing.get,
        )

    @cached_property
    def dns(self) -> AsyncDNSWithStreamingResponse:
        return AsyncDNSWithStreamingResponse(self._routing.dns)

    @cached_property
    def rules(self) -> AsyncRulesWithStreamingResponse:
        return AsyncRulesWithStreamingResponse(self._routing.rules)

    @cached_property
    def addresses(self) -> AsyncAddressesWithStreamingResponse:
        return AsyncAddressesWithStreamingResponse(self._routing.addresses)
