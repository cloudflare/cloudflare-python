# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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
from ...types import EmailRoutingGetResponse, EmailRoutingEnableResponse, EmailRoutingDisableResponse
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from .addresses import (
    Addresses,
    AsyncAddresses,
    AddressesWithRawResponse,
    AsyncAddressesWithRawResponse,
    AddressesWithStreamingResponse,
    AsyncAddressesWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from .rules.rules import Rules, AsyncRules
from ..._base_client import (
    make_request_options,
)

__all__ = ["EmailRouting", "AsyncEmailRouting"]


class EmailRouting(SyncAPIResource):
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
    def with_raw_response(self) -> EmailRoutingWithRawResponse:
        return EmailRoutingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailRoutingWithStreamingResponse:
        return EmailRoutingWithStreamingResponse(self)

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
    ) -> EmailRoutingDisableResponse:
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
            cast_to=cast(Type[EmailRoutingDisableResponse], ResultWrapper[EmailRoutingDisableResponse]),
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
    ) -> EmailRoutingEnableResponse:
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
            cast_to=cast(Type[EmailRoutingEnableResponse], ResultWrapper[EmailRoutingEnableResponse]),
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
    ) -> EmailRoutingGetResponse:
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
            cast_to=cast(Type[EmailRoutingGetResponse], ResultWrapper[EmailRoutingGetResponse]),
        )


class AsyncEmailRouting(AsyncAPIResource):
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
    def with_raw_response(self) -> AsyncEmailRoutingWithRawResponse:
        return AsyncEmailRoutingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailRoutingWithStreamingResponse:
        return AsyncEmailRoutingWithStreamingResponse(self)

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
    ) -> EmailRoutingDisableResponse:
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
            cast_to=cast(Type[EmailRoutingDisableResponse], ResultWrapper[EmailRoutingDisableResponse]),
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
    ) -> EmailRoutingEnableResponse:
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
            cast_to=cast(Type[EmailRoutingEnableResponse], ResultWrapper[EmailRoutingEnableResponse]),
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
    ) -> EmailRoutingGetResponse:
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
            cast_to=cast(Type[EmailRoutingGetResponse], ResultWrapper[EmailRoutingGetResponse]),
        )


class EmailRoutingWithRawResponse:
    def __init__(self, email_routing: EmailRouting) -> None:
        self._email_routing = email_routing

        self.disable = to_raw_response_wrapper(
            email_routing.disable,
        )
        self.enable = to_raw_response_wrapper(
            email_routing.enable,
        )
        self.get = to_raw_response_wrapper(
            email_routing.get,
        )

    @cached_property
    def dns(self) -> DNSWithRawResponse:
        return DNSWithRawResponse(self._email_routing.dns)

    @cached_property
    def rules(self) -> RulesWithRawResponse:
        return RulesWithRawResponse(self._email_routing.rules)

    @cached_property
    def addresses(self) -> AddressesWithRawResponse:
        return AddressesWithRawResponse(self._email_routing.addresses)


class AsyncEmailRoutingWithRawResponse:
    def __init__(self, email_routing: AsyncEmailRouting) -> None:
        self._email_routing = email_routing

        self.disable = async_to_raw_response_wrapper(
            email_routing.disable,
        )
        self.enable = async_to_raw_response_wrapper(
            email_routing.enable,
        )
        self.get = async_to_raw_response_wrapper(
            email_routing.get,
        )

    @cached_property
    def dns(self) -> AsyncDNSWithRawResponse:
        return AsyncDNSWithRawResponse(self._email_routing.dns)

    @cached_property
    def rules(self) -> AsyncRulesWithRawResponse:
        return AsyncRulesWithRawResponse(self._email_routing.rules)

    @cached_property
    def addresses(self) -> AsyncAddressesWithRawResponse:
        return AsyncAddressesWithRawResponse(self._email_routing.addresses)


class EmailRoutingWithStreamingResponse:
    def __init__(self, email_routing: EmailRouting) -> None:
        self._email_routing = email_routing

        self.disable = to_streamed_response_wrapper(
            email_routing.disable,
        )
        self.enable = to_streamed_response_wrapper(
            email_routing.enable,
        )
        self.get = to_streamed_response_wrapper(
            email_routing.get,
        )

    @cached_property
    def dns(self) -> DNSWithStreamingResponse:
        return DNSWithStreamingResponse(self._email_routing.dns)

    @cached_property
    def rules(self) -> RulesWithStreamingResponse:
        return RulesWithStreamingResponse(self._email_routing.rules)

    @cached_property
    def addresses(self) -> AddressesWithStreamingResponse:
        return AddressesWithStreamingResponse(self._email_routing.addresses)


class AsyncEmailRoutingWithStreamingResponse:
    def __init__(self, email_routing: AsyncEmailRouting) -> None:
        self._email_routing = email_routing

        self.disable = async_to_streamed_response_wrapper(
            email_routing.disable,
        )
        self.enable = async_to_streamed_response_wrapper(
            email_routing.enable,
        )
        self.get = async_to_streamed_response_wrapper(
            email_routing.get,
        )

    @cached_property
    def dns(self) -> AsyncDNSWithStreamingResponse:
        return AsyncDNSWithStreamingResponse(self._email_routing.dns)

    @cached_property
    def rules(self) -> AsyncRulesWithStreamingResponse:
        return AsyncRulesWithStreamingResponse(self._email_routing.rules)

    @cached_property
    def addresses(self) -> AsyncAddressesWithStreamingResponse:
        return AsyncAddressesWithStreamingResponse(self._email_routing.addresses)
